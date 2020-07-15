# coding: utf-8

import pprint
import re

import six





class RestartInstanceRequestBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'target_type': 'str',
        'target_id': 'str'
    }

    attribute_map = {
        'target_type': 'target_type',
        'target_id': 'target_id'
    }

    def __init__(self, target_type=None, target_id=None):
        """RestartInstanceRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._target_type = None
        self._target_id = None
        self.discriminator = None

        if target_type is not None:
            self.target_type = target_type
        self.target_id = target_id

    @property
    def target_type(self):
        """Gets the target_type of this RestartInstanceRequestBody.

        待重启对象的类型。 - 重启集群实例下的节点时，该参数必选。取值为“mongos”、“shard”、或“config”。 - 重启整个实例时，不传该参数。

        :return: The target_type of this RestartInstanceRequestBody.
        :rtype: str
        """
        return self._target_type

    @target_type.setter
    def target_type(self, target_type):
        """Sets the target_type of this RestartInstanceRequestBody.

        待重启对象的类型。 - 重启集群实例下的节点时，该参数必选。取值为“mongos”、“shard”、或“config”。 - 重启整个实例时，不传该参数。

        :param target_type: The target_type of this RestartInstanceRequestBody.
        :type: str
        """
        self._target_type = target_type

    @property
    def target_id(self):
        """Gets the target_id of this RestartInstanceRequestBody.

        待重启对象的ID。 - 重启集群实例下的节点时，对于mongos节点，取值为mongos节点ID，对于shard和config组，取值为shard和config组ID。 - 重启整个实例时，取值为实例ID。

        :return: The target_id of this RestartInstanceRequestBody.
        :rtype: str
        """
        return self._target_id

    @target_id.setter
    def target_id(self, target_id):
        """Sets the target_id of this RestartInstanceRequestBody.

        待重启对象的ID。 - 重启集群实例下的节点时，对于mongos节点，取值为mongos节点ID，对于shard和config组，取值为shard和config组ID。 - 重启整个实例时，取值为实例ID。

        :param target_id: The target_id of this RestartInstanceRequestBody.
        :type: str
        """
        self._target_id = target_id

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
        if not isinstance(other, RestartInstanceRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
