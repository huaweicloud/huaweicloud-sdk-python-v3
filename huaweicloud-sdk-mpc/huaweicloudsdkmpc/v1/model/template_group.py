# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TemplateGroup:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'group_id': 'str',
        'name': 'str',
        'template_ids': 'list[int]',
        'videos': 'list[VideoAndTemplate]',
        'audio': 'Audio',
        'video_common': 'VideoCommon',
        'common': 'Common'
    }

    attribute_map = {
        'group_id': 'group_id',
        'name': 'name',
        'template_ids': 'template_ids',
        'videos': 'videos',
        'audio': 'audio',
        'video_common': 'video_common',
        'common': 'common'
    }

    def __init__(self, group_id=None, name=None, template_ids=None, videos=None, audio=None, video_common=None, common=None):
        """TemplateGroup

        The model defined in huaweicloud sdk

        :param group_id: 模板组id 
        :type group_id: str
        :param name: 模板组名称 
        :type name: str
        :param template_ids: 模板组模板ID 
        :type template_ids: list[int]
        :param videos: 视频信息列表 
        :type videos: list[:class:`huaweicloudsdkmpc.v1.VideoAndTemplate`]
        :param audio: 
        :type audio: :class:`huaweicloudsdkmpc.v1.Audio`
        :param video_common: 
        :type video_common: :class:`huaweicloudsdkmpc.v1.VideoCommon`
        :param common: 
        :type common: :class:`huaweicloudsdkmpc.v1.Common`
        """
        
        

        self._group_id = None
        self._name = None
        self._template_ids = None
        self._videos = None
        self._audio = None
        self._video_common = None
        self._common = None
        self.discriminator = None

        if group_id is not None:
            self.group_id = group_id
        if name is not None:
            self.name = name
        if template_ids is not None:
            self.template_ids = template_ids
        if videos is not None:
            self.videos = videos
        if audio is not None:
            self.audio = audio
        if video_common is not None:
            self.video_common = video_common
        if common is not None:
            self.common = common

    @property
    def group_id(self):
        """Gets the group_id of this TemplateGroup.

        模板组id 

        :return: The group_id of this TemplateGroup.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this TemplateGroup.

        模板组id 

        :param group_id: The group_id of this TemplateGroup.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def name(self):
        """Gets the name of this TemplateGroup.

        模板组名称 

        :return: The name of this TemplateGroup.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TemplateGroup.

        模板组名称 

        :param name: The name of this TemplateGroup.
        :type name: str
        """
        self._name = name

    @property
    def template_ids(self):
        """Gets the template_ids of this TemplateGroup.

        模板组模板ID 

        :return: The template_ids of this TemplateGroup.
        :rtype: list[int]
        """
        return self._template_ids

    @template_ids.setter
    def template_ids(self, template_ids):
        """Sets the template_ids of this TemplateGroup.

        模板组模板ID 

        :param template_ids: The template_ids of this TemplateGroup.
        :type template_ids: list[int]
        """
        self._template_ids = template_ids

    @property
    def videos(self):
        """Gets the videos of this TemplateGroup.

        视频信息列表 

        :return: The videos of this TemplateGroup.
        :rtype: list[:class:`huaweicloudsdkmpc.v1.VideoAndTemplate`]
        """
        return self._videos

    @videos.setter
    def videos(self, videos):
        """Sets the videos of this TemplateGroup.

        视频信息列表 

        :param videos: The videos of this TemplateGroup.
        :type videos: list[:class:`huaweicloudsdkmpc.v1.VideoAndTemplate`]
        """
        self._videos = videos

    @property
    def audio(self):
        """Gets the audio of this TemplateGroup.


        :return: The audio of this TemplateGroup.
        :rtype: :class:`huaweicloudsdkmpc.v1.Audio`
        """
        return self._audio

    @audio.setter
    def audio(self, audio):
        """Sets the audio of this TemplateGroup.


        :param audio: The audio of this TemplateGroup.
        :type audio: :class:`huaweicloudsdkmpc.v1.Audio`
        """
        self._audio = audio

    @property
    def video_common(self):
        """Gets the video_common of this TemplateGroup.


        :return: The video_common of this TemplateGroup.
        :rtype: :class:`huaweicloudsdkmpc.v1.VideoCommon`
        """
        return self._video_common

    @video_common.setter
    def video_common(self, video_common):
        """Sets the video_common of this TemplateGroup.


        :param video_common: The video_common of this TemplateGroup.
        :type video_common: :class:`huaweicloudsdkmpc.v1.VideoCommon`
        """
        self._video_common = video_common

    @property
    def common(self):
        """Gets the common of this TemplateGroup.


        :return: The common of this TemplateGroup.
        :rtype: :class:`huaweicloudsdkmpc.v1.Common`
        """
        return self._common

    @common.setter
    def common(self, common):
        """Sets the common of this TemplateGroup.


        :param common: The common of this TemplateGroup.
        :type common: :class:`huaweicloudsdkmpc.v1.Common`
        """
        self._common = common

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
        if not isinstance(other, TemplateGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
