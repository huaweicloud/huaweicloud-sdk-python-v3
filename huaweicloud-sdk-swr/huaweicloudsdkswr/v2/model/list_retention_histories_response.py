# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListRetentionHistoriesResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'retention_log': 'list[RetentionLog]',
        'total': 'int',
        'content_range': 'str'
    }

    attribute_map = {
        'retention_log': 'retention_log',
        'total': 'total',
        'content_range': 'Content-Range'
    }

    def __init__(self, retention_log=None, total=None, content_range=None):
        """ListRetentionHistoriesResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._retention_log = None
        self._total = None
        self._content_range = None
        self.discriminator = None

        if retention_log is not None:
            self.retention_log = retention_log
        if total is not None:
            self.total = total
        if content_range is not None:
            self.content_range = content_range

    @property
    def retention_log(self):
        """Gets the retention_log of this ListRetentionHistoriesResponse.

        镜像老化日志

        :return: The retention_log of this ListRetentionHistoriesResponse.
        :rtype: list[RetentionLog]
        """
        return self._retention_log

    @retention_log.setter
    def retention_log(self, retention_log):
        """Sets the retention_log of this ListRetentionHistoriesResponse.

        镜像老化日志

        :param retention_log: The retention_log of this ListRetentionHistoriesResponse.
        :type: list[RetentionLog]
        """
        self._retention_log = retention_log

    @property
    def total(self):
        """Gets the total of this ListRetentionHistoriesResponse.

        总个数

        :return: The total of this ListRetentionHistoriesResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListRetentionHistoriesResponse.

        总个数

        :param total: The total of this ListRetentionHistoriesResponse.
        :type: int
        """
        self._total = total

    @property
    def content_range(self):
        """Gets the content_range of this ListRetentionHistoriesResponse.


        :return: The content_range of this ListRetentionHistoriesResponse.
        :rtype: str
        """
        return self._content_range

    @content_range.setter
    def content_range(self, content_range):
        """Sets the content_range of this ListRetentionHistoriesResponse.


        :param content_range: The content_range of this ListRetentionHistoriesResponse.
        :type: str
        """
        self._content_range = content_range

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
        if not isinstance(other, ListRetentionHistoriesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
