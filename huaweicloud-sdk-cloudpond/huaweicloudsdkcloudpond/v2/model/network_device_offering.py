# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NetworkDeviceOffering:

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
        'zone_code': 'str',
        'scene_code': 'str',
        'status': 'str',
        'spec': 'NetworkDeviceSpec',
        'product_info': 'ProductInfo',
        'sale_cycles': 'list[SaleCycle]'
    }

    attribute_map = {
        'id': 'id',
        'zone_code': 'zone_code',
        'scene_code': 'scene_code',
        'status': 'status',
        'spec': 'spec',
        'product_info': 'product_info',
        'sale_cycles': 'sale_cycles'
    }

    def __init__(self, id=None, zone_code=None, scene_code=None, status=None, spec=None, product_info=None, sale_cycles=None):
        r"""NetworkDeviceOffering

        The model defined in huaweicloud sdk

        :param id: 网络设备商品ID
        :type id: str
        :param zone_code: 地区编码，表示允许在这个地区购买部署
        :type zone_code: str
        :param scene_code: 销售场景编码
        :type scene_code: str
        :param status: 商品状态说明：   - TESTING - 测试   - ONSALE - 在售   - SUSPENDED - 已停售   - RETIREMENT - 产品退出
        :type status: str
        :param spec: 
        :type spec: :class:`huaweicloudsdkcloudpond.v2.NetworkDeviceSpec`
        :param product_info: 
        :type product_info: :class:`huaweicloudsdkcloudpond.v2.ProductInfo`
        :param sale_cycles: 
        :type sale_cycles: list[:class:`huaweicloudsdkcloudpond.v2.SaleCycle`]
        """
        
        

        self._id = None
        self._zone_code = None
        self._scene_code = None
        self._status = None
        self._spec = None
        self._product_info = None
        self._sale_cycles = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if zone_code is not None:
            self.zone_code = zone_code
        if scene_code is not None:
            self.scene_code = scene_code
        if status is not None:
            self.status = status
        if spec is not None:
            self.spec = spec
        if product_info is not None:
            self.product_info = product_info
        if sale_cycles is not None:
            self.sale_cycles = sale_cycles

    @property
    def id(self):
        r"""Gets the id of this NetworkDeviceOffering.

        网络设备商品ID

        :return: The id of this NetworkDeviceOffering.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this NetworkDeviceOffering.

        网络设备商品ID

        :param id: The id of this NetworkDeviceOffering.
        :type id: str
        """
        self._id = id

    @property
    def zone_code(self):
        r"""Gets the zone_code of this NetworkDeviceOffering.

        地区编码，表示允许在这个地区购买部署

        :return: The zone_code of this NetworkDeviceOffering.
        :rtype: str
        """
        return self._zone_code

    @zone_code.setter
    def zone_code(self, zone_code):
        r"""Sets the zone_code of this NetworkDeviceOffering.

        地区编码，表示允许在这个地区购买部署

        :param zone_code: The zone_code of this NetworkDeviceOffering.
        :type zone_code: str
        """
        self._zone_code = zone_code

    @property
    def scene_code(self):
        r"""Gets the scene_code of this NetworkDeviceOffering.

        销售场景编码

        :return: The scene_code of this NetworkDeviceOffering.
        :rtype: str
        """
        return self._scene_code

    @scene_code.setter
    def scene_code(self, scene_code):
        r"""Sets the scene_code of this NetworkDeviceOffering.

        销售场景编码

        :param scene_code: The scene_code of this NetworkDeviceOffering.
        :type scene_code: str
        """
        self._scene_code = scene_code

    @property
    def status(self):
        r"""Gets the status of this NetworkDeviceOffering.

        商品状态说明：   - TESTING - 测试   - ONSALE - 在售   - SUSPENDED - 已停售   - RETIREMENT - 产品退出

        :return: The status of this NetworkDeviceOffering.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this NetworkDeviceOffering.

        商品状态说明：   - TESTING - 测试   - ONSALE - 在售   - SUSPENDED - 已停售   - RETIREMENT - 产品退出

        :param status: The status of this NetworkDeviceOffering.
        :type status: str
        """
        self._status = status

    @property
    def spec(self):
        r"""Gets the spec of this NetworkDeviceOffering.

        :return: The spec of this NetworkDeviceOffering.
        :rtype: :class:`huaweicloudsdkcloudpond.v2.NetworkDeviceSpec`
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        r"""Sets the spec of this NetworkDeviceOffering.

        :param spec: The spec of this NetworkDeviceOffering.
        :type spec: :class:`huaweicloudsdkcloudpond.v2.NetworkDeviceSpec`
        """
        self._spec = spec

    @property
    def product_info(self):
        r"""Gets the product_info of this NetworkDeviceOffering.

        :return: The product_info of this NetworkDeviceOffering.
        :rtype: :class:`huaweicloudsdkcloudpond.v2.ProductInfo`
        """
        return self._product_info

    @product_info.setter
    def product_info(self, product_info):
        r"""Sets the product_info of this NetworkDeviceOffering.

        :param product_info: The product_info of this NetworkDeviceOffering.
        :type product_info: :class:`huaweicloudsdkcloudpond.v2.ProductInfo`
        """
        self._product_info = product_info

    @property
    def sale_cycles(self):
        r"""Gets the sale_cycles of this NetworkDeviceOffering.

        :return: The sale_cycles of this NetworkDeviceOffering.
        :rtype: list[:class:`huaweicloudsdkcloudpond.v2.SaleCycle`]
        """
        return self._sale_cycles

    @sale_cycles.setter
    def sale_cycles(self, sale_cycles):
        r"""Sets the sale_cycles of this NetworkDeviceOffering.

        :param sale_cycles: The sale_cycles of this NetworkDeviceOffering.
        :type sale_cycles: list[:class:`huaweicloudsdkcloudpond.v2.SaleCycle`]
        """
        self._sale_cycles = sale_cycles

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
        if not isinstance(other, NetworkDeviceOffering):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
