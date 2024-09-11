import os
import pm4py
import json
from utils import llm_model_generator, shared


api_url = open("api_url.txt", "r").read().strip()
api_key = open("api_key.txt", "r").read().strip()
openai_model = open("api_model.txt", "r").read().strip()
n_candidates = 1

folders = ["short", "medium", "long"]

for fold in folders:
    for proc_file in os.listdir(fold):
        output_file = os.path.join("results", "01_diff_llms__"+openai_model.replace("/", "").replace(":", "")+"__"+fold+"__"+proc_file)
        proc_descr = open(os.path.join(fold, proc_file), "r").read().strip()

        if not os.path.exists(output_file):
            try:
                obj = llm_model_generator.initialize(process_description=proc_descr, api_key=api_key, openai_model=openai_model,
                                                     api_url=api_url, n_candidates=n_candidates)

                powl = obj.process_model
                net, im, fm = pm4py.convert_to_petri_net(powl)
                visible_transitions = [x for x in net.transitions if x.label is not None]

                reachability_graph = pm4py.convert_to_reachability_graph(net, im, fm)

                dictio = {"visible_transitions": len(visible_transitions), "states_reachability_graph": len(reachability_graph.states), "n_iterations": shared.LAST_ITERATIONS, "self_grading": obj.grade_process_model()}

                F = open(output_file, "w")
                json.dump(dictio, F)
                F.close()
            except:
                pass

        break
    break
