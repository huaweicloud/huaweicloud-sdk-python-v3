# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModifyTransTemplateGroup:

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
        'videos': 'list[VideoObj]',
        'audio': 'Audio',
        'video_common': 'VideoCommon',
        'common': 'Common'
    }

    attribute_map = {
        'group_id': 'group_id',
        'name': 'name',
        'videos': 'videos',
        'audio': 'audio',
        'video_common': 'video_common',
        'common': 'common'
    }

    def __init__(self, group_id=None, name=None, videos=None, audio=None, video_common=None, common=None):
        """ModifyTransTemplateGroup

        The model defined in huaweicloud sdk

        :param group_id: 模板组ID 
        :type group_id: str
        :param name: 模板组名称 
        :type name: str
        :param videos: 视频信息列表 
        :type videos: list[:class:`huaweicloudsdkmpc.v1.VideoObj`]
        :param audio: 
        :type audio: :class:`huaweicloudsdkmpc.v1.Audio`
        :param video_common: 
        :type video_common: :class:`huaweicloudsdkmpc.v1.VideoCommon`
        :param common: 
        :type common: :class:`huaweicloudsdkmpc.v1.Common`
        """
        
        

        self._group_id = None
        self._name = None
        self._videos = None
        self._audio = None
        self._video_common = None
        self._common = None
        self.discriminator = None

        self.group_id = group_id
        if name is not None:
            self.name = name
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
        """Gets the group_id of this ModifyTransTemplateGroup.

        模板组ID 

        :return: The group_id of this ModifyTransTemplateGroup.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this ModifyTransTemplateGroup.

        模板组ID 

        :param group_id: The group_id of this ModifyTransTemplateGroup.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def name(self):
        """Gets the name of this ModifyTransTemplateGroup.

        模板组名称 

        :return: The name of this ModifyTransTemplateGroup.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ModifyTransTemplateGroup.

        模板组名称 

        :param name: The name of this ModifyTransTemplateGroup.
        :type name: str
        """
        self._name = name

    @property
    def videos(self):
        """Gets the videos of this ModifyTransTemplateGroup.

        视频信息列表 

        :return: The videos of this ModifyTransTemplateGroup.
        :rtype: list[:class:`huaweicloudsdkmpc.v1.VideoObj`]
        """
        return self._videos

    @videos.setter
    def videos(self, videos):
        """Sets the videos of this ModifyTransTemplateGroup.

        视频信息列表 

        :param videos: The videos of this ModifyTransTemplateGroup.
        :type videos: list[:class:`huaweicloudsdkmpc.v1.VideoObj`]
        """
        self._videos = videos

    @property
    def audio(self):
        """Gets the audio of this ModifyTransTemplateGroup.

        :return: The audio of this ModifyTransTemplateGroup.
        :rtype: :class:`huaweicloudsdkmpc.v1.Audio`
        """
        return self._audio

    @audio.setter
    def audio(self, audio):
        """Sets the audio of this ModifyTransTemplateGroup.

        :param audio: The audio of this ModifyTransTemplateGroup.
        :type audio: :class:`huaweicloudsdkmpc.v1.Audio`
        """
        self._audio = audio

    @property
    def video_common(self):
        """Gets the video_common of this ModifyTransTemplateGroup.

        :return: The video_common of this ModifyTransTemplateGroup.
        :rtype: :class:`huaweicloudsdkmpc.v1.VideoCommon`
        """
        return self._video_common

    @video_common.setter
    def video_common(self, video_common):
        """Sets the video_common of this ModifyTransTemplateGroup.

        :param video_common: The video_common of this ModifyTransTemplateGroup.
        :type video_common: :class:`huaweicloudsdkmpc.v1.VideoCommon`
        """
        self._video_common = video_common

    @property
    def common(self):
        """Gets the common of this ModifyTransTemplateGroup.

        :return: The common of this ModifyTransTemplateGroup.
        :rtype: :class:`huaweicloudsdkmpc.v1.Common`
        """
        return self._common

    @common.setter
    def common(self, common):
        """Sets the common of this ModifyTransTemplateGroup.

        :param common: The common of this ModifyTransTemplateGroup.
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
        if not isinstance(other, ModifyTransTemplateGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
