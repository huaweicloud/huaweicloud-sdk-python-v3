# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AccessPolicyResp:

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
        'policy_id': 'str',
        'clusters': 'list[str]',
        'access_scope': 'AccessScope',
        'policy_type': 'str',
        'principal': 'Principal',
        'create_time': 'datetime',
        'update_time': 'datetime'
    }

    attribute_map = {
        'kind': 'kind',
        'api_version': 'apiVersion',
        'name': 'name',
        'policy_id': 'policyId',
        'clusters': 'clusters',
        'access_scope': 'accessScope',
        'policy_type': 'policyType',
        'principal': 'principal',
        'create_time': 'createTime',
        'update_time': 'updateTime'
    }

    def __init__(self, kind=None, api_version=None, name=None, policy_id=None, clusters=None, access_scope=None, policy_type=None, principal=None, create_time=None, update_time=None):
        r"""AccessPolicyResp

        The model defined in huaweicloud sdk

        :param kind: **参数解释：** API类型。 **约束限制：** 该值不可修改。 **取值范围：** 不涉及 **默认取值：** AccessPolicy
        :type kind: str
        :param api_version: **参数解释：** API版本。 **约束限制：** 该值不可修改。 **取值范围：** 不涉及 **默认取值：** v3
        :type api_version: str
        :param name: **参数解释：** 访问策略名称。 **约束限制：** 以小写字母开头，由小写字母、数字、中划线(-)、点(.)组成，长度范围1-56位，且不能以中划线(-)结尾。 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type name: str
        :param policy_id: **参数解释：** 权限ID。 **约束限制：** 系统自动生成，该值不可修改。 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type policy_id: str
        :param clusters: **参数解释：** 集群ID的列表，允许使用通配符（“\\*”），表示所有集群。 **约束限制：** 当前最多支持同时授权200个集群。 **取值范围：** \\[\&quot;\\*\&quot;\\]或者集群ID列表。 **默认取值：** 不涉及
        :type clusters: list[str]
        :param access_scope: 
        :type access_scope: :class:`huaweicloudsdkcce.v3.AccessScope`
        :param policy_type: **参数解释：** 权限类型。 **约束限制：** 不涉及 **取值范围：** - CCEClusterAdminPolicy：管理员权限 - CCEAdminPolicy：运维权限 - CCEEditPolicy：开发权限 - CCEViewPolicy：只读权限  **默认取值：** 不涉及
        :type policy_type: str
        :param principal: 
        :type principal: :class:`huaweicloudsdkcce.v3.Principal`
        :param create_time: **参数解释：** 创建时间。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type create_time: datetime
        :param update_time: **参数解释：** 更新时间。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type update_time: datetime
        """
        
        

        self._kind = None
        self._api_version = None
        self._name = None
        self._policy_id = None
        self._clusters = None
        self._access_scope = None
        self._policy_type = None
        self._principal = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if kind is not None:
            self.kind = kind
        if api_version is not None:
            self.api_version = api_version
        if name is not None:
            self.name = name
        if policy_id is not None:
            self.policy_id = policy_id
        if clusters is not None:
            self.clusters = clusters
        if access_scope is not None:
            self.access_scope = access_scope
        if policy_type is not None:
            self.policy_type = policy_type
        if principal is not None:
            self.principal = principal
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def kind(self):
        r"""Gets the kind of this AccessPolicyResp.

        **参数解释：** API类型。 **约束限制：** 该值不可修改。 **取值范围：** 不涉及 **默认取值：** AccessPolicy

        :return: The kind of this AccessPolicyResp.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        r"""Sets the kind of this AccessPolicyResp.

        **参数解释：** API类型。 **约束限制：** 该值不可修改。 **取值范围：** 不涉及 **默认取值：** AccessPolicy

        :param kind: The kind of this AccessPolicyResp.
        :type kind: str
        """
        self._kind = kind

    @property
    def api_version(self):
        r"""Gets the api_version of this AccessPolicyResp.

        **参数解释：** API版本。 **约束限制：** 该值不可修改。 **取值范围：** 不涉及 **默认取值：** v3

        :return: The api_version of this AccessPolicyResp.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        r"""Sets the api_version of this AccessPolicyResp.

        **参数解释：** API版本。 **约束限制：** 该值不可修改。 **取值范围：** 不涉及 **默认取值：** v3

        :param api_version: The api_version of this AccessPolicyResp.
        :type api_version: str
        """
        self._api_version = api_version

    @property
    def name(self):
        r"""Gets the name of this AccessPolicyResp.

        **参数解释：** 访问策略名称。 **约束限制：** 以小写字母开头，由小写字母、数字、中划线(-)、点(.)组成，长度范围1-56位，且不能以中划线(-)结尾。 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The name of this AccessPolicyResp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this AccessPolicyResp.

        **参数解释：** 访问策略名称。 **约束限制：** 以小写字母开头，由小写字母、数字、中划线(-)、点(.)组成，长度范围1-56位，且不能以中划线(-)结尾。 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param name: The name of this AccessPolicyResp.
        :type name: str
        """
        self._name = name

    @property
    def policy_id(self):
        r"""Gets the policy_id of this AccessPolicyResp.

        **参数解释：** 权限ID。 **约束限制：** 系统自动生成，该值不可修改。 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The policy_id of this AccessPolicyResp.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        r"""Sets the policy_id of this AccessPolicyResp.

        **参数解释：** 权限ID。 **约束限制：** 系统自动生成，该值不可修改。 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param policy_id: The policy_id of this AccessPolicyResp.
        :type policy_id: str
        """
        self._policy_id = policy_id

    @property
    def clusters(self):
        r"""Gets the clusters of this AccessPolicyResp.

        **参数解释：** 集群ID的列表，允许使用通配符（“\\*”），表示所有集群。 **约束限制：** 当前最多支持同时授权200个集群。 **取值范围：** \\[\"\\*\"\\]或者集群ID列表。 **默认取值：** 不涉及

        :return: The clusters of this AccessPolicyResp.
        :rtype: list[str]
        """
        return self._clusters

    @clusters.setter
    def clusters(self, clusters):
        r"""Sets the clusters of this AccessPolicyResp.

        **参数解释：** 集群ID的列表，允许使用通配符（“\\*”），表示所有集群。 **约束限制：** 当前最多支持同时授权200个集群。 **取值范围：** \\[\"\\*\"\\]或者集群ID列表。 **默认取值：** 不涉及

        :param clusters: The clusters of this AccessPolicyResp.
        :type clusters: list[str]
        """
        self._clusters = clusters

    @property
    def access_scope(self):
        r"""Gets the access_scope of this AccessPolicyResp.

        :return: The access_scope of this AccessPolicyResp.
        :rtype: :class:`huaweicloudsdkcce.v3.AccessScope`
        """
        return self._access_scope

    @access_scope.setter
    def access_scope(self, access_scope):
        r"""Sets the access_scope of this AccessPolicyResp.

        :param access_scope: The access_scope of this AccessPolicyResp.
        :type access_scope: :class:`huaweicloudsdkcce.v3.AccessScope`
        """
        self._access_scope = access_scope

    @property
    def policy_type(self):
        r"""Gets the policy_type of this AccessPolicyResp.

        **参数解释：** 权限类型。 **约束限制：** 不涉及 **取值范围：** - CCEClusterAdminPolicy：管理员权限 - CCEAdminPolicy：运维权限 - CCEEditPolicy：开发权限 - CCEViewPolicy：只读权限  **默认取值：** 不涉及

        :return: The policy_type of this AccessPolicyResp.
        :rtype: str
        """
        return self._policy_type

    @policy_type.setter
    def policy_type(self, policy_type):
        r"""Sets the policy_type of this AccessPolicyResp.

        **参数解释：** 权限类型。 **约束限制：** 不涉及 **取值范围：** - CCEClusterAdminPolicy：管理员权限 - CCEAdminPolicy：运维权限 - CCEEditPolicy：开发权限 - CCEViewPolicy：只读权限  **默认取值：** 不涉及

        :param policy_type: The policy_type of this AccessPolicyResp.
        :type policy_type: str
        """
        self._policy_type = policy_type

    @property
    def principal(self):
        r"""Gets the principal of this AccessPolicyResp.

        :return: The principal of this AccessPolicyResp.
        :rtype: :class:`huaweicloudsdkcce.v3.Principal`
        """
        return self._principal

    @principal.setter
    def principal(self, principal):
        r"""Sets the principal of this AccessPolicyResp.

        :param principal: The principal of this AccessPolicyResp.
        :type principal: :class:`huaweicloudsdkcce.v3.Principal`
        """
        self._principal = principal

    @property
    def create_time(self):
        r"""Gets the create_time of this AccessPolicyResp.

        **参数解释：** 创建时间。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The create_time of this AccessPolicyResp.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this AccessPolicyResp.

        **参数解释：** 创建时间。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param create_time: The create_time of this AccessPolicyResp.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this AccessPolicyResp.

        **参数解释：** 更新时间。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The update_time of this AccessPolicyResp.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this AccessPolicyResp.

        **参数解释：** 更新时间。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param update_time: The update_time of this AccessPolicyResp.
        :type update_time: datetime
        """
        self._update_time = update_time

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
        if not isinstance(other, AccessPolicyResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
