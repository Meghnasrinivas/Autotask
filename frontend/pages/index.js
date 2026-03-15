import { useEffect, useState } from "react";
import axios from "axios";

export default function Home() {
  const [agents, setAgents] = useState([]);
  const [selected, setSelected] = useState([]);
  const [query, setQuery] = useState("");
  const [files, setFiles] = useState([]);
  const [response, setResponse] = useState(null);
  const [loading, setLoading] = useState(false);
  const [showAgentMenu, setShowAgentMenu] = useState(false);

  const BACKEND_URL =
    process.env.NEXT_PUBLIC_BACKEND_URL || "http://localhost:8000";

  useEffect(() => {
    axios
      .get(`${BACKEND_URL}/api/agents`)
      .then((res) => {
        setAgents(res.data.agents || []);
      })
      .catch((err) => console.error("Agent fetch error:", err));
  }, []);

  const toggleAgent = (id) => {
    setSelected((prev) =>
      prev.includes(id) ? prev.filter((x) => x !== id) : [...prev, id]
    );
  };

  const onSend = async () => {
    if (!query.trim()) {
      alert("Please type a query.");
      return;
    }

    if (selected.length === 0) {
      alert("Please select at least one agent.");
      return;
    }

    const formData = new FormData();

    formData.append("user_query", query);
    formData.append("selected_agents", selected.join(","));
    formData.append("user_id", "anonymous");

    for (let i = 0; i < files.length; i++) {
      formData.append("files", files[i]);
    }

    setLoading(true);

    try {
      const res = await axios.post(`${BACKEND_URL}/api/ask`, formData, {
        headers: { "Content-Type": "multipart/form-data" },
      });

      setResponse(res.data);
    } catch (error) {
      console.error(error);
      alert("Backend error. Make sure FastAPI is running.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div
      style={{
        maxWidth: "900px",
        margin: "auto",
        padding: "40px",
        color: "white",
      }}
    >
      <h1 style={{ textAlign: "center" }}>
        Multi-Agent Discussion Chat AI
      </h1>

      <p style={{ textAlign: "center", marginBottom: "30px" }}>
        Upload files, choose agents, and get combined answers.
      </p>

      {/* QUERY INPUT */}
      <div style={{ display: "flex", alignItems: "center", gap: "10px" }}>
        <button
          onClick={() => setShowAgentMenu(!showAgentMenu)}
          style={{
            fontSize: "22px",
            padding: "12px",
            borderRadius: "10px",
            background: "#3b82f6",
            border: "none",
            color: "white",
            cursor: "pointer",
          }}
        >
          +
        </button>

        <textarea
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Type your query..."
          style={{
            flex: 1,
            padding: "15px",
            borderRadius: "10px",
            border: "1px solid #333",
            background: "#111",
            color: "white",
          }}
        />
      </div>

      {/* AGENT MENU */}
      {showAgentMenu && (
        <div
          style={{
            background: "#111",
            padding: "15px",
            borderRadius: "10px",
            marginTop: "10px",
          }}
        >
          <h3>Select AI Agents</h3>

          {agents.length === 0 && <p>No agents available</p>}

          {agents.map((agent) => (
            <div key={agent.id}>
              <label style={{ cursor: "pointer" }}>
                <input
                  type="checkbox"
                  checked={selected.includes(agent.id)}
                  onChange={() => toggleAgent(agent.id)}
                  style={{ marginRight: "8px" }}
                />
                {agent.name}
              </label>
            </div>
          ))}
        </div>
      )}

      {/* SELECTED AGENT TAGS */}
      {selected.length > 0 && (
        <div style={{ marginTop: "10px" }}>
          {selected.map((id) => {
            const agent = agents.find((a) => a.id === id);

            return (
              <span
                key={id}
                style={{
                  background: "#2563eb",
                  padding: "6px 10px",
                  borderRadius: "6px",
                  marginRight: "6px",
                  fontSize: "12px",
                }}
              >
                {agent?.name || id}
              </span>
            );
          })}
        </div>
      )}

      {/* FILE UPLOAD */}
      <div style={{ marginTop: "10px" }}>
        <input
          type="file"
          multiple
          onChange={(e) => setFiles([...e.target.files])}
        />
      </div>

      {/* SEND BUTTON */}
      <button
        onClick={onSend}
        disabled={loading}
        style={{
          width: "100%",
          marginTop: "10px",
          padding: "12px",
          borderRadius: "10px",
          background: "#2563eb",
          color: "white",
          border: "none",
          cursor: "pointer",
        }}
      >
        {loading ? "Working..." : "Send"}
      </button>

      {/* RESPONSE AREA */}
      <div
        style={{
          marginTop: "30px",
          background: "#111",
          padding: "20px",
          borderRadius: "10px",
        }}
      >
        {response ? (
          <>
            <h2>Final Answer</h2>

            <pre style={{ whiteSpace: "pre-wrap" }}>
              {response.final_answer}
            </pre>

            {/* DOWNLOAD PDF */}
            {response?.pdf_file && (
              <a
                href={`http://localhost:8000/${response.pdf_file}`}
                target="_blank"
                style={{
                  display: "inline-block",
                  marginTop: "10px",
                  padding: "10px 15px",
                  background: "#22c55e",
                  color: "white",
                  borderRadius: "8px",
                  textDecoration: "none",
                }}
              >
                Download PDF Report
              </a>
            )}

            <h3>Agent Details</h3>

            <pre>
              {JSON.stringify(response.agent_responses, null, 2)}
            </pre>
          </>
        ) : (
          <p>No answer yet.</p>
        )}
      </div>
    </div>
  );
}