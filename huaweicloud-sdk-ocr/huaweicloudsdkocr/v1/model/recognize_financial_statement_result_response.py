# coding: utf-8

import pprint
import re

import six





class RecognizeFinancialStatementResultResponse:


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
        'words_region_list': 'list[RecognizeFinancialStatementWordsRegionItemsResponse]',
        'image_size': 'object'
    }

    attribute_map = {
        'words_region_count': 'words_region_count',
        'words_region_list': 'words_region_list',
        'image_size': 'image_size'
    }

    def __init__(self, words_region_count=None, words_region_list=None, image_size=None):
        """RecognizeFinancialStatementResultResponse - a model defined in huaweicloud sdk"""
        
        

        self._words_region_count = None
        self._words_region_list = None
        self._image_size = None
        self.discriminator = None

        self.words_region_count = words_region_count
        self.words_region_list = words_region_list
        self.image_size = image_size

    @property
    def words_region_count(self):
        """Gets the words_region_count of this RecognizeFinancialStatementResultResponse.

        识别出来的表格、文本区域个数。 

        :return: The words_region_count of this RecognizeFinancialStatementResultResponse.
        :rtype: int
        """
        return self._words_region_count

    @words_region_count.setter
    def words_region_count(self, words_region_count):
        """Sets the words_region_count of this RecognizeFinancialStatementResultResponse.

        识别出来的表格、文本区域个数。 

        :param words_region_count: The words_region_count of this RecognizeFinancialStatementResultResponse.
        :type: int
        """
        self._words_region_count = words_region_count

    @property
    def words_region_list(self):
        """Gets the words_region_list of this RecognizeFinancialStatementResultResponse.

        返回的表格、文本区域列表。输出顺序从左到右，从上到下。 

        :return: The words_region_list of this RecognizeFinancialStatementResultResponse.
        :rtype: list[RecognizeFinancialStatementWordsRegionItemsResponse]
        """
        return self._words_region_list

    @words_region_list.setter
    def words_region_list(self, words_region_list):
        """Sets the words_region_list of this RecognizeFinancialStatementResultResponse.

        返回的表格、文本区域列表。输出顺序从左到右，从上到下。 

        :param words_region_list: The words_region_list of this RecognizeFinancialStatementResultResponse.
        :type: list[RecognizeFinancialStatementWordsRegionItemsResponse]
        """
        self._words_region_list = words_region_list

    @property
    def image_size(self):
        """Gets the image_size of this RecognizeFinancialStatementResultResponse.

        服务对倾斜、透视等输入图片自动矫正，该字段表示矫正后的图片大小，字典格式。 

        :return: The image_size of this RecognizeFinancialStatementResultResponse.
        :rtype: object
        """
        return self._image_size

    @image_size.setter
    def image_size(self, image_size):
        """Sets the image_size of this RecognizeFinancialStatementResultResponse.

        服务对倾斜、透视等输入图片自动矫正，该字段表示矫正后的图片大小，字典格式。 

        :param image_size: The image_size of this RecognizeFinancialStatementResultResponse.
        :type: object
        """
        self._image_size = image_size

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
        if not isinstance(other, RecognizeFinancialStatementResultResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
