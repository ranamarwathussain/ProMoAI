from utils import llm_model_generator


def execute_script():
    proc_descr = "A then B then C"
    api_key = open("api_key.txt", "r").read().strip()
    openai_model = open("api_model.txt", "r").read().strip()
    n_candidates = 1

    obj = llm_model_generator.initialize(process_description=proc_descr, api_key=api_key, openai_model=openai_model, n_candidates=n_candidates)
    print(obj.grade_process_model())
    obj.view_bpmn("svg")


if __name__ == "__main__":
    execute_script()
