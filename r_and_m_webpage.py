import requests

# Base URL
url = "https://rickandmortyapi.com/api/character"

# Request API data
response = requests.get(url)
data = response.json()

# Start HTML structure
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Rick and Morty Characters</title>
</head>
<body>
"""



# Add character cards
for char in data["results"]:
    html_content += f"""
    
    
    <div>
        <h2>{char['name']}</h2>
    <table>
        <tr>
            <td rowspan="3"><img src= "{char['image']}" alt ="Character Picture"></td>
            <th>Status:</th>
            <td>{char['status']}ive</td>
        </tr>
        <tr>
            <th>Species:</th>
            <td>{char['species']}</td>
        </tr>
        <tr>
            <th>Location:</th>
            <td>{char['origin']['name']}</td>
        </tr>
    </table>
    </div>
    """
# End character cards


html_content += """
</body>
</html>
"""
# End HTML structure

# Write to HTML file
with open("rick_and_morty.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("HTML file created: rick_and_morty_strong.html")

