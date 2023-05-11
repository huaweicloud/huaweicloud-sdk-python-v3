# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReleaseFileVersionDo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'version': 'str',
        'path': 'str',
        'download_url': 'str'
    }

    attribute_map = {
        'version': 'version',
        'path': 'path',
        'download_url': 'download_url'
    }

    def __init__(self, version=None, path=None, download_url=None):
        """ReleaseFileVersionDo

        The model defined in huaweicloud sdk

        :param version: 发布库文件的版本
        :type version: str
        :param path: 发布库文件的路径
        :type path: str
        :param download_url: 发布库文件的下载链接
        :type download_url: str
        """
        
        

        self._version = None
        self._path = None
        self._download_url = None
        self.discriminator = None

        if version is not None:
            self.version = version
        if path is not None:
            self.path = path
        if download_url is not None:
            self.download_url = download_url

    @property
    def version(self):
        """Gets the version of this ReleaseFileVersionDo.

        发布库文件的版本

        :return: The version of this ReleaseFileVersionDo.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ReleaseFileVersionDo.

        发布库文件的版本

        :param version: The version of this ReleaseFileVersionDo.
        :type version: str
        """
        self._version = version

    @property
    def path(self):
        """Gets the path of this ReleaseFileVersionDo.

        发布库文件的路径

        :return: The path of this ReleaseFileVersionDo.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this ReleaseFileVersionDo.

        发布库文件的路径

        :param path: The path of this ReleaseFileVersionDo.
        :type path: str
        """
        self._path = path

    @property
    def download_url(self):
        """Gets the download_url of this ReleaseFileVersionDo.

        发布库文件的下载链接

        :return: The download_url of this ReleaseFileVersionDo.
        :rtype: str
        """
        return self._download_url

    @download_url.setter
    def download_url(self, download_url):
        """Sets the download_url of this ReleaseFileVersionDo.

        发布库文件的下载链接

        :param download_url: The download_url of this ReleaseFileVersionDo.
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
        if not isinstance(other, ReleaseFileVersionDo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
