# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QuotaLimitInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit_key': 'str',
        'limit_values': 'list[LimitValue]'
    }

    attribute_map = {
        'limit_key': 'limit_key',
        'limit_values': 'limit_values'
    }

    def __init__(self, limit_key=None, limit_values=None):
        r"""QuotaLimitInfo

        The model defined in huaweicloud sdk

        :param limit_key: 属性key值。
        :type limit_key: str
        :param limit_values: 属性值，具体参见表3。
        :type limit_values: list[:class:`huaweicloudsdkbss.v2.LimitValue`]
        """
        
        

        self._limit_key = None
        self._limit_values = None
        self.discriminator = None

        if limit_key is not None:
            self.limit_key = limit_key
        if limit_values is not None:
            self.limit_values = limit_values

    @property
    def limit_key(self):
        r"""Gets the limit_key of this QuotaLimitInfo.

        属性key值。

        :return: The limit_key of this QuotaLimitInfo.
        :rtype: str
        """
        return self._limit_key

    @limit_key.setter
    def limit_key(self, limit_key):
        r"""Sets the limit_key of this QuotaLimitInfo.

        属性key值。

        :param limit_key: The limit_key of this QuotaLimitInfo.
        :type limit_key: str
        """
        self._limit_key = limit_key

    @property
    def limit_values(self):
        r"""Gets the limit_values of this QuotaLimitInfo.

        属性值，具体参见表3。

        :return: The limit_values of this QuotaLimitInfo.
        :rtype: list[:class:`huaweicloudsdkbss.v2.LimitValue`]
        """
        return self._limit_values

    @limit_values.setter
    def limit_values(self, limit_values):
        r"""Sets the limit_values of this QuotaLimitInfo.

        属性值，具体参见表3。

        :param limit_values: The limit_values of this QuotaLimitInfo.
        :type limit_values: list[:class:`huaweicloudsdkbss.v2.LimitValue`]
        """
        self._limit_values = limit_values

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
        if not isinstance(other, QuotaLimitInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
