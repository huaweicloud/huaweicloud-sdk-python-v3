# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EventExInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'participants': 'list[EventParticipant]',
        'congestion_info': 'CongestionInfo'
    }

    attribute_map = {
        'participants': 'participants',
        'congestion_info': 'congestion_info'
    }

    def __init__(self, participants=None, congestion_info=None):
        """EventExInfo

        The model defined in huaweicloud sdk

        :param participants: **参数说明**：识别出交通事件时所对应的交通参与者。
        :type participants: list[:class:`huaweicloudsdkdris.v1.EventParticipant`]
        :param congestion_info: 
        :type congestion_info: :class:`huaweicloudsdkdris.v1.CongestionInfo`
        """
        
        

        self._participants = None
        self._congestion_info = None
        self.discriminator = None

        if participants is not None:
            self.participants = participants
        if congestion_info is not None:
            self.congestion_info = congestion_info

    @property
    def participants(self):
        """Gets the participants of this EventExInfo.

        **参数说明**：识别出交通事件时所对应的交通参与者。

        :return: The participants of this EventExInfo.
        :rtype: list[:class:`huaweicloudsdkdris.v1.EventParticipant`]
        """
        return self._participants

    @participants.setter
    def participants(self, participants):
        """Sets the participants of this EventExInfo.

        **参数说明**：识别出交通事件时所对应的交通参与者。

        :param participants: The participants of this EventExInfo.
        :type participants: list[:class:`huaweicloudsdkdris.v1.EventParticipant`]
        """
        self._participants = participants

    @property
    def congestion_info(self):
        """Gets the congestion_info of this EventExInfo.

        :return: The congestion_info of this EventExInfo.
        :rtype: :class:`huaweicloudsdkdris.v1.CongestionInfo`
        """
        return self._congestion_info

    @congestion_info.setter
    def congestion_info(self, congestion_info):
        """Sets the congestion_info of this EventExInfo.

        :param congestion_info: The congestion_info of this EventExInfo.
        :type congestion_info: :class:`huaweicloudsdkdris.v1.CongestionInfo`
        """
        self._congestion_info = congestion_info

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
        if not isinstance(other, EventExInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
