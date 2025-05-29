# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExceptionOpersOfTable:

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
        'unprocessed_opers': 'list[int]',
        'failed_opers': 'list[Fail]'
    }

    attribute_map = {
        'table_name': 'table_name',
        'unprocessed_opers': 'unprocessed_opers',
        'failed_opers': 'failed_opers'
    }

    def __init__(self, table_name=None, unprocessed_opers=None, failed_opers=None):
        r"""ExceptionOpersOfTable

        The model defined in huaweicloud sdk

        :param table_name: 表名，仓内唯一。 - 长度：[3, 63] - 取值字符限制：[a-z0-9_-]+
        :type table_name: str
        :param unprocessed_opers: 未处理的操作列表。 - 数组元素：未处理的操作标识。
        :type unprocessed_opers: list[int]
        :param failed_opers: 失败的操作列表，可以是多个。
        :type failed_opers: list[:class:`huaweicloudsdkkvs.v1.Fail`]
        """
        
        

        self._table_name = None
        self._unprocessed_opers = None
        self._failed_opers = None
        self.discriminator = None

        self.table_name = table_name
        if unprocessed_opers is not None:
            self.unprocessed_opers = unprocessed_opers
        if failed_opers is not None:
            self.failed_opers = failed_opers

    @property
    def table_name(self):
        r"""Gets the table_name of this ExceptionOpersOfTable.

        表名，仓内唯一。 - 长度：[3, 63] - 取值字符限制：[a-z0-9_-]+

        :return: The table_name of this ExceptionOpersOfTable.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        r"""Sets the table_name of this ExceptionOpersOfTable.

        表名，仓内唯一。 - 长度：[3, 63] - 取值字符限制：[a-z0-9_-]+

        :param table_name: The table_name of this ExceptionOpersOfTable.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def unprocessed_opers(self):
        r"""Gets the unprocessed_opers of this ExceptionOpersOfTable.

        未处理的操作列表。 - 数组元素：未处理的操作标识。

        :return: The unprocessed_opers of this ExceptionOpersOfTable.
        :rtype: list[int]
        """
        return self._unprocessed_opers

    @unprocessed_opers.setter
    def unprocessed_opers(self, unprocessed_opers):
        r"""Sets the unprocessed_opers of this ExceptionOpersOfTable.

        未处理的操作列表。 - 数组元素：未处理的操作标识。

        :param unprocessed_opers: The unprocessed_opers of this ExceptionOpersOfTable.
        :type unprocessed_opers: list[int]
        """
        self._unprocessed_opers = unprocessed_opers

    @property
    def failed_opers(self):
        r"""Gets the failed_opers of this ExceptionOpersOfTable.

        失败的操作列表，可以是多个。

        :return: The failed_opers of this ExceptionOpersOfTable.
        :rtype: list[:class:`huaweicloudsdkkvs.v1.Fail`]
        """
        return self._failed_opers

    @failed_opers.setter
    def failed_opers(self, failed_opers):
        r"""Sets the failed_opers of this ExceptionOpersOfTable.

        失败的操作列表，可以是多个。

        :param failed_opers: The failed_opers of this ExceptionOpersOfTable.
        :type failed_opers: list[:class:`huaweicloudsdkkvs.v1.Fail`]
        """
        self._failed_opers = failed_opers

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
        if not isinstance(other, ExceptionOpersOfTable):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
