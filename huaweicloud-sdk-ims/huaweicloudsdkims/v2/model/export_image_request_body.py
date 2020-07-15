# coding: utf-8

import pprint
import re

import six





class ExportImageRequestBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'bucket_url': 'str',
        'file_format': 'str'
    }

    attribute_map = {
        'bucket_url': 'bucket_url',
        'file_format': 'file_format'
    }

    def __init__(self, bucket_url=None, file_format=None):
        """ExportImageRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._bucket_url = None
        self._file_format = None
        self.discriminator = None

        self.bucket_url = bucket_url
        self.file_format = file_format

    @property
    def bucket_url(self):
        """Gets the bucket_url of this ExportImageRequestBody.

        目的文件的URL，格式：<bucket>:<file>。 说明：此处的OBS桶和镜像文件的存储类别必须是OBS标准存储。

        :return: The bucket_url of this ExportImageRequestBody.
        :rtype: str
        """
        return self._bucket_url

    @bucket_url.setter
    def bucket_url(self, bucket_url):
        """Sets the bucket_url of this ExportImageRequestBody.

        目的文件的URL，格式：<bucket>:<file>。 说明：此处的OBS桶和镜像文件的存储类别必须是OBS标准存储。

        :param bucket_url: The bucket_url of this ExportImageRequestBody.
        :type: str
        """
        self._bucket_url = bucket_url

    @property
    def file_format(self):
        """Gets the file_format of this ExportImageRequestBody.

        文件格式，支持qcow2、vhd、zvhd和vmdk。

        :return: The file_format of this ExportImageRequestBody.
        :rtype: str
        """
        return self._file_format

    @file_format.setter
    def file_format(self, file_format):
        """Sets the file_format of this ExportImageRequestBody.

        文件格式，支持qcow2、vhd、zvhd和vmdk。

        :param file_format: The file_format of this ExportImageRequestBody.
        :type: str
        """
        self._file_format = file_format

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
        if not isinstance(other, ExportImageRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
