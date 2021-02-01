# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class DownloadSlowlogResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'list': 'list[DownloadSlowlogResult]',
        'status': 'str',
        'total_record': 'str'
    }

    attribute_map = {
        'list': 'list',
        'status': 'status',
        'total_record': 'total_record'
    }

    def __init__(self, list=None, status=None, total_record=None):
        """DownloadSlowlogResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._list = None
        self._status = None
        self._total_record = None
        self.discriminator = None

        if list is not None:
            self.list = list
        if status is not None:
            self.status = status
        if total_record is not None:
            self.total_record = total_record

    @property
    def list(self):
        """Gets the list of this DownloadSlowlogResponse.

        具体信息。

        :return: The list of this DownloadSlowlogResponse.
        :rtype: list[DownloadSlowlogResult]
        """
        return self._list

    @list.setter
    def list(self, list):
        """Sets the list of this DownloadSlowlogResponse.

        具体信息。

        :param list: The list of this DownloadSlowlogResponse.
        :type: list[DownloadSlowlogResult]
        """
        self._list = list

    @property
    def status(self):
        """Gets the status of this DownloadSlowlogResponse.

        查询状态。

        :return: The status of this DownloadSlowlogResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DownloadSlowlogResponse.

        查询状态。

        :param status: The status of this DownloadSlowlogResponse.
        :type: str
        """
        self._status = status

    @property
    def total_record(self):
        """Gets the total_record of this DownloadSlowlogResponse.

        总记录数。

        :return: The total_record of this DownloadSlowlogResponse.
        :rtype: str
        """
        return self._total_record

    @total_record.setter
    def total_record(self, total_record):
        """Sets the total_record of this DownloadSlowlogResponse.

        总记录数。

        :param total_record: The total_record of this DownloadSlowlogResponse.
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
        if not isinstance(other, DownloadSlowlogResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
