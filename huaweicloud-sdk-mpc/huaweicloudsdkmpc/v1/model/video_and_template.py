# coding: utf-8

import pprint
import re

import six





class VideoAndTemplate:


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
        'width': 'int',
        'height': 'int',
        'bitrate': 'int'
    }

    attribute_map = {
        'template_id': 'template_id',
        'width': 'width',
        'height': 'height',
        'bitrate': 'bitrate'
    }

    def __init__(self, template_id=None, width=None, height=None, bitrate=None):
        """VideoAndTemplate - a model defined in huaweicloud sdk"""
        
        

        self._template_id = None
        self._width = None
        self._height = None
        self._bitrate = None
        self.discriminator = None

        if template_id is not None:
            self.template_id = template_id
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if bitrate is not None:
            self.bitrate = bitrate

    @property
    def template_id(self):
        """Gets the template_id of this VideoAndTemplate.

        模板ID 

        :return: The template_id of this VideoAndTemplate.
        :rtype: int
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """Sets the template_id of this VideoAndTemplate.

        模板ID 

        :param template_id: The template_id of this VideoAndTemplate.
        :type: int
        """
        self._template_id = template_id

    @property
    def width(self):
        """Gets the width of this VideoAndTemplate.

        视频宽度（单位：像素） - H264：范围[32,4096]，必须为2的倍数 - H265：范围[320,4096]，必须是4的倍数 

        :return: The width of this VideoAndTemplate.
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this VideoAndTemplate.

        视频宽度（单位：像素） - H264：范围[32,4096]，必须为2的倍数 - H265：范围[320,4096]，必须是4的倍数 

        :param width: The width of this VideoAndTemplate.
        :type: int
        """
        self._width = width

    @property
    def height(self):
        """Gets the height of this VideoAndTemplate.

        视频高度（单位：像素） - H264：范围[32,2880]，必须为2的倍数 - H265：范围[240,2880]，必须是4的倍数 

        :return: The height of this VideoAndTemplate.
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this VideoAndTemplate.

        视频高度（单位：像素） - H264：范围[32,2880]，必须为2的倍数 - H265：范围[240,2880]，必须是4的倍数 

        :param height: The height of this VideoAndTemplate.
        :type: int
        """
        self._height = height

    @property
    def bitrate(self):
        """Gets the bitrate of this VideoAndTemplate.

        输出平均码率。  取值范围：0或[40,30000]之间的整数。  单位：kbit/s  若设置为0，则输出平均码率为自适应值。 

        :return: The bitrate of this VideoAndTemplate.
        :rtype: int
        """
        return self._bitrate

    @bitrate.setter
    def bitrate(self, bitrate):
        """Sets the bitrate of this VideoAndTemplate.

        输出平均码率。  取值范围：0或[40,30000]之间的整数。  单位：kbit/s  若设置为0，则输出平均码率为自适应值。 

        :param bitrate: The bitrate of this VideoAndTemplate.
        :type: int
        """
        self._bitrate = bitrate

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
        if not isinstance(other, VideoAndTemplate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
