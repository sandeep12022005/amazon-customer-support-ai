import "./App.css";
import { useState, useEffect, useRef } from "react";
import axios from "axios";
import ReactMarkdown from "react-markdown";
import AdminDashboard from "./AdminDashboard";

// Railway Backend URL
const API_URL =
  "https://amazon-customer-support-ai-production.up.railway.app";

function App() {
  const [page, setPage] = useState("chat");

  const sessionId =
    localStorage.getItem("session_id") || crypto.randomUUID();

  localStorage.setItem("session_id", sessionId);

  const [message, setMessage] = useState("");

  const [loading, setLoading] = useState(false);

  const [messages, setMessages] = useState([
    {
      sender: "bot",
      text:
        "👋 Welcome to Amazon Customer Support!\n\nI can help you with:\n\n• Orders\n• Returns & Refunds\n• Prime Membership\n• Billing\n• Products\n\nHow may I assist you today?"
    }
  ]);

  const bottomRef = useRef(null);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({
      behavior: "smooth"
    });
  }, [messages, loading]);

  async function sendMessage() {
    if (message.trim() === "") return;

    const userMessage = {
      sender: "user",
      text: message
    };

    setMessages((prev) => [...prev, userMessage]);

    const currentMessage = message;

    setMessage("");

    setLoading(true);

    try {
      const response = await axios.post(
        `${API_URL}/chat`,
        {
          session_id: sessionId,
          message: currentMessage
        }
      );

      const botMessage = {
        sender: "bot",
        text: response.data.reply
      };

      setMessages((prev) => [...prev, botMessage]);
    } catch (err) {
      console.log(err);

      setMessages((prev) => [
        ...prev,
        {
          sender: "bot",
          text: "❌ Unable to contact server."
        }
      ]);
    }

    setLoading(false);
  }

  if (page === "dashboard") {
    return (
      <div>
        <div className="navbar">
          <div className="logo">
            🛒 Amazon Customer Support AI
          </div>

          <div className="nav-right">
            <button onClick={() => setPage("chat")}>
              💬 Customer Chat
            </button>

            <button onClick={() => setPage("dashboard")}>
              📊 Dashboard
            </button>

            <span className="status">
              🟢 Online
            </span>
          </div>
        </div>

        <AdminDashboard />
      </div>
    );
  }

  return (
    <div className="container">
      <div className="navbar">
        <div className="logo">
          🛒 Amazon Customer Support AI
        </div>

        <div className="nav-right">
          <button onClick={() => setPage("chat")}>
            💬 Customer Chat
          </button>

          <button onClick={() => setPage("dashboard")}>
            📊 Dashboard
          </button>

          <span className="status">
            🟢 Online
          </span>
        </div>
      </div>

      <div className="chat-box">
        {messages.map((msg, index) => (
          <div
            key={index}
            className={
              msg.sender === "user"
                ? "user-message"
                : "bot-message"
            }
          >
            <div className="message-content">
  <span className="avatar">
    {msg.sender === "user" ? "👤" : "🤖"}
  </span>

  <div className="markdown-content">
    {msg.sender === "bot" ? (
      <ReactMarkdown>{msg.text}</ReactMarkdown>
    ) : (
      <span>{msg.text}</span>
    )}
  </div>
</div>
          </div>
        ))}

        {loading && (
          <div className="bot-message">
            <div className="message-content">
              <span className="avatar">
                🤖
              </span>

              <span>Typing...</span>
            </div>
          </div>
        )}

        <div ref={bottomRef}></div>
      </div>

      <div className="input-area">
        <input
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          onKeyDown={(e) => {
            if (e.key === "Enter") {
              sendMessage();
            }
          }}
          placeholder="Ask about orders, returns, Prime, billing..."
        />

        <button
          onClick={sendMessage}
          disabled={loading}
        >
          {loading ? "Sending..." : "Send"}
        </button>
      </div>
    </div>
  );
}

export default App;