# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RTCRoomInfoList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'app_id': 'str',
        'room_id': 'str',
        'users': 'list[RTCUserInfo]'
    }

    attribute_map = {
        'app_id': 'app_id',
        'room_id': 'room_id',
        'users': 'users'
    }

    def __init__(self, app_id=None, room_id=None, users=None):
        """RTCRoomInfoList

        The model defined in huaweicloud sdk

        :param app_id: RTC应用ID。
        :type app_id: str
        :param room_id: RTC房间ID。
        :type room_id: str
        :param users: 加入RTC房间用户信息。
        :type users: list[:class:`huaweicloudsdkmetastudio.v1.RTCUserInfo`]
        """
        
        

        self._app_id = None
        self._room_id = None
        self._users = None
        self.discriminator = None

        if app_id is not None:
            self.app_id = app_id
        if room_id is not None:
            self.room_id = room_id
        if users is not None:
            self.users = users

    @property
    def app_id(self):
        """Gets the app_id of this RTCRoomInfoList.

        RTC应用ID。

        :return: The app_id of this RTCRoomInfoList.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this RTCRoomInfoList.

        RTC应用ID。

        :param app_id: The app_id of this RTCRoomInfoList.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def room_id(self):
        """Gets the room_id of this RTCRoomInfoList.

        RTC房间ID。

        :return: The room_id of this RTCRoomInfoList.
        :rtype: str
        """
        return self._room_id

    @room_id.setter
    def room_id(self, room_id):
        """Sets the room_id of this RTCRoomInfoList.

        RTC房间ID。

        :param room_id: The room_id of this RTCRoomInfoList.
        :type room_id: str
        """
        self._room_id = room_id

    @property
    def users(self):
        """Gets the users of this RTCRoomInfoList.

        加入RTC房间用户信息。

        :return: The users of this RTCRoomInfoList.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.RTCUserInfo`]
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this RTCRoomInfoList.

        加入RTC房间用户信息。

        :param users: The users of this RTCRoomInfoList.
        :type users: list[:class:`huaweicloudsdkmetastudio.v1.RTCUserInfo`]
        """
        self._users = users

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
        if not isinstance(other, RTCRoomInfoList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
