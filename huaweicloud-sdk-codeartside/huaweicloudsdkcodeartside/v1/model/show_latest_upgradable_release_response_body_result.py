# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowLatestUpgradableReleaseResponseBodyResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'hash': 'str',
        'available': 'bool',
        'sub_product_name': 'str',
        'version': 'str',
        'url': 'str'
    }

    attribute_map = {
        'hash': 'hash',
        'available': 'available',
        'sub_product_name': 'sub_product_name',
        'version': 'version',
        'url': 'url'
    }

    def __init__(self, hash=None, available=None, sub_product_name=None, version=None, url=None):
        r"""ShowLatestUpgradableReleaseResponseBodyResult

        The model defined in huaweicloud sdk

        :param hash: 哈希值
        :type hash: str
        :param available: 版本是否可用
        :type available: bool
        :param sub_product_name: 子产品名称
        :type sub_product_name: str
        :param version: 子产品版本
        :type version: str
        :param url: 下载链接
        :type url: str
        """
        
        

        self._hash = None
        self._available = None
        self._sub_product_name = None
        self._version = None
        self._url = None
        self.discriminator = None

        self.hash = hash
        self.available = available
        self.sub_product_name = sub_product_name
        self.version = version
        self.url = url

    @property
    def hash(self):
        r"""Gets the hash of this ShowLatestUpgradableReleaseResponseBodyResult.

        哈希值

        :return: The hash of this ShowLatestUpgradableReleaseResponseBodyResult.
        :rtype: str
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        r"""Sets the hash of this ShowLatestUpgradableReleaseResponseBodyResult.

        哈希值

        :param hash: The hash of this ShowLatestUpgradableReleaseResponseBodyResult.
        :type hash: str
        """
        self._hash = hash

    @property
    def available(self):
        r"""Gets the available of this ShowLatestUpgradableReleaseResponseBodyResult.

        版本是否可用

        :return: The available of this ShowLatestUpgradableReleaseResponseBodyResult.
        :rtype: bool
        """
        return self._available

    @available.setter
    def available(self, available):
        r"""Sets the available of this ShowLatestUpgradableReleaseResponseBodyResult.

        版本是否可用

        :param available: The available of this ShowLatestUpgradableReleaseResponseBodyResult.
        :type available: bool
        """
        self._available = available

    @property
    def sub_product_name(self):
        r"""Gets the sub_product_name of this ShowLatestUpgradableReleaseResponseBodyResult.

        子产品名称

        :return: The sub_product_name of this ShowLatestUpgradableReleaseResponseBodyResult.
        :rtype: str
        """
        return self._sub_product_name

    @sub_product_name.setter
    def sub_product_name(self, sub_product_name):
        r"""Sets the sub_product_name of this ShowLatestUpgradableReleaseResponseBodyResult.

        子产品名称

        :param sub_product_name: The sub_product_name of this ShowLatestUpgradableReleaseResponseBodyResult.
        :type sub_product_name: str
        """
        self._sub_product_name = sub_product_name

    @property
    def version(self):
        r"""Gets the version of this ShowLatestUpgradableReleaseResponseBodyResult.

        子产品版本

        :return: The version of this ShowLatestUpgradableReleaseResponseBodyResult.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this ShowLatestUpgradableReleaseResponseBodyResult.

        子产品版本

        :param version: The version of this ShowLatestUpgradableReleaseResponseBodyResult.
        :type version: str
        """
        self._version = version

    @property
    def url(self):
        r"""Gets the url of this ShowLatestUpgradableReleaseResponseBodyResult.

        下载链接

        :return: The url of this ShowLatestUpgradableReleaseResponseBodyResult.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this ShowLatestUpgradableReleaseResponseBodyResult.

        下载链接

        :param url: The url of this ShowLatestUpgradableReleaseResponseBodyResult.
        :type url: str
        """
        self._url = url

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
        if not isinstance(other, ShowLatestUpgradableReleaseResponseBodyResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
