# coding: utf-8

import pprint
import re

import six





class TranscodeDetail:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'multitask_info': 'list[MultiTaskInfo]',
        'input_file': 'SourceInfo'
    }

    attribute_map = {
        'multitask_info': 'multitask_info',
        'input_file': 'input_file'
    }

    def __init__(self, multitask_info=None, input_file=None):
        """TranscodeDetail - a model defined in huaweicloud sdk"""
        
        

        self._multitask_info = None
        self._input_file = None
        self.discriminator = None

        if multitask_info is not None:
            self.multitask_info = multitask_info
        if input_file is not None:
            self.input_file = input_file

    @property
    def multitask_info(self):
        """Gets the multitask_info of this TranscodeDetail.

        一进多出情况下部分转码失败的情况。 

        :return: The multitask_info of this TranscodeDetail.
        :rtype: list[MultiTaskInfo]
        """
        return self._multitask_info

    @multitask_info.setter
    def multitask_info(self, multitask_info):
        """Sets the multitask_info of this TranscodeDetail.

        一进多出情况下部分转码失败的情况。 

        :param multitask_info: The multitask_info of this TranscodeDetail.
        :type: list[MultiTaskInfo]
        """
        self._multitask_info = multitask_info

    @property
    def input_file(self):
        """Gets the input_file of this TranscodeDetail.


        :return: The input_file of this TranscodeDetail.
        :rtype: SourceInfo
        """
        return self._input_file

    @input_file.setter
    def input_file(self, input_file):
        """Sets the input_file of this TranscodeDetail.


        :param input_file: The input_file of this TranscodeDetail.
        :type: SourceInfo
        """
        self._input_file = input_file

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
        if not isinstance(other, TranscodeDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
