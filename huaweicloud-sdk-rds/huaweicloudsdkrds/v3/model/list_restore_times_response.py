# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListRestoreTimesResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'restore_time': 'list[GetRestoreTimeResponseRestoreTime]'
    }

    attribute_map = {
        'restore_time': 'restore_time'
    }

    def __init__(self, restore_time=None):
        """ListRestoreTimesResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._restore_time = None
        self.discriminator = None

        if restore_time is not None:
            self.restore_time = restore_time

    @property
    def restore_time(self):
        """Gets the restore_time of this ListRestoreTimesResponse.

        可恢复时间段列表。

        :return: The restore_time of this ListRestoreTimesResponse.
        :rtype: list[GetRestoreTimeResponseRestoreTime]
        """
        return self._restore_time

    @restore_time.setter
    def restore_time(self, restore_time):
        """Sets the restore_time of this ListRestoreTimesResponse.

        可恢复时间段列表。

        :param restore_time: The restore_time of this ListRestoreTimesResponse.
        :type: list[GetRestoreTimeResponseRestoreTime]
        """
        self._restore_time = restore_time

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
        if not isinstance(other, ListRestoreTimesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
