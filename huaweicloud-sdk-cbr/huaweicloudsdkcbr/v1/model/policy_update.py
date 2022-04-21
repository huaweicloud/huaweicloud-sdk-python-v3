# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PolicyUpdate:

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
        'trigger': 'PolicyTriggerReq'
    }

    attribute_map = {
        'enabled': 'enabled',
        'name': 'name',
        'operation_definition': 'operation_definition',
        'trigger': 'trigger'
    }

    def __init__(self, enabled=None, name=None, operation_definition=None, trigger=None):
        """PolicyUpdate

        The model defined in huaweicloud sdk

        :param enabled: 是否启用策略
        :type enabled: bool
        :param name: 策略名称
        :type name: str
        :param operation_definition: 
        :type operation_definition: :class:`huaweicloudsdkcbr.v1.PolicyoODCreate`
        :param trigger: 
        :type trigger: :class:`huaweicloudsdkcbr.v1.PolicyTriggerReq`
        """
        
        

        self._enabled = None
        self._name = None
        self._operation_definition = None
        self._trigger = None
        self.discriminator = None

        if enabled is not None:
            self.enabled = enabled
        if name is not None:
            self.name = name
        if operation_definition is not None:
            self.operation_definition = operation_definition
        if trigger is not None:
            self.trigger = trigger

    @property
    def enabled(self):
        """Gets the enabled of this PolicyUpdate.

        是否启用策略

        :return: The enabled of this PolicyUpdate.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this PolicyUpdate.

        是否启用策略

        :param enabled: The enabled of this PolicyUpdate.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def name(self):
        """Gets the name of this PolicyUpdate.

        策略名称

        :return: The name of this PolicyUpdate.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PolicyUpdate.

        策略名称

        :param name: The name of this PolicyUpdate.
        :type name: str
        """
        self._name = name

    @property
    def operation_definition(self):
        """Gets the operation_definition of this PolicyUpdate.


        :return: The operation_definition of this PolicyUpdate.
        :rtype: :class:`huaweicloudsdkcbr.v1.PolicyoODCreate`
        """
        return self._operation_definition

    @operation_definition.setter
    def operation_definition(self, operation_definition):
        """Sets the operation_definition of this PolicyUpdate.


        :param operation_definition: The operation_definition of this PolicyUpdate.
        :type operation_definition: :class:`huaweicloudsdkcbr.v1.PolicyoODCreate`
        """
        self._operation_definition = operation_definition

    @property
    def trigger(self):
        """Gets the trigger of this PolicyUpdate.


        :return: The trigger of this PolicyUpdate.
        :rtype: :class:`huaweicloudsdkcbr.v1.PolicyTriggerReq`
        """
        return self._trigger

    @trigger.setter
    def trigger(self, trigger):
        """Sets the trigger of this PolicyUpdate.


        :param trigger: The trigger of this PolicyUpdate.
        :type trigger: :class:`huaweicloudsdkcbr.v1.PolicyTriggerReq`
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
        if not isinstance(other, PolicyUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
