import pandas as pd

class CSVResponseEngine:

    def __init__(self):
        self.files = {
            "courses": "app/data/neurax_employees_dataset.csv",
            "products": "app/data/neurax_project_history_dataset.csv",
            "faq": "app/data/neurax_project_dataset.csv",
            "support": "app/data/neurax_tools_dataset(1).csv"
        }

    def detect_file(self, query):

        query = query.lower()

        if "course" in query:
            return "courses"

        elif "product" in query:
            return "products"

        elif "help" in query or "support" in query:
            return "support"

        else:
            return "faq"

    def search_csv(self, query):

        file_key = self.detect_file(query)

        df = pd.read_csv(self.files[file_key])

        query = query.lower()

        for _, row in df.iterrows():

            row_text = " ".join(str(value).lower() for value in row)

            if query in row_text:
                return row.to_dict()

        return {"message": "No information found."}