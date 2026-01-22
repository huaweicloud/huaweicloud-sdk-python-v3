# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowQuotasRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'include_tags_quota': 'str',
        'only_quota': 'str'
    }

    attribute_map = {
        'include_tags_quota': 'includeTagsQuota',
        'only_quota': 'onlyQuota'
    }

    def __init__(self, include_tags_quota=None, only_quota=None):
        r"""ShowQuotasRequest

        The model defined in huaweicloud sdk

        :param include_tags_quota: **参数解释**： 是否包含标签配额标志。 **约束限制**： 不涉及。 **取值范围**： - true：包含配额。 - false：不包含配额。 **默认取值**： true。
        :type include_tags_quota: str
        :param only_quota: **参数解释**： 查询指定配额引擎。 **约束限制**： 不涉及。 **取值范围**： - reliability：RocketMQ消息引擎别称。 - kafka：kafka消息引擎别称。 **默认取值**： 不涉及。
        :type only_quota: str
        """
        
        

        self._include_tags_quota = None
        self._only_quota = None
        self.discriminator = None

        if include_tags_quota is not None:
            self.include_tags_quota = include_tags_quota
        if only_quota is not None:
            self.only_quota = only_quota

    @property
    def include_tags_quota(self):
        r"""Gets the include_tags_quota of this ShowQuotasRequest.

        **参数解释**： 是否包含标签配额标志。 **约束限制**： 不涉及。 **取值范围**： - true：包含配额。 - false：不包含配额。 **默认取值**： true。

        :return: The include_tags_quota of this ShowQuotasRequest.
        :rtype: str
        """
        return self._include_tags_quota

    @include_tags_quota.setter
    def include_tags_quota(self, include_tags_quota):
        r"""Sets the include_tags_quota of this ShowQuotasRequest.

        **参数解释**： 是否包含标签配额标志。 **约束限制**： 不涉及。 **取值范围**： - true：包含配额。 - false：不包含配额。 **默认取值**： true。

        :param include_tags_quota: The include_tags_quota of this ShowQuotasRequest.
        :type include_tags_quota: str
        """
        self._include_tags_quota = include_tags_quota

    @property
    def only_quota(self):
        r"""Gets the only_quota of this ShowQuotasRequest.

        **参数解释**： 查询指定配额引擎。 **约束限制**： 不涉及。 **取值范围**： - reliability：RocketMQ消息引擎别称。 - kafka：kafka消息引擎别称。 **默认取值**： 不涉及。

        :return: The only_quota of this ShowQuotasRequest.
        :rtype: str
        """
        return self._only_quota

    @only_quota.setter
    def only_quota(self, only_quota):
        r"""Sets the only_quota of this ShowQuotasRequest.

        **参数解释**： 查询指定配额引擎。 **约束限制**： 不涉及。 **取值范围**： - reliability：RocketMQ消息引擎别称。 - kafka：kafka消息引擎别称。 **默认取值**： 不涉及。

        :param only_quota: The only_quota of this ShowQuotasRequest.
        :type only_quota: str
        """
        self._only_quota = only_quota

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
        if not isinstance(other, ShowQuotasRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
