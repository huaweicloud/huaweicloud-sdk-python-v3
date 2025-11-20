# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAutopilotKubernetesClusterCertResponse(SdkResponse):

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
        r"""CreateAutopilotKubernetesClusterCertResponse

        The model defined in huaweicloud sdk

        :param kind: **参数解释**： API类型 **约束限制**： 该值不可修改 **取值范围**： 不涉及 **默认取值**： Config 
        :type kind: str
        :param api_version: **参数解释**： API版本 **约束限制**： 该值不可修改 **取值范围**： 不涉及 **默认取值**： v1 
        :type api_version: str
        :param preferences: **参数解释**： 当前未使用该字段 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 默认为空 
        :type preferences: object
        :param clusters: **参数解释**： 集群列表。 **约束限制**： 不涉及 
        :type clusters: list[:class:`huaweicloudsdkcce.v3.Clusters`]
        :param users: **参数解释**： 存放了指定用户的一些证书信息和ClientKey信息。 **约束限制**： 不涉及 
        :type users: list[:class:`huaweicloudsdkcce.v3.Users`]
        :param contexts: **参数解释**： 上下文列表。 **约束限制**： 不涉及 
        :type contexts: list[:class:`huaweicloudsdkcce.v3.Contexts`]
        :param current_context: **参数解释**： 当前上下文 **约束限制**： 不涉及 **取值范围**： - external：公网访问  - internal：私网访问  **默认取值**： - 若存在publicIp（虚拟机弹性IP）时为 external。 - 若不存在publicIp为 internal。 
        :type current_context: str
        :param port_id: 
        :type port_id: str
        """
        
        super().__init__()

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
        r"""Gets the kind of this CreateAutopilotKubernetesClusterCertResponse.

        **参数解释**： API类型 **约束限制**： 该值不可修改 **取值范围**： 不涉及 **默认取值**： Config 

        :return: The kind of this CreateAutopilotKubernetesClusterCertResponse.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        r"""Sets the kind of this CreateAutopilotKubernetesClusterCertResponse.

        **参数解释**： API类型 **约束限制**： 该值不可修改 **取值范围**： 不涉及 **默认取值**： Config 

        :param kind: The kind of this CreateAutopilotKubernetesClusterCertResponse.
        :type kind: str
        """
        self._kind = kind

    @property
    def api_version(self):
        r"""Gets the api_version of this CreateAutopilotKubernetesClusterCertResponse.

        **参数解释**： API版本 **约束限制**： 该值不可修改 **取值范围**： 不涉及 **默认取值**： v1 

        :return: The api_version of this CreateAutopilotKubernetesClusterCertResponse.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        r"""Sets the api_version of this CreateAutopilotKubernetesClusterCertResponse.

        **参数解释**： API版本 **约束限制**： 该值不可修改 **取值范围**： 不涉及 **默认取值**： v1 

        :param api_version: The api_version of this CreateAutopilotKubernetesClusterCertResponse.
        :type api_version: str
        """
        self._api_version = api_version

    @property
    def preferences(self):
        r"""Gets the preferences of this CreateAutopilotKubernetesClusterCertResponse.

        **参数解释**： 当前未使用该字段 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 默认为空 

        :return: The preferences of this CreateAutopilotKubernetesClusterCertResponse.
        :rtype: object
        """
        return self._preferences

    @preferences.setter
    def preferences(self, preferences):
        r"""Sets the preferences of this CreateAutopilotKubernetesClusterCertResponse.

        **参数解释**： 当前未使用该字段 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 默认为空 

        :param preferences: The preferences of this CreateAutopilotKubernetesClusterCertResponse.
        :type preferences: object
        """
        self._preferences = preferences

    @property
    def clusters(self):
        r"""Gets the clusters of this CreateAutopilotKubernetesClusterCertResponse.

        **参数解释**： 集群列表。 **约束限制**： 不涉及 

        :return: The clusters of this CreateAutopilotKubernetesClusterCertResponse.
        :rtype: list[:class:`huaweicloudsdkcce.v3.Clusters`]
        """
        return self._clusters

    @clusters.setter
    def clusters(self, clusters):
        r"""Sets the clusters of this CreateAutopilotKubernetesClusterCertResponse.

        **参数解释**： 集群列表。 **约束限制**： 不涉及 

        :param clusters: The clusters of this CreateAutopilotKubernetesClusterCertResponse.
        :type clusters: list[:class:`huaweicloudsdkcce.v3.Clusters`]
        """
        self._clusters = clusters

    @property
    def users(self):
        r"""Gets the users of this CreateAutopilotKubernetesClusterCertResponse.

        **参数解释**： 存放了指定用户的一些证书信息和ClientKey信息。 **约束限制**： 不涉及 

        :return: The users of this CreateAutopilotKubernetesClusterCertResponse.
        :rtype: list[:class:`huaweicloudsdkcce.v3.Users`]
        """
        return self._users

    @users.setter
    def users(self, users):
        r"""Sets the users of this CreateAutopilotKubernetesClusterCertResponse.

        **参数解释**： 存放了指定用户的一些证书信息和ClientKey信息。 **约束限制**： 不涉及 

        :param users: The users of this CreateAutopilotKubernetesClusterCertResponse.
        :type users: list[:class:`huaweicloudsdkcce.v3.Users`]
        """
        self._users = users

    @property
    def contexts(self):
        r"""Gets the contexts of this CreateAutopilotKubernetesClusterCertResponse.

        **参数解释**： 上下文列表。 **约束限制**： 不涉及 

        :return: The contexts of this CreateAutopilotKubernetesClusterCertResponse.
        :rtype: list[:class:`huaweicloudsdkcce.v3.Contexts`]
        """
        return self._contexts

    @contexts.setter
    def contexts(self, contexts):
        r"""Sets the contexts of this CreateAutopilotKubernetesClusterCertResponse.

        **参数解释**： 上下文列表。 **约束限制**： 不涉及 

        :param contexts: The contexts of this CreateAutopilotKubernetesClusterCertResponse.
        :type contexts: list[:class:`huaweicloudsdkcce.v3.Contexts`]
        """
        self._contexts = contexts

    @property
    def current_context(self):
        r"""Gets the current_context of this CreateAutopilotKubernetesClusterCertResponse.

        **参数解释**： 当前上下文 **约束限制**： 不涉及 **取值范围**： - external：公网访问  - internal：私网访问  **默认取值**： - 若存在publicIp（虚拟机弹性IP）时为 external。 - 若不存在publicIp为 internal。 

        :return: The current_context of this CreateAutopilotKubernetesClusterCertResponse.
        :rtype: str
        """
        return self._current_context

    @current_context.setter
    def current_context(self, current_context):
        r"""Sets the current_context of this CreateAutopilotKubernetesClusterCertResponse.

        **参数解释**： 当前上下文 **约束限制**： 不涉及 **取值范围**： - external：公网访问  - internal：私网访问  **默认取值**： - 若存在publicIp（虚拟机弹性IP）时为 external。 - 若不存在publicIp为 internal。 

        :param current_context: The current_context of this CreateAutopilotKubernetesClusterCertResponse.
        :type current_context: str
        """
        self._current_context = current_context

    @property
    def port_id(self):
        r"""Gets the port_id of this CreateAutopilotKubernetesClusterCertResponse.

        :return: The port_id of this CreateAutopilotKubernetesClusterCertResponse.
        :rtype: str
        """
        return self._port_id

    @port_id.setter
    def port_id(self, port_id):
        r"""Sets the port_id of this CreateAutopilotKubernetesClusterCertResponse.

        :param port_id: The port_id of this CreateAutopilotKubernetesClusterCertResponse.
        :type port_id: str
        """
        self._port_id = port_id

    def to_dict(self):
        import warnings
        warnings.warn("CreateAutopilotKubernetesClusterCertResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, CreateAutopilotKubernetesClusterCertResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
