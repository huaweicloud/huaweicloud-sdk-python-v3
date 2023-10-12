# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FileRedirectionOptionsLinuxFileSizeSupportedOptions:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'linux_file_size_supported_threshold': 'int'
    }

    attribute_map = {
        'linux_file_size_supported_threshold': 'linux_file_size_supported_threshold'
    }

    def __init__(self, linux_file_size_supported_threshold=None):
        """FileRedirectionOptionsLinuxFileSizeSupportedOptions

        The model defined in huaweicloud sdk

        :param linux_file_size_supported_threshold: Linux设置文件大小阈值（Byte）。取值范围为[0-4096]。默认：100。
        :type linux_file_size_supported_threshold: int
        """
        
        

        self._linux_file_size_supported_threshold = None
        self.discriminator = None

        if linux_file_size_supported_threshold is not None:
            self.linux_file_size_supported_threshold = linux_file_size_supported_threshold

    @property
    def linux_file_size_supported_threshold(self):
        """Gets the linux_file_size_supported_threshold of this FileRedirectionOptionsLinuxFileSizeSupportedOptions.

        Linux设置文件大小阈值（Byte）。取值范围为[0-4096]。默认：100。

        :return: The linux_file_size_supported_threshold of this FileRedirectionOptionsLinuxFileSizeSupportedOptions.
        :rtype: int
        """
        return self._linux_file_size_supported_threshold

    @linux_file_size_supported_threshold.setter
    def linux_file_size_supported_threshold(self, linux_file_size_supported_threshold):
        """Sets the linux_file_size_supported_threshold of this FileRedirectionOptionsLinuxFileSizeSupportedOptions.

        Linux设置文件大小阈值（Byte）。取值范围为[0-4096]。默认：100。

        :param linux_file_size_supported_threshold: The linux_file_size_supported_threshold of this FileRedirectionOptionsLinuxFileSizeSupportedOptions.
        :type linux_file_size_supported_threshold: int
        """
        self._linux_file_size_supported_threshold = linux_file_size_supported_threshold

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
        if not isinstance(other, FileRedirectionOptionsLinuxFileSizeSupportedOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
