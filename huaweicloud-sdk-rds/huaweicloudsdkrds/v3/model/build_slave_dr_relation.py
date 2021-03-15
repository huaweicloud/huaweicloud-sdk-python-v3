# coding: utf-8

import pprint
import re

import six





class BuildSlaveDrRelation:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'target_instance_id': 'str',
        'target_project_id': 'str',
        'target_region': 'str',
        'target_ip': 'str'
    }

    attribute_map = {
        'target_instance_id': 'target_instance_id',
        'target_project_id': 'target_project_id',
        'target_region': 'target_region',
        'target_ip': 'target_ip'
    }

    def __init__(self, target_instance_id=None, target_project_id=None, target_region=None, target_ip=None):
        """BuildSlaveDrRelation - a model defined in huaweicloud sdk"""
        
        

        self._target_instance_id = None
        self._target_project_id = None
        self._target_region = None
        self._target_ip = None
        self.discriminator = None

        self.target_instance_id = target_instance_id
        self.target_project_id = target_project_id
        self.target_region = target_region
        self.target_ip = target_ip

    @property
    def target_instance_id(self):
        """Gets the target_instance_id of this BuildSlaveDrRelation.

        主实例的实例 ID。

        :return: The target_instance_id of this BuildSlaveDrRelation.
        :rtype: str
        """
        return self._target_instance_id

    @target_instance_id.setter
    def target_instance_id(self, target_instance_id):
        """Sets the target_instance_id of this BuildSlaveDrRelation.

        主实例的实例 ID。

        :param target_instance_id: The target_instance_id of this BuildSlaveDrRelation.
        :type: str
        """
        self._target_instance_id = target_instance_id

    @property
    def target_project_id(self):
        """Gets the target_project_id of this BuildSlaveDrRelation.

        主实例所在租户的项目 ID。

        :return: The target_project_id of this BuildSlaveDrRelation.
        :rtype: str
        """
        return self._target_project_id

    @target_project_id.setter
    def target_project_id(self, target_project_id):
        """Sets the target_project_id of this BuildSlaveDrRelation.

        主实例所在租户的项目 ID。

        :param target_project_id: The target_project_id of this BuildSlaveDrRelation.
        :type: str
        """
        self._target_project_id = target_project_id

    @property
    def target_region(self):
        """Gets the target_region of this BuildSlaveDrRelation.

        主实例所在的区域 ID。

        :return: The target_region of this BuildSlaveDrRelation.
        :rtype: str
        """
        return self._target_region

    @target_region.setter
    def target_region(self, target_region):
        """Sets the target_region of this BuildSlaveDrRelation.

        主实例所在的区域 ID。

        :param target_region: The target_region of this BuildSlaveDrRelation.
        :type: str
        """
        self._target_region = target_region

    @property
    def target_ip(self):
        """Gets the target_ip of this BuildSlaveDrRelation.

        主实例的数据虚拟IP（数据VIP）。

        :return: The target_ip of this BuildSlaveDrRelation.
        :rtype: str
        """
        return self._target_ip

    @target_ip.setter
    def target_ip(self, target_ip):
        """Sets the target_ip of this BuildSlaveDrRelation.

        主实例的数据虚拟IP（数据VIP）。

        :param target_ip: The target_ip of this BuildSlaveDrRelation.
        :type: str
        """
        self._target_ip = target_ip

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
        if not isinstance(other, BuildSlaveDrRelation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
