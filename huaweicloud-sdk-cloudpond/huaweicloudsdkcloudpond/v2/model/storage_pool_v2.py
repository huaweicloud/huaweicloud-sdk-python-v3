# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StoragePoolV2:

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
        'storage_type': 'str',
        'status': 'str',
        'assigned_size': 'int',
        'product_info': 'ProductInfo',
        'capacity': 'int',
        'market_options': 'MarketOptions',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'parent_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'edge_site_id': 'edge_site_id',
        'storage_type': 'storage_type',
        'status': 'status',
        'assigned_size': 'assigned_size',
        'product_info': 'product_info',
        'capacity': 'capacity',
        'market_options': 'market_options',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'parent_id': 'parent_id'
    }

    def __init__(self, id=None, name=None, edge_site_id=None, storage_type=None, status=None, assigned_size=None, product_info=None, capacity=None, market_options=None, created_at=None, updated_at=None, parent_id=None):
        r"""StoragePoolV2

        The model defined in huaweicloud sdk

        :param id: 存储池ID
        :type id: str
        :param name: 存储池名称
        :type name: str
        :param edge_site_id: 边缘小站ID
        :type edge_site_id: str
        :param storage_type: 存储类型
        :type storage_type: str
        :param status: 存储池状态。 - CREATING：创建中 - AVAILABLE：可用 - EXPANDING：扩容中 - PENDING_PAYMENT：待支付 - FROZEN：已冻结
        :type status: str
        :param assigned_size: 存储池大小。 当前已购买的存储容量。
        :type assigned_size: int
        :param product_info: 
        :type product_info: :class:`huaweicloudsdkcloudpond.v2.ProductInfo`
        :param capacity: 总容量
        :type capacity: int
        :param market_options: 
        :type market_options: :class:`huaweicloudsdkcloudpond.v2.MarketOptions`
        :param created_at: 创建时间
        :type created_at: datetime
        :param updated_at: 更新时间
        :type updated_at: datetime
        :param parent_id: 扩容场景预生成存储池关联的存储池ID
        :type parent_id: str
        """
        
        

        self._id = None
        self._name = None
        self._edge_site_id = None
        self._storage_type = None
        self._status = None
        self._assigned_size = None
        self._product_info = None
        self._capacity = None
        self._market_options = None
        self._created_at = None
        self._updated_at = None
        self._parent_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if edge_site_id is not None:
            self.edge_site_id = edge_site_id
        if storage_type is not None:
            self.storage_type = storage_type
        if status is not None:
            self.status = status
        if assigned_size is not None:
            self.assigned_size = assigned_size
        if product_info is not None:
            self.product_info = product_info
        if capacity is not None:
            self.capacity = capacity
        if market_options is not None:
            self.market_options = market_options
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if parent_id is not None:
            self.parent_id = parent_id

    @property
    def id(self):
        r"""Gets the id of this StoragePoolV2.

        存储池ID

        :return: The id of this StoragePoolV2.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this StoragePoolV2.

        存储池ID

        :param id: The id of this StoragePoolV2.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this StoragePoolV2.

        存储池名称

        :return: The name of this StoragePoolV2.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this StoragePoolV2.

        存储池名称

        :param name: The name of this StoragePoolV2.
        :type name: str
        """
        self._name = name

    @property
    def edge_site_id(self):
        r"""Gets the edge_site_id of this StoragePoolV2.

        边缘小站ID

        :return: The edge_site_id of this StoragePoolV2.
        :rtype: str
        """
        return self._edge_site_id

    @edge_site_id.setter
    def edge_site_id(self, edge_site_id):
        r"""Sets the edge_site_id of this StoragePoolV2.

        边缘小站ID

        :param edge_site_id: The edge_site_id of this StoragePoolV2.
        :type edge_site_id: str
        """
        self._edge_site_id = edge_site_id

    @property
    def storage_type(self):
        r"""Gets the storage_type of this StoragePoolV2.

        存储类型

        :return: The storage_type of this StoragePoolV2.
        :rtype: str
        """
        return self._storage_type

    @storage_type.setter
    def storage_type(self, storage_type):
        r"""Sets the storage_type of this StoragePoolV2.

        存储类型

        :param storage_type: The storage_type of this StoragePoolV2.
        :type storage_type: str
        """
        self._storage_type = storage_type

    @property
    def status(self):
        r"""Gets the status of this StoragePoolV2.

        存储池状态。 - CREATING：创建中 - AVAILABLE：可用 - EXPANDING：扩容中 - PENDING_PAYMENT：待支付 - FROZEN：已冻结

        :return: The status of this StoragePoolV2.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this StoragePoolV2.

        存储池状态。 - CREATING：创建中 - AVAILABLE：可用 - EXPANDING：扩容中 - PENDING_PAYMENT：待支付 - FROZEN：已冻结

        :param status: The status of this StoragePoolV2.
        :type status: str
        """
        self._status = status

    @property
    def assigned_size(self):
        r"""Gets the assigned_size of this StoragePoolV2.

        存储池大小。 当前已购买的存储容量。

        :return: The assigned_size of this StoragePoolV2.
        :rtype: int
        """
        return self._assigned_size

    @assigned_size.setter
    def assigned_size(self, assigned_size):
        r"""Sets the assigned_size of this StoragePoolV2.

        存储池大小。 当前已购买的存储容量。

        :param assigned_size: The assigned_size of this StoragePoolV2.
        :type assigned_size: int
        """
        self._assigned_size = assigned_size

    @property
    def product_info(self):
        r"""Gets the product_info of this StoragePoolV2.

        :return: The product_info of this StoragePoolV2.
        :rtype: :class:`huaweicloudsdkcloudpond.v2.ProductInfo`
        """
        return self._product_info

    @product_info.setter
    def product_info(self, product_info):
        r"""Sets the product_info of this StoragePoolV2.

        :param product_info: The product_info of this StoragePoolV2.
        :type product_info: :class:`huaweicloudsdkcloudpond.v2.ProductInfo`
        """
        self._product_info = product_info

    @property
    def capacity(self):
        r"""Gets the capacity of this StoragePoolV2.

        总容量

        :return: The capacity of this StoragePoolV2.
        :rtype: int
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        r"""Sets the capacity of this StoragePoolV2.

        总容量

        :param capacity: The capacity of this StoragePoolV2.
        :type capacity: int
        """
        self._capacity = capacity

    @property
    def market_options(self):
        r"""Gets the market_options of this StoragePoolV2.

        :return: The market_options of this StoragePoolV2.
        :rtype: :class:`huaweicloudsdkcloudpond.v2.MarketOptions`
        """
        return self._market_options

    @market_options.setter
    def market_options(self, market_options):
        r"""Sets the market_options of this StoragePoolV2.

        :param market_options: The market_options of this StoragePoolV2.
        :type market_options: :class:`huaweicloudsdkcloudpond.v2.MarketOptions`
        """
        self._market_options = market_options

    @property
    def created_at(self):
        r"""Gets the created_at of this StoragePoolV2.

        创建时间

        :return: The created_at of this StoragePoolV2.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this StoragePoolV2.

        创建时间

        :param created_at: The created_at of this StoragePoolV2.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this StoragePoolV2.

        更新时间

        :return: The updated_at of this StoragePoolV2.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this StoragePoolV2.

        更新时间

        :param updated_at: The updated_at of this StoragePoolV2.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

    @property
    def parent_id(self):
        r"""Gets the parent_id of this StoragePoolV2.

        扩容场景预生成存储池关联的存储池ID

        :return: The parent_id of this StoragePoolV2.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        r"""Sets the parent_id of this StoragePoolV2.

        扩容场景预生成存储池关联的存储池ID

        :param parent_id: The parent_id of this StoragePoolV2.
        :type parent_id: str
        """
        self._parent_id = parent_id

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
        if not isinstance(other, StoragePoolV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
