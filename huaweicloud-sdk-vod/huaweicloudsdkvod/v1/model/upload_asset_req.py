# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UploadAssetReq:

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
        """UploadAssetReq

        The model defined in huaweicloud sdk

        :param asset_id: 媒资ID。
        :type asset_id: str
        :param video_md5: 视频文件MD5值。  建议参考[媒资上传和更新](https://support.huaweicloud.com/api-vod/vod_04_0212.html)生成对应的MD5值。
        :type video_md5: str
        :param video_name: 视频文件名。  文件名后缀为可选。
        :type video_name: str
        :param video_type: 视频文件类型。 取值为MP4、TS、MOV、MXF、MPG、FLV、WMV、AVI、M4V、F4V、MPEG、3GP、ASF、MKV
        :type video_type: str
        :param cover_id: 封面ID。  取值范围：[0,7]。  当前只支持一张封面，只能设置为0。
        :type cover_id: int
        :param cover_type: 封面图片格式类型。  取值如下： - JPG - PNG
        :type cover_type: str
        :param cover_md5: 封面文件的MD5值。
        :type cover_md5: str
        :param subtitles: 字幕文件信息
        :type subtitles: list[:class:`huaweicloudsdkvod.v1.Subtitle`]
        """
        
        

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
        """Gets the asset_id of this UploadAssetReq.

        媒资ID。

        :return: The asset_id of this UploadAssetReq.
        :rtype: str
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        """Sets the asset_id of this UploadAssetReq.

        媒资ID。

        :param asset_id: The asset_id of this UploadAssetReq.
        :type asset_id: str
        """
        self._asset_id = asset_id

    @property
    def video_md5(self):
        """Gets the video_md5 of this UploadAssetReq.

        视频文件MD5值。  建议参考[媒资上传和更新](https://support.huaweicloud.com/api-vod/vod_04_0212.html)生成对应的MD5值。

        :return: The video_md5 of this UploadAssetReq.
        :rtype: str
        """
        return self._video_md5

    @video_md5.setter
    def video_md5(self, video_md5):
        """Sets the video_md5 of this UploadAssetReq.

        视频文件MD5值。  建议参考[媒资上传和更新](https://support.huaweicloud.com/api-vod/vod_04_0212.html)生成对应的MD5值。

        :param video_md5: The video_md5 of this UploadAssetReq.
        :type video_md5: str
        """
        self._video_md5 = video_md5

    @property
    def video_name(self):
        """Gets the video_name of this UploadAssetReq.

        视频文件名。  文件名后缀为可选。

        :return: The video_name of this UploadAssetReq.
        :rtype: str
        """
        return self._video_name

    @video_name.setter
    def video_name(self, video_name):
        """Sets the video_name of this UploadAssetReq.

        视频文件名。  文件名后缀为可选。

        :param video_name: The video_name of this UploadAssetReq.
        :type video_name: str
        """
        self._video_name = video_name

    @property
    def video_type(self):
        """Gets the video_type of this UploadAssetReq.

        视频文件类型。 取值为MP4、TS、MOV、MXF、MPG、FLV、WMV、AVI、M4V、F4V、MPEG、3GP、ASF、MKV

        :return: The video_type of this UploadAssetReq.
        :rtype: str
        """
        return self._video_type

    @video_type.setter
    def video_type(self, video_type):
        """Sets the video_type of this UploadAssetReq.

        视频文件类型。 取值为MP4、TS、MOV、MXF、MPG、FLV、WMV、AVI、M4V、F4V、MPEG、3GP、ASF、MKV

        :param video_type: The video_type of this UploadAssetReq.
        :type video_type: str
        """
        self._video_type = video_type

    @property
    def cover_id(self):
        """Gets the cover_id of this UploadAssetReq.

        封面ID。  取值范围：[0,7]。  当前只支持一张封面，只能设置为0。

        :return: The cover_id of this UploadAssetReq.
        :rtype: int
        """
        return self._cover_id

    @cover_id.setter
    def cover_id(self, cover_id):
        """Sets the cover_id of this UploadAssetReq.

        封面ID。  取值范围：[0,7]。  当前只支持一张封面，只能设置为0。

        :param cover_id: The cover_id of this UploadAssetReq.
        :type cover_id: int
        """
        self._cover_id = cover_id

    @property
    def cover_type(self):
        """Gets the cover_type of this UploadAssetReq.

        封面图片格式类型。  取值如下： - JPG - PNG

        :return: The cover_type of this UploadAssetReq.
        :rtype: str
        """
        return self._cover_type

    @cover_type.setter
    def cover_type(self, cover_type):
        """Sets the cover_type of this UploadAssetReq.

        封面图片格式类型。  取值如下： - JPG - PNG

        :param cover_type: The cover_type of this UploadAssetReq.
        :type cover_type: str
        """
        self._cover_type = cover_type

    @property
    def cover_md5(self):
        """Gets the cover_md5 of this UploadAssetReq.

        封面文件的MD5值。

        :return: The cover_md5 of this UploadAssetReq.
        :rtype: str
        """
        return self._cover_md5

    @cover_md5.setter
    def cover_md5(self, cover_md5):
        """Sets the cover_md5 of this UploadAssetReq.

        封面文件的MD5值。

        :param cover_md5: The cover_md5 of this UploadAssetReq.
        :type cover_md5: str
        """
        self._cover_md5 = cover_md5

    @property
    def subtitles(self):
        """Gets the subtitles of this UploadAssetReq.

        字幕文件信息

        :return: The subtitles of this UploadAssetReq.
        :rtype: list[:class:`huaweicloudsdkvod.v1.Subtitle`]
        """
        return self._subtitles

    @subtitles.setter
    def subtitles(self, subtitles):
        """Sets the subtitles of this UploadAssetReq.

        字幕文件信息

        :param subtitles: The subtitles of this UploadAssetReq.
        :type subtitles: list[:class:`huaweicloudsdkvod.v1.Subtitle`]
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
        if not isinstance(other, UploadAssetReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
