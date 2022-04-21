# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EmbeddedDatabaseWatermark:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'watermark_content': 'str',
        'watermark_key': 'str',
        'columns': 'list[Columns]',
        'data': 'list[dict(str, object)]'
    }

    attribute_map = {
        'watermark_content': 'watermark_content',
        'watermark_key': 'watermark_key',
        'columns': 'columns',
        'data': 'data'
    }

    def __init__(self, watermark_content=None, watermark_key=None, columns=None, data=None):
        """EmbeddedDatabaseWatermark

        The model defined in huaweicloud sdk

        :param watermark_content: 添加水印的内容
        :type watermark_content: str
        :param watermark_key: 水印密钥
        :type watermark_key: str
        :param columns: 字段类型列表，最大长度100。使用时，至少包含两个字段，一个“primary_key”为true表示主键，一个为false用来嵌入水印
        :type columns: list[:class:`huaweicloudsdkdsc.v1.Columns`]
        :param data: 数据字段的内容，最大支持长度2000
        :type data: list[dict(str, object)]
        """
        
        

        self._watermark_content = None
        self._watermark_key = None
        self._columns = None
        self._data = None
        self.discriminator = None

        self.watermark_content = watermark_content
        self.watermark_key = watermark_key
        self.columns = columns
        self.data = data

    @property
    def watermark_content(self):
        """Gets the watermark_content of this EmbeddedDatabaseWatermark.

        添加水印的内容

        :return: The watermark_content of this EmbeddedDatabaseWatermark.
        :rtype: str
        """
        return self._watermark_content

    @watermark_content.setter
    def watermark_content(self, watermark_content):
        """Sets the watermark_content of this EmbeddedDatabaseWatermark.

        添加水印的内容

        :param watermark_content: The watermark_content of this EmbeddedDatabaseWatermark.
        :type watermark_content: str
        """
        self._watermark_content = watermark_content

    @property
    def watermark_key(self):
        """Gets the watermark_key of this EmbeddedDatabaseWatermark.

        水印密钥

        :return: The watermark_key of this EmbeddedDatabaseWatermark.
        :rtype: str
        """
        return self._watermark_key

    @watermark_key.setter
    def watermark_key(self, watermark_key):
        """Sets the watermark_key of this EmbeddedDatabaseWatermark.

        水印密钥

        :param watermark_key: The watermark_key of this EmbeddedDatabaseWatermark.
        :type watermark_key: str
        """
        self._watermark_key = watermark_key

    @property
    def columns(self):
        """Gets the columns of this EmbeddedDatabaseWatermark.

        字段类型列表，最大长度100。使用时，至少包含两个字段，一个“primary_key”为true表示主键，一个为false用来嵌入水印

        :return: The columns of this EmbeddedDatabaseWatermark.
        :rtype: list[:class:`huaweicloudsdkdsc.v1.Columns`]
        """
        return self._columns

    @columns.setter
    def columns(self, columns):
        """Sets the columns of this EmbeddedDatabaseWatermark.

        字段类型列表，最大长度100。使用时，至少包含两个字段，一个“primary_key”为true表示主键，一个为false用来嵌入水印

        :param columns: The columns of this EmbeddedDatabaseWatermark.
        :type columns: list[:class:`huaweicloudsdkdsc.v1.Columns`]
        """
        self._columns = columns

    @property
    def data(self):
        """Gets the data of this EmbeddedDatabaseWatermark.

        数据字段的内容，最大支持长度2000

        :return: The data of this EmbeddedDatabaseWatermark.
        :rtype: list[dict(str, object)]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this EmbeddedDatabaseWatermark.

        数据字段的内容，最大支持长度2000

        :param data: The data of this EmbeddedDatabaseWatermark.
        :type data: list[dict(str, object)]
        """
        self._data = data

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
        if not isinstance(other, EmbeddedDatabaseWatermark):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
