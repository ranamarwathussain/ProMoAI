from utils import llm_model_generator
from utils.general_utils import improve_descr


def execute_script():
    proc_descr = "please model a Purchase-to-Pay process."
    feedback = "Please improve the process model"
    api_key = open("api_key.txt", "r").read()
    openai_model = "gpt-3.5-turbo"
    n_candidates = 2

    # improve the process description
    proc_descr = improve_descr.improve_process_description(proc_descr, api_key, openai_model)
    print(proc_descr)

    obj = llm_model_generator.initialize(process_description=proc_descr, api_key=api_key, openai_model=openai_model, n_candidates=n_candidates, debug=True)
    print("(executed another time) Grade of the best candidate: ", obj.grade_process_model())
    obj = llm_model_generator.update(obj, feedback, n_candidates=n_candidates, debug=True)
    print("(executed another time) Grade of the best candidate after improvement: ", obj.grade_process_model())
    obj.view_bpmn("svg")


if __name__ == "__main__":
    execute_script()
