import fileinput

def count_topic_occurences(topics, reviews):
    """
    :param topics: A mapping of topic name to topic keyword list.
    :type topics: dict of str -> list
    :param reviews: A list of Yelp reviews.
    :type reviews: list of str
    :return: A mapping of topic name to topic occurences in the given list of reviews.
    :rtype: dict of str -> int
    """
    # TODO: Complete me.
    out = {}
    for topic in topics.keys():
        out[topic] = 0
    sentence_index = 1
    for sentence in reviews:
        x = sentence.split(' ')
        lower_x = list(map(lambda x: x.lower(),x))
        lower_x[-1] = lower_x[-1][0:-1]
        search_index = 0
        search_words = ""
        for search_length in range(0,len(lower_x)):
            space = 0 
            for match_length in range(0, search_length +1):
                if match_length > 1:
                    for i in range(space, space + search_length):
                        search_words += " " + lower_x[i]
                
                print(search_words)
                # check
                for top in topics.keys():
                    if search_words in topics[top]:
                        out[top] = sentence_index
                search_words = ""
            space += 1
            search_index += 1
if __name__ == '__main__':