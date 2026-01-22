# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ItemInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'max_quota': 'int',
        'used_quota': 'int',
        'extras_info': 'dict(str, str)'
    }

    attribute_map = {
        'max_quota': 'max_quota',
        'used_quota': 'used_quota',
        'extras_info': 'extras_info'
    }

    def __init__(self, max_quota=None, used_quota=None, extras_info=None):
        r"""ItemInfo

        The model defined in huaweicloud sdk

        :param max_quota: **参数解释**： 最大配额 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及
        :type max_quota: int
        :param used_quota: **参数解释**： 已使用配额 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及
        :type used_quota: int
        :param extras_info: **参数解释**： 额外参数，ACL和网络域名使用 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及
        :type extras_info: dict(str, str)
        """
        
        

        self._max_quota = None
        self._used_quota = None
        self._extras_info = None
        self.discriminator = None

        if max_quota is not None:
            self.max_quota = max_quota
        if used_quota is not None:
            self.used_quota = used_quota
        if extras_info is not None:
            self.extras_info = extras_info

    @property
    def max_quota(self):
        r"""Gets the max_quota of this ItemInfo.

        **参数解释**： 最大配额 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :return: The max_quota of this ItemInfo.
        :rtype: int
        """
        return self._max_quota

    @max_quota.setter
    def max_quota(self, max_quota):
        r"""Sets the max_quota of this ItemInfo.

        **参数解释**： 最大配额 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :param max_quota: The max_quota of this ItemInfo.
        :type max_quota: int
        """
        self._max_quota = max_quota

    @property
    def used_quota(self):
        r"""Gets the used_quota of this ItemInfo.

        **参数解释**： 已使用配额 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :return: The used_quota of this ItemInfo.
        :rtype: int
        """
        return self._used_quota

    @used_quota.setter
    def used_quota(self, used_quota):
        r"""Sets the used_quota of this ItemInfo.

        **参数解释**： 已使用配额 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :param used_quota: The used_quota of this ItemInfo.
        :type used_quota: int
        """
        self._used_quota = used_quota

    @property
    def extras_info(self):
        r"""Gets the extras_info of this ItemInfo.

        **参数解释**： 额外参数，ACL和网络域名使用 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :return: The extras_info of this ItemInfo.
        :rtype: dict(str, str)
        """
        return self._extras_info

    @extras_info.setter
    def extras_info(self, extras_info):
        r"""Sets the extras_info of this ItemInfo.

        **参数解释**： 额外参数，ACL和网络域名使用 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :param extras_info: The extras_info of this ItemInfo.
        :type extras_info: dict(str, str)
        """
        self._extras_info = extras_info

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
        if not isinstance(other, ItemInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
