# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FileRedirectionOptionsCompressionSwitchOptions:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'compression_threshold': 'int',
        'minimum_compression_rate': 'int'
    }

    attribute_map = {
        'compression_threshold': 'compression_threshold',
        'minimum_compression_rate': 'minimum_compression_rate'
    }

    def __init__(self, compression_threshold=None, minimum_compression_rate=None):
        """FileRedirectionOptionsCompressionSwitchOptions

        The model defined in huaweicloud sdk

        :param compression_threshold: 压缩阈值（Byte）。取值范围为[0-10240]。默认：512。
        :type compression_threshold: int
        :param minimum_compression_rate: 最小压缩率。取值范围为[0-1000]。默认：900。
        :type minimum_compression_rate: int
        """
        
        

        self._compression_threshold = None
        self._minimum_compression_rate = None
        self.discriminator = None

        if compression_threshold is not None:
            self.compression_threshold = compression_threshold
        if minimum_compression_rate is not None:
            self.minimum_compression_rate = minimum_compression_rate

    @property
    def compression_threshold(self):
        """Gets the compression_threshold of this FileRedirectionOptionsCompressionSwitchOptions.

        压缩阈值（Byte）。取值范围为[0-10240]。默认：512。

        :return: The compression_threshold of this FileRedirectionOptionsCompressionSwitchOptions.
        :rtype: int
        """
        return self._compression_threshold

    @compression_threshold.setter
    def compression_threshold(self, compression_threshold):
        """Sets the compression_threshold of this FileRedirectionOptionsCompressionSwitchOptions.

        压缩阈值（Byte）。取值范围为[0-10240]。默认：512。

        :param compression_threshold: The compression_threshold of this FileRedirectionOptionsCompressionSwitchOptions.
        :type compression_threshold: int
        """
        self._compression_threshold = compression_threshold

    @property
    def minimum_compression_rate(self):
        """Gets the minimum_compression_rate of this FileRedirectionOptionsCompressionSwitchOptions.

        最小压缩率。取值范围为[0-1000]。默认：900。

        :return: The minimum_compression_rate of this FileRedirectionOptionsCompressionSwitchOptions.
        :rtype: int
        """
        return self._minimum_compression_rate

    @minimum_compression_rate.setter
    def minimum_compression_rate(self, minimum_compression_rate):
        """Sets the minimum_compression_rate of this FileRedirectionOptionsCompressionSwitchOptions.

        最小压缩率。取值范围为[0-1000]。默认：900。

        :param minimum_compression_rate: The minimum_compression_rate of this FileRedirectionOptionsCompressionSwitchOptions.
        :type minimum_compression_rate: int
        """
        self._minimum_compression_rate = minimum_compression_rate

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
        if not isinstance(other, FileRedirectionOptionsCompressionSwitchOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
