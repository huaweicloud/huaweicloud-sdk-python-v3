# coding: utf-8

import pprint
import re

import six





class Policy:


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
        'id': 'str',
        'name': 'str',
        'operation_definition': 'PolicyoODCreate',
        'operation_type': 'str',
        'trigger': 'PolicyTriggerResp',
        'associated_vaults': 'list[PolicyAssociateVault]'
    }

    attribute_map = {
        'enabled': 'enabled',
        'id': 'id',
        'name': 'name',
        'operation_definition': 'operation_definition',
        'operation_type': 'operation_type',
        'trigger': 'trigger',
        'associated_vaults': 'associated_vaults'
    }

    def __init__(self, enabled=None, id=None, name=None, operation_definition=None, operation_type=None, trigger=None, associated_vaults=None):
        """Policy - a model defined in huaweicloud sdk"""
        
        

        self._enabled = None
        self._id = None
        self._name = None
        self._operation_definition = None
        self._operation_type = None
        self._trigger = None
        self._associated_vaults = None
        self.discriminator = None

        self.enabled = enabled
        self.id = id
        self.name = name
        self.operation_definition = operation_definition
        self.operation_type = operation_type
        self.trigger = trigger
        if associated_vaults is not None:
            self.associated_vaults = associated_vaults

    @property
    def enabled(self):
        """Gets the enabled of this Policy.

        策略是否启用

        :return: The enabled of this Policy.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this Policy.

        策略是否启用

        :param enabled: The enabled of this Policy.
        :type: bool
        """
        self._enabled = enabled

    @property
    def id(self):
        """Gets the id of this Policy.

        策略ID

        :return: The id of this Policy.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Policy.

        策略ID

        :param id: The id of this Policy.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this Policy.

        策略名称

        :return: The name of this Policy.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Policy.

        策略名称

        :param name: The name of this Policy.
        :type: str
        """
        self._name = name

    @property
    def operation_definition(self):
        """Gets the operation_definition of this Policy.


        :return: The operation_definition of this Policy.
        :rtype: PolicyoODCreate
        """
        return self._operation_definition

    @operation_definition.setter
    def operation_definition(self, operation_definition):
        """Sets the operation_definition of this Policy.


        :param operation_definition: The operation_definition of this Policy.
        :type: PolicyoODCreate
        """
        self._operation_definition = operation_definition

    @property
    def operation_type(self):
        """Gets the operation_type of this Policy.

        策略类型,例如 ‘backup’：自动备份

        :return: The operation_type of this Policy.
        :rtype: str
        """
        return self._operation_type

    @operation_type.setter
    def operation_type(self, operation_type):
        """Sets the operation_type of this Policy.

        策略类型,例如 ‘backup’：自动备份

        :param operation_type: The operation_type of this Policy.
        :type: str
        """
        self._operation_type = operation_type

    @property
    def trigger(self):
        """Gets the trigger of this Policy.


        :return: The trigger of this Policy.
        :rtype: PolicyTriggerResp
        """
        return self._trigger

    @trigger.setter
    def trigger(self, trigger):
        """Sets the trigger of this Policy.


        :param trigger: The trigger of this Policy.
        :type: PolicyTriggerResp
        """
        self._trigger = trigger

    @property
    def associated_vaults(self):
        """Gets the associated_vaults of this Policy.

        关联的存储库

        :return: The associated_vaults of this Policy.
        :rtype: list[PolicyAssociateVault]
        """
        return self._associated_vaults

    @associated_vaults.setter
    def associated_vaults(self, associated_vaults):
        """Sets the associated_vaults of this Policy.

        关联的存储库

        :param associated_vaults: The associated_vaults of this Policy.
        :type: list[PolicyAssociateVault]
        """
        self._associated_vaults = associated_vaults

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
        if not isinstance(other, Policy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
