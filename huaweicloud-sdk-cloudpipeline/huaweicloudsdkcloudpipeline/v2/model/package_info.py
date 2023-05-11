# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PackageInfo:

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
        'package_type': 'str',
        'version': 'str',
        'download_url': 'str'
    }

    attribute_map = {
        'name': 'name',
        'package_type': 'packageType',
        'version': 'version',
        'download_url': 'downloadUrl'
    }

    def __init__(self, name=None, package_type=None, version=None, download_url=None):
        """PackageInfo

        The model defined in huaweicloud sdk

        :param name: 产物名
        :type name: str
        :param package_type: 产物类型
        :type package_type: str
        :param version: 产物版本号
        :type version: str
        :param download_url: 产物下载地址
        :type download_url: str
        """
        
        

        self._name = None
        self._package_type = None
        self._version = None
        self._download_url = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if package_type is not None:
            self.package_type = package_type
        if version is not None:
            self.version = version
        if download_url is not None:
            self.download_url = download_url

    @property
    def name(self):
        """Gets the name of this PackageInfo.

        产物名

        :return: The name of this PackageInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PackageInfo.

        产物名

        :param name: The name of this PackageInfo.
        :type name: str
        """
        self._name = name

    @property
    def package_type(self):
        """Gets the package_type of this PackageInfo.

        产物类型

        :return: The package_type of this PackageInfo.
        :rtype: str
        """
        return self._package_type

    @package_type.setter
    def package_type(self, package_type):
        """Sets the package_type of this PackageInfo.

        产物类型

        :param package_type: The package_type of this PackageInfo.
        :type package_type: str
        """
        self._package_type = package_type

    @property
    def version(self):
        """Gets the version of this PackageInfo.

        产物版本号

        :return: The version of this PackageInfo.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this PackageInfo.

        产物版本号

        :param version: The version of this PackageInfo.
        :type version: str
        """
        self._version = version

    @property
    def download_url(self):
        """Gets the download_url of this PackageInfo.

        产物下载地址

        :return: The download_url of this PackageInfo.
        :rtype: str
        """
        return self._download_url

    @download_url.setter
    def download_url(self, download_url):
        """Sets the download_url of this PackageInfo.

        产物下载地址

        :param download_url: The download_url of this PackageInfo.
        :type download_url: str
        """
        self._download_url = download_url

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
        if not isinstance(other, PackageInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
