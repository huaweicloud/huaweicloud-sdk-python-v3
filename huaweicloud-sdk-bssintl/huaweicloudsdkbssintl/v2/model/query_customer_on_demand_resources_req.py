# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryCustomerOnDemandResourcesReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'customer_id': 'str',
        'region_code': 'str',
        'service_type_code': 'str',
        'resource_ids': 'list[str]',
        'effective_time_begin': 'str',
        'effective_time_end': 'str',
        'offset': 'int',
        'limit': 'int',
        'status': 'int',
        'indirect_partner_id': 'str'
    }

    attribute_map = {
        'customer_id': 'customer_id',
        'region_code': 'region_code',
        'service_type_code': 'service_type_code',
        'resource_ids': 'resource_ids',
        'effective_time_begin': 'effective_time_begin',
        'effective_time_end': 'effective_time_end',
        'offset': 'offset',
        'limit': 'limit',
        'status': 'status',
        'indirect_partner_id': 'indirect_partner_id'
    }

    def __init__(self, customer_id=None, region_code=None, service_type_code=None, resource_ids=None, effective_time_begin=None, effective_time_end=None, offset=None, limit=None, status=None, indirect_partner_id=None):
        """QueryCustomerOnDemandResourcesReq

        The model defined in huaweicloud sdk

        :param customer_id: 客户账号ID。 您可以调用查询客户列表接口获取customer_id。
        :type customer_id: str
        :param region_code: 云服务区编码，例如：“ap-southeast-1”。具体请参见地区和终端节点对应云服务的“区域”列的值。
        :type region_code: str
        :param service_type_code: 云服务类型编码，例如OBS的云服务类型编码为“hws.service.type.obs”。您可以调用查询云服务类型列表接口获取。
        :type service_type_code: str
        :param resource_ids: 资源ID批量查询。 用于查询指定资源ID对应的资源。 最多支持同时传递50个ID的列表。
        :type resource_ids: list[str]
        :param effective_time_begin: 生效时间的开始时间。 UTC时间，格式：yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39;，如“2019-05-06T08:05:01Z”。 其中，HH范围是0～23，mm和ss范围是0～59。
        :type effective_time_begin: str
        :param effective_time_end: 生效时间的结束时间 UTC时间，格式：yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39;，如“2019-05-06T08:05:01Z”。 其中，HH范围是0～23，mm和ss范围是0～59。
        :type effective_time_end: str
        :param offset: 偏移量，从0开始。默认值为0。  说明： offset用于分页处理，如不涉及分页，请使用默认值0。offset表示相对于满足条件的第一个数据的偏移量。如offset &#x3D; 1，则返回满足条件的第二个数据至最后一个数据。 例如，满足查询条件的结果共10条数据，limit取值为10，offset取值为1，则返回的数据为2~10，第一条数据不返回。
        :type offset: int
        :param limit: 一次查询的条数，默认值为10。
        :type limit: int
        :param status: 资源状态： 1：正常（已开通）2：宽限期3：冻结中4：变更中5：正在关闭6：已关闭
        :type status: int
        :param indirect_partner_id: 云经销商ID。如果需要查询云经销商子客户的按需资源列表，必须携带该字段，除此之外，此参数不做处理。否则只能查询自己的子客户按需资源。
        :type indirect_partner_id: str
        """
        
        

        self._customer_id = None
        self._region_code = None
        self._service_type_code = None
        self._resource_ids = None
        self._effective_time_begin = None
        self._effective_time_end = None
        self._offset = None
        self._limit = None
        self._status = None
        self._indirect_partner_id = None
        self.discriminator = None

        self.customer_id = customer_id
        if region_code is not None:
            self.region_code = region_code
        if service_type_code is not None:
            self.service_type_code = service_type_code
        if resource_ids is not None:
            self.resource_ids = resource_ids
        if effective_time_begin is not None:
            self.effective_time_begin = effective_time_begin
        if effective_time_end is not None:
            self.effective_time_end = effective_time_end
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if status is not None:
            self.status = status
        if indirect_partner_id is not None:
            self.indirect_partner_id = indirect_partner_id

    @property
    def customer_id(self):
        """Gets the customer_id of this QueryCustomerOnDemandResourcesReq.

        客户账号ID。 您可以调用查询客户列表接口获取customer_id。

        :return: The customer_id of this QueryCustomerOnDemandResourcesReq.
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this QueryCustomerOnDemandResourcesReq.

        客户账号ID。 您可以调用查询客户列表接口获取customer_id。

        :param customer_id: The customer_id of this QueryCustomerOnDemandResourcesReq.
        :type customer_id: str
        """
        self._customer_id = customer_id

    @property
    def region_code(self):
        """Gets the region_code of this QueryCustomerOnDemandResourcesReq.

        云服务区编码，例如：“ap-southeast-1”。具体请参见地区和终端节点对应云服务的“区域”列的值。

        :return: The region_code of this QueryCustomerOnDemandResourcesReq.
        :rtype: str
        """
        return self._region_code

    @region_code.setter
    def region_code(self, region_code):
        """Sets the region_code of this QueryCustomerOnDemandResourcesReq.

        云服务区编码，例如：“ap-southeast-1”。具体请参见地区和终端节点对应云服务的“区域”列的值。

        :param region_code: The region_code of this QueryCustomerOnDemandResourcesReq.
        :type region_code: str
        """
        self._region_code = region_code

    @property
    def service_type_code(self):
        """Gets the service_type_code of this QueryCustomerOnDemandResourcesReq.

        云服务类型编码，例如OBS的云服务类型编码为“hws.service.type.obs”。您可以调用查询云服务类型列表接口获取。

        :return: The service_type_code of this QueryCustomerOnDemandResourcesReq.
        :rtype: str
        """
        return self._service_type_code

    @service_type_code.setter
    def service_type_code(self, service_type_code):
        """Sets the service_type_code of this QueryCustomerOnDemandResourcesReq.

        云服务类型编码，例如OBS的云服务类型编码为“hws.service.type.obs”。您可以调用查询云服务类型列表接口获取。

        :param service_type_code: The service_type_code of this QueryCustomerOnDemandResourcesReq.
        :type service_type_code: str
        """
        self._service_type_code = service_type_code

    @property
    def resource_ids(self):
        """Gets the resource_ids of this QueryCustomerOnDemandResourcesReq.

        资源ID批量查询。 用于查询指定资源ID对应的资源。 最多支持同时传递50个ID的列表。

        :return: The resource_ids of this QueryCustomerOnDemandResourcesReq.
        :rtype: list[str]
        """
        return self._resource_ids

    @resource_ids.setter
    def resource_ids(self, resource_ids):
        """Sets the resource_ids of this QueryCustomerOnDemandResourcesReq.

        资源ID批量查询。 用于查询指定资源ID对应的资源。 最多支持同时传递50个ID的列表。

        :param resource_ids: The resource_ids of this QueryCustomerOnDemandResourcesReq.
        :type resource_ids: list[str]
        """
        self._resource_ids = resource_ids

    @property
    def effective_time_begin(self):
        """Gets the effective_time_begin of this QueryCustomerOnDemandResourcesReq.

        生效时间的开始时间。 UTC时间，格式：yyyy-MM-dd'T'HH:mm:ss'Z'，如“2019-05-06T08:05:01Z”。 其中，HH范围是0～23，mm和ss范围是0～59。

        :return: The effective_time_begin of this QueryCustomerOnDemandResourcesReq.
        :rtype: str
        """
        return self._effective_time_begin

    @effective_time_begin.setter
    def effective_time_begin(self, effective_time_begin):
        """Sets the effective_time_begin of this QueryCustomerOnDemandResourcesReq.

        生效时间的开始时间。 UTC时间，格式：yyyy-MM-dd'T'HH:mm:ss'Z'，如“2019-05-06T08:05:01Z”。 其中，HH范围是0～23，mm和ss范围是0～59。

        :param effective_time_begin: The effective_time_begin of this QueryCustomerOnDemandResourcesReq.
        :type effective_time_begin: str
        """
        self._effective_time_begin = effective_time_begin

    @property
    def effective_time_end(self):
        """Gets the effective_time_end of this QueryCustomerOnDemandResourcesReq.

        生效时间的结束时间 UTC时间，格式：yyyy-MM-dd'T'HH:mm:ss'Z'，如“2019-05-06T08:05:01Z”。 其中，HH范围是0～23，mm和ss范围是0～59。

        :return: The effective_time_end of this QueryCustomerOnDemandResourcesReq.
        :rtype: str
        """
        return self._effective_time_end

    @effective_time_end.setter
    def effective_time_end(self, effective_time_end):
        """Sets the effective_time_end of this QueryCustomerOnDemandResourcesReq.

        生效时间的结束时间 UTC时间，格式：yyyy-MM-dd'T'HH:mm:ss'Z'，如“2019-05-06T08:05:01Z”。 其中，HH范围是0～23，mm和ss范围是0～59。

        :param effective_time_end: The effective_time_end of this QueryCustomerOnDemandResourcesReq.
        :type effective_time_end: str
        """
        self._effective_time_end = effective_time_end

    @property
    def offset(self):
        """Gets the offset of this QueryCustomerOnDemandResourcesReq.

        偏移量，从0开始。默认值为0。  说明： offset用于分页处理，如不涉及分页，请使用默认值0。offset表示相对于满足条件的第一个数据的偏移量。如offset = 1，则返回满足条件的第二个数据至最后一个数据。 例如，满足查询条件的结果共10条数据，limit取值为10，offset取值为1，则返回的数据为2~10，第一条数据不返回。

        :return: The offset of this QueryCustomerOnDemandResourcesReq.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this QueryCustomerOnDemandResourcesReq.

        偏移量，从0开始。默认值为0。  说明： offset用于分页处理，如不涉及分页，请使用默认值0。offset表示相对于满足条件的第一个数据的偏移量。如offset = 1，则返回满足条件的第二个数据至最后一个数据。 例如，满足查询条件的结果共10条数据，limit取值为10，offset取值为1，则返回的数据为2~10，第一条数据不返回。

        :param offset: The offset of this QueryCustomerOnDemandResourcesReq.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this QueryCustomerOnDemandResourcesReq.

        一次查询的条数，默认值为10。

        :return: The limit of this QueryCustomerOnDemandResourcesReq.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this QueryCustomerOnDemandResourcesReq.

        一次查询的条数，默认值为10。

        :param limit: The limit of this QueryCustomerOnDemandResourcesReq.
        :type limit: int
        """
        self._limit = limit

    @property
    def status(self):
        """Gets the status of this QueryCustomerOnDemandResourcesReq.

        资源状态： 1：正常（已开通）2：宽限期3：冻结中4：变更中5：正在关闭6：已关闭

        :return: The status of this QueryCustomerOnDemandResourcesReq.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this QueryCustomerOnDemandResourcesReq.

        资源状态： 1：正常（已开通）2：宽限期3：冻结中4：变更中5：正在关闭6：已关闭

        :param status: The status of this QueryCustomerOnDemandResourcesReq.
        :type status: int
        """
        self._status = status

    @property
    def indirect_partner_id(self):
        """Gets the indirect_partner_id of this QueryCustomerOnDemandResourcesReq.

        云经销商ID。如果需要查询云经销商子客户的按需资源列表，必须携带该字段，除此之外，此参数不做处理。否则只能查询自己的子客户按需资源。

        :return: The indirect_partner_id of this QueryCustomerOnDemandResourcesReq.
        :rtype: str
        """
        return self._indirect_partner_id

    @indirect_partner_id.setter
    def indirect_partner_id(self, indirect_partner_id):
        """Sets the indirect_partner_id of this QueryCustomerOnDemandResourcesReq.

        云经销商ID。如果需要查询云经销商子客户的按需资源列表，必须携带该字段，除此之外，此参数不做处理。否则只能查询自己的子客户按需资源。

        :param indirect_partner_id: The indirect_partner_id of this QueryCustomerOnDemandResourcesReq.
        :type indirect_partner_id: str
        """
        self._indirect_partner_id = indirect_partner_id

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
        if not isinstance(other, QueryCustomerOnDemandResourcesReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
