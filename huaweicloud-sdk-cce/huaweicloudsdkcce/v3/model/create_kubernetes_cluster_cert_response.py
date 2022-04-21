# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateKubernetesClusterCertResponse(SdkResponse):

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
        'preferences': 'object',
        'clusters': 'list[Clusters]',
        'users': 'list[Users]',
        'contexts': 'list[Contexts]',
        'current_context': 'str',
        'port_id': 'str'
    }

    attribute_map = {
        'kind': 'kind',
        'api_version': 'apiVersion',
        'preferences': 'preferences',
        'clusters': 'clusters',
        'users': 'users',
        'contexts': 'contexts',
        'current_context': 'current-context',
        'port_id': 'Port-ID'
    }

    def __init__(self, kind=None, api_version=None, preferences=None, clusters=None, users=None, contexts=None, current_context=None, port_id=None):
        """CreateKubernetesClusterCertResponse

        The model defined in huaweicloud sdk

        :param kind: API类型，固定值“Config”，该值不可修改。 
        :type kind: str
        :param api_version: API版本，固定值“v1”。
        :type api_version: str
        :param preferences: 当前未使用该字段，当前默认为空。
        :type preferences: object
        :param clusters: 集群列表。
        :type clusters: list[:class:`huaweicloudsdkcce.v3.Clusters`]
        :param users: 存放了指定用户的一些证书信息和ClientKey信息。
        :type users: list[:class:`huaweicloudsdkcce.v3.Users`]
        :param contexts: 上下文列表。
        :type contexts: list[:class:`huaweicloudsdkcce.v3.Contexts`]
        :param current_context: 当前上下文，若存在publicIp（虚拟机弹性IP）时为 external; 若不存在publicIp为 internal。
        :type current_context: str
        :param port_id: 
        :type port_id: str
        """
        
        super(CreateKubernetesClusterCertResponse, self).__init__()

        self._kind = None
        self._api_version = None
        self._preferences = None
        self._clusters = None
        self._users = None
        self._contexts = None
        self._current_context = None
        self._port_id = None
        self.discriminator = None

        if kind is not None:
            self.kind = kind
        if api_version is not None:
            self.api_version = api_version
        if preferences is not None:
            self.preferences = preferences
        if clusters is not None:
            self.clusters = clusters
        if users is not None:
            self.users = users
        if contexts is not None:
            self.contexts = contexts
        if current_context is not None:
            self.current_context = current_context
        if port_id is not None:
            self.port_id = port_id

    @property
    def kind(self):
        """Gets the kind of this CreateKubernetesClusterCertResponse.

        API类型，固定值“Config”，该值不可修改。 

        :return: The kind of this CreateKubernetesClusterCertResponse.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this CreateKubernetesClusterCertResponse.

        API类型，固定值“Config”，该值不可修改。 

        :param kind: The kind of this CreateKubernetesClusterCertResponse.
        :type kind: str
        """
        self._kind = kind

    @property
    def api_version(self):
        """Gets the api_version of this CreateKubernetesClusterCertResponse.

        API版本，固定值“v1”。

        :return: The api_version of this CreateKubernetesClusterCertResponse.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """Sets the api_version of this CreateKubernetesClusterCertResponse.

        API版本，固定值“v1”。

        :param api_version: The api_version of this CreateKubernetesClusterCertResponse.
        :type api_version: str
        """
        self._api_version = api_version

    @property
    def preferences(self):
        """Gets the preferences of this CreateKubernetesClusterCertResponse.

        当前未使用该字段，当前默认为空。

        :return: The preferences of this CreateKubernetesClusterCertResponse.
        :rtype: object
        """
        return self._preferences

    @preferences.setter
    def preferences(self, preferences):
        """Sets the preferences of this CreateKubernetesClusterCertResponse.

        当前未使用该字段，当前默认为空。

        :param preferences: The preferences of this CreateKubernetesClusterCertResponse.
        :type preferences: object
        """
        self._preferences = preferences

    @property
    def clusters(self):
        """Gets the clusters of this CreateKubernetesClusterCertResponse.

        集群列表。

        :return: The clusters of this CreateKubernetesClusterCertResponse.
        :rtype: list[:class:`huaweicloudsdkcce.v3.Clusters`]
        """
        return self._clusters

    @clusters.setter
    def clusters(self, clusters):
        """Sets the clusters of this CreateKubernetesClusterCertResponse.

        集群列表。

        :param clusters: The clusters of this CreateKubernetesClusterCertResponse.
        :type clusters: list[:class:`huaweicloudsdkcce.v3.Clusters`]
        """
        self._clusters = clusters

    @property
    def users(self):
        """Gets the users of this CreateKubernetesClusterCertResponse.

        存放了指定用户的一些证书信息和ClientKey信息。

        :return: The users of this CreateKubernetesClusterCertResponse.
        :rtype: list[:class:`huaweicloudsdkcce.v3.Users`]
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this CreateKubernetesClusterCertResponse.

        存放了指定用户的一些证书信息和ClientKey信息。

        :param users: The users of this CreateKubernetesClusterCertResponse.
        :type users: list[:class:`huaweicloudsdkcce.v3.Users`]
        """
        self._users = users

    @property
    def contexts(self):
        """Gets the contexts of this CreateKubernetesClusterCertResponse.

        上下文列表。

        :return: The contexts of this CreateKubernetesClusterCertResponse.
        :rtype: list[:class:`huaweicloudsdkcce.v3.Contexts`]
        """
        return self._contexts

    @contexts.setter
    def contexts(self, contexts):
        """Sets the contexts of this CreateKubernetesClusterCertResponse.

        上下文列表。

        :param contexts: The contexts of this CreateKubernetesClusterCertResponse.
        :type contexts: list[:class:`huaweicloudsdkcce.v3.Contexts`]
        """
        self._contexts = contexts

    @property
    def current_context(self):
        """Gets the current_context of this CreateKubernetesClusterCertResponse.

        当前上下文，若存在publicIp（虚拟机弹性IP）时为 external; 若不存在publicIp为 internal。

        :return: The current_context of this CreateKubernetesClusterCertResponse.
        :rtype: str
        """
        return self._current_context

    @current_context.setter
    def current_context(self, current_context):
        """Sets the current_context of this CreateKubernetesClusterCertResponse.

        当前上下文，若存在publicIp（虚拟机弹性IP）时为 external; 若不存在publicIp为 internal。

        :param current_context: The current_context of this CreateKubernetesClusterCertResponse.
        :type current_context: str
        """
        self._current_context = current_context

    @property
    def port_id(self):
        """Gets the port_id of this CreateKubernetesClusterCertResponse.


        :return: The port_id of this CreateKubernetesClusterCertResponse.
        :rtype: str
        """
        return self._port_id

    @port_id.setter
    def port_id(self, port_id):
        """Sets the port_id of this CreateKubernetesClusterCertResponse.


        :param port_id: The port_id of this CreateKubernetesClusterCertResponse.
        :type port_id: str
        """
        self._port_id = port_id

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
        if not isinstance(other, CreateKubernetesClusterCertResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
