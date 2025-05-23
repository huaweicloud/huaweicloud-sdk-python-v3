# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InputInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'rtc_room_info': 'RTCRoomInfoList'
    }

    attribute_map = {
        'rtc_room_info': 'rtc_room_info'
    }

    def __init__(self, rtc_room_info=None):
        r"""InputInfo

        The model defined in huaweicloud sdk

        :param rtc_room_info: 
        :type rtc_room_info: :class:`huaweicloudsdkmetastudio.v1.RTCRoomInfoList`
        """
        
        

        self._rtc_room_info = None
        self.discriminator = None

        if rtc_room_info is not None:
            self.rtc_room_info = rtc_room_info

    @property
    def rtc_room_info(self):
        r"""Gets the rtc_room_info of this InputInfo.

        :return: The rtc_room_info of this InputInfo.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.RTCRoomInfoList`
        """
        return self._rtc_room_info

    @rtc_room_info.setter
    def rtc_room_info(self, rtc_room_info):
        r"""Sets the rtc_room_info of this InputInfo.

        :param rtc_room_info: The rtc_room_info of this InputInfo.
        :type rtc_room_info: :class:`huaweicloudsdkmetastudio.v1.RTCRoomInfoList`
        """
        self._rtc_room_info = rtc_room_info

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
        if not isinstance(other, InputInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
