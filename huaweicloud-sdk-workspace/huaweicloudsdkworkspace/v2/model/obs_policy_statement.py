# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ObsPolicyStatement:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'effect': 'str',
        'action': 'list[str]',
        'resource': 'list[str]'
    }

    attribute_map = {
        'effect': 'effect',
        'action': 'action',
        'resource': 'resource'
    }

    def __init__(self, effect=None, action=None, resource=None):
        r"""ObsPolicyStatement

        The model defined in huaweicloud sdk

        :param effect: 状态(正常、禁用)： * &#39;Allow&#39; - 允许 * &#39;Deny&#39; - 禁用
        :type effect: str
        :param action: 可以进行操作的权限合集。
        :type action: list[str]
        :param resource: 允许访问的资源。
        :type resource: list[str]
        """
        
        

        self._effect = None
        self._action = None
        self._resource = None
        self.discriminator = None

        if effect is not None:
            self.effect = effect
        if action is not None:
            self.action = action
        if resource is not None:
            self.resource = resource

    @property
    def effect(self):
        r"""Gets the effect of this ObsPolicyStatement.

        状态(正常、禁用)： * 'Allow' - 允许 * 'Deny' - 禁用

        :return: The effect of this ObsPolicyStatement.
        :rtype: str
        """
        return self._effect

    @effect.setter
    def effect(self, effect):
        r"""Sets the effect of this ObsPolicyStatement.

        状态(正常、禁用)： * 'Allow' - 允许 * 'Deny' - 禁用

        :param effect: The effect of this ObsPolicyStatement.
        :type effect: str
        """
        self._effect = effect

    @property
    def action(self):
        r"""Gets the action of this ObsPolicyStatement.

        可以进行操作的权限合集。

        :return: The action of this ObsPolicyStatement.
        :rtype: list[str]
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this ObsPolicyStatement.

        可以进行操作的权限合集。

        :param action: The action of this ObsPolicyStatement.
        :type action: list[str]
        """
        self._action = action

    @property
    def resource(self):
        r"""Gets the resource of this ObsPolicyStatement.

        允许访问的资源。

        :return: The resource of this ObsPolicyStatement.
        :rtype: list[str]
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        r"""Sets the resource of this ObsPolicyStatement.

        允许访问的资源。

        :param resource: The resource of this ObsPolicyStatement.
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
        if not isinstance(other, ObsPolicyStatement):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
