# Gitlab

<details>
   
<summary>Count Gitlab bots</summary>

```
#!/usr/bin/python3
#author: Am0rphous
#03.07.23

from gitlab import Gitlab

gitlab_url = 'https://gitlab.example'
access_token = 'glpat-secret-123'

# Create a GitLab client
gl = Gitlab(gitlab_url, private_token=access_token)

def count_users():
    try:
        # Get all the users
        users = gl.users.list(all=True)
        
        # Count users with usernames containing "bot"
        count = len([user for user in users if 'bot' in user.username.lower()])
        return count
    except Exception as e:
        print(f'Something went wrong: {str(e)}')
        return None

# Call the function
user_count = count_users()
if user_count is not None:
    print(f'The number of bots on {gitlab_url}: {user_count}')
```

</details>

<details>
   
<summary>Count total number of Gitlab users</summary>

```
#!/usr/bin/python3
#author: Am0rphous
#03.07.23

from gitlab import Gitlab

gitlab_url = 'https://gitlab.example.com
access_token = 'glpat-secret-token'

#creates a gitlab client
gl = Gitlab(gitlab_url, private_token=access_token)

def count_users():
    try:
        #get all the users
        users = gl.users.list(all=True)
        #now count them
        count = len(users)
        return count
    except Exception as e:
        print(f'Something went wrong: {str(e)}')
        return None

#call the function
user_count = count_users()
if user_count is not None:
    print(f'The number of users on {gitlab_url}: {user_count}')

```

</details>