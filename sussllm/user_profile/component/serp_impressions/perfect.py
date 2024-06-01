from sussllm.search.interfaces import Document
from sussllm.user_profile.component.serp_impressions.base import BaseSERPImpression

class PerfectSERPImpression(BaseSERPImpression):
    """
    A SERP impression component that has access to TREC QRELS.
    From this information, the component is able to make a "perfect" judgement about the attractiveness of a SERP.
    If the precision is above the specified precision threshold, then it is attractive; else it is unattractive.
    """
    def __init__(self,
                 user_context,
                 qrel_file,
                 host=None,
                 port=None,
                 viewport_precision_threshold=0.1):
        super(PerfectSERPImpression, self).__init__(user_context=user_context,
                                                       qrel_file=qrel_file,
                                                       host=host,
                                                       port=port)
        
        self.__viewport_precision_threshold = viewport_precision_threshold
    
    
    def is_serp_attractive(self):
        """
        Determines whether the SERP is sufficiently attractive enough to enter.
        Uses "perfect judgements", that is, judgements from the TREC QRELS.
        """
        # Work out the patch type first, using code from the base (SimpleSERPImpression) class.
        judgements = self._get_patch_judgements()
        patch_type = self._calculate_patch_type(judgements)
        self._set_query_patch_type(patch_type)
        
        results_len = self._user_context.get_current_results_length()
        results_list = self._user_context.get_current_results()
        judged_precision = sum(judgements) / float(len(judgements))
        
        if judged_precision <= self.__viewport_precision_threshold:
            # We have a poor quality SERP.
            return False
        
        # If we get here, the SERP will be of quality good enough to enter.
        return True