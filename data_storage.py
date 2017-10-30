class DataStorage(object):

    dic_data = {}
    list_data = []

    def add_data(self, object):
        self.dic_data[object.get_userID()] = object
        return self.dic_data

    def add_to_list(self, object):
        self.list_data.append(object)
        return self.list_data
