# import requests, json, re
#
# username = 'KevinXu17'
# token = ''
#
# repos_url = 'https://api.github.com/search/repositories?q=language:JavaScript+fork:false+archived:false+stars:>100+size:>10000+sort:updated'
#
# gh_session = requests.Session()
# gh_session.auth = (username, token)
#
# repos = []
#
# while True:
#     response = gh_session.get(repos_url)
#     headers = response.headers
#     links = headers['link']
#     links = re.findall(r'<([^>]+)>;\s*rel="([^"]+)"', links)
#     repos_items = json.loads(response.text)
#
#     # datas to repos
#     for r in repos_items['items']:
#         repos.append(r)
#
#     is_last = True
#     # get next link
#     for l in links:
#         if l[1] == 'next':
#             repos_url = l[0]
#             is_last = False
#     if is_last:
#         break
#
#
# # print the repo names
# for repo in repos:
#     print(repo['name'])


from github import Github, Auth

def read_token_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read().strip()
    except IOError as e:
        print(f"Error reading the token file: {e}")
        return None


if __name__ == '__main__':
    token_path = 'token.txt'
    t = read_token_from_file(token_path)
    auth = Auth.Token(t)
    g = Github(auth=auth)

    query = 'is:public language:JavaScript fork:false archived:false stars:>100 size:>10000 sort:updated'

    repositories = g.search_repositories(query)
    for repo in repositories:
        print(f'{repo.full_name}')
