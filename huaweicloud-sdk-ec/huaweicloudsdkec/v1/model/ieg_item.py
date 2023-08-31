# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IegItem:

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
        'project_id': 'str',
        'domain_id': 'str',
        'name': 'str',
        'area_id': 'str',
        'equipment_type': 'str',
        'high_availability': 'str',
        'frozen_effect': 'int',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'status': 'str',
        'bind_ecn': 'str',
        'enterprise_project_id': 'str',
        'order_id': 'str',
        'product_id': 'str',
        'equipment_infos': 'list[EquipmentItem]'
    }

    attribute_map = {
        'id': 'id',
        'project_id': 'project_id',
        'domain_id': 'domain_id',
        'name': 'name',
        'area_id': 'area_id',
        'equipment_type': 'equipment_type',
        'high_availability': 'high_availability',
        'frozen_effect': 'frozen_effect',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'status': 'status',
        'bind_ecn': 'bind_ecn',
        'enterprise_project_id': 'enterprise_project_id',
        'order_id': 'order_id',
        'product_id': 'product_id',
        'equipment_infos': 'equipment_infos'
    }

    def __init__(self, id=None, project_id=None, domain_id=None, name=None, area_id=None, equipment_type=None, high_availability=None, frozen_effect=None, created_at=None, updated_at=None, status=None, bind_ecn=None, enterprise_project_id=None, order_id=None, product_id=None, equipment_infos=None):
        """IegItem

        The model defined in huaweicloud sdk

        :param id: 智能企业网关ID
        :type id: str
        :param project_id: 项目ID
        :type project_id: str
        :param domain_id: 租户账号ID
        :type domain_id: str
        :param name: 智能企业网关名字
        :type name: str
        :param area_id: 大区ID
        :type area_id: str
        :param equipment_type: 设备类型
        :type equipment_type: str
        :param high_availability: 高可用性
        :type high_availability: str
        :param frozen_effect: 冻结效果
        :type frozen_effect: int
        :param created_at: 创建时间
        :type created_at: datetime
        :param updated_at: 更新时间
        :type updated_at: datetime
        :param status: 状态
        :type status: str
        :param bind_ecn: 绑定的企业连接网络ID
        :type bind_ecn: str
        :param enterprise_project_id: 企业项目ID
        :type enterprise_project_id: str
        :param order_id: 包周期场景下购买的订单号，按需场景下为空
        :type order_id: str
        :param product_id: 包周期场景下购买的订单号，按需场景下为空
        :type product_id: str
        :param equipment_infos: ieg设备信息
        :type equipment_infos: list[:class:`huaweicloudsdkec.v1.EquipmentItem`]
        """
        
        

        self._id = None
        self._project_id = None
        self._domain_id = None
        self._name = None
        self._area_id = None
        self._equipment_type = None
        self._high_availability = None
        self._frozen_effect = None
        self._created_at = None
        self._updated_at = None
        self._status = None
        self._bind_ecn = None
        self._enterprise_project_id = None
        self._order_id = None
        self._product_id = None
        self._equipment_infos = None
        self.discriminator = None

        self.id = id
        if project_id is not None:
            self.project_id = project_id
        if domain_id is not None:
            self.domain_id = domain_id
        if name is not None:
            self.name = name
        if area_id is not None:
            self.area_id = area_id
        if equipment_type is not None:
            self.equipment_type = equipment_type
        if high_availability is not None:
            self.high_availability = high_availability
        if frozen_effect is not None:
            self.frozen_effect = frozen_effect
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if status is not None:
            self.status = status
        if bind_ecn is not None:
            self.bind_ecn = bind_ecn
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if order_id is not None:
            self.order_id = order_id
        if product_id is not None:
            self.product_id = product_id
        if equipment_infos is not None:
            self.equipment_infos = equipment_infos

    @property
    def id(self):
        """Gets the id of this IegItem.

        智能企业网关ID

        :return: The id of this IegItem.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IegItem.

        智能企业网关ID

        :param id: The id of this IegItem.
        :type id: str
        """
        self._id = id

    @property
    def project_id(self):
        """Gets the project_id of this IegItem.

        项目ID

        :return: The project_id of this IegItem.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this IegItem.

        项目ID

        :param project_id: The project_id of this IegItem.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def domain_id(self):
        """Gets the domain_id of this IegItem.

        租户账号ID

        :return: The domain_id of this IegItem.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this IegItem.

        租户账号ID

        :param domain_id: The domain_id of this IegItem.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def name(self):
        """Gets the name of this IegItem.

        智能企业网关名字

        :return: The name of this IegItem.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IegItem.

        智能企业网关名字

        :param name: The name of this IegItem.
        :type name: str
        """
        self._name = name

    @property
    def area_id(self):
        """Gets the area_id of this IegItem.

        大区ID

        :return: The area_id of this IegItem.
        :rtype: str
        """
        return self._area_id

    @area_id.setter
    def area_id(self, area_id):
        """Sets the area_id of this IegItem.

        大区ID

        :param area_id: The area_id of this IegItem.
        :type area_id: str
        """
        self._area_id = area_id

    @property
    def equipment_type(self):
        """Gets the equipment_type of this IegItem.

        设备类型

        :return: The equipment_type of this IegItem.
        :rtype: str
        """
        return self._equipment_type

    @equipment_type.setter
    def equipment_type(self, equipment_type):
        """Sets the equipment_type of this IegItem.

        设备类型

        :param equipment_type: The equipment_type of this IegItem.
        :type equipment_type: str
        """
        self._equipment_type = equipment_type

    @property
    def high_availability(self):
        """Gets the high_availability of this IegItem.

        高可用性

        :return: The high_availability of this IegItem.
        :rtype: str
        """
        return self._high_availability

    @high_availability.setter
    def high_availability(self, high_availability):
        """Sets the high_availability of this IegItem.

        高可用性

        :param high_availability: The high_availability of this IegItem.
        :type high_availability: str
        """
        self._high_availability = high_availability

    @property
    def frozen_effect(self):
        """Gets the frozen_effect of this IegItem.

        冻结效果

        :return: The frozen_effect of this IegItem.
        :rtype: int
        """
        return self._frozen_effect

    @frozen_effect.setter
    def frozen_effect(self, frozen_effect):
        """Sets the frozen_effect of this IegItem.

        冻结效果

        :param frozen_effect: The frozen_effect of this IegItem.
        :type frozen_effect: int
        """
        self._frozen_effect = frozen_effect

    @property
    def created_at(self):
        """Gets the created_at of this IegItem.

        创建时间

        :return: The created_at of this IegItem.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this IegItem.

        创建时间

        :param created_at: The created_at of this IegItem.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this IegItem.

        更新时间

        :return: The updated_at of this IegItem.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this IegItem.

        更新时间

        :param updated_at: The updated_at of this IegItem.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

    @property
    def status(self):
        """Gets the status of this IegItem.

        状态

        :return: The status of this IegItem.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this IegItem.

        状态

        :param status: The status of this IegItem.
        :type status: str
        """
        self._status = status

    @property
    def bind_ecn(self):
        """Gets the bind_ecn of this IegItem.

        绑定的企业连接网络ID

        :return: The bind_ecn of this IegItem.
        :rtype: str
        """
        return self._bind_ecn

    @bind_ecn.setter
    def bind_ecn(self, bind_ecn):
        """Sets the bind_ecn of this IegItem.

        绑定的企业连接网络ID

        :param bind_ecn: The bind_ecn of this IegItem.
        :type bind_ecn: str
        """
        self._bind_ecn = bind_ecn

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this IegItem.

        企业项目ID

        :return: The enterprise_project_id of this IegItem.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this IegItem.

        企业项目ID

        :param enterprise_project_id: The enterprise_project_id of this IegItem.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def order_id(self):
        """Gets the order_id of this IegItem.

        包周期场景下购买的订单号，按需场景下为空

        :return: The order_id of this IegItem.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this IegItem.

        包周期场景下购买的订单号，按需场景下为空

        :param order_id: The order_id of this IegItem.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def product_id(self):
        """Gets the product_id of this IegItem.

        包周期场景下购买的订单号，按需场景下为空

        :return: The product_id of this IegItem.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this IegItem.

        包周期场景下购买的订单号，按需场景下为空

        :param product_id: The product_id of this IegItem.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def equipment_infos(self):
        """Gets the equipment_infos of this IegItem.

        ieg设备信息

        :return: The equipment_infos of this IegItem.
        :rtype: list[:class:`huaweicloudsdkec.v1.EquipmentItem`]
        """
        return self._equipment_infos

    @equipment_infos.setter
    def equipment_infos(self, equipment_infos):
        """Sets the equipment_infos of this IegItem.

        ieg设备信息

        :param equipment_infos: The equipment_infos of this IegItem.
        :type equipment_infos: list[:class:`huaweicloudsdkec.v1.EquipmentItem`]
        """
        self._equipment_infos = equipment_infos

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
        if not isinstance(other, IegItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
