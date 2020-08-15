# coding: utf-8

import pprint
import re

import six





class QueryTransTemplate:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'template_name': 'str',
        'tenant_id': 'str',
        'video': 'Video',
        'audio': 'Audio',
        'common': 'Common'
    }

    attribute_map = {
        'template_name': 'template_name',
        'tenant_id': 'tenant_id',
        'video': 'video',
        'audio': 'audio',
        'common': 'common'
    }

    def __init__(self, template_name=None, tenant_id=None, video=None, audio=None, common=None):
        """QueryTransTemplate - a model defined in huaweicloud sdk"""
        
        

        self._template_name = None
        self._tenant_id = None
        self._video = None
        self._audio = None
        self._common = None
        self.discriminator = None

        self.template_name = template_name
        if tenant_id is not None:
            self.tenant_id = tenant_id
        self.video = video
        if audio is not None:
            self.audio = audio
        if common is not None:
            self.common = common

    @property
    def template_name(self):
        """Gets the template_name of this QueryTransTemplate.

        转码模板名称。 

        :return: The template_name of this QueryTransTemplate.
        :rtype: str
        """
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        """Sets the template_name of this QueryTransTemplate.

        转码模板名称。 

        :param template_name: The template_name of this QueryTransTemplate.
        :type: str
        """
        self._template_name = template_name

    @property
    def tenant_id(self):
        """Gets the tenant_id of this QueryTransTemplate.

        租户ID。 

        :return: The tenant_id of this QueryTransTemplate.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this QueryTransTemplate.

        租户ID。 

        :param tenant_id: The tenant_id of this QueryTransTemplate.
        :type: str
        """
        self._tenant_id = tenant_id

    @property
    def video(self):
        """Gets the video of this QueryTransTemplate.


        :return: The video of this QueryTransTemplate.
        :rtype: Video
        """
        return self._video

    @video.setter
    def video(self, video):
        """Sets the video of this QueryTransTemplate.


        :param video: The video of this QueryTransTemplate.
        :type: Video
        """
        self._video = video

    @property
    def audio(self):
        """Gets the audio of this QueryTransTemplate.


        :return: The audio of this QueryTransTemplate.
        :rtype: Audio
        """
        return self._audio

    @audio.setter
    def audio(self, audio):
        """Sets the audio of this QueryTransTemplate.


        :param audio: The audio of this QueryTransTemplate.
        :type: Audio
        """
        self._audio = audio

    @property
    def common(self):
        """Gets the common of this QueryTransTemplate.


        :return: The common of this QueryTransTemplate.
        :rtype: Common
        """
        return self._common

    @common.setter
    def common(self, common):
        """Sets the common of this QueryTransTemplate.


        :param common: The common of this QueryTransTemplate.
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
        if not isinstance(other, QueryTransTemplate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
