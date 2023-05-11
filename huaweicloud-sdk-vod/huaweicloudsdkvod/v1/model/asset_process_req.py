# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AssetProcessReq:

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
        'template_group_name': 'str',
        'auto_encrypt': 'int',
        'thumbnail': 'Thumbnail',
        'subtitle_id': 'list[int]'
    }

    attribute_map = {
        'asset_id': 'asset_id',
        'template_group_name': 'template_group_name',
        'auto_encrypt': 'auto_encrypt',
        'thumbnail': 'thumbnail',
        'subtitle_id': 'subtitle_id'
    }

    def __init__(self, asset_id=None, template_group_name=None, auto_encrypt=None, thumbnail=None, subtitle_id=None):
        """AssetProcessReq

        The model defined in huaweicloud sdk

        :param asset_id: 媒资ID。
        :type asset_id: str
        :param template_group_name: 转码模板组名称。   若不为空，则使用指定的转码模板对上传的音视频进行转码，您可以在视频点播控制台配置转码模板，具体请参见[转码设置](https://support.huaweicloud.com/usermanual-vod/vod_01_0072.html)。
        :type template_group_name: str
        :param auto_encrypt: 是否自动加密。  取值如下： - 0：表示不加密。 - 1：表示需要加密。  默认值：0。  加密与转码必须要一起进行，当需要加密时，转码参数不能为空，且转码输出格式必须要为HLS。
        :type auto_encrypt: int
        :param thumbnail: 
        :type thumbnail: :class:`huaweicloudsdkvod.v1.Thumbnail`
        :param subtitle_id: 字幕文件ID。  &gt; 仅在[创建媒资](https://support.huaweicloud.com/api-vod/vod_04_0196.html)时，请求参数设置了“**subtitles**”时，该参数设置才生效。
        :type subtitle_id: list[int]
        """
        
        

        self._asset_id = None
        self._template_group_name = None
        self._auto_encrypt = None
        self._thumbnail = None
        self._subtitle_id = None
        self.discriminator = None

        self.asset_id = asset_id
        if template_group_name is not None:
            self.template_group_name = template_group_name
        if auto_encrypt is not None:
            self.auto_encrypt = auto_encrypt
        if thumbnail is not None:
            self.thumbnail = thumbnail
        if subtitle_id is not None:
            self.subtitle_id = subtitle_id

    @property
    def asset_id(self):
        """Gets the asset_id of this AssetProcessReq.

        媒资ID。

        :return: The asset_id of this AssetProcessReq.
        :rtype: str
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        """Sets the asset_id of this AssetProcessReq.

        媒资ID。

        :param asset_id: The asset_id of this AssetProcessReq.
        :type asset_id: str
        """
        self._asset_id = asset_id

    @property
    def template_group_name(self):
        """Gets the template_group_name of this AssetProcessReq.

        转码模板组名称。   若不为空，则使用指定的转码模板对上传的音视频进行转码，您可以在视频点播控制台配置转码模板，具体请参见[转码设置](https://support.huaweicloud.com/usermanual-vod/vod_01_0072.html)。

        :return: The template_group_name of this AssetProcessReq.
        :rtype: str
        """
        return self._template_group_name

    @template_group_name.setter
    def template_group_name(self, template_group_name):
        """Sets the template_group_name of this AssetProcessReq.

        转码模板组名称。   若不为空，则使用指定的转码模板对上传的音视频进行转码，您可以在视频点播控制台配置转码模板，具体请参见[转码设置](https://support.huaweicloud.com/usermanual-vod/vod_01_0072.html)。

        :param template_group_name: The template_group_name of this AssetProcessReq.
        :type template_group_name: str
        """
        self._template_group_name = template_group_name

    @property
    def auto_encrypt(self):
        """Gets the auto_encrypt of this AssetProcessReq.

        是否自动加密。  取值如下： - 0：表示不加密。 - 1：表示需要加密。  默认值：0。  加密与转码必须要一起进行，当需要加密时，转码参数不能为空，且转码输出格式必须要为HLS。

        :return: The auto_encrypt of this AssetProcessReq.
        :rtype: int
        """
        return self._auto_encrypt

    @auto_encrypt.setter
    def auto_encrypt(self, auto_encrypt):
        """Sets the auto_encrypt of this AssetProcessReq.

        是否自动加密。  取值如下： - 0：表示不加密。 - 1：表示需要加密。  默认值：0。  加密与转码必须要一起进行，当需要加密时，转码参数不能为空，且转码输出格式必须要为HLS。

        :param auto_encrypt: The auto_encrypt of this AssetProcessReq.
        :type auto_encrypt: int
        """
        self._auto_encrypt = auto_encrypt

    @property
    def thumbnail(self):
        """Gets the thumbnail of this AssetProcessReq.

        :return: The thumbnail of this AssetProcessReq.
        :rtype: :class:`huaweicloudsdkvod.v1.Thumbnail`
        """
        return self._thumbnail

    @thumbnail.setter
    def thumbnail(self, thumbnail):
        """Sets the thumbnail of this AssetProcessReq.

        :param thumbnail: The thumbnail of this AssetProcessReq.
        :type thumbnail: :class:`huaweicloudsdkvod.v1.Thumbnail`
        """
        self._thumbnail = thumbnail

    @property
    def subtitle_id(self):
        """Gets the subtitle_id of this AssetProcessReq.

        字幕文件ID。  > 仅在[创建媒资](https://support.huaweicloud.com/api-vod/vod_04_0196.html)时，请求参数设置了“**subtitles**”时，该参数设置才生效。

        :return: The subtitle_id of this AssetProcessReq.
        :rtype: list[int]
        """
        return self._subtitle_id

    @subtitle_id.setter
    def subtitle_id(self, subtitle_id):
        """Sets the subtitle_id of this AssetProcessReq.

        字幕文件ID。  > 仅在[创建媒资](https://support.huaweicloud.com/api-vod/vod_04_0196.html)时，请求参数设置了“**subtitles**”时，该参数设置才生效。

        :param subtitle_id: The subtitle_id of this AssetProcessReq.
        :type subtitle_id: list[int]
        """
        self._subtitle_id = subtitle_id

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
        if not isinstance(other, AssetProcessReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
