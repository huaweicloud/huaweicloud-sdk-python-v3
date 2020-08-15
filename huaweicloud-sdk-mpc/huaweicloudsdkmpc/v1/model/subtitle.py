# coding: utf-8

import pprint
import re

import six





class Subtitle:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'input': 'ObsObjInfo',
        'inputs': 'list[MulInputFileInfo]',
        'subtitle_type': 'int'
    }

    attribute_map = {
        'input': 'input',
        'inputs': 'inputs',
        'subtitle_type': 'subtitle_type'
    }

    def __init__(self, input=None, inputs=None, subtitle_type=None):
        """Subtitle - a model defined in huaweicloud sdk"""
        
        

        self._input = None
        self._inputs = None
        self._subtitle_type = None
        self.discriminator = None

        if input is not None:
            self.input = input
        if inputs is not None:
            self.inputs = inputs
        if subtitle_type is not None:
            self.subtitle_type = subtitle_type

    @property
    def input(self):
        """Gets the input of this Subtitle.


        :return: The input of this Subtitle.
        :rtype: ObsObjInfo
        """
        return self._input

    @input.setter
    def input(self, input):
        """Sets the input of this Subtitle.


        :param input: The input of this Subtitle.
        :type: ObsObjInfo
        """
        self._input = input

    @property
    def inputs(self):
        """Gets the inputs of this Subtitle.

        多字幕文件地址。 

        :return: The inputs of this Subtitle.
        :rtype: list[MulInputFileInfo]
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        """Sets the inputs of this Subtitle.

        多字幕文件地址。 

        :param inputs: The inputs of this Subtitle.
        :type: list[MulInputFileInfo]
        """
        self._inputs = inputs

    @property
    def subtitle_type(self):
        """Gets the subtitle_type of this Subtitle.

        字幕类型 

        :return: The subtitle_type of this Subtitle.
        :rtype: int
        """
        return self._subtitle_type

    @subtitle_type.setter
    def subtitle_type(self, subtitle_type):
        """Sets the subtitle_type of this Subtitle.

        字幕类型 

        :param subtitle_type: The subtitle_type of this Subtitle.
        :type: int
        """
        self._subtitle_type = subtitle_type

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
        if not isinstance(other, Subtitle):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
