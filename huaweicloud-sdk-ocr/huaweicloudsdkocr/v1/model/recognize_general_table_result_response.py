# coding: utf-8

import pprint
import re

import six





class RecognizeGeneralTableResultResponse:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'words_region_count': 'int',
        'words_region_list': 'list[WordsRegionList]'
    }

    attribute_map = {
        'words_region_count': 'words_region_count',
        'words_region_list': 'words_region_list'
    }

    def __init__(self, words_region_count=None, words_region_list=None):
        """RecognizeGeneralTableResultResponse - a model defined in huaweicloud sdk"""
        
        

        self._words_region_count = None
        self._words_region_list = None
        self.discriminator = None

        self.words_region_count = words_region_count
        self.words_region_list = words_region_list

    @property
    def words_region_count(self):
        """Gets the words_region_count of this RecognizeGeneralTableResultResponse.

        文字区域数目。          

        :return: The words_region_count of this RecognizeGeneralTableResultResponse.
        :rtype: int
        """
        return self._words_region_count

    @words_region_count.setter
    def words_region_count(self, words_region_count):
        """Sets the words_region_count of this RecognizeGeneralTableResultResponse.

        文字区域数目。          

        :param words_region_count: The words_region_count of this RecognizeGeneralTableResultResponse.
        :type: int
        """
        self._words_region_count = words_region_count

    @property
    def words_region_list(self):
        """Gets the words_region_list of this RecognizeGeneralTableResultResponse.

        文字区域识别结果列表，输出顺序从左到右，先上后下。 

        :return: The words_region_list of this RecognizeGeneralTableResultResponse.
        :rtype: list[WordsRegionList]
        """
        return self._words_region_list

    @words_region_list.setter
    def words_region_list(self, words_region_list):
        """Sets the words_region_list of this RecognizeGeneralTableResultResponse.

        文字区域识别结果列表，输出顺序从左到右，先上后下。 

        :param words_region_list: The words_region_list of this RecognizeGeneralTableResultResponse.
        :type: list[WordsRegionList]
        """
        self._words_region_list = words_region_list

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
        if not isinstance(other, RecognizeGeneralTableResultResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
