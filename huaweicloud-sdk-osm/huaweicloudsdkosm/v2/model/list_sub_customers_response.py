# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListSubCustomersResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'sub_customer_infos': 'list[SubCutomerInfoV2]'
    }

    attribute_map = {
        'sub_customer_infos': 'sub_customer_infos'
    }

    def __init__(self, sub_customer_infos=None):
        """ListSubCustomersResponse - a model defined in huaweicloud sdk"""
        
        super(ListSubCustomersResponse, self).__init__()

        self._sub_customer_infos = None
        self.discriminator = None

        if sub_customer_infos is not None:
            self.sub_customer_infos = sub_customer_infos

    @property
    def sub_customer_infos(self):
        """Gets the sub_customer_infos of this ListSubCustomersResponse.

        子用户列表

        :return: The sub_customer_infos of this ListSubCustomersResponse.
        :rtype: list[SubCutomerInfoV2]
        """
        return self._sub_customer_infos

    @sub_customer_infos.setter
    def sub_customer_infos(self, sub_customer_infos):
        """Sets the sub_customer_infos of this ListSubCustomersResponse.

        子用户列表

        :param sub_customer_infos: The sub_customer_infos of this ListSubCustomersResponse.
        :type: list[SubCutomerInfoV2]
        """
        self._sub_customer_infos = sub_customer_infos

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
        if not isinstance(other, ListSubCustomersResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other