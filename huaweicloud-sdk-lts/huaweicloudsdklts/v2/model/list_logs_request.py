# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListLogsRequest:

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
        'body': 'QueryLtsLogParams'
    }

    attribute_map = {
        'log_group_id': 'log_group_id',
        'log_stream_id': 'log_stream_id',
        'body': 'body'
    }

    def __init__(self, log_group_id=None, log_stream_id=None, body=None):
        """ListLogsRequest

        The model defined in huaweicloud sdk

        :param log_group_id: 日志组id。
        :type log_group_id: str
        :param log_stream_id: 日志流id。
        :type log_stream_id: str
        :param body: Body of the ListLogsRequest
        :type body: :class:`huaweicloudsdklts.v2.QueryLtsLogParams`
        """
        
        

        self._log_group_id = None
        self._log_stream_id = None
        self._body = None
        self.discriminator = None

        self.log_group_id = log_group_id
        self.log_stream_id = log_stream_id
        if body is not None:
            self.body = body

    @property
    def log_group_id(self):
        """Gets the log_group_id of this ListLogsRequest.

        日志组id。

        :return: The log_group_id of this ListLogsRequest.
        :rtype: str
        """
        return self._log_group_id

    @log_group_id.setter
    def log_group_id(self, log_group_id):
        """Sets the log_group_id of this ListLogsRequest.

        日志组id。

        :param log_group_id: The log_group_id of this ListLogsRequest.
        :type log_group_id: str
        """
        self._log_group_id = log_group_id

    @property
    def log_stream_id(self):
        """Gets the log_stream_id of this ListLogsRequest.

        日志流id。

        :return: The log_stream_id of this ListLogsRequest.
        :rtype: str
        """
        return self._log_stream_id

    @log_stream_id.setter
    def log_stream_id(self, log_stream_id):
        """Sets the log_stream_id of this ListLogsRequest.

        日志流id。

        :param log_stream_id: The log_stream_id of this ListLogsRequest.
        :type log_stream_id: str
        """
        self._log_stream_id = log_stream_id

    @property
    def body(self):
        """Gets the body of this ListLogsRequest.

        :return: The body of this ListLogsRequest.
        :rtype: :class:`huaweicloudsdklts.v2.QueryLtsLogParams`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this ListLogsRequest.

        :param body: The body of this ListLogsRequest.
        :type body: :class:`huaweicloudsdklts.v2.QueryLtsLogParams`
        """
        self._body = body

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
        if not isinstance(other, ListLogsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
