# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListHookInstancesResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'instance_hanging_info': 'list[InstanceHangingInfos]'
    }

    attribute_map = {
        'instance_hanging_info': 'instance_hanging_info'
    }

    def __init__(self, instance_hanging_info=None):
        """ListHookInstancesResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._instance_hanging_info = None
        self.discriminator = None

        if instance_hanging_info is not None:
            self.instance_hanging_info = instance_hanging_info

    @property
    def instance_hanging_info(self):
        """Gets the instance_hanging_info of this ListHookInstancesResponse.

        伸缩实例生命周期挂钩列表。

        :return: The instance_hanging_info of this ListHookInstancesResponse.
        :rtype: list[InstanceHangingInfos]
        """
        return self._instance_hanging_info

    @instance_hanging_info.setter
    def instance_hanging_info(self, instance_hanging_info):
        """Sets the instance_hanging_info of this ListHookInstancesResponse.

        伸缩实例生命周期挂钩列表。

        :param instance_hanging_info: The instance_hanging_info of this ListHookInstancesResponse.
        :type: list[InstanceHangingInfos]
        """
        self._instance_hanging_info = instance_hanging_info

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
        if not isinstance(other, ListHookInstancesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
