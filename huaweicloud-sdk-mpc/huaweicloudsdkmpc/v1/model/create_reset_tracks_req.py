# coding: utf-8

import pprint
import re

import six





class CreateResetTracksReq:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'audio_file': 'SubAudioFile'
    }

    attribute_map = {
        'audio_file': 'audio_file'
    }

    def __init__(self, audio_file=None):
        """CreateResetTracksReq - a model defined in huaweicloud sdk"""
        
        

        self._audio_file = None
        self.discriminator = None

        if audio_file is not None:
            self.audio_file = audio_file

    @property
    def audio_file(self):
        """Gets the audio_file of this CreateResetTracksReq.


        :return: The audio_file of this CreateResetTracksReq.
        :rtype: SubAudioFile
        """
        return self._audio_file

    @audio_file.setter
    def audio_file(self, audio_file):
        """Sets the audio_file of this CreateResetTracksReq.


        :param audio_file: The audio_file of this CreateResetTracksReq.
        :type: SubAudioFile
        """
        self._audio_file = audio_file

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
        if not isinstance(other, CreateResetTracksReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
