import collections

#TODO: definitely needs to be tested
#TODO: this method is doin more than just sorting, should be broken out
def sort_repo_data(repo_data):
    repo_data_sorted = []
    for data_item in range(len(repo_data)):
        #sorts the dict into a tuple
        repo_data_sorted.append(sorted(repo_data[data_item].items(), key=lambda x: x[1], reverse=True))

        #To maintain sorted nature of the values we use the OrderedDict
        repo_data_sorted_dict = collections.OrderedDict()
    
    #TODO: using array indices is not semantic and is a code smell. Need to remove
    repo_data_sorted_dict = {'Stars': repo_data_sorted[0], 'Forks': repo_data_sorted[1], 'Contributors': repo_data_sorted[2]}
    return repo_data_sorted_dict