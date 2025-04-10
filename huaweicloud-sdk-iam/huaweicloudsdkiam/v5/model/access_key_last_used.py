# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AccessKeyLastUsed:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'last_used_at': 'datetime'
    }

    attribute_map = {
        'last_used_at': 'last_used_at'
    }

    def __init__(self, last_used_at=None):
        r"""AccessKeyLastUsed

        The model defined in huaweicloud sdk

        :param last_used_at: 访问密钥的最后使用时间。若不存在则表示从未使用过。
        :type last_used_at: datetime
        """
        
        

        self._last_used_at = None
        self.discriminator = None

        if last_used_at is not None:
            self.last_used_at = last_used_at

    @property
    def last_used_at(self):
        r"""Gets the last_used_at of this AccessKeyLastUsed.

        访问密钥的最后使用时间。若不存在则表示从未使用过。

        :return: The last_used_at of this AccessKeyLastUsed.
        :rtype: datetime
        """
        return self._last_used_at

    @last_used_at.setter
    def last_used_at(self, last_used_at):
        r"""Sets the last_used_at of this AccessKeyLastUsed.

        访问密钥的最后使用时间。若不存在则表示从未使用过。

        :param last_used_at: The last_used_at of this AccessKeyLastUsed.
        :type last_used_at: datetime
        """
        self._last_used_at = last_used_at

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
        if not isinstance(other, AccessKeyLastUsed):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
