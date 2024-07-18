from utils.llm_model_generator import LLMProcessModelGenerator


def execute_script():
    obj = LLMProcessModelGenerator(process_description="A then B then C", api_key="sk-", openai_model="gpt-4o")
    print(obj.grade_process_model())


if __name__ == "__main__":
    execute_script()
