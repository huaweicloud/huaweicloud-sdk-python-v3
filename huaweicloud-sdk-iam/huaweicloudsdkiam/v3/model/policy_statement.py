# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PolicyStatement:

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
        'condition': 'object',
        'resource': 'list[str]'
    }

    attribute_map = {
        'action': 'Action',
        'effect': 'Effect',
        'condition': 'Condition',
        'resource': 'Resource'
    }

    def __init__(self, action=None, effect=None, condition=None, resource=None):
        """PolicyStatement

        The model defined in huaweicloud sdk

        :param action: 授权项，指对资源的具体操作权限，不超过100个。 &gt; - 格式为：服务名:资源类型:操作，例：vpc:ports:create。 &gt; - 服务名为产品名称，例如ecs、evs和vpc等，服务名仅支持小写。 资源类型和操作没有大小写，要求支持通配符号*，无需罗列全部授权项。 &gt; - 当自定义策略为委托自定义策略时，该字段值为：&#x60;&#x60;&#x60; \&quot;Action\&quot;: [\&quot;iam:agencies:assume\&quot;]&#x60;&#x60;&#x60;。
        :type action: list[str]
        :param effect: 作用。包含两种：允许（Allow）和拒绝（Deny），既有Allow又有Deny的授权语句时，遵循Deny优先的原则。
        :type effect: str
        :param condition: 限制条件。不超过10个。
        :type condition: object
        :param resource: 资源。数组长度不超过10，每个字符串长度不超过128，规则如下： &gt; - 可填 * 的五段式：&lt;service-name&gt;:&lt;region&gt;:&lt;account-id&gt;:&lt;resource-type&gt;:&lt;resource-path&gt;，例：\&quot;obs:*:*:bucket:*\&quot;。 &gt; - region字段为*或用户可访问的region。service必须存在且resource属于对应service。 &gt; - 当该自定义策略为委托自定义策略时，该字段类型为Object，值为：&#x60;&#x60;&#x60;\&quot;Resource\&quot;: {\&quot;uri\&quot;: [\&quot;/iam/agencies/07805acaba800fdd4fbdc00b8f888c7c\&quot;]}&#x60;&#x60;&#x60;。
        :type resource: list[str]
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
        """Gets the action of this PolicyStatement.

        授权项，指对资源的具体操作权限，不超过100个。 > - 格式为：服务名:资源类型:操作，例：vpc:ports:create。 > - 服务名为产品名称，例如ecs、evs和vpc等，服务名仅支持小写。 资源类型和操作没有大小写，要求支持通配符号*，无需罗列全部授权项。 > - 当自定义策略为委托自定义策略时，该字段值为：``` \"Action\": [\"iam:agencies:assume\"]```。

        :return: The action of this PolicyStatement.
        :rtype: list[str]
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this PolicyStatement.

        授权项，指对资源的具体操作权限，不超过100个。 > - 格式为：服务名:资源类型:操作，例：vpc:ports:create。 > - 服务名为产品名称，例如ecs、evs和vpc等，服务名仅支持小写。 资源类型和操作没有大小写，要求支持通配符号*，无需罗列全部授权项。 > - 当自定义策略为委托自定义策略时，该字段值为：``` \"Action\": [\"iam:agencies:assume\"]```。

        :param action: The action of this PolicyStatement.
        :type action: list[str]
        """
        self._action = action

    @property
    def effect(self):
        """Gets the effect of this PolicyStatement.

        作用。包含两种：允许（Allow）和拒绝（Deny），既有Allow又有Deny的授权语句时，遵循Deny优先的原则。

        :return: The effect of this PolicyStatement.
        :rtype: str
        """
        return self._effect

    @effect.setter
    def effect(self, effect):
        """Sets the effect of this PolicyStatement.

        作用。包含两种：允许（Allow）和拒绝（Deny），既有Allow又有Deny的授权语句时，遵循Deny优先的原则。

        :param effect: The effect of this PolicyStatement.
        :type effect: str
        """
        self._effect = effect

    @property
    def condition(self):
        """Gets the condition of this PolicyStatement.

        限制条件。不超过10个。

        :return: The condition of this PolicyStatement.
        :rtype: object
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        """Sets the condition of this PolicyStatement.

        限制条件。不超过10个。

        :param condition: The condition of this PolicyStatement.
        :type condition: object
        """
        self._condition = condition

    @property
    def resource(self):
        """Gets the resource of this PolicyStatement.

        资源。数组长度不超过10，每个字符串长度不超过128，规则如下： > - 可填 * 的五段式：<service-name>:<region>:<account-id>:<resource-type>:<resource-path>，例：\"obs:*:*:bucket:*\"。 > - region字段为*或用户可访问的region。service必须存在且resource属于对应service。 > - 当该自定义策略为委托自定义策略时，该字段类型为Object，值为：```\"Resource\": {\"uri\": [\"/iam/agencies/07805acaba800fdd4fbdc00b8f888c7c\"]}```。

        :return: The resource of this PolicyStatement.
        :rtype: list[str]
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """Sets the resource of this PolicyStatement.

        资源。数组长度不超过10，每个字符串长度不超过128，规则如下： > - 可填 * 的五段式：<service-name>:<region>:<account-id>:<resource-type>:<resource-path>，例：\"obs:*:*:bucket:*\"。 > - region字段为*或用户可访问的region。service必须存在且resource属于对应service。 > - 当该自定义策略为委托自定义策略时，该字段类型为Object，值为：```\"Resource\": {\"uri\": [\"/iam/agencies/07805acaba800fdd4fbdc00b8f888c7c\"]}```。

        :param resource: The resource of this PolicyStatement.
        :type resource: list[str]
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
        if not isinstance(other, PolicyStatement):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
