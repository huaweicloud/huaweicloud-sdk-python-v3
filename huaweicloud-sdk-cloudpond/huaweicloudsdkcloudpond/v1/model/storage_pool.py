# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StoragePool:

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
        'storage_type': 'StorageType',
        'status': 'StoragePoolStatus',
        'assigned_size': 'int',
        'resource_spec_code': 'str',
        'product_info': 'ProductInfo',
        'capacity': 'int',
        'market_options': 'MarketOptions',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'effected_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'edge_site_id': 'edge_site_id',
        'storage_type': 'storage_type',
        'status': 'status',
        'assigned_size': 'assigned_size',
        'resource_spec_code': 'resource_spec_code',
        'product_info': 'product_info',
        'capacity': 'capacity',
        'market_options': 'market_options',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'effected_at': 'effected_at'
    }

    def __init__(self, id=None, name=None, edge_site_id=None, storage_type=None, status=None, assigned_size=None, resource_spec_code=None, product_info=None, capacity=None, market_options=None, created_at=None, updated_at=None, effected_at=None):
        r"""StoragePool

        The model defined in huaweicloud sdk

        :param id: 机柜ID
        :type id: str
        :param name: 存储池名称
        :type name: str
        :param edge_site_id: 边缘小站ID
        :type edge_site_id: str
        :param storage_type: 
        :type storage_type: :class:`huaweicloudsdkcloudpond.v1.StorageType`
        :param status: 
        :type status: :class:`huaweicloudsdkcloudpond.v1.StoragePoolStatus`
        :param assigned_size: 存储池大小。 当前购买的存储容量。
        :type assigned_size: int
        :param resource_spec_code: 资源规格编码
        :type resource_spec_code: str
        :param product_info: 
        :type product_info: :class:`huaweicloudsdkcloudpond.v1.ProductInfo`
        :param capacity: 总容量
        :type capacity: int
        :param market_options: 
        :type market_options: :class:`huaweicloudsdkcloudpond.v1.MarketOptions`
        :param created_at: 创建时间
        :type created_at: datetime
        :param updated_at: 更新时间
        :type updated_at: datetime
        :param effected_at: 生效时间
        :type effected_at: datetime
        """
        
        

        self._id = None
        self._name = None
        self._edge_site_id = None
        self._storage_type = None
        self._status = None
        self._assigned_size = None
        self._resource_spec_code = None
        self._product_info = None
        self._capacity = None
        self._market_options = None
        self._created_at = None
        self._updated_at = None
        self._effected_at = None
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
        if resource_spec_code is not None:
            self.resource_spec_code = resource_spec_code
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
        if effected_at is not None:
            self.effected_at = effected_at

    @property
    def id(self):
        r"""Gets the id of this StoragePool.

        机柜ID

        :return: The id of this StoragePool.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this StoragePool.

        机柜ID

        :param id: The id of this StoragePool.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this StoragePool.

        存储池名称

        :return: The name of this StoragePool.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this StoragePool.

        存储池名称

        :param name: The name of this StoragePool.
        :type name: str
        """
        self._name = name

    @property
    def edge_site_id(self):
        r"""Gets the edge_site_id of this StoragePool.

        边缘小站ID

        :return: The edge_site_id of this StoragePool.
        :rtype: str
        """
        return self._edge_site_id

    @edge_site_id.setter
    def edge_site_id(self, edge_site_id):
        r"""Sets the edge_site_id of this StoragePool.

        边缘小站ID

        :param edge_site_id: The edge_site_id of this StoragePool.
        :type edge_site_id: str
        """
        self._edge_site_id = edge_site_id

    @property
    def storage_type(self):
        r"""Gets the storage_type of this StoragePool.

        :return: The storage_type of this StoragePool.
        :rtype: :class:`huaweicloudsdkcloudpond.v1.StorageType`
        """
        return self._storage_type

    @storage_type.setter
    def storage_type(self, storage_type):
        r"""Sets the storage_type of this StoragePool.

        :param storage_type: The storage_type of this StoragePool.
        :type storage_type: :class:`huaweicloudsdkcloudpond.v1.StorageType`
        """
        self._storage_type = storage_type

    @property
    def status(self):
        r"""Gets the status of this StoragePool.

        :return: The status of this StoragePool.
        :rtype: :class:`huaweicloudsdkcloudpond.v1.StoragePoolStatus`
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this StoragePool.

        :param status: The status of this StoragePool.
        :type status: :class:`huaweicloudsdkcloudpond.v1.StoragePoolStatus`
        """
        self._status = status

    @property
    def assigned_size(self):
        r"""Gets the assigned_size of this StoragePool.

        存储池大小。 当前购买的存储容量。

        :return: The assigned_size of this StoragePool.
        :rtype: int
        """
        return self._assigned_size

    @assigned_size.setter
    def assigned_size(self, assigned_size):
        r"""Sets the assigned_size of this StoragePool.

        存储池大小。 当前购买的存储容量。

        :param assigned_size: The assigned_size of this StoragePool.
        :type assigned_size: int
        """
        self._assigned_size = assigned_size

    @property
    def resource_spec_code(self):
        r"""Gets the resource_spec_code of this StoragePool.

        资源规格编码

        :return: The resource_spec_code of this StoragePool.
        :rtype: str
        """
        return self._resource_spec_code

    @resource_spec_code.setter
    def resource_spec_code(self, resource_spec_code):
        r"""Sets the resource_spec_code of this StoragePool.

        资源规格编码

        :param resource_spec_code: The resource_spec_code of this StoragePool.
        :type resource_spec_code: str
        """
        self._resource_spec_code = resource_spec_code

    @property
    def product_info(self):
        r"""Gets the product_info of this StoragePool.

        :return: The product_info of this StoragePool.
        :rtype: :class:`huaweicloudsdkcloudpond.v1.ProductInfo`
        """
        return self._product_info

    @product_info.setter
    def product_info(self, product_info):
        r"""Sets the product_info of this StoragePool.

        :param product_info: The product_info of this StoragePool.
        :type product_info: :class:`huaweicloudsdkcloudpond.v1.ProductInfo`
        """
        self._product_info = product_info

    @property
    def capacity(self):
        r"""Gets the capacity of this StoragePool.

        总容量

        :return: The capacity of this StoragePool.
        :rtype: int
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        r"""Sets the capacity of this StoragePool.

        总容量

        :param capacity: The capacity of this StoragePool.
        :type capacity: int
        """
        self._capacity = capacity

    @property
    def market_options(self):
        r"""Gets the market_options of this StoragePool.

        :return: The market_options of this StoragePool.
        :rtype: :class:`huaweicloudsdkcloudpond.v1.MarketOptions`
        """
        return self._market_options

    @market_options.setter
    def market_options(self, market_options):
        r"""Sets the market_options of this StoragePool.

        :param market_options: The market_options of this StoragePool.
        :type market_options: :class:`huaweicloudsdkcloudpond.v1.MarketOptions`
        """
        self._market_options = market_options

    @property
    def created_at(self):
        r"""Gets the created_at of this StoragePool.

        创建时间

        :return: The created_at of this StoragePool.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this StoragePool.

        创建时间

        :param created_at: The created_at of this StoragePool.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this StoragePool.

        更新时间

        :return: The updated_at of this StoragePool.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this StoragePool.

        更新时间

        :param updated_at: The updated_at of this StoragePool.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

    @property
    def effected_at(self):
        r"""Gets the effected_at of this StoragePool.

        生效时间

        :return: The effected_at of this StoragePool.
        :rtype: datetime
        """
        return self._effected_at

    @effected_at.setter
    def effected_at(self, effected_at):
        r"""Sets the effected_at of this StoragePool.

        生效时间

        :param effected_at: The effected_at of this StoragePool.
        :type effected_at: datetime
        """
        self._effected_at = effected_at

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
        if not isinstance(other, StoragePool):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
