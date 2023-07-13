# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpenRoomSettingReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'room_introduce': 'str',
        'crop_logo_id': 'str',
        'cover_picture_id': 'str',
        'show_audience_mode': 'str',
        'is_redouble_open': 'str',
        'base_audience_count': 'int',
        'multiple': 'float'
    }

    attribute_map = {
        'room_introduce': 'roomIntroduce',
        'crop_logo_id': 'cropLogoId',
        'cover_picture_id': 'coverPictureId',
        'show_audience_mode': 'showAudienceMode',
        'is_redouble_open': 'isRedoubleOpen',
        'base_audience_count': 'baseAudienceCount',
        'multiple': 'multiple'
    }

    def __init__(self, room_introduce=None, crop_logo_id=None, cover_picture_id=None, show_audience_mode=None, is_redouble_open=None, base_audience_count=None, multiple=None):
        """OpenRoomSettingReq

        The model defined in huaweicloud sdk

        :param room_introduce: 网络研讨会介绍。
        :type room_introduce: str
        :param crop_logo_id: 企业Logo的文件id。
        :type crop_logo_id: str
        :param cover_picture_id: 欢迎界面的文件id。
        :type cover_picture_id: str
        :param show_audience_mode: 显示观众人数的模式。默认值为real_time。 - none: 不显示 - real_time: 实时显示 
        :type show_audience_mode: str
        :param is_redouble_open: 智能倍增开关。默认值为Y。 - Y 开启智能倍增 - N 关闭智能倍增 
        :type is_redouble_open: str
        :param base_audience_count: 基础设置人数(网络研讨会没人时显示的人数)。默认值为0。取值范围为[0, 10000]。
        :type base_audience_count: int
        :param multiple: 设置倍数(基础人数+真实人数*倍数)。默认值为1.0。 取值范围为[0, 10]，取1位小数。
        :type multiple: float
        """
        
        

        self._room_introduce = None
        self._crop_logo_id = None
        self._cover_picture_id = None
        self._show_audience_mode = None
        self._is_redouble_open = None
        self._base_audience_count = None
        self._multiple = None
        self.discriminator = None

        if room_introduce is not None:
            self.room_introduce = room_introduce
        if crop_logo_id is not None:
            self.crop_logo_id = crop_logo_id
        if cover_picture_id is not None:
            self.cover_picture_id = cover_picture_id
        if show_audience_mode is not None:
            self.show_audience_mode = show_audience_mode
        if is_redouble_open is not None:
            self.is_redouble_open = is_redouble_open
        if base_audience_count is not None:
            self.base_audience_count = base_audience_count
        if multiple is not None:
            self.multiple = multiple

    @property
    def room_introduce(self):
        """Gets the room_introduce of this OpenRoomSettingReq.

        网络研讨会介绍。

        :return: The room_introduce of this OpenRoomSettingReq.
        :rtype: str
        """
        return self._room_introduce

    @room_introduce.setter
    def room_introduce(self, room_introduce):
        """Sets the room_introduce of this OpenRoomSettingReq.

        网络研讨会介绍。

        :param room_introduce: The room_introduce of this OpenRoomSettingReq.
        :type room_introduce: str
        """
        self._room_introduce = room_introduce

    @property
    def crop_logo_id(self):
        """Gets the crop_logo_id of this OpenRoomSettingReq.

        企业Logo的文件id。

        :return: The crop_logo_id of this OpenRoomSettingReq.
        :rtype: str
        """
        return self._crop_logo_id

    @crop_logo_id.setter
    def crop_logo_id(self, crop_logo_id):
        """Sets the crop_logo_id of this OpenRoomSettingReq.

        企业Logo的文件id。

        :param crop_logo_id: The crop_logo_id of this OpenRoomSettingReq.
        :type crop_logo_id: str
        """
        self._crop_logo_id = crop_logo_id

    @property
    def cover_picture_id(self):
        """Gets the cover_picture_id of this OpenRoomSettingReq.

        欢迎界面的文件id。

        :return: The cover_picture_id of this OpenRoomSettingReq.
        :rtype: str
        """
        return self._cover_picture_id

    @cover_picture_id.setter
    def cover_picture_id(self, cover_picture_id):
        """Sets the cover_picture_id of this OpenRoomSettingReq.

        欢迎界面的文件id。

        :param cover_picture_id: The cover_picture_id of this OpenRoomSettingReq.
        :type cover_picture_id: str
        """
        self._cover_picture_id = cover_picture_id

    @property
    def show_audience_mode(self):
        """Gets the show_audience_mode of this OpenRoomSettingReq.

        显示观众人数的模式。默认值为real_time。 - none: 不显示 - real_time: 实时显示 

        :return: The show_audience_mode of this OpenRoomSettingReq.
        :rtype: str
        """
        return self._show_audience_mode

    @show_audience_mode.setter
    def show_audience_mode(self, show_audience_mode):
        """Sets the show_audience_mode of this OpenRoomSettingReq.

        显示观众人数的模式。默认值为real_time。 - none: 不显示 - real_time: 实时显示 

        :param show_audience_mode: The show_audience_mode of this OpenRoomSettingReq.
        :type show_audience_mode: str
        """
        self._show_audience_mode = show_audience_mode

    @property
    def is_redouble_open(self):
        """Gets the is_redouble_open of this OpenRoomSettingReq.

        智能倍增开关。默认值为Y。 - Y 开启智能倍增 - N 关闭智能倍增 

        :return: The is_redouble_open of this OpenRoomSettingReq.
        :rtype: str
        """
        return self._is_redouble_open

    @is_redouble_open.setter
    def is_redouble_open(self, is_redouble_open):
        """Sets the is_redouble_open of this OpenRoomSettingReq.

        智能倍增开关。默认值为Y。 - Y 开启智能倍增 - N 关闭智能倍增 

        :param is_redouble_open: The is_redouble_open of this OpenRoomSettingReq.
        :type is_redouble_open: str
        """
        self._is_redouble_open = is_redouble_open

    @property
    def base_audience_count(self):
        """Gets the base_audience_count of this OpenRoomSettingReq.

        基础设置人数(网络研讨会没人时显示的人数)。默认值为0。取值范围为[0, 10000]。

        :return: The base_audience_count of this OpenRoomSettingReq.
        :rtype: int
        """
        return self._base_audience_count

    @base_audience_count.setter
    def base_audience_count(self, base_audience_count):
        """Sets the base_audience_count of this OpenRoomSettingReq.

        基础设置人数(网络研讨会没人时显示的人数)。默认值为0。取值范围为[0, 10000]。

        :param base_audience_count: The base_audience_count of this OpenRoomSettingReq.
        :type base_audience_count: int
        """
        self._base_audience_count = base_audience_count

    @property
    def multiple(self):
        """Gets the multiple of this OpenRoomSettingReq.

        设置倍数(基础人数+真实人数*倍数)。默认值为1.0。 取值范围为[0, 10]，取1位小数。

        :return: The multiple of this OpenRoomSettingReq.
        :rtype: float
        """
        return self._multiple

    @multiple.setter
    def multiple(self, multiple):
        """Sets the multiple of this OpenRoomSettingReq.

        设置倍数(基础人数+真实人数*倍数)。默认值为1.0。 取值范围为[0, 10]，取1位小数。

        :param multiple: The multiple of this OpenRoomSettingReq.
        :type multiple: float
        """
        self._multiple = multiple

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
        if not isinstance(other, OpenRoomSettingReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
