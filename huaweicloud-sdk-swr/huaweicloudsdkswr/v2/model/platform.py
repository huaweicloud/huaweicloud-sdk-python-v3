# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Platform:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'architecture': 'str',
        'os': 'str',
        'os_version': 'str',
        'os_features': 'list[str]',
        'variant': 'str'
    }

    attribute_map = {
        'architecture': 'architecture',
        'os': 'os',
        'os_version': 'os.version',
        'os_features': 'os.features',
        'variant': 'variant'
    }

    def __init__(self, architecture=None, os=None, os_version=None, os_features=None, variant=None):
        r"""Platform

        The model defined in huaweicloud sdk

        :param architecture: 制品适用的CPU架构。
        :type architecture: str
        :param os: 制品适用的操作系统。
        :type os: str
        :param os_version: 制品适用的操作系统版本。
        :type os_version: str
        :param os_features: 制品适用的操作系统特性。
        :type os_features: list[str]
        :param variant: 同一系列 CPU 下的细分型号，例如 Intel i5-13400、i5-13600 属于同代不同 variant。
        :type variant: str
        """
        
        

        self._architecture = None
        self._os = None
        self._os_version = None
        self._os_features = None
        self._variant = None
        self.discriminator = None

        if architecture is not None:
            self.architecture = architecture
        if os is not None:
            self.os = os
        if os_version is not None:
            self.os_version = os_version
        if os_features is not None:
            self.os_features = os_features
        if variant is not None:
            self.variant = variant

    @property
    def architecture(self):
        r"""Gets the architecture of this Platform.

        制品适用的CPU架构。

        :return: The architecture of this Platform.
        :rtype: str
        """
        return self._architecture

    @architecture.setter
    def architecture(self, architecture):
        r"""Sets the architecture of this Platform.

        制品适用的CPU架构。

        :param architecture: The architecture of this Platform.
        :type architecture: str
        """
        self._architecture = architecture

    @property
    def os(self):
        r"""Gets the os of this Platform.

        制品适用的操作系统。

        :return: The os of this Platform.
        :rtype: str
        """
        return self._os

    @os.setter
    def os(self, os):
        r"""Sets the os of this Platform.

        制品适用的操作系统。

        :param os: The os of this Platform.
        :type os: str
        """
        self._os = os

    @property
    def os_version(self):
        r"""Gets the os_version of this Platform.

        制品适用的操作系统版本。

        :return: The os_version of this Platform.
        :rtype: str
        """
        return self._os_version

    @os_version.setter
    def os_version(self, os_version):
        r"""Sets the os_version of this Platform.

        制品适用的操作系统版本。

        :param os_version: The os_version of this Platform.
        :type os_version: str
        """
        self._os_version = os_version

    @property
    def os_features(self):
        r"""Gets the os_features of this Platform.

        制品适用的操作系统特性。

        :return: The os_features of this Platform.
        :rtype: list[str]
        """
        return self._os_features

    @os_features.setter
    def os_features(self, os_features):
        r"""Sets the os_features of this Platform.

        制品适用的操作系统特性。

        :param os_features: The os_features of this Platform.
        :type os_features: list[str]
        """
        self._os_features = os_features

    @property
    def variant(self):
        r"""Gets the variant of this Platform.

        同一系列 CPU 下的细分型号，例如 Intel i5-13400、i5-13600 属于同代不同 variant。

        :return: The variant of this Platform.
        :rtype: str
        """
        return self._variant

    @variant.setter
    def variant(self, variant):
        r"""Sets the variant of this Platform.

        同一系列 CPU 下的细分型号，例如 Intel i5-13400、i5-13600 属于同代不同 variant。

        :param variant: The variant of this Platform.
        :type variant: str
        """
        self._variant = variant

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
        if not isinstance(other, Platform):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
