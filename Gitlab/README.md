# Gitlab

<details>
   
<summary>Count Gitlab bots</summary>

```
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
