# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListDeploymentsResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'deployments': 'list[Deployment]'
    }

    attribute_map = {
        'count': 'count',
        'deployments': 'deployments'
    }

    def __init__(self, count=None, deployments=None):
        """ListDeploymentsResponse - a model defined in huaweicloud sdk"""
        
        super(ListDeploymentsResponse, self).__init__()

        self._count = None
        self._deployments = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if deployments is not None:
            self.deployments = deployments

    @property
    def count(self):
        """Gets the count of this ListDeploymentsResponse.

        部署计划列表的总和。

        :return: The count of this ListDeploymentsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListDeploymentsResponse.

        部署计划列表的总和。

        :param count: The count of this ListDeploymentsResponse.
        :type: int
        """
        self._count = count

    @property
    def deployments(self):
        """Gets the deployments of this ListDeploymentsResponse.

        部署计划列表。

        :return: The deployments of this ListDeploymentsResponse.
        :rtype: list[Deployment]
        """
        return self._deployments

    @deployments.setter
    def deployments(self, deployments):
        """Sets the deployments of this ListDeploymentsResponse.

        部署计划列表。

        :param deployments: The deployments of this ListDeploymentsResponse.
        :type: list[Deployment]
        """
        self._deployments = deployments

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
        if not isinstance(other, ListDeploymentsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
