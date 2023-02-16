res = requests.get("https://oauth.reddit.com/r/norge/hot",
                   headers=headers)

print(res.json())  # let's see what we get
