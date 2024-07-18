from utils.general_utils import openai_connection


def improve_process_description(descr: str,  api_key, openai_model, api_url: str = "https://api.openai.com/v1") -> str:
    conversation = [{"role": "user", "content": "Can you make the following process description richer and detailed? I need it for process modeling purposes.\n\n"+str(descr)}]

    return openai_connection.generate_response_with_history(conversation, api_key=api_key, openai_model=openai_model, api_url=api_url)
