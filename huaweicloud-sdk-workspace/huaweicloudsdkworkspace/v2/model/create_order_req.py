# coding: utf-8

import six

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
        'resources': 'list[Resource]',
        'order_id': 'str',
        'promotion_id': 'str',
        'promotion_plan_id': 'str',
        'promotion_info': 'str',
        'extend_param': 'OrderExtendParam'
    }

    attribute_map = {
        'type': 'type',
        'enterprise_project_id': 'enterprise_project_id',
        'resources': 'resources',
        'order_id': 'order_id',
        'promotion_id': 'promotion_id',
        'promotion_plan_id': 'promotion_plan_id',
        'promotion_info': 'promotion_info',
        'extend_param': 'extend_param'
    }

    def __init__(self, type=None, enterprise_project_id=None, resources=None, order_id=None, promotion_id=None, promotion_plan_id=None, promotion_info=None, extend_param=None):
        """CreateOrderReq

        The model defined in huaweicloud sdk

        :param type: 订单类型，createDesktops：创建桌面，addVolumes：添加磁盘[，createDehHosts：创建专属主机](tag:ZQ)，rebuildDesktops：重建系统盘，createDesktopPool 创建桌面池，expandDesktopPool 扩容桌面池，applyDesktopsInternet：开通桌面EIP上网，createExclusiveHosts：创建专享主机，subscribeUserSharer：订购用户协同资源，ApplySubnetBandwidth：开通云办公带宽
        :type type: str
        :param enterprise_project_id: 企业项目ID，默认\&quot;0\&quot;
        :type enterprise_project_id: str
        :param resources: 包周期资源
        :type resources: list[:class:`huaweicloudsdkworkspace.v2.Resource`]
        :param order_id: 组合购订单ID
        :type order_id: str
        :param promotion_id: 促销ID
        :type promotion_id: str
        :param promotion_plan_id: 促销计划ID
        :type promotion_plan_id: str
        :param promotion_info: 促销信息
        :type promotion_info: str
        :param extend_param: 
        :type extend_param: :class:`huaweicloudsdkworkspace.v2.OrderExtendParam`
        """
        
        

        self._type = None
        self._enterprise_project_id = None
        self._resources = None
        self._order_id = None
        self._promotion_id = None
        self._promotion_plan_id = None
        self._promotion_info = None
        self._extend_param = None
        self.discriminator = None

        self.type = type
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.resources = resources
        if order_id is not None:
            self.order_id = order_id
        if promotion_id is not None:
            self.promotion_id = promotion_id
        if promotion_plan_id is not None:
            self.promotion_plan_id = promotion_plan_id
        if promotion_info is not None:
            self.promotion_info = promotion_info
        if extend_param is not None:
            self.extend_param = extend_param

    @property
    def type(self):
        """Gets the type of this CreateOrderReq.

        订单类型，createDesktops：创建桌面，addVolumes：添加磁盘[，createDehHosts：创建专属主机](tag:ZQ)，rebuildDesktops：重建系统盘，createDesktopPool 创建桌面池，expandDesktopPool 扩容桌面池，applyDesktopsInternet：开通桌面EIP上网，createExclusiveHosts：创建专享主机，subscribeUserSharer：订购用户协同资源，ApplySubnetBandwidth：开通云办公带宽

        :return: The type of this CreateOrderReq.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreateOrderReq.

        订单类型，createDesktops：创建桌面，addVolumes：添加磁盘[，createDehHosts：创建专属主机](tag:ZQ)，rebuildDesktops：重建系统盘，createDesktopPool 创建桌面池，expandDesktopPool 扩容桌面池，applyDesktopsInternet：开通桌面EIP上网，createExclusiveHosts：创建专享主机，subscribeUserSharer：订购用户协同资源，ApplySubnetBandwidth：开通云办公带宽

        :param type: The type of this CreateOrderReq.
        :type type: str
        """
        self._type = type

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this CreateOrderReq.

        企业项目ID，默认\"0\"

        :return: The enterprise_project_id of this CreateOrderReq.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this CreateOrderReq.

        企业项目ID，默认\"0\"

        :param enterprise_project_id: The enterprise_project_id of this CreateOrderReq.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def resources(self):
        """Gets the resources of this CreateOrderReq.

        包周期资源

        :return: The resources of this CreateOrderReq.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.Resource`]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this CreateOrderReq.

        包周期资源

        :param resources: The resources of this CreateOrderReq.
        :type resources: list[:class:`huaweicloudsdkworkspace.v2.Resource`]
        """
        self._resources = resources

    @property
    def order_id(self):
        """Gets the order_id of this CreateOrderReq.

        组合购订单ID

        :return: The order_id of this CreateOrderReq.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this CreateOrderReq.

        组合购订单ID

        :param order_id: The order_id of this CreateOrderReq.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def promotion_id(self):
        """Gets the promotion_id of this CreateOrderReq.

        促销ID

        :return: The promotion_id of this CreateOrderReq.
        :rtype: str
        """
        return self._promotion_id

    @promotion_id.setter
    def promotion_id(self, promotion_id):
        """Sets the promotion_id of this CreateOrderReq.

        促销ID

        :param promotion_id: The promotion_id of this CreateOrderReq.
        :type promotion_id: str
        """
        self._promotion_id = promotion_id

    @property
    def promotion_plan_id(self):
        """Gets the promotion_plan_id of this CreateOrderReq.

        促销计划ID

        :return: The promotion_plan_id of this CreateOrderReq.
        :rtype: str
        """
        return self._promotion_plan_id

    @promotion_plan_id.setter
    def promotion_plan_id(self, promotion_plan_id):
        """Sets the promotion_plan_id of this CreateOrderReq.

        促销计划ID

        :param promotion_plan_id: The promotion_plan_id of this CreateOrderReq.
        :type promotion_plan_id: str
        """
        self._promotion_plan_id = promotion_plan_id

    @property
    def promotion_info(self):
        """Gets the promotion_info of this CreateOrderReq.

        促销信息

        :return: The promotion_info of this CreateOrderReq.
        :rtype: str
        """
        return self._promotion_info

    @promotion_info.setter
    def promotion_info(self, promotion_info):
        """Sets the promotion_info of this CreateOrderReq.

        促销信息

        :param promotion_info: The promotion_info of this CreateOrderReq.
        :type promotion_info: str
        """
        self._promotion_info = promotion_info

    @property
    def extend_param(self):
        """Gets the extend_param of this CreateOrderReq.

        :return: The extend_param of this CreateOrderReq.
        :rtype: :class:`huaweicloudsdkworkspace.v2.OrderExtendParam`
        """
        return self._extend_param

    @extend_param.setter
    def extend_param(self, extend_param):
        """Sets the extend_param of this CreateOrderReq.

        :param extend_param: The extend_param of this CreateOrderReq.
        :type extend_param: :class:`huaweicloudsdkworkspace.v2.OrderExtendParam`
        """
        self._extend_param = extend_param

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
        if not isinstance(other, CreateOrderReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
