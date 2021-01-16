# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListOffSiteBackupsResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'offsite_backups': 'list[OffSiteBackupForList]',
        'total_count': 'int'
    }

    attribute_map = {
        'offsite_backups': 'offsite_backups',
        'total_count': 'total_count'
    }

    def __init__(self, offsite_backups=None, total_count=None):
        """ListOffSiteBackupsResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._offsite_backups = None
        self._total_count = None
        self.discriminator = None

        if offsite_backups is not None:
            self.offsite_backups = offsite_backups
        if total_count is not None:
            self.total_count = total_count

    @property
    def offsite_backups(self):
        """Gets the offsite_backups of this ListOffSiteBackupsResponse.

        跨区域备份信息。

        :return: The offsite_backups of this ListOffSiteBackupsResponse.
        :rtype: list[OffSiteBackupForList]
        """
        return self._offsite_backups

    @offsite_backups.setter
    def offsite_backups(self, offsite_backups):
        """Sets the offsite_backups of this ListOffSiteBackupsResponse.

        跨区域备份信息。

        :param offsite_backups: The offsite_backups of this ListOffSiteBackupsResponse.
        :type: list[OffSiteBackupForList]
        """
        self._offsite_backups = offsite_backups

    @property
    def total_count(self):
        """Gets the total_count of this ListOffSiteBackupsResponse.

        总记录数。

        :return: The total_count of this ListOffSiteBackupsResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ListOffSiteBackupsResponse.

        总记录数。

        :param total_count: The total_count of this ListOffSiteBackupsResponse.
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
        if not isinstance(other, ListOffSiteBackupsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
