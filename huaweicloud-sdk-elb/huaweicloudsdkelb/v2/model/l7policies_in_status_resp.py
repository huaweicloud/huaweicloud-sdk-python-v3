# coding: utf-8

import pprint
import re

import six





class L7policiesInStatusResp:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'rules': 'list[L7rulesInStatusResp]',
        'action': 'str',
        'provisioning_status': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'rules': 'rules',
        'action': 'action',
        'provisioning_status': 'provisioning_status'
    }

    def __init__(self, id=None, name=None, rules=None, action=None, provisioning_status=None):
        """L7policiesInStatusResp - a model defined in huaweicloud sdk"""
        
        

        self._id = None
        self._name = None
        self._rules = None
        self._action = None
        self._provisioning_status = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.rules = rules
        self.action = action
        self.provisioning_status = provisioning_status

    @property
    def id(self):
        """Gets the id of this L7policiesInStatusResp.

        转发策略ID

        :return: The id of this L7policiesInStatusResp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this L7policiesInStatusResp.

        转发策略ID

        :param id: The id of this L7policiesInStatusResp.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this L7policiesInStatusResp.

        转发策略名称

        :return: The name of this L7policiesInStatusResp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this L7policiesInStatusResp.

        转发策略名称

        :param name: The name of this L7policiesInStatusResp.
        :type: str
        """
        self._name = name

    @property
    def rules(self):
        """Gets the rules of this L7policiesInStatusResp.

        转发策略关联的转发规则列表

        :return: The rules of this L7policiesInStatusResp.
        :rtype: list[L7rulesInStatusResp]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """Sets the rules of this L7policiesInStatusResp.

        转发策略关联的转发规则列表

        :param rules: The rules of this L7policiesInStatusResp.
        :type: list[L7rulesInStatusResp]
        """
        self._rules = rules

    @property
    def action(self):
        """Gets the action of this L7policiesInStatusResp.

        转发策略的转发动作；取值：REDIRECT_TO_POOL：转发到后端云服务器组；REDIRECT_TO_LISTENER：重定向到监听器

        :return: The action of this L7policiesInStatusResp.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this L7policiesInStatusResp.

        转发策略的转发动作；取值：REDIRECT_TO_POOL：转发到后端云服务器组；REDIRECT_TO_LISTENER：重定向到监听器

        :param action: The action of this L7policiesInStatusResp.
        :type: str
        """
        self._action = action

    @property
    def provisioning_status(self):
        """Gets the provisioning_status of this L7policiesInStatusResp.

        健康检查的配置状态；该字段为预留字段，暂未启用。默认为ACTIVE。

        :return: The provisioning_status of this L7policiesInStatusResp.
        :rtype: str
        """
        return self._provisioning_status

    @provisioning_status.setter
    def provisioning_status(self, provisioning_status):
        """Sets the provisioning_status of this L7policiesInStatusResp.

        健康检查的配置状态；该字段为预留字段，暂未启用。默认为ACTIVE。

        :param provisioning_status: The provisioning_status of this L7policiesInStatusResp.
        :type: str
        """
        self._provisioning_status = provisioning_status

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, L7policiesInStatusResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
