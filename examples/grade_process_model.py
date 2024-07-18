from utils import llm_model_generator


def execute_script():
    obj = llm_model_generator.initialize(process_description="A then B then C", api_key="sk-", openai_model="gpt-4o")
    print(obj.grade_process_model())


if __name__ == "__main__":
    execute_script()
