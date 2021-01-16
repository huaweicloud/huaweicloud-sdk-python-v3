# coding: utf-8

import pprint
import re

import six





class WebImageResponseBodyItem:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'words_block_count': 'int',
        'words_block_list': 'list[WebImageWordsBlockList]'
    }

    attribute_map = {
        'words_block_count': 'words_block_count',
        'words_block_list': 'words_block_list'
    }

    def __init__(self, words_block_count=None, words_block_list=None):
        """WebImageResponseBodyItem - a model defined in huaweicloud sdk"""
        
        

        self._words_block_count = None
        self._words_block_list = None
        self.discriminator = None

        self.words_block_count = words_block_count
        self.words_block_list = words_block_list

    @property
    def words_block_count(self):
        """Gets the words_block_count of this WebImageResponseBodyItem.

        代表检测识别出来的文字块数目。 

        :return: The words_block_count of this WebImageResponseBodyItem.
        :rtype: int
        """
        return self._words_block_count

    @words_block_count.setter
    def words_block_count(self, words_block_count):
        """Sets the words_block_count of this WebImageResponseBodyItem.

        代表检测识别出来的文字块数目。 

        :param words_block_count: The words_block_count of this WebImageResponseBodyItem.
        :type: int
        """
        self._words_block_count = words_block_count

    @property
    def words_block_list(self):
        """Gets the words_block_list of this WebImageResponseBodyItem.

        识别文字块列表，输出顺序从左到右，从上到下。 

        :return: The words_block_list of this WebImageResponseBodyItem.
        :rtype: list[WebImageWordsBlockList]
        """
        return self._words_block_list

    @words_block_list.setter
    def words_block_list(self, words_block_list):
        """Sets the words_block_list of this WebImageResponseBodyItem.

        识别文字块列表，输出顺序从左到右，从上到下。 

        :param words_block_list: The words_block_list of this WebImageResponseBodyItem.
        :type: list[WebImageWordsBlockList]
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
        if not isinstance(other, WebImageResponseBodyItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
