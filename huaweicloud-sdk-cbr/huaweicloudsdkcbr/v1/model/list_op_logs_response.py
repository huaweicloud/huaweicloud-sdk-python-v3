# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListOpLogsResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'operation_logs': 'list[OperationLog]',
        'count': 'int'
    }

    attribute_map = {
        'operation_logs': 'operation_logs',
        'count': 'count'
    }

    def __init__(self, operation_logs=None, count=None):
        """ListOpLogsResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._operation_logs = None
        self._count = None
        self.discriminator = None

        if operation_logs is not None:
            self.operation_logs = operation_logs
        if count is not None:
            self.count = count

    @property
    def operation_logs(self):
        """Gets the operation_logs of this ListOpLogsResponse.

        任务列表

        :return: The operation_logs of this ListOpLogsResponse.
        :rtype: list[OperationLog]
        """
        return self._operation_logs

    @operation_logs.setter
    def operation_logs(self, operation_logs):
        """Sets the operation_logs of this ListOpLogsResponse.

        任务列表

        :param operation_logs: The operation_logs of this ListOpLogsResponse.
        :type: list[OperationLog]
        """
        self._operation_logs = operation_logs

    @property
    def count(self):
        """Gets the count of this ListOpLogsResponse.

        任务个数

        :return: The count of this ListOpLogsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListOpLogsResponse.

        任务个数

        :param count: The count of this ListOpLogsResponse.
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
        if not isinstance(other, ListOpLogsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
