# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTenantResourcesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'offset': 'int',
        'resource': 'str',
        'business': 'str',
        'resource_source': 'str',
        'resource_name': 'str',
        'resource_id': 'str',
        'order_id': 'str',
        'charging_mode': 'str',
        'resource_expire_start_time': 'str',
        'resource_expire_end_time': 'str',
        'sub_resource': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'offset': 'offset',
        'resource': 'resource',
        'business': 'business',
        'resource_source': 'resource_source',
        'resource_name': 'resource_name',
        'resource_id': 'resource_id',
        'order_id': 'order_id',
        'charging_mode': 'charging_mode',
        'resource_expire_start_time': 'resource_expire_start_time',
        'resource_expire_end_time': 'resource_expire_end_time',
        'sub_resource': 'sub_resource'
    }

    def __init__(self, limit=None, offset=None, resource=None, business=None, resource_source=None, resource_name=None, resource_id=None, order_id=None, charging_mode=None, resource_expire_start_time=None, resource_expire_end_time=None, sub_resource=None):
        """ListTenantResourcesRequest

        The model defined in huaweicloud sdk

        :param limit: 每页显示的条目数量。
        :type limit: int
        :param offset: 偏移量，表示从此偏移量开始查询。
        :type offset: int
        :param resource: 资源类型。
        :type resource: str
        :param business: 业务类型。
        :type business: str
        :param resource_source: 资源来源。
        :type resource_source: str
        :param resource_name: 资源名称。
        :type resource_name: str
        :param resource_id: 资源id。
        :type resource_id: str
        :param order_id: 订单id。
        :type order_id: str
        :param charging_mode: 计费模式。
        :type charging_mode: str
        :param resource_expire_start_time: 资源过期时间段 开始时间。格式遵循：RFC 3339 如\&quot;2021-01-10T08:43:17Z\&quot;
        :type resource_expire_start_time: str
        :param resource_expire_end_time: 资源过期时间段 结束时间。格式遵循：RFC 3339 如\&quot;2021-01-10T08:43:17Z\&quot;
        :type resource_expire_end_time: str
        :param sub_resource: 子资源类型。
        :type sub_resource: str
        """
        
        

        self._limit = None
        self._offset = None
        self._resource = None
        self._business = None
        self._resource_source = None
        self._resource_name = None
        self._resource_id = None
        self._order_id = None
        self._charging_mode = None
        self._resource_expire_start_time = None
        self._resource_expire_end_time = None
        self._sub_resource = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if resource is not None:
            self.resource = resource
        if business is not None:
            self.business = business
        self.resource_source = resource_source
        if resource_name is not None:
            self.resource_name = resource_name
        if resource_id is not None:
            self.resource_id = resource_id
        if order_id is not None:
            self.order_id = order_id
        if charging_mode is not None:
            self.charging_mode = charging_mode
        if resource_expire_start_time is not None:
            self.resource_expire_start_time = resource_expire_start_time
        if resource_expire_end_time is not None:
            self.resource_expire_end_time = resource_expire_end_time
        if sub_resource is not None:
            self.sub_resource = sub_resource

    @property
    def limit(self):
        """Gets the limit of this ListTenantResourcesRequest.

        每页显示的条目数量。

        :return: The limit of this ListTenantResourcesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListTenantResourcesRequest.

        每页显示的条目数量。

        :param limit: The limit of this ListTenantResourcesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListTenantResourcesRequest.

        偏移量，表示从此偏移量开始查询。

        :return: The offset of this ListTenantResourcesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListTenantResourcesRequest.

        偏移量，表示从此偏移量开始查询。

        :param offset: The offset of this ListTenantResourcesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def resource(self):
        """Gets the resource of this ListTenantResourcesRequest.

        资源类型。

        :return: The resource of this ListTenantResourcesRequest.
        :rtype: str
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """Sets the resource of this ListTenantResourcesRequest.

        资源类型。

        :param resource: The resource of this ListTenantResourcesRequest.
        :type resource: str
        """
        self._resource = resource

    @property
    def business(self):
        """Gets the business of this ListTenantResourcesRequest.

        业务类型。

        :return: The business of this ListTenantResourcesRequest.
        :rtype: str
        """
        return self._business

    @business.setter
    def business(self, business):
        """Sets the business of this ListTenantResourcesRequest.

        业务类型。

        :param business: The business of this ListTenantResourcesRequest.
        :type business: str
        """
        self._business = business

    @property
    def resource_source(self):
        """Gets the resource_source of this ListTenantResourcesRequest.

        资源来源。

        :return: The resource_source of this ListTenantResourcesRequest.
        :rtype: str
        """
        return self._resource_source

    @resource_source.setter
    def resource_source(self, resource_source):
        """Sets the resource_source of this ListTenantResourcesRequest.

        资源来源。

        :param resource_source: The resource_source of this ListTenantResourcesRequest.
        :type resource_source: str
        """
        self._resource_source = resource_source

    @property
    def resource_name(self):
        """Gets the resource_name of this ListTenantResourcesRequest.

        资源名称。

        :return: The resource_name of this ListTenantResourcesRequest.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """Sets the resource_name of this ListTenantResourcesRequest.

        资源名称。

        :param resource_name: The resource_name of this ListTenantResourcesRequest.
        :type resource_name: str
        """
        self._resource_name = resource_name

    @property
    def resource_id(self):
        """Gets the resource_id of this ListTenantResourcesRequest.

        资源id。

        :return: The resource_id of this ListTenantResourcesRequest.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this ListTenantResourcesRequest.

        资源id。

        :param resource_id: The resource_id of this ListTenantResourcesRequest.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def order_id(self):
        """Gets the order_id of this ListTenantResourcesRequest.

        订单id。

        :return: The order_id of this ListTenantResourcesRequest.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this ListTenantResourcesRequest.

        订单id。

        :param order_id: The order_id of this ListTenantResourcesRequest.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def charging_mode(self):
        """Gets the charging_mode of this ListTenantResourcesRequest.

        计费模式。

        :return: The charging_mode of this ListTenantResourcesRequest.
        :rtype: str
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        """Sets the charging_mode of this ListTenantResourcesRequest.

        计费模式。

        :param charging_mode: The charging_mode of this ListTenantResourcesRequest.
        :type charging_mode: str
        """
        self._charging_mode = charging_mode

    @property
    def resource_expire_start_time(self):
        """Gets the resource_expire_start_time of this ListTenantResourcesRequest.

        资源过期时间段 开始时间。格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"

        :return: The resource_expire_start_time of this ListTenantResourcesRequest.
        :rtype: str
        """
        return self._resource_expire_start_time

    @resource_expire_start_time.setter
    def resource_expire_start_time(self, resource_expire_start_time):
        """Sets the resource_expire_start_time of this ListTenantResourcesRequest.

        资源过期时间段 开始时间。格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"

        :param resource_expire_start_time: The resource_expire_start_time of this ListTenantResourcesRequest.
        :type resource_expire_start_time: str
        """
        self._resource_expire_start_time = resource_expire_start_time

    @property
    def resource_expire_end_time(self):
        """Gets the resource_expire_end_time of this ListTenantResourcesRequest.

        资源过期时间段 结束时间。格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"

        :return: The resource_expire_end_time of this ListTenantResourcesRequest.
        :rtype: str
        """
        return self._resource_expire_end_time

    @resource_expire_end_time.setter
    def resource_expire_end_time(self, resource_expire_end_time):
        """Sets the resource_expire_end_time of this ListTenantResourcesRequest.

        资源过期时间段 结束时间。格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"

        :param resource_expire_end_time: The resource_expire_end_time of this ListTenantResourcesRequest.
        :type resource_expire_end_time: str
        """
        self._resource_expire_end_time = resource_expire_end_time

    @property
    def sub_resource(self):
        """Gets the sub_resource of this ListTenantResourcesRequest.

        子资源类型。

        :return: The sub_resource of this ListTenantResourcesRequest.
        :rtype: str
        """
        return self._sub_resource

    @sub_resource.setter
    def sub_resource(self, sub_resource):
        """Sets the sub_resource of this ListTenantResourcesRequest.

        子资源类型。

        :param sub_resource: The sub_resource of this ListTenantResourcesRequest.
        :type sub_resource: str
        """
        self._sub_resource = sub_resource

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
        if not isinstance(other, ListTenantResourcesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
