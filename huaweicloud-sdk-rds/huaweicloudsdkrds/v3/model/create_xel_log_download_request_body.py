# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateXelLogDownloadRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'file_name': 'str'
    }

    attribute_map = {
        'file_name': 'file_name'
    }

    def __init__(self, file_name=None):
        """CreateXelLogDownloadRequestBody

        The model defined in huaweicloud sdk

        :param file_name: 文件名。取值范围：不为null和空字符串，只为大小写字母，数字和下划线，以“.xel”结尾
        :type file_name: str
        """
        
        

        self._file_name = None
        self.discriminator = None

        self.file_name = file_name

    @property
    def file_name(self):
        """Gets the file_name of this CreateXelLogDownloadRequestBody.

        文件名。取值范围：不为null和空字符串，只为大小写字母，数字和下划线，以“.xel”结尾

        :return: The file_name of this CreateXelLogDownloadRequestBody.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this CreateXelLogDownloadRequestBody.

        文件名。取值范围：不为null和空字符串，只为大小写字母，数字和下划线，以“.xel”结尾

        :param file_name: The file_name of this CreateXelLogDownloadRequestBody.
        :type file_name: str
        """
        self._file_name = file_name

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
        if not isinstance(other, CreateXelLogDownloadRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
