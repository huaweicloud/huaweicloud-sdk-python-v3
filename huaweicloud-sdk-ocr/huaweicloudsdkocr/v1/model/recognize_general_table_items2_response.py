# coding: utf-8

import pprint
import re

import six





class RecognizeGeneralTableItems2Response:


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
        'rows': 'list[int]',
        'columns': 'list[int]',
        'confidence': 'float'
    }

    attribute_map = {
        'words': 'words',
        'rows': 'rows',
        'columns': 'columns',
        'confidence': 'confidence'
    }

    def __init__(self, words=None, rows=None, columns=None, confidence=None):
        """RecognizeGeneralTableItems2Response - a model defined in huaweicloud sdk"""
        
        

        self._words = None
        self._rows = None
        self._columns = None
        self._confidence = None
        self.discriminator = None

        self.words = words
        self.rows = rows
        self.columns = columns
        self.confidence = confidence

    @property
    def words(self):
        """Gets the words of this RecognizeGeneralTableItems2Response.

        文字块识别结果。 

        :return: The words of this RecognizeGeneralTableItems2Response.
        :rtype: str
        """
        return self._words

    @words.setter
    def words(self, words):
        """Sets the words of this RecognizeGeneralTableItems2Response.

        文字块识别结果。 

        :param words: The words of this RecognizeGeneralTableItems2Response.
        :type: str
        """
        self._words = words

    @property
    def rows(self):
        """Gets the rows of this RecognizeGeneralTableItems2Response.

        文字块占用的行信息，编号从0开始，列表形式，数据类型为Integer。仅在表格区域内有效，即type字段为\"table\"时该字段有效。 

        :return: The rows of this RecognizeGeneralTableItems2Response.
        :rtype: list[int]
        """
        return self._rows

    @rows.setter
    def rows(self, rows):
        """Sets the rows of this RecognizeGeneralTableItems2Response.

        文字块占用的行信息，编号从0开始，列表形式，数据类型为Integer。仅在表格区域内有效，即type字段为\"table\"时该字段有效。 

        :param rows: The rows of this RecognizeGeneralTableItems2Response.
        :type: list[int]
        """
        self._rows = rows

    @property
    def columns(self):
        """Gets the columns of this RecognizeGeneralTableItems2Response.

        文字块占用的列信息，编号从0开始，列表形式，数据类型为Integer。仅在表格区域内有效，即type字段为\"table\"时该字段有效。 

        :return: The columns of this RecognizeGeneralTableItems2Response.
        :rtype: list[int]
        """
        return self._columns

    @columns.setter
    def columns(self, columns):
        """Sets the columns of this RecognizeGeneralTableItems2Response.

        文字块占用的列信息，编号从0开始，列表形式，数据类型为Integer。仅在表格区域内有效，即type字段为\"table\"时该字段有效。 

        :param columns: The columns of this RecognizeGeneralTableItems2Response.
        :type: list[int]
        """
        self._columns = columns

    @property
    def confidence(self):
        """Gets the confidence of this RecognizeGeneralTableItems2Response.

        字段的平均置信度，置信度越大，表示本次识别的对应字段的可靠性越高，在统计意义上，置信度越大，准确率越高。置信度由算法给出，不直接等价于对应字段的准确率。 

        :return: The confidence of this RecognizeGeneralTableItems2Response.
        :rtype: float
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this RecognizeGeneralTableItems2Response.

        字段的平均置信度，置信度越大，表示本次识别的对应字段的可靠性越高，在统计意义上，置信度越大，准确率越高。置信度由算法给出，不直接等价于对应字段的准确率。 

        :param confidence: The confidence of this RecognizeGeneralTableItems2Response.
        :type: float
        """
        self._confidence = confidence

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
        if not isinstance(other, RecognizeGeneralTableItems2Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
