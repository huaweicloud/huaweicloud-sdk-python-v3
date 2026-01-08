# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateOrderReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'enterprise_project_id': 'str',
        'agency_urn': 'str',
        'resources': 'list[Resource]',
        'extend_param': 'OrderExtendParam'
    }

    attribute_map = {
        'type': 'type',
        'enterprise_project_id': 'enterprise_project_id',
        'agency_urn': 'agency_urn',
        'resources': 'resources',
        'extend_param': 'extend_param'
    }

    def __init__(self, type=None, enterprise_project_id=None, agency_urn=None, resources=None, extend_param=None):
        r"""CreateOrderReq

        The model defined in huaweicloud sdk

        :param type: 订单类型，createDesktops：创建桌面，addVolumes：添加磁盘，rebuildDesktops：重建系统盘，createDesktopPool 创建桌面池，expandDesktopPool 扩容桌面池，applyDesktopsInternet：开通桌面EIP上网，createExclusiveHosts：创建专享主机，subscribeUserSharer：订购用户协同资源，ApplySubnetBandwidth：开通云办公带宽。
        :type type: str
        :param enterprise_project_id: 企业项目ID，默认\&quot;0。\&quot;
        :type enterprise_project_id: str
        :param agency_urn: 授权给Billing服务的委托URN。使用RAM共享密钥创建包周期云桌面或添加包周期磁盘时，需要传入该字段。
        :type agency_urn: str
        :param resources: 包周期资源。
        :type resources: list[:class:`huaweicloudsdkworkspace.v2.Resource`]
        :param extend_param: 
        :type extend_param: :class:`huaweicloudsdkworkspace.v2.OrderExtendParam`
        """
        
        

        self._type = None
        self._enterprise_project_id = None
        self._agency_urn = None
        self._resources = None
        self._extend_param = None
        self.discriminator = None

        self.type = type
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if agency_urn is not None:
            self.agency_urn = agency_urn
        self.resources = resources
        if extend_param is not None:
            self.extend_param = extend_param

    @property
    def type(self):
        r"""Gets the type of this CreateOrderReq.

        订单类型，createDesktops：创建桌面，addVolumes：添加磁盘，rebuildDesktops：重建系统盘，createDesktopPool 创建桌面池，expandDesktopPool 扩容桌面池，applyDesktopsInternet：开通桌面EIP上网，createExclusiveHosts：创建专享主机，subscribeUserSharer：订购用户协同资源，ApplySubnetBandwidth：开通云办公带宽。

        :return: The type of this CreateOrderReq.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CreateOrderReq.

        订单类型，createDesktops：创建桌面，addVolumes：添加磁盘，rebuildDesktops：重建系统盘，createDesktopPool 创建桌面池，expandDesktopPool 扩容桌面池，applyDesktopsInternet：开通桌面EIP上网，createExclusiveHosts：创建专享主机，subscribeUserSharer：订购用户协同资源，ApplySubnetBandwidth：开通云办公带宽。

        :param type: The type of this CreateOrderReq.
        :type type: str
        """
        self._type = type

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this CreateOrderReq.

        企业项目ID，默认\"0。\"

        :return: The enterprise_project_id of this CreateOrderReq.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this CreateOrderReq.

        企业项目ID，默认\"0。\"

        :param enterprise_project_id: The enterprise_project_id of this CreateOrderReq.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def agency_urn(self):
        r"""Gets the agency_urn of this CreateOrderReq.

        授权给Billing服务的委托URN。使用RAM共享密钥创建包周期云桌面或添加包周期磁盘时，需要传入该字段。

        :return: The agency_urn of this CreateOrderReq.
        :rtype: str
        """
        return self._agency_urn

    @agency_urn.setter
    def agency_urn(self, agency_urn):
        r"""Sets the agency_urn of this CreateOrderReq.

        授权给Billing服务的委托URN。使用RAM共享密钥创建包周期云桌面或添加包周期磁盘时，需要传入该字段。

        :param agency_urn: The agency_urn of this CreateOrderReq.
        :type agency_urn: str
        """
        self._agency_urn = agency_urn

    @property
    def resources(self):
        r"""Gets the resources of this CreateOrderReq.

        包周期资源。

        :return: The resources of this CreateOrderReq.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.Resource`]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        r"""Sets the resources of this CreateOrderReq.

        包周期资源。

        :param resources: The resources of this CreateOrderReq.
        :type resources: list[:class:`huaweicloudsdkworkspace.v2.Resource`]
        """
        self._resources = resources

    @property
    def extend_param(self):
        r"""Gets the extend_param of this CreateOrderReq.

        :return: The extend_param of this CreateOrderReq.
        :rtype: :class:`huaweicloudsdkworkspace.v2.OrderExtendParam`
        """
        return self._extend_param

    @extend_param.setter
    def extend_param(self, extend_param):
        r"""Sets the extend_param of this CreateOrderReq.

        :param extend_param: The extend_param of this CreateOrderReq.
        :type extend_param: :class:`huaweicloudsdkworkspace.v2.OrderExtendParam`
        """
        self._extend_param = extend_param

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
        if not isinstance(other, CreateOrderReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
