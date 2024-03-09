import random 
from datetime import datetime, timedelta
import json
filename = 'generated_data.json'

class TropicalArea():
    """A program that generates data for a tropical area"""
    def __init__(self, num_entries = 50):
        self.num_entries = num_entries
        self.tropical_area = {
            "data": []
        }
        
    def generating_data(self):
        """Using random attributes to generate data"""
        for data in range(0, self.num_entries):
            timestamp = (datetime.now() - timedelta(days=self.num_entries - data)).isoformat()
            entry = {
            'id' : data,
            'timestamp' : timestamp,
            'humidity': round(random.uniform(20,80),2),
            'temperature': round(random.uniform(15,35),2),
            'sunshine': random.choice([True, False]),
            'air_quality': round(random.uniform(50,100),2),
            'N': round(random.uniform(1,10),2),
            'P': round(random.uniform(1,10),2),
            'K': round(random.uniform(1,10),2),
            'soil_moisture': round(random.uniform(0,10),2),
            'carbon_data': round(random.uniform(0,10),2),
            'soil_moisture': round(random.uniform(0,30),2),
            }
            self.tropical_area["data"].append(entry)
            
    def store_data(self):
        """Storing the generated dataset in a json file"""
        self.generating_data()
        with open(filename, "w") as fn:
            json.dump(self.tropical_area,fn)