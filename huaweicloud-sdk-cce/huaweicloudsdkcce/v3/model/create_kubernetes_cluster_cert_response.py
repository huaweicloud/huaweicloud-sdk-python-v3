# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


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
        'api_version': 'str',
        'clusters': 'list[Clusters]',
        'contexts': 'list[Contexts]',
        'current_context': 'str',
        'kind': 'str',
        'preferences': 'object',
        'users': 'list[Users]'
    }

    attribute_map = {
        'api_version': 'apiVersion',
        'clusters': 'clusters',
        'contexts': 'contexts',
        'current_context': 'current-context',
        'kind': 'kind',
        'preferences': 'preferences',
        'users': 'users'
    }

    def __init__(self, api_version=None, clusters=None, contexts=None, current_context=None, kind='Config', preferences=None, users=None):
        """CreateKubernetesClusterCertResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._api_version = None
        self._clusters = None
        self._contexts = None
        self._current_context = None
        self._kind = None
        self._preferences = None
        self._users = None
        self.discriminator = None

        if api_version is not None:
            self.api_version = api_version
        if clusters is not None:
            self.clusters = clusters
        if contexts is not None:
            self.contexts = contexts
        if current_context is not None:
            self.current_context = current_context
        if kind is not None:
            self.kind = kind
        if preferences is not None:
            self.preferences = preferences
        if users is not None:
            self.users = users

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
        :type: str
        """
        self._api_version = api_version

    @property
    def clusters(self):
        """Gets the clusters of this CreateKubernetesClusterCertResponse.

        集群列表。

        :return: The clusters of this CreateKubernetesClusterCertResponse.
        :rtype: list[Clusters]
        """
        return self._clusters

    @clusters.setter
    def clusters(self, clusters):
        """Sets the clusters of this CreateKubernetesClusterCertResponse.

        集群列表。

        :param clusters: The clusters of this CreateKubernetesClusterCertResponse.
        :type: list[Clusters]
        """
        self._clusters = clusters

    @property
    def contexts(self):
        """Gets the contexts of this CreateKubernetesClusterCertResponse.

        上下文列表。

        :return: The contexts of this CreateKubernetesClusterCertResponse.
        :rtype: list[Contexts]
        """
        return self._contexts

    @contexts.setter
    def contexts(self, contexts):
        """Sets the contexts of this CreateKubernetesClusterCertResponse.

        上下文列表。

        :param contexts: The contexts of this CreateKubernetesClusterCertResponse.
        :type: list[Contexts]
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
        :type: str
        """
        self._current_context = current_context

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
        :type: str
        """
        self._kind = kind

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
        :type: object
        """
        self._preferences = preferences

    @property
    def users(self):
        """Gets the users of this CreateKubernetesClusterCertResponse.

        存放了指定用户的一些证书信息和ClientKey信息。

        :return: The users of this CreateKubernetesClusterCertResponse.
        :rtype: list[Users]
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this CreateKubernetesClusterCertResponse.

        存放了指定用户的一些证书信息和ClientKey信息。

        :param users: The users of this CreateKubernetesClusterCertResponse.
        :type: list[Users]
        """
        self._users = users

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateKubernetesClusterCertResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
