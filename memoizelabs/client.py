import requests
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class Fork:
    def __init__(self, api_key, base_url='http://3.93.16.238:5000'):
        self.api_key = api_key
        self.base_url = base_url
        self.state_machine = self.StateMachine()

    def fork(self, file_paths, voice_name, voice_description=''):
        url = f"{self.base_url}/process"
        headers = {
            'key': self.api_key,
            'request-type': 'ADD_USER',
            'voice_description': voice_description
        }
        files = [('files[]', open(file_path, 'rb'))
                 for file_path in file_paths]
        data = {'voice': voice_name}

        logger.info("Sending request to %s with voice name %s and description %s",
                    url, voice_name, voice_description)

        try:
            response = requests.post(
                url, files=files, headers=headers, data=data)

            for _, file_handle in files:
                file_handle.close()

            logger.info("Received response with status code %d",
                        response.status_code)

            if response.status_code == 200:
                logger.info("Request successful: %s", response.json())
                return response.json()
            else:
                response.raise_for_status()
        except requests.exceptions.RequestException as e:
            logger.error("Request failed: %s", str(e))
            return None

    class StateMachine:
        INIT = 'INIT'
        PRE_OP = 'PRE-OP'
        FAULT = 'FAULT'
        OPERATIONAL = 'OPERATIONAL'

        def __init__(self):
            self.current_state = self.INIT
            logger.info("State machine initialized in state: %s",
                        self.current_state)

        def change_state(self, new_state):
            if new_state in [self.INIT, self.PRE_OP, self.FAULT, self.OPERATIONAL]:
                logger.info("Changing state from %s to %s",
                            self.current_state, new_state)
                self.current_state = new_state
                logger.info("State changed to %s", self.current_state)
            else:
                logger.error("Invalid state: %s", new_state)
