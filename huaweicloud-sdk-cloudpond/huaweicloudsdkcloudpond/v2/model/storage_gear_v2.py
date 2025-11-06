# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StorageGearV2:

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
        'gear': 'int',
        'storage_type': 'str',
        'product_info': 'ProductInfo',
        'zone_code': 'str',
        'sale_cycles': 'list[SaleCycle]'
    }

    attribute_map = {
        'id': 'id',
        'gear': 'gear',
        'storage_type': 'storage_type',
        'product_info': 'product_info',
        'zone_code': 'zone_code',
        'sale_cycles': 'sale_cycles'
    }

    def __init__(self, id=None, gear=None, storage_type=None, product_info=None, zone_code=None, sale_cycles=None):
        r"""StorageGearV2

        The model defined in huaweicloud sdk

        :param id: 存储档位ID
        :type id: str
        :param gear: 存储阶梯值, 如：35TB
        :type gear: int
        :param storage_type: 存储类型. SAS:高IO,SSD:超高IO [VS_SMALL_CAP,VS_MEDIUM_CAP,VS_LARGE_CAP 视图存储](tag:cmcc)
        :type storage_type: str
        :param product_info: 
        :type product_info: :class:`huaweicloudsdkcloudpond.v2.ProductInfo`
        :param zone_code: 部署地区
        :type zone_code: str
        :param sale_cycles: 
        :type sale_cycles: list[:class:`huaweicloudsdkcloudpond.v2.SaleCycle`]
        """
        
        

        self._id = None
        self._gear = None
        self._storage_type = None
        self._product_info = None
        self._zone_code = None
        self._sale_cycles = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if gear is not None:
            self.gear = gear
        if storage_type is not None:
            self.storage_type = storage_type
        if product_info is not None:
            self.product_info = product_info
        if zone_code is not None:
            self.zone_code = zone_code
        if sale_cycles is not None:
            self.sale_cycles = sale_cycles

    @property
    def id(self):
        r"""Gets the id of this StorageGearV2.

        存储档位ID

        :return: The id of this StorageGearV2.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this StorageGearV2.

        存储档位ID

        :param id: The id of this StorageGearV2.
        :type id: str
        """
        self._id = id

    @property
    def gear(self):
        r"""Gets the gear of this StorageGearV2.

        存储阶梯值, 如：35TB

        :return: The gear of this StorageGearV2.
        :rtype: int
        """
        return self._gear

    @gear.setter
    def gear(self, gear):
        r"""Sets the gear of this StorageGearV2.

        存储阶梯值, 如：35TB

        :param gear: The gear of this StorageGearV2.
        :type gear: int
        """
        self._gear = gear

    @property
    def storage_type(self):
        r"""Gets the storage_type of this StorageGearV2.

        存储类型. SAS:高IO,SSD:超高IO [VS_SMALL_CAP,VS_MEDIUM_CAP,VS_LARGE_CAP 视图存储](tag:cmcc)

        :return: The storage_type of this StorageGearV2.
        :rtype: str
        """
        return self._storage_type

    @storage_type.setter
    def storage_type(self, storage_type):
        r"""Sets the storage_type of this StorageGearV2.

        存储类型. SAS:高IO,SSD:超高IO [VS_SMALL_CAP,VS_MEDIUM_CAP,VS_LARGE_CAP 视图存储](tag:cmcc)

        :param storage_type: The storage_type of this StorageGearV2.
        :type storage_type: str
        """
        self._storage_type = storage_type

    @property
    def product_info(self):
        r"""Gets the product_info of this StorageGearV2.

        :return: The product_info of this StorageGearV2.
        :rtype: :class:`huaweicloudsdkcloudpond.v2.ProductInfo`
        """
        return self._product_info

    @product_info.setter
    def product_info(self, product_info):
        r"""Sets the product_info of this StorageGearV2.

        :param product_info: The product_info of this StorageGearV2.
        :type product_info: :class:`huaweicloudsdkcloudpond.v2.ProductInfo`
        """
        self._product_info = product_info

    @property
    def zone_code(self):
        r"""Gets the zone_code of this StorageGearV2.

        部署地区

        :return: The zone_code of this StorageGearV2.
        :rtype: str
        """
        return self._zone_code

    @zone_code.setter
    def zone_code(self, zone_code):
        r"""Sets the zone_code of this StorageGearV2.

        部署地区

        :param zone_code: The zone_code of this StorageGearV2.
        :type zone_code: str
        """
        self._zone_code = zone_code

    @property
    def sale_cycles(self):
        r"""Gets the sale_cycles of this StorageGearV2.

        :return: The sale_cycles of this StorageGearV2.
        :rtype: list[:class:`huaweicloudsdkcloudpond.v2.SaleCycle`]
        """
        return self._sale_cycles

    @sale_cycles.setter
    def sale_cycles(self, sale_cycles):
        r"""Sets the sale_cycles of this StorageGearV2.

        :param sale_cycles: The sale_cycles of this StorageGearV2.
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
        if not isinstance(other, StorageGearV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
