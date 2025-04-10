# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CustomStatement:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'action': 'list[str]',
        'effect': 'str',
        'condition': 'dict(str, dict(str, list[str]))',
        'resource': 'object'
    }

    attribute_map = {
        'action': 'Action',
        'effect': 'Effect',
        'condition': 'Condition',
        'resource': 'Resource'
    }

    def __init__(self, action=None, effect=None, condition=None, resource=None):
        r"""CustomStatement

        The model defined in huaweicloud sdk

        :param action: 授权项，指对资源的具体操作权限。 &gt; - 格式为：服务名:资源类型:操作，例：vpc:ports:create。 &gt; - 服务名为产品名称，例如ecs、evs和vpc等，服务名仅支持小写。 资源类型和操作没有大小写，要求支持通配符号*，无需罗列全部授权项。
        :type action: list[str]
        :param effect: 作用。包含两种：允许（Allow）和拒绝（Deny），既有Allow又有Deny的授权语句时，遵循Deny优先的原则。
        :type effect: str
        :param condition: 
        :type condition: dict(str, dict(str, list[str]))
        :param resource: 资源。规则如下： &gt; - 可填 * 的五段式：&lt;service-name&gt;:&lt;region&gt;:&lt;account-id&gt;:&lt;resource-type&gt;:&lt;resource-path&gt;，例：\&quot;obs:*:*:bucket:*\&quot;。 &gt; - region字段为*或用户可访问的region。service必须存在且resource属于对应service。
        :type resource: object
        """
        
        

        self._action = None
        self._effect = None
        self._condition = None
        self._resource = None
        self.discriminator = None

        self.action = action
        self.effect = effect
        if condition is not None:
            self.condition = condition
        if resource is not None:
            self.resource = resource

    @property
    def action(self):
        r"""Gets the action of this CustomStatement.

        授权项，指对资源的具体操作权限。 > - 格式为：服务名:资源类型:操作，例：vpc:ports:create。 > - 服务名为产品名称，例如ecs、evs和vpc等，服务名仅支持小写。 资源类型和操作没有大小写，要求支持通配符号*，无需罗列全部授权项。

        :return: The action of this CustomStatement.
        :rtype: list[str]
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this CustomStatement.

        授权项，指对资源的具体操作权限。 > - 格式为：服务名:资源类型:操作，例：vpc:ports:create。 > - 服务名为产品名称，例如ecs、evs和vpc等，服务名仅支持小写。 资源类型和操作没有大小写，要求支持通配符号*，无需罗列全部授权项。

        :param action: The action of this CustomStatement.
        :type action: list[str]
        """
        self._action = action

    @property
    def effect(self):
        r"""Gets the effect of this CustomStatement.

        作用。包含两种：允许（Allow）和拒绝（Deny），既有Allow又有Deny的授权语句时，遵循Deny优先的原则。

        :return: The effect of this CustomStatement.
        :rtype: str
        """
        return self._effect

    @effect.setter
    def effect(self, effect):
        r"""Sets the effect of this CustomStatement.

        作用。包含两种：允许（Allow）和拒绝（Deny），既有Allow又有Deny的授权语句时，遵循Deny优先的原则。

        :param effect: The effect of this CustomStatement.
        :type effect: str
        """
        self._effect = effect

    @property
    def condition(self):
        r"""Gets the condition of this CustomStatement.

        :return: The condition of this CustomStatement.
        :rtype: dict(str, dict(str, list[str]))
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        r"""Sets the condition of this CustomStatement.

        :param condition: The condition of this CustomStatement.
        :type condition: dict(str, dict(str, list[str]))
        """
        self._condition = condition

    @property
    def resource(self):
        r"""Gets the resource of this CustomStatement.

        资源。规则如下： > - 可填 * 的五段式：<service-name>:<region>:<account-id>:<resource-type>:<resource-path>，例：\"obs:*:*:bucket:*\"。 > - region字段为*或用户可访问的region。service必须存在且resource属于对应service。

        :return: The resource of this CustomStatement.
        :rtype: object
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        r"""Sets the resource of this CustomStatement.

        资源。规则如下： > - 可填 * 的五段式：<service-name>:<region>:<account-id>:<resource-type>:<resource-path>，例：\"obs:*:*:bucket:*\"。 > - region字段为*或用户可访问的region。service必须存在且resource属于对应service。

        :param resource: The resource of this CustomStatement.
        :type resource: object
        """
        self._resource = resource

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
        if not isinstance(other, CustomStatement):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
