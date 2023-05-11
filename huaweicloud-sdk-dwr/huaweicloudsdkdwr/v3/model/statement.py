# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Statement:

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
        'resource': 'list[str]'
    }

    attribute_map = {
        'action': 'action',
        'resource': 'resource'
    }

    def __init__(self, action=None, resource=None):
        """Statement

        The model defined in huaweicloud sdk

        :param action: 授权项。指对资源的具体操作权限，不超过100个。 - 格式为：服务名:资源类型:操作，例：vpc:ports:create。 - 服务名为产品名称，例如ecs、evs和vpc等，服务名仅支持小写。 资源类型和操作没有大小写，要求支持通配符号*，无需罗列全部授权项。 - 当自定义策略为委托自定义策略时，该字段值为： \&quot;Action\&quot;: [\&quot;iam:agencies:assume\&quot;]。
        :type action: list[str]
        :param resource: 资源。数组长度不超过10，每个字符串长度不超过128，规则如下： - 可填 * 的五段式：::::，例：\&quot;obs:::bucket:*\&quot;。 - region字段为*或用户可访问的region。service必须存在且resource属于对应service。 - 当该自定义策略为委托自定义策略时，该字段类型为Object，值为：\&quot;Resource\&quot;: {\&quot;uri\&quot;: [\&quot;/iam/agencies/07805acaba800fdd4fbdc00b8f888c7c\&quot;]}。
        :type resource: list[str]
        """
        
        

        self._action = None
        self._resource = None
        self.discriminator = None

        if action is not None:
            self.action = action
        if resource is not None:
            self.resource = resource

    @property
    def action(self):
        """Gets the action of this Statement.

        授权项。指对资源的具体操作权限，不超过100个。 - 格式为：服务名:资源类型:操作，例：vpc:ports:create。 - 服务名为产品名称，例如ecs、evs和vpc等，服务名仅支持小写。 资源类型和操作没有大小写，要求支持通配符号*，无需罗列全部授权项。 - 当自定义策略为委托自定义策略时，该字段值为： \"Action\": [\"iam:agencies:assume\"]。

        :return: The action of this Statement.
        :rtype: list[str]
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this Statement.

        授权项。指对资源的具体操作权限，不超过100个。 - 格式为：服务名:资源类型:操作，例：vpc:ports:create。 - 服务名为产品名称，例如ecs、evs和vpc等，服务名仅支持小写。 资源类型和操作没有大小写，要求支持通配符号*，无需罗列全部授权项。 - 当自定义策略为委托自定义策略时，该字段值为： \"Action\": [\"iam:agencies:assume\"]。

        :param action: The action of this Statement.
        :type action: list[str]
        """
        self._action = action

    @property
    def resource(self):
        """Gets the resource of this Statement.

        资源。数组长度不超过10，每个字符串长度不超过128，规则如下： - 可填 * 的五段式：::::，例：\"obs:::bucket:*\"。 - region字段为*或用户可访问的region。service必须存在且resource属于对应service。 - 当该自定义策略为委托自定义策略时，该字段类型为Object，值为：\"Resource\": {\"uri\": [\"/iam/agencies/07805acaba800fdd4fbdc00b8f888c7c\"]}。

        :return: The resource of this Statement.
        :rtype: list[str]
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """Sets the resource of this Statement.

        资源。数组长度不超过10，每个字符串长度不超过128，规则如下： - 可填 * 的五段式：::::，例：\"obs:::bucket:*\"。 - region字段为*或用户可访问的region。service必须存在且resource属于对应service。 - 当该自定义策略为委托自定义策略时，该字段类型为Object，值为：\"Resource\": {\"uri\": [\"/iam/agencies/07805acaba800fdd4fbdc00b8f888c7c\"]}。

        :param resource: The resource of this Statement.
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
        if not isinstance(other, Statement):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
