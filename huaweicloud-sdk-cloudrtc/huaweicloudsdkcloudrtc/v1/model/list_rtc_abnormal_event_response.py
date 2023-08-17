# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRtcAbnormalEventResponse(SdkResponse):

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
        'uid': 'str',
        'exp_id': 'str',
        'abnormal_list': 'list[RTCCause]',
        'x_request_id': 'str'
    }

    attribute_map = {
        'room_id': 'room_id',
        'uid': 'uid',
        'exp_id': 'exp_id',
        'abnormal_list': 'abnormal_list',
        'x_request_id': 'X-request-id'
    }

    def __init__(self, room_id=None, uid=None, exp_id=None, abnormal_list=None, x_request_id=None):
        """ListRtcAbnormalEventResponse

        The model defined in huaweicloud sdk

        :param room_id: 房间ID 
        :type room_id: str
        :param uid: 用户ID 
        :type uid: str
        :param exp_id: 体验ID 
        :type exp_id: str
        :param abnormal_list: 异常信息列表。注意：此字段可能返回null，表示取不到有效值。 
        :type abnormal_list: list[:class:`huaweicloudsdkcloudrtc.v1.RTCCause`]
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ListRtcAbnormalEventResponse, self).__init__()

        self._room_id = None
        self._uid = None
        self._exp_id = None
        self._abnormal_list = None
        self._x_request_id = None
        self.discriminator = None

        if room_id is not None:
            self.room_id = room_id
        if uid is not None:
            self.uid = uid
        if exp_id is not None:
            self.exp_id = exp_id
        if abnormal_list is not None:
            self.abnormal_list = abnormal_list
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def room_id(self):
        """Gets the room_id of this ListRtcAbnormalEventResponse.

        房间ID 

        :return: The room_id of this ListRtcAbnormalEventResponse.
        :rtype: str
        """
        return self._room_id

    @room_id.setter
    def room_id(self, room_id):
        """Sets the room_id of this ListRtcAbnormalEventResponse.

        房间ID 

        :param room_id: The room_id of this ListRtcAbnormalEventResponse.
        :type room_id: str
        """
        self._room_id = room_id

    @property
    def uid(self):
        """Gets the uid of this ListRtcAbnormalEventResponse.

        用户ID 

        :return: The uid of this ListRtcAbnormalEventResponse.
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this ListRtcAbnormalEventResponse.

        用户ID 

        :param uid: The uid of this ListRtcAbnormalEventResponse.
        :type uid: str
        """
        self._uid = uid

    @property
    def exp_id(self):
        """Gets the exp_id of this ListRtcAbnormalEventResponse.

        体验ID 

        :return: The exp_id of this ListRtcAbnormalEventResponse.
        :rtype: str
        """
        return self._exp_id

    @exp_id.setter
    def exp_id(self, exp_id):
        """Sets the exp_id of this ListRtcAbnormalEventResponse.

        体验ID 

        :param exp_id: The exp_id of this ListRtcAbnormalEventResponse.
        :type exp_id: str
        """
        self._exp_id = exp_id

    @property
    def abnormal_list(self):
        """Gets the abnormal_list of this ListRtcAbnormalEventResponse.

        异常信息列表。注意：此字段可能返回null，表示取不到有效值。 

        :return: The abnormal_list of this ListRtcAbnormalEventResponse.
        :rtype: list[:class:`huaweicloudsdkcloudrtc.v1.RTCCause`]
        """
        return self._abnormal_list

    @abnormal_list.setter
    def abnormal_list(self, abnormal_list):
        """Sets the abnormal_list of this ListRtcAbnormalEventResponse.

        异常信息列表。注意：此字段可能返回null，表示取不到有效值。 

        :param abnormal_list: The abnormal_list of this ListRtcAbnormalEventResponse.
        :type abnormal_list: list[:class:`huaweicloudsdkcloudrtc.v1.RTCCause`]
        """
        self._abnormal_list = abnormal_list

    @property
    def x_request_id(self):
        """Gets the x_request_id of this ListRtcAbnormalEventResponse.

        :return: The x_request_id of this ListRtcAbnormalEventResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        """Sets the x_request_id of this ListRtcAbnormalEventResponse.

        :param x_request_id: The x_request_id of this ListRtcAbnormalEventResponse.
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
        if not isinstance(other, ListRtcAbnormalEventResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
