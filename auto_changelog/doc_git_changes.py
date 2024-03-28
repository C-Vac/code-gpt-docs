import os
import subprocess
import json
import requests

def get_git_changes():
    # Run the git log command to get the latest commit info
    process = subprocess.Popen(['git', 'log', '-1', '--pretty=format:%H%n%s%n%b'], stdout=subprocess.PIPE)
    output, _ = process.communicate()
    return output.decode('utf-8')

def read_prompt(prompt_path):
    with open(prompt_path, 'r') as file:
        return file.read()
    
def call_codegpt_api(model, prompt, data):
    # Get the API key from the environment variable
    api_key = os.getenv('CODEGPT_API_KEY')
    if not api_key:
        raise ValueError("You forgot to set the CODEGPT_API_KEY environment variable, homie!")

    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json',
    }
    # Use the actual endpoint URL for the CodeGPT API
    codegpt_api_endpoint = "https://api.codegpt.co/ai/generate"
    
    # Construct the payload with the model, prompt, and data
    payload = {
        'model': model,
        'prompt': prompt + data,  # Concatenate the prompt with the git changes
        'max_tokens': 1024  # Adjust as needed
    }
    
    response = requests.post(codegpt_api_endpoint, headers=headers, data=json.dumps(payload))
    return response.json()

# Function to load the template
def load_template(template_name):
    template_dir = os.path.join(os.path.dirname(__file__), 'markup-templates')
    template_path = os.path.join(template_dir, template_name)
    with open(template_path, 'r') as file:
        return file.read()

# Function to format the changelog in HTML
def format_changelog_in_html(template, commit_data):
    commit_lines = commit_data.split('\n')
    commit_hash = commit_lines[0]
    commit_message = commit_lines[1]
    commit_body = '\n'.join(commit_lines[2:])

    return template.format(commit_hash=commit_hash, commit_message=commit_message, commit_body=commit_body)

# Function to populate the XML template with commit data
def populate_xml_template(template, version, commit_hash, commit_message, change_notes):
    return template.format(Version=version, commit_hash=commit_hash, commit_message=commit_message, change_notes=change_notes)


# Function to save output to a file
def save_to_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

# Main flow
if __name__ == '__main__':
    # TODO: Load settings from /config.json, refactor code to use symbols instead of literals

    templatesdir = os.path.join(os.path.dirname(__file__),'markup-templates')
    
    # Load the prompt instructions
    prompt_instructions = read_prompt('prompt.md')

    # Load templates from /markup-templates/
    html_template = load_template('message/change_message.html')
    xml_template = load_template('message/change_message.xml')
    
    # Get the latest changes from git
    changes = get_git_changes()
    
    # Serialize the data
    changes_json = json.dumps({'text': changes})
    
    # Call the CodeGPT API
    codegpt_response = call_codegpt_api(changes_json)
    
    # Check if the response is successful
    if codegpt_response.get('status') == 'success':
        # Format the changelog in HTML
        html_changelog = format_changelog_in_html(html_template, changes)
        
        # Save the HTML formatted changelog to a file
        save_to_file('automated_changelog.html', html_changelog)
        print("🔥 Done, homie! Check 'automated_changelog.html' for the output. 🔥")
    else:
        print("💩 Something went wrong with the CodeGPT API call, bruh. Check your setup. 💩")
