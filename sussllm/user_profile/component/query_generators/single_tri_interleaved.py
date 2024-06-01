from sussllm.user_profile.component.query_generators.base import BaseQueryGenerator

from sussllm.user_profile.component.query_generators.single_term import SingleTermQueryGenerator
from sussllm.user_profile.component.query_generators.tri_term import TriTermQueryGenerator

class SingleTriInterleavedQueryGenerator(BaseQueryGenerator):
    """
    Takes the SingleTermGenerator and the TriTermGenerator, and interleaves like [Single,Tri,Single,Tri,Single,Tri...]
    """
    def __init__(self, stopword_file, background_file=[]):
        super(SingleTriInterleavedQueryGenerator, self).__init__(stopword_file, background_file=background_file)
        self.__single = SingleTermQueryGenerator( stopword_file, background_file)
        self.__tri = TriTermQueryGenerator(stopword_file, background_file)

    def generate_query_list(self, user_context):
        """
        Given a Topic object, produces a list of query terms that could be issued by the simulated agent.
        """

        topic = user_context.topic

        single_queries = self.__single.generate_query_list(user_context)
        tri_queries = self.__tri.generate_query_list(user_context)
        
        interleaved_queries = [val for pair in zip(single_queries, tri_queries) for val in pair]
        
        return interleaved_queries