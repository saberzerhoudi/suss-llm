from sussllm.user_profile.component.loggers import Actions
from sussllm.user_profile.component.result_stopping_decider.base import BaseDecisionMaker

class SequentialNonrelDecisionMaker(BaseDecisionMaker):
    """
    A concrete implementation of a decision maker.
    Returns True iif the depth at which a user is in a SERP is less than a predetermined value.
    """
    def __init__(self, user_context, logger, nonrelevant_threshold=3):
        super(SequentialNonrelDecisionMaker, self).__init__(user_context, logger)
        self.__nonrelevant_threshold = nonrelevant_threshold  # The threshold; get to this point, we stop in the current SERP.

    def decide(self):
        """
        If the user's current position in the current SERP is < the maximum depth, look at the next snippet in the SERP.
        Otherwise, a new query should be issued.
        """
        counter = 0
        examined_snippets = self._user_context.get_examined_snippets()
        
        for snippet in examined_snippets:
            judgment = snippet.judgment
            
            if judgment == 0:
                counter = counter + 1
                
                if counter == self.__nonrelevant_threshold:
                    return Actions.QUERY
            else:
                counter = 0  # Break the sequence; found something relevant, reset the counter.
        
        return Actions.SNIPPET