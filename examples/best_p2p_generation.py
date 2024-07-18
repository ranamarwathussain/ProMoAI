from utils import llm_model_generator


def execute_script():
    obj = llm_model_generator.initialize(process_description="please model a Purchase-to-Pay process.", api_key=open("api_key.txt", "r").read(), openai_model="gpt-3.5-turbo", n_candidates=2, debug=True)
    print("(executed another time) Grade of the best candidate: ", obj.grade_process_model())
    obj = llm_model_generator.update(obj, "Please improve the process model", n_candidates=2, debug=True)
    print("(executed another time) Grade of the best candidate after improvement: ", obj.grade_process_model())
    obj.view_bpmn("svg")


if __name__ == "__main__":
    execute_script()
