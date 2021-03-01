from kodexa.assistant import Assistant, AssistantContext, AssistantResponse
from kodexa.assistant.assistant import AssistantPipeline
from kodexa.model.model import BaseEvent
from kodexa.pipeline import Pipeline


class TestAction:
    """ """

    def __init__(self, cheese: str = None):
        self.cheese = cheese

    def get_name(self):
        """ """
        return "Hello"


class TestAssistant(Assistant):
    """ """

    def process_event(self, event: BaseEvent, context: AssistantContext = None) -> AssistantResponse:
        """

        Args:
          event: BaseEvent:
          context: AssistantContext:  (Default value = None)

        Returns:

        """
        # This is just an example of an assistant
        # basically we are just going to return a pipeline that
        # adds a label to the document - creating a new version

        pipeline = Pipeline()
        pipeline.add_label('hello')

        return AssistantResponse([AssistantPipeline(pipeline, write_back_to_store=True)])
