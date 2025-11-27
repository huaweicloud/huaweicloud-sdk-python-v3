# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateFederationCertResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'kind': 'str',
        'api_version': 'str',
        'clusters': 'list[NamedCluster]',
        'users': 'list[NamedAuthInfo]',
        'contexts': 'list[NamedContext]',
        'current_context': 'str'
    }

    attribute_map = {
        'kind': 'kind',
        'api_version': 'apiVersion',
        'clusters': 'clusters',
        'users': 'users',
        'contexts': 'contexts',
        'current_context': 'current-context'
    }

    def __init__(self, kind=None, api_version=None, clusters=None, users=None, contexts=None, current_context=None):
        r"""CreateFederationCertResponse

        The model defined in huaweicloud sdk

        :param kind: API类型，固定值“Config”，该值不可修改
        :type kind: str
        :param api_version: API版本，固定值“v1”，该值不可修改
        :type api_version: str
        :param clusters: 集群列表
        :type clusters: list[:class:`huaweicloudsdkucs.v1.NamedCluster`]
        :param users: 存放了指定用户的一些证书信息和ClientKey信息
        :type users: list[:class:`huaweicloudsdkucs.v1.NamedAuthInfo`]
        :param contexts: 上下文列表
        :type contexts: list[:class:`huaweicloudsdkucs.v1.NamedContext`]
        :param current_context: 当前上下文
        :type current_context: str
        """
        
        super().__init__()

        self._kind = None
        self._api_version = None
        self._clusters = None
        self._users = None
        self._contexts = None
        self._current_context = None
        self.discriminator = None

        if kind is not None:
            self.kind = kind
        if api_version is not None:
            self.api_version = api_version
        if clusters is not None:
            self.clusters = clusters
        if users is not None:
            self.users = users
        if contexts is not None:
            self.contexts = contexts
        if current_context is not None:
            self.current_context = current_context

    @property
    def kind(self):
        r"""Gets the kind of this CreateFederationCertResponse.

        API类型，固定值“Config”，该值不可修改

        :return: The kind of this CreateFederationCertResponse.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        r"""Sets the kind of this CreateFederationCertResponse.

        API类型，固定值“Config”，该值不可修改

        :param kind: The kind of this CreateFederationCertResponse.
        :type kind: str
        """
        self._kind = kind

    @property
    def api_version(self):
        r"""Gets the api_version of this CreateFederationCertResponse.

        API版本，固定值“v1”，该值不可修改

        :return: The api_version of this CreateFederationCertResponse.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        r"""Sets the api_version of this CreateFederationCertResponse.

        API版本，固定值“v1”，该值不可修改

        :param api_version: The api_version of this CreateFederationCertResponse.
        :type api_version: str
        """
        self._api_version = api_version

    @property
    def clusters(self):
        r"""Gets the clusters of this CreateFederationCertResponse.

        集群列表

        :return: The clusters of this CreateFederationCertResponse.
        :rtype: list[:class:`huaweicloudsdkucs.v1.NamedCluster`]
        """
        return self._clusters

    @clusters.setter
    def clusters(self, clusters):
        r"""Sets the clusters of this CreateFederationCertResponse.

        集群列表

        :param clusters: The clusters of this CreateFederationCertResponse.
        :type clusters: list[:class:`huaweicloudsdkucs.v1.NamedCluster`]
        """
        self._clusters = clusters

    @property
    def users(self):
        r"""Gets the users of this CreateFederationCertResponse.

        存放了指定用户的一些证书信息和ClientKey信息

        :return: The users of this CreateFederationCertResponse.
        :rtype: list[:class:`huaweicloudsdkucs.v1.NamedAuthInfo`]
        """
        return self._users

    @users.setter
    def users(self, users):
        r"""Sets the users of this CreateFederationCertResponse.

        存放了指定用户的一些证书信息和ClientKey信息

        :param users: The users of this CreateFederationCertResponse.
        :type users: list[:class:`huaweicloudsdkucs.v1.NamedAuthInfo`]
        """
        self._users = users

    @property
    def contexts(self):
        r"""Gets the contexts of this CreateFederationCertResponse.

        上下文列表

        :return: The contexts of this CreateFederationCertResponse.
        :rtype: list[:class:`huaweicloudsdkucs.v1.NamedContext`]
        """
        return self._contexts

    @contexts.setter
    def contexts(self, contexts):
        r"""Sets the contexts of this CreateFederationCertResponse.

        上下文列表

        :param contexts: The contexts of this CreateFederationCertResponse.
        :type contexts: list[:class:`huaweicloudsdkucs.v1.NamedContext`]
        """
        self._contexts = contexts

    @property
    def current_context(self):
        r"""Gets the current_context of this CreateFederationCertResponse.

        当前上下文

        :return: The current_context of this CreateFederationCertResponse.
        :rtype: str
        """
        return self._current_context

    @current_context.setter
    def current_context(self, current_context):
        r"""Sets the current_context of this CreateFederationCertResponse.

        当前上下文

        :param current_context: The current_context of this CreateFederationCertResponse.
        :type current_context: str
        """
        self._current_context = current_context

    def to_dict(self):
        import warnings
        warnings.warn("CreateFederationCertResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, CreateFederationCertResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
