# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstancesWeight:

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
        'weight': 'int'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'weight': 'weight'
    }

    def __init__(self, instance_id=None, weight=None):
        """InstancesWeight

        The model defined in huaweicloud sdk

        :param instance_id: 数据库实例ID。
        :type instance_id: str
        :param weight: 数据库代理读权重。
        :type weight: int
        """
        
        

        self._instance_id = None
        self._weight = None
        self.discriminator = None

        self.instance_id = instance_id
        self.weight = weight

    @property
    def instance_id(self):
        """Gets the instance_id of this InstancesWeight.

        数据库实例ID。

        :return: The instance_id of this InstancesWeight.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this InstancesWeight.

        数据库实例ID。

        :param instance_id: The instance_id of this InstancesWeight.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def weight(self):
        """Gets the weight of this InstancesWeight.

        数据库代理读权重。

        :return: The weight of this InstancesWeight.
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this InstancesWeight.

        数据库代理读权重。

        :param weight: The weight of this InstancesWeight.
        :type weight: int
        """
        self._weight = weight

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
        if not isinstance(other, InstancesWeight):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
