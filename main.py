from github import Github, Auth
import json

class SearchProjects:
    def __init__(self, t, q, o):
        self.token_path = t
        self.query = q
        self.output_path = o

    def read_token_from_file(self):
        try:
            with open(self.token_path, 'r') as file:
                return file.read().strip()
        except IOError as e:
            print(f"Error reading the token file: {e}")
            return None

    def search_download(self):
        t = self.read_token_from_file(self.token_path)
        auth = Auth.Token(t)
        g = Github(auth=auth)

        output_reps = []
        repositories = g.search_repositories(query)
        i = 0
        for repo in repositories:
            # Systematic Sampling => total sample around 500
            if i % 2 == 0:
                r = {
                    'clone_url': repo.clone_url,
                    'full_name': repo.full_name,
                    'size': repo.size,
                    'stargazers_count': repo.stargazers_count,
                    'subscribers_count': repo.subscribers_count,
                    'watchers_count': repo.watchers_count,
                }
                output_reps.append(r)
            i += 1

        try:
            with open(self.output_path, 'w') as file:
                json.dump(output_reps, file, indent=4)
            print(f"Data successfully written to {self.output_path}")
        except IOError:
            print(f"Could not write to file {self.output_path}.")

# rule category format
# return [{'type': 'xx', 'desc':'xxx', 'rules':['a', 'b']}]
def read_json(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"The file {file_path} was not found.")
    except json.JSONDecodeError:
        print(f"Error decoding JSON from file {file_path}.")


if __name__ == '__main__':
    # 1 search projects => output url
    token_path = 'token.txt'
    query = 'is:public language:JavaScript fork:false archived:false stars:>100 size:>10000 sort:updated'
    output_path = 'rawData/repositories.json'
    # search_project = SearchProjects(token_path, query, output_path)
    # search_project.search_download()

    # 2 read raw project url
    res = read_json(output_path)
