import pandas as pd


class DatasetAgent:

    def analyze(self, loader, query):

        query = query.lower()

        # highest success project
        if "success" in query and loader.history is not None:

            df = loader.history

            row = df.loc[df["success_score"].idxmax()]

            return f"The most successful project is {row['project_name']} with score {row['success_score']}."

        # most used tool
        if "tool" in query and loader.history is not None:

            df = loader.history

            tool = df["tools_used"].value_counts().idxmax()

            return f"The most frequently used tool is {tool}."

        # highest experience employee
        if "experience" in query and loader.employees is not None:

            df = loader.employees

            row = df.loc[df["experience_years"].idxmax()]

            return f"The most experienced employee is {row['name']} with {row['experience_years']} years."

        # lowest workload
        if "workload" in query and loader.employees is not None:

            df = loader.employees

            row = df.loc[df["current_workload_percent"].idxmin()]

            return f"The employee with the lowest workload is {row['name']}."

        return "Dataset loaded successfully but query type not recognized."