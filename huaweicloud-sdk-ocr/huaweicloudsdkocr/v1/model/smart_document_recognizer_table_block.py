# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SmartDocumentRecognizerTableBlock:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'location': 'list[list[int]]',
        'words_block_count': 'int',
        'words_block_list': 'list[SmartDocumentRecognizerTableWordsBlock]',
        'excel': 'str'
    }

    attribute_map = {
        'location': 'location',
        'words_block_count': 'words_block_count',
        'words_block_list': 'words_block_list',
        'excel': 'excel'
    }

    def __init__(self, location=None, words_block_count=None, words_block_list=None, excel=None):
        """SmartDocumentRecognizerTableBlock

        The model defined in huaweicloud sdk

        :param location: 当前表格的位置信息，列表形式，分别表示文字块4个顶点的x, y坐标；坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 
        :type location: list[list[int]]
        :param words_block_count: 表格中所包含的单元格数量。 
        :type words_block_count: int
        :param words_block_list: 单元格识别结果列表。 
        :type words_block_list: list[:class:`huaweicloudsdkocr.v1.SmartDocumentRecognizerTableWordsBlock`]
        :param excel: 表格识别结果的base64编码，仅当return_excel为True时返回该字段。对返回的excel编码可用base64.b64decode解码并保存为.xlsx文件。 
        :type excel: str
        """
        
        

        self._location = None
        self._words_block_count = None
        self._words_block_list = None
        self._excel = None
        self.discriminator = None

        if location is not None:
            self.location = location
        if words_block_count is not None:
            self.words_block_count = words_block_count
        if words_block_list is not None:
            self.words_block_list = words_block_list
        if excel is not None:
            self.excel = excel

    @property
    def location(self):
        """Gets the location of this SmartDocumentRecognizerTableBlock.

        当前表格的位置信息，列表形式，分别表示文字块4个顶点的x, y坐标；坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 

        :return: The location of this SmartDocumentRecognizerTableBlock.
        :rtype: list[list[int]]
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this SmartDocumentRecognizerTableBlock.

        当前表格的位置信息，列表形式，分别表示文字块4个顶点的x, y坐标；坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 

        :param location: The location of this SmartDocumentRecognizerTableBlock.
        :type location: list[list[int]]
        """
        self._location = location

    @property
    def words_block_count(self):
        """Gets the words_block_count of this SmartDocumentRecognizerTableBlock.

        表格中所包含的单元格数量。 

        :return: The words_block_count of this SmartDocumentRecognizerTableBlock.
        :rtype: int
        """
        return self._words_block_count

    @words_block_count.setter
    def words_block_count(self, words_block_count):
        """Sets the words_block_count of this SmartDocumentRecognizerTableBlock.

        表格中所包含的单元格数量。 

        :param words_block_count: The words_block_count of this SmartDocumentRecognizerTableBlock.
        :type words_block_count: int
        """
        self._words_block_count = words_block_count

    @property
    def words_block_list(self):
        """Gets the words_block_list of this SmartDocumentRecognizerTableBlock.

        单元格识别结果列表。 

        :return: The words_block_list of this SmartDocumentRecognizerTableBlock.
        :rtype: list[:class:`huaweicloudsdkocr.v1.SmartDocumentRecognizerTableWordsBlock`]
        """
        return self._words_block_list

    @words_block_list.setter
    def words_block_list(self, words_block_list):
        """Sets the words_block_list of this SmartDocumentRecognizerTableBlock.

        单元格识别结果列表。 

        :param words_block_list: The words_block_list of this SmartDocumentRecognizerTableBlock.
        :type words_block_list: list[:class:`huaweicloudsdkocr.v1.SmartDocumentRecognizerTableWordsBlock`]
        """
        self._words_block_list = words_block_list

    @property
    def excel(self):
        """Gets the excel of this SmartDocumentRecognizerTableBlock.

        表格识别结果的base64编码，仅当return_excel为True时返回该字段。对返回的excel编码可用base64.b64decode解码并保存为.xlsx文件。 

        :return: The excel of this SmartDocumentRecognizerTableBlock.
        :rtype: str
        """
        return self._excel

    @excel.setter
    def excel(self, excel):
        """Sets the excel of this SmartDocumentRecognizerTableBlock.

        表格识别结果的base64编码，仅当return_excel为True时返回该字段。对返回的excel编码可用base64.b64decode解码并保存为.xlsx文件。 

        :param excel: The excel of this SmartDocumentRecognizerTableBlock.
        :type excel: str
        """
        self._excel = excel

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
        if not isinstance(other, SmartDocumentRecognizerTableBlock):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
