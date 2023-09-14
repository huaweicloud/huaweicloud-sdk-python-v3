# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Rack:

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
        'edge_site_id': 'str',
        'rack_category_id': 'str',
        'rack_type': 'str',
        'status': 'RackStatus',
        'storage_assigned_size': 'int',
        'description': 'str',
        'rack_sn_no': 'str',
        'rack_location_no': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'effected_at': 'datetime',
        'market_options': 'MarketOptions',
        'compute_unit': 'list[ComputeSpec]',
        'storage_unit': 'StorageUnit',
        'rack_info': 'RackInfo'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'edge_site_id': 'edge_site_id',
        'rack_category_id': 'rack_category_id',
        'rack_type': 'rack_type',
        'status': 'status',
        'storage_assigned_size': 'storage_assigned_size',
        'description': 'description',
        'rack_sn_no': 'rack_sn_no',
        'rack_location_no': 'rack_location_no',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'effected_at': 'effected_at',
        'market_options': 'market_options',
        'compute_unit': 'compute_unit',
        'storage_unit': 'storage_unit',
        'rack_info': 'rack_info'
    }

    def __init__(self, id=None, name=None, edge_site_id=None, rack_category_id=None, rack_type=None, status=None, storage_assigned_size=None, description=None, rack_sn_no=None, rack_location_no=None, created_at=None, updated_at=None, effected_at=None, market_options=None, compute_unit=None, storage_unit=None, rack_info=None):
        """Rack

        The model defined in huaweicloud sdk

        :param id: 机柜ID
        :type id: str
        :param name: 机柜名称
        :type name: str
        :param edge_site_id: 边缘小站ID
        :type edge_site_id: str
        :param rack_category_id: 机柜目录ID
        :type rack_category_id: str
        :param rack_type: 机柜类型
        :type rack_type: str
        :param status: 
        :type status: :class:`huaweicloudsdkcloudpond.v1.RackStatus`
        :param storage_assigned_size: 已分配存储容量
        :type storage_assigned_size: int
        :param description: 机柜描述
        :type description: str
        :param rack_sn_no: 机柜SN号
        :type rack_sn_no: str
        :param rack_location_no: 机柜位置号
        :type rack_location_no: str
        :param created_at: 创建时间
        :type created_at: datetime
        :param updated_at: 更新时间
        :type updated_at: datetime
        :param effected_at: 生效时间
        :type effected_at: datetime
        :param market_options: 
        :type market_options: :class:`huaweicloudsdkcloudpond.v1.MarketOptions`
        :param compute_unit: 计算单元信息
        :type compute_unit: list[:class:`huaweicloudsdkcloudpond.v1.ComputeSpec`]
        :param storage_unit: 
        :type storage_unit: :class:`huaweicloudsdkcloudpond.v1.StorageUnit`
        :param rack_info: 
        :type rack_info: :class:`huaweicloudsdkcloudpond.v1.RackInfo`
        """
        
        

        self._id = None
        self._name = None
        self._edge_site_id = None
        self._rack_category_id = None
        self._rack_type = None
        self._status = None
        self._storage_assigned_size = None
        self._description = None
        self._rack_sn_no = None
        self._rack_location_no = None
        self._created_at = None
        self._updated_at = None
        self._effected_at = None
        self._market_options = None
        self._compute_unit = None
        self._storage_unit = None
        self._rack_info = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if edge_site_id is not None:
            self.edge_site_id = edge_site_id
        if rack_category_id is not None:
            self.rack_category_id = rack_category_id
        if rack_type is not None:
            self.rack_type = rack_type
        if status is not None:
            self.status = status
        if storage_assigned_size is not None:
            self.storage_assigned_size = storage_assigned_size
        if description is not None:
            self.description = description
        if rack_sn_no is not None:
            self.rack_sn_no = rack_sn_no
        if rack_location_no is not None:
            self.rack_location_no = rack_location_no
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if effected_at is not None:
            self.effected_at = effected_at
        if market_options is not None:
            self.market_options = market_options
        if compute_unit is not None:
            self.compute_unit = compute_unit
        if storage_unit is not None:
            self.storage_unit = storage_unit
        if rack_info is not None:
            self.rack_info = rack_info

    @property
    def id(self):
        """Gets the id of this Rack.

        机柜ID

        :return: The id of this Rack.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Rack.

        机柜ID

        :param id: The id of this Rack.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this Rack.

        机柜名称

        :return: The name of this Rack.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Rack.

        机柜名称

        :param name: The name of this Rack.
        :type name: str
        """
        self._name = name

    @property
    def edge_site_id(self):
        """Gets the edge_site_id of this Rack.

        边缘小站ID

        :return: The edge_site_id of this Rack.
        :rtype: str
        """
        return self._edge_site_id

    @edge_site_id.setter
    def edge_site_id(self, edge_site_id):
        """Sets the edge_site_id of this Rack.

        边缘小站ID

        :param edge_site_id: The edge_site_id of this Rack.
        :type edge_site_id: str
        """
        self._edge_site_id = edge_site_id

    @property
    def rack_category_id(self):
        """Gets the rack_category_id of this Rack.

        机柜目录ID

        :return: The rack_category_id of this Rack.
        :rtype: str
        """
        return self._rack_category_id

    @rack_category_id.setter
    def rack_category_id(self, rack_category_id):
        """Sets the rack_category_id of this Rack.

        机柜目录ID

        :param rack_category_id: The rack_category_id of this Rack.
        :type rack_category_id: str
        """
        self._rack_category_id = rack_category_id

    @property
    def rack_type(self):
        """Gets the rack_type of this Rack.

        机柜类型

        :return: The rack_type of this Rack.
        :rtype: str
        """
        return self._rack_type

    @rack_type.setter
    def rack_type(self, rack_type):
        """Sets the rack_type of this Rack.

        机柜类型

        :param rack_type: The rack_type of this Rack.
        :type rack_type: str
        """
        self._rack_type = rack_type

    @property
    def status(self):
        """Gets the status of this Rack.

        :return: The status of this Rack.
        :rtype: :class:`huaweicloudsdkcloudpond.v1.RackStatus`
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Rack.

        :param status: The status of this Rack.
        :type status: :class:`huaweicloudsdkcloudpond.v1.RackStatus`
        """
        self._status = status

    @property
    def storage_assigned_size(self):
        """Gets the storage_assigned_size of this Rack.

        已分配存储容量

        :return: The storage_assigned_size of this Rack.
        :rtype: int
        """
        return self._storage_assigned_size

    @storage_assigned_size.setter
    def storage_assigned_size(self, storage_assigned_size):
        """Sets the storage_assigned_size of this Rack.

        已分配存储容量

        :param storage_assigned_size: The storage_assigned_size of this Rack.
        :type storage_assigned_size: int
        """
        self._storage_assigned_size = storage_assigned_size

    @property
    def description(self):
        """Gets the description of this Rack.

        机柜描述

        :return: The description of this Rack.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Rack.

        机柜描述

        :param description: The description of this Rack.
        :type description: str
        """
        self._description = description

    @property
    def rack_sn_no(self):
        """Gets the rack_sn_no of this Rack.

        机柜SN号

        :return: The rack_sn_no of this Rack.
        :rtype: str
        """
        return self._rack_sn_no

    @rack_sn_no.setter
    def rack_sn_no(self, rack_sn_no):
        """Sets the rack_sn_no of this Rack.

        机柜SN号

        :param rack_sn_no: The rack_sn_no of this Rack.
        :type rack_sn_no: str
        """
        self._rack_sn_no = rack_sn_no

    @property
    def rack_location_no(self):
        """Gets the rack_location_no of this Rack.

        机柜位置号

        :return: The rack_location_no of this Rack.
        :rtype: str
        """
        return self._rack_location_no

    @rack_location_no.setter
    def rack_location_no(self, rack_location_no):
        """Sets the rack_location_no of this Rack.

        机柜位置号

        :param rack_location_no: The rack_location_no of this Rack.
        :type rack_location_no: str
        """
        self._rack_location_no = rack_location_no

    @property
    def created_at(self):
        """Gets the created_at of this Rack.

        创建时间

        :return: The created_at of this Rack.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Rack.

        创建时间

        :param created_at: The created_at of this Rack.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this Rack.

        更新时间

        :return: The updated_at of this Rack.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Rack.

        更新时间

        :param updated_at: The updated_at of this Rack.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

    @property
    def effected_at(self):
        """Gets the effected_at of this Rack.

        生效时间

        :return: The effected_at of this Rack.
        :rtype: datetime
        """
        return self._effected_at

    @effected_at.setter
    def effected_at(self, effected_at):
        """Sets the effected_at of this Rack.

        生效时间

        :param effected_at: The effected_at of this Rack.
        :type effected_at: datetime
        """
        self._effected_at = effected_at

    @property
    def market_options(self):
        """Gets the market_options of this Rack.

        :return: The market_options of this Rack.
        :rtype: :class:`huaweicloudsdkcloudpond.v1.MarketOptions`
        """
        return self._market_options

    @market_options.setter
    def market_options(self, market_options):
        """Sets the market_options of this Rack.

        :param market_options: The market_options of this Rack.
        :type market_options: :class:`huaweicloudsdkcloudpond.v1.MarketOptions`
        """
        self._market_options = market_options

    @property
    def compute_unit(self):
        """Gets the compute_unit of this Rack.

        计算单元信息

        :return: The compute_unit of this Rack.
        :rtype: list[:class:`huaweicloudsdkcloudpond.v1.ComputeSpec`]
        """
        return self._compute_unit

    @compute_unit.setter
    def compute_unit(self, compute_unit):
        """Sets the compute_unit of this Rack.

        计算单元信息

        :param compute_unit: The compute_unit of this Rack.
        :type compute_unit: list[:class:`huaweicloudsdkcloudpond.v1.ComputeSpec`]
        """
        self._compute_unit = compute_unit

    @property
    def storage_unit(self):
        """Gets the storage_unit of this Rack.

        :return: The storage_unit of this Rack.
        :rtype: :class:`huaweicloudsdkcloudpond.v1.StorageUnit`
        """
        return self._storage_unit

    @storage_unit.setter
    def storage_unit(self, storage_unit):
        """Sets the storage_unit of this Rack.

        :param storage_unit: The storage_unit of this Rack.
        :type storage_unit: :class:`huaweicloudsdkcloudpond.v1.StorageUnit`
        """
        self._storage_unit = storage_unit

    @property
    def rack_info(self):
        """Gets the rack_info of this Rack.

        :return: The rack_info of this Rack.
        :rtype: :class:`huaweicloudsdkcloudpond.v1.RackInfo`
        """
        return self._rack_info

    @rack_info.setter
    def rack_info(self, rack_info):
        """Sets the rack_info of this Rack.

        :param rack_info: The rack_info of this Rack.
        :type rack_info: :class:`huaweicloudsdkcloudpond.v1.RackInfo`
        """
        self._rack_info = rack_info

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
        if not isinstance(other, Rack):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
