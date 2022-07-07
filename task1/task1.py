import requests
import xml.etree.ElementTree as ET


def task1_solution():
    url = 'https://coding-academy.pl/all_customers'
    response = requests.get(url)
    root = ET.fromstring(response.content)

    customer_numbers = list()
    for element in root.findall('customer'):
        customer_numbers.append(element.text)

    with open(r'task1_solution.txt', 'w') as fp:
        for number in customer_numbers:
            fp.write(f"{number}\n")
    pass


if __name__ == '__main__':
    task1_solution()
