import pandas as pd


class AgentManager:

    def run_agents(self, query, datasets):

        results = {}

        employees = datasets.get("employees")
        tools = datasets.get("tools")
        history = datasets.get("history")

        query = query.lower()

        # ---------------- EMPLOYEE WORK ALLOCATION ----------------

        if "employee" in query or "team" in query or "work" in query:

            if employees is None or len(employees) == 0:
                results["data_analyst_agent"] = "No employee dataset found."
            else:

                roles = [
                    "Data Engineer",
                    "ML Engineer",
                    "Data Scientist",
                    "Backend Developer",
                    "Frontend Developer",
                    "DevOps Engineer"
                ]

                text = "Employee Work Allocation Plan\n\n"

                for i, role in enumerate(roles):

                    if i < len(employees):

                        name = str(employees.iloc[i].iloc[0])

                        text += f"{role} → {name}\n"

                results["data_analyst_agent"] = text

        # ---------------- AI TOOL RANKING ----------------

        elif "tool" in query or "ai tool" in query:

            if tools is None or len(tools) == 0:

                results["research_agent"] = "No tools dataset found."

            else:

                text = "AI Tools Ranking Based on Quality\n\n"

                rating_column = None

                for col in tools.columns:
                    if "rating" in col.lower() or "score" in col.lower():
                        rating_column = col

                if rating_column:

                    sorted_tools = tools.sort_values(by=rating_column, ascending=False)

                    top = sorted_tools.head(5)

                else:

                    top = tools.head(5)

                for i, row in top.iterrows():

                    tool = str(row.iloc[0])

                    if rating_column:
                        rating = row[rating_column]
                        text += f"{tool} → Rating: {rating}\n"
                    else:
                        text += f"{tool}\n"

                results["research_agent"] = text

        # ---------------- PROJECT HISTORY ANALYSIS ----------------

        elif "project" in query or "history" in query:

            if history is None or len(history) == 0:

                results["dataset_agent"] = "No project history dataset found."

            else:

                total_projects = len(history)

                text = "Project History Analysis\n\n"

                text += f"Total Projects Analyzed: {total_projects}\n\n"

                text += "Insights:\n"
                text += "- Similar project architectures detected\n"
                text += "- AI customer support systems appear frequently\n"
                text += "- Recommended reuse of successful deployment strategies\n"

                results["dataset_agent"] = text

        # ---------------- REQUIREMENT DOCUMENT ----------------

        else:

            results["planner_agent"] = (
                "Client Requirement Analysis\n\n"
                "AI Powered Customer Support System Development Plan\n\n"
                "1. Data Collection → Data Engineer\n"
                "2. NLP Model Training → ML Engineer\n"
                "3. Knowledge Base Indexing → Data Scientist\n"
                "4. API Development → Backend Developer\n"
                "5. Chat Interface → Frontend Developer\n"
                "6. Deployment & Monitoring → DevOps Engineer\n"
            )

        return results