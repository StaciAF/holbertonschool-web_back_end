# 0x04. Pagination

### Learning Objectives
* How to paginate a dataset with simple page and page_size parameters
* How to paginate a dataset with hypermedia metadata
* How to paginate in a deletion-resilient manner

### Tasks
#### 0. Simple helper function
  * The function should return a tuple of size two containing a start index and an end index corresponding to the range of indexes to return in a list for those particular pagination parameters.

#### 1. Simple pagination
  * Implement a method named ``get_page`` that takes two integer arguments ``page`` with default value 1 and ``page_size`` with default value 10.

#### 2. Hypermedia pagination
  * Implement a ``get_hyper`` method that takes the same arguments (and defaults) as ``get_page`` and returns a dictionary containing the following key-value pairs:

#### 3. Deletion-resilient hypermedia pagination
  * Implement a ``get_hyper_index`` method with two integer arguments: ``index`` with a ``None`` default value and ``page_size`` with default value of 10.
  * The goal here is that if between two queries, certain rows are removed from the dataset, the user does not miss items from dataset when changing page.
  