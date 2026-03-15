from fastapi import APIRouter, UploadFile, File, Form
from typing import List

from app.modules.agent_manager import AgentManager
from app.modules.dataset_loader import DatasetLoader
from app.modules.discussion_engine import DiscussionEngine
from app.modules.pdf_generator import generate_pdf

router = APIRouter()

agent_manager = AgentManager()
dataset_loader = DatasetLoader()
discussion_engine = DiscussionEngine()


AGENTS = [
    {"id": "planner_agent", "name": "Planner Agent"},
    {"id": "research_agent", "name": "Research Agent"},
    {"id": "dataset_agent", "name": "Dataset Intelligence Agent"},
    {"id": "data_analyst_agent", "name": "Data Analyst Agent"},
    {"id": "visualization_agent", "name": "Visualization Agent"},
    {"id": "code_agent", "name": "Code Interpreter Agent"},
    {"id": "writer_agent", "name": "Writer Agent"},
    {"id": "report_agent", "name": "Report Generator Agent"}
]


@router.get("/agents")
def get_agents():
    return {"agents": AGENTS}


@router.post("/ask")
async def ask_agents(
    user_query: str = Form(...),
    selected_agents: str = Form(...),
    user_id: str = Form(...),
    files: List[UploadFile] = File(default=[])
):

    # Load datasets
    datasets = dataset_loader.load_all_datasets()

    # Run agent analysis
    agent_results = agent_manager.run_agents(user_query, datasets)

    # Combine results
    final_answer = discussion_engine.combine_results(agent_results)

    # Generate PDF
    pdf_file = generate_pdf(final_answer)

    return {
        "final_answer": final_answer,
        "pdf_file": pdf_file,
        "agent_responses": agent_results
    }