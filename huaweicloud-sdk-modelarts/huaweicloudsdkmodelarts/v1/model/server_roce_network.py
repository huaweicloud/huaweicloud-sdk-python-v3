# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ServerRoceNetwork:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'project_id': 'str',
        'status': 'str',
        'tenant_id': 'str',
        'subnets': 'str',
        'providernetwork_type': 'str',
        'providerphysical_network': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'project_id': 'project_id',
        'status': 'status',
        'tenant_id': 'tenant_id',
        'subnets': 'subnets',
        'providernetwork_type': 'provider:network_type',
        'providerphysical_network': 'provider:physical_network'
    }

    def __init__(self, id=None, name=None, project_id=None, status=None, tenant_id=None, subnets=None, providernetwork_type=None, providerphysical_network=None):
        r"""ServerRoceNetwork

        The model defined in huaweicloud sdk

        :param id: **参数解释**：RoCE网络id。 **取值范围**：不涉及。
        :type id: str
        :param name: **参数解释**：RoCE网络名称。 **取值范围**：不涉及。
        :type name: str
        :param project_id: **参数解释**：项目ID。 **取值范围**：不涉及。
        :type project_id: str
        :param status: **参数解释**：状态。 **参数解释**：不涉及。
        :type status: str
        :param tenant_id: **参数解释**：租户id。 **取值范围**：不涉及。
        :type tenant_id: str
        :param subnets: **参数解释**：子网。 **取值范围**：不涉及。
        :type subnets: str
        :param providernetwork_type: **参数解释**：RoCE网络类型。 **取值范围**：不涉及。
        :type providernetwork_type: str
        :param providerphysical_network: **参数解释**：实际物理网络。 **取值范围**：不涉及。
        :type providerphysical_network: str
        """
        
        

        self._id = None
        self._name = None
        self._project_id = None
        self._status = None
        self._tenant_id = None
        self._subnets = None
        self._providernetwork_type = None
        self._providerphysical_network = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if project_id is not None:
            self.project_id = project_id
        if status is not None:
            self.status = status
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if subnets is not None:
            self.subnets = subnets
        if providernetwork_type is not None:
            self.providernetwork_type = providernetwork_type
        if providerphysical_network is not None:
            self.providerphysical_network = providerphysical_network

    @property
    def id(self):
        r"""Gets the id of this ServerRoceNetwork.

        **参数解释**：RoCE网络id。 **取值范围**：不涉及。

        :return: The id of this ServerRoceNetwork.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ServerRoceNetwork.

        **参数解释**：RoCE网络id。 **取值范围**：不涉及。

        :param id: The id of this ServerRoceNetwork.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ServerRoceNetwork.

        **参数解释**：RoCE网络名称。 **取值范围**：不涉及。

        :return: The name of this ServerRoceNetwork.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ServerRoceNetwork.

        **参数解释**：RoCE网络名称。 **取值范围**：不涉及。

        :param name: The name of this ServerRoceNetwork.
        :type name: str
        """
        self._name = name

    @property
    def project_id(self):
        r"""Gets the project_id of this ServerRoceNetwork.

        **参数解释**：项目ID。 **取值范围**：不涉及。

        :return: The project_id of this ServerRoceNetwork.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ServerRoceNetwork.

        **参数解释**：项目ID。 **取值范围**：不涉及。

        :param project_id: The project_id of this ServerRoceNetwork.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def status(self):
        r"""Gets the status of this ServerRoceNetwork.

        **参数解释**：状态。 **参数解释**：不涉及。

        :return: The status of this ServerRoceNetwork.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ServerRoceNetwork.

        **参数解释**：状态。 **参数解释**：不涉及。

        :param status: The status of this ServerRoceNetwork.
        :type status: str
        """
        self._status = status

    @property
    def tenant_id(self):
        r"""Gets the tenant_id of this ServerRoceNetwork.

        **参数解释**：租户id。 **取值范围**：不涉及。

        :return: The tenant_id of this ServerRoceNetwork.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        r"""Sets the tenant_id of this ServerRoceNetwork.

        **参数解释**：租户id。 **取值范围**：不涉及。

        :param tenant_id: The tenant_id of this ServerRoceNetwork.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def subnets(self):
        r"""Gets the subnets of this ServerRoceNetwork.

        **参数解释**：子网。 **取值范围**：不涉及。

        :return: The subnets of this ServerRoceNetwork.
        :rtype: str
        """
        return self._subnets

    @subnets.setter
    def subnets(self, subnets):
        r"""Sets the subnets of this ServerRoceNetwork.

        **参数解释**：子网。 **取值范围**：不涉及。

        :param subnets: The subnets of this ServerRoceNetwork.
        :type subnets: str
        """
        self._subnets = subnets

    @property
    def providernetwork_type(self):
        r"""Gets the providernetwork_type of this ServerRoceNetwork.

        **参数解释**：RoCE网络类型。 **取值范围**：不涉及。

        :return: The providernetwork_type of this ServerRoceNetwork.
        :rtype: str
        """
        return self._providernetwork_type

    @providernetwork_type.setter
    def providernetwork_type(self, providernetwork_type):
        r"""Sets the providernetwork_type of this ServerRoceNetwork.

        **参数解释**：RoCE网络类型。 **取值范围**：不涉及。

        :param providernetwork_type: The providernetwork_type of this ServerRoceNetwork.
        :type providernetwork_type: str
        """
        self._providernetwork_type = providernetwork_type

    @property
    def providerphysical_network(self):
        r"""Gets the providerphysical_network of this ServerRoceNetwork.

        **参数解释**：实际物理网络。 **取值范围**：不涉及。

        :return: The providerphysical_network of this ServerRoceNetwork.
        :rtype: str
        """
        return self._providerphysical_network

    @providerphysical_network.setter
    def providerphysical_network(self, providerphysical_network):
        r"""Sets the providerphysical_network of this ServerRoceNetwork.

        **参数解释**：实际物理网络。 **取值范围**：不涉及。

        :param providerphysical_network: The providerphysical_network of this ServerRoceNetwork.
        :type providerphysical_network: str
        """
        self._providerphysical_network = providerphysical_network

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
        if not isinstance(other, ServerRoceNetwork):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
