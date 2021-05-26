# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListOffSiteInstancesResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'offsite_backup_instance': 'list[OffsiteBackupInstance]',
        'total_count': 'int'
    }

    attribute_map = {
        'offsite_backup_instance': 'offsite_backup_instance',
        'total_count': 'total_count'
    }

    def __init__(self, offsite_backup_instance=None, total_count=None):
        """ListOffSiteInstancesResponse - a model defined in huaweicloud sdk"""
        
        super(ListOffSiteInstancesResponse, self).__init__()

        self._offsite_backup_instance = None
        self._total_count = None
        self.discriminator = None

        if offsite_backup_instance is not None:
            self.offsite_backup_instance = offsite_backup_instance
        if total_count is not None:
            self.total_count = total_count

    @property
    def offsite_backup_instance(self):
        """Gets the offsite_backup_instance of this ListOffSiteInstancesResponse.

        跨区域备份实例信息。

        :return: The offsite_backup_instance of this ListOffSiteInstancesResponse.
        :rtype: list[OffsiteBackupInstance]
        """
        return self._offsite_backup_instance

    @offsite_backup_instance.setter
    def offsite_backup_instance(self, offsite_backup_instance):
        """Sets the offsite_backup_instance of this ListOffSiteInstancesResponse.

        跨区域备份实例信息。

        :param offsite_backup_instance: The offsite_backup_instance of this ListOffSiteInstancesResponse.
        :type: list[OffsiteBackupInstance]
        """
        self._offsite_backup_instance = offsite_backup_instance

    @property
    def total_count(self):
        """Gets the total_count of this ListOffSiteInstancesResponse.

        总记录数。

        :return: The total_count of this ListOffSiteInstancesResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ListOffSiteInstancesResponse.

        总记录数。

        :param total_count: The total_count of this ListOffSiteInstancesResponse.
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
        if not isinstance(other, ListOffSiteInstancesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
