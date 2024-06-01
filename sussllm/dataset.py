import json
import csv
import xml.etree.ElementTree as ET
from typing import List, Dict

class DatasetManager:
    """
    Manages dataset creation, storage, retrieval, and processing operations for both simulated and real-world user search behavior data.
    """
    def __init__(self, dataset_path: str):
        self.dataset_path = dataset_path

    def save_data(self, data: List[Dict]):
        """
        Saves a list of data points to a JSON file.
        """
        with open(self.dataset_path, 'w') as file:
            json.dump(data, file, indent=4)

    def load_data(self) -> List[Dict]:
        """
        Loads data from a JSON file.
        """
        with open(self.dataset_path, 'r') as file:
            return json.load(file)

    def add_data_point(self, data_point: Dict):
        """
        Adds a new data point to the existing dataset and saves the updated dataset.
        """
        data = self.load_data()
        data.append(data_point)
        self.save_data(data)

    def load_aol_data(self, aol_file_path: str) -> List[Dict]:
        """
        Loads AOL data from a CSV file.
        """
        with open(aol_file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            return [row for row in reader]

    def load_trec_data(self, trec_file_path: str) -> List[Dict]:
        """
        Loads TREC 2014 Session Track data from an XML file.
        """
        tree = ET.parse(trec_file_path)
        root = tree.getroot()
        sessions = []
        for session in root.findall('.//session'):
            session_id = session.find('sessionid').text
            interactions = []
            for interaction in session.findall('.//interaction'):
                query = interaction.find('query').text
                clicks = interaction.findall('.//click')
                clicks_list = [{'rank': click.find('rank').text, 'url': click.find('url').text} for click in clicks]
                interactions.append({'query': query, 'clicks': clicks_list})
            sessions.append({'session_id': session_id, 'interactions': interactions})
        return sessions

def main():
    
    dataset_manager = DatasetManager('simulated_search_sessions.json')

    aol_data = dataset_manager.load_aol_data('aol_data.csv')
    trec_data = dataset_manager.load_trec_data('trec_data.xml')

    dataset_manager.save_data(aol_data) 
    dataset_manager.save_data(trec_data)  

if __name__ == "__main__":
    main()
