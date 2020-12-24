# coding: utf-8

import pprint
import re

import six





class MpcMultiAudio:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'output': 'ObsObjInfo',
        'audio_files': 'list[AudioFile]',
        'output_filename': 'str'
    }

    attribute_map = {
        'output': 'output',
        'audio_files': 'audio_files',
        'output_filename': 'output_filename'
    }

    def __init__(self, output=None, audio_files=None, output_filename=None):
        """MpcMultiAudio - a model defined in huaweicloud sdk"""
        
        

        self._output = None
        self._audio_files = None
        self._output_filename = None
        self.discriminator = None

        if output is not None:
            self.output = output
        if audio_files is not None:
            self.audio_files = audio_files
        if output_filename is not None:
            self.output_filename = output_filename

    @property
    def output(self):
        """Gets the output of this MpcMultiAudio.


        :return: The output of this MpcMultiAudio.
        :rtype: ObsObjInfo
        """
        return self._output

    @output.setter
    def output(self, output):
        """Sets the output of this MpcMultiAudio.


        :param output: The output of this MpcMultiAudio.
        :type: ObsObjInfo
        """
        self._output = output

    @property
    def audio_files(self):
        """Gets the audio_files of this MpcMultiAudio.

        音频文件列表

        :return: The audio_files of this MpcMultiAudio.
        :rtype: list[AudioFile]
        """
        return self._audio_files

    @audio_files.setter
    def audio_files(self, audio_files):
        """Sets the audio_files of this MpcMultiAudio.

        音频文件列表

        :param audio_files: The audio_files of this MpcMultiAudio.
        :type: list[AudioFile]
        """
        self._audio_files = audio_files

    @property
    def output_filename(self):
        """Gets the output_filename of this MpcMultiAudio.

        输出文件名。 

        :return: The output_filename of this MpcMultiAudio.
        :rtype: str
        """
        return self._output_filename

    @output_filename.setter
    def output_filename(self, output_filename):
        """Sets the output_filename of this MpcMultiAudio.

        输出文件名。 

        :param output_filename: The output_filename of this MpcMultiAudio.
        :type: str
        """
        self._output_filename = output_filename

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
        if not isinstance(other, MpcMultiAudio):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
