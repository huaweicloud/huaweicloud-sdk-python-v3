# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HandwritingResult:


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
        'words_block_list': 'list[HandwritingWordsBlockList]',
        'extracted_data': 'ExtractedData'
    }

    attribute_map = {
        'words_block_count': 'words_block_count',
        'words_block_list': 'words_block_list',
        'extracted_data': 'extracted_data'
    }

    def __init__(self, words_block_count=None, words_block_list=None, extracted_data=None):
        """HandwritingResult - a model defined in huaweicloud sdk"""
        
        

        self._words_block_count = None
        self._words_block_list = None
        self._extracted_data = None
        self.discriminator = None

        self.words_block_count = words_block_count
        self.words_block_list = words_block_list
        if extracted_data is not None:
            self.extracted_data = extracted_data

    @property
    def words_block_count(self):
        """Gets the words_block_count of this HandwritingResult.

        代表检测识别出来的文字块数目。 \"segment_digit\" 和\"segment\"默认为1。       

        :return: The words_block_count of this HandwritingResult.
        :rtype: int
        """
        return self._words_block_count

    @words_block_count.setter
    def words_block_count(self, words_block_count):
        """Sets the words_block_count of this HandwritingResult.

        代表检测识别出来的文字块数目。 \"segment_digit\" 和\"segment\"默认为1。       

        :param words_block_count: The words_block_count of this HandwritingResult.
        :type: int
        """
        self._words_block_count = words_block_count

    @property
    def words_block_list(self):
        """Gets the words_block_list of this HandwritingResult.

        识别文字块列表，输出顺序从左到右，从上到下。 

        :return: The words_block_list of this HandwritingResult.
        :rtype: list[HandwritingWordsBlockList]
        """
        return self._words_block_list

    @words_block_list.setter
    def words_block_list(self, words_block_list):
        """Sets the words_block_list of this HandwritingResult.

        识别文字块列表，输出顺序从左到右，从上到下。 

        :param words_block_list: The words_block_list of this HandwritingResult.
        :type: list[HandwritingWordsBlockList]
        """
        self._words_block_list = words_block_list

    @property
    def extracted_data(self):
        """Gets the extracted_data of this HandwritingResult.


        :return: The extracted_data of this HandwritingResult.
        :rtype: ExtractedData
        """
        return self._extracted_data

    @extracted_data.setter
    def extracted_data(self, extracted_data):
        """Sets the extracted_data of this HandwritingResult.


        :param extracted_data: The extracted_data of this HandwritingResult.
        :type: ExtractedData
        """
        self._extracted_data = extracted_data

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
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, HandwritingResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
