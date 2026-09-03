# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateSecurityPolicyControlReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enabled_instances': 'list[str]',
        'enabled_tags': 'list[str]',
        'disabled_instances': 'list[str]',
        'disabled_tags': 'list[str]'
    }

    attribute_map = {
        'enabled_instances': 'enabled_instances',
        'enabled_tags': 'enabled_tags',
        'disabled_instances': 'disabled_instances',
        'disabled_tags': 'disabled_tags'
    }

    def __init__(self, enabled_instances=None, enabled_tags=None, disabled_instances=None, disabled_tags=None):
        r"""UpdateSecurityPolicyControlReq

        The model defined in huaweicloud sdk

        :param enabled_instances: 需要开启安全策略管控的实例 ID 列表。
        :type enabled_instances: list[str]
        :param enabled_tags: 需要开启安全策略管控的标签列表，格式为 key:value。
        :type enabled_tags: list[str]
        :param disabled_instances: 需要关闭安全策略管控的实例 ID 列表。
        :type disabled_instances: list[str]
        :param disabled_tags: 需要关闭安全策略管控的标签列表，格式为 key:value。
        :type disabled_tags: list[str]
        """
        
        

        self._enabled_instances = None
        self._enabled_tags = None
        self._disabled_instances = None
        self._disabled_tags = None
        self.discriminator = None

        if enabled_instances is not None:
            self.enabled_instances = enabled_instances
        if enabled_tags is not None:
            self.enabled_tags = enabled_tags
        if disabled_instances is not None:
            self.disabled_instances = disabled_instances
        if disabled_tags is not None:
            self.disabled_tags = disabled_tags

    @property
    def enabled_instances(self):
        r"""Gets the enabled_instances of this UpdateSecurityPolicyControlReq.

        需要开启安全策略管控的实例 ID 列表。

        :return: The enabled_instances of this UpdateSecurityPolicyControlReq.
        :rtype: list[str]
        """
        return self._enabled_instances

    @enabled_instances.setter
    def enabled_instances(self, enabled_instances):
        r"""Sets the enabled_instances of this UpdateSecurityPolicyControlReq.

        需要开启安全策略管控的实例 ID 列表。

        :param enabled_instances: The enabled_instances of this UpdateSecurityPolicyControlReq.
        :type enabled_instances: list[str]
        """
        self._enabled_instances = enabled_instances

    @property
    def enabled_tags(self):
        r"""Gets the enabled_tags of this UpdateSecurityPolicyControlReq.

        需要开启安全策略管控的标签列表，格式为 key:value。

        :return: The enabled_tags of this UpdateSecurityPolicyControlReq.
        :rtype: list[str]
        """
        return self._enabled_tags

    @enabled_tags.setter
    def enabled_tags(self, enabled_tags):
        r"""Sets the enabled_tags of this UpdateSecurityPolicyControlReq.

        需要开启安全策略管控的标签列表，格式为 key:value。

        :param enabled_tags: The enabled_tags of this UpdateSecurityPolicyControlReq.
        :type enabled_tags: list[str]
        """
        self._enabled_tags = enabled_tags

    @property
    def disabled_instances(self):
        r"""Gets the disabled_instances of this UpdateSecurityPolicyControlReq.

        需要关闭安全策略管控的实例 ID 列表。

        :return: The disabled_instances of this UpdateSecurityPolicyControlReq.
        :rtype: list[str]
        """
        return self._disabled_instances

    @disabled_instances.setter
    def disabled_instances(self, disabled_instances):
        r"""Sets the disabled_instances of this UpdateSecurityPolicyControlReq.

        需要关闭安全策略管控的实例 ID 列表。

        :param disabled_instances: The disabled_instances of this UpdateSecurityPolicyControlReq.
        :type disabled_instances: list[str]
        """
        self._disabled_instances = disabled_instances

    @property
    def disabled_tags(self):
        r"""Gets the disabled_tags of this UpdateSecurityPolicyControlReq.

        需要关闭安全策略管控的标签列表，格式为 key:value。

        :return: The disabled_tags of this UpdateSecurityPolicyControlReq.
        :rtype: list[str]
        """
        return self._disabled_tags

    @disabled_tags.setter
    def disabled_tags(self, disabled_tags):
        r"""Sets the disabled_tags of this UpdateSecurityPolicyControlReq.

        需要关闭安全策略管控的标签列表，格式为 key:value。

        :param disabled_tags: The disabled_tags of this UpdateSecurityPolicyControlReq.
        :type disabled_tags: list[str]
        """
        self._disabled_tags = disabled_tags

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
        if not isinstance(other, UpdateSecurityPolicyControlReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
