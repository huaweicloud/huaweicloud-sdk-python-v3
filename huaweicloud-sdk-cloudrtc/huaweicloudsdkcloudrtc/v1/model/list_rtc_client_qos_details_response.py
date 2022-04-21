# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRtcClientQosDetailsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'room_id': 'str',
        'data': 'list[QosQualityData]',
        'x_request_id': 'str'
    }

    attribute_map = {
        'room_id': 'room_id',
        'data': 'data',
        'x_request_id': 'X-request-id'
    }

    def __init__(self, room_id=None, data=None, x_request_id=None):
        """ListRtcClientQosDetailsResponse

        The model defined in huaweicloud sdk

        :param room_id: 房间ID
        :type room_id: str
        :param data: QoS质量数据
        :type data: list[:class:`huaweicloudsdkcloudrtc.v1.QosQualityData`]
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ListRtcClientQosDetailsResponse, self).__init__()

        self._room_id = None
        self._data = None
        self._x_request_id = None
        self.discriminator = None

        if room_id is not None:
            self.room_id = room_id
        if data is not None:
            self.data = data
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def room_id(self):
        """Gets the room_id of this ListRtcClientQosDetailsResponse.

        房间ID

        :return: The room_id of this ListRtcClientQosDetailsResponse.
        :rtype: str
        """
        return self._room_id

    @room_id.setter
    def room_id(self, room_id):
        """Sets the room_id of this ListRtcClientQosDetailsResponse.

        房间ID

        :param room_id: The room_id of this ListRtcClientQosDetailsResponse.
        :type room_id: str
        """
        self._room_id = room_id

    @property
    def data(self):
        """Gets the data of this ListRtcClientQosDetailsResponse.

        QoS质量数据

        :return: The data of this ListRtcClientQosDetailsResponse.
        :rtype: list[:class:`huaweicloudsdkcloudrtc.v1.QosQualityData`]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this ListRtcClientQosDetailsResponse.

        QoS质量数据

        :param data: The data of this ListRtcClientQosDetailsResponse.
        :type data: list[:class:`huaweicloudsdkcloudrtc.v1.QosQualityData`]
        """
        self._data = data

    @property
    def x_request_id(self):
        """Gets the x_request_id of this ListRtcClientQosDetailsResponse.


        :return: The x_request_id of this ListRtcClientQosDetailsResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        """Sets the x_request_id of this ListRtcClientQosDetailsResponse.


        :param x_request_id: The x_request_id of this ListRtcClientQosDetailsResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, ListRtcClientQosDetailsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
