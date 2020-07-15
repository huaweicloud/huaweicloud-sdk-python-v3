# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListGroupReplicationInfoResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'group_list': 'list[InstanceGroupListInfo]',
        'group_count': 'str'
    }

    attribute_map = {
        'group_list': 'group_list',
        'group_count': 'group_count'
    }

    def __init__(self, group_list=None, group_count=None):
        """ListGroupReplicationInfoResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._group_list = None
        self._group_count = None
        self.discriminator = None

        if group_list is not None:
            self.group_list = group_list
        if group_count is not None:
            self.group_count = group_count

    @property
    def group_list(self):
        """Gets the group_list of this ListGroupReplicationInfoResponse.

        分片列表

        :return: The group_list of this ListGroupReplicationInfoResponse.
        :rtype: list[InstanceGroupListInfo]
        """
        return self._group_list

    @group_list.setter
    def group_list(self, group_list):
        """Sets the group_list of this ListGroupReplicationInfoResponse.

        分片列表

        :param group_list: The group_list of this ListGroupReplicationInfoResponse.
        :type: list[InstanceGroupListInfo]
        """
        self._group_list = group_list

    @property
    def group_count(self):
        """Gets the group_count of this ListGroupReplicationInfoResponse.

        实例分片总数。

        :return: The group_count of this ListGroupReplicationInfoResponse.
        :rtype: str
        """
        return self._group_count

    @group_count.setter
    def group_count(self, group_count):
        """Sets the group_count of this ListGroupReplicationInfoResponse.

        实例分片总数。

        :param group_count: The group_count of this ListGroupReplicationInfoResponse.
        :type: str
        """
        self._group_count = group_count

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
        if not isinstance(other, ListGroupReplicationInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
