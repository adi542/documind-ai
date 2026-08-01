from app.models.models.search_result import SearchResult


class PromptBuilder:

    def build_prompt(
        self,
        question: str,
        results: list[SearchResult]
    ) -> str:

        system_prompt = self._build_system_prompt()

        rules = self._build_rules()

        context = self._build_context(results)

        question_section = self._build_question(question)

        return "\n\n".join([
            system_prompt,
            rules,
            context,
            question_section
        ])

    def _build_system_prompt(self) -> str:

        return (
            "You are an AI assistant that answers questions "
            "about uploaded documents."
        )

    def _build_rules(self) -> str:

        return (
            "Rules:\n"
            "- Answer only using the provided context.\n"
            "- If the answer is not present in the context, "
            "say that you could not find the information "
            "in the uploaded documents.\n"
            "- Do not make up facts.\n"
            "- Be clear, accurate, and concise."
        )

    def _build_context(
        self,
        results: list[SearchResult]
    ) -> str:

        sections = ["Context:"]

        for result in results:

            chunk = result.chunk

            sections.append(
                (
                    f"\nDocument: {chunk.chunk.document_id}\n"
                    
                    f"Content:\n"
                    f"{chunk.chunk.text}\n"
                    f"{'-' * 40}"
                )
            )

        return "\n".join(sections)

    def _build_question(
        self,
        question: str
    ) -> str:

        return (
            f"Question:\n"
            f"{question}\n\n"
            "Answer:"
        )