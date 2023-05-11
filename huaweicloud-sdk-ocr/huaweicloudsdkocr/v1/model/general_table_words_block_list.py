# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GeneralTableWordsBlockList:

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
        'location': 'list[list[int]]',
        'words_list': 'list[WordsListIem]',
        'rows': 'list[int]',
        'columns': 'list[int]',
        'cell_location': 'list[list[int]]'
    }

    attribute_map = {
        'words': 'words',
        'confidence': 'confidence',
        'location': 'location',
        'words_list': 'words_list',
        'rows': 'rows',
        'columns': 'columns',
        'cell_location': 'cell_location'
    }

    def __init__(self, words=None, confidence=None, location=None, words_list=None, rows=None, columns=None, cell_location=None):
        """GeneralTableWordsBlockList

        The model defined in huaweicloud sdk

        :param words: 文字块识别结果。 
        :type words: str
        :param confidence: 字段的平均置信度，置信度越大，表示本次识别的对应字段的可靠性越高，在统计意义上，置信度越大，准确率越高。置信度由算法给出，不直接等价于对应字段的准确率。 
        :type confidence: float
        :param location: 文字块位置信息，列表形式，分别表示文字块4个顶点的x, y坐标;坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 
        :type location: list[list[int]]
        :param words_list: 单元格内文字段列表。输出顺序从左到右，从上到下。仅当入参\&quot;return_text_location\&quot;为true时存在。 
        :type words_list: list[:class:`huaweicloudsdkocr.v1.WordsListIem`]
        :param rows: 文字块占用的行信息，编号从0开始，列表形式，数据类型为Integer。仅在表格区域内有效，即type字段为\&quot;table\&quot;时该字段有效。 
        :type rows: list[int]
        :param columns: 文字块占用的列信息，编号从0开始，列表形式，数据类型为Integer。仅在表格区域内有效，即type字段为\&quot;table\&quot;时该字段有效。 
        :type columns: list[int]
        :param cell_location: 单元格位置信息，列表形式，分别表示单元格4个顶点的x, y坐标;坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 
        :type cell_location: list[list[int]]
        """
        
        

        self._words = None
        self._confidence = None
        self._location = None
        self._words_list = None
        self._rows = None
        self._columns = None
        self._cell_location = None
        self.discriminator = None

        if words is not None:
            self.words = words
        if confidence is not None:
            self.confidence = confidence
        if location is not None:
            self.location = location
        if words_list is not None:
            self.words_list = words_list
        if rows is not None:
            self.rows = rows
        if columns is not None:
            self.columns = columns
        if cell_location is not None:
            self.cell_location = cell_location

    @property
    def words(self):
        """Gets the words of this GeneralTableWordsBlockList.

        文字块识别结果。 

        :return: The words of this GeneralTableWordsBlockList.
        :rtype: str
        """
        return self._words

    @words.setter
    def words(self, words):
        """Sets the words of this GeneralTableWordsBlockList.

        文字块识别结果。 

        :param words: The words of this GeneralTableWordsBlockList.
        :type words: str
        """
        self._words = words

    @property
    def confidence(self):
        """Gets the confidence of this GeneralTableWordsBlockList.

        字段的平均置信度，置信度越大，表示本次识别的对应字段的可靠性越高，在统计意义上，置信度越大，准确率越高。置信度由算法给出，不直接等价于对应字段的准确率。 

        :return: The confidence of this GeneralTableWordsBlockList.
        :rtype: float
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this GeneralTableWordsBlockList.

        字段的平均置信度，置信度越大，表示本次识别的对应字段的可靠性越高，在统计意义上，置信度越大，准确率越高。置信度由算法给出，不直接等价于对应字段的准确率。 

        :param confidence: The confidence of this GeneralTableWordsBlockList.
        :type confidence: float
        """
        self._confidence = confidence

    @property
    def location(self):
        """Gets the location of this GeneralTableWordsBlockList.

        文字块位置信息，列表形式，分别表示文字块4个顶点的x, y坐标;坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 

        :return: The location of this GeneralTableWordsBlockList.
        :rtype: list[list[int]]
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this GeneralTableWordsBlockList.

        文字块位置信息，列表形式，分别表示文字块4个顶点的x, y坐标;坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 

        :param location: The location of this GeneralTableWordsBlockList.
        :type location: list[list[int]]
        """
        self._location = location

    @property
    def words_list(self):
        """Gets the words_list of this GeneralTableWordsBlockList.

        单元格内文字段列表。输出顺序从左到右，从上到下。仅当入参\"return_text_location\"为true时存在。 

        :return: The words_list of this GeneralTableWordsBlockList.
        :rtype: list[:class:`huaweicloudsdkocr.v1.WordsListIem`]
        """
        return self._words_list

    @words_list.setter
    def words_list(self, words_list):
        """Sets the words_list of this GeneralTableWordsBlockList.

        单元格内文字段列表。输出顺序从左到右，从上到下。仅当入参\"return_text_location\"为true时存在。 

        :param words_list: The words_list of this GeneralTableWordsBlockList.
        :type words_list: list[:class:`huaweicloudsdkocr.v1.WordsListIem`]
        """
        self._words_list = words_list

    @property
    def rows(self):
        """Gets the rows of this GeneralTableWordsBlockList.

        文字块占用的行信息，编号从0开始，列表形式，数据类型为Integer。仅在表格区域内有效，即type字段为\"table\"时该字段有效。 

        :return: The rows of this GeneralTableWordsBlockList.
        :rtype: list[int]
        """
        return self._rows

    @rows.setter
    def rows(self, rows):
        """Sets the rows of this GeneralTableWordsBlockList.

        文字块占用的行信息，编号从0开始，列表形式，数据类型为Integer。仅在表格区域内有效，即type字段为\"table\"时该字段有效。 

        :param rows: The rows of this GeneralTableWordsBlockList.
        :type rows: list[int]
        """
        self._rows = rows

    @property
    def columns(self):
        """Gets the columns of this GeneralTableWordsBlockList.

        文字块占用的列信息，编号从0开始，列表形式，数据类型为Integer。仅在表格区域内有效，即type字段为\"table\"时该字段有效。 

        :return: The columns of this GeneralTableWordsBlockList.
        :rtype: list[int]
        """
        return self._columns

    @columns.setter
    def columns(self, columns):
        """Sets the columns of this GeneralTableWordsBlockList.

        文字块占用的列信息，编号从0开始，列表形式，数据类型为Integer。仅在表格区域内有效，即type字段为\"table\"时该字段有效。 

        :param columns: The columns of this GeneralTableWordsBlockList.
        :type columns: list[int]
        """
        self._columns = columns

    @property
    def cell_location(self):
        """Gets the cell_location of this GeneralTableWordsBlockList.

        单元格位置信息，列表形式，分别表示单元格4个顶点的x, y坐标;坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 

        :return: The cell_location of this GeneralTableWordsBlockList.
        :rtype: list[list[int]]
        """
        return self._cell_location

    @cell_location.setter
    def cell_location(self, cell_location):
        """Sets the cell_location of this GeneralTableWordsBlockList.

        单元格位置信息，列表形式，分别表示单元格4个顶点的x, y坐标;坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 

        :param cell_location: The cell_location of this GeneralTableWordsBlockList.
        :type cell_location: list[list[int]]
        """
        self._cell_location = cell_location

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
        if not isinstance(other, GeneralTableWordsBlockList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
