# coding: utf-8

import pprint
import re

import six





class ListLogStreamRequest:


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
        'tag': 'str'
    }

    attribute_map = {
        'log_group_id': 'log_group_id',
        'tag': 'tag'
    }

    def __init__(self, log_group_id=None, tag=None):
        """ListLogStreamRequest - a model defined in huaweicloud sdk"""
        
        

        self._log_group_id = None
        self._tag = None
        self.discriminator = None

        self.log_group_id = log_group_id
        if tag is not None:
            self.tag = tag

    @property
    def log_group_id(self):
        """Gets the log_group_id of this ListLogStreamRequest.

        租户想查询的日志流所在的日志组的groupid，一般为36位字符串。 

        :return: The log_group_id of this ListLogStreamRequest.
        :rtype: str
        """
        return self._log_group_id

    @log_group_id.setter
    def log_group_id(self, log_group_id):
        """Sets the log_group_id of this ListLogStreamRequest.

        租户想查询的日志流所在的日志组的groupid，一般为36位字符串。 

        :param log_group_id: The log_group_id of this ListLogStreamRequest.
        :type: str
        """
        self._log_group_id = log_group_id

    @property
    def tag(self):
        """Gets the tag of this ListLogStreamRequest.

        按条件搜索，内容设置为日志流的tag键值对，比如k1=v1； 

        :return: The tag of this ListLogStreamRequest.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this ListLogStreamRequest.

        按条件搜索，内容设置为日志流的tag键值对，比如k1=v1； 

        :param tag: The tag of this ListLogStreamRequest.
        :type: str
        """
        self._tag = tag

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
        if not isinstance(other, ListLogStreamRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other