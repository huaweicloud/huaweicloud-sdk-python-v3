# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BusinessDiscountQueryReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'quoting_item_type': 'str',
        'cloud_service_types': 'list[str]',
        'charging_modes': 'list[str]',
        'site_code': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'quoting_item_type': 'quoting_item_type',
        'cloud_service_types': 'cloud_service_types',
        'charging_modes': 'charging_modes',
        'site_code': 'site_code',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, quoting_item_type=None, cloud_service_types=None, charging_modes=None, site_code=None, offset=None, limit=None):
        r"""BusinessDiscountQueryReq

        The model defined in huaweicloud sdk

        :param quoting_item_type: 报价项类型，必填，PRODUCT_ITEM（产品报价项）/ CATEGORY_ITEM（分类报价项）
        :type quoting_item_type: str
        :param cloud_service_types: 云服务类型编码列表，非必填，大小写不敏感，数组范围限制:0-100，字符长度限制1-64。此参数不携带或携带值为空列表或携带值为null时，不作为筛选条件。
        :type cloud_service_types: list[str]
        :param charging_modes: 计费模式列表，非必填，大小写不敏感，数组范围限制:0-20，字符长度限制1-64。此参数不携带或携带值为空列表或携带值为null时，不作为筛选条件。
        :type charging_modes: list[str]
        :param site_code: 运营站点编码，非必填，大小写不敏感，字符长度限制1-64。此参数不携带或携带值为null时，不作为筛选条件。
        :type site_code: str
        :param offset: 分页偏移量，非必填，取值范围0-2147483647，默认值0
        :type offset: int
        :param limit: 查询条数，非必填，取值范围1-1000，默认值20
        :type limit: int
        """
        
        

        self._quoting_item_type = None
        self._cloud_service_types = None
        self._charging_modes = None
        self._site_code = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.quoting_item_type = quoting_item_type
        if cloud_service_types is not None:
            self.cloud_service_types = cloud_service_types
        if charging_modes is not None:
            self.charging_modes = charging_modes
        if site_code is not None:
            self.site_code = site_code
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def quoting_item_type(self):
        r"""Gets the quoting_item_type of this BusinessDiscountQueryReq.

        报价项类型，必填，PRODUCT_ITEM（产品报价项）/ CATEGORY_ITEM（分类报价项）

        :return: The quoting_item_type of this BusinessDiscountQueryReq.
        :rtype: str
        """
        return self._quoting_item_type

    @quoting_item_type.setter
    def quoting_item_type(self, quoting_item_type):
        r"""Sets the quoting_item_type of this BusinessDiscountQueryReq.

        报价项类型，必填，PRODUCT_ITEM（产品报价项）/ CATEGORY_ITEM（分类报价项）

        :param quoting_item_type: The quoting_item_type of this BusinessDiscountQueryReq.
        :type quoting_item_type: str
        """
        self._quoting_item_type = quoting_item_type

    @property
    def cloud_service_types(self):
        r"""Gets the cloud_service_types of this BusinessDiscountQueryReq.

        云服务类型编码列表，非必填，大小写不敏感，数组范围限制:0-100，字符长度限制1-64。此参数不携带或携带值为空列表或携带值为null时，不作为筛选条件。

        :return: The cloud_service_types of this BusinessDiscountQueryReq.
        :rtype: list[str]
        """
        return self._cloud_service_types

    @cloud_service_types.setter
    def cloud_service_types(self, cloud_service_types):
        r"""Sets the cloud_service_types of this BusinessDiscountQueryReq.

        云服务类型编码列表，非必填，大小写不敏感，数组范围限制:0-100，字符长度限制1-64。此参数不携带或携带值为空列表或携带值为null时，不作为筛选条件。

        :param cloud_service_types: The cloud_service_types of this BusinessDiscountQueryReq.
        :type cloud_service_types: list[str]
        """
        self._cloud_service_types = cloud_service_types

    @property
    def charging_modes(self):
        r"""Gets the charging_modes of this BusinessDiscountQueryReq.

        计费模式列表，非必填，大小写不敏感，数组范围限制:0-20，字符长度限制1-64。此参数不携带或携带值为空列表或携带值为null时，不作为筛选条件。

        :return: The charging_modes of this BusinessDiscountQueryReq.
        :rtype: list[str]
        """
        return self._charging_modes

    @charging_modes.setter
    def charging_modes(self, charging_modes):
        r"""Sets the charging_modes of this BusinessDiscountQueryReq.

        计费模式列表，非必填，大小写不敏感，数组范围限制:0-20，字符长度限制1-64。此参数不携带或携带值为空列表或携带值为null时，不作为筛选条件。

        :param charging_modes: The charging_modes of this BusinessDiscountQueryReq.
        :type charging_modes: list[str]
        """
        self._charging_modes = charging_modes

    @property
    def site_code(self):
        r"""Gets the site_code of this BusinessDiscountQueryReq.

        运营站点编码，非必填，大小写不敏感，字符长度限制1-64。此参数不携带或携带值为null时，不作为筛选条件。

        :return: The site_code of this BusinessDiscountQueryReq.
        :rtype: str
        """
        return self._site_code

    @site_code.setter
    def site_code(self, site_code):
        r"""Sets the site_code of this BusinessDiscountQueryReq.

        运营站点编码，非必填，大小写不敏感，字符长度限制1-64。此参数不携带或携带值为null时，不作为筛选条件。

        :param site_code: The site_code of this BusinessDiscountQueryReq.
        :type site_code: str
        """
        self._site_code = site_code

    @property
    def offset(self):
        r"""Gets the offset of this BusinessDiscountQueryReq.

        分页偏移量，非必填，取值范围0-2147483647，默认值0

        :return: The offset of this BusinessDiscountQueryReq.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this BusinessDiscountQueryReq.

        分页偏移量，非必填，取值范围0-2147483647，默认值0

        :param offset: The offset of this BusinessDiscountQueryReq.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this BusinessDiscountQueryReq.

        查询条数，非必填，取值范围1-1000，默认值20

        :return: The limit of this BusinessDiscountQueryReq.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this BusinessDiscountQueryReq.

        查询条数，非必填，取值范围1-1000，默认值20

        :param limit: The limit of this BusinessDiscountQueryReq.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, BusinessDiscountQueryReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
