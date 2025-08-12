import os
import time
import logging

from dotenv import load_dotenv
from openai import OpenAI

from bots import create_chatbot_assistant


load_dotenv()
logging.basicConfig(level=logging.INFO)

client = OpenAI()
MODEL = "gpt-3.5-turbo-16k"


assistant_id = os.getenv("CHATBOT_ASSISTANT_ID")
thread_id = os.getenv("CHATBOT_THREAD_ID")

if not assistant_id:
    assistant = create_chatbot_assistant(client, MODEL)
    assistant_id = assistant.id
    logging.info("Created assistant %s", assistant_id)

if not thread_id:
    thread = client.beta.threads.create()
    thread_id = thread.id
    logging.info("Created thread %s", thread_id)


message_text = "Witaj, czy mogę Ci w czymś pomóc?"
client.beta.threads.messages.create(
    thread_id=thread_id, role="user", content=message_text
)

run = client.beta.threads.runs.create(
    thread_id=thread_id,
    assistant_id=assistant_id,
)


def wait_for_run_completion(client, thread_id, run_id, sleep_interval=5, timeout=60):
    """Polls the run until completion or timeout."""

    start_time = time.time()
    while True:
        if time.time() - start_time > timeout:
            raise TimeoutError("Run did not complete within the timeout period")

        try:
            current_run = client.beta.threads.runs.retrieve(
                thread_id=thread_id, run_id=run_id
            )
            if current_run.completed_at:
                elapsed_time = current_run.completed_at - current_run.created_at
                formatted = time.strftime("%H:%M:%S", time.gmtime(elapsed_time))
                logging.info("Run completed in %s", formatted)

                messages = client.beta.threads.messages.list(thread_id=thread_id)
                last_message = messages.data[0]
                response = last_message.content[0].text.value
                print(f"Assistant Response: {response}")
                break
        except Exception as exc:  # noqa: BLE001
            logging.error("An error occurred while retrieving the run: %s", exc)
            break

        logging.info("Waiting for run to complete...")
        time.sleep(sleep_interval)


wait_for_run_completion(client, thread_id, run.id)

