# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Artifact:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'path': 'str',
        'url': 'str',
        'revision': 'str',
        'digest': 'str',
        'last_update_time': 'str',
        'size': 'int'
    }

    attribute_map = {
        'path': 'path',
        'url': 'url',
        'revision': 'revision',
        'digest': 'digest',
        'last_update_time': 'lastUpdateTime',
        'size': 'size'
    }

    def __init__(self, path=None, url=None, revision=None, digest=None, last_update_time=None, size=None):
        r"""Artifact

        The model defined in huaweicloud sdk

        :param path: 制品的相对文件路径
        :type path: str
        :param url: HTTP地址，可通过该地址下载或访问制品内容
        :type url: str
        :param revision: 版本标识符
        :type revision: str
        :param digest: 文件摘要，格式为 &lt;算法&gt;:&lt;校验值&gt;
        :type digest: str
        :param last_update_time: 最后更新时间
        :type last_update_time: str
        :param size: 文件大小（以字节为单位）
        :type size: int
        """
        
        

        self._path = None
        self._url = None
        self._revision = None
        self._digest = None
        self._last_update_time = None
        self._size = None
        self.discriminator = None

        if path is not None:
            self.path = path
        if url is not None:
            self.url = url
        if revision is not None:
            self.revision = revision
        if digest is not None:
            self.digest = digest
        if last_update_time is not None:
            self.last_update_time = last_update_time
        if size is not None:
            self.size = size

    @property
    def path(self):
        r"""Gets the path of this Artifact.

        制品的相对文件路径

        :return: The path of this Artifact.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        r"""Sets the path of this Artifact.

        制品的相对文件路径

        :param path: The path of this Artifact.
        :type path: str
        """
        self._path = path

    @property
    def url(self):
        r"""Gets the url of this Artifact.

        HTTP地址，可通过该地址下载或访问制品内容

        :return: The url of this Artifact.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this Artifact.

        HTTP地址，可通过该地址下载或访问制品内容

        :param url: The url of this Artifact.
        :type url: str
        """
        self._url = url

    @property
    def revision(self):
        r"""Gets the revision of this Artifact.

        版本标识符

        :return: The revision of this Artifact.
        :rtype: str
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        r"""Sets the revision of this Artifact.

        版本标识符

        :param revision: The revision of this Artifact.
        :type revision: str
        """
        self._revision = revision

    @property
    def digest(self):
        r"""Gets the digest of this Artifact.

        文件摘要，格式为 <算法>:<校验值>

        :return: The digest of this Artifact.
        :rtype: str
        """
        return self._digest

    @digest.setter
    def digest(self, digest):
        r"""Sets the digest of this Artifact.

        文件摘要，格式为 <算法>:<校验值>

        :param digest: The digest of this Artifact.
        :type digest: str
        """
        self._digest = digest

    @property
    def last_update_time(self):
        r"""Gets the last_update_time of this Artifact.

        最后更新时间

        :return: The last_update_time of this Artifact.
        :rtype: str
        """
        return self._last_update_time

    @last_update_time.setter
    def last_update_time(self, last_update_time):
        r"""Sets the last_update_time of this Artifact.

        最后更新时间

        :param last_update_time: The last_update_time of this Artifact.
        :type last_update_time: str
        """
        self._last_update_time = last_update_time

    @property
    def size(self):
        r"""Gets the size of this Artifact.

        文件大小（以字节为单位）

        :return: The size of this Artifact.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this Artifact.

        文件大小（以字节为单位）

        :param size: The size of this Artifact.
        :type size: int
        """
        self._size = size

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
        if not isinstance(other, Artifact):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
