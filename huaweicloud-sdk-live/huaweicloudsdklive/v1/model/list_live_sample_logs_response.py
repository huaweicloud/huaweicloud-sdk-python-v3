# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListLiveSampleLogsResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'domain': 'str',
        'logs': 'list[LogInfo]'
    }

    attribute_map = {
        'total': 'total',
        'domain': 'domain',
        'logs': 'logs'
    }

    def __init__(self, total=None, domain=None, logs=None):
        """ListLiveSampleLogsResponse - a model defined in huaweicloud sdk"""
        
        super(ListLiveSampleLogsResponse, self).__init__()

        self._total = None
        self._domain = None
        self._logs = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if domain is not None:
            self.domain = domain
        if logs is not None:
            self.logs = logs

    @property
    def total(self):
        """Gets the total of this ListLiveSampleLogsResponse.

        符合查询条件的总条目数

        :return: The total of this ListLiveSampleLogsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListLiveSampleLogsResponse.

        符合查询条件的总条目数

        :param total: The total of this ListLiveSampleLogsResponse.
        :type: int
        """
        self._total = total

    @property
    def domain(self):
        """Gets the domain of this ListLiveSampleLogsResponse.

        播放域名

        :return: The domain of this ListLiveSampleLogsResponse.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this ListLiveSampleLogsResponse.

        播放域名

        :param domain: The domain of this ListLiveSampleLogsResponse.
        :type: str
        """
        self._domain = domain

    @property
    def logs(self):
        """Gets the logs of this ListLiveSampleLogsResponse.

        日志信息列表

        :return: The logs of this ListLiveSampleLogsResponse.
        :rtype: list[LogInfo]
        """
        return self._logs

    @logs.setter
    def logs(self, logs):
        """Sets the logs of this ListLiveSampleLogsResponse.

        日志信息列表

        :param logs: The logs of this ListLiveSampleLogsResponse.
        :type: list[LogInfo]
        """
        self._logs = logs

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
        if not isinstance(other, ListLiveSampleLogsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
