from openai import OpenAI
import time
import json


def pure_json_filter(reply_text:str)->json:
    # filter the "```json" and "```" in the response message
    if reply_text.startswith("```json"):
        reply_text = reply_text[7:]
    if reply_text.endswith("```"):
        reply_text = reply_text[:-3]
    while reply_text[0] != "{":
        reply_text = reply_text[1:]
    while reply_text[-1] != "}":
        reply_text = reply_text[:-1]
    # print the json
    # print(json.loads(reply_text))
    # write the json to file and 4 space indent (ensure_ascii=False for Chinese)
    return json.dumps(json.loads(reply_text), ensure_ascii=False)

# private content detection
def assistant_api(filepath)->json:
    # if apikey and assistantId not exist, throw error says api key or assistant id is missing.
    try: 
        apikey = open('./API_key.txt', 'r').read()
        assistantId = open('./assistant_id.txt', 'r').read()
    except FileNotFoundError:
        print("api key or assistant id is missing.")
        exit(1)

    try:
        file = open(filepath, 'r', encoding='utf-8').read()
    except FileNotFoundError:
        print("file not found: ", filepath)
        exit(1)

    client = OpenAI(api_key=apikey)
    thread = client.beta.threads.create()

    message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=file,
    )
    run = client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=assistantId
    )


    # wait for run to complete
    while True:
        run = client.beta.threads.runs.retrieve(
            thread_id=thread.id,
            run_id=run.id,
        )
        if run.status not in ["queued", "in_progress"]:
            break
        time.sleep(0.5)
        print ("Waiting for run to complete...")


    messages = client.beta.threads.messages.list(
        thread_id=thread.id,
    )

    reply = messages.data[0].content[0].text.value
    # print("private content list:", reply)


    # return private content list in json format
    return pure_json_filter(reply)



if __name__ == '__main__':
    filepath = './tempFiles/udgra_01/ScanText/images_5.txt'
    result = assistant_api(filepath)
    print(result)

    # # save the json to file
    # with open('./images_0.json', 'w', encoding='utf-8') as json_file:
    #     json.dump(json.loads(result), json_file, ensure_ascii=False, indent=4)

