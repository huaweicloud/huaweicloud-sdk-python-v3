# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListEnterpriseProjectResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'enterprise_projects': 'list[EpDetail]',
        'total_count': 'int'
    }

    attribute_map = {
        'enterprise_projects': 'enterprise_projects',
        'total_count': 'total_count'
    }

    def __init__(self, enterprise_projects=None, total_count=None):
        """ListEnterpriseProjectResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._enterprise_projects = None
        self._total_count = None
        self.discriminator = None

        if enterprise_projects is not None:
            self.enterprise_projects = enterprise_projects
        if total_count is not None:
            self.total_count = total_count

    @property
    def enterprise_projects(self):
        """Gets the enterprise_projects of this ListEnterpriseProjectResponse.

        企业项目列表

        :return: The enterprise_projects of this ListEnterpriseProjectResponse.
        :rtype: list[EpDetail]
        """
        return self._enterprise_projects

    @enterprise_projects.setter
    def enterprise_projects(self, enterprise_projects):
        """Sets the enterprise_projects of this ListEnterpriseProjectResponse.

        企业项目列表

        :param enterprise_projects: The enterprise_projects of this ListEnterpriseProjectResponse.
        :type: list[EpDetail]
        """
        self._enterprise_projects = enterprise_projects

    @property
    def total_count(self):
        """Gets the total_count of this ListEnterpriseProjectResponse.

        企业项目总数

        :return: The total_count of this ListEnterpriseProjectResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ListEnterpriseProjectResponse.

        企业项目总数

        :param total_count: The total_count of this ListEnterpriseProjectResponse.
        :type: int
        """
        self._total_count = total_count

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
        if not isinstance(other, ListEnterpriseProjectResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
