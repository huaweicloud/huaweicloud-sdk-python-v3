# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ScanProtectionOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'high_frequency_scan_blocking_config': 'HighFrequencyScanBlockingConfig',
        'directory_traversal_protection_config': 'DirectoryTraversalProtectionConfig'
    }

    attribute_map = {
        'high_frequency_scan_blocking_config': 'high_frequency_scan_blocking_config',
        'directory_traversal_protection_config': 'directory_traversal_protection_config'
    }

    def __init__(self, high_frequency_scan_blocking_config=None, directory_traversal_protection_config=None):
        r"""ScanProtectionOption

        The model defined in huaweicloud sdk

        :param high_frequency_scan_blocking_config: 
        :type high_frequency_scan_blocking_config: :class:`huaweicloudsdkwaf.v1.HighFrequencyScanBlockingConfig`
        :param directory_traversal_protection_config: 
        :type directory_traversal_protection_config: :class:`huaweicloudsdkwaf.v1.DirectoryTraversalProtectionConfig`
        """
        
        

        self._high_frequency_scan_blocking_config = None
        self._directory_traversal_protection_config = None
        self.discriminator = None

        if high_frequency_scan_blocking_config is not None:
            self.high_frequency_scan_blocking_config = high_frequency_scan_blocking_config
        if directory_traversal_protection_config is not None:
            self.directory_traversal_protection_config = directory_traversal_protection_config

    @property
    def high_frequency_scan_blocking_config(self):
        r"""Gets the high_frequency_scan_blocking_config of this ScanProtectionOption.

        :return: The high_frequency_scan_blocking_config of this ScanProtectionOption.
        :rtype: :class:`huaweicloudsdkwaf.v1.HighFrequencyScanBlockingConfig`
        """
        return self._high_frequency_scan_blocking_config

    @high_frequency_scan_blocking_config.setter
    def high_frequency_scan_blocking_config(self, high_frequency_scan_blocking_config):
        r"""Sets the high_frequency_scan_blocking_config of this ScanProtectionOption.

        :param high_frequency_scan_blocking_config: The high_frequency_scan_blocking_config of this ScanProtectionOption.
        :type high_frequency_scan_blocking_config: :class:`huaweicloudsdkwaf.v1.HighFrequencyScanBlockingConfig`
        """
        self._high_frequency_scan_blocking_config = high_frequency_scan_blocking_config

    @property
    def directory_traversal_protection_config(self):
        r"""Gets the directory_traversal_protection_config of this ScanProtectionOption.

        :return: The directory_traversal_protection_config of this ScanProtectionOption.
        :rtype: :class:`huaweicloudsdkwaf.v1.DirectoryTraversalProtectionConfig`
        """
        return self._directory_traversal_protection_config

    @directory_traversal_protection_config.setter
    def directory_traversal_protection_config(self, directory_traversal_protection_config):
        r"""Sets the directory_traversal_protection_config of this ScanProtectionOption.

        :param directory_traversal_protection_config: The directory_traversal_protection_config of this ScanProtectionOption.
        :type directory_traversal_protection_config: :class:`huaweicloudsdkwaf.v1.DirectoryTraversalProtectionConfig`
        """
        self._directory_traversal_protection_config = directory_traversal_protection_config

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ScanProtectionOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
