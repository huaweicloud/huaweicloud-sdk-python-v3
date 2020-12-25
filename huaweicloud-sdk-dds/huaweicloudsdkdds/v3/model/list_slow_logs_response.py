# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListSlowLogsResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'slow_log_list': 'list[SlowlogResult]',
        'total_record': 'str'
    }

    attribute_map = {
        'slow_log_list': 'slow_log_list',
        'total_record': 'total_record'
    }

    def __init__(self, slow_log_list=None, total_record=None):
        """ListSlowLogsResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._slow_log_list = None
        self._total_record = None
        self.discriminator = None

        if slow_log_list is not None:
            self.slow_log_list = slow_log_list
        if total_record is not None:
            self.total_record = total_record

    @property
    def slow_log_list(self):
        """Gets the slow_log_list of this ListSlowLogsResponse.

        具体信息。

        :return: The slow_log_list of this ListSlowLogsResponse.
        :rtype: list[SlowlogResult]
        """
        return self._slow_log_list

    @slow_log_list.setter
    def slow_log_list(self, slow_log_list):
        """Sets the slow_log_list of this ListSlowLogsResponse.

        具体信息。

        :param slow_log_list: The slow_log_list of this ListSlowLogsResponse.
        :type: list[SlowlogResult]
        """
        self._slow_log_list = slow_log_list

    @property
    def total_record(self):
        """Gets the total_record of this ListSlowLogsResponse.

        数据库版本总记录数。

        :return: The total_record of this ListSlowLogsResponse.
        :rtype: str
        """
        return self._total_record

    @total_record.setter
    def total_record(self, total_record):
        """Sets the total_record of this ListSlowLogsResponse.

        数据库版本总记录数。

        :param total_record: The total_record of this ListSlowLogsResponse.
        :type: str
        """
        self._total_record = total_record

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
        if not isinstance(other, ListSlowLogsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
