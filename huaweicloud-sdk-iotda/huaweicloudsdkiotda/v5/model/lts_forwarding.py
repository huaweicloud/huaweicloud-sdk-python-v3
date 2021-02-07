# coding: utf-8

import pprint
import re

import six





class LtsForwarding:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'log_group_id': 'str',
        'log_stream_id': 'str'
    }

    attribute_map = {
        'log_group_id': 'log_group_id',
        'log_stream_id': 'log_stream_id'
    }

    def __init__(self, log_group_id=None, log_stream_id=None):
        """LtsForwarding - a model defined in huaweicloud sdk"""
        
        

        self._log_group_id = None
        self._log_stream_id = None
        self.discriminator = None

        self.log_group_id = log_group_id
        self.log_stream_id = log_stream_id

    @property
    def log_group_id(self):
        """Gets the log_group_id of this LtsForwarding.

        用于接收日志的日志组Id，通过调用LTS服务创建日志组接口获取(https://support.huaweicloud.com/api-lts/lts_api_0012.html)。

        :return: The log_group_id of this LtsForwarding.
        :rtype: str
        """
        return self._log_group_id

    @log_group_id.setter
    def log_group_id(self, log_group_id):
        """Sets the log_group_id of this LtsForwarding.

        用于接收日志的日志组Id，通过调用LTS服务创建日志组接口获取(https://support.huaweicloud.com/api-lts/lts_api_0012.html)。

        :param log_group_id: The log_group_id of this LtsForwarding.
        :type: str
        """
        self._log_group_id = log_group_id

    @property
    def log_stream_id(self):
        """Gets the log_stream_id of this LtsForwarding.

        用于接收日志的日志流Id，通过调用LTS服务创建日志流接口获取(https://support.huaweicloud.com/api-lts/lts_api_0016.html)。

        :return: The log_stream_id of this LtsForwarding.
        :rtype: str
        """
        return self._log_stream_id

    @log_stream_id.setter
    def log_stream_id(self, log_stream_id):
        """Sets the log_stream_id of this LtsForwarding.

        用于接收日志的日志流Id，通过调用LTS服务创建日志流接口获取(https://support.huaweicloud.com/api-lts/lts_api_0016.html)。

        :param log_stream_id: The log_stream_id of this LtsForwarding.
        :type: str
        """
        self._log_stream_id = log_stream_id

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
        if not isinstance(other, LtsForwarding):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
