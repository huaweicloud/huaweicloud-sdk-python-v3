# coding: utf-8

import pprint
import re

import six





class UploadFileRequestBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'file': 'file'
    }

    attribute_map = {
        'file': 'file'
    }

    def __init__(self, file=None):
        """UploadFileRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._file = None
        self.discriminator = None

        self.file = file

    @property
    def file(self):
        """Gets the file of this UploadFileRequestBody.

        需要上传的文件

        :return: The file of this UploadFileRequestBody.
        :rtype: file
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this UploadFileRequestBody.

        需要上传的文件

        :param file: The file of this UploadFileRequestBody.
        :type: file
        """
        self._file = file

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
        if not isinstance(other, UploadFileRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other