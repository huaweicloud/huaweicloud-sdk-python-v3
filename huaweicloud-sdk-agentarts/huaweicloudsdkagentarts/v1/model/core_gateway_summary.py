# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CoreGatewaySummary:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'gateway_id': 'str',
        'name': 'str',
        'status': 'str',
        'protocol_type': 'str',
        'authorizer_type': 'str',
        'agency_name': 'str',
        'tags': 'list[CoreGatewayTag]',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'gateway_id': 'gateway_id',
        'name': 'name',
        'status': 'status',
        'protocol_type': 'protocol_type',
        'authorizer_type': 'authorizer_type',
        'agency_name': 'agency_name',
        'tags': 'tags',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, gateway_id=None, name=None, status=None, protocol_type=None, authorizer_type=None, agency_name=None, tags=None, created_at=None, updated_at=None):
        r"""CoreGatewaySummary

        The model defined in huaweicloud sdk

        :param gateway_id: 网关的唯一标识符。
        :type gateway_id: str
        :param name: 网关名称。
        :type name: str
        :param status: 网关的当前状态。
        :type status: str
        :param protocol_type: 网关协议类型。
        :type protocol_type: str
        :param authorizer_type: 授权器类型。
        :type authorizer_type: str
        :param agency_name: 委托名称。
        :type agency_name: str
        :param tags: 资源标签列表。
        :type tags: list[:class:`huaweicloudsdkagentarts.v1.CoreGatewayTag`]
        :param created_at: 网关创建时间戳。
        :type created_at: datetime
        :param updated_at: 网关最后更新时间戳。
        :type updated_at: datetime
        """
        
        

        self._gateway_id = None
        self._name = None
        self._status = None
        self._protocol_type = None
        self._authorizer_type = None
        self._agency_name = None
        self._tags = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        self.gateway_id = gateway_id
        self.name = name
        self.status = status
        self.protocol_type = protocol_type
        self.authorizer_type = authorizer_type
        self.agency_name = agency_name
        if tags is not None:
            self.tags = tags
        self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def gateway_id(self):
        r"""Gets the gateway_id of this CoreGatewaySummary.

        网关的唯一标识符。

        :return: The gateway_id of this CoreGatewaySummary.
        :rtype: str
        """
        return self._gateway_id

    @gateway_id.setter
    def gateway_id(self, gateway_id):
        r"""Sets the gateway_id of this CoreGatewaySummary.

        网关的唯一标识符。

        :param gateway_id: The gateway_id of this CoreGatewaySummary.
        :type gateway_id: str
        """
        self._gateway_id = gateway_id

    @property
    def name(self):
        r"""Gets the name of this CoreGatewaySummary.

        网关名称。

        :return: The name of this CoreGatewaySummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CoreGatewaySummary.

        网关名称。

        :param name: The name of this CoreGatewaySummary.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        r"""Gets the status of this CoreGatewaySummary.

        网关的当前状态。

        :return: The status of this CoreGatewaySummary.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this CoreGatewaySummary.

        网关的当前状态。

        :param status: The status of this CoreGatewaySummary.
        :type status: str
        """
        self._status = status

    @property
    def protocol_type(self):
        r"""Gets the protocol_type of this CoreGatewaySummary.

        网关协议类型。

        :return: The protocol_type of this CoreGatewaySummary.
        :rtype: str
        """
        return self._protocol_type

    @protocol_type.setter
    def protocol_type(self, protocol_type):
        r"""Sets the protocol_type of this CoreGatewaySummary.

        网关协议类型。

        :param protocol_type: The protocol_type of this CoreGatewaySummary.
        :type protocol_type: str
        """
        self._protocol_type = protocol_type

    @property
    def authorizer_type(self):
        r"""Gets the authorizer_type of this CoreGatewaySummary.

        授权器类型。

        :return: The authorizer_type of this CoreGatewaySummary.
        :rtype: str
        """
        return self._authorizer_type

    @authorizer_type.setter
    def authorizer_type(self, authorizer_type):
        r"""Sets the authorizer_type of this CoreGatewaySummary.

        授权器类型。

        :param authorizer_type: The authorizer_type of this CoreGatewaySummary.
        :type authorizer_type: str
        """
        self._authorizer_type = authorizer_type

    @property
    def agency_name(self):
        r"""Gets the agency_name of this CoreGatewaySummary.

        委托名称。

        :return: The agency_name of this CoreGatewaySummary.
        :rtype: str
        """
        return self._agency_name

    @agency_name.setter
    def agency_name(self, agency_name):
        r"""Sets the agency_name of this CoreGatewaySummary.

        委托名称。

        :param agency_name: The agency_name of this CoreGatewaySummary.
        :type agency_name: str
        """
        self._agency_name = agency_name

    @property
    def tags(self):
        r"""Gets the tags of this CoreGatewaySummary.

        资源标签列表。

        :return: The tags of this CoreGatewaySummary.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.CoreGatewayTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this CoreGatewaySummary.

        资源标签列表。

        :param tags: The tags of this CoreGatewaySummary.
        :type tags: list[:class:`huaweicloudsdkagentarts.v1.CoreGatewayTag`]
        """
        self._tags = tags

    @property
    def created_at(self):
        r"""Gets the created_at of this CoreGatewaySummary.

        网关创建时间戳。

        :return: The created_at of this CoreGatewaySummary.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this CoreGatewaySummary.

        网关创建时间戳。

        :param created_at: The created_at of this CoreGatewaySummary.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this CoreGatewaySummary.

        网关最后更新时间戳。

        :return: The updated_at of this CoreGatewaySummary.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this CoreGatewaySummary.

        网关最后更新时间戳。

        :param updated_at: The updated_at of this CoreGatewaySummary.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

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
        if not isinstance(other, CoreGatewaySummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
