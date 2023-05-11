# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowEventDetailRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'trace_id': 'str',
        'span_id': 'str',
        'event_id': 'str',
        'env_id': 'int'
    }

    attribute_map = {
        'trace_id': 'trace_id',
        'span_id': 'span_id',
        'event_id': 'event_id',
        'env_id': 'env_id'
    }

    def __init__(self, trace_id=None, span_id=None, event_id=None, env_id=None):
        """ShowEventDetailRequest

        The model defined in huaweicloud sdk

        :param trace_id: trace id。
        :type trace_id: str
        :param span_id: span id。
        :type span_id: str
        :param event_id: event id。
        :type event_id: str
        :param env_id: 环境id。
        :type env_id: int
        """
        
        

        self._trace_id = None
        self._span_id = None
        self._event_id = None
        self._env_id = None
        self.discriminator = None

        self.trace_id = trace_id
        self.span_id = span_id
        self.event_id = event_id
        self.env_id = env_id

    @property
    def trace_id(self):
        """Gets the trace_id of this ShowEventDetailRequest.

        trace id。

        :return: The trace_id of this ShowEventDetailRequest.
        :rtype: str
        """
        return self._trace_id

    @trace_id.setter
    def trace_id(self, trace_id):
        """Sets the trace_id of this ShowEventDetailRequest.

        trace id。

        :param trace_id: The trace_id of this ShowEventDetailRequest.
        :type trace_id: str
        """
        self._trace_id = trace_id

    @property
    def span_id(self):
        """Gets the span_id of this ShowEventDetailRequest.

        span id。

        :return: The span_id of this ShowEventDetailRequest.
        :rtype: str
        """
        return self._span_id

    @span_id.setter
    def span_id(self, span_id):
        """Sets the span_id of this ShowEventDetailRequest.

        span id。

        :param span_id: The span_id of this ShowEventDetailRequest.
        :type span_id: str
        """
        self._span_id = span_id

    @property
    def event_id(self):
        """Gets the event_id of this ShowEventDetailRequest.

        event id。

        :return: The event_id of this ShowEventDetailRequest.
        :rtype: str
        """
        return self._event_id

    @event_id.setter
    def event_id(self, event_id):
        """Sets the event_id of this ShowEventDetailRequest.

        event id。

        :param event_id: The event_id of this ShowEventDetailRequest.
        :type event_id: str
        """
        self._event_id = event_id

    @property
    def env_id(self):
        """Gets the env_id of this ShowEventDetailRequest.

        环境id。

        :return: The env_id of this ShowEventDetailRequest.
        :rtype: int
        """
        return self._env_id

    @env_id.setter
    def env_id(self, env_id):
        """Sets the env_id of this ShowEventDetailRequest.

        环境id。

        :param env_id: The env_id of this ShowEventDetailRequest.
        :type env_id: int
        """
        self._env_id = env_id

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
        if not isinstance(other, ShowEventDetailRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
