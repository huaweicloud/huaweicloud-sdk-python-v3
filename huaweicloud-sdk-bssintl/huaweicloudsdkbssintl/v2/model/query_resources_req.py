# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryResourcesReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_ids': 'list[str]',
        'order_id': 'str',
        'only_main_resource': 'int',
        'status_list': 'list[int]',
        'offset': 'int',
        'limit': 'int',
        'expire_time_begin': 'str',
        'expire_time_end': 'str'
    }

    attribute_map = {
        'resource_ids': 'resource_ids',
        'order_id': 'order_id',
        'only_main_resource': 'only_main_resource',
        'status_list': 'status_list',
        'offset': 'offset',
        'limit': 'limit',
        'expire_time_begin': 'expire_time_begin',
        'expire_time_end': 'expire_time_end'
    }

    def __init__(self, resource_ids=None, order_id=None, only_main_resource=None, status_list=None, offset=None, limit=None, expire_time_begin=None, expire_time_end=None):
        """QueryResourcesReq

        The model defined in huaweicloud sdk

        :param resource_ids: 资源ID列表。 查询指定资源ID的资源（当only_main_resource&#x3D;0时，查询指定资源及其附属资源）。最大支持50个ID同时作为条件查询，多个ID以英文逗号分隔。  说明： 资源ID是指开通资源以后，云服务针对该资源分配的标志，譬如云主机ECS的资源ID是server_id。
        :type resource_ids: list[str]
        :param order_id: 订单号。查询指定订单下的资源。  说明： 使用特殊字符进行查询的时候，请注意进行URL编码转换，如“%”的转码应为“%25”。
        :type order_id: str
        :param only_main_resource: 是否只查询主资源，该参数对于请求参数是子资源ID的时候无效，如果resource_ids是子资源ID，只能查询自己。 0：查询主资源及附属资源。1：只查询主资源。 默认值为0。  说明： 主资源是指有关联的几个资源中，处于主导位置的资源。 对于ECS而言，虚拟机VM是主资源，磁盘EVS是辅资源。对于VPC而言，共享带宽的情况下，带宽为主资源，对应的从资源为弹性IP（可能包含多个IP）；独享带宽的情况下，弹性IP为主资源，对应的从资源为带宽。
        :type only_main_resource: int
        :param status_list: 资源状态。 查询指定状态的资源。多个状态以英文逗号分隔。 2：使用中4：已冻结5：已过期
        :type status_list: list[int]
        :param offset: 偏移量，从0开始。默认值为0。  说明： offset用于分页处理，如不涉及分页，请使用默认值0。offset表示相对于满足条件的第一个数据的偏移量。如offset &#x3D; 1，则返回满足条件的第二个数据至最后一个数据。 例如，满足查询条件的结果共10条数据，limit取值为10，offset取值为1，则返回的数据为2~10，第一条数据不返回。
        :type offset: int
        :param limit: 每次查询的条数。默认值为10。
        :type limit: int
        :param expire_time_begin: 查询指定时间段内失效的资源列表，时间段的起始时间，UTC时间。
        :type expire_time_begin: str
        :param expire_time_end: 查询指定时间段内失效的资源列表，时间段的结束时间，UTC时间。
        :type expire_time_end: str
        """
        
        

        self._resource_ids = None
        self._order_id = None
        self._only_main_resource = None
        self._status_list = None
        self._offset = None
        self._limit = None
        self._expire_time_begin = None
        self._expire_time_end = None
        self.discriminator = None

        if resource_ids is not None:
            self.resource_ids = resource_ids
        if order_id is not None:
            self.order_id = order_id
        if only_main_resource is not None:
            self.only_main_resource = only_main_resource
        if status_list is not None:
            self.status_list = status_list
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if expire_time_begin is not None:
            self.expire_time_begin = expire_time_begin
        if expire_time_end is not None:
            self.expire_time_end = expire_time_end

    @property
    def resource_ids(self):
        """Gets the resource_ids of this QueryResourcesReq.

        资源ID列表。 查询指定资源ID的资源（当only_main_resource=0时，查询指定资源及其附属资源）。最大支持50个ID同时作为条件查询，多个ID以英文逗号分隔。  说明： 资源ID是指开通资源以后，云服务针对该资源分配的标志，譬如云主机ECS的资源ID是server_id。

        :return: The resource_ids of this QueryResourcesReq.
        :rtype: list[str]
        """
        return self._resource_ids

    @resource_ids.setter
    def resource_ids(self, resource_ids):
        """Sets the resource_ids of this QueryResourcesReq.

        资源ID列表。 查询指定资源ID的资源（当only_main_resource=0时，查询指定资源及其附属资源）。最大支持50个ID同时作为条件查询，多个ID以英文逗号分隔。  说明： 资源ID是指开通资源以后，云服务针对该资源分配的标志，譬如云主机ECS的资源ID是server_id。

        :param resource_ids: The resource_ids of this QueryResourcesReq.
        :type resource_ids: list[str]
        """
        self._resource_ids = resource_ids

    @property
    def order_id(self):
        """Gets the order_id of this QueryResourcesReq.

        订单号。查询指定订单下的资源。  说明： 使用特殊字符进行查询的时候，请注意进行URL编码转换，如“%”的转码应为“%25”。

        :return: The order_id of this QueryResourcesReq.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this QueryResourcesReq.

        订单号。查询指定订单下的资源。  说明： 使用特殊字符进行查询的时候，请注意进行URL编码转换，如“%”的转码应为“%25”。

        :param order_id: The order_id of this QueryResourcesReq.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def only_main_resource(self):
        """Gets the only_main_resource of this QueryResourcesReq.

        是否只查询主资源，该参数对于请求参数是子资源ID的时候无效，如果resource_ids是子资源ID，只能查询自己。 0：查询主资源及附属资源。1：只查询主资源。 默认值为0。  说明： 主资源是指有关联的几个资源中，处于主导位置的资源。 对于ECS而言，虚拟机VM是主资源，磁盘EVS是辅资源。对于VPC而言，共享带宽的情况下，带宽为主资源，对应的从资源为弹性IP（可能包含多个IP）；独享带宽的情况下，弹性IP为主资源，对应的从资源为带宽。

        :return: The only_main_resource of this QueryResourcesReq.
        :rtype: int
        """
        return self._only_main_resource

    @only_main_resource.setter
    def only_main_resource(self, only_main_resource):
        """Sets the only_main_resource of this QueryResourcesReq.

        是否只查询主资源，该参数对于请求参数是子资源ID的时候无效，如果resource_ids是子资源ID，只能查询自己。 0：查询主资源及附属资源。1：只查询主资源。 默认值为0。  说明： 主资源是指有关联的几个资源中，处于主导位置的资源。 对于ECS而言，虚拟机VM是主资源，磁盘EVS是辅资源。对于VPC而言，共享带宽的情况下，带宽为主资源，对应的从资源为弹性IP（可能包含多个IP）；独享带宽的情况下，弹性IP为主资源，对应的从资源为带宽。

        :param only_main_resource: The only_main_resource of this QueryResourcesReq.
        :type only_main_resource: int
        """
        self._only_main_resource = only_main_resource

    @property
    def status_list(self):
        """Gets the status_list of this QueryResourcesReq.

        资源状态。 查询指定状态的资源。多个状态以英文逗号分隔。 2：使用中4：已冻结5：已过期

        :return: The status_list of this QueryResourcesReq.
        :rtype: list[int]
        """
        return self._status_list

    @status_list.setter
    def status_list(self, status_list):
        """Sets the status_list of this QueryResourcesReq.

        资源状态。 查询指定状态的资源。多个状态以英文逗号分隔。 2：使用中4：已冻结5：已过期

        :param status_list: The status_list of this QueryResourcesReq.
        :type status_list: list[int]
        """
        self._status_list = status_list

    @property
    def offset(self):
        """Gets the offset of this QueryResourcesReq.

        偏移量，从0开始。默认值为0。  说明： offset用于分页处理，如不涉及分页，请使用默认值0。offset表示相对于满足条件的第一个数据的偏移量。如offset = 1，则返回满足条件的第二个数据至最后一个数据。 例如，满足查询条件的结果共10条数据，limit取值为10，offset取值为1，则返回的数据为2~10，第一条数据不返回。

        :return: The offset of this QueryResourcesReq.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this QueryResourcesReq.

        偏移量，从0开始。默认值为0。  说明： offset用于分页处理，如不涉及分页，请使用默认值0。offset表示相对于满足条件的第一个数据的偏移量。如offset = 1，则返回满足条件的第二个数据至最后一个数据。 例如，满足查询条件的结果共10条数据，limit取值为10，offset取值为1，则返回的数据为2~10，第一条数据不返回。

        :param offset: The offset of this QueryResourcesReq.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this QueryResourcesReq.

        每次查询的条数。默认值为10。

        :return: The limit of this QueryResourcesReq.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this QueryResourcesReq.

        每次查询的条数。默认值为10。

        :param limit: The limit of this QueryResourcesReq.
        :type limit: int
        """
        self._limit = limit

    @property
    def expire_time_begin(self):
        """Gets the expire_time_begin of this QueryResourcesReq.

        查询指定时间段内失效的资源列表，时间段的起始时间，UTC时间。

        :return: The expire_time_begin of this QueryResourcesReq.
        :rtype: str
        """
        return self._expire_time_begin

    @expire_time_begin.setter
    def expire_time_begin(self, expire_time_begin):
        """Sets the expire_time_begin of this QueryResourcesReq.

        查询指定时间段内失效的资源列表，时间段的起始时间，UTC时间。

        :param expire_time_begin: The expire_time_begin of this QueryResourcesReq.
        :type expire_time_begin: str
        """
        self._expire_time_begin = expire_time_begin

    @property
    def expire_time_end(self):
        """Gets the expire_time_end of this QueryResourcesReq.

        查询指定时间段内失效的资源列表，时间段的结束时间，UTC时间。

        :return: The expire_time_end of this QueryResourcesReq.
        :rtype: str
        """
        return self._expire_time_end

    @expire_time_end.setter
    def expire_time_end(self, expire_time_end):
        """Sets the expire_time_end of this QueryResourcesReq.

        查询指定时间段内失效的资源列表，时间段的结束时间，UTC时间。

        :param expire_time_end: The expire_time_end of this QueryResourcesReq.
        :type expire_time_end: str
        """
        self._expire_time_end = expire_time_end

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
        if not isinstance(other, QueryResourcesReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
