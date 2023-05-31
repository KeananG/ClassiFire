#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os

def generate_directory_tree(path, indent=''):
    tree = ''
    items = sorted(os.listdir(path))
    items = [item for item in items if item not in ['.DS_Store', '.git', '.ipynb_checkpoints']]

    for i, item in enumerate(items):
        item_path = os.path.join(path, item)
        tree += f'{indent}├── {item}\n'
        
        if os.path.isdir(item_path):
            if i == len(items) - 1:
                tree += generate_directory_tree(item_path, indent + '    ')
            else:
                tree += generate_directory_tree(item_path, indent + '│   ')
    
    return tree

# Specify the path to the root directory of your project
root_directory = '.'

# Generate the directory tree
directory_tree = generate_directory_tree(root_directory)

# Print the directory tree
print(directory_tree)

# Read the current README.md file
with open('README.md', 'r') as readme_file:
    readme_content = readme_file.read()

# Find the section to update in the README.md file
start_tag = '```'
end_tag = '```'
start_index = readme_content.find(start_tag)
end_index = readme_content.find(end_tag, start_index + len(start_tag))

# Replace the old directory structure with the updated one
updated_readme_content = readme_content[:start_index + len(start_tag)] + '\n' + directory_tree + readme_content[end_index:]

# Write the updated content back to the README.md file
with open('README.md', 'w') as readme_file:
    readme_file.write(updated_readme_content)


print('Directory structure in README.md updated successfully.')

