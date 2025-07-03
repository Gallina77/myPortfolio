import json
import random
import os
import time

class TypeAndLetGo:
    def __init__(self):
        self.prompt = None
        self.writing_time = 125


    def get_prompt(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        json_path = os.path.join(script_dir, 'writing_prompts.json')
        with open(json_path, 'r') as f:
            data = json.load(f)
            self.prompt = random.choice(data["writing_prompts"])
        return self.prompt

    def writing_timer_countdown(self):
        while self.writing_time:
            time.sleep(1)
            self.writing_time -= 1
        print("Timer is up")






