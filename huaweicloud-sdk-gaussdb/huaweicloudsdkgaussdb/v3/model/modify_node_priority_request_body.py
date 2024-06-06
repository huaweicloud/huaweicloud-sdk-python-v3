# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModifyNodePriorityRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'priority': 'str'
    }

    attribute_map = {
        'priority': 'priority'
    }

    def __init__(self, priority=None):
        """ModifyNodePriorityRequestBody

        The model defined in huaweicloud sdk

        :param priority: 故障倒换优先级。  故障倒换优先级的取值范围为1~16以及-1。取正数时数字越小，优先级越大，即故障倒换时，主节点会优先倒换到优先级高的只读节点上，优先级相同的只读节点选为主节点的概率相同。取-1时表示节点不参与故障倒换，当单可用区实例超过两个只读节点，或者多可用区实例修改后的可用区多于1个时可以设置成-1。 
        :type priority: str
        """
        
        

        self._priority = None
        self.discriminator = None

        self.priority = priority

    @property
    def priority(self):
        """Gets the priority of this ModifyNodePriorityRequestBody.

        故障倒换优先级。  故障倒换优先级的取值范围为1~16以及-1。取正数时数字越小，优先级越大，即故障倒换时，主节点会优先倒换到优先级高的只读节点上，优先级相同的只读节点选为主节点的概率相同。取-1时表示节点不参与故障倒换，当单可用区实例超过两个只读节点，或者多可用区实例修改后的可用区多于1个时可以设置成-1。 

        :return: The priority of this ModifyNodePriorityRequestBody.
        :rtype: str
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this ModifyNodePriorityRequestBody.

        故障倒换优先级。  故障倒换优先级的取值范围为1~16以及-1。取正数时数字越小，优先级越大，即故障倒换时，主节点会优先倒换到优先级高的只读节点上，优先级相同的只读节点选为主节点的概率相同。取-1时表示节点不参与故障倒换，当单可用区实例超过两个只读节点，或者多可用区实例修改后的可用区多于1个时可以设置成-1。 

        :param priority: The priority of this ModifyNodePriorityRequestBody.
        :type priority: str
        """
        self._priority = priority

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
        if not isinstance(other, ModifyNodePriorityRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
