# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SupportedDevice:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vendor': 'str',
        'platform': 'str',
        'version': 'str'
    }

    attribute_map = {
        'vendor': 'vendor',
        'platform': 'platform',
        'version': 'version'
    }

    def __init__(self, vendor=None, platform=None, version=None):
        r"""SupportedDevice

        The model defined in huaweicloud sdk

        :param vendor: 厂商
        :type vendor: str
        :param platform: 型号
        :type platform: str
        :param version: 版本
        :type version: str
        """
        
        

        self._vendor = None
        self._platform = None
        self._version = None
        self.discriminator = None

        if vendor is not None:
            self.vendor = vendor
        if platform is not None:
            self.platform = platform
        if version is not None:
            self.version = version

    @property
    def vendor(self):
        r"""Gets the vendor of this SupportedDevice.

        厂商

        :return: The vendor of this SupportedDevice.
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        r"""Sets the vendor of this SupportedDevice.

        厂商

        :param vendor: The vendor of this SupportedDevice.
        :type vendor: str
        """
        self._vendor = vendor

    @property
    def platform(self):
        r"""Gets the platform of this SupportedDevice.

        型号

        :return: The platform of this SupportedDevice.
        :rtype: str
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        r"""Sets the platform of this SupportedDevice.

        型号

        :param platform: The platform of this SupportedDevice.
        :type platform: str
        """
        self._platform = platform

    @property
    def version(self):
        r"""Gets the version of this SupportedDevice.

        版本

        :return: The version of this SupportedDevice.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this SupportedDevice.

        版本

        :param version: The version of this SupportedDevice.
        :type version: str
        """
        self._version = version

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
        if not isinstance(other, SupportedDevice):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
