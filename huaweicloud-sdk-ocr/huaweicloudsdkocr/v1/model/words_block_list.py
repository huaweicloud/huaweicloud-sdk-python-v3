# coding: utf-8

import pprint
import re

import six





class WordsBlockList:


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
        'words_list': 'list[object]',
        'rows': 'list[int]',
        'columns': 'list[int]',
        'location': 'list[object]',
        'cell_location': 'list[object]',
        'confidence': 'float',
        'excel': 'str'
    }

    attribute_map = {
        'words': 'words',
        'words_list': 'words_list',
        'rows': 'rows',
        'columns': 'columns',
        'location': 'location',
        'cell_location': 'cell_location',
        'confidence': 'confidence',
        'excel': 'excel'
    }

    def __init__(self, words=None, words_list=None, rows=None, columns=None, location=None, cell_location=None, confidence=None, excel=None):
        """WordsBlockList - a model defined in huaweicloud sdk"""
        
        

        self._words = None
        self._words_list = None
        self._rows = None
        self._columns = None
        self._location = None
        self._cell_location = None
        self._confidence = None
        self._excel = None
        self.discriminator = None

        self.words = words
        if words_list is not None:
            self.words_list = words_list
        self.rows = rows
        self.columns = columns
        if location is not None:
            self.location = location
        if cell_location is not None:
            self.cell_location = cell_location
        self.confidence = confidence
        if excel is not None:
            self.excel = excel

    @property
    def words(self):
        """Gets the words of this WordsBlockList.

        文字块识别结果。 

        :return: The words of this WordsBlockList.
        :rtype: str
        """
        return self._words

    @words.setter
    def words(self, words):
        """Sets the words of this WordsBlockList.

        文字块识别结果。 

        :param words: The words of this WordsBlockList.
        :type: str
        """
        self._words = words

    @property
    def words_list(self):
        """Gets the words_list of this WordsBlockList.

        单元格内文字段列表。输出顺序从左到右，从上到下。仅当入参\"return_text_location\"为true时存在。 

        :return: The words_list of this WordsBlockList.
        :rtype: list[object]
        """
        return self._words_list

    @words_list.setter
    def words_list(self, words_list):
        """Sets the words_list of this WordsBlockList.

        单元格内文字段列表。输出顺序从左到右，从上到下。仅当入参\"return_text_location\"为true时存在。 

        :param words_list: The words_list of this WordsBlockList.
        :type: list[object]
        """
        self._words_list = words_list

    @property
    def rows(self):
        """Gets the rows of this WordsBlockList.

        文字块占用的行信息，编号从0开始，列表形式，数据类型为Integer。仅在表格区域内有效，即type字段为\"table\"时该字段有效。 

        :return: The rows of this WordsBlockList.
        :rtype: list[int]
        """
        return self._rows

    @rows.setter
    def rows(self, rows):
        """Sets the rows of this WordsBlockList.

        文字块占用的行信息，编号从0开始，列表形式，数据类型为Integer。仅在表格区域内有效，即type字段为\"table\"时该字段有效。 

        :param rows: The rows of this WordsBlockList.
        :type: list[int]
        """
        self._rows = rows

    @property
    def columns(self):
        """Gets the columns of this WordsBlockList.

        文字块占用的列信息，编号从0开始，列表形式，数据类型为Integer。仅在表格区域内有效，即type字段为\"table\"时该字段有效。 

        :return: The columns of this WordsBlockList.
        :rtype: list[int]
        """
        return self._columns

    @columns.setter
    def columns(self, columns):
        """Sets the columns of this WordsBlockList.

        文字块占用的列信息，编号从0开始，列表形式，数据类型为Integer。仅在表格区域内有效，即type字段为\"table\"时该字段有效。 

        :param columns: The columns of this WordsBlockList.
        :type: list[int]
        """
        self._columns = columns

    @property
    def location(self):
        """Gets the location of this WordsBlockList.

        文字块位置信息，列表形式，分别表示文字块4个顶点的x, y坐标;坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 

        :return: The location of this WordsBlockList.
        :rtype: list[object]
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this WordsBlockList.

        文字块位置信息，列表形式，分别表示文字块4个顶点的x, y坐标;坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 

        :param location: The location of this WordsBlockList.
        :type: list[object]
        """
        self._location = location

    @property
    def cell_location(self):
        """Gets the cell_location of this WordsBlockList.

        单元格位置信息，列表形式，分别表示单元格4个顶点的x, y坐标;坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 

        :return: The cell_location of this WordsBlockList.
        :rtype: list[object]
        """
        return self._cell_location

    @cell_location.setter
    def cell_location(self, cell_location):
        """Sets the cell_location of this WordsBlockList.

        单元格位置信息，列表形式，分别表示单元格4个顶点的x, y坐标;坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 

        :param cell_location: The cell_location of this WordsBlockList.
        :type: list[object]
        """
        self._cell_location = cell_location

    @property
    def confidence(self):
        """Gets the confidence of this WordsBlockList.

        字段的平均置信度，置信度越大，表示本次识别的对应字段的可靠性越高，在统计意义上，置信度越大，准确率越高。置信度由算法给出，不直接等价于对应字段的准确率。 

        :return: The confidence of this WordsBlockList.
        :rtype: float
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this WordsBlockList.

        字段的平均置信度，置信度越大，表示本次识别的对应字段的可靠性越高，在统计意义上，置信度越大，准确率越高。置信度由算法给出，不直接等价于对应字段的准确率。 

        :param confidence: The confidence of this WordsBlockList.
        :type: float
        """
        self._confidence = confidence

    @property
    def excel(self):
        """Gets the excel of this WordsBlockList.

        表格图像转换为excel的base64编码，图像中的文字和表格按位置写入excel。对返回的excel编码可用base64.b64decode解码并保存为.xlsx文件。 

        :return: The excel of this WordsBlockList.
        :rtype: str
        """
        return self._excel

    @excel.setter
    def excel(self, excel):
        """Sets the excel of this WordsBlockList.

        表格图像转换为excel的base64编码，图像中的文字和表格按位置写入excel。对返回的excel编码可用base64.b64decode解码并保存为.xlsx文件。 

        :param excel: The excel of this WordsBlockList.
        :type: str
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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, WordsBlockList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
