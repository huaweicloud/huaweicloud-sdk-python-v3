# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SmartDocumentRecognizerTableWordsBlock:

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
        'columns': 'list[int]'
    }

    attribute_map = {
        'words': 'words',
        'rows': 'rows',
        'columns': 'columns'
    }

    def __init__(self, words=None, rows=None, columns=None):
        r"""SmartDocumentRecognizerTableWordsBlock

        The model defined in huaweicloud sdk

        :param words: 单元格内的文字识别结果。 
        :type words: str
        :param rows: 文字块占用的行信息，编号从0开始，列表形式，数据类型为Integer。 
        :type rows: list[int]
        :param columns: 文字块占用的列信息，编号从0开始，列表形式，数据类型为Integer。 
        :type columns: list[int]
        """
        
        

        self._words = None
        self._rows = None
        self._columns = None
        self.discriminator = None

        if words is not None:
            self.words = words
        if rows is not None:
            self.rows = rows
        if columns is not None:
            self.columns = columns

    @property
    def words(self):
        r"""Gets the words of this SmartDocumentRecognizerTableWordsBlock.

        单元格内的文字识别结果。 

        :return: The words of this SmartDocumentRecognizerTableWordsBlock.
        :rtype: str
        """
        return self._words

    @words.setter
    def words(self, words):
        r"""Sets the words of this SmartDocumentRecognizerTableWordsBlock.

        单元格内的文字识别结果。 

        :param words: The words of this SmartDocumentRecognizerTableWordsBlock.
        :type words: str
        """
        self._words = words

    @property
    def rows(self):
        r"""Gets the rows of this SmartDocumentRecognizerTableWordsBlock.

        文字块占用的行信息，编号从0开始，列表形式，数据类型为Integer。 

        :return: The rows of this SmartDocumentRecognizerTableWordsBlock.
        :rtype: list[int]
        """
        return self._rows

    @rows.setter
    def rows(self, rows):
        r"""Sets the rows of this SmartDocumentRecognizerTableWordsBlock.

        文字块占用的行信息，编号从0开始，列表形式，数据类型为Integer。 

        :param rows: The rows of this SmartDocumentRecognizerTableWordsBlock.
        :type rows: list[int]
        """
        self._rows = rows

    @property
    def columns(self):
        r"""Gets the columns of this SmartDocumentRecognizerTableWordsBlock.

        文字块占用的列信息，编号从0开始，列表形式，数据类型为Integer。 

        :return: The columns of this SmartDocumentRecognizerTableWordsBlock.
        :rtype: list[int]
        """
        return self._columns

    @columns.setter
    def columns(self, columns):
        r"""Sets the columns of this SmartDocumentRecognizerTableWordsBlock.

        文字块占用的列信息，编号从0开始，列表形式，数据类型为Integer。 

        :param columns: The columns of this SmartDocumentRecognizerTableWordsBlock.
        :type columns: list[int]
        """
        self._columns = columns

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
        if not isinstance(other, SmartDocumentRecognizerTableWordsBlock):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
