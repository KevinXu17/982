import json, os, re
import pandas as pd

class ETL:

    def read_json(self, file_path):
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                return data
        except FileNotFoundError:
            print(f"The file {file_path} was not found.")
        except json.JSONDecodeError:
            print(f"Error decoding JSON from file {file_path}.")

    def read_txt_files_in_directory(self, directory_path):
        txt_files_content = {}
        for filename in os.listdir(directory_path):
            if filename.endswith(".txt"):
                file_path = os.path.join(directory_path, filename)
                with open(file_path, 'r') as file:
                    txt_files_content[filename[:-4]] = file.read()
        return txt_files_content

    # dataframe columns names: category....rule...
    def create_column_names(self, d):
        categories = set()
        rules = set()

        # find out rule belong to which category
        rule_category_dict = {}
        # input rule or category, find column index
        column_name_index = {}

        for rule_category in d:
            category = rule_category['type']
            categories.add(category)
            for r in rule_category['rules']:
                rules.add(r)
                rule_category_dict[r] =category
        column_names = list(categories) + list(rules)
        for i, v in enumerate(column_names):
            column_name_index[v] = i
        return column_names, column_name_index, rule_category_dict

if __name__ == '__main__':
    etl = ETL()
    # 1 rules by category
    rules_file = 'rulesCategory.json'
    # rule category format
    # return [{'type': 'xx', 'desc':'xxx', 'rules':['a', 'b']}]
    rules_category = etl.read_json(rules_file)
    column_names, column_name_index, rule_category_dict = etl.create_column_names(rules_category)

    # 2 read validation result
    directory_path = 'results'
    projects_result = etl.read_txt_files_in_directory(directory_path)

    rows_list = []
    # dataframe format: projectName, category1, category2...rule1, rule2...
    for k in projects_result.keys():
        row_list = [0] * len(column_names)

        res = projects_result[k]
        res_list = res.splitlines()
        for r in res_list:
            start_index = r.find('(')
            end_index = r.find(')')
            if start_index != -1 and end_index != -1:
                rule_name = r[start_index + 1 : end_index]
                if rule_name in rule_category_dict:
                    # rule + 1
                    rule_idx = column_name_index[rule_name]
                    row_list[rule_idx] = row_list[rule_idx] + 1
                    # category + 1
                    category_name = rule_category_dict[rule_name]
                    category_index = column_name_index[category_name]
                    row_list[category_index] = row_list[category_index] + 1

        rows_list.append([k] + row_list)

    # 3 dataframe -> file
    column_names = ['projectName'] +  column_names
    df = pd.DataFrame(columns=column_names)

    for i in range(len(rows_list)):
        df.loc[i] = rows_list[i]

    # load data
    csv_path = 'data/data.csv'
    df.to_csv(csv_path, index=False)




