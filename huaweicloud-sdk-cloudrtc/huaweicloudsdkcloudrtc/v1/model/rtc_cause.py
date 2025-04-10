# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RTCCause:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ts': 'str',
        'event_id': 'str',
        'peer_id': 'str'
    }

    attribute_map = {
        'ts': 'ts',
        'event_id': 'event_id',
        'peer_id': 'peer_id'
    }

    def __init__(self, ts=None, event_id=None, peer_id=None):
        r"""RTCCause

        The model defined in huaweicloud sdk

        :param ts: 异常事件的时间戳 
        :type ts: str
        :param event_id: 异常事件ID 
        :type event_id: str
        :param peer_id: 对端的用户ID 
        :type peer_id: str
        """
        
        

        self._ts = None
        self._event_id = None
        self._peer_id = None
        self.discriminator = None

        if ts is not None:
            self.ts = ts
        if event_id is not None:
            self.event_id = event_id
        if peer_id is not None:
            self.peer_id = peer_id

    @property
    def ts(self):
        r"""Gets the ts of this RTCCause.

        异常事件的时间戳 

        :return: The ts of this RTCCause.
        :rtype: str
        """
        return self._ts

    @ts.setter
    def ts(self, ts):
        r"""Sets the ts of this RTCCause.

        异常事件的时间戳 

        :param ts: The ts of this RTCCause.
        :type ts: str
        """
        self._ts = ts

    @property
    def event_id(self):
        r"""Gets the event_id of this RTCCause.

        异常事件ID 

        :return: The event_id of this RTCCause.
        :rtype: str
        """
        return self._event_id

    @event_id.setter
    def event_id(self, event_id):
        r"""Sets the event_id of this RTCCause.

        异常事件ID 

        :param event_id: The event_id of this RTCCause.
        :type event_id: str
        """
        self._event_id = event_id

    @property
    def peer_id(self):
        r"""Gets the peer_id of this RTCCause.

        对端的用户ID 

        :return: The peer_id of this RTCCause.
        :rtype: str
        """
        return self._peer_id

    @peer_id.setter
    def peer_id(self, peer_id):
        r"""Sets the peer_id of this RTCCause.

        对端的用户ID 

        :param peer_id: The peer_id of this RTCCause.
        :type peer_id: str
        """
        self._peer_id = peer_id

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
        if not isinstance(other, RTCCause):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
