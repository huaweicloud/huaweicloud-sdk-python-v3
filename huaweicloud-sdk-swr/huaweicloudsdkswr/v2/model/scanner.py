# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Scanner:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'vendor': 'str',
        'version': 'str'
    }

    attribute_map = {
        'name': 'name',
        'vendor': 'vendor',
        'version': 'version'
    }

    def __init__(self, name=None, vendor=None, version=None):
        r"""Scanner

        The model defined in huaweicloud sdk

        :param name: 扫描器的名称
        :type name: str
        :param vendor: 扫描器的提供商
        :type vendor: str
        :param version: 扫描器的版本号
        :type version: str
        """
        
        

        self._name = None
        self._vendor = None
        self._version = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if vendor is not None:
            self.vendor = vendor
        if version is not None:
            self.version = version

    @property
    def name(self):
        r"""Gets the name of this Scanner.

        扫描器的名称

        :return: The name of this Scanner.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this Scanner.

        扫描器的名称

        :param name: The name of this Scanner.
        :type name: str
        """
        self._name = name

    @property
    def vendor(self):
        r"""Gets the vendor of this Scanner.

        扫描器的提供商

        :return: The vendor of this Scanner.
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        r"""Sets the vendor of this Scanner.

        扫描器的提供商

        :param vendor: The vendor of this Scanner.
        :type vendor: str
        """
        self._vendor = vendor

    @property
    def version(self):
        r"""Gets the version of this Scanner.

        扫描器的版本号

        :return: The version of this Scanner.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this Scanner.

        扫描器的版本号

        :param version: The version of this Scanner.
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
        if not isinstance(other, Scanner):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
