# This is a simple engine based on openai's api.
# the engin will be used to generate a response to a given input.
# the main purpose is to help get data quickly structrued for faster processing.

import openai

class ai_cotex:
    def __init__(self, api_key):
        openai.api_key = api_key

    def compare_locations(self, sites_data):
        prompt = (f"Please provide a list of sites and their current and new locations as urls  in the following format: 'parent_folder/parent_site_1 , destination_dir/destination_dir_1', return in csv format. \n {sites_data}"
                  f"Task: mapping")

        completions = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )

        message = completions.choices[0].text
        return message

        
        
    