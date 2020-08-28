# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListProjectWorkHoursResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'work_hours': 'list[ShowProjectWorkHoursResponseBodyWorkHours]',
        'total': 'int'
    }

    attribute_map = {
        'work_hours': 'work_hours',
        'total': 'total'
    }

    def __init__(self, work_hours=None, total=None):
        """ListProjectWorkHoursResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._work_hours = None
        self._total = None
        self.discriminator = None

        if work_hours is not None:
            self.work_hours = work_hours
        if total is not None:
            self.total = total

    @property
    def work_hours(self):
        """Gets the work_hours of this ListProjectWorkHoursResponse.

        工时列表

        :return: The work_hours of this ListProjectWorkHoursResponse.
        :rtype: list[ShowProjectWorkHoursResponseBodyWorkHours]
        """
        return self._work_hours

    @work_hours.setter
    def work_hours(self, work_hours):
        """Sets the work_hours of this ListProjectWorkHoursResponse.

        工时列表

        :param work_hours: The work_hours of this ListProjectWorkHoursResponse.
        :type: list[ShowProjectWorkHoursResponseBodyWorkHours]
        """
        self._work_hours = work_hours

    @property
    def total(self):
        """Gets the total of this ListProjectWorkHoursResponse.

        总数

        :return: The total of this ListProjectWorkHoursResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListProjectWorkHoursResponse.

        总数

        :param total: The total of this ListProjectWorkHoursResponse.
        :type: int
        """
        self._total = total

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
        if not isinstance(other, ListProjectWorkHoursResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
