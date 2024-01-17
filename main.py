# ------------------------------
#  Python Imports
# ------------------------------
import json

# ------------------------------
#  External Imports
# ------------------------------
from openfabric_pysdk.utility import SchemaUtil
from openfabric_pysdk.context import Ray, State
from openfabric_pysdk.loader import ConfigClass

# ------------------------------
#  Module Imports
# ------------------------------
from utils import generate_response
from ontology_dc8f06af066e4a7880a5938933236037.simple_text import SimpleText

# ------------------------------
#  Error Classes
# ------------------------------


############################################################
# Callback function called on update config
############################################################
def config(configuration: ConfigClass):
    # Open the "config/execution.json" file in write mode
    with open("config/execution.json", "w") as jsonfile:
        # Load the existing JSON content from the file
        config_object = json.load(jsonfile)

        # Update the "config_class" field in the loaded JSON with the provided configuration
        config_object["config_class"] = configuration

        # Dump the modified JSON back into the file
        json.dump(config_object, jsonfile)

        # Close the file after writing the updated JSON content
        jsonfile.close()


############################################################
# Callback function called on each execution pass
############################################################
def execute(request: SimpleText, ray: Ray, state: State) -> SimpleText:
    # Initialize an empty list to store the bot's responses
    output = []

    # Iterate through each text in the request
    for text in request.text:
        # Generate a response from the bot based on the constructed query
        bot_response = generate_response(query=text)

        # Add the bot's response to the output list
        output.append(bot_response)

    # Create a SimpleText object using SchemaUtil, with the generated bot responses
    return SchemaUtil.create(SimpleText(), dict(text=output))
