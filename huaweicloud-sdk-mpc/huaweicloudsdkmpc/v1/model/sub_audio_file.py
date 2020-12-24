# coding: utf-8

import pprint
import re

import six





class SubAudioFile:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'tracks_info': 'list[TracksInfo]',
        'input': 'ObsObjInfo',
        'output': 'ObsObjInfo',
        'output_filename': 'str'
    }

    attribute_map = {
        'tracks_info': 'tracks_info',
        'input': 'input',
        'output': 'output',
        'output_filename': 'output_filename'
    }

    def __init__(self, tracks_info=None, input=None, output=None, output_filename=None):
        """SubAudioFile - a model defined in huaweicloud sdk"""
        
        

        self._tracks_info = None
        self._input = None
        self._output = None
        self._output_filename = None
        self.discriminator = None

        if tracks_info is not None:
            self.tracks_info = tracks_info
        if input is not None:
            self.input = input
        if output is not None:
            self.output = output
        if output_filename is not None:
            self.output_filename = output_filename

    @property
    def tracks_info(self):
        """Gets the tracks_info of this SubAudioFile.

        音轨信息

        :return: The tracks_info of this SubAudioFile.
        :rtype: list[TracksInfo]
        """
        return self._tracks_info

    @tracks_info.setter
    def tracks_info(self, tracks_info):
        """Sets the tracks_info of this SubAudioFile.

        音轨信息

        :param tracks_info: The tracks_info of this SubAudioFile.
        :type: list[TracksInfo]
        """
        self._tracks_info = tracks_info

    @property
    def input(self):
        """Gets the input of this SubAudioFile.


        :return: The input of this SubAudioFile.
        :rtype: ObsObjInfo
        """
        return self._input

    @input.setter
    def input(self, input):
        """Sets the input of this SubAudioFile.


        :param input: The input of this SubAudioFile.
        :type: ObsObjInfo
        """
        self._input = input

    @property
    def output(self):
        """Gets the output of this SubAudioFile.


        :return: The output of this SubAudioFile.
        :rtype: ObsObjInfo
        """
        return self._output

    @output.setter
    def output(self, output):
        """Sets the output of this SubAudioFile.


        :param output: The output of this SubAudioFile.
        :type: ObsObjInfo
        """
        self._output = output

    @property
    def output_filename(self):
        """Gets the output_filename of this SubAudioFile.

        输出文件名。 

        :return: The output_filename of this SubAudioFile.
        :rtype: str
        """
        return self._output_filename

    @output_filename.setter
    def output_filename(self, output_filename):
        """Sets the output_filename of this SubAudioFile.

        输出文件名。 

        :param output_filename: The output_filename of this SubAudioFile.
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
        if not isinstance(other, SubAudioFile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
