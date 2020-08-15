# coding: utf-8

import pprint
import re

import six





class Multidrm:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'content_id': 'str',
        'streaming_mode': 'str',
        'encrypt_audio': 'int',
        'emi': 'int',
        'drm_list': 'list[str]'
    }

    attribute_map = {
        'content_id': 'content_id',
        'streaming_mode': 'streaming_mode',
        'encrypt_audio': 'encrypt_audio',
        'emi': 'emi',
        'drm_list': 'drm_list'
    }

    def __init__(self, content_id=None, streaming_mode=None, encrypt_audio=None, emi=16420, drm_list=None):
        """Multidrm - a model defined in huaweicloud sdk"""
        
        

        self._content_id = None
        self._streaming_mode = None
        self._encrypt_audio = None
        self._emi = None
        self._drm_list = None
        self.discriminator = None

        if content_id is not None:
            self.content_id = content_id
        self.streaming_mode = streaming_mode
        if encrypt_audio is not None:
            self.encrypt_audio = encrypt_audio
        if emi is not None:
            self.emi = emi
        self.drm_list = drm_list

    @property
    def content_id(self):
        """Gets the content_id of this Multidrm.

        唯一标识 

        :return: The content_id of this Multidrm.
        :rtype: str
        """
        return self._content_id

    @content_id.setter
    def content_id(self, content_id):
        """Sets the content_id of this Multidrm.

        唯一标识 

        :param content_id: The content_id of this Multidrm.
        :type: str
        """
        self._content_id = content_id

    @property
    def streaming_mode(self):
        """Gets the streaming_mode of this Multidrm.

        定义数据流的类型，取值为DASH或HLS 

        :return: The streaming_mode of this Multidrm.
        :rtype: str
        """
        return self._streaming_mode

    @streaming_mode.setter
    def streaming_mode(self, streaming_mode):
        """Sets the streaming_mode of this Multidrm.

        定义数据流的类型，取值为DASH或HLS 

        :param streaming_mode: The streaming_mode of this Multidrm.
        :type: str
        """
        self._streaming_mode = streaming_mode

    @property
    def encrypt_audio(self):
        """Gets the encrypt_audio of this Multidrm.

        音频加密开关。  取值如下： - 0：标识音频不加密。 - 1：标识音频加密。  默认值：0。 该参数只对dash有效。 

        :return: The encrypt_audio of this Multidrm.
        :rtype: int
        """
        return self._encrypt_audio

    @encrypt_audio.setter
    def encrypt_audio(self, encrypt_audio):
        """Sets the encrypt_audio of this Multidrm.

        音频加密开关。  取值如下： - 0：标识音频不加密。 - 1：标识音频加密。  默认值：0。 该参数只对dash有效。 

        :param encrypt_audio: The encrypt_audio of this Multidrm.
        :type: int
        """
        self._encrypt_audio = encrypt_audio

    @property
    def emi(self):
        """Gets the emi of this Multidrm.

        定义加密方式。  取值如下： - 16418(AES-128,CBC) - 16420(AES-128,CTR) - 16422(SM4CBC) 

        :return: The emi of this Multidrm.
        :rtype: int
        """
        return self._emi

    @emi.setter
    def emi(self, emi):
        """Sets the emi of this Multidrm.

        定义加密方式。  取值如下： - 16418(AES-128,CBC) - 16420(AES-128,CTR) - 16422(SM4CBC) 

        :param emi: The emi of this Multidrm.
        :type: int
        """
        self._emi = emi

    @property
    def drm_list(self):
        """Gets the drm_list of this Multidrm.

        HLS视频加密控制参数。  取值如下： - PLAYREADY - CHINA_DRM - WIDEVINE 

        :return: The drm_list of this Multidrm.
        :rtype: list[str]
        """
        return self._drm_list

    @drm_list.setter
    def drm_list(self, drm_list):
        """Sets the drm_list of this Multidrm.

        HLS视频加密控制参数。  取值如下： - PLAYREADY - CHINA_DRM - WIDEVINE 

        :param drm_list: The drm_list of this Multidrm.
        :type: list[str]
        """
        self._drm_list = drm_list

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
        if not isinstance(other, Multidrm):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
