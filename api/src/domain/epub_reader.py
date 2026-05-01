import re

from bs4 import BeautifulSoup
from ebooklib import ITEM_DOCUMENT, epub
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter


class EpubReader:
    CHUNK_SIZE = 400
    CHUNK_OVER = 50

    def read(self) -> list:
        cv_epub = "law_texts/BOE-127_Codigo_de_la_Vivienda_del_Estado.epub"
        codigo_vivienda_docs = self.extract_epub_text(cv_epub)
        lau_epub = "law_texts/BOE-A-1994-26003-consolidado.epub"
        lau_docs = self.extract_epub_text(lau_epub)

        script_splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.CHUNK_SIZE,
            chunk_overlap=self.CHUNK_OVER,
            add_start_index=True,
            separators=[" Artículo ", "\n\n", "\n", " ", ""],
        )

        all_chunks = []
        for doc in codigo_vivienda_docs:
            chunks = [
                Document(
                    page_content=doc,
                    metadata={"title": "Código de la Vivienda del Estado"},
                )
                for doc in script_splitter.split_text(doc)
            ]
            all_chunks.extend(chunks)

        for doc in lau_docs:
            chunks = [
                Document(
                    page_content=doc,
                    metadata={"title": "Ley de Arrendamientos Urbanos (LAU)"},
                )
                for doc in script_splitter.split_text(doc)
            ]
            all_chunks.extend(chunks)
        print(f"Total chunks: {len(all_chunks)}")
        return all_chunks

    def extract_epub_text(self, epub_path: str):
        book = epub.read_epub(epub_path)
        documents = []

        for item in book.get_items():
            if item.get_type() == ITEM_DOCUMENT:
                soup = BeautifulSoup(item.get_content(), "xml")

                # Remove scripts/styles
                for tag in soup(["script", "style"]):
                    tag.decompose()

                text = soup.get_text(separator=" ")
                text = self.__clean_text(text)

                if text:
                    documents.append(text)

        return documents

    def __clean_text(self, text: str):
        # Remove excessive whitespace
        text = re.sub(r"\s+", " ", text)
        return text.strip()

    def _to_jsonl(self):
        with open("chunks.jsonl", mode="w") as file:
            for document in self.read():
                file.write(f"{document.page_content}\n")
