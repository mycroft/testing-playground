from jinja2 import Template
from datetime import datetime
import random

# Define the key-value pairs for the template
context = {
    "project_name": "Testing playground",
    "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "random_number": random.randint(1, 100)
}

# Read the template file
template_file = "README.md.tmpl"
output_file = "README.md"

with open(template_file, "r") as tmpl:
    template_content = tmpl.read()

# Use Jinja2 to render the template
template = Template(template_content)
rendered_content = template.render(context)

# Write the rendered content to README.md
with open(output_file, "w") as output:
    output.write(rendered_content)

print(f"Generated {output_file} from {template_file}")
