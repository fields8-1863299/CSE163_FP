"""
Contains test methods to verify results in plots file
"""


from process_files import getDF_A as getDFA
from process_files import getDF_B as getDFB


def test_school(x):
    """
    This method takes a parameter which is the dataset
    A after its been parsed.
    This method tests the value of those who went to
    highschool for the column 2017 Total Below Poverty.
    It  returns this value.
    This value can be compared visually to our graphs to make sure
    they are correct as well as directly compare to the dataset
    """
    # for education and poverty (Dataset A)
    high_school = x[x['Category'] == 'High school, no college']
    test_high_school = high_school['2017 Total Below Poverty']
    return test_high_school


def test_no_work(x):
    """
    This method takes a parameter which is the dataset
    A after its been parsed.
    This method tests the value of those who went to
    didn't work for the column 2017 Total Below Poverty.
    It  returns this value.
    This value can be compared visually to our graphs to make sure
    they are correct as well as directly compare to the dataset
    """
    did_not_work = x[x['Category'] == 'Did not work at least 1 week']
    test_did_not_work = did_not_work['2017 Total Below Poverty']
    return test_did_not_work


def test_degree(b):
    """
    This method takes a parameter which is the dataset
    B after its been parsed.
    This method tests by giving the row "Associates" of the dataset.
    It  returns this row.
    The values in this row can be compared visually to our graphs to make sure
    they are correct as well as directly compare to the dataset
    """
    associates_degree = b[b['Degree'] == 'Associates']
    return associates_degree


def test_merging(x):
    """
    This method takes a parameter which is the dataset
    A after its been parsed.
    This method returns the values of the Category column. This will
    help to verify that the datasets merged correctly
    It  returns this column.
    This value can be compared visually to our graphs to make sure
    they are correct as well as directly compare to the dataset
    """
    columns_merge = x['Category']
    return columns_merge


def main():
    x = getDFA()
    b = getDFB()
    print(test_school(x))
    print(test_no_work(x))
    print(test_degree(b))
    print(test_merging(x))


if __name__ == '__main__':
    main()
