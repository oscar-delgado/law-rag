# LawRAG

> [!NOTE]
> This project is currently under development

## 🔨 Build and run locally

For running this project locally you'll need to have [Docker](https://docs.docker.com/engine/install/) installed. Once Docker is currently installed, you can follow the steps:

1. Add a .env file with the following content

```
OPENAI_API_KEY=<Your OpenAI key>
```

2. Build the project

```bash
docker compose build
```

3. Run the project

```bash
docker compose up
```

Once all is OK, you'll be able to access `http://localhost:5173` to use it.

> [!WARNING]
> The first time may be slower than usual because it may be ingesting the documents in the `api/law_texts` folder.
