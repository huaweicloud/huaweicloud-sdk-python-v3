# coding: utf-8

import pprint
import re

import six





class RecognizeFinancialStatementWordsBlockItemsResponse:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'words': 'str',
        'location': 'list[int]',
        'confidence': 'float',
        'rows': 'list[int]',
        'columns': 'list[int]',
        'cell_location': 'list[int]',
        'words_list': 'list[RecognizeFinancialStatementWordsListItemsResponse]'
    }

    attribute_map = {
        'words': 'words',
        'location': 'location',
        'confidence': 'confidence',
        'rows': 'rows',
        'columns': 'columns',
        'cell_location': 'cell_location',
        'words_list': 'words_list'
    }

    def __init__(self, words=None, location=None, confidence=None, rows=None, columns=None, cell_location=None, words_list=None):
        """RecognizeFinancialStatementWordsBlockItemsResponse - a model defined in huaweicloud sdk"""
        
        

        self._words = None
        self._location = None
        self._confidence = None
        self._rows = None
        self._columns = None
        self._cell_location = None
        self._words_list = None
        self.discriminator = None

        if words is not None:
            self.words = words
        if location is not None:
            self.location = location
        if confidence is not None:
            self.confidence = confidence
        if rows is not None:
            self.rows = rows
        if columns is not None:
            self.columns = columns
        if cell_location is not None:
            self.cell_location = cell_location
        if words_list is not None:
            self.words_list = words_list

    @property
    def words(self):
        """Gets the words of this RecognizeFinancialStatementWordsBlockItemsResponse.

        文字块内容。当入参\"return_text_location\"为false时，每个单元格返回一个文本值，不同行文本由换行符 \"\\n\" 拼接。 

        :return: The words of this RecognizeFinancialStatementWordsBlockItemsResponse.
        :rtype: str
        """
        return self._words

    @words.setter
    def words(self, words):
        """Sets the words of this RecognizeFinancialStatementWordsBlockItemsResponse.

        文字块内容。当入参\"return_text_location\"为false时，每个单元格返回一个文本值，不同行文本由换行符 \"\\n\" 拼接。 

        :param words: The words of this RecognizeFinancialStatementWordsBlockItemsResponse.
        :type: str
        """
        self._words = words

    @property
    def location(self):
        """Gets the location of this RecognizeFinancialStatementWordsBlockItemsResponse.

        文字块信息。 

        :return: The location of this RecognizeFinancialStatementWordsBlockItemsResponse.
        :rtype: list[int]
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this RecognizeFinancialStatementWordsBlockItemsResponse.

        文字块信息。 

        :param location: The location of this RecognizeFinancialStatementWordsBlockItemsResponse.
        :type: list[int]
        """
        self._location = location

    @property
    def confidence(self):
        """Gets the confidence of this RecognizeFinancialStatementWordsBlockItemsResponse.

        文字块识别结果置信度信息，置信度越大，表示本次识别的对应字段的可靠性越大，在统计意义上，置信度越大正确率越高。注：置信度由算法给出，其不直接等价于对应字段的精度。 

        :return: The confidence of this RecognizeFinancialStatementWordsBlockItemsResponse.
        :rtype: float
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this RecognizeFinancialStatementWordsBlockItemsResponse.

        文字块识别结果置信度信息，置信度越大，表示本次识别的对应字段的可靠性越大，在统计意义上，置信度越大正确率越高。注：置信度由算法给出，其不直接等价于对应字段的精度。 

        :param confidence: The confidence of this RecognizeFinancialStatementWordsBlockItemsResponse.
        :type: float
        """
        self._confidence = confidence

    @property
    def rows(self):
        """Gets the rows of this RecognizeFinancialStatementWordsBlockItemsResponse.

        单元格行信息，列表形式。多个连续值表示单元格垮多行。 

        :return: The rows of this RecognizeFinancialStatementWordsBlockItemsResponse.
        :rtype: list[int]
        """
        return self._rows

    @rows.setter
    def rows(self, rows):
        """Sets the rows of this RecognizeFinancialStatementWordsBlockItemsResponse.

        单元格行信息，列表形式。多个连续值表示单元格垮多行。 

        :param rows: The rows of this RecognizeFinancialStatementWordsBlockItemsResponse.
        :type: list[int]
        """
        self._rows = rows

    @property
    def columns(self):
        """Gets the columns of this RecognizeFinancialStatementWordsBlockItemsResponse.

        单元格列信息，列表形式。多个连续值表示单元格垮多列。 

        :return: The columns of this RecognizeFinancialStatementWordsBlockItemsResponse.
        :rtype: list[int]
        """
        return self._columns

    @columns.setter
    def columns(self, columns):
        """Sets the columns of this RecognizeFinancialStatementWordsBlockItemsResponse.

        单元格列信息，列表形式。多个连续值表示单元格垮多列。 

        :param columns: The columns of this RecognizeFinancialStatementWordsBlockItemsResponse.
        :type: list[int]
        """
        self._columns = columns

    @property
    def cell_location(self):
        """Gets the cell_location of this RecognizeFinancialStatementWordsBlockItemsResponse.

        文字块信息。 

        :return: The cell_location of this RecognizeFinancialStatementWordsBlockItemsResponse.
        :rtype: list[int]
        """
        return self._cell_location

    @cell_location.setter
    def cell_location(self, cell_location):
        """Sets the cell_location of this RecognizeFinancialStatementWordsBlockItemsResponse.

        文字块信息。 

        :param cell_location: The cell_location of this RecognizeFinancialStatementWordsBlockItemsResponse.
        :type: list[int]
        """
        self._cell_location = cell_location

    @property
    def words_list(self):
        """Gets the words_list of this RecognizeFinancialStatementWordsBlockItemsResponse.

        文字块信息。 

        :return: The words_list of this RecognizeFinancialStatementWordsBlockItemsResponse.
        :rtype: list[RecognizeFinancialStatementWordsListItemsResponse]
        """
        return self._words_list

    @words_list.setter
    def words_list(self, words_list):
        """Sets the words_list of this RecognizeFinancialStatementWordsBlockItemsResponse.

        文字块信息。 

        :param words_list: The words_list of this RecognizeFinancialStatementWordsBlockItemsResponse.
        :type: list[RecognizeFinancialStatementWordsListItemsResponse]
        """
        self._words_list = words_list

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RecognizeFinancialStatementWordsBlockItemsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
