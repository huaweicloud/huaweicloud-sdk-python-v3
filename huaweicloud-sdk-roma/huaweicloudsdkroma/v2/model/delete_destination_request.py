# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteDestinationRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'rule_id': 'str',
        'destination_id': 'int'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'rule_id': 'rule_id',
        'destination_id': 'destination_id'
    }

    def __init__(self, instance_id=None, rule_id=None, destination_id=None):
        """DeleteDestinationRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID
        :type instance_id: str
        :param rule_id: 规则ID
        :type rule_id: str
        :param destination_id: 目标数据源ID
        :type destination_id: int
        """
        
        

        self._instance_id = None
        self._rule_id = None
        self._destination_id = None
        self.discriminator = None

        self.instance_id = instance_id
        self.rule_id = rule_id
        self.destination_id = destination_id

    @property
    def instance_id(self):
        """Gets the instance_id of this DeleteDestinationRequest.

        实例ID

        :return: The instance_id of this DeleteDestinationRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this DeleteDestinationRequest.

        实例ID

        :param instance_id: The instance_id of this DeleteDestinationRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def rule_id(self):
        """Gets the rule_id of this DeleteDestinationRequest.

        规则ID

        :return: The rule_id of this DeleteDestinationRequest.
        :rtype: str
        """
        return self._rule_id

    @rule_id.setter
    def rule_id(self, rule_id):
        """Sets the rule_id of this DeleteDestinationRequest.

        规则ID

        :param rule_id: The rule_id of this DeleteDestinationRequest.
        :type rule_id: str
        """
        self._rule_id = rule_id

    @property
    def destination_id(self):
        """Gets the destination_id of this DeleteDestinationRequest.

        目标数据源ID

        :return: The destination_id of this DeleteDestinationRequest.
        :rtype: int
        """
        return self._destination_id

    @destination_id.setter
    def destination_id(self, destination_id):
        """Sets the destination_id of this DeleteDestinationRequest.

        目标数据源ID

        :param destination_id: The destination_id of this DeleteDestinationRequest.
        :type destination_id: int
        """
        self._destination_id = destination_id

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
        if not isinstance(other, DeleteDestinationRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
