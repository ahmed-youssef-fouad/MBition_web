import unittest.mock
import requests
import coverage

cov = coverage.Coverage()
cov.start()

def fetchUsers(page):
    response = requests.get(f'https://reqres.in/api/users?page={page}')
    data = response.json()
    return data['data']

def renderUsers(users):
    table_html = """
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>Name</th>
          <th>Email</th>
          <th>Avatar</th>
        </tr>
      </thead>
      <tbody>
    """
    for user in users:
        table_html += f"""
        <tr>
          <td>{user['id']}</td>
          <td>{user['first_name']} {user['last_name']}</td>
          <td>{user['email']}</td>
          <td><img src="{user['avatar']}" alt="Avatar" width="200"></td>
        </tr>
        """
    table_html += """
      </tbody>
    </table>
    """
    return table_html

def UserRendering():
    users = []
    totalPages = 1
    page = 1

    while page <= totalPages:
        currentPageUsers = fetchUsers(page)
        users.extend(currentPageUsers)

        if page == 1:
            response = requests.get('https://reqres.in/api/users')
            data = response.json()
            totalPages = data['total_pages']

        page += 1

    table_html = renderUsers(users)
    print(table_html, file=open('output.html', 'w'))

class UserRenderingTestCase(unittest.TestCase):
    def test_fetchUsers(self):
        # Mock the response from the API
        response_data = {
            'data': [
                {'id': 1, 'first_name': 'John', 'last_name': 'Doe', 'email': 'john@example.com', 'avatar': 'example.com/avatar1.png'},
                {'id': 2, 'first_name': 'Jane', 'last_name': 'Smith', 'email': 'jane@example.com', 'avatar': 'example.com/avatar2.png'}
            ]
        }
        with unittest.mock.patch('requests.get') as mock_get:
            mock_get.return_value.json.return_value = response_data

            # Test the fetchUsers function
            users = fetchUsers(1)

        self.assertEqual(len(users), 2)
        self.assertEqual(users[0]['id'], 1)
        self.assertEqual(users[1]['email'], 'jane@example.com')

    def test_renderUsers(self):
        # Test the renderUsers function
        users = [
            {'id': 1, 'first_name': 'John', 'last_name': 'Doe', 'email': 'john@example.com', 'avatar': 'example.com/avatar1.png'},
            {'id': 2, 'first_name': 'Jane', 'last_name': 'Smith', 'email': 'jane@example.com', 'avatar': 'example.com/avatar2.png'}
        ]
        table_html = renderUsers(users)

        # Verify that the generated HTML contains user information
        self.assertIn('<td>1</td>', table_html)
        self.assertIn('John Doe', table_html)
        self.assertIn('john@example.com', table_html)
        self.assertIn('<img src="example.com/avatar2.png" alt="Avatar" width="200">', table_html)

if __name__ == '__main__':
    # Run the unit tests
    unittest.main()
    
cov.stop()
cov.save()
cov.report()
