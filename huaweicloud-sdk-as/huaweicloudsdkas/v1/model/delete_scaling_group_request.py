# coding: utf-8

import pprint
import re

import six





class DeleteScalingGroupRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'scaling_group_id': 'str',
        'force_delete': 'str'
    }

    attribute_map = {
        'scaling_group_id': 'scaling_group_id',
        'force_delete': 'force_delete'
    }

    def __init__(self, scaling_group_id=None, force_delete=None):
        """DeleteScalingGroupRequest - a model defined in huaweicloud sdk"""
        
        

        self._scaling_group_id = None
        self._force_delete = None
        self.discriminator = None

        self.scaling_group_id = scaling_group_id
        if force_delete is not None:
            self.force_delete = force_delete

    @property
    def scaling_group_id(self):
        """Gets the scaling_group_id of this DeleteScalingGroupRequest.


        :return: The scaling_group_id of this DeleteScalingGroupRequest.
        :rtype: str
        """
        return self._scaling_group_id

    @scaling_group_id.setter
    def scaling_group_id(self, scaling_group_id):
        """Sets the scaling_group_id of this DeleteScalingGroupRequest.


        :param scaling_group_id: The scaling_group_id of this DeleteScalingGroupRequest.
        :type: str
        """
        self._scaling_group_id = scaling_group_id

    @property
    def force_delete(self):
        """Gets the force_delete of this DeleteScalingGroupRequest.


        :return: The force_delete of this DeleteScalingGroupRequest.
        :rtype: str
        """
        return self._force_delete

    @force_delete.setter
    def force_delete(self, force_delete):
        """Sets the force_delete of this DeleteScalingGroupRequest.


        :param force_delete: The force_delete of this DeleteScalingGroupRequest.
        :type: str
        """
        self._force_delete = force_delete

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
        if not isinstance(other, DeleteScalingGroupRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
