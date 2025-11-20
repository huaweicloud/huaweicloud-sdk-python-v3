# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AccessPolicy:

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
        'name': 'str',
        'clusters': 'list[str]',
        'access_scope': 'AccessScope',
        'policy_type': 'str',
        'principal': 'Principal'
    }

    attribute_map = {
        'kind': 'kind',
        'api_version': 'apiVersion',
        'name': 'name',
        'clusters': 'clusters',
        'access_scope': 'accessScope',
        'policy_type': 'policyType',
        'principal': 'principal'
    }

    def __init__(self, kind=None, api_version=None, name=None, clusters=None, access_scope=None, policy_type=None, principal=None):
        r"""AccessPolicy

        The model defined in huaweicloud sdk

        :param kind: **参数解释：** API类型。 **约束限制：** 该值不可修改 **取值范围：** 不涉及 **默认取值：** AccessPolicy
        :type kind: str
        :param api_version: **参数解释：** API版本。 **约束限制：** 该值不可修改 **取值范围：** 不涉及 **默认取值：** v3
        :type api_version: str
        :param name: **参数解释：** 访问策略名称。 **约束限制：** 以小写字母开头，由小写字母、数字、中划线(-)、点(.)组成，长度范围1-56位，且不能以中划线(-)结尾。 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type name: str
        :param clusters: **参数解释：** 集群ID的列表，允许使用通配符（“\\*”），表示所有集群。获取方式请参见[如何获取接口URI中参数](cce_02_0271.xml)。 **约束限制：** 当前最多支持同时授权200个集群。 **取值范围：** \\[\&quot;\\*\&quot;\\]或者集群ID列表。 **默认取值：** 不涉及
        :type clusters: list[str]
        :param access_scope: 
        :type access_scope: :class:`huaweicloudsdkcce.v3.AccessScope`
        :param policy_type: **参数解释：** 权限类型。 **约束限制：** 不涉及 **取值范围：** - CCEClusterAdminPolicy：管理员权限 - CCEAdminPolicy：运维权限 - CCEEditPolicy：开发权限 - CCEViewPolicy：只读权限  **默认取值：** 不涉及
        :type policy_type: str
        :param principal: 
        :type principal: :class:`huaweicloudsdkcce.v3.Principal`
        """
        
        

        self._kind = None
        self._api_version = None
        self._name = None
        self._clusters = None
        self._access_scope = None
        self._policy_type = None
        self._principal = None
        self.discriminator = None

        if kind is not None:
            self.kind = kind
        if api_version is not None:
            self.api_version = api_version
        if name is not None:
            self.name = name
        self.clusters = clusters
        self.access_scope = access_scope
        self.policy_type = policy_type
        self.principal = principal

    @property
    def kind(self):
        r"""Gets the kind of this AccessPolicy.

        **参数解释：** API类型。 **约束限制：** 该值不可修改 **取值范围：** 不涉及 **默认取值：** AccessPolicy

        :return: The kind of this AccessPolicy.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        r"""Sets the kind of this AccessPolicy.

        **参数解释：** API类型。 **约束限制：** 该值不可修改 **取值范围：** 不涉及 **默认取值：** AccessPolicy

        :param kind: The kind of this AccessPolicy.
        :type kind: str
        """
        self._kind = kind

    @property
    def api_version(self):
        r"""Gets the api_version of this AccessPolicy.

        **参数解释：** API版本。 **约束限制：** 该值不可修改 **取值范围：** 不涉及 **默认取值：** v3

        :return: The api_version of this AccessPolicy.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        r"""Sets the api_version of this AccessPolicy.

        **参数解释：** API版本。 **约束限制：** 该值不可修改 **取值范围：** 不涉及 **默认取值：** v3

        :param api_version: The api_version of this AccessPolicy.
        :type api_version: str
        """
        self._api_version = api_version

    @property
    def name(self):
        r"""Gets the name of this AccessPolicy.

        **参数解释：** 访问策略名称。 **约束限制：** 以小写字母开头，由小写字母、数字、中划线(-)、点(.)组成，长度范围1-56位，且不能以中划线(-)结尾。 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The name of this AccessPolicy.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this AccessPolicy.

        **参数解释：** 访问策略名称。 **约束限制：** 以小写字母开头，由小写字母、数字、中划线(-)、点(.)组成，长度范围1-56位，且不能以中划线(-)结尾。 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param name: The name of this AccessPolicy.
        :type name: str
        """
        self._name = name

    @property
    def clusters(self):
        r"""Gets the clusters of this AccessPolicy.

        **参数解释：** 集群ID的列表，允许使用通配符（“\\*”），表示所有集群。获取方式请参见[如何获取接口URI中参数](cce_02_0271.xml)。 **约束限制：** 当前最多支持同时授权200个集群。 **取值范围：** \\[\"\\*\"\\]或者集群ID列表。 **默认取值：** 不涉及

        :return: The clusters of this AccessPolicy.
        :rtype: list[str]
        """
        return self._clusters

    @clusters.setter
    def clusters(self, clusters):
        r"""Sets the clusters of this AccessPolicy.

        **参数解释：** 集群ID的列表，允许使用通配符（“\\*”），表示所有集群。获取方式请参见[如何获取接口URI中参数](cce_02_0271.xml)。 **约束限制：** 当前最多支持同时授权200个集群。 **取值范围：** \\[\"\\*\"\\]或者集群ID列表。 **默认取值：** 不涉及

        :param clusters: The clusters of this AccessPolicy.
        :type clusters: list[str]
        """
        self._clusters = clusters

    @property
    def access_scope(self):
        r"""Gets the access_scope of this AccessPolicy.

        :return: The access_scope of this AccessPolicy.
        :rtype: :class:`huaweicloudsdkcce.v3.AccessScope`
        """
        return self._access_scope

    @access_scope.setter
    def access_scope(self, access_scope):
        r"""Sets the access_scope of this AccessPolicy.

        :param access_scope: The access_scope of this AccessPolicy.
        :type access_scope: :class:`huaweicloudsdkcce.v3.AccessScope`
        """
        self._access_scope = access_scope

    @property
    def policy_type(self):
        r"""Gets the policy_type of this AccessPolicy.

        **参数解释：** 权限类型。 **约束限制：** 不涉及 **取值范围：** - CCEClusterAdminPolicy：管理员权限 - CCEAdminPolicy：运维权限 - CCEEditPolicy：开发权限 - CCEViewPolicy：只读权限  **默认取值：** 不涉及

        :return: The policy_type of this AccessPolicy.
        :rtype: str
        """
        return self._policy_type

    @policy_type.setter
    def policy_type(self, policy_type):
        r"""Sets the policy_type of this AccessPolicy.

        **参数解释：** 权限类型。 **约束限制：** 不涉及 **取值范围：** - CCEClusterAdminPolicy：管理员权限 - CCEAdminPolicy：运维权限 - CCEEditPolicy：开发权限 - CCEViewPolicy：只读权限  **默认取值：** 不涉及

        :param policy_type: The policy_type of this AccessPolicy.
        :type policy_type: str
        """
        self._policy_type = policy_type

    @property
    def principal(self):
        r"""Gets the principal of this AccessPolicy.

        :return: The principal of this AccessPolicy.
        :rtype: :class:`huaweicloudsdkcce.v3.Principal`
        """
        return self._principal

    @principal.setter
    def principal(self, principal):
        r"""Sets the principal of this AccessPolicy.

        :param principal: The principal of this AccessPolicy.
        :type principal: :class:`huaweicloudsdkcce.v3.Principal`
        """
        self._principal = principal

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
        if not isinstance(other, AccessPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
