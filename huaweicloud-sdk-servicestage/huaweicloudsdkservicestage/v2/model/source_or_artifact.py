# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SourceOrArtifact:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'storage': 'str',
        'type': 'str',
        'url': 'str',
        'web_url': 'str',
        'auth': 'str',
        'properties': 'ObsProperties',
        'repo_type': 'SourceRepoType',
        'repo_url': 'str',
        'repo_ref': 'str',
        'repo_auth': 'str'
    }

    attribute_map = {
        'storage': 'storage',
        'type': 'type',
        'url': 'url',
        'web_url': 'webUrl',
        'auth': 'auth',
        'properties': 'properties',
        'repo_type': 'repo_type',
        'repo_url': 'repo_url',
        'repo_ref': 'repo_ref',
        'repo_auth': 'repo_auth'
    }

    def __init__(self, storage=None, type=None, url=None, web_url=None, auth=None, properties=None, repo_type=None, repo_url=None, repo_ref=None, repo_auth=None):
        """SourceOrArtifact

        The model defined in huaweicloud sdk

        :param storage: 存储方式，支持软件仓库swr和对象存储obs。
        :type storage: str
        :param type: 类别，支持package。
        :type type: str
        :param url: 软件包源码地址，如https://{IP}:20202/xxx/xxx.jar。
        :type url: str
        :param web_url: 软件包/源码仓库地址
        :type web_url: str
        :param auth: 认证方式，支持iam，none，默认是iam。
        :type auth: str
        :param properties: 
        :type properties: :class:`huaweicloudsdkservicestage.v2.ObsProperties`
        :param repo_type: 
        :type repo_type: :class:`huaweicloudsdkservicestage.v2.SourceRepoType`
        :param repo_url: 代码仓url，如：https://github.com/example/demo.git
        :type repo_url: str
        :param repo_ref: 代码分支或者Tag，默认是master。
        :type repo_ref: str
        :param repo_auth: 授权名称，在授权列表获取。
        :type repo_auth: str
        """
        
        

        self._storage = None
        self._type = None
        self._url = None
        self._web_url = None
        self._auth = None
        self._properties = None
        self._repo_type = None
        self._repo_url = None
        self._repo_ref = None
        self._repo_auth = None
        self.discriminator = None

        if storage is not None:
            self.storage = storage
        if type is not None:
            self.type = type
        if url is not None:
            self.url = url
        if web_url is not None:
            self.web_url = web_url
        if auth is not None:
            self.auth = auth
        if properties is not None:
            self.properties = properties
        if repo_type is not None:
            self.repo_type = repo_type
        if repo_url is not None:
            self.repo_url = repo_url
        if repo_ref is not None:
            self.repo_ref = repo_ref
        if repo_auth is not None:
            self.repo_auth = repo_auth

    @property
    def storage(self):
        """Gets the storage of this SourceOrArtifact.

        存储方式，支持软件仓库swr和对象存储obs。

        :return: The storage of this SourceOrArtifact.
        :rtype: str
        """
        return self._storage

    @storage.setter
    def storage(self, storage):
        """Sets the storage of this SourceOrArtifact.

        存储方式，支持软件仓库swr和对象存储obs。

        :param storage: The storage of this SourceOrArtifact.
        :type storage: str
        """
        self._storage = storage

    @property
    def type(self):
        """Gets the type of this SourceOrArtifact.

        类别，支持package。

        :return: The type of this SourceOrArtifact.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SourceOrArtifact.

        类别，支持package。

        :param type: The type of this SourceOrArtifact.
        :type type: str
        """
        self._type = type

    @property
    def url(self):
        """Gets the url of this SourceOrArtifact.

        软件包源码地址，如https://{IP}:20202/xxx/xxx.jar。

        :return: The url of this SourceOrArtifact.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this SourceOrArtifact.

        软件包源码地址，如https://{IP}:20202/xxx/xxx.jar。

        :param url: The url of this SourceOrArtifact.
        :type url: str
        """
        self._url = url

    @property
    def web_url(self):
        """Gets the web_url of this SourceOrArtifact.

        软件包/源码仓库地址

        :return: The web_url of this SourceOrArtifact.
        :rtype: str
        """
        return self._web_url

    @web_url.setter
    def web_url(self, web_url):
        """Sets the web_url of this SourceOrArtifact.

        软件包/源码仓库地址

        :param web_url: The web_url of this SourceOrArtifact.
        :type web_url: str
        """
        self._web_url = web_url

    @property
    def auth(self):
        """Gets the auth of this SourceOrArtifact.

        认证方式，支持iam，none，默认是iam。

        :return: The auth of this SourceOrArtifact.
        :rtype: str
        """
        return self._auth

    @auth.setter
    def auth(self, auth):
        """Sets the auth of this SourceOrArtifact.

        认证方式，支持iam，none，默认是iam。

        :param auth: The auth of this SourceOrArtifact.
        :type auth: str
        """
        self._auth = auth

    @property
    def properties(self):
        """Gets the properties of this SourceOrArtifact.

        :return: The properties of this SourceOrArtifact.
        :rtype: :class:`huaweicloudsdkservicestage.v2.ObsProperties`
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this SourceOrArtifact.

        :param properties: The properties of this SourceOrArtifact.
        :type properties: :class:`huaweicloudsdkservicestage.v2.ObsProperties`
        """
        self._properties = properties

    @property
    def repo_type(self):
        """Gets the repo_type of this SourceOrArtifact.

        :return: The repo_type of this SourceOrArtifact.
        :rtype: :class:`huaweicloudsdkservicestage.v2.SourceRepoType`
        """
        return self._repo_type

    @repo_type.setter
    def repo_type(self, repo_type):
        """Sets the repo_type of this SourceOrArtifact.

        :param repo_type: The repo_type of this SourceOrArtifact.
        :type repo_type: :class:`huaweicloudsdkservicestage.v2.SourceRepoType`
        """
        self._repo_type = repo_type

    @property
    def repo_url(self):
        """Gets the repo_url of this SourceOrArtifact.

        代码仓url，如：https://github.com/example/demo.git

        :return: The repo_url of this SourceOrArtifact.
        :rtype: str
        """
        return self._repo_url

    @repo_url.setter
    def repo_url(self, repo_url):
        """Sets the repo_url of this SourceOrArtifact.

        代码仓url，如：https://github.com/example/demo.git

        :param repo_url: The repo_url of this SourceOrArtifact.
        :type repo_url: str
        """
        self._repo_url = repo_url

    @property
    def repo_ref(self):
        """Gets the repo_ref of this SourceOrArtifact.

        代码分支或者Tag，默认是master。

        :return: The repo_ref of this SourceOrArtifact.
        :rtype: str
        """
        return self._repo_ref

    @repo_ref.setter
    def repo_ref(self, repo_ref):
        """Sets the repo_ref of this SourceOrArtifact.

        代码分支或者Tag，默认是master。

        :param repo_ref: The repo_ref of this SourceOrArtifact.
        :type repo_ref: str
        """
        self._repo_ref = repo_ref

    @property
    def repo_auth(self):
        """Gets the repo_auth of this SourceOrArtifact.

        授权名称，在授权列表获取。

        :return: The repo_auth of this SourceOrArtifact.
        :rtype: str
        """
        return self._repo_auth

    @repo_auth.setter
    def repo_auth(self, repo_auth):
        """Sets the repo_auth of this SourceOrArtifact.

        授权名称，在授权列表获取。

        :param repo_auth: The repo_auth of this SourceOrArtifact.
        :type repo_auth: str
        """
        self._repo_auth = repo_auth

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
        if not isinstance(other, SourceOrArtifact):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
