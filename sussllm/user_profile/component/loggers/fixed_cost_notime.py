from sussllm.user_profile.component.loggers import Actions
from sussllm.user_profile.component.loggers.fixed_cost import FixedCostLogger

class FixedCostNoTimeLogger(FixedCostLogger):
    """
    A simple extension to the FixedCostLogger - only this time, no time limit is specified.
    """
    def __init__(self,
                 output_controller,
                 user_context,
                 query_cost=10,
                 document_cost=20,
                 snippet_cost=3,
                 serp_results_cost=5,
                 mark_document_cost=3):
        """
        Instantiates the BaseLogger class and sets up additional instance variables for the FixedCostLogger.
        Note that this does not enforce the time limit...
        """
        time_limit = 0
        
        super(FixedCostNoTimeLogger, self).__init__(output_controller,
                                                    user_context,
                                                    time_limit,
                                                    query_cost,
                                                    document_cost,
                                                    snippet_cost,
                                                    serp_results_cost,
                                                    mark_document_cost)
    
    def get_progress(self):
        """
        Concrete implementation of the abstract get_progress() method.
        Returns a value between 0 and 1 representing how far through the current simulation the user is.
        """
        return len(self._user_context.get_issued_queries()) / float(len(self._user_context.get_all_queries()))
    
    def is_finished(self):
        """
        Concrete implementation of the is_finished() method from the BaseLogger.
        Returns True if the user has exhausted the generated query list - no time limit.
        """
        return self._queries_exhausted