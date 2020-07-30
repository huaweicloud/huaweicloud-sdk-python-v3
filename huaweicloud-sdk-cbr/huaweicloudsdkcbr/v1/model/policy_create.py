# coding: utf-8

import pprint
import re

import six





class PolicyCreate:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'enabled': 'bool',
        'name': 'str',
        'operation_definition': 'PolicyoODCreate',
        'operation_type': 'str',
        'trigger': 'PolicyTriggerReq'
    }

    attribute_map = {
        'enabled': 'enabled',
        'name': 'name',
        'operation_definition': 'operation_definition',
        'operation_type': 'operation_type',
        'trigger': 'trigger'
    }

    def __init__(self, enabled=True, name=None, operation_definition=None, operation_type=None, trigger=None):
        """PolicyCreate - a model defined in huaweicloud sdk"""
        
        

        self._enabled = None
        self._name = None
        self._operation_definition = None
        self._operation_type = None
        self._trigger = None
        self.discriminator = None

        if enabled is not None:
            self.enabled = enabled
        self.name = name
        self.operation_definition = operation_definition
        self.operation_type = operation_type
        self.trigger = trigger

    @property
    def enabled(self):
        """Gets the enabled of this PolicyCreate.

        是否启用策略

        :return: The enabled of this PolicyCreate.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this PolicyCreate.

        是否启用策略

        :param enabled: The enabled of this PolicyCreate.
        :type: bool
        """
        self._enabled = enabled

    @property
    def name(self):
        """Gets the name of this PolicyCreate.

        策略名称，长度限制：1- 64，只能由中文、字母、数字、“_”、“-”组成。

        :return: The name of this PolicyCreate.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PolicyCreate.

        策略名称，长度限制：1- 64，只能由中文、字母、数字、“_”、“-”组成。

        :param name: The name of this PolicyCreate.
        :type: str
        """
        self._name = name

    @property
    def operation_definition(self):
        """Gets the operation_definition of this PolicyCreate.


        :return: The operation_definition of this PolicyCreate.
        :rtype: PolicyoODCreate
        """
        return self._operation_definition

    @operation_definition.setter
    def operation_definition(self, operation_definition):
        """Sets the operation_definition of this PolicyCreate.


        :param operation_definition: The operation_definition of this PolicyCreate.
        :type: PolicyoODCreate
        """
        self._operation_definition = operation_definition

    @property
    def operation_type(self):
        """Gets the operation_type of this PolicyCreate.

        策略类型，如备份，复制 Enum:[ backup，replication]

        :return: The operation_type of this PolicyCreate.
        :rtype: str
        """
        return self._operation_type

    @operation_type.setter
    def operation_type(self, operation_type):
        """Sets the operation_type of this PolicyCreate.

        策略类型，如备份，复制 Enum:[ backup，replication]

        :param operation_type: The operation_type of this PolicyCreate.
        :type: str
        """
        self._operation_type = operation_type

    @property
    def trigger(self):
        """Gets the trigger of this PolicyCreate.


        :return: The trigger of this PolicyCreate.
        :rtype: PolicyTriggerReq
        """
        return self._trigger

    @trigger.setter
    def trigger(self, trigger):
        """Sets the trigger of this PolicyCreate.


        :param trigger: The trigger of this PolicyCreate.
        :type: PolicyTriggerReq
        """
        self._trigger = trigger

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
        if not isinstance(other, PolicyCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
