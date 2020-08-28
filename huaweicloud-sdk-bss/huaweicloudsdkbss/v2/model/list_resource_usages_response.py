# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListResourceUsagesResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'package_usage_infos': 'list[PackageUsageInfo]'
    }

    attribute_map = {
        'package_usage_infos': 'package_usage_infos'
    }

    def __init__(self, package_usage_infos=None):
        """ListResourceUsagesResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._package_usage_infos = None
        self.discriminator = None

        if package_usage_infos is not None:
            self.package_usage_infos = package_usage_infos

    @property
    def package_usage_infos(self):
        """Gets the package_usage_infos of this ListResourceUsagesResponse.

        |参数名称：套餐包使用量信息| |参数的约束及描述：套餐包使用量信息|

        :return: The package_usage_infos of this ListResourceUsagesResponse.
        :rtype: list[PackageUsageInfo]
        """
        return self._package_usage_infos

    @package_usage_infos.setter
    def package_usage_infos(self, package_usage_infos):
        """Sets the package_usage_infos of this ListResourceUsagesResponse.

        |参数名称：套餐包使用量信息| |参数的约束及描述：套餐包使用量信息|

        :param package_usage_infos: The package_usage_infos of this ListResourceUsagesResponse.
        :type: list[PackageUsageInfo]
        """
        self._package_usage_infos = package_usage_infos

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
        if not isinstance(other, ListResourceUsagesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
