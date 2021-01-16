# coding: utf-8

import pprint
import re

import six





class MathInfo:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'question_number': 'str',
        'answer_block_count': 'int',
        'answer_block_list': 'list[AnswerBlockList]'
    }

    attribute_map = {
        'question_number': 'question_number',
        'answer_block_count': 'answer_block_count',
        'answer_block_list': 'answer_block_list'
    }

    def __init__(self, question_number=None, answer_block_count=None, answer_block_list=None):
        """MathInfo - a model defined in huaweicloud sdk"""
        
        

        self._question_number = None
        self._answer_block_count = None
        self._answer_block_list = None
        self.discriminator = None

        if question_number is not None:
            self.question_number = question_number
        if answer_block_count is not None:
            self.answer_block_count = answer_block_count
        if answer_block_list is not None:
            self.answer_block_list = answer_block_list

    @property
    def question_number(self):
        """Gets the question_number of this MathInfo.

        数学试卷返回结果，表示题号。 

        :return: The question_number of this MathInfo.
        :rtype: str
        """
        return self._question_number

    @question_number.setter
    def question_number(self, question_number):
        """Sets the question_number of this MathInfo.

        数学试卷返回结果，表示题号。 

        :param question_number: The question_number of this MathInfo.
        :type: str
        """
        self._question_number = question_number

    @property
    def answer_block_count(self):
        """Gets the answer_block_count of this MathInfo.

        数学试卷答案的文字块数目。 

        :return: The answer_block_count of this MathInfo.
        :rtype: int
        """
        return self._answer_block_count

    @answer_block_count.setter
    def answer_block_count(self, answer_block_count):
        """Sets the answer_block_count of this MathInfo.

        数学试卷答案的文字块数目。 

        :param answer_block_count: The answer_block_count of this MathInfo.
        :type: int
        """
        self._answer_block_count = answer_block_count

    @property
    def answer_block_list(self):
        """Gets the answer_block_list of this MathInfo.

        数学试卷答案识别文字块列表，输出顺序从左到右，从上到下。 

        :return: The answer_block_list of this MathInfo.
        :rtype: list[AnswerBlockList]
        """
        return self._answer_block_list

    @answer_block_list.setter
    def answer_block_list(self, answer_block_list):
        """Sets the answer_block_list of this MathInfo.

        数学试卷答案识别文字块列表，输出顺序从左到右，从上到下。 

        :param answer_block_list: The answer_block_list of this MathInfo.
        :type: list[AnswerBlockList]
        """
        self._answer_block_list = answer_block_list

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
        if not isinstance(other, MathInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
