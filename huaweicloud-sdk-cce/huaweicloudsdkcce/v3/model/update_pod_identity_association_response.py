# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdatePodIdentityAssociationResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'uid': 'str',
        'cluster_id': 'str',
        'namespace': 'str',
        'service_account': 'str',
        'agency_name': 'str',
        'tags': 'list[ResourceTag]',
        'created_at': 'str',
        'modified_at': 'str'
    }

    attribute_map = {
        'uid': 'uid',
        'cluster_id': 'clusterId',
        'namespace': 'namespace',
        'service_account': 'serviceAccount',
        'agency_name': 'agencyName',
        'tags': 'tags',
        'created_at': 'createdAt',
        'modified_at': 'modifiedAt'
    }

    def __init__(self, uid=None, cluster_id=None, namespace=None, service_account=None, agency_name=None, tags=None, created_at=None, modified_at=None):
        r"""UpdatePodIdentityAssociationResponse

        The model defined in huaweicloud sdk

        :param uid: **参数解释：** pod-identity关联的uid。 **约束限制：** 该值不可修改 **取值范围：** 不涉及 **默认取值：** 无
        :type uid: str
        :param cluster_id: **参数解释：** pod-identity关联所属的集群id。 **约束限制：** 该值不可修改 **取值范围：** 不涉及 **默认取值：** 无
        :type cluster_id: str
        :param namespace: **参数解释：** pod-identity关联所要绑定的serviceaccount所属的命名空间。 **约束限制：** 该值不可修改 **取值范围：** 不涉及 **默认取值：** 无
        :type namespace: str
        :param service_account: **参数解释：** pod-identity关联所要绑定的serviceaccount名称。 **约束限制：** 该值不可修改 **取值范围：** 不涉及 **默认取值：** 无
        :type service_account: str
        :param agency_name: **参数解释：** pod-identity关联所要绑定的委托名称。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 无
        :type agency_name: str
        :param tags: **参数解释：** pod-identity关联的资源标签列表。 **约束限制：** 不涉及 
        :type tags: list[:class:`huaweicloudsdkcce.v3.ResourceTag`]
        :param created_at: **参数解释：** pod-identity关联创建时间。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 无
        :type created_at: str
        :param modified_at: **参数解释：** pod-identity关联最近一次更新时间。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 无
        :type modified_at: str
        """
        
        super().__init__()

        self._uid = None
        self._cluster_id = None
        self._namespace = None
        self._service_account = None
        self._agency_name = None
        self._tags = None
        self._created_at = None
        self._modified_at = None
        self.discriminator = None

        if uid is not None:
            self.uid = uid
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if namespace is not None:
            self.namespace = namespace
        if service_account is not None:
            self.service_account = service_account
        if agency_name is not None:
            self.agency_name = agency_name
        if tags is not None:
            self.tags = tags
        if created_at is not None:
            self.created_at = created_at
        if modified_at is not None:
            self.modified_at = modified_at

    @property
    def uid(self):
        r"""Gets the uid of this UpdatePodIdentityAssociationResponse.

        **参数解释：** pod-identity关联的uid。 **约束限制：** 该值不可修改 **取值范围：** 不涉及 **默认取值：** 无

        :return: The uid of this UpdatePodIdentityAssociationResponse.
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        r"""Sets the uid of this UpdatePodIdentityAssociationResponse.

        **参数解释：** pod-identity关联的uid。 **约束限制：** 该值不可修改 **取值范围：** 不涉及 **默认取值：** 无

        :param uid: The uid of this UpdatePodIdentityAssociationResponse.
        :type uid: str
        """
        self._uid = uid

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this UpdatePodIdentityAssociationResponse.

        **参数解释：** pod-identity关联所属的集群id。 **约束限制：** 该值不可修改 **取值范围：** 不涉及 **默认取值：** 无

        :return: The cluster_id of this UpdatePodIdentityAssociationResponse.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this UpdatePodIdentityAssociationResponse.

        **参数解释：** pod-identity关联所属的集群id。 **约束限制：** 该值不可修改 **取值范围：** 不涉及 **默认取值：** 无

        :param cluster_id: The cluster_id of this UpdatePodIdentityAssociationResponse.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def namespace(self):
        r"""Gets the namespace of this UpdatePodIdentityAssociationResponse.

        **参数解释：** pod-identity关联所要绑定的serviceaccount所属的命名空间。 **约束限制：** 该值不可修改 **取值范围：** 不涉及 **默认取值：** 无

        :return: The namespace of this UpdatePodIdentityAssociationResponse.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this UpdatePodIdentityAssociationResponse.

        **参数解释：** pod-identity关联所要绑定的serviceaccount所属的命名空间。 **约束限制：** 该值不可修改 **取值范围：** 不涉及 **默认取值：** 无

        :param namespace: The namespace of this UpdatePodIdentityAssociationResponse.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def service_account(self):
        r"""Gets the service_account of this UpdatePodIdentityAssociationResponse.

        **参数解释：** pod-identity关联所要绑定的serviceaccount名称。 **约束限制：** 该值不可修改 **取值范围：** 不涉及 **默认取值：** 无

        :return: The service_account of this UpdatePodIdentityAssociationResponse.
        :rtype: str
        """
        return self._service_account

    @service_account.setter
    def service_account(self, service_account):
        r"""Sets the service_account of this UpdatePodIdentityAssociationResponse.

        **参数解释：** pod-identity关联所要绑定的serviceaccount名称。 **约束限制：** 该值不可修改 **取值范围：** 不涉及 **默认取值：** 无

        :param service_account: The service_account of this UpdatePodIdentityAssociationResponse.
        :type service_account: str
        """
        self._service_account = service_account

    @property
    def agency_name(self):
        r"""Gets the agency_name of this UpdatePodIdentityAssociationResponse.

        **参数解释：** pod-identity关联所要绑定的委托名称。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 无

        :return: The agency_name of this UpdatePodIdentityAssociationResponse.
        :rtype: str
        """
        return self._agency_name

    @agency_name.setter
    def agency_name(self, agency_name):
        r"""Sets the agency_name of this UpdatePodIdentityAssociationResponse.

        **参数解释：** pod-identity关联所要绑定的委托名称。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 无

        :param agency_name: The agency_name of this UpdatePodIdentityAssociationResponse.
        :type agency_name: str
        """
        self._agency_name = agency_name

    @property
    def tags(self):
        r"""Gets the tags of this UpdatePodIdentityAssociationResponse.

        **参数解释：** pod-identity关联的资源标签列表。 **约束限制：** 不涉及 

        :return: The tags of this UpdatePodIdentityAssociationResponse.
        :rtype: list[:class:`huaweicloudsdkcce.v3.ResourceTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this UpdatePodIdentityAssociationResponse.

        **参数解释：** pod-identity关联的资源标签列表。 **约束限制：** 不涉及 

        :param tags: The tags of this UpdatePodIdentityAssociationResponse.
        :type tags: list[:class:`huaweicloudsdkcce.v3.ResourceTag`]
        """
        self._tags = tags

    @property
    def created_at(self):
        r"""Gets the created_at of this UpdatePodIdentityAssociationResponse.

        **参数解释：** pod-identity关联创建时间。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 无

        :return: The created_at of this UpdatePodIdentityAssociationResponse.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this UpdatePodIdentityAssociationResponse.

        **参数解释：** pod-identity关联创建时间。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 无

        :param created_at: The created_at of this UpdatePodIdentityAssociationResponse.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def modified_at(self):
        r"""Gets the modified_at of this UpdatePodIdentityAssociationResponse.

        **参数解释：** pod-identity关联最近一次更新时间。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 无

        :return: The modified_at of this UpdatePodIdentityAssociationResponse.
        :rtype: str
        """
        return self._modified_at

    @modified_at.setter
    def modified_at(self, modified_at):
        r"""Sets the modified_at of this UpdatePodIdentityAssociationResponse.

        **参数解释：** pod-identity关联最近一次更新时间。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 无

        :param modified_at: The modified_at of this UpdatePodIdentityAssociationResponse.
        :type modified_at: str
        """
        self._modified_at = modified_at

    def to_dict(self):
        import warnings
        warnings.warn("UpdatePodIdentityAssociationResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, UpdatePodIdentityAssociationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
