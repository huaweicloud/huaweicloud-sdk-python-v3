# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AccessConfigQueryLogInfo:

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
        'log_stream_id': 'str',
        'log_group_name': 'str',
        'log_stream_name': 'str'
    }

    attribute_map = {
        'log_group_id': 'log_group_id',
        'log_stream_id': 'log_stream_id',
        'log_group_name': 'log_group_name',
        'log_stream_name': 'log_stream_name'
    }

    def __init__(self, log_group_id=None, log_stream_id=None, log_group_name=None, log_stream_name=None):
        """AccessConfigQueryLogInfo

        The model defined in huaweicloud sdk

        :param log_group_id: 日志组ID
        :type log_group_id: str
        :param log_stream_id: 日志流ID
        :type log_stream_id: str
        :param log_group_name: 日志组名称
        :type log_group_name: str
        :param log_stream_name: 日志流名称
        :type log_stream_name: str
        """
        
        

        self._log_group_id = None
        self._log_stream_id = None
        self._log_group_name = None
        self._log_stream_name = None
        self.discriminator = None

        if log_group_id is not None:
            self.log_group_id = log_group_id
        if log_stream_id is not None:
            self.log_stream_id = log_stream_id
        if log_group_name is not None:
            self.log_group_name = log_group_name
        if log_stream_name is not None:
            self.log_stream_name = log_stream_name

    @property
    def log_group_id(self):
        """Gets the log_group_id of this AccessConfigQueryLogInfo.

        日志组ID

        :return: The log_group_id of this AccessConfigQueryLogInfo.
        :rtype: str
        """
        return self._log_group_id

    @log_group_id.setter
    def log_group_id(self, log_group_id):
        """Sets the log_group_id of this AccessConfigQueryLogInfo.

        日志组ID

        :param log_group_id: The log_group_id of this AccessConfigQueryLogInfo.
        :type log_group_id: str
        """
        self._log_group_id = log_group_id

    @property
    def log_stream_id(self):
        """Gets the log_stream_id of this AccessConfigQueryLogInfo.

        日志流ID

        :return: The log_stream_id of this AccessConfigQueryLogInfo.
        :rtype: str
        """
        return self._log_stream_id

    @log_stream_id.setter
    def log_stream_id(self, log_stream_id):
        """Sets the log_stream_id of this AccessConfigQueryLogInfo.

        日志流ID

        :param log_stream_id: The log_stream_id of this AccessConfigQueryLogInfo.
        :type log_stream_id: str
        """
        self._log_stream_id = log_stream_id

    @property
    def log_group_name(self):
        """Gets the log_group_name of this AccessConfigQueryLogInfo.

        日志组名称

        :return: The log_group_name of this AccessConfigQueryLogInfo.
        :rtype: str
        """
        return self._log_group_name

    @log_group_name.setter
    def log_group_name(self, log_group_name):
        """Sets the log_group_name of this AccessConfigQueryLogInfo.

        日志组名称

        :param log_group_name: The log_group_name of this AccessConfigQueryLogInfo.
        :type log_group_name: str
        """
        self._log_group_name = log_group_name

    @property
    def log_stream_name(self):
        """Gets the log_stream_name of this AccessConfigQueryLogInfo.

        日志流名称

        :return: The log_stream_name of this AccessConfigQueryLogInfo.
        :rtype: str
        """
        return self._log_stream_name

    @log_stream_name.setter
    def log_stream_name(self, log_stream_name):
        """Sets the log_stream_name of this AccessConfigQueryLogInfo.

        日志流名称

        :param log_stream_name: The log_stream_name of this AccessConfigQueryLogInfo.
        :type log_stream_name: str
        """
        self._log_stream_name = log_stream_name

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
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AccessConfigQueryLogInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
