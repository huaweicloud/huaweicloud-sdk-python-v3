# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FinancialStatementWordsRegionList:

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
        'words_block_count': 'float',
        'table_location': 'list[list[int]]',
        'words_block_list': 'list[FinancialStatementWordsBlockList]'
    }

    attribute_map = {
        'type': 'type',
        'words_block_count': 'words_block_count',
        'table_location': 'table_location',
        'words_block_list': 'words_block_list'
    }

    def __init__(self, type=None, words_block_count=None, table_location=None, words_block_list=None):
        """FinancialStatementWordsRegionList

        The model defined in huaweicloud sdk

        :param type: 区域属性：文本或表格。 
        :type type: str
        :param words_block_count: 区域内文字块数目。对文本区，文字块以文本字段为单位；对表格区，文字块以单元格内所有字段为单位。 
        :type words_block_count: float
        :param table_location: 表格位置信息，列表形式，分别表示表格4个顶点的x, y坐标;坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 
        :type table_location: list[list[int]]
        :param words_block_list: 区域内文字块列表，输出顺序从左到右，从上到下。 
        :type words_block_list: list[:class:`huaweicloudsdkocr.v1.FinancialStatementWordsBlockList`]
        """
        
        

        self._type = None
        self._words_block_count = None
        self._table_location = None
        self._words_block_list = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if words_block_count is not None:
            self.words_block_count = words_block_count
        if table_location is not None:
            self.table_location = table_location
        if words_block_list is not None:
            self.words_block_list = words_block_list

    @property
    def type(self):
        """Gets the type of this FinancialStatementWordsRegionList.

        区域属性：文本或表格。 

        :return: The type of this FinancialStatementWordsRegionList.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this FinancialStatementWordsRegionList.

        区域属性：文本或表格。 

        :param type: The type of this FinancialStatementWordsRegionList.
        :type type: str
        """
        self._type = type

    @property
    def words_block_count(self):
        """Gets the words_block_count of this FinancialStatementWordsRegionList.

        区域内文字块数目。对文本区，文字块以文本字段为单位；对表格区，文字块以单元格内所有字段为单位。 

        :return: The words_block_count of this FinancialStatementWordsRegionList.
        :rtype: float
        """
        return self._words_block_count

    @words_block_count.setter
    def words_block_count(self, words_block_count):
        """Sets the words_block_count of this FinancialStatementWordsRegionList.

        区域内文字块数目。对文本区，文字块以文本字段为单位；对表格区，文字块以单元格内所有字段为单位。 

        :param words_block_count: The words_block_count of this FinancialStatementWordsRegionList.
        :type words_block_count: float
        """
        self._words_block_count = words_block_count

    @property
    def table_location(self):
        """Gets the table_location of this FinancialStatementWordsRegionList.

        表格位置信息，列表形式，分别表示表格4个顶点的x, y坐标;坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 

        :return: The table_location of this FinancialStatementWordsRegionList.
        :rtype: list[list[int]]
        """
        return self._table_location

    @table_location.setter
    def table_location(self, table_location):
        """Sets the table_location of this FinancialStatementWordsRegionList.

        表格位置信息，列表形式，分别表示表格4个顶点的x, y坐标;坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 

        :param table_location: The table_location of this FinancialStatementWordsRegionList.
        :type table_location: list[list[int]]
        """
        self._table_location = table_location

    @property
    def words_block_list(self):
        """Gets the words_block_list of this FinancialStatementWordsRegionList.

        区域内文字块列表，输出顺序从左到右，从上到下。 

        :return: The words_block_list of this FinancialStatementWordsRegionList.
        :rtype: list[:class:`huaweicloudsdkocr.v1.FinancialStatementWordsBlockList`]
        """
        return self._words_block_list

    @words_block_list.setter
    def words_block_list(self, words_block_list):
        """Sets the words_block_list of this FinancialStatementWordsRegionList.

        区域内文字块列表，输出顺序从左到右，从上到下。 

        :param words_block_list: The words_block_list of this FinancialStatementWordsRegionList.
        :type words_block_list: list[:class:`huaweicloudsdkocr.v1.FinancialStatementWordsBlockList`]
        """
        self._words_block_list = words_block_list

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
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, FinancialStatementWordsRegionList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
