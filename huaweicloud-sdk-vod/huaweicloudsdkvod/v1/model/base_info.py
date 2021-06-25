# coding: utf-8

import pprint
import re

import six





class BaseInfo:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'asset_status': 'str',
        'title': 'str',
        'video_name': 'str',
        'description': 'str',
        'category_id': 'int',
        'category_name': 'str',
        'create_time': 'str',
        'last_modified': 'str',
        'video_type': 'str',
        'tags': 'str',
        'meta_data': 'MetaData',
        'video_url': 'str',
        'cover_info_array': 'list[CoverInfo]',
        'subtitle_info': 'list[SubtitleInfo]',
        'sourch_path': 'FileAddr',
        'source_path': 'FileAddr',
        'output_path': 'FileAddr',
        'create_user': 'str',
        'privilege': 'str',
        'folder_name': 'str',
        'custom_metadata': 'dict(str, object)'
    }

    attribute_map = {
        'asset_status': 'asset_status',
        'title': 'title',
        'video_name': 'video_name',
        'description': 'description',
        'category_id': 'category_id',
        'category_name': 'category_name',
        'create_time': 'create_time',
        'last_modified': 'last_modified',
        'video_type': 'video_type',
        'tags': 'tags',
        'meta_data': 'meta_data',
        'video_url': 'video_url',
        'cover_info_array': 'cover_info_array',
        'subtitle_info': 'subtitle_info',
        'sourch_path': 'sourch_path',
        'source_path': 'source_path',
        'output_path': 'output_path',
        'create_user': 'create_user',
        'privilege': 'privilege',
        'folder_name': 'folder_name',
        'custom_metadata': 'custom_metadata'
    }

    def __init__(self, asset_status=None, title=None, video_name=None, description=None, category_id=None, category_name=None, create_time=None, last_modified=None, video_type=None, tags=None, meta_data=None, video_url=None, cover_info_array=None, subtitle_info=None, sourch_path=None, source_path=None, output_path=None, create_user=None, privilege=None, folder_name=None, custom_metadata=None):
        """BaseInfo - a model defined in huaweicloud sdk"""
        
        

        self._asset_status = None
        self._title = None
        self._video_name = None
        self._description = None
        self._category_id = None
        self._category_name = None
        self._create_time = None
        self._last_modified = None
        self._video_type = None
        self._tags = None
        self._meta_data = None
        self._video_url = None
        self._cover_info_array = None
        self._subtitle_info = None
        self._sourch_path = None
        self._source_path = None
        self._output_path = None
        self._create_user = None
        self._privilege = None
        self._folder_name = None
        self._custom_metadata = None
        self.discriminator = None

        if asset_status is not None:
            self.asset_status = asset_status
        if title is not None:
            self.title = title
        if video_name is not None:
            self.video_name = video_name
        if description is not None:
            self.description = description
        if category_id is not None:
            self.category_id = category_id
        if category_name is not None:
            self.category_name = category_name
        if create_time is not None:
            self.create_time = create_time
        if last_modified is not None:
            self.last_modified = last_modified
        if video_type is not None:
            self.video_type = video_type
        if tags is not None:
            self.tags = tags
        if meta_data is not None:
            self.meta_data = meta_data
        if video_url is not None:
            self.video_url = video_url
        if cover_info_array is not None:
            self.cover_info_array = cover_info_array
        if subtitle_info is not None:
            self.subtitle_info = subtitle_info
        if sourch_path is not None:
            self.sourch_path = sourch_path
        if source_path is not None:
            self.source_path = source_path
        if output_path is not None:
            self.output_path = output_path
        if create_user is not None:
            self.create_user = create_user
        if privilege is not None:
            self.privilege = privilege
        if folder_name is not None:
            self.folder_name = folder_name
        if custom_metadata is not None:
            self.custom_metadata = custom_metadata

    @property
    def asset_status(self):
        """Gets the asset_status of this BaseInfo.

        媒资状态。 \"CREATING\"   //上传中 \"FAILED\"     //上传失败 \"CREATED\"  //上传成功 \"PUBLISHED\"  //已发布 \"DELETED\"  //已删除 

        :return: The asset_status of this BaseInfo.
        :rtype: str
        """
        return self._asset_status

    @asset_status.setter
    def asset_status(self, asset_status):
        """Sets the asset_status of this BaseInfo.

        媒资状态。 \"CREATING\"   //上传中 \"FAILED\"     //上传失败 \"CREATED\"  //上传成功 \"PUBLISHED\"  //已发布 \"DELETED\"  //已删除 

        :param asset_status: The asset_status of this BaseInfo.
        :type: str
        """
        self._asset_status = asset_status

    @property
    def title(self):
        """Gets the title of this BaseInfo.

        媒体标题<br/> 

        :return: The title of this BaseInfo.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this BaseInfo.

        媒体标题<br/> 

        :param title: The title of this BaseInfo.
        :type: str
        """
        self._title = title

    @property
    def video_name(self):
        """Gets the video_name of this BaseInfo.

        视频文件名<br/> 

        :return: The video_name of this BaseInfo.
        :rtype: str
        """
        return self._video_name

    @video_name.setter
    def video_name(self, video_name):
        """Sets the video_name of this BaseInfo.

        视频文件名<br/> 

        :param video_name: The video_name of this BaseInfo.
        :type: str
        """
        self._video_name = video_name

    @property
    def description(self):
        """Gets the description of this BaseInfo.

        视频描述<br/> 

        :return: The description of this BaseInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this BaseInfo.

        视频描述<br/> 

        :param description: The description of this BaseInfo.
        :type: str
        """
        self._description = description

    @property
    def category_id(self):
        """Gets the category_id of this BaseInfo.

        媒资分类id<br/> 

        :return: The category_id of this BaseInfo.
        :rtype: int
        """
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        """Sets the category_id of this BaseInfo.

        媒资分类id<br/> 

        :param category_id: The category_id of this BaseInfo.
        :type: int
        """
        self._category_id = category_id

    @property
    def category_name(self):
        """Gets the category_name of this BaseInfo.

        媒资分类名称<br/> 

        :return: The category_name of this BaseInfo.
        :rtype: str
        """
        return self._category_name

    @category_name.setter
    def category_name(self, category_name):
        """Sets the category_name of this BaseInfo.

        媒资分类名称<br/> 

        :param category_name: The category_name of this BaseInfo.
        :type: str
        """
        self._category_name = category_name

    @property
    def create_time(self):
        """Gets the create_time of this BaseInfo.

        媒资创建时间<br/> 

        :return: The create_time of this BaseInfo.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this BaseInfo.

        媒资创建时间<br/> 

        :param create_time: The create_time of this BaseInfo.
        :type: str
        """
        self._create_time = create_time

    @property
    def last_modified(self):
        """Gets the last_modified of this BaseInfo.

        媒资最近修改时间<br/> 

        :return: The last_modified of this BaseInfo.
        :rtype: str
        """
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified):
        """Sets the last_modified of this BaseInfo.

        媒资最近修改时间<br/> 

        :param last_modified: The last_modified of this BaseInfo.
        :type: str
        """
        self._last_modified = last_modified

    @property
    def video_type(self):
        """Gets the video_type of this BaseInfo.

        音视频文件类型。 取值如下： 视频文件：MP4、TS、MOV、MXF、MPG、FLV、WMV、AVI、M4V、F4V、MPEG、3GP、ASF、MKV 音频文件：MP3、OGG、WAV、WMA、APE、FLAC、AAC、AC3、MMF、AMR、M4A、M4R、WV、MP2 

        :return: The video_type of this BaseInfo.
        :rtype: str
        """
        return self._video_type

    @video_type.setter
    def video_type(self, video_type):
        """Sets the video_type of this BaseInfo.

        音视频文件类型。 取值如下： 视频文件：MP4、TS、MOV、MXF、MPG、FLV、WMV、AVI、M4V、F4V、MPEG、3GP、ASF、MKV 音频文件：MP3、OGG、WAV、WMA、APE、FLAC、AAC、AC3、MMF、AMR、M4A、M4R、WV、MP2 

        :param video_type: The video_type of this BaseInfo.
        :type: str
        """
        self._video_type = video_type

    @property
    def tags(self):
        """Gets the tags of this BaseInfo.

        视频标签<br/> 

        :return: The tags of this BaseInfo.
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this BaseInfo.

        视频标签<br/> 

        :param tags: The tags of this BaseInfo.
        :type: str
        """
        self._tags = tags

    @property
    def meta_data(self):
        """Gets the meta_data of this BaseInfo.


        :return: The meta_data of this BaseInfo.
        :rtype: MetaData
        """
        return self._meta_data

    @meta_data.setter
    def meta_data(self, meta_data):
        """Sets the meta_data of this BaseInfo.


        :param meta_data: The meta_data of this BaseInfo.
        :type: MetaData
        """
        self._meta_data = meta_data

    @property
    def video_url(self):
        """Gets the video_url of this BaseInfo.

        原始视频文件的下载地址<br/> 

        :return: The video_url of this BaseInfo.
        :rtype: str
        """
        return self._video_url

    @video_url.setter
    def video_url(self, video_url):
        """Sets the video_url of this BaseInfo.

        原始视频文件的下载地址<br/> 

        :param video_url: The video_url of this BaseInfo.
        :type: str
        """
        self._video_url = video_url

    @property
    def cover_info_array(self):
        """Gets the cover_info_array of this BaseInfo.

        封面信息数组<br/> 

        :return: The cover_info_array of this BaseInfo.
        :rtype: list[CoverInfo]
        """
        return self._cover_info_array

    @cover_info_array.setter
    def cover_info_array(self, cover_info_array):
        """Sets the cover_info_array of this BaseInfo.

        封面信息数组<br/> 

        :param cover_info_array: The cover_info_array of this BaseInfo.
        :type: list[CoverInfo]
        """
        self._cover_info_array = cover_info_array

    @property
    def subtitle_info(self):
        """Gets the subtitle_info of this BaseInfo.

        字幕信息数组<br/> 

        :return: The subtitle_info of this BaseInfo.
        :rtype: list[SubtitleInfo]
        """
        return self._subtitle_info

    @subtitle_info.setter
    def subtitle_info(self, subtitle_info):
        """Sets the subtitle_info of this BaseInfo.

        字幕信息数组<br/> 

        :param subtitle_info: The subtitle_info of this BaseInfo.
        :type: list[SubtitleInfo]
        """
        self._subtitle_info = subtitle_info

    @property
    def sourch_path(self):
        """Gets the sourch_path of this BaseInfo.


        :return: The sourch_path of this BaseInfo.
        :rtype: FileAddr
        """
        return self._sourch_path

    @sourch_path.setter
    def sourch_path(self, sourch_path):
        """Sets the sourch_path of this BaseInfo.


        :param sourch_path: The sourch_path of this BaseInfo.
        :type: FileAddr
        """
        self._sourch_path = sourch_path

    @property
    def source_path(self):
        """Gets the source_path of this BaseInfo.


        :return: The source_path of this BaseInfo.
        :rtype: FileAddr
        """
        return self._source_path

    @source_path.setter
    def source_path(self, source_path):
        """Sets the source_path of this BaseInfo.


        :param source_path: The source_path of this BaseInfo.
        :type: FileAddr
        """
        self._source_path = source_path

    @property
    def output_path(self):
        """Gets the output_path of this BaseInfo.


        :return: The output_path of this BaseInfo.
        :rtype: FileAddr
        """
        return self._output_path

    @output_path.setter
    def output_path(self, output_path):
        """Sets the output_path of this BaseInfo.


        :param output_path: The output_path of this BaseInfo.
        :type: FileAddr
        """
        self._output_path = output_path

    @property
    def create_user(self):
        """Gets the create_user of this BaseInfo.

        创建该资源的用户<br/> 

        :return: The create_user of this BaseInfo.
        :rtype: str
        """
        return self._create_user

    @create_user.setter
    def create_user(self, create_user):
        """Sets the create_user of this BaseInfo.

        创建该资源的用户<br/> 

        :param create_user: The create_user of this BaseInfo.
        :type: str
        """
        self._create_user = create_user

    @property
    def privilege(self):
        """Gets the privilege of this BaseInfo.

        权限<br/> 

        :return: The privilege of this BaseInfo.
        :rtype: str
        """
        return self._privilege

    @privilege.setter
    def privilege(self, privilege):
        """Sets the privilege of this BaseInfo.

        权限<br/> 

        :param privilege: The privilege of this BaseInfo.
        :type: str
        """
        self._privilege = privilege

    @property
    def folder_name(self):
        """Gets the folder_name of this BaseInfo.

        文件夹code<br/> 

        :return: The folder_name of this BaseInfo.
        :rtype: str
        """
        return self._folder_name

    @folder_name.setter
    def folder_name(self, folder_name):
        """Sets the folder_name of this BaseInfo.

        文件夹code<br/> 

        :param folder_name: The folder_name of this BaseInfo.
        :type: str
        """
        self._folder_name = folder_name

    @property
    def custom_metadata(self):
        """Gets the custom_metadata of this BaseInfo.

        自定义元数据<br/> 

        :return: The custom_metadata of this BaseInfo.
        :rtype: dict(str, object)
        """
        return self._custom_metadata

    @custom_metadata.setter
    def custom_metadata(self, custom_metadata):
        """Sets the custom_metadata of this BaseInfo.

        自定义元数据<br/> 

        :param custom_metadata: The custom_metadata of this BaseInfo.
        :type: dict(str, object)
        """
        self._custom_metadata = custom_metadata

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
        if not isinstance(other, BaseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
