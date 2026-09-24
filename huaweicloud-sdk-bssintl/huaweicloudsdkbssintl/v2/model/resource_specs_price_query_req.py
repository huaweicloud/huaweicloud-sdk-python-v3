# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourceSpecsPriceQueryReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cloud_service_type': 'str',
        'resource_type': 'str',
        'region_code': 'str',
        'filters': 'list[ResourceSpecsPriceFilter]',
        'need_attributes': 'bool',
        'need_price': 'bool',
        'marker': 'str',
        'limit': 'int'
    }

    attribute_map = {
        'cloud_service_type': 'cloud_service_type',
        'resource_type': 'resource_type',
        'region_code': 'region_code',
        'filters': 'filters',
        'need_attributes': 'need_attributes',
        'need_price': 'need_price',
        'marker': 'marker',
        'limit': 'limit'
    }

    def __init__(self, cloud_service_type=None, resource_type=None, region_code=None, filters=None, need_attributes=None, need_price=None, marker=None, limit=None):
        r"""ResourceSpecsPriceQueryReq

        The model defined in huaweicloud sdk

        :param cloud_service_type: 云服务类型编码，非必填，范围1-64，此参数不携带或携带值为null时，不作为筛选条件。
        :type cloud_service_type: str
        :param resource_type: 资源类型编码，非必填，范围1-64，此参数不携带或携带值为null时，不作为筛选条件。
        :type resource_type: str
        :param region_code: 区域编码，必填，范围1-64。
        :type region_code: str
        :param filters: 过滤条件列表，非必填，最多1个。此参数不携带或携带值为空列表或携带值为null时，不作为筛选条件。
        :type filters: list[:class:`huaweicloudsdkbssintl.v2.ResourceSpecsPriceFilter`]
        :param need_attributes: 是否返回资源规格属性信息，非必填，false：不返回（默认）true：返回
        :type need_attributes: bool
        :param need_price: 是否返回资源规格官网定价信息，非必填，false：不返回（默认）true：返回
        :type need_price: bool
        :param marker: 翻页信息，非必填，首页查询不携带此参数或携带值为null，非首页查询传入上一页响应返回的next_marker
        :type marker: str
        :param limit: 查询条数，非必填，取值范围1-50，默认值50
        :type limit: int
        """
        
        

        self._cloud_service_type = None
        self._resource_type = None
        self._region_code = None
        self._filters = None
        self._need_attributes = None
        self._need_price = None
        self._marker = None
        self._limit = None
        self.discriminator = None

        if cloud_service_type is not None:
            self.cloud_service_type = cloud_service_type
        if resource_type is not None:
            self.resource_type = resource_type
        self.region_code = region_code
        if filters is not None:
            self.filters = filters
        if need_attributes is not None:
            self.need_attributes = need_attributes
        if need_price is not None:
            self.need_price = need_price
        if marker is not None:
            self.marker = marker
        if limit is not None:
            self.limit = limit

    @property
    def cloud_service_type(self):
        r"""Gets the cloud_service_type of this ResourceSpecsPriceQueryReq.

        云服务类型编码，非必填，范围1-64，此参数不携带或携带值为null时，不作为筛选条件。

        :return: The cloud_service_type of this ResourceSpecsPriceQueryReq.
        :rtype: str
        """
        return self._cloud_service_type

    @cloud_service_type.setter
    def cloud_service_type(self, cloud_service_type):
        r"""Sets the cloud_service_type of this ResourceSpecsPriceQueryReq.

        云服务类型编码，非必填，范围1-64，此参数不携带或携带值为null时，不作为筛选条件。

        :param cloud_service_type: The cloud_service_type of this ResourceSpecsPriceQueryReq.
        :type cloud_service_type: str
        """
        self._cloud_service_type = cloud_service_type

    @property
    def resource_type(self):
        r"""Gets the resource_type of this ResourceSpecsPriceQueryReq.

        资源类型编码，非必填，范围1-64，此参数不携带或携带值为null时，不作为筛选条件。

        :return: The resource_type of this ResourceSpecsPriceQueryReq.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this ResourceSpecsPriceQueryReq.

        资源类型编码，非必填，范围1-64，此参数不携带或携带值为null时，不作为筛选条件。

        :param resource_type: The resource_type of this ResourceSpecsPriceQueryReq.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def region_code(self):
        r"""Gets the region_code of this ResourceSpecsPriceQueryReq.

        区域编码，必填，范围1-64。

        :return: The region_code of this ResourceSpecsPriceQueryReq.
        :rtype: str
        """
        return self._region_code

    @region_code.setter
    def region_code(self, region_code):
        r"""Sets the region_code of this ResourceSpecsPriceQueryReq.

        区域编码，必填，范围1-64。

        :param region_code: The region_code of this ResourceSpecsPriceQueryReq.
        :type region_code: str
        """
        self._region_code = region_code

    @property
    def filters(self):
        r"""Gets the filters of this ResourceSpecsPriceQueryReq.

        过滤条件列表，非必填，最多1个。此参数不携带或携带值为空列表或携带值为null时，不作为筛选条件。

        :return: The filters of this ResourceSpecsPriceQueryReq.
        :rtype: list[:class:`huaweicloudsdkbssintl.v2.ResourceSpecsPriceFilter`]
        """
        return self._filters

    @filters.setter
    def filters(self, filters):
        r"""Sets the filters of this ResourceSpecsPriceQueryReq.

        过滤条件列表，非必填，最多1个。此参数不携带或携带值为空列表或携带值为null时，不作为筛选条件。

        :param filters: The filters of this ResourceSpecsPriceQueryReq.
        :type filters: list[:class:`huaweicloudsdkbssintl.v2.ResourceSpecsPriceFilter`]
        """
        self._filters = filters

    @property
    def need_attributes(self):
        r"""Gets the need_attributes of this ResourceSpecsPriceQueryReq.

        是否返回资源规格属性信息，非必填，false：不返回（默认）true：返回

        :return: The need_attributes of this ResourceSpecsPriceQueryReq.
        :rtype: bool
        """
        return self._need_attributes

    @need_attributes.setter
    def need_attributes(self, need_attributes):
        r"""Sets the need_attributes of this ResourceSpecsPriceQueryReq.

        是否返回资源规格属性信息，非必填，false：不返回（默认）true：返回

        :param need_attributes: The need_attributes of this ResourceSpecsPriceQueryReq.
        :type need_attributes: bool
        """
        self._need_attributes = need_attributes

    @property
    def need_price(self):
        r"""Gets the need_price of this ResourceSpecsPriceQueryReq.

        是否返回资源规格官网定价信息，非必填，false：不返回（默认）true：返回

        :return: The need_price of this ResourceSpecsPriceQueryReq.
        :rtype: bool
        """
        return self._need_price

    @need_price.setter
    def need_price(self, need_price):
        r"""Sets the need_price of this ResourceSpecsPriceQueryReq.

        是否返回资源规格官网定价信息，非必填，false：不返回（默认）true：返回

        :param need_price: The need_price of this ResourceSpecsPriceQueryReq.
        :type need_price: bool
        """
        self._need_price = need_price

    @property
    def marker(self):
        r"""Gets the marker of this ResourceSpecsPriceQueryReq.

        翻页信息，非必填，首页查询不携带此参数或携带值为null，非首页查询传入上一页响应返回的next_marker

        :return: The marker of this ResourceSpecsPriceQueryReq.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ResourceSpecsPriceQueryReq.

        翻页信息，非必填，首页查询不携带此参数或携带值为null，非首页查询传入上一页响应返回的next_marker

        :param marker: The marker of this ResourceSpecsPriceQueryReq.
        :type marker: str
        """
        self._marker = marker

    @property
    def limit(self):
        r"""Gets the limit of this ResourceSpecsPriceQueryReq.

        查询条数，非必填，取值范围1-50，默认值50

        :return: The limit of this ResourceSpecsPriceQueryReq.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ResourceSpecsPriceQueryReq.

        查询条数，非必填，取值范围1-50，默认值50

        :param limit: The limit of this ResourceSpecsPriceQueryReq.
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
        if not isinstance(other, ResourceSpecsPriceQueryReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
