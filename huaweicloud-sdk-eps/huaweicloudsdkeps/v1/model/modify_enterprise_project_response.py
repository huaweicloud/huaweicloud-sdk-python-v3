# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ModifyEnterpriseProjectResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'enterprise_project': 'EpDetail'
    }

    attribute_map = {
        'enterprise_project': 'enterprise_project'
    }

    def __init__(self, enterprise_project=None):
        """ModifyEnterpriseProjectResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._enterprise_project = None
        self.discriminator = None

        if enterprise_project is not None:
            self.enterprise_project = enterprise_project

    @property
    def enterprise_project(self):
        """Gets the enterprise_project of this ModifyEnterpriseProjectResponse.


        :return: The enterprise_project of this ModifyEnterpriseProjectResponse.
        :rtype: EpDetail
        """
        return self._enterprise_project

    @enterprise_project.setter
    def enterprise_project(self, enterprise_project):
        """Sets the enterprise_project of this ModifyEnterpriseProjectResponse.


        :param enterprise_project: The enterprise_project of this ModifyEnterpriseProjectResponse.
        :type: EpDetail
        """
        self._enterprise_project = enterprise_project

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
        if not isinstance(other, ModifyEnterpriseProjectResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
