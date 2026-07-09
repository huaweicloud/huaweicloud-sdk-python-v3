# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourceSpecsQueryReq:

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
        'charge_mode': 'str',
        'filters': 'list[ResourceSpecsFilter]',
        'marker': 'str',
        'limit': 'int'
    }

    attribute_map = {
        'cloud_service_type': 'cloud_service_type',
        'resource_type': 'resource_type',
        'region_code': 'region_code',
        'charge_mode': 'charge_mode',
        'filters': 'filters',
        'marker': 'marker',
        'limit': 'limit'
    }

    def __init__(self, cloud_service_type=None, resource_type=None, region_code=None, charge_mode=None, filters=None, marker=None, limit=None):
        r"""ResourceSpecsQueryReq

        The model defined in huaweicloud sdk

        :param cloud_service_type: |参数名称：云服务类型编码| |参数的约束及描述：必填，云服务类型编码|
        :type cloud_service_type: str
        :param resource_type: |参数名称：资源类型编码| |参数的约束及描述：必填，资源类型编码|
        :type resource_type: str
        :param region_code: |参数名称：区域编码| |参数的约束及描述：必填，区域编码|
        :type region_code: str
        :param charge_mode: |参数名称：计费模式| |参数的约束及描述：必填，1：包年/包月，3：按需|
        :type charge_mode: str
        :param filters: |参数名称：过滤条件| |参数的约束及描述：非必填，过滤条件列表，最多1个|
        :type filters: list[:class:`huaweicloudsdkbssintl.v2.ResourceSpecsFilter`]
        :param marker: |参数名称：翻页信息| |参数的约束及描述：非必填，首页查询不携带此参数，非首页查询传入上一页响应返回的next_marker|
        :type marker: str
        :param limit: |参数名称：查询条数| |参数的约束及描述：非必填，取值范围1-100，默认值100|
        :type limit: int
        """
        
        

        self._cloud_service_type = None
        self._resource_type = None
        self._region_code = None
        self._charge_mode = None
        self._filters = None
        self._marker = None
        self._limit = None
        self.discriminator = None

        self.cloud_service_type = cloud_service_type
        self.resource_type = resource_type
        self.region_code = region_code
        self.charge_mode = charge_mode
        if filters is not None:
            self.filters = filters
        if marker is not None:
            self.marker = marker
        if limit is not None:
            self.limit = limit

    @property
    def cloud_service_type(self):
        r"""Gets the cloud_service_type of this ResourceSpecsQueryReq.

        |参数名称：云服务类型编码| |参数的约束及描述：必填，云服务类型编码|

        :return: The cloud_service_type of this ResourceSpecsQueryReq.
        :rtype: str
        """
        return self._cloud_service_type

    @cloud_service_type.setter
    def cloud_service_type(self, cloud_service_type):
        r"""Sets the cloud_service_type of this ResourceSpecsQueryReq.

        |参数名称：云服务类型编码| |参数的约束及描述：必填，云服务类型编码|

        :param cloud_service_type: The cloud_service_type of this ResourceSpecsQueryReq.
        :type cloud_service_type: str
        """
        self._cloud_service_type = cloud_service_type

    @property
    def resource_type(self):
        r"""Gets the resource_type of this ResourceSpecsQueryReq.

        |参数名称：资源类型编码| |参数的约束及描述：必填，资源类型编码|

        :return: The resource_type of this ResourceSpecsQueryReq.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this ResourceSpecsQueryReq.

        |参数名称：资源类型编码| |参数的约束及描述：必填，资源类型编码|

        :param resource_type: The resource_type of this ResourceSpecsQueryReq.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def region_code(self):
        r"""Gets the region_code of this ResourceSpecsQueryReq.

        |参数名称：区域编码| |参数的约束及描述：必填，区域编码|

        :return: The region_code of this ResourceSpecsQueryReq.
        :rtype: str
        """
        return self._region_code

    @region_code.setter
    def region_code(self, region_code):
        r"""Sets the region_code of this ResourceSpecsQueryReq.

        |参数名称：区域编码| |参数的约束及描述：必填，区域编码|

        :param region_code: The region_code of this ResourceSpecsQueryReq.
        :type region_code: str
        """
        self._region_code = region_code

    @property
    def charge_mode(self):
        r"""Gets the charge_mode of this ResourceSpecsQueryReq.

        |参数名称：计费模式| |参数的约束及描述：必填，1：包年/包月，3：按需|

        :return: The charge_mode of this ResourceSpecsQueryReq.
        :rtype: str
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        r"""Sets the charge_mode of this ResourceSpecsQueryReq.

        |参数名称：计费模式| |参数的约束及描述：必填，1：包年/包月，3：按需|

        :param charge_mode: The charge_mode of this ResourceSpecsQueryReq.
        :type charge_mode: str
        """
        self._charge_mode = charge_mode

    @property
    def filters(self):
        r"""Gets the filters of this ResourceSpecsQueryReq.

        |参数名称：过滤条件| |参数的约束及描述：非必填，过滤条件列表，最多1个|

        :return: The filters of this ResourceSpecsQueryReq.
        :rtype: list[:class:`huaweicloudsdkbssintl.v2.ResourceSpecsFilter`]
        """
        return self._filters

    @filters.setter
    def filters(self, filters):
        r"""Sets the filters of this ResourceSpecsQueryReq.

        |参数名称：过滤条件| |参数的约束及描述：非必填，过滤条件列表，最多1个|

        :param filters: The filters of this ResourceSpecsQueryReq.
        :type filters: list[:class:`huaweicloudsdkbssintl.v2.ResourceSpecsFilter`]
        """
        self._filters = filters

    @property
    def marker(self):
        r"""Gets the marker of this ResourceSpecsQueryReq.

        |参数名称：翻页信息| |参数的约束及描述：非必填，首页查询不携带此参数，非首页查询传入上一页响应返回的next_marker|

        :return: The marker of this ResourceSpecsQueryReq.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ResourceSpecsQueryReq.

        |参数名称：翻页信息| |参数的约束及描述：非必填，首页查询不携带此参数，非首页查询传入上一页响应返回的next_marker|

        :param marker: The marker of this ResourceSpecsQueryReq.
        :type marker: str
        """
        self._marker = marker

    @property
    def limit(self):
        r"""Gets the limit of this ResourceSpecsQueryReq.

        |参数名称：查询条数| |参数的约束及描述：非必填，取值范围1-100，默认值100|

        :return: The limit of this ResourceSpecsQueryReq.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ResourceSpecsQueryReq.

        |参数名称：查询条数| |参数的约束及描述：非必填，取值范围1-100，默认值100|

        :param limit: The limit of this ResourceSpecsQueryReq.
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
        if not isinstance(other, ResourceSpecsQueryReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
