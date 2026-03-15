import pandas as pd
import os


class DatasetLoader:

    def __init__(self):

        self.data_path = "app/data"

    def load_all_datasets(self):

        datasets = {}

        try:
            datasets["employees"] = pd.read_csv(
                os.path.join(self.data_path, "neurax_employees_dataset.csv")
            )
        except:
            datasets["employees"] = None

        try:
            datasets["tools"] = pd.read_csv(
                os.path.join(self.data_path, "neurax_tools_dataset (1).csv")
            )
        except:
            datasets["tools"] = None

        try:
            datasets["projects"] = pd.read_csv(
                os.path.join(self.data_path, "neurax_projects_dataset.csv")
            )
        except:
            datasets["projects"] = None

        try:
            datasets["history"] = pd.read_csv(
                os.path.join(self.data_path, "neurax_project_history_dataset.csv")
            )
        except:
            datasets["history"] = None

        return datasets