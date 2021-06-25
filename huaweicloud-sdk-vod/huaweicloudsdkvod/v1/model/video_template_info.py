# coding: utf-8

import pprint
import re

import six





class VideoTemplateInfo:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'quality': 'str',
        'width': 'int',
        'height': 'int',
        'bitrate': 'int',
        'frame_rate': 'int'
    }

    attribute_map = {
        'quality': 'quality',
        'width': 'width',
        'height': 'height',
        'bitrate': 'bitrate',
        'frame_rate': 'frame_rate'
    }

    def __init__(self, quality=None, width=None, height=None, bitrate=None, frame_rate=None):
        """VideoTemplateInfo - a model defined in huaweicloud sdk"""
        
        

        self._quality = None
        self._width = None
        self._height = None
        self._bitrate = None
        self._frame_rate = None
        self.discriminator = None

        self.quality = quality
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if bitrate is not None:
            self.bitrate = bitrate
        if frame_rate is not None:
            self.frame_rate = frame_rate

    @property
    def quality(self):
        """Gets the quality of this VideoTemplateInfo.

        画质<br/> 

        :return: The quality of this VideoTemplateInfo.
        :rtype: str
        """
        return self._quality

    @quality.setter
    def quality(self, quality):
        """Sets the quality of this VideoTemplateInfo.

        画质<br/> 

        :param quality: The quality of this VideoTemplateInfo.
        :type: str
        """
        self._quality = quality

    @property
    def width(self):
        """Gets the width of this VideoTemplateInfo.

        视频宽度<br/> 

        :return: The width of this VideoTemplateInfo.
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this VideoTemplateInfo.

        视频宽度<br/> 

        :param width: The width of this VideoTemplateInfo.
        :type: int
        """
        self._width = width

    @property
    def height(self):
        """Gets the height of this VideoTemplateInfo.

        视频高度<br/> 

        :return: The height of this VideoTemplateInfo.
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this VideoTemplateInfo.

        视频高度<br/> 

        :param height: The height of this VideoTemplateInfo.
        :type: int
        """
        self._height = height

    @property
    def bitrate(self):
        """Gets the bitrate of this VideoTemplateInfo.

        码率<br/> 

        :return: The bitrate of this VideoTemplateInfo.
        :rtype: int
        """
        return self._bitrate

    @bitrate.setter
    def bitrate(self, bitrate):
        """Sets the bitrate of this VideoTemplateInfo.

        码率<br/> 

        :param bitrate: The bitrate of this VideoTemplateInfo.
        :type: int
        """
        self._bitrate = bitrate

    @property
    def frame_rate(self):
        """Gets the frame_rate of this VideoTemplateInfo.

        帧率（默认为1，1代表自适应，单位是帧每秒）<br/> 

        :return: The frame_rate of this VideoTemplateInfo.
        :rtype: int
        """
        return self._frame_rate

    @frame_rate.setter
    def frame_rate(self, frame_rate):
        """Sets the frame_rate of this VideoTemplateInfo.

        帧率（默认为1，1代表自适应，单位是帧每秒）<br/> 

        :param frame_rate: The frame_rate of this VideoTemplateInfo.
        :type: int
        """
        self._frame_rate = frame_rate

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
        if not isinstance(other, VideoTemplateInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other