# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFreeResourcesUsageRecordsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'free_resource_id': 'str',
        'product_id': 'str',
        'resource_type_code': 'str',
        'deduct_time_begin': 'str',
        'deduct_time_end': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'free_resource_id': 'free_resource_id',
        'product_id': 'product_id',
        'resource_type_code': 'resource_type_code',
        'deduct_time_begin': 'deduct_time_begin',
        'deduct_time_end': 'deduct_time_end',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, free_resource_id=None, product_id=None, resource_type_code=None, deduct_time_begin=None, deduct_time_end=None, offset=None, limit=None):
        r"""ListFreeResourcesUsageRecordsRequest

        The model defined in huaweicloud sdk

        :param free_resource_id: 资源项ID，一个资源包中会含有多个资源项，一个使用量类型对应一个资源项。资源项ID来自查询资源包列表接口的响应。 此参数不携带或携带值为空时，不作为筛选条件。
        :type free_resource_id: str
        :param product_id: 产品ID，即资源包ID。 此参数不携带或携带值为空时，不作为筛选条件。
        :type product_id: str
        :param resource_type_code: 资源类型编码，例如ECS的VM为“hws.resource.type.vm”。您可以调用查询资源类型列表接口获取。 此参数不携带或携带值为空时，不作为筛选条件。
        :type resource_type_code: str
        :param deduct_time_begin: 资源抵扣的起始时间。东八区时间，格式为YYYY-MM-DD。
        :type deduct_time_begin: str
        :param deduct_time_end: 资源抵扣的结束时间。东八区时间，格式为YYYY-MM-DD。  说明： 抵扣结束时间-抵扣起始时间&lt;&#x3D;90天。
        :type deduct_time_end: str
        :param offset: 偏移量，从0开始。默认值为0。  说明： offset用于分页处理，如不涉及分页，请使用默认值0。offset表示相对于满足条件的第一个数据的偏移量。如offset &#x3D; 1，则返回满足条件的第二个数据至最后一个数据。 例如，满足查询条件的结果共10条数据，limit取值为10，offset取值为1，则返回的数据为2~10，第一条数据不返回。
        :type offset: int
        :param limit: 每次查询的数量限制。默认值为10。
        :type limit: int
        """
        
        

        self._free_resource_id = None
        self._product_id = None
        self._resource_type_code = None
        self._deduct_time_begin = None
        self._deduct_time_end = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if free_resource_id is not None:
            self.free_resource_id = free_resource_id
        if product_id is not None:
            self.product_id = product_id
        if resource_type_code is not None:
            self.resource_type_code = resource_type_code
        self.deduct_time_begin = deduct_time_begin
        self.deduct_time_end = deduct_time_end
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def free_resource_id(self):
        r"""Gets the free_resource_id of this ListFreeResourcesUsageRecordsRequest.

        资源项ID，一个资源包中会含有多个资源项，一个使用量类型对应一个资源项。资源项ID来自查询资源包列表接口的响应。 此参数不携带或携带值为空时，不作为筛选条件。

        :return: The free_resource_id of this ListFreeResourcesUsageRecordsRequest.
        :rtype: str
        """
        return self._free_resource_id

    @free_resource_id.setter
    def free_resource_id(self, free_resource_id):
        r"""Sets the free_resource_id of this ListFreeResourcesUsageRecordsRequest.

        资源项ID，一个资源包中会含有多个资源项，一个使用量类型对应一个资源项。资源项ID来自查询资源包列表接口的响应。 此参数不携带或携带值为空时，不作为筛选条件。

        :param free_resource_id: The free_resource_id of this ListFreeResourcesUsageRecordsRequest.
        :type free_resource_id: str
        """
        self._free_resource_id = free_resource_id

    @property
    def product_id(self):
        r"""Gets the product_id of this ListFreeResourcesUsageRecordsRequest.

        产品ID，即资源包ID。 此参数不携带或携带值为空时，不作为筛选条件。

        :return: The product_id of this ListFreeResourcesUsageRecordsRequest.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        r"""Sets the product_id of this ListFreeResourcesUsageRecordsRequest.

        产品ID，即资源包ID。 此参数不携带或携带值为空时，不作为筛选条件。

        :param product_id: The product_id of this ListFreeResourcesUsageRecordsRequest.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def resource_type_code(self):
        r"""Gets the resource_type_code of this ListFreeResourcesUsageRecordsRequest.

        资源类型编码，例如ECS的VM为“hws.resource.type.vm”。您可以调用查询资源类型列表接口获取。 此参数不携带或携带值为空时，不作为筛选条件。

        :return: The resource_type_code of this ListFreeResourcesUsageRecordsRequest.
        :rtype: str
        """
        return self._resource_type_code

    @resource_type_code.setter
    def resource_type_code(self, resource_type_code):
        r"""Sets the resource_type_code of this ListFreeResourcesUsageRecordsRequest.

        资源类型编码，例如ECS的VM为“hws.resource.type.vm”。您可以调用查询资源类型列表接口获取。 此参数不携带或携带值为空时，不作为筛选条件。

        :param resource_type_code: The resource_type_code of this ListFreeResourcesUsageRecordsRequest.
        :type resource_type_code: str
        """
        self._resource_type_code = resource_type_code

    @property
    def deduct_time_begin(self):
        r"""Gets the deduct_time_begin of this ListFreeResourcesUsageRecordsRequest.

        资源抵扣的起始时间。东八区时间，格式为YYYY-MM-DD。

        :return: The deduct_time_begin of this ListFreeResourcesUsageRecordsRequest.
        :rtype: str
        """
        return self._deduct_time_begin

    @deduct_time_begin.setter
    def deduct_time_begin(self, deduct_time_begin):
        r"""Sets the deduct_time_begin of this ListFreeResourcesUsageRecordsRequest.

        资源抵扣的起始时间。东八区时间，格式为YYYY-MM-DD。

        :param deduct_time_begin: The deduct_time_begin of this ListFreeResourcesUsageRecordsRequest.
        :type deduct_time_begin: str
        """
        self._deduct_time_begin = deduct_time_begin

    @property
    def deduct_time_end(self):
        r"""Gets the deduct_time_end of this ListFreeResourcesUsageRecordsRequest.

        资源抵扣的结束时间。东八区时间，格式为YYYY-MM-DD。  说明： 抵扣结束时间-抵扣起始时间<=90天。

        :return: The deduct_time_end of this ListFreeResourcesUsageRecordsRequest.
        :rtype: str
        """
        return self._deduct_time_end

    @deduct_time_end.setter
    def deduct_time_end(self, deduct_time_end):
        r"""Sets the deduct_time_end of this ListFreeResourcesUsageRecordsRequest.

        资源抵扣的结束时间。东八区时间，格式为YYYY-MM-DD。  说明： 抵扣结束时间-抵扣起始时间<=90天。

        :param deduct_time_end: The deduct_time_end of this ListFreeResourcesUsageRecordsRequest.
        :type deduct_time_end: str
        """
        self._deduct_time_end = deduct_time_end

    @property
    def offset(self):
        r"""Gets the offset of this ListFreeResourcesUsageRecordsRequest.

        偏移量，从0开始。默认值为0。  说明： offset用于分页处理，如不涉及分页，请使用默认值0。offset表示相对于满足条件的第一个数据的偏移量。如offset = 1，则返回满足条件的第二个数据至最后一个数据。 例如，满足查询条件的结果共10条数据，limit取值为10，offset取值为1，则返回的数据为2~10，第一条数据不返回。

        :return: The offset of this ListFreeResourcesUsageRecordsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListFreeResourcesUsageRecordsRequest.

        偏移量，从0开始。默认值为0。  说明： offset用于分页处理，如不涉及分页，请使用默认值0。offset表示相对于满足条件的第一个数据的偏移量。如offset = 1，则返回满足条件的第二个数据至最后一个数据。 例如，满足查询条件的结果共10条数据，limit取值为10，offset取值为1，则返回的数据为2~10，第一条数据不返回。

        :param offset: The offset of this ListFreeResourcesUsageRecordsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListFreeResourcesUsageRecordsRequest.

        每次查询的数量限制。默认值为10。

        :return: The limit of this ListFreeResourcesUsageRecordsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListFreeResourcesUsageRecordsRequest.

        每次查询的数量限制。默认值为10。

        :param limit: The limit of this ListFreeResourcesUsageRecordsRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListFreeResourcesUsageRecordsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
