# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListJobInstancesResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'instances': 'list[JobInstance]'
    }

    attribute_map = {
        'total': 'total',
        'instances': 'instances'
    }

    def __init__(self, total=None, instances=None):
        """ListJobInstancesResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._total = None
        self._instances = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if instances is not None:
            self.instances = instances

    @property
    def total(self):
        """Gets the total of this ListJobInstancesResponse.


        :return: The total of this ListJobInstancesResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListJobInstancesResponse.


        :param total: The total of this ListJobInstancesResponse.
        :type: int
        """
        self._total = total

    @property
    def instances(self):
        """Gets the instances of this ListJobInstancesResponse.


        :return: The instances of this ListJobInstancesResponse.
        :rtype: list[JobInstance]
        """
        return self._instances

    @instances.setter
    def instances(self, instances):
        """Sets the instances of this ListJobInstancesResponse.


        :param instances: The instances of this ListJobInstancesResponse.
        :type: list[JobInstance]
        """
        self._instances = instances

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
        if not isinstance(other, ListJobInstancesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
