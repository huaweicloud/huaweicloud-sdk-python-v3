# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PublishAssetFromObsReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'video_type': 'str',
        'title': 'str',
        'description': 'str',
        'category_id': 'int',
        'tags': 'str',
        'auto_publish': 'int',
        'template_group_name': 'str',
        'auto_encrypt': 'int',
        'auto_preheat': 'int',
        'thumbnail': 'Thumbnail',
        'review': 'Review',
        'workflow_name': 'str',
        'input': 'FileAddr',
        'storage_mode': 'int',
        'output_bucket': 'str',
        'output_path': 'str'
    }

    attribute_map = {
        'video_type': 'video_type',
        'title': 'title',
        'description': 'description',
        'category_id': 'category_id',
        'tags': 'tags',
        'auto_publish': 'auto_publish',
        'template_group_name': 'template_group_name',
        'auto_encrypt': 'auto_encrypt',
        'auto_preheat': 'auto_preheat',
        'thumbnail': 'thumbnail',
        'review': 'review',
        'workflow_name': 'workflow_name',
        'input': 'input',
        'storage_mode': 'storage_mode',
        'output_bucket': 'output_bucket',
        'output_path': 'output_path'
    }

    def __init__(self, video_type=None, title=None, description=None, category_id=None, tags=None, auto_publish=None, template_group_name=None, auto_encrypt=None, auto_preheat=None, thumbnail=None, review=None, workflow_name=None, input=None, storage_mode=None, output_bucket=None, output_path=None):
        """PublishAssetFromObsReq

        The model defined in huaweicloud sdk

        :param video_type: 转存的音视频文件类型。  取值如下： - 视频文件：MP4、TS、MOV、MXF、MPG、FLV、WMV、AVI、M4V、F4V、MPEG、3GP、ASF、MKV、HLS - 音频文件：MP3、OGG、WAV、WMA、APE、FLAC、AAC、AC3、MMF、AMR、M4A、M4R、WV、MP2  若上传格式为音频文件，则不支持转码、添加水印和字幕。  &gt; 当**video_type**选择HLS时，**storage_mode**（存储模式）需选择存储在租户桶，且输出路径设置为和输入路径在同一个目录。
        :type video_type: str
        :param title: 媒资标题，长度不超过128个字节，UTF-8编码。
        :type title: str
        :param description: 视频描述，长度不超过1024个字节。
        :type description: str
        :param category_id: 媒资分类ID。  您可以调用[创建媒资分类](https://support.huaweicloud.com/api-vod/vod_04_0028.html)接口或在点播控制台的[分类设置](https://support.huaweicloud.com/usermanual-vod/vod010006.html)中创建对应的媒资分类，并获取分类ID。  &gt; 若不设置或者设置为-1，则上传的音视频归类到系统预置的“其它”分类中。
        :type category_id: int
        :param tags: 视频标签。  单个标签不超过16个字节，最多不超过16个标签。  多个用逗号分隔，UTF8编码。
        :type tags: str
        :param auto_publish: 是否自动发布。  取值如下： - 0：表示不自动发布。 - 1：表示自动发布。  默认值：0。
        :type auto_publish: int
        :param template_group_name: 转码模板组名称。  若不为空，则使用指定的转码模板对上传的音视频进行转码，您可以在视频点播控制台配置转码模板，具体请参见[转码设置](https://support.huaweicloud.com/usermanual-vod/vod_01_0072.html)。  &gt; 若同时设置了“**template_group_name**”和“**workflow_name**”字段，则“**template_group_name**”字段生效。
        :type template_group_name: str
        :param auto_encrypt: 是否自动加密。  取值如下： - 0：表示不加密。 - 1：表示需要加密。  默认值：0。  若设置为需要加密，则必须配置转码模板，且转码的输出格式是HLS。
        :type auto_encrypt: int
        :param auto_preheat: 是否自动预热到CDN。  取值如下： - 0：表示不自动预热。 - 1：表示自动预热。  默认值：0。
        :type auto_preheat: int
        :param thumbnail: 
        :type thumbnail: :class:`huaweicloudsdkvod.v1.Thumbnail`
        :param review: 
        :type review: :class:`huaweicloudsdkvod.v1.Review`
        :param workflow_name: 工作流名称。  若不为空，则使用指定的工作流对上传的音视频进行处理，您可以在视频点播控制台配置工作流，具体请参见[工作流设置](https://support.huaweicloud.com/usermanual-vod/vod010041.html)。
        :type workflow_name: str
        :param input: 
        :type input: :class:`huaweicloudsdkvod.v1.FileAddr`
        :param storage_mode: 存储模式。  取值如下： - 0：表示视频拷贝到点播桶。 - 1：表示视频存储在租户桶。  默认值：0
        :type storage_mode: int
        :param output_bucket: 输出桶名，“**storage_mode**”为1时必选。
        :type output_bucket: str
        :param output_path: 输出路径名，“**storage_mode**”为1时必选。
        :type output_path: str
        """
        
        

        self._video_type = None
        self._title = None
        self._description = None
        self._category_id = None
        self._tags = None
        self._auto_publish = None
        self._template_group_name = None
        self._auto_encrypt = None
        self._auto_preheat = None
        self._thumbnail = None
        self._review = None
        self._workflow_name = None
        self._input = None
        self._storage_mode = None
        self._output_bucket = None
        self._output_path = None
        self.discriminator = None

        self.video_type = video_type
        self.title = title
        if description is not None:
            self.description = description
        if category_id is not None:
            self.category_id = category_id
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
        self.input = input
        if storage_mode is not None:
            self.storage_mode = storage_mode
        if output_bucket is not None:
            self.output_bucket = output_bucket
        if output_path is not None:
            self.output_path = output_path

    @property
    def video_type(self):
        """Gets the video_type of this PublishAssetFromObsReq.

        转存的音视频文件类型。  取值如下： - 视频文件：MP4、TS、MOV、MXF、MPG、FLV、WMV、AVI、M4V、F4V、MPEG、3GP、ASF、MKV、HLS - 音频文件：MP3、OGG、WAV、WMA、APE、FLAC、AAC、AC3、MMF、AMR、M4A、M4R、WV、MP2  若上传格式为音频文件，则不支持转码、添加水印和字幕。  > 当**video_type**选择HLS时，**storage_mode**（存储模式）需选择存储在租户桶，且输出路径设置为和输入路径在同一个目录。

        :return: The video_type of this PublishAssetFromObsReq.
        :rtype: str
        """
        return self._video_type

    @video_type.setter
    def video_type(self, video_type):
        """Sets the video_type of this PublishAssetFromObsReq.

        转存的音视频文件类型。  取值如下： - 视频文件：MP4、TS、MOV、MXF、MPG、FLV、WMV、AVI、M4V、F4V、MPEG、3GP、ASF、MKV、HLS - 音频文件：MP3、OGG、WAV、WMA、APE、FLAC、AAC、AC3、MMF、AMR、M4A、M4R、WV、MP2  若上传格式为音频文件，则不支持转码、添加水印和字幕。  > 当**video_type**选择HLS时，**storage_mode**（存储模式）需选择存储在租户桶，且输出路径设置为和输入路径在同一个目录。

        :param video_type: The video_type of this PublishAssetFromObsReq.
        :type video_type: str
        """
        self._video_type = video_type

    @property
    def title(self):
        """Gets the title of this PublishAssetFromObsReq.

        媒资标题，长度不超过128个字节，UTF-8编码。

        :return: The title of this PublishAssetFromObsReq.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this PublishAssetFromObsReq.

        媒资标题，长度不超过128个字节，UTF-8编码。

        :param title: The title of this PublishAssetFromObsReq.
        :type title: str
        """
        self._title = title

    @property
    def description(self):
        """Gets the description of this PublishAssetFromObsReq.

        视频描述，长度不超过1024个字节。

        :return: The description of this PublishAssetFromObsReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PublishAssetFromObsReq.

        视频描述，长度不超过1024个字节。

        :param description: The description of this PublishAssetFromObsReq.
        :type description: str
        """
        self._description = description

    @property
    def category_id(self):
        """Gets the category_id of this PublishAssetFromObsReq.

        媒资分类ID。  您可以调用[创建媒资分类](https://support.huaweicloud.com/api-vod/vod_04_0028.html)接口或在点播控制台的[分类设置](https://support.huaweicloud.com/usermanual-vod/vod010006.html)中创建对应的媒资分类，并获取分类ID。  > 若不设置或者设置为-1，则上传的音视频归类到系统预置的“其它”分类中。

        :return: The category_id of this PublishAssetFromObsReq.
        :rtype: int
        """
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        """Sets the category_id of this PublishAssetFromObsReq.

        媒资分类ID。  您可以调用[创建媒资分类](https://support.huaweicloud.com/api-vod/vod_04_0028.html)接口或在点播控制台的[分类设置](https://support.huaweicloud.com/usermanual-vod/vod010006.html)中创建对应的媒资分类，并获取分类ID。  > 若不设置或者设置为-1，则上传的音视频归类到系统预置的“其它”分类中。

        :param category_id: The category_id of this PublishAssetFromObsReq.
        :type category_id: int
        """
        self._category_id = category_id

    @property
    def tags(self):
        """Gets the tags of this PublishAssetFromObsReq.

        视频标签。  单个标签不超过16个字节，最多不超过16个标签。  多个用逗号分隔，UTF8编码。

        :return: The tags of this PublishAssetFromObsReq.
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this PublishAssetFromObsReq.

        视频标签。  单个标签不超过16个字节，最多不超过16个标签。  多个用逗号分隔，UTF8编码。

        :param tags: The tags of this PublishAssetFromObsReq.
        :type tags: str
        """
        self._tags = tags

    @property
    def auto_publish(self):
        """Gets the auto_publish of this PublishAssetFromObsReq.

        是否自动发布。  取值如下： - 0：表示不自动发布。 - 1：表示自动发布。  默认值：0。

        :return: The auto_publish of this PublishAssetFromObsReq.
        :rtype: int
        """
        return self._auto_publish

    @auto_publish.setter
    def auto_publish(self, auto_publish):
        """Sets the auto_publish of this PublishAssetFromObsReq.

        是否自动发布。  取值如下： - 0：表示不自动发布。 - 1：表示自动发布。  默认值：0。

        :param auto_publish: The auto_publish of this PublishAssetFromObsReq.
        :type auto_publish: int
        """
        self._auto_publish = auto_publish

    @property
    def template_group_name(self):
        """Gets the template_group_name of this PublishAssetFromObsReq.

        转码模板组名称。  若不为空，则使用指定的转码模板对上传的音视频进行转码，您可以在视频点播控制台配置转码模板，具体请参见[转码设置](https://support.huaweicloud.com/usermanual-vod/vod_01_0072.html)。  > 若同时设置了“**template_group_name**”和“**workflow_name**”字段，则“**template_group_name**”字段生效。

        :return: The template_group_name of this PublishAssetFromObsReq.
        :rtype: str
        """
        return self._template_group_name

    @template_group_name.setter
    def template_group_name(self, template_group_name):
        """Sets the template_group_name of this PublishAssetFromObsReq.

        转码模板组名称。  若不为空，则使用指定的转码模板对上传的音视频进行转码，您可以在视频点播控制台配置转码模板，具体请参见[转码设置](https://support.huaweicloud.com/usermanual-vod/vod_01_0072.html)。  > 若同时设置了“**template_group_name**”和“**workflow_name**”字段，则“**template_group_name**”字段生效。

        :param template_group_name: The template_group_name of this PublishAssetFromObsReq.
        :type template_group_name: str
        """
        self._template_group_name = template_group_name

    @property
    def auto_encrypt(self):
        """Gets the auto_encrypt of this PublishAssetFromObsReq.

        是否自动加密。  取值如下： - 0：表示不加密。 - 1：表示需要加密。  默认值：0。  若设置为需要加密，则必须配置转码模板，且转码的输出格式是HLS。

        :return: The auto_encrypt of this PublishAssetFromObsReq.
        :rtype: int
        """
        return self._auto_encrypt

    @auto_encrypt.setter
    def auto_encrypt(self, auto_encrypt):
        """Sets the auto_encrypt of this PublishAssetFromObsReq.

        是否自动加密。  取值如下： - 0：表示不加密。 - 1：表示需要加密。  默认值：0。  若设置为需要加密，则必须配置转码模板，且转码的输出格式是HLS。

        :param auto_encrypt: The auto_encrypt of this PublishAssetFromObsReq.
        :type auto_encrypt: int
        """
        self._auto_encrypt = auto_encrypt

    @property
    def auto_preheat(self):
        """Gets the auto_preheat of this PublishAssetFromObsReq.

        是否自动预热到CDN。  取值如下： - 0：表示不自动预热。 - 1：表示自动预热。  默认值：0。

        :return: The auto_preheat of this PublishAssetFromObsReq.
        :rtype: int
        """
        return self._auto_preheat

    @auto_preheat.setter
    def auto_preheat(self, auto_preheat):
        """Sets the auto_preheat of this PublishAssetFromObsReq.

        是否自动预热到CDN。  取值如下： - 0：表示不自动预热。 - 1：表示自动预热。  默认值：0。

        :param auto_preheat: The auto_preheat of this PublishAssetFromObsReq.
        :type auto_preheat: int
        """
        self._auto_preheat = auto_preheat

    @property
    def thumbnail(self):
        """Gets the thumbnail of this PublishAssetFromObsReq.

        :return: The thumbnail of this PublishAssetFromObsReq.
        :rtype: :class:`huaweicloudsdkvod.v1.Thumbnail`
        """
        return self._thumbnail

    @thumbnail.setter
    def thumbnail(self, thumbnail):
        """Sets the thumbnail of this PublishAssetFromObsReq.

        :param thumbnail: The thumbnail of this PublishAssetFromObsReq.
        :type thumbnail: :class:`huaweicloudsdkvod.v1.Thumbnail`
        """
        self._thumbnail = thumbnail

    @property
    def review(self):
        """Gets the review of this PublishAssetFromObsReq.

        :return: The review of this PublishAssetFromObsReq.
        :rtype: :class:`huaweicloudsdkvod.v1.Review`
        """
        return self._review

    @review.setter
    def review(self, review):
        """Sets the review of this PublishAssetFromObsReq.

        :param review: The review of this PublishAssetFromObsReq.
        :type review: :class:`huaweicloudsdkvod.v1.Review`
        """
        self._review = review

    @property
    def workflow_name(self):
        """Gets the workflow_name of this PublishAssetFromObsReq.

        工作流名称。  若不为空，则使用指定的工作流对上传的音视频进行处理，您可以在视频点播控制台配置工作流，具体请参见[工作流设置](https://support.huaweicloud.com/usermanual-vod/vod010041.html)。

        :return: The workflow_name of this PublishAssetFromObsReq.
        :rtype: str
        """
        return self._workflow_name

    @workflow_name.setter
    def workflow_name(self, workflow_name):
        """Sets the workflow_name of this PublishAssetFromObsReq.

        工作流名称。  若不为空，则使用指定的工作流对上传的音视频进行处理，您可以在视频点播控制台配置工作流，具体请参见[工作流设置](https://support.huaweicloud.com/usermanual-vod/vod010041.html)。

        :param workflow_name: The workflow_name of this PublishAssetFromObsReq.
        :type workflow_name: str
        """
        self._workflow_name = workflow_name

    @property
    def input(self):
        """Gets the input of this PublishAssetFromObsReq.

        :return: The input of this PublishAssetFromObsReq.
        :rtype: :class:`huaweicloudsdkvod.v1.FileAddr`
        """
        return self._input

    @input.setter
    def input(self, input):
        """Sets the input of this PublishAssetFromObsReq.

        :param input: The input of this PublishAssetFromObsReq.
        :type input: :class:`huaweicloudsdkvod.v1.FileAddr`
        """
        self._input = input

    @property
    def storage_mode(self):
        """Gets the storage_mode of this PublishAssetFromObsReq.

        存储模式。  取值如下： - 0：表示视频拷贝到点播桶。 - 1：表示视频存储在租户桶。  默认值：0

        :return: The storage_mode of this PublishAssetFromObsReq.
        :rtype: int
        """
        return self._storage_mode

    @storage_mode.setter
    def storage_mode(self, storage_mode):
        """Sets the storage_mode of this PublishAssetFromObsReq.

        存储模式。  取值如下： - 0：表示视频拷贝到点播桶。 - 1：表示视频存储在租户桶。  默认值：0

        :param storage_mode: The storage_mode of this PublishAssetFromObsReq.
        :type storage_mode: int
        """
        self._storage_mode = storage_mode

    @property
    def output_bucket(self):
        """Gets the output_bucket of this PublishAssetFromObsReq.

        输出桶名，“**storage_mode**”为1时必选。

        :return: The output_bucket of this PublishAssetFromObsReq.
        :rtype: str
        """
        return self._output_bucket

    @output_bucket.setter
    def output_bucket(self, output_bucket):
        """Sets the output_bucket of this PublishAssetFromObsReq.

        输出桶名，“**storage_mode**”为1时必选。

        :param output_bucket: The output_bucket of this PublishAssetFromObsReq.
        :type output_bucket: str
        """
        self._output_bucket = output_bucket

    @property
    def output_path(self):
        """Gets the output_path of this PublishAssetFromObsReq.

        输出路径名，“**storage_mode**”为1时必选。

        :return: The output_path of this PublishAssetFromObsReq.
        :rtype: str
        """
        return self._output_path

    @output_path.setter
    def output_path(self, output_path):
        """Sets the output_path of this PublishAssetFromObsReq.

        输出路径名，“**storage_mode**”为1时必选。

        :param output_path: The output_path of this PublishAssetFromObsReq.
        :type output_path: str
        """
        self._output_path = output_path

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
        if not isinstance(other, PublishAssetFromObsReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
