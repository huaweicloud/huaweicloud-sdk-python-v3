# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ShowOrgResResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'used_rec_storage': 'float',
        'used_accounts_count': 'int',
        'used_live_count': 'int',
        'conf_count': 'int',
        'conf_length': 'int',
        'active_attendee_count': 'int',
        'total_attendee_count': 'int'
    }

    attribute_map = {
        'used_rec_storage': 'usedRecStorage',
        'used_accounts_count': 'usedAccountsCount',
        'used_live_count': 'usedLiveCount',
        'conf_count': 'confCount',
        'conf_length': 'confLength',
        'active_attendee_count': 'activeAttendeeCount',
        'total_attendee_count': 'totalAttendeeCount'
    }

    def __init__(self, used_rec_storage=None, used_accounts_count=None, used_live_count=None, conf_count=None, conf_length=None, active_attendee_count=None, total_attendee_count=None):
        """ShowOrgResResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._used_rec_storage = None
        self._used_accounts_count = None
        self._used_live_count = None
        self._conf_count = None
        self._conf_length = None
        self._active_attendee_count = None
        self._total_attendee_count = None
        self.discriminator = None

        if used_rec_storage is not None:
            self.used_rec_storage = used_rec_storage
        if used_accounts_count is not None:
            self.used_accounts_count = used_accounts_count
        if used_live_count is not None:
            self.used_live_count = used_live_count
        if conf_count is not None:
            self.conf_count = conf_count
        if conf_length is not None:
            self.conf_length = conf_length
        if active_attendee_count is not None:
            self.active_attendee_count = active_attendee_count
        if total_attendee_count is not None:
            self.total_attendee_count = total_attendee_count

    @property
    def used_rec_storage(self):
        """Gets the used_rec_storage of this ShowOrgResResponse.

        已用录制存储空间(单位G)

        :return: The used_rec_storage of this ShowOrgResResponse.
        :rtype: float
        """
        return self._used_rec_storage

    @used_rec_storage.setter
    def used_rec_storage(self, used_rec_storage):
        """Sets the used_rec_storage of this ShowOrgResResponse.

        已用录制存储空间(单位G)

        :param used_rec_storage: The used_rec_storage of this ShowOrgResResponse.
        :type: float
        """
        self._used_rec_storage = used_rec_storage

    @property
    def used_accounts_count(self):
        """Gets the used_accounts_count of this ShowOrgResResponse.

        已用的企业并发数

        :return: The used_accounts_count of this ShowOrgResResponse.
        :rtype: int
        """
        return self._used_accounts_count

    @used_accounts_count.setter
    def used_accounts_count(self, used_accounts_count):
        """Sets the used_accounts_count of this ShowOrgResResponse.

        已用的企业并发数

        :param used_accounts_count: The used_accounts_count of this ShowOrgResResponse.
        :type: int
        """
        self._used_accounts_count = used_accounts_count

    @property
    def used_live_count(self):
        """Gets the used_live_count of this ShowOrgResResponse.

        已用的直播推流资源

        :return: The used_live_count of this ShowOrgResResponse.
        :rtype: int
        """
        return self._used_live_count

    @used_live_count.setter
    def used_live_count(self, used_live_count):
        """Sets the used_live_count of this ShowOrgResResponse.

        已用的直播推流资源

        :param used_live_count: The used_live_count of this ShowOrgResResponse.
        :type: int
        """
        self._used_live_count = used_live_count

    @property
    def conf_count(self):
        """Gets the conf_count of this ShowOrgResResponse.

        会议总次数

        :return: The conf_count of this ShowOrgResResponse.
        :rtype: int
        """
        return self._conf_count

    @conf_count.setter
    def conf_count(self, conf_count):
        """Sets the conf_count of this ShowOrgResResponse.

        会议总次数

        :param conf_count: The conf_count of this ShowOrgResResponse.
        :type: int
        """
        self._conf_count = conf_count

    @property
    def conf_length(self):
        """Gets the conf_length of this ShowOrgResResponse.

        会议总时长

        :return: The conf_length of this ShowOrgResResponse.
        :rtype: int
        """
        return self._conf_length

    @conf_length.setter
    def conf_length(self, conf_length):
        """Sets the conf_length of this ShowOrgResResponse.

        会议总时长

        :param conf_length: The conf_length of this ShowOrgResResponse.
        :type: int
        """
        self._conf_length = conf_length

    @property
    def active_attendee_count(self):
        """Gets the active_attendee_count of this ShowOrgResResponse.

        活跃用户数

        :return: The active_attendee_count of this ShowOrgResResponse.
        :rtype: int
        """
        return self._active_attendee_count

    @active_attendee_count.setter
    def active_attendee_count(self, active_attendee_count):
        """Sets the active_attendee_count of this ShowOrgResResponse.

        活跃用户数

        :param active_attendee_count: The active_attendee_count of this ShowOrgResResponse.
        :type: int
        """
        self._active_attendee_count = active_attendee_count

    @property
    def total_attendee_count(self):
        """Gets the total_attendee_count of this ShowOrgResResponse.

        总与会人数

        :return: The total_attendee_count of this ShowOrgResResponse.
        :rtype: int
        """
        return self._total_attendee_count

    @total_attendee_count.setter
    def total_attendee_count(self, total_attendee_count):
        """Sets the total_attendee_count of this ShowOrgResResponse.

        总与会人数

        :param total_attendee_count: The total_attendee_count of this ShowOrgResResponse.
        :type: int
        """
        self._total_attendee_count = total_attendee_count

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
        if not isinstance(other, ShowOrgResResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
