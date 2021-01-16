# coding: utf-8

import pprint
import re

import six





class GeneralTextWordsBlockList:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'words': 'str',
        'location': 'list[int]'
    }

    attribute_map = {
        'words': 'words',
        'location': 'location'
    }

    def __init__(self, words=None, location=None):
        """GeneralTextWordsBlockList - a model defined in huaweicloud sdk"""
        
        

        self._words = None
        self._location = None
        self.discriminator = None

        self.words = words
        self.location = location

    @property
    def words(self):
        """Gets the words of this GeneralTextWordsBlockList.

        文字块识别结果。 

        :return: The words of this GeneralTextWordsBlockList.
        :rtype: str
        """
        return self._words

    @words.setter
    def words(self, words):
        """Sets the words of this GeneralTextWordsBlockList.

        文字块识别结果。 

        :param words: The words of this GeneralTextWordsBlockList.
        :type: str
        """
        self._words = words

    @property
    def location(self):
        """Gets the location of this GeneralTextWordsBlockList.

        文字块的区域位置信息，列表形式，包含文字区域四个顶点的二维坐标（x,y）;坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 

        :return: The location of this GeneralTextWordsBlockList.
        :rtype: list[int]
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this GeneralTextWordsBlockList.

        文字块的区域位置信息，列表形式，包含文字区域四个顶点的二维坐标（x,y）;坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 

        :param location: The location of this GeneralTextWordsBlockList.
        :type: list[int]
        """
        self._location = location

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
        if not isinstance(other, GeneralTextWordsBlockList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
