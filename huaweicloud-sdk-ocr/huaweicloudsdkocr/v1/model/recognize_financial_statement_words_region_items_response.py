# coding: utf-8

import pprint
import re

import six





class RecognizeFinancialStatementWordsRegionItemsResponse:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'words_block_count': 'str',
        'words_block_list': 'list[RecognizeFinancialStatementWordsBlockItemsResponse]',
        'table_location': 'list[int]',
        'confidence': 'float'
    }

    attribute_map = {
        'type': 'type',
        'words_block_count': 'words_block_count',
        'words_block_list': 'words_block_list',
        'table_location': 'table_location',
        'confidence': 'confidence'
    }

    def __init__(self, type=None, words_block_count=None, words_block_list=None, table_location=None, confidence=None):
        """RecognizeFinancialStatementWordsRegionItemsResponse - a model defined in huaweicloud sdk"""
        
        

        self._type = None
        self._words_block_count = None
        self._words_block_list = None
        self._table_location = None
        self._confidence = None
        self.discriminator = None

        self.type = type
        self.words_block_count = words_block_count
        self.words_block_list = words_block_list
        if table_location is not None:
            self.table_location = table_location
        if confidence is not None:
            self.confidence = confidence

    @property
    def type(self):
        """Gets the type of this RecognizeFinancialStatementWordsRegionItemsResponse.

        区域属性：文本或表格。 

        :return: The type of this RecognizeFinancialStatementWordsRegionItemsResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this RecognizeFinancialStatementWordsRegionItemsResponse.

        区域属性：文本或表格。 

        :param type: The type of this RecognizeFinancialStatementWordsRegionItemsResponse.
        :type: str
        """
        self._type = type

    @property
    def words_block_count(self):
        """Gets the words_block_count of this RecognizeFinancialStatementWordsRegionItemsResponse.

        区域内文字块数目。对文本区，文字块以文本字段为单位；对表格区，文字块以单元格内所有字段为单位。 

        :return: The words_block_count of this RecognizeFinancialStatementWordsRegionItemsResponse.
        :rtype: str
        """
        return self._words_block_count

    @words_block_count.setter
    def words_block_count(self, words_block_count):
        """Sets the words_block_count of this RecognizeFinancialStatementWordsRegionItemsResponse.

        区域内文字块数目。对文本区，文字块以文本字段为单位；对表格区，文字块以单元格内所有字段为单位。 

        :param words_block_count: The words_block_count of this RecognizeFinancialStatementWordsRegionItemsResponse.
        :type: str
        """
        self._words_block_count = words_block_count

    @property
    def words_block_list(self):
        """Gets the words_block_list of this RecognizeFinancialStatementWordsRegionItemsResponse.

        区域内文字块列表，输出顺序从左到右，从上到下。 

        :return: The words_block_list of this RecognizeFinancialStatementWordsRegionItemsResponse.
        :rtype: list[RecognizeFinancialStatementWordsBlockItemsResponse]
        """
        return self._words_block_list

    @words_block_list.setter
    def words_block_list(self, words_block_list):
        """Sets the words_block_list of this RecognizeFinancialStatementWordsRegionItemsResponse.

        区域内文字块列表，输出顺序从左到右，从上到下。 

        :param words_block_list: The words_block_list of this RecognizeFinancialStatementWordsRegionItemsResponse.
        :type: list[RecognizeFinancialStatementWordsBlockItemsResponse]
        """
        self._words_block_list = words_block_list

    @property
    def table_location(self):
        """Gets the table_location of this RecognizeFinancialStatementWordsRegionItemsResponse.

        表格位置信息，列表形式，分别表示表格4个顶点的x, y坐标;坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 

        :return: The table_location of this RecognizeFinancialStatementWordsRegionItemsResponse.
        :rtype: list[int]
        """
        return self._table_location

    @table_location.setter
    def table_location(self, table_location):
        """Sets the table_location of this RecognizeFinancialStatementWordsRegionItemsResponse.

        表格位置信息，列表形式，分别表示表格4个顶点的x, y坐标;坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 

        :param table_location: The table_location of this RecognizeFinancialStatementWordsRegionItemsResponse.
        :type: list[int]
        """
        self._table_location = table_location

    @property
    def confidence(self):
        """Gets the confidence of this RecognizeFinancialStatementWordsRegionItemsResponse.

        文字块识别结果置信度信息，置信度越大，表示本次识别的对应字段的可靠性越大，在统计意义上，置信度越大正确率越高。注：置信度由算法给出，其不直接等价于对应字段的精度。 

        :return: The confidence of this RecognizeFinancialStatementWordsRegionItemsResponse.
        :rtype: float
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this RecognizeFinancialStatementWordsRegionItemsResponse.

        文字块识别结果置信度信息，置信度越大，表示本次识别的对应字段的可靠性越大，在统计意义上，置信度越大正确率越高。注：置信度由算法给出，其不直接等价于对应字段的精度。 

        :param confidence: The confidence of this RecognizeFinancialStatementWordsRegionItemsResponse.
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
        if not isinstance(other, RecognizeFinancialStatementWordsRegionItemsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
