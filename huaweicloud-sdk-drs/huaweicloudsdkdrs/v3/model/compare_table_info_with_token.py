# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CompareTableInfoWithToken:

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
        'min_token': 'str',
        'max_token': 'str'
    }

    attribute_map = {
        'table_name': 'table_name',
        'min_token': 'min_token',
        'max_token': 'max_token'
    }

    def __init__(self, table_name=None, min_token=None, max_token=None):
        r"""CompareTableInfoWithToken

        The model defined in huaweicloud sdk

        :param table_name: 表名。
        :type table_name: str
        :param min_token: 该表的min token。
        :type min_token: str
        :param max_token: 该表的max token。
        :type max_token: str
        """
        
        

        self._table_name = None
        self._min_token = None
        self._max_token = None
        self.discriminator = None

        self.table_name = table_name
        if min_token is not None:
            self.min_token = min_token
        if max_token is not None:
            self.max_token = max_token

    @property
    def table_name(self):
        r"""Gets the table_name of this CompareTableInfoWithToken.

        表名。

        :return: The table_name of this CompareTableInfoWithToken.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        r"""Sets the table_name of this CompareTableInfoWithToken.

        表名。

        :param table_name: The table_name of this CompareTableInfoWithToken.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def min_token(self):
        r"""Gets the min_token of this CompareTableInfoWithToken.

        该表的min token。

        :return: The min_token of this CompareTableInfoWithToken.
        :rtype: str
        """
        return self._min_token

    @min_token.setter
    def min_token(self, min_token):
        r"""Sets the min_token of this CompareTableInfoWithToken.

        该表的min token。

        :param min_token: The min_token of this CompareTableInfoWithToken.
        :type min_token: str
        """
        self._min_token = min_token

    @property
    def max_token(self):
        r"""Gets the max_token of this CompareTableInfoWithToken.

        该表的max token。

        :return: The max_token of this CompareTableInfoWithToken.
        :rtype: str
        """
        return self._max_token

    @max_token.setter
    def max_token(self, max_token):
        r"""Sets the max_token of this CompareTableInfoWithToken.

        该表的max token。

        :param max_token: The max_token of this CompareTableInfoWithToken.
        :type max_token: str
        """
        self._max_token = max_token

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
        if not isinstance(other, CompareTableInfoWithToken):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
