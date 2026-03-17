# Updated Architecture Flow (Mermaid)

Below is the updated Mermaid diagram representing the high-level flow of the PDF Summary App with vectorless RAG:

```mermaid
flowchart LR
    subgraph User
        U1["User Uploads PDF"]
        U2["User Views Summary"]
        U3["User Asks Qs"]
    end
    subgraph Frontend
        FE["React App"]
    end
    subgraph Backend
        BE["FastAPI Server"]
        UPLOADS["Uploads Folder"]
        PDFPROC["PDF Processing (PyPDF2)"]
        CHUNK["Chunking (Text Split)"]
        SEARCH["Keyword-Based Search (BM25)"]
        DB["SQLite DB (SQLAlchemy)"]
    end
    subgraph LLM
        OLLAMA["Ollama LLM (Llama2)"]
    end

    U1-->|Upload|FE
    FE-->|REST API|BE
    BE-->|Save PDF|UPLOADS
    BE-->|Process PDF|PDFPROC
    PDFPROC-->|Chunk|CHUNK
    CHUNK-->|Index|SEARCH
    SEARCH-->|Store|DB
    DB-->|Retrieve Context|BE
    BE-->|Summarize|OLLAMA
    OLLAMA-->|Summary|BE
    BE-->|Summary|FE
    FE-->|Show|U2

    FE-->|Ask Q|BE
    BE-->|Retrieve|SEARCH
    SEARCH-->|Retrieve Context|BE
    BE-->|Answer|OLLAMA
    OLLAMA-->|Answer|BE
    BE-->|Answer|FE
    FE-->|Show|U3

    classDef store fill:#f9f,stroke:#333,stroke-width:1px;
    class UPLOADS,DB store;
```

**Legend:**

- User interacts with the React frontend (upload, view summary, ask questions)
- Frontend communicates with FastAPI backend
- Backend processes PDF, stores files, manages summary (persistent) and Q&A (in-memory) caches
- Ollama LLM is used for summarization and Q&A
- Results are returned to the user via the frontend

---

For more details, see the rest of this `architecture.md` and the backend `README.md`.
