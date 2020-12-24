# coding: utf-8

import pprint
import re

import six





class RecognizeFinancialStatementWordsListItemsResponse:


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
        'confidence': 'float',
        'location': 'list[int]'
    }

    attribute_map = {
        'words': 'words',
        'confidence': 'confidence',
        'location': 'location'
    }

    def __init__(self, words=None, confidence=None, location=None):
        """RecognizeFinancialStatementWordsListItemsResponse - a model defined in huaweicloud sdk"""
        
        

        self._words = None
        self._confidence = None
        self._location = None
        self.discriminator = None

        self.words = words
        self.confidence = confidence
        self.location = location

    @property
    def words(self):
        """Gets the words of this RecognizeFinancialStatementWordsListItemsResponse.

        区域属性：文本或表格。 

        :return: The words of this RecognizeFinancialStatementWordsListItemsResponse.
        :rtype: str
        """
        return self._words

    @words.setter
    def words(self, words):
        """Sets the words of this RecognizeFinancialStatementWordsListItemsResponse.

        区域属性：文本或表格。 

        :param words: The words of this RecognizeFinancialStatementWordsListItemsResponse.
        :type: str
        """
        self._words = words

    @property
    def confidence(self):
        """Gets the confidence of this RecognizeFinancialStatementWordsListItemsResponse.

        区域内文字块数目。对文本区，文字块以文本字段为单位；对表格区，文字块以单元格内所有字段为单位。 

        :return: The confidence of this RecognizeFinancialStatementWordsListItemsResponse.
        :rtype: float
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this RecognizeFinancialStatementWordsListItemsResponse.

        区域内文字块数目。对文本区，文字块以文本字段为单位；对表格区，文字块以单元格内所有字段为单位。 

        :param confidence: The confidence of this RecognizeFinancialStatementWordsListItemsResponse.
        :type: float
        """
        self._confidence = confidence

    @property
    def location(self):
        """Gets the location of this RecognizeFinancialStatementWordsListItemsResponse.

        文字块信息。 

        :return: The location of this RecognizeFinancialStatementWordsListItemsResponse.
        :rtype: list[int]
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this RecognizeFinancialStatementWordsListItemsResponse.

        文字块信息。 

        :param location: The location of this RecognizeFinancialStatementWordsListItemsResponse.
        :type: list[int]
        """
        self._location = location

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
        if not isinstance(other, RecognizeFinancialStatementWordsListItemsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
