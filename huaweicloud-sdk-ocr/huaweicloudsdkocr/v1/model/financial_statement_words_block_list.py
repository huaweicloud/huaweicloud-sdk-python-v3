# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FinancialStatementWordsBlockList:

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
        'location': 'list[list[int]]',
        'confidence': 'float',
        'rows': 'list[int]',
        'columns': 'list[int]',
        'cell_location': 'list[list[int]]'
    }

    attribute_map = {
        'words': 'words',
        'location': 'location',
        'confidence': 'confidence',
        'rows': 'rows',
        'columns': 'columns',
        'cell_location': 'cell_location'
    }

    def __init__(self, words=None, location=None, confidence=None, rows=None, columns=None, cell_location=None):
        r"""FinancialStatementWordsBlockList

        The model defined in huaweicloud sdk

        :param words: 文字块内容。当入参\&quot;return_text_location\&quot;为false时，每个单元格返回一个文本值，不同行文本由换行符 \&quot;\\n\&quot; 拼接。 
        :type words: str
        :param location: 文字块位置信息，列表形式，分别表示文字块4个顶点的x, y坐标;坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 
        :type location: list[list[int]]
        :param confidence: 文字块识别结果置信度信息，置信度越大，表示本次识别的对应字段的可靠性越大，在统计意义上，置信度越大正确率越高。注：置信度由算法给出，其不直接等价于对应字段的精度。 
        :type confidence: float
        :param rows: 单元格行信息，列表形式。多个连续值表示单元格垮多行。 
        :type rows: list[int]
        :param columns: 单元格列信息，列表形式。多个连续值表示单元格垮多列。 
        :type columns: list[int]
        :param cell_location: 单元格位置信息，列表形式，分别表示单元格4个顶点的x, y坐标;坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 
        :type cell_location: list[list[int]]
        """
        
        

        self._words = None
        self._location = None
        self._confidence = None
        self._rows = None
        self._columns = None
        self._cell_location = None
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

    @property
    def words(self):
        r"""Gets the words of this FinancialStatementWordsBlockList.

        文字块内容。当入参\"return_text_location\"为false时，每个单元格返回一个文本值，不同行文本由换行符 \"\\n\" 拼接。 

        :return: The words of this FinancialStatementWordsBlockList.
        :rtype: str
        """
        return self._words

    @words.setter
    def words(self, words):
        r"""Sets the words of this FinancialStatementWordsBlockList.

        文字块内容。当入参\"return_text_location\"为false时，每个单元格返回一个文本值，不同行文本由换行符 \"\\n\" 拼接。 

        :param words: The words of this FinancialStatementWordsBlockList.
        :type words: str
        """
        self._words = words

    @property
    def location(self):
        r"""Gets the location of this FinancialStatementWordsBlockList.

        文字块位置信息，列表形式，分别表示文字块4个顶点的x, y坐标;坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 

        :return: The location of this FinancialStatementWordsBlockList.
        :rtype: list[list[int]]
        """
        return self._location

    @location.setter
    def location(self, location):
        r"""Sets the location of this FinancialStatementWordsBlockList.

        文字块位置信息，列表形式，分别表示文字块4个顶点的x, y坐标;坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 

        :param location: The location of this FinancialStatementWordsBlockList.
        :type location: list[list[int]]
        """
        self._location = location

    @property
    def confidence(self):
        r"""Gets the confidence of this FinancialStatementWordsBlockList.

        文字块识别结果置信度信息，置信度越大，表示本次识别的对应字段的可靠性越大，在统计意义上，置信度越大正确率越高。注：置信度由算法给出，其不直接等价于对应字段的精度。 

        :return: The confidence of this FinancialStatementWordsBlockList.
        :rtype: float
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        r"""Sets the confidence of this FinancialStatementWordsBlockList.

        文字块识别结果置信度信息，置信度越大，表示本次识别的对应字段的可靠性越大，在统计意义上，置信度越大正确率越高。注：置信度由算法给出，其不直接等价于对应字段的精度。 

        :param confidence: The confidence of this FinancialStatementWordsBlockList.
        :type confidence: float
        """
        self._confidence = confidence

    @property
    def rows(self):
        r"""Gets the rows of this FinancialStatementWordsBlockList.

        单元格行信息，列表形式。多个连续值表示单元格垮多行。 

        :return: The rows of this FinancialStatementWordsBlockList.
        :rtype: list[int]
        """
        return self._rows

    @rows.setter
    def rows(self, rows):
        r"""Sets the rows of this FinancialStatementWordsBlockList.

        单元格行信息，列表形式。多个连续值表示单元格垮多行。 

        :param rows: The rows of this FinancialStatementWordsBlockList.
        :type rows: list[int]
        """
        self._rows = rows

    @property
    def columns(self):
        r"""Gets the columns of this FinancialStatementWordsBlockList.

        单元格列信息，列表形式。多个连续值表示单元格垮多列。 

        :return: The columns of this FinancialStatementWordsBlockList.
        :rtype: list[int]
        """
        return self._columns

    @columns.setter
    def columns(self, columns):
        r"""Sets the columns of this FinancialStatementWordsBlockList.

        单元格列信息，列表形式。多个连续值表示单元格垮多列。 

        :param columns: The columns of this FinancialStatementWordsBlockList.
        :type columns: list[int]
        """
        self._columns = columns

    @property
    def cell_location(self):
        r"""Gets the cell_location of this FinancialStatementWordsBlockList.

        单元格位置信息，列表形式，分别表示单元格4个顶点的x, y坐标;坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 

        :return: The cell_location of this FinancialStatementWordsBlockList.
        :rtype: list[list[int]]
        """
        return self._cell_location

    @cell_location.setter
    def cell_location(self, cell_location):
        r"""Sets the cell_location of this FinancialStatementWordsBlockList.

        单元格位置信息，列表形式，分别表示单元格4个顶点的x, y坐标;坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 

        :param cell_location: The cell_location of this FinancialStatementWordsBlockList.
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
        if not isinstance(other, FinancialStatementWordsBlockList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
