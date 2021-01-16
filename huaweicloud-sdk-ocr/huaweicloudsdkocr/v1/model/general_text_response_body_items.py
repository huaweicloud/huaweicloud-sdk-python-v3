# coding: utf-8

import pprint
import re

import six





class GeneralTextResponseBodyItems:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'direction': 'int',
        'words_block_count': 'int',
        'words_block_list': 'list[GeneralTextWordsBlockList]'
    }

    attribute_map = {
        'direction': 'direction',
        'words_block_count': 'words_block_count',
        'words_block_list': 'words_block_list'
    }

    def __init__(self, direction=None, words_block_count=None, words_block_list=None):
        """GeneralTextResponseBodyItems - a model defined in huaweicloud sdk"""
        
        

        self._direction = None
        self._words_block_count = None
        self._words_block_list = None
        self.discriminator = None

        self.direction = direction
        self.words_block_count = words_block_count
        self.words_block_list = words_block_list

    @property
    def direction(self):
        """Gets the direction of this GeneralTextResponseBodyItems.

        图片朝向，仅当detect_direction为true时，该字段有效。返回图片逆时针旋转角度，值区间为[0， 359]。当detect_direction为false时，该字段值为 -1。 

        :return: The direction of this GeneralTextResponseBodyItems.
        :rtype: int
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """Sets the direction of this GeneralTextResponseBodyItems.

        图片朝向，仅当detect_direction为true时，该字段有效。返回图片逆时针旋转角度，值区间为[0， 359]。当detect_direction为false时，该字段值为 -1。 

        :param direction: The direction of this GeneralTextResponseBodyItems.
        :type: int
        """
        self._direction = direction

    @property
    def words_block_count(self):
        """Gets the words_block_count of this GeneralTextResponseBodyItems.

        识别文字块数目。 

        :return: The words_block_count of this GeneralTextResponseBodyItems.
        :rtype: int
        """
        return self._words_block_count

    @words_block_count.setter
    def words_block_count(self, words_block_count):
        """Sets the words_block_count of this GeneralTextResponseBodyItems.

        识别文字块数目。 

        :param words_block_count: The words_block_count of this GeneralTextResponseBodyItems.
        :type: int
        """
        self._words_block_count = words_block_count

    @property
    def words_block_list(self):
        """Gets the words_block_list of this GeneralTextResponseBodyItems.

        识别文字块列表，输出顺序从左到右，先上后下。 

        :return: The words_block_list of this GeneralTextResponseBodyItems.
        :rtype: list[GeneralTextWordsBlockList]
        """
        return self._words_block_list

    @words_block_list.setter
    def words_block_list(self, words_block_list):
        """Sets the words_block_list of this GeneralTextResponseBodyItems.

        识别文字块列表，输出顺序从左到右，先上后下。 

        :param words_block_list: The words_block_list of this GeneralTextResponseBodyItems.
        :type: list[GeneralTextWordsBlockList]
        """
        self._words_block_list = words_block_list

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
        if not isinstance(other, GeneralTextResponseBodyItems):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
