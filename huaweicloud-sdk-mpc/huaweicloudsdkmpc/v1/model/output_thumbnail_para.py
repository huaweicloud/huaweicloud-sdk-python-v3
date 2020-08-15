# coding: utf-8

import pprint
import re

import six





class OutputThumbnailPara:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'total_pictures': 'int',
        'width': 'int',
        'height': 'int',
        'file_name': 'str',
        'output': 'ObsObjInfo'
    }

    attribute_map = {
        'total_pictures': 'total_pictures',
        'width': 'width',
        'height': 'height',
        'file_name': 'file_name',
        'output': 'output'
    }

    def __init__(self, total_pictures=None, width=None, height=None, file_name=None, output=None):
        """OutputThumbnailPara - a model defined in huaweicloud sdk"""
        
        

        self._total_pictures = None
        self._width = None
        self._height = None
        self._file_name = None
        self._output = None
        self.discriminator = None

        if total_pictures is not None:
            self.total_pictures = total_pictures
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if file_name is not None:
            self.file_name = file_name
        if output is not None:
            self.output = output

    @property
    def total_pictures(self):
        """Gets the total_pictures of this OutputThumbnailPara.

        抽帧图片张数 

        :return: The total_pictures of this OutputThumbnailPara.
        :rtype: int
        """
        return self._total_pictures

    @total_pictures.setter
    def total_pictures(self, total_pictures):
        """Sets the total_pictures of this OutputThumbnailPara.

        抽帧图片张数 

        :param total_pictures: The total_pictures of this OutputThumbnailPara.
        :type: int
        """
        self._total_pictures = total_pictures

    @property
    def width(self):
        """Gets the width of this OutputThumbnailPara.

        抽帧图片宽度 

        :return: The width of this OutputThumbnailPara.
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this OutputThumbnailPara.

        抽帧图片宽度 

        :param width: The width of this OutputThumbnailPara.
        :type: int
        """
        self._width = width

    @property
    def height(self):
        """Gets the height of this OutputThumbnailPara.

        抽帧图片高度 

        :return: The height of this OutputThumbnailPara.
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this OutputThumbnailPara.

        抽帧图片高度 

        :param height: The height of this OutputThumbnailPara.
        :type: int
        """
        self._height = height

    @property
    def file_name(self):
        """Gets the file_name of this OutputThumbnailPara.

        抽帧文件名 

        :return: The file_name of this OutputThumbnailPara.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this OutputThumbnailPara.

        抽帧文件名 

        :param file_name: The file_name of this OutputThumbnailPara.
        :type: str
        """
        self._file_name = file_name

    @property
    def output(self):
        """Gets the output of this OutputThumbnailPara.


        :return: The output of this OutputThumbnailPara.
        :rtype: ObsObjInfo
        """
        return self._output

    @output.setter
    def output(self, output):
        """Sets the output of this OutputThumbnailPara.


        :param output: The output of this OutputThumbnailPara.
        :type: ObsObjInfo
        """
        self._output = output

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
        if not isinstance(other, OutputThumbnailPara):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
