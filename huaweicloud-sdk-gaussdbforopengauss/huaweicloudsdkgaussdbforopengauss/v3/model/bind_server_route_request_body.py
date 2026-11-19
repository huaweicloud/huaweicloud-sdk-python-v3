# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BindServerRouteRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'operate': 'str',
        'target_server_ips': 'list[str]'
    }

    attribute_map = {
        'operate': 'operate',
        'target_server_ips': 'target_server_ips'
    }

    def __init__(self, operate=None, target_server_ips=None):
        r"""BindServerRouteRequestBody

        The model defined in huaweicloud sdk

        :param operate: **参数解释**: 操作类型。 **约束限制**: 不涉及。 **取值范围**: - add：绑定服务端IP路由 - delete：解绑服务端IP路由  **默认取值**: 不涉及。
        :type operate: str
        :param target_server_ips: **参数解释**: 服务端IP列表。 **约束限制**: 列表元素需要满足IPv4格式要求。 **取值范围**: 不涉及。 **默认取值**: 不涉及。
        :type target_server_ips: list[str]
        """
        
        

        self._operate = None
        self._target_server_ips = None
        self.discriminator = None

        self.operate = operate
        self.target_server_ips = target_server_ips

    @property
    def operate(self):
        r"""Gets the operate of this BindServerRouteRequestBody.

        **参数解释**: 操作类型。 **约束限制**: 不涉及。 **取值范围**: - add：绑定服务端IP路由 - delete：解绑服务端IP路由  **默认取值**: 不涉及。

        :return: The operate of this BindServerRouteRequestBody.
        :rtype: str
        """
        return self._operate

    @operate.setter
    def operate(self, operate):
        r"""Sets the operate of this BindServerRouteRequestBody.

        **参数解释**: 操作类型。 **约束限制**: 不涉及。 **取值范围**: - add：绑定服务端IP路由 - delete：解绑服务端IP路由  **默认取值**: 不涉及。

        :param operate: The operate of this BindServerRouteRequestBody.
        :type operate: str
        """
        self._operate = operate

    @property
    def target_server_ips(self):
        r"""Gets the target_server_ips of this BindServerRouteRequestBody.

        **参数解释**: 服务端IP列表。 **约束限制**: 列表元素需要满足IPv4格式要求。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :return: The target_server_ips of this BindServerRouteRequestBody.
        :rtype: list[str]
        """
        return self._target_server_ips

    @target_server_ips.setter
    def target_server_ips(self, target_server_ips):
        r"""Sets the target_server_ips of this BindServerRouteRequestBody.

        **参数解释**: 服务端IP列表。 **约束限制**: 列表元素需要满足IPv4格式要求。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :param target_server_ips: The target_server_ips of this BindServerRouteRequestBody.
        :type target_server_ips: list[str]
        """
        self._target_server_ips = target_server_ips

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
        if not isinstance(other, BindServerRouteRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
