# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAssetByFileUploadReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'title': 'str',
        'description': 'str',
        'video_name': 'str',
        'video_type': 'str',
        'category_id': 'str',
        'video_md5': 'str',
        'cover_type': 'str',
        'cover_md5': 'str',
        'subtitles': 'list[Subtitle]',
        'tags': 'str',
        'auto_publish': 'int',
        'template_group_name': 'str',
        'auto_encrypt': 'int',
        'auto_preheat': 'str',
        'thumbnail': 'Thumbnail',
        'review': 'Review',
        'workflow_name': 'str'
    }

    attribute_map = {
        'title': 'title',
        'description': 'description',
        'video_name': 'video_name',
        'video_type': 'video_type',
        'category_id': 'category_id',
        'video_md5': 'video_md5',
        'cover_type': 'cover_type',
        'cover_md5': 'cover_md5',
        'subtitles': 'subtitles',
        'tags': 'tags',
        'auto_publish': 'auto_publish',
        'template_group_name': 'template_group_name',
        'auto_encrypt': 'auto_encrypt',
        'auto_preheat': 'auto_preheat',
        'thumbnail': 'thumbnail',
        'review': 'review',
        'workflow_name': 'workflow_name'
    }

    def __init__(self, title=None, description=None, video_name=None, video_type=None, category_id=None, video_md5=None, cover_type=None, cover_md5=None, subtitles=None, tags=None, auto_publish=None, template_group_name=None, auto_encrypt=None, auto_preheat=None, thumbnail=None, review=None, workflow_name=None):
        """CreateAssetByFileUploadReq

        The model defined in huaweicloud sdk

        :param title: 媒资标题，长度不超过128个字节，UTF-8编码。
        :type title: str
        :param description: 视频描述，长度不超过1024个字节。
        :type description: str
        :param video_name: 音视频文件名，长度不超过128个字节。  文件名后缀可选。
        :type video_name: str
        :param video_type: 上传音视频文件的格式。  取值如下： - 视频文件：MP4、TS、MOV、MXF、MPG、FLV、WMV、AVI、M4V、F4V、MPEG、3GP、ASF、MKV、HLS - 音频文件：MP3、OGG、WAV、WMA、APE、FLAC、AAC、AC3、MMF、AMR、M4A、M4R、WV、MP2  若上传格式为音频文件，则不支持转码、添加水印和字幕。
        :type video_type: str
        :param category_id: 媒资分类ID。  您可以调用[创建媒资分类](https://support.huaweicloud.com/api-vod/vod_04_0028.html)接口或在点播控制台的[分类设置](https://support.huaweicloud.com/usermanual-vod/vod010006.html)中创建对应的媒资分类，并获取分类ID。  &gt; 若不设置或者设置为-1，则上传的音视频归类到系统预置的“其它”分类中。
        :type category_id: str
        :param video_md5: 视频文件MD5值。  建议参考[媒资上传和更新](https://support.huaweicloud.com/api-vod/vod_04_0212.html)生成对应的MD5值。
        :type video_md5: str
        :param cover_type: 封面图片文件类型。  取值如下： - JPG - PNG  上传后的封面名称是固定的，后缀名为封面类型缩写。例如cover0.jpg，cover1.png 若不指定类型，则封面文件无后缀名。  &gt; 如果设置了图片格式，则不会执行首帧截图作为封面动作，需自行上传封面。
        :type cover_type: str
        :param cover_md5: 封面文件MD5值
        :type cover_md5: str
        :param subtitles: 字幕文件信息
        :type subtitles: list[:class:`huaweicloudsdkvod.v1.Subtitle`]
        :param tags: 视频标签。  单个标签不超过16个字节，最多不超过16个标签。  多个用逗号分隔，UTF8编码。
        :type tags: str
        :param auto_publish: 是否自动发布。  取值如下： - 0：表示不自动发布。 - 1：表示自动发布。  默认值：0。
        :type auto_publish: int
        :param template_group_name: 转码模板组名称。  若不为空，则使用指定的转码模板对上传的音视频进行转码，您可以在视频点播控制台配置转码模板，具体请参见[转码设置](https://support.huaweicloud.com/usermanual-vod/vod_01_0072.html)。  &gt; 若同时设置了“**template_group_name**”和“**workflow_name**”字段，则“**template_group_name**”字段生效。
        :type template_group_name: str
        :param auto_encrypt: 是否自动加密。  取值如下： - 0：表示不加密。 - 1：表示需要加密。  默认值：0。  加密与转码必须要一起进行，当需要加密时，转码参数不能为空，且转码输出格式必须要为HLS。
        :type auto_encrypt: int
        :param auto_preheat: 是否自动预热到CDN。  取值如下： - 0：表示不自动预热。 - 1：表示自动预热。  默认值：0。
        :type auto_preheat: str
        :param thumbnail: 
        :type thumbnail: :class:`huaweicloudsdkvod.v1.Thumbnail`
        :param review: 
        :type review: :class:`huaweicloudsdkvod.v1.Review`
        :param workflow_name: 工作流名称。  若不为空，则使用指定的工作流对上传的音视频进行处理，您可以在视频点播控制台配置工作流，具体请参见[工作流设置](https://support.huaweicloud.com/usermanual-vod/vod010041.html)。
        :type workflow_name: str
        """
        
        

        self._title = None
        self._description = None
        self._video_name = None
        self._video_type = None
        self._category_id = None
        self._video_md5 = None
        self._cover_type = None
        self._cover_md5 = None
        self._subtitles = None
        self._tags = None
        self._auto_publish = None
        self._template_group_name = None
        self._auto_encrypt = None
        self._auto_preheat = None
        self._thumbnail = None
        self._review = None
        self._workflow_name = None
        self.discriminator = None

        self.title = title
        if description is not None:
            self.description = description
        self.video_name = video_name
        self.video_type = video_type
        if category_id is not None:
            self.category_id = category_id
        if video_md5 is not None:
            self.video_md5 = video_md5
        if cover_type is not None:
            self.cover_type = cover_type
        if cover_md5 is not None:
            self.cover_md5 = cover_md5
        if subtitles is not None:
            self.subtitles = subtitles
        if tags is not None:
            self.tags = tags
        if auto_publish is not None:
            self.auto_publish = auto_publish
        if template_group_name is not None:
            self.template_group_name = template_group_name
        if auto_encrypt is not None:
            self.auto_encrypt = auto_encrypt
        if auto_preheat is not None:
            self.auto_preheat = auto_preheat
        if thumbnail is not None:
            self.thumbnail = thumbnail
        if review is not None:
            self.review = review
        if workflow_name is not None:
            self.workflow_name = workflow_name

    @property
    def title(self):
        """Gets the title of this CreateAssetByFileUploadReq.

        媒资标题，长度不超过128个字节，UTF-8编码。

        :return: The title of this CreateAssetByFileUploadReq.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this CreateAssetByFileUploadReq.

        媒资标题，长度不超过128个字节，UTF-8编码。

        :param title: The title of this CreateAssetByFileUploadReq.
        :type title: str
        """
        self._title = title

    @property
    def description(self):
        """Gets the description of this CreateAssetByFileUploadReq.

        视频描述，长度不超过1024个字节。

        :return: The description of this CreateAssetByFileUploadReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateAssetByFileUploadReq.

        视频描述，长度不超过1024个字节。

        :param description: The description of this CreateAssetByFileUploadReq.
        :type description: str
        """
        self._description = description

    @property
    def video_name(self):
        """Gets the video_name of this CreateAssetByFileUploadReq.

        音视频文件名，长度不超过128个字节。  文件名后缀可选。

        :return: The video_name of this CreateAssetByFileUploadReq.
        :rtype: str
        """
        return self._video_name

    @video_name.setter
    def video_name(self, video_name):
        """Sets the video_name of this CreateAssetByFileUploadReq.

        音视频文件名，长度不超过128个字节。  文件名后缀可选。

        :param video_name: The video_name of this CreateAssetByFileUploadReq.
        :type video_name: str
        """
        self._video_name = video_name

    @property
    def video_type(self):
        """Gets the video_type of this CreateAssetByFileUploadReq.

        上传音视频文件的格式。  取值如下： - 视频文件：MP4、TS、MOV、MXF、MPG、FLV、WMV、AVI、M4V、F4V、MPEG、3GP、ASF、MKV、HLS - 音频文件：MP3、OGG、WAV、WMA、APE、FLAC、AAC、AC3、MMF、AMR、M4A、M4R、WV、MP2  若上传格式为音频文件，则不支持转码、添加水印和字幕。

        :return: The video_type of this CreateAssetByFileUploadReq.
        :rtype: str
        """
        return self._video_type

    @video_type.setter
    def video_type(self, video_type):
        """Sets the video_type of this CreateAssetByFileUploadReq.

        上传音视频文件的格式。  取值如下： - 视频文件：MP4、TS、MOV、MXF、MPG、FLV、WMV、AVI、M4V、F4V、MPEG、3GP、ASF、MKV、HLS - 音频文件：MP3、OGG、WAV、WMA、APE、FLAC、AAC、AC3、MMF、AMR、M4A、M4R、WV、MP2  若上传格式为音频文件，则不支持转码、添加水印和字幕。

        :param video_type: The video_type of this CreateAssetByFileUploadReq.
        :type video_type: str
        """
        self._video_type = video_type

    @property
    def category_id(self):
        """Gets the category_id of this CreateAssetByFileUploadReq.

        媒资分类ID。  您可以调用[创建媒资分类](https://support.huaweicloud.com/api-vod/vod_04_0028.html)接口或在点播控制台的[分类设置](https://support.huaweicloud.com/usermanual-vod/vod010006.html)中创建对应的媒资分类，并获取分类ID。  > 若不设置或者设置为-1，则上传的音视频归类到系统预置的“其它”分类中。

        :return: The category_id of this CreateAssetByFileUploadReq.
        :rtype: str
        """
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        """Sets the category_id of this CreateAssetByFileUploadReq.

        媒资分类ID。  您可以调用[创建媒资分类](https://support.huaweicloud.com/api-vod/vod_04_0028.html)接口或在点播控制台的[分类设置](https://support.huaweicloud.com/usermanual-vod/vod010006.html)中创建对应的媒资分类，并获取分类ID。  > 若不设置或者设置为-1，则上传的音视频归类到系统预置的“其它”分类中。

        :param category_id: The category_id of this CreateAssetByFileUploadReq.
        :type category_id: str
        """
        self._category_id = category_id

    @property
    def video_md5(self):
        """Gets the video_md5 of this CreateAssetByFileUploadReq.

        视频文件MD5值。  建议参考[媒资上传和更新](https://support.huaweicloud.com/api-vod/vod_04_0212.html)生成对应的MD5值。

        :return: The video_md5 of this CreateAssetByFileUploadReq.
        :rtype: str
        """
        return self._video_md5

    @video_md5.setter
    def video_md5(self, video_md5):
        """Sets the video_md5 of this CreateAssetByFileUploadReq.

        视频文件MD5值。  建议参考[媒资上传和更新](https://support.huaweicloud.com/api-vod/vod_04_0212.html)生成对应的MD5值。

        :param video_md5: The video_md5 of this CreateAssetByFileUploadReq.
        :type video_md5: str
        """
        self._video_md5 = video_md5

    @property
    def cover_type(self):
        """Gets the cover_type of this CreateAssetByFileUploadReq.

        封面图片文件类型。  取值如下： - JPG - PNG  上传后的封面名称是固定的，后缀名为封面类型缩写。例如cover0.jpg，cover1.png 若不指定类型，则封面文件无后缀名。  > 如果设置了图片格式，则不会执行首帧截图作为封面动作，需自行上传封面。

        :return: The cover_type of this CreateAssetByFileUploadReq.
        :rtype: str
        """
        return self._cover_type

    @cover_type.setter
    def cover_type(self, cover_type):
        """Sets the cover_type of this CreateAssetByFileUploadReq.

        封面图片文件类型。  取值如下： - JPG - PNG  上传后的封面名称是固定的，后缀名为封面类型缩写。例如cover0.jpg，cover1.png 若不指定类型，则封面文件无后缀名。  > 如果设置了图片格式，则不会执行首帧截图作为封面动作，需自行上传封面。

        :param cover_type: The cover_type of this CreateAssetByFileUploadReq.
        :type cover_type: str
        """
        self._cover_type = cover_type

    @property
    def cover_md5(self):
        """Gets the cover_md5 of this CreateAssetByFileUploadReq.

        封面文件MD5值

        :return: The cover_md5 of this CreateAssetByFileUploadReq.
        :rtype: str
        """
        return self._cover_md5

    @cover_md5.setter
    def cover_md5(self, cover_md5):
        """Sets the cover_md5 of this CreateAssetByFileUploadReq.

        封面文件MD5值

        :param cover_md5: The cover_md5 of this CreateAssetByFileUploadReq.
        :type cover_md5: str
        """
        self._cover_md5 = cover_md5

    @property
    def subtitles(self):
        """Gets the subtitles of this CreateAssetByFileUploadReq.

        字幕文件信息

        :return: The subtitles of this CreateAssetByFileUploadReq.
        :rtype: list[:class:`huaweicloudsdkvod.v1.Subtitle`]
        """
        return self._subtitles

    @subtitles.setter
    def subtitles(self, subtitles):
        """Sets the subtitles of this CreateAssetByFileUploadReq.

        字幕文件信息

        :param subtitles: The subtitles of this CreateAssetByFileUploadReq.
        :type subtitles: list[:class:`huaweicloudsdkvod.v1.Subtitle`]
        """
        self._subtitles = subtitles

    @property
    def tags(self):
        """Gets the tags of this CreateAssetByFileUploadReq.

        视频标签。  单个标签不超过16个字节，最多不超过16个标签。  多个用逗号分隔，UTF8编码。

        :return: The tags of this CreateAssetByFileUploadReq.
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CreateAssetByFileUploadReq.

        视频标签。  单个标签不超过16个字节，最多不超过16个标签。  多个用逗号分隔，UTF8编码。

        :param tags: The tags of this CreateAssetByFileUploadReq.
        :type tags: str
        """
        self._tags = tags

    @property
    def auto_publish(self):
        """Gets the auto_publish of this CreateAssetByFileUploadReq.

        是否自动发布。  取值如下： - 0：表示不自动发布。 - 1：表示自动发布。  默认值：0。

        :return: The auto_publish of this CreateAssetByFileUploadReq.
        :rtype: int
        """
        return self._auto_publish

    @auto_publish.setter
    def auto_publish(self, auto_publish):
        """Sets the auto_publish of this CreateAssetByFileUploadReq.

        是否自动发布。  取值如下： - 0：表示不自动发布。 - 1：表示自动发布。  默认值：0。

        :param auto_publish: The auto_publish of this CreateAssetByFileUploadReq.
        :type auto_publish: int
        """
        self._auto_publish = auto_publish

    @property
    def template_group_name(self):
        """Gets the template_group_name of this CreateAssetByFileUploadReq.

        转码模板组名称。  若不为空，则使用指定的转码模板对上传的音视频进行转码，您可以在视频点播控制台配置转码模板，具体请参见[转码设置](https://support.huaweicloud.com/usermanual-vod/vod_01_0072.html)。  > 若同时设置了“**template_group_name**”和“**workflow_name**”字段，则“**template_group_name**”字段生效。

        :return: The template_group_name of this CreateAssetByFileUploadReq.
        :rtype: str
        """
        return self._template_group_name

    @template_group_name.setter
    def template_group_name(self, template_group_name):
        """Sets the template_group_name of this CreateAssetByFileUploadReq.

        转码模板组名称。  若不为空，则使用指定的转码模板对上传的音视频进行转码，您可以在视频点播控制台配置转码模板，具体请参见[转码设置](https://support.huaweicloud.com/usermanual-vod/vod_01_0072.html)。  > 若同时设置了“**template_group_name**”和“**workflow_name**”字段，则“**template_group_name**”字段生效。

        :param template_group_name: The template_group_name of this CreateAssetByFileUploadReq.
        :type template_group_name: str
        """
        self._template_group_name = template_group_name

    @property
    def auto_encrypt(self):
        """Gets the auto_encrypt of this CreateAssetByFileUploadReq.

        是否自动加密。  取值如下： - 0：表示不加密。 - 1：表示需要加密。  默认值：0。  加密与转码必须要一起进行，当需要加密时，转码参数不能为空，且转码输出格式必须要为HLS。

        :return: The auto_encrypt of this CreateAssetByFileUploadReq.
        :rtype: int
        """
        return self._auto_encrypt

    @auto_encrypt.setter
    def auto_encrypt(self, auto_encrypt):
        """Sets the auto_encrypt of this CreateAssetByFileUploadReq.

        是否自动加密。  取值如下： - 0：表示不加密。 - 1：表示需要加密。  默认值：0。  加密与转码必须要一起进行，当需要加密时，转码参数不能为空，且转码输出格式必须要为HLS。

        :param auto_encrypt: The auto_encrypt of this CreateAssetByFileUploadReq.
        :type auto_encrypt: int
        """
        self._auto_encrypt = auto_encrypt

    @property
    def auto_preheat(self):
        """Gets the auto_preheat of this CreateAssetByFileUploadReq.

        是否自动预热到CDN。  取值如下： - 0：表示不自动预热。 - 1：表示自动预热。  默认值：0。

        :return: The auto_preheat of this CreateAssetByFileUploadReq.
        :rtype: str
        """
        return self._auto_preheat

    @auto_preheat.setter
    def auto_preheat(self, auto_preheat):
        """Sets the auto_preheat of this CreateAssetByFileUploadReq.

        是否自动预热到CDN。  取值如下： - 0：表示不自动预热。 - 1：表示自动预热。  默认值：0。

        :param auto_preheat: The auto_preheat of this CreateAssetByFileUploadReq.
        :type auto_preheat: str
        """
        self._auto_preheat = auto_preheat

    @property
    def thumbnail(self):
        """Gets the thumbnail of this CreateAssetByFileUploadReq.

        :return: The thumbnail of this CreateAssetByFileUploadReq.
        :rtype: :class:`huaweicloudsdkvod.v1.Thumbnail`
        """
        return self._thumbnail

    @thumbnail.setter
    def thumbnail(self, thumbnail):
        """Sets the thumbnail of this CreateAssetByFileUploadReq.

        :param thumbnail: The thumbnail of this CreateAssetByFileUploadReq.
        :type thumbnail: :class:`huaweicloudsdkvod.v1.Thumbnail`
        """
        self._thumbnail = thumbnail

    @property
    def review(self):
        """Gets the review of this CreateAssetByFileUploadReq.

        :return: The review of this CreateAssetByFileUploadReq.
        :rtype: :class:`huaweicloudsdkvod.v1.Review`
        """
        return self._review

    @review.setter
    def review(self, review):
        """Sets the review of this CreateAssetByFileUploadReq.

        :param review: The review of this CreateAssetByFileUploadReq.
        :type review: :class:`huaweicloudsdkvod.v1.Review`
        """
        self._review = review

    @property
    def workflow_name(self):
        """Gets the workflow_name of this CreateAssetByFileUploadReq.

        工作流名称。  若不为空，则使用指定的工作流对上传的音视频进行处理，您可以在视频点播控制台配置工作流，具体请参见[工作流设置](https://support.huaweicloud.com/usermanual-vod/vod010041.html)。

        :return: The workflow_name of this CreateAssetByFileUploadReq.
        :rtype: str
        """
        return self._workflow_name

    @workflow_name.setter
    def workflow_name(self, workflow_name):
        """Sets the workflow_name of this CreateAssetByFileUploadReq.

        工作流名称。  若不为空，则使用指定的工作流对上传的音视频进行处理，您可以在视频点播控制台配置工作流，具体请参见[工作流设置](https://support.huaweicloud.com/usermanual-vod/vod010041.html)。

        :param workflow_name: The workflow_name of this CreateAssetByFileUploadReq.
        :type workflow_name: str
        """
        self._workflow_name = workflow_name

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
        if not isinstance(other, CreateAssetByFileUploadReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
