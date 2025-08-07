# coding: utf-8

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
        'effect': 'str',
        'action': 'list[str]',
        'resource': 'list[str]',
        'condition': 'object',
        'sid': 'str'
    }

    attribute_map = {
        'effect': 'Effect',
        'action': 'Action',
        'resource': 'Resource',
        'condition': 'Condition',
        'sid': 'Sid'
    }

    def __init__(self, effect=None, action=None, resource=None, condition=None, sid=None):
        r"""PolicyStatement

        The model defined in huaweicloud sdk

        :param effect: - Allow，允许控制访问权限 - Deny，拒绝控制访问权限
        :type effect: str
        :param action: obs访问权限
        :type action: list[str]
        :param resource: obs对象
        :type resource: list[str]
        :param condition: statement生效的条件
        :type condition: object
        :param sid: 策略Id
        :type sid: str
        """
        
        

        self._effect = None
        self._action = None
        self._resource = None
        self._condition = None
        self._sid = None
        self.discriminator = None

        self.effect = effect
        self.action = action
        self.resource = resource
        if condition is not None:
            self.condition = condition
        if sid is not None:
            self.sid = sid

    @property
    def effect(self):
        r"""Gets the effect of this PolicyStatement.

        - Allow，允许控制访问权限 - Deny，拒绝控制访问权限

        :return: The effect of this PolicyStatement.
        :rtype: str
        """
        return self._effect

    @effect.setter
    def effect(self, effect):
        r"""Sets the effect of this PolicyStatement.

        - Allow，允许控制访问权限 - Deny，拒绝控制访问权限

        :param effect: The effect of this PolicyStatement.
        :type effect: str
        """
        self._effect = effect

    @property
    def action(self):
        r"""Gets the action of this PolicyStatement.

        obs访问权限

        :return: The action of this PolicyStatement.
        :rtype: list[str]
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this PolicyStatement.

        obs访问权限

        :param action: The action of this PolicyStatement.
        :type action: list[str]
        """
        self._action = action

    @property
    def resource(self):
        r"""Gets the resource of this PolicyStatement.

        obs对象

        :return: The resource of this PolicyStatement.
        :rtype: list[str]
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        r"""Sets the resource of this PolicyStatement.

        obs对象

        :param resource: The resource of this PolicyStatement.
        :type resource: list[str]
        """
        self._resource = resource

    @property
    def condition(self):
        r"""Gets the condition of this PolicyStatement.

        statement生效的条件

        :return: The condition of this PolicyStatement.
        :rtype: object
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        r"""Sets the condition of this PolicyStatement.

        statement生效的条件

        :param condition: The condition of this PolicyStatement.
        :type condition: object
        """
        self._condition = condition

    @property
    def sid(self):
        r"""Gets the sid of this PolicyStatement.

        策略Id

        :return: The sid of this PolicyStatement.
        :rtype: str
        """
        return self._sid

    @sid.setter
    def sid(self, sid):
        r"""Sets the sid of this PolicyStatement.

        策略Id

        :param sid: The sid of this PolicyStatement.
        :type sid: str
        """
        self._sid = sid

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
