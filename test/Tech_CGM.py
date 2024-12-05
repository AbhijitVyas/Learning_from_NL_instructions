import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY', 'your-key-if-not-using-env')
client = OpenAI()

class OpenAIChatBot:
    def __init__(self):
        pass

    def ask_to_chat_gpt(self, prompt_msg: str) -> str:
        """
         This method makes call to chatgpt with prompt_msg as input parameter
        :return: a response form the GPT model as string
        """

        stream = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt_msg}],
            stream=False,
        )

        steamOutPut = stream.choices[0].message.content
        print(f"steam output English {steamOutPut}")
        return steamOutPut


if __name__ == "__main__":
    prompt_inquire_about_healthcare = ("you are a bot which scrolls though internet looking for the latest "
                                       "advancements in healthcare. create a response by providing a quick "
                                       "insights into following table formate, find 10 entries: "
                                       "sr. no., topic, summery, authors, source, date of publishing, "
                                       "for example: Sr. No. is number of raw, Topic is Name of the topic, Summery is summery of the article found, "
                                       "Authors is Writer of the article, Source is the link of the webpage, Date of publishing is article date")
    openAIChatBot = OpenAIChatBot()
    steamOutPut = openAIChatBot.ask_to_chat_gpt(prompt_inquire_about_healthcare)
    prompt_to_convert_into_german_language = f"translate the given text into German language: {steamOutPut}"

    steam_out_put_german = openAIChatBot.ask_to_chat_gpt(prompt_to_convert_into_german_language)


