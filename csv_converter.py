import csv
import json
import xml.etree.ElementTree as ET


def csv_to_json(csv_file_path, json_file_path):
    """Convert CSV file to JSON file."""
    with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        data = list(csv_reader)
    with open(json_file_path, mode='w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4)


def csv_to_xml(csv_file_path, xml_file_path):
    """Convert CSV file to XML file."""
    with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        data = list(csv_reader)

    root = ET.Element("root")
    for row in data:
        item = ET.SubElement(root, "item")
        for key, value in row.items():
            child = ET.SubElement(item, key)
            child.text = value

    tree = ET.ElementTree(root)
    tree.write(xml_file_path, encoding='utf-8', xml_declaration=True)


def main():
    csv_file_path = 'data.csv'
    json_file_path = 'data.json'
    xml_file_path = 'data.xml'

    csv_to_json(csv_file_path, json_file_path)
    print(f"Converted {csv_file_path} to {json_file_path}")

    csv_to_xml(csv_file_path, xml_file_path)
    print(f"Converted {csv_file_path} to {xml_file_path}")

if __name__ == "__main__":
    main()