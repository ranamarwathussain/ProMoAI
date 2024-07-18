import pm4py
from utils import llm_model_generator
from utils.general_utils import pt_to_powl_code


def execute_script():
    log = pm4py.read_xes("running-example.xes")
    process_tree = pm4py.discover_process_tree_inductive(log)
    powl_code = pt_to_powl_code.recursively_transform_process_tree(process_tree)
    obj = llm_model_generator.initialize(None, "sk-",
                                   powl_model_code=powl_code, openai_model="gpt-4o")
    obj = llm_model_generator.update(obj, "Can you add an activity Explode Bomb in the end")
    obj.view_bpmn("svg")


if __name__ == "__main__":
    execute_script()
