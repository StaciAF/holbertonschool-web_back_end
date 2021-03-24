#!/usr/bin/env python3
"""
module uses index_range function & Server class to implement simple pagination
"""
import csv
import math
from typing import List, Dict

index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ finds indexes to paginate and returns the corresponding pages """
        pageRange = ()
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0
        allMyData = self.dataset()
        pageRange = index_range(page, page_size)
        pageList = []
        if page * page_size > len(allMyData):
            return pageList
        for i in range(pageRange[0], pageRange[1]):
            newPage = allMyData[i]
            pageList.append(newPage)
        return pageList

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """ returns a dictionary with set keys to be given value """
        allMyData = self.dataset()
        hyperDict = {}
        dataSize = len(allMyData)
        nextPage = page + 1
        prevPage = page - 1
        totalPages = (dataSize + 1) // page_size
        if nextPage * page_size < dataSize:
            hyperDict['page_size'] = page_size
            hyperDict['page'] = page
            hyperDict['data'] = self.get_page(page, page_size)
            hyperDict['next_page'] = nextPage
            if hyperDict['page'] == 1:
                hyperDict['prev_page'] = None
            else:
                hyperDict['prev_page'] = prevPage
            hyperDict['total_pages'] = totalPages
        else:
            hyperDict['page_size'] = 0
            hyperDict['data'] = []
            hyperDict['next_page'] = None
            hyperDict['prev_page'] = prevPage
            hyperDict['total_pages'] = totalPages + 1
        return hyperDict
