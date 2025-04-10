# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetKvRequestBody:

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
        'primary_key': 'dict'
    }

    attribute_map = {
        'table_name': 'table_name',
        'primary_key': 'primary_key'
    }

    def __init__(self, table_name=None, primary_key=None):
        r"""GetKvRequestBody

        The model defined in huaweicloud sdk

        :param table_name: 表名，仓内唯一。 - 长度：[3, 63] - 取值字符限制：[a-z0-9_-]+
        :type table_name: str
        :param primary_key: 用户自定义的主键名及值。
        :type primary_key: dict
        """
        
        

        self._table_name = None
        self._primary_key = None
        self.discriminator = None

        self.table_name = table_name
        self.primary_key = primary_key

    @property
    def table_name(self):
        r"""Gets the table_name of this GetKvRequestBody.

        表名，仓内唯一。 - 长度：[3, 63] - 取值字符限制：[a-z0-9_-]+

        :return: The table_name of this GetKvRequestBody.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        r"""Sets the table_name of this GetKvRequestBody.

        表名，仓内唯一。 - 长度：[3, 63] - 取值字符限制：[a-z0-9_-]+

        :param table_name: The table_name of this GetKvRequestBody.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def primary_key(self):
        r"""Gets the primary_key of this GetKvRequestBody.

        用户自定义的主键名及值。

        :return: The primary_key of this GetKvRequestBody.
        :rtype: dict
        """
        return self._primary_key

    @primary_key.setter
    def primary_key(self, primary_key):
        r"""Sets the primary_key of this GetKvRequestBody.

        用户自定义的主键名及值。

        :param primary_key: The primary_key of this GetKvRequestBody.
        :type primary_key: dict
        """
        self._primary_key = primary_key

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
        if not isinstance(other, GetKvRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
