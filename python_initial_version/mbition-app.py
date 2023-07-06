import requests

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
    print(table_html, file=open('index.html', 'w'))
    

UserRendering()
