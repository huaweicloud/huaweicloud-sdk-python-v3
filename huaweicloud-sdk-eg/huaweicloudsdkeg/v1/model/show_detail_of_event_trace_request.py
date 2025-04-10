# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDetailOfEventTraceRequest:

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
        'channel_id': 'str'
    }

    attribute_map = {
        'trace_id': 'trace_id',
        'channel_id': 'channel_id'
    }

    def __init__(self, trace_id=None, channel_id=None):
        r"""ShowDetailOfEventTraceRequest

        The model defined in huaweicloud sdk

        :param trace_id: 事件唯一标识
        :type trace_id: str
        :param channel_id: 通道id
        :type channel_id: str
        """
        
        

        self._trace_id = None
        self._channel_id = None
        self.discriminator = None

        self.trace_id = trace_id
        self.channel_id = channel_id

    @property
    def trace_id(self):
        r"""Gets the trace_id of this ShowDetailOfEventTraceRequest.

        事件唯一标识

        :return: The trace_id of this ShowDetailOfEventTraceRequest.
        :rtype: str
        """
        return self._trace_id

    @trace_id.setter
    def trace_id(self, trace_id):
        r"""Sets the trace_id of this ShowDetailOfEventTraceRequest.

        事件唯一标识

        :param trace_id: The trace_id of this ShowDetailOfEventTraceRequest.
        :type trace_id: str
        """
        self._trace_id = trace_id

    @property
    def channel_id(self):
        r"""Gets the channel_id of this ShowDetailOfEventTraceRequest.

        通道id

        :return: The channel_id of this ShowDetailOfEventTraceRequest.
        :rtype: str
        """
        return self._channel_id

    @channel_id.setter
    def channel_id(self, channel_id):
        r"""Sets the channel_id of this ShowDetailOfEventTraceRequest.

        通道id

        :param channel_id: The channel_id of this ShowDetailOfEventTraceRequest.
        :type channel_id: str
        """
        self._channel_id = channel_id

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
        if not isinstance(other, ShowDetailOfEventTraceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
