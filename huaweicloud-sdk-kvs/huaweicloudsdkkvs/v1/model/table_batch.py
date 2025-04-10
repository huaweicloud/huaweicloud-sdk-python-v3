# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TableBatch:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'table_name': 'str',
        'kv_opers': 'list[OperItem]'
    }

    attribute_map = {
        'table_name': 'table_name',
        'kv_opers': 'kv_opers'
    }

    def __init__(self, table_name=None, kv_opers=None):
        r"""TableBatch

        The model defined in huaweicloud sdk

        :param table_name: 表名，仓内唯一。 - 长度：[3, 63] - 取值字符限制：[a-z0-9_-]+
        :type table_name: str
        :param kv_opers: kv操作数组。
        :type kv_opers: list[:class:`huaweicloudsdkkvs.v1.OperItem`]
        """
        
        

        self._table_name = None
        self._kv_opers = None
        self.discriminator = None

        self.table_name = table_name
        self.kv_opers = kv_opers

    @property
    def table_name(self):
        r"""Gets the table_name of this TableBatch.

        表名，仓内唯一。 - 长度：[3, 63] - 取值字符限制：[a-z0-9_-]+

        :return: The table_name of this TableBatch.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        r"""Sets the table_name of this TableBatch.

        表名，仓内唯一。 - 长度：[3, 63] - 取值字符限制：[a-z0-9_-]+

        :param table_name: The table_name of this TableBatch.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def kv_opers(self):
        r"""Gets the kv_opers of this TableBatch.

        kv操作数组。

        :return: The kv_opers of this TableBatch.
        :rtype: list[:class:`huaweicloudsdkkvs.v1.OperItem`]
        """
        return self._kv_opers

    @kv_opers.setter
    def kv_opers(self, kv_opers):
        r"""Sets the kv_opers of this TableBatch.

        kv操作数组。

        :param kv_opers: The kv_opers of this TableBatch.
        :type kv_opers: list[:class:`huaweicloudsdkkvs.v1.OperItem`]
        """
        self._kv_opers = kv_opers

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
        if not isinstance(other, TableBatch):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
