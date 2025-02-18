#! /usr/bin/python3

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import json

url = 'https://agora.xtec.cat/iesmila/oferta-educativa/cicles-formatius-de-grau-mitja/'

# First parsing of the HTML to get the <td> tags with a specific attribute
html = requests.get(url)
soup = BeautifulSoup(html.content, 'html.parser')
tds = soup.find_all("td", attrs={"style":"width: 45.1627%; height: 51px;"})

# We use a set to avoid duplicate links
seen_links = set()

# List where we will store the excursions
excursions_data = []

# Create the file
with open("excursions.json", "w") as excursions_file:
    # Explore the links on the main page where all the cycle links are located
    for td in tds:
        # Get the links that lead us to the cycles
        link = td.find("a")
        # Get the name of the cycle
        module = link.text.strip()
        if link:
            # href of the cycle page link
            href = link['href']
            # Make the HTTP request for the cycle page
            html_cycle = requests.get(href)
            soup_cycle = BeautifulSoup(html_cycle.content, 'html.parser')

            # Search for the excursion links
            tags_cycle = soup_cycle.find_all("a", attrs={"rel": "bookmark"})
            for tag in tags_cycle:
                if tag and tag.has_attr('href'):
                    # Get the href of the excursion
                    href_cycle = tag['href']
                    title_excursion = tag.text.strip()

                    # Write only if the title is not empty and the link has not been written before
                    if title_excursion and href_cycle not in seen_links:
                        seen_links.add(href_cycle)

                        # Make sure the href is a full URL
                        full_url = urljoin(url, href_cycle)

                        # Scrape the excursion page
                        html_excursion = requests.get(full_url)
                        soup_excursion = BeautifulSoup(html_excursion.content, 'html.parser')

                        # Get the date of the excursion
                        date_excursion = soup_excursion.find("span", attrs={"class":"entry-date"})
                        date = date_excursion.text.strip() if date_excursion else "Date not available"

                        # Get the content of the excursion
                        div_excursion = soup_excursion.find_all("div", attrs={"class":"entry-content"})
                        content = ""
                        for div in div_excursion:
                            content += div.text.strip() + "\n"

                        # Store the data in a dictionary
                        excursion = {
                            "module": module[0:4],
                            "title": title_excursion,
                            "url": full_url,
                            "date": date,
                            "content": content.strip()
                        }

                        # Add the excursion dictionary to the list
                        excursions_data.append(excursion)
    # Save all the data to a JSON file
    json.dump(excursions_data, excursions_file, indent=4, ensure_ascii=False)
