# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ShowScalingGroupResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'scaling_group': 'ScalingGroups'
    }

    attribute_map = {
        'scaling_group': 'scaling_group'
    }

    def __init__(self, scaling_group=None):
        """ShowScalingGroupResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._scaling_group = None
        self.discriminator = None

        if scaling_group is not None:
            self.scaling_group = scaling_group

    @property
    def scaling_group(self):
        """Gets the scaling_group of this ShowScalingGroupResponse.


        :return: The scaling_group of this ShowScalingGroupResponse.
        :rtype: ScalingGroups
        """
        return self._scaling_group

    @scaling_group.setter
    def scaling_group(self, scaling_group):
        """Sets the scaling_group of this ShowScalingGroupResponse.


        :param scaling_group: The scaling_group of this ShowScalingGroupResponse.
        :type: ScalingGroups
        """
        self._scaling_group = scaling_group

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
        if not isinstance(other, ShowScalingGroupResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
