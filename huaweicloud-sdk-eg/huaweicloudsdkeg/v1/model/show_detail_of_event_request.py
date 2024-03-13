# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDetailOfEventRequest:

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
        """ShowDetailOfEventRequest

        The model defined in huaweicloud sdk

        :param trace_id: 追踪事件的uniqueId
        :type trace_id: str
        :param channel_id: 指定查询的事件通道ID
        :type channel_id: str
        """
        
        

        self._trace_id = None
        self._channel_id = None
        self.discriminator = None

        self.trace_id = trace_id
        if channel_id is not None:
            self.channel_id = channel_id

    @property
    def trace_id(self):
        """Gets the trace_id of this ShowDetailOfEventRequest.

        追踪事件的uniqueId

        :return: The trace_id of this ShowDetailOfEventRequest.
        :rtype: str
        """
        return self._trace_id

    @trace_id.setter
    def trace_id(self, trace_id):
        """Sets the trace_id of this ShowDetailOfEventRequest.

        追踪事件的uniqueId

        :param trace_id: The trace_id of this ShowDetailOfEventRequest.
        :type trace_id: str
        """
        self._trace_id = trace_id

    @property
    def channel_id(self):
        """Gets the channel_id of this ShowDetailOfEventRequest.

        指定查询的事件通道ID

        :return: The channel_id of this ShowDetailOfEventRequest.
        :rtype: str
        """
        return self._channel_id

    @channel_id.setter
    def channel_id(self, channel_id):
        """Sets the channel_id of this ShowDetailOfEventRequest.

        指定查询的事件通道ID

        :param channel_id: The channel_id of this ShowDetailOfEventRequest.
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
        if not isinstance(other, ShowDetailOfEventRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
