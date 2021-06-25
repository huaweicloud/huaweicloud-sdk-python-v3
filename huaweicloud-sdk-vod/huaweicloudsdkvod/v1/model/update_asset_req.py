# coding: utf-8

import pprint
import re

import six





class UpdateAssetReq:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'asset_id': 'str',
        'video_md5': 'str',
        'video_name': 'str',
        'video_type': 'str',
        'cover_id': 'int',
        'cover_type': 'str',
        'cover_md5': 'str',
        'subtitles': 'list[Subtitle]'
    }

    attribute_map = {
        'asset_id': 'asset_id',
        'video_md5': 'video_md5',
        'video_name': 'video_name',
        'video_type': 'video_type',
        'cover_id': 'cover_id',
        'cover_type': 'cover_type',
        'cover_md5': 'cover_md5',
        'subtitles': 'subtitles'
    }

    def __init__(self, asset_id=None, video_md5=None, video_name=None, video_type=None, cover_id=None, cover_type=None, cover_md5=None, subtitles=None):
        """UpdateAssetReq - a model defined in huaweicloud sdk"""
        
        

        self._asset_id = None
        self._video_md5 = None
        self._video_name = None
        self._video_type = None
        self._cover_id = None
        self._cover_type = None
        self._cover_md5 = None
        self._subtitles = None
        self.discriminator = None

        self.asset_id = asset_id
        if video_md5 is not None:
            self.video_md5 = video_md5
        if video_name is not None:
            self.video_name = video_name
        if video_type is not None:
            self.video_type = video_type
        if cover_id is not None:
            self.cover_id = cover_id
        if cover_type is not None:
            self.cover_type = cover_type
        if cover_md5 is not None:
            self.cover_md5 = cover_md5
        if subtitles is not None:
            self.subtitles = subtitles

    @property
    def asset_id(self):
        """Gets the asset_id of this UpdateAssetReq.

        媒体ID<br/> 

        :return: The asset_id of this UpdateAssetReq.
        :rtype: str
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        """Sets the asset_id of this UpdateAssetReq.

        媒体ID<br/> 

        :param asset_id: The asset_id of this UpdateAssetReq.
        :type: str
        """
        self._asset_id = asset_id

    @property
    def video_md5(self):
        """Gets the video_md5 of this UpdateAssetReq.

        视频文件MD5值<br/> 

        :return: The video_md5 of this UpdateAssetReq.
        :rtype: str
        """
        return self._video_md5

    @video_md5.setter
    def video_md5(self, video_md5):
        """Sets the video_md5 of this UpdateAssetReq.

        视频文件MD5值<br/> 

        :param video_md5: The video_md5 of this UpdateAssetReq.
        :type: str
        """
        self._video_md5 = video_md5

    @property
    def video_name(self):
        """Gets the video_name of this UpdateAssetReq.

        视频文件名<br/> 

        :return: The video_name of this UpdateAssetReq.
        :rtype: str
        """
        return self._video_name

    @video_name.setter
    def video_name(self, video_name):
        """Sets the video_name of this UpdateAssetReq.

        视频文件名<br/> 

        :param video_name: The video_name of this UpdateAssetReq.
        :type: str
        """
        self._video_name = video_name

    @property
    def video_type(self):
        """Gets the video_type of this UpdateAssetReq.

        视频文件类型<br/> 

        :return: The video_type of this UpdateAssetReq.
        :rtype: str
        """
        return self._video_type

    @video_type.setter
    def video_type(self, video_type):
        """Sets the video_type of this UpdateAssetReq.

        视频文件类型<br/> 

        :param video_type: The video_type of this UpdateAssetReq.
        :type: str
        """
        self._video_type = video_type

    @property
    def cover_id(self):
        """Gets the cover_id of this UpdateAssetReq.

        封面ID，取值0-7。当前只支持一张封面，只能填0<br/> 

        :return: The cover_id of this UpdateAssetReq.
        :rtype: int
        """
        return self._cover_id

    @cover_id.setter
    def cover_id(self, cover_id):
        """Sets the cover_id of this UpdateAssetReq.

        封面ID，取值0-7。当前只支持一张封面，只能填0<br/> 

        :param cover_id: The cover_id of this UpdateAssetReq.
        :type: int
        """
        self._cover_id = cover_id

    @property
    def cover_type(self):
        """Gets the cover_type of this UpdateAssetReq.

        封面图片格式类型<br/> 

        :return: The cover_type of this UpdateAssetReq.
        :rtype: str
        """
        return self._cover_type

    @cover_type.setter
    def cover_type(self, cover_type):
        """Sets the cover_type of this UpdateAssetReq.

        封面图片格式类型<br/> 

        :param cover_type: The cover_type of this UpdateAssetReq.
        :type: str
        """
        self._cover_type = cover_type

    @property
    def cover_md5(self):
        """Gets the cover_md5 of this UpdateAssetReq.

        封面文件MD5值<br/> 

        :return: The cover_md5 of this UpdateAssetReq.
        :rtype: str
        """
        return self._cover_md5

    @cover_md5.setter
    def cover_md5(self, cover_md5):
        """Sets the cover_md5 of this UpdateAssetReq.

        封面文件MD5值<br/> 

        :param cover_md5: The cover_md5 of this UpdateAssetReq.
        :type: str
        """
        self._cover_md5 = cover_md5

    @property
    def subtitles(self):
        """Gets the subtitles of this UpdateAssetReq.

        字幕文件信息<br/> 

        :return: The subtitles of this UpdateAssetReq.
        :rtype: list[Subtitle]
        """
        return self._subtitles

    @subtitles.setter
    def subtitles(self, subtitles):
        """Sets the subtitles of this UpdateAssetReq.

        字幕文件信息<br/> 

        :param subtitles: The subtitles of this UpdateAssetReq.
        :type: list[Subtitle]
        """
        self._subtitles = subtitles

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
        if not isinstance(other, UpdateAssetReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other