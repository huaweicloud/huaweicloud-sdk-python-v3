# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TokensQuota:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'used': 'int',
        'expire_time': 'datetime'
    }

    attribute_map = {
        'total': 'total',
        'used': 'used',
        'expire_time': 'expire_time'
    }

    def __init__(self, total=None, used=None, expire_time=None):
        r"""TokensQuota

        The model defined in huaweicloud sdk

        :param total: 总配额。
        :type total: int
        :param used: 已使用配额。
        :type used: int
        :param expire_time: **参数解释**：到期时间。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。 
        :type expire_time: datetime
        """
        
        

        self._total = None
        self._used = None
        self._expire_time = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if used is not None:
            self.used = used
        if expire_time is not None:
            self.expire_time = expire_time

    @property
    def total(self):
        r"""Gets the total of this TokensQuota.

        总配额。

        :return: The total of this TokensQuota.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this TokensQuota.

        总配额。

        :param total: The total of this TokensQuota.
        :type total: int
        """
        self._total = total

    @property
    def used(self):
        r"""Gets the used of this TokensQuota.

        已使用配额。

        :return: The used of this TokensQuota.
        :rtype: int
        """
        return self._used

    @used.setter
    def used(self, used):
        r"""Sets the used of this TokensQuota.

        已使用配额。

        :param used: The used of this TokensQuota.
        :type used: int
        """
        self._used = used

    @property
    def expire_time(self):
        r"""Gets the expire_time of this TokensQuota.

        **参数解释**：到期时间。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。 

        :return: The expire_time of this TokensQuota.
        :rtype: datetime
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        r"""Sets the expire_time of this TokensQuota.

        **参数解释**：到期时间。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。 

        :param expire_time: The expire_time of this TokensQuota.
        :type expire_time: datetime
        """
        self._expire_time = expire_time

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TokensQuota):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
