# coding: utf-8

import pprint
import re

import six





class ResizeInstanceOption:


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
        'target_id': 'str',
        'target_spec_code': 'str'
    }

    attribute_map = {
        'target_type': 'target_type',
        'target_id': 'target_id',
        'target_spec_code': 'target_spec_code'
    }

    def __init__(self, target_type=None, target_id=None, target_spec_code=None):
        """ResizeInstanceOption - a model defined in huaweicloud sdk"""
        
        

        self._target_type = None
        self._target_id = None
        self._target_spec_code = None
        self.discriminator = None

        if target_type is not None:
            self.target_type = target_type
        self.target_id = target_id
        self.target_spec_code = target_spec_code

    @property
    def target_type(self):
        """Gets the target_type of this ResizeInstanceOption.

        对象类型。 - 对于集群实例，该参数为必选。变更mongos节点规格时，取值为“mongos”；变更shard组规格时，取值为“shard”。 - 对于副本集和单节点实例，不传该参数。

        :return: The target_type of this ResizeInstanceOption.
        :rtype: str
        """
        return self._target_type

    @target_type.setter
    def target_type(self, target_type):
        """Sets the target_type of this ResizeInstanceOption.

        对象类型。 - 对于集群实例，该参数为必选。变更mongos节点规格时，取值为“mongos”；变更shard组规格时，取值为“shard”。 - 对于副本集和单节点实例，不传该参数。

        :param target_type: The target_type of this ResizeInstanceOption.
        :type: str
        """
        self._target_type = target_type

    @property
    def target_id(self):
        """Gets the target_id of this ResizeInstanceOption.

        待变更规格的节点ID或实例ID。 - 对于集群实例，变更mongos节点规格时，取值为mongos节点ID；变更shard组规格时，取值为shard组ID。 - 对于副本集实例，取值为相应的实例ID。 - 对于单节点实例，取值为相应的实例ID。

        :return: The target_id of this ResizeInstanceOption.
        :rtype: str
        """
        return self._target_id

    @target_id.setter
    def target_id(self, target_id):
        """Sets the target_id of this ResizeInstanceOption.

        待变更规格的节点ID或实例ID。 - 对于集群实例，变更mongos节点规格时，取值为mongos节点ID；变更shard组规格时，取值为shard组ID。 - 对于副本集实例，取值为相应的实例ID。 - 对于单节点实例，取值为相应的实例ID。

        :param target_id: The target_id of this ResizeInstanceOption.
        :type: str
        """
        self._target_id = target_id

    @property
    def target_spec_code(self):
        """Gets the target_spec_code of this ResizeInstanceOption.

        变更至新规格的资源规格编码。

        :return: The target_spec_code of this ResizeInstanceOption.
        :rtype: str
        """
        return self._target_spec_code

    @target_spec_code.setter
    def target_spec_code(self, target_spec_code):
        """Sets the target_spec_code of this ResizeInstanceOption.

        变更至新规格的资源规格编码。

        :param target_spec_code: The target_spec_code of this ResizeInstanceOption.
        :type: str
        """
        self._target_spec_code = target_spec_code

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
        if not isinstance(other, ResizeInstanceOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
