# coding: utf-8

import pprint
import re

import six





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
        'limit': 'int'
    }

    attribute_map = {
        'resource_ids': 'resource_ids',
        'order_id': 'order_id',
        'only_main_resource': 'only_main_resource',
        'status_list': 'status_list',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, resource_ids=None, order_id=None, only_main_resource=0, status_list=None, offset=None, limit=None):
        """QueryResourcesReq - a model defined in huaweicloud sdk"""
        
        

        self._resource_ids = None
        self._order_id = None
        self._only_main_resource = None
        self._status_list = None
        self._offset = None
        self._limit = None
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

    @property
    def resource_ids(self):
        """Gets the resource_ids of this QueryResourcesReq.

        |参数名称：资源ID列表。查询指定资源ID的资源（当only_main_resource=0时，查询指定资源及其附属资源）。最大支持50个ID同时作为条件查询。| |参数约束以及描述：资源ID列表。查询指定资源ID的资源（当only_main_resource=0时，查询指定资源及其附属资源）。最大支持50个ID同时作为条件查询。|

        :return: The resource_ids of this QueryResourcesReq.
        :rtype: list[str]
        """
        return self._resource_ids

    @resource_ids.setter
    def resource_ids(self, resource_ids):
        """Sets the resource_ids of this QueryResourcesReq.

        |参数名称：资源ID列表。查询指定资源ID的资源（当only_main_resource=0时，查询指定资源及其附属资源）。最大支持50个ID同时作为条件查询。| |参数约束以及描述：资源ID列表。查询指定资源ID的资源（当only_main_resource=0时，查询指定资源及其附属资源）。最大支持50个ID同时作为条件查询。|

        :param resource_ids: The resource_ids of this QueryResourcesReq.
        :type: list[str]
        """
        self._resource_ids = resource_ids

    @property
    def order_id(self):
        """Gets the order_id of this QueryResourcesReq.

        |参数名称：订单号。查询指定订单下的资源。| |参数约束及描述：订单号。查询指定订单下的资源。|

        :return: The order_id of this QueryResourcesReq.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this QueryResourcesReq.

        |参数名称：订单号。查询指定订单下的资源。| |参数约束及描述：订单号。查询指定订单下的资源。|

        :param order_id: The order_id of this QueryResourcesReq.
        :type: str
        """
        self._order_id = order_id

    @property
    def only_main_resource(self):
        """Gets the only_main_resource of this QueryResourcesReq.

        |参数名称：是否只查询主资源。0：查询主资源及附属资源。1：只查询主资源。默认值为0。| |参数的约束及描述：是否只查询主资源。0：查询主资源及附属资源。1：只查询主资源。默认值为0。|

        :return: The only_main_resource of this QueryResourcesReq.
        :rtype: int
        """
        return self._only_main_resource

    @only_main_resource.setter
    def only_main_resource(self, only_main_resource):
        """Sets the only_main_resource of this QueryResourcesReq.

        |参数名称：是否只查询主资源。0：查询主资源及附属资源。1：只查询主资源。默认值为0。| |参数的约束及描述：是否只查询主资源。0：查询主资源及附属资源。1：只查询主资源。默认值为0。|

        :param only_main_resource: The only_main_resource of this QueryResourcesReq.
        :type: int
        """
        self._only_main_resource = only_main_resource

    @property
    def status_list(self):
        """Gets the status_list of this QueryResourcesReq.

        |参数名称：资源状态。查询指定状态的资源。1：初始化2：已生效3：已过期4：已冻结5：宽限期6：冻结中7：冻结恢复中（预留，未启用）8：正在关闭| |参数约束以及描述：资源状态。查询指定状态的资源。1：初始化2：已生效3：已过期4：已冻结5：宽限期6：冻结中7：冻结恢复中（预留，未启用）8：正在关闭|

        :return: The status_list of this QueryResourcesReq.
        :rtype: list[int]
        """
        return self._status_list

    @status_list.setter
    def status_list(self, status_list):
        """Sets the status_list of this QueryResourcesReq.

        |参数名称：资源状态。查询指定状态的资源。1：初始化2：已生效3：已过期4：已冻结5：宽限期6：冻结中7：冻结恢复中（预留，未启用）8：正在关闭| |参数约束以及描述：资源状态。查询指定状态的资源。1：初始化2：已生效3：已过期4：已冻结5：宽限期6：冻结中7：冻结恢复中（预留，未启用）8：正在关闭|

        :param status_list: The status_list of this QueryResourcesReq.
        :type: list[int]
        """
        self._status_list = status_list

    @property
    def offset(self):
        """Gets the offset of this QueryResourcesReq.

        |参数名称：偏移量，从0开始默认值是0。| |参数的约束及描述：偏移量，从0开始默认值是0。|

        :return: The offset of this QueryResourcesReq.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this QueryResourcesReq.

        |参数名称：偏移量，从0开始默认值是0。| |参数的约束及描述：偏移量，从0开始默认值是0。|

        :param offset: The offset of this QueryResourcesReq.
        :type: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this QueryResourcesReq.

        |参数名称：每次查询的条数。默认值是10。最大值是500。| |参数的约束及描述：每次查询的条数。默认值是10。最大值是500。|

        :return: The limit of this QueryResourcesReq.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this QueryResourcesReq.

        |参数名称：每次查询的条数。默认值是10。最大值是500。| |参数的约束及描述：每次查询的条数。默认值是10。最大值是500。|

        :param limit: The limit of this QueryResourcesReq.
        :type: int
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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, QueryResourcesReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
