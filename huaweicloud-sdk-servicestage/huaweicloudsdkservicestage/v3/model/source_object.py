# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SourceObject:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'kind': 'SourceKind',
        'url': 'str',
        'version': 'str',
        'storage': 'str',
        'auth': 'str',
        'repo_auth': 'str',
        'repo_namespace': 'str',
        'repo_ref': 'str',
        'repo_type': 'str',
        'web_url': 'str',
        'repo_url': 'str'
    }

    attribute_map = {
        'kind': 'kind',
        'url': 'url',
        'version': 'version',
        'storage': 'storage',
        'auth': 'auth',
        'repo_auth': 'repo_auth',
        'repo_namespace': 'repo_namespace',
        'repo_ref': 'repo_ref',
        'repo_type': 'repo_type',
        'web_url': 'web_url',
        'repo_url': 'repo_url'
    }

    def __init__(self, kind=None, url=None, version=None, storage=None, auth=None, repo_auth=None, repo_namespace=None, repo_ref=None, repo_type=None, web_url=None, repo_url=None):
        """SourceObject

        The model defined in huaweicloud sdk

        :param kind: 
        :type kind: :class:`huaweicloudsdkservicestage.v3.SourceKind`
        :param url: 
        :type url: str
        :param version: 软件包版本
        :type version: str
        :param storage: 
        :type storage: str
        :param auth: 
        :type auth: str
        :param repo_auth: 
        :type repo_auth: str
        :param repo_namespace: 
        :type repo_namespace: str
        :param repo_ref: 
        :type repo_ref: str
        :param repo_type: 
        :type repo_type: str
        :param web_url: 
        :type web_url: str
        :param repo_url: 
        :type repo_url: str
        """
        
        

        self._kind = None
        self._url = None
        self._version = None
        self._storage = None
        self._auth = None
        self._repo_auth = None
        self._repo_namespace = None
        self._repo_ref = None
        self._repo_type = None
        self._web_url = None
        self._repo_url = None
        self.discriminator = None

        self.kind = kind
        if url is not None:
            self.url = url
        if version is not None:
            self.version = version
        if storage is not None:
            self.storage = storage
        if auth is not None:
            self.auth = auth
        if repo_auth is not None:
            self.repo_auth = repo_auth
        if repo_namespace is not None:
            self.repo_namespace = repo_namespace
        if repo_ref is not None:
            self.repo_ref = repo_ref
        if repo_type is not None:
            self.repo_type = repo_type
        if web_url is not None:
            self.web_url = web_url
        if repo_url is not None:
            self.repo_url = repo_url

    @property
    def kind(self):
        """Gets the kind of this SourceObject.

        :return: The kind of this SourceObject.
        :rtype: :class:`huaweicloudsdkservicestage.v3.SourceKind`
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this SourceObject.

        :param kind: The kind of this SourceObject.
        :type kind: :class:`huaweicloudsdkservicestage.v3.SourceKind`
        """
        self._kind = kind

    @property
    def url(self):
        """Gets the url of this SourceObject.

        :return: The url of this SourceObject.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this SourceObject.

        :param url: The url of this SourceObject.
        :type url: str
        """
        self._url = url

    @property
    def version(self):
        """Gets the version of this SourceObject.

        软件包版本

        :return: The version of this SourceObject.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this SourceObject.

        软件包版本

        :param version: The version of this SourceObject.
        :type version: str
        """
        self._version = version

    @property
    def storage(self):
        """Gets the storage of this SourceObject.

        :return: The storage of this SourceObject.
        :rtype: str
        """
        return self._storage

    @storage.setter
    def storage(self, storage):
        """Sets the storage of this SourceObject.

        :param storage: The storage of this SourceObject.
        :type storage: str
        """
        self._storage = storage

    @property
    def auth(self):
        """Gets the auth of this SourceObject.

        :return: The auth of this SourceObject.
        :rtype: str
        """
        return self._auth

    @auth.setter
    def auth(self, auth):
        """Sets the auth of this SourceObject.

        :param auth: The auth of this SourceObject.
        :type auth: str
        """
        self._auth = auth

    @property
    def repo_auth(self):
        """Gets the repo_auth of this SourceObject.

        :return: The repo_auth of this SourceObject.
        :rtype: str
        """
        return self._repo_auth

    @repo_auth.setter
    def repo_auth(self, repo_auth):
        """Sets the repo_auth of this SourceObject.

        :param repo_auth: The repo_auth of this SourceObject.
        :type repo_auth: str
        """
        self._repo_auth = repo_auth

    @property
    def repo_namespace(self):
        """Gets the repo_namespace of this SourceObject.

        :return: The repo_namespace of this SourceObject.
        :rtype: str
        """
        return self._repo_namespace

    @repo_namespace.setter
    def repo_namespace(self, repo_namespace):
        """Sets the repo_namespace of this SourceObject.

        :param repo_namespace: The repo_namespace of this SourceObject.
        :type repo_namespace: str
        """
        self._repo_namespace = repo_namespace

    @property
    def repo_ref(self):
        """Gets the repo_ref of this SourceObject.

        :return: The repo_ref of this SourceObject.
        :rtype: str
        """
        return self._repo_ref

    @repo_ref.setter
    def repo_ref(self, repo_ref):
        """Sets the repo_ref of this SourceObject.

        :param repo_ref: The repo_ref of this SourceObject.
        :type repo_ref: str
        """
        self._repo_ref = repo_ref

    @property
    def repo_type(self):
        """Gets the repo_type of this SourceObject.

        :return: The repo_type of this SourceObject.
        :rtype: str
        """
        return self._repo_type

    @repo_type.setter
    def repo_type(self, repo_type):
        """Sets the repo_type of this SourceObject.

        :param repo_type: The repo_type of this SourceObject.
        :type repo_type: str
        """
        self._repo_type = repo_type

    @property
    def web_url(self):
        """Gets the web_url of this SourceObject.

        :return: The web_url of this SourceObject.
        :rtype: str
        """
        return self._web_url

    @web_url.setter
    def web_url(self, web_url):
        """Sets the web_url of this SourceObject.

        :param web_url: The web_url of this SourceObject.
        :type web_url: str
        """
        self._web_url = web_url

    @property
    def repo_url(self):
        """Gets the repo_url of this SourceObject.

        :return: The repo_url of this SourceObject.
        :rtype: str
        """
        return self._repo_url

    @repo_url.setter
    def repo_url(self, repo_url):
        """Sets the repo_url of this SourceObject.

        :param repo_url: The repo_url of this SourceObject.
        :type repo_url: str
        """
        self._repo_url = repo_url

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
        if not isinstance(other, SourceObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
