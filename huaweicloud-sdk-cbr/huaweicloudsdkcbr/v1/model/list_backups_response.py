# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListBackupsResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'backups': 'list[BackupResp]',
        'count': 'int'
    }

    attribute_map = {
        'backups': 'backups',
        'count': 'count'
    }

    def __init__(self, backups=None, count=None):
        """ListBackupsResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._backups = None
        self._count = None
        self.discriminator = None

        if backups is not None:
            self.backups = backups
        if count is not None:
            self.count = count

    @property
    def backups(self):
        """Gets the backups of this ListBackupsResponse.

        备份列表

        :return: The backups of this ListBackupsResponse.
        :rtype: list[BackupResp]
        """
        return self._backups

    @backups.setter
    def backups(self, backups):
        """Sets the backups of this ListBackupsResponse.

        备份列表

        :param backups: The backups of this ListBackupsResponse.
        :type: list[BackupResp]
        """
        self._backups = backups

    @property
    def count(self):
        """Gets the count of this ListBackupsResponse.

        备份个数

        :return: The count of this ListBackupsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListBackupsResponse.

        备份个数

        :param count: The count of this ListBackupsResponse.
        :type: int
        """
        self._count = count

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
        if not isinstance(other, ListBackupsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
