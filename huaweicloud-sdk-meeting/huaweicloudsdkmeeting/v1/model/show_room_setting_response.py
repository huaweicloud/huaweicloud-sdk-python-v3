# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ShowRoomSettingResponse(SdkResponse):


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
        """ShowRoomSettingResponse - a model defined in huaweicloud sdk"""
        
        super(ShowRoomSettingResponse, self).__init__()

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
        """Gets the room_introduce of this ShowRoomSettingResponse.

        直播介绍, 最大不超过500个字符

        :return: The room_introduce of this ShowRoomSettingResponse.
        :rtype: str
        """
        return self._room_introduce

    @room_introduce.setter
    def room_introduce(self, room_introduce):
        """Sets the room_introduce of this ShowRoomSettingResponse.

        直播介绍, 最大不超过500个字符

        :param room_introduce: The room_introduce of this ShowRoomSettingResponse.
        :type: str
        """
        self._room_introduce = room_introduce

    @property
    def crop_logo_id(self):
        """Gets the crop_logo_id of this ShowRoomSettingResponse.

        企业Logo（文件id）,不超过32字符

        :return: The crop_logo_id of this ShowRoomSettingResponse.
        :rtype: str
        """
        return self._crop_logo_id

    @crop_logo_id.setter
    def crop_logo_id(self, crop_logo_id):
        """Sets the crop_logo_id of this ShowRoomSettingResponse.

        企业Logo（文件id）,不超过32字符

        :param crop_logo_id: The crop_logo_id of this ShowRoomSettingResponse.
        :type: str
        """
        self._crop_logo_id = crop_logo_id

    @property
    def cover_picture_id(self):
        """Gets the cover_picture_id of this ShowRoomSettingResponse.

        封面内容(文件id)，不超过32字符

        :return: The cover_picture_id of this ShowRoomSettingResponse.
        :rtype: str
        """
        return self._cover_picture_id

    @cover_picture_id.setter
    def cover_picture_id(self, cover_picture_id):
        """Sets the cover_picture_id of this ShowRoomSettingResponse.

        封面内容(文件id)，不超过32字符

        :param cover_picture_id: The cover_picture_id of this ShowRoomSettingResponse.
        :type: str
        """
        self._cover_picture_id = cover_picture_id

    @property
    def show_audience_mode(self):
        """Gets the show_audience_mode of this ShowRoomSettingResponse.

        显示观众人数的模式。默认值为real_time - none:不显示 - real_time:实时显示 

        :return: The show_audience_mode of this ShowRoomSettingResponse.
        :rtype: str
        """
        return self._show_audience_mode

    @show_audience_mode.setter
    def show_audience_mode(self, show_audience_mode):
        """Sets the show_audience_mode of this ShowRoomSettingResponse.

        显示观众人数的模式。默认值为real_time - none:不显示 - real_time:实时显示 

        :param show_audience_mode: The show_audience_mode of this ShowRoomSettingResponse.
        :type: str
        """
        self._show_audience_mode = show_audience_mode

    @property
    def is_redouble_open(self):
        """Gets the is_redouble_open of this ShowRoomSettingResponse.

        智能倍增开关。默认值为Y - Y 开启智能倍增 - N 关闭智能倍增 

        :return: The is_redouble_open of this ShowRoomSettingResponse.
        :rtype: str
        """
        return self._is_redouble_open

    @is_redouble_open.setter
    def is_redouble_open(self, is_redouble_open):
        """Sets the is_redouble_open of this ShowRoomSettingResponse.

        智能倍增开关。默认值为Y - Y 开启智能倍增 - N 关闭智能倍增 

        :param is_redouble_open: The is_redouble_open of this ShowRoomSettingResponse.
        :type: str
        """
        self._is_redouble_open = is_redouble_open

    @property
    def base_audience_count(self):
        """Gets the base_audience_count of this ShowRoomSettingResponse.

        基础设置人数(直播间没人时显示的人数). 取值范围为[0, 10000]。默认值为0

        :return: The base_audience_count of this ShowRoomSettingResponse.
        :rtype: int
        """
        return self._base_audience_count

    @base_audience_count.setter
    def base_audience_count(self, base_audience_count):
        """Sets the base_audience_count of this ShowRoomSettingResponse.

        基础设置人数(直播间没人时显示的人数). 取值范围为[0, 10000]。默认值为0

        :param base_audience_count: The base_audience_count of this ShowRoomSettingResponse.
        :type: int
        """
        self._base_audience_count = base_audience_count

    @property
    def multiple(self):
        """Gets the multiple of this ShowRoomSettingResponse.

        设置倍数(基础人数+真实人数*倍数). 取值范围为[0, 10]，取1位小数。默认值为1.0

        :return: The multiple of this ShowRoomSettingResponse.
        :rtype: float
        """
        return self._multiple

    @multiple.setter
    def multiple(self, multiple):
        """Sets the multiple of this ShowRoomSettingResponse.

        设置倍数(基础人数+真实人数*倍数). 取值范围为[0, 10]，取1位小数。默认值为1.0

        :param multiple: The multiple of this ShowRoomSettingResponse.
        :type: float
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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ShowRoomSettingResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other