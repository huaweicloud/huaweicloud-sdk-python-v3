# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListServiceTypesResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'service_types': 'list[ServiceType]'
    }

    attribute_map = {
        'service_types': 'service_types'
    }

    def __init__(self, service_types=None):
        """ListServiceTypesResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._service_types = None
        self.discriminator = None

        if service_types is not None:
            self.service_types = service_types

    @property
    def service_types(self):
        """Gets the service_types of this ListServiceTypesResponse.

        |参数名称：返回数据| |参数约束以及描述：返回数据|

        :return: The service_types of this ListServiceTypesResponse.
        :rtype: list[ServiceType]
        """
        return self._service_types

    @service_types.setter
    def service_types(self, service_types):
        """Sets the service_types of this ListServiceTypesResponse.

        |参数名称：返回数据| |参数约束以及描述：返回数据|

        :param service_types: The service_types of this ListServiceTypesResponse.
        :type: list[ServiceType]
        """
        self._service_types = service_types

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
        if not isinstance(other, ListServiceTypesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
