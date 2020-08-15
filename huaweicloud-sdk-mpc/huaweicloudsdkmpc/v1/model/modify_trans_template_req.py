# coding: utf-8

import pprint
import re

import six





class ModifyTransTemplateReq:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'template_id': 'int',
        'template_name': 'str',
        'video': 'Video',
        'audio': 'Audio',
        'common': 'Common'
    }

    attribute_map = {
        'template_id': 'template_id',
        'template_name': 'template_name',
        'video': 'video',
        'audio': 'audio',
        'common': 'common'
    }

    def __init__(self, template_id=None, template_name=None, video=None, audio=None, common=None):
        """ModifyTransTemplateReq - a model defined in huaweicloud sdk"""
        
        

        self._template_id = None
        self._template_name = None
        self._video = None
        self._audio = None
        self._common = None
        self.discriminator = None

        self.template_id = template_id
        self.template_name = template_name
        if video is not None:
            self.video = video
        if audio is not None:
            self.audio = audio
        self.common = common

    @property
    def template_id(self):
        """Gets the template_id of this ModifyTransTemplateReq.

        转码模板ID 

        :return: The template_id of this ModifyTransTemplateReq.
        :rtype: int
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """Sets the template_id of this ModifyTransTemplateReq.

        转码模板ID 

        :param template_id: The template_id of this ModifyTransTemplateReq.
        :type: int
        """
        self._template_id = template_id

    @property
    def template_name(self):
        """Gets the template_name of this ModifyTransTemplateReq.

        转码模板名称。 

        :return: The template_name of this ModifyTransTemplateReq.
        :rtype: str
        """
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        """Sets the template_name of this ModifyTransTemplateReq.

        转码模板名称。 

        :param template_name: The template_name of this ModifyTransTemplateReq.
        :type: str
        """
        self._template_name = template_name

    @property
    def video(self):
        """Gets the video of this ModifyTransTemplateReq.


        :return: The video of this ModifyTransTemplateReq.
        :rtype: Video
        """
        return self._video

    @video.setter
    def video(self, video):
        """Sets the video of this ModifyTransTemplateReq.


        :param video: The video of this ModifyTransTemplateReq.
        :type: Video
        """
        self._video = video

    @property
    def audio(self):
        """Gets the audio of this ModifyTransTemplateReq.


        :return: The audio of this ModifyTransTemplateReq.
        :rtype: Audio
        """
        return self._audio

    @audio.setter
    def audio(self, audio):
        """Sets the audio of this ModifyTransTemplateReq.


        :param audio: The audio of this ModifyTransTemplateReq.
        :type: Audio
        """
        self._audio = audio

    @property
    def common(self):
        """Gets the common of this ModifyTransTemplateReq.


        :return: The common of this ModifyTransTemplateReq.
        :rtype: Common
        """
        return self._common

    @common.setter
    def common(self, common):
        """Sets the common of this ModifyTransTemplateReq.


        :param common: The common of this ModifyTransTemplateReq.
        :type: Common
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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ModifyTransTemplateReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
