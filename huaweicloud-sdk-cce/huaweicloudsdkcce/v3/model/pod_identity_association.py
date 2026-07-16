# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PodIdentityAssociation:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'namespace': 'str',
        'service_account': 'str',
        'agency_name': 'str',
        'tags': 'list[ResourceTag]'
    }

    attribute_map = {
        'namespace': 'namespace',
        'service_account': 'serviceAccount',
        'agency_name': 'agencyName',
        'tags': 'tags'
    }

    def __init__(self, namespace=None, service_account=None, agency_name=None, tags=None):
        r"""PodIdentityAssociation

        The model defined in huaweicloud sdk

        :param namespace: **参数解释：** pod-identity关联所要绑定的serviceaccount所属的命名空间。 **约束限制：** 该值不可修改 **取值范围：** 不涉及 **默认取值：** 无
        :type namespace: str
        :param service_account: **参数解释：** pod-identity关联所要绑定的serviceaccount名称。 **约束限制：** 同一个serviceaccount最多创建一条pod-identity关联记录，不支持创建多个 **取值范围：** 不涉及 **默认取值：** 无
        :type service_account: str
        :param agency_name: **参数解释：** pod-identity关联所要绑定的委托名称，委托可以是一般委托或信任委托。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 无
        :type agency_name: str
        :param tags: **参数解释：** pod-identity关联的资源标签列表。 **约束限制：** 不涉及 
        :type tags: list[:class:`huaweicloudsdkcce.v3.ResourceTag`]
        """
        
        

        self._namespace = None
        self._service_account = None
        self._agency_name = None
        self._tags = None
        self.discriminator = None

        self.namespace = namespace
        self.service_account = service_account
        self.agency_name = agency_name
        if tags is not None:
            self.tags = tags

    @property
    def namespace(self):
        r"""Gets the namespace of this PodIdentityAssociation.

        **参数解释：** pod-identity关联所要绑定的serviceaccount所属的命名空间。 **约束限制：** 该值不可修改 **取值范围：** 不涉及 **默认取值：** 无

        :return: The namespace of this PodIdentityAssociation.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this PodIdentityAssociation.

        **参数解释：** pod-identity关联所要绑定的serviceaccount所属的命名空间。 **约束限制：** 该值不可修改 **取值范围：** 不涉及 **默认取值：** 无

        :param namespace: The namespace of this PodIdentityAssociation.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def service_account(self):
        r"""Gets the service_account of this PodIdentityAssociation.

        **参数解释：** pod-identity关联所要绑定的serviceaccount名称。 **约束限制：** 同一个serviceaccount最多创建一条pod-identity关联记录，不支持创建多个 **取值范围：** 不涉及 **默认取值：** 无

        :return: The service_account of this PodIdentityAssociation.
        :rtype: str
        """
        return self._service_account

    @service_account.setter
    def service_account(self, service_account):
        r"""Sets the service_account of this PodIdentityAssociation.

        **参数解释：** pod-identity关联所要绑定的serviceaccount名称。 **约束限制：** 同一个serviceaccount最多创建一条pod-identity关联记录，不支持创建多个 **取值范围：** 不涉及 **默认取值：** 无

        :param service_account: The service_account of this PodIdentityAssociation.
        :type service_account: str
        """
        self._service_account = service_account

    @property
    def agency_name(self):
        r"""Gets the agency_name of this PodIdentityAssociation.

        **参数解释：** pod-identity关联所要绑定的委托名称，委托可以是一般委托或信任委托。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 无

        :return: The agency_name of this PodIdentityAssociation.
        :rtype: str
        """
        return self._agency_name

    @agency_name.setter
    def agency_name(self, agency_name):
        r"""Sets the agency_name of this PodIdentityAssociation.

        **参数解释：** pod-identity关联所要绑定的委托名称，委托可以是一般委托或信任委托。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 无

        :param agency_name: The agency_name of this PodIdentityAssociation.
        :type agency_name: str
        """
        self._agency_name = agency_name

    @property
    def tags(self):
        r"""Gets the tags of this PodIdentityAssociation.

        **参数解释：** pod-identity关联的资源标签列表。 **约束限制：** 不涉及 

        :return: The tags of this PodIdentityAssociation.
        :rtype: list[:class:`huaweicloudsdkcce.v3.ResourceTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this PodIdentityAssociation.

        **参数解释：** pod-identity关联的资源标签列表。 **约束限制：** 不涉及 

        :param tags: The tags of this PodIdentityAssociation.
        :type tags: list[:class:`huaweicloudsdkcce.v3.ResourceTag`]
        """
        self._tags = tags

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
        if not isinstance(other, PodIdentityAssociation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
