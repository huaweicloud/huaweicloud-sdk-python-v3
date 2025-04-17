# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListResourceGroupsServicesResourcesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_id': 'str',
        'service': 'str',
        'dim_name': 'str',
        'limit': 'str',
        'offset': 'int',
        'status': 'str',
        'dim_value': 'str',
        'tag': 'str',
        'extend_relation_id': 'str',
        'product_name': 'str',
        'resource_name': 'str',
        'event_status': 'str'
    }

    attribute_map = {
        'group_id': 'group_id',
        'service': 'service',
        'dim_name': 'dim_name',
        'limit': 'limit',
        'offset': 'offset',
        'status': 'status',
        'dim_value': 'dim_value',
        'tag': 'tag',
        'extend_relation_id': 'extend_relation_id',
        'product_name': 'product_name',
        'resource_name': 'resource_name',
        'event_status': 'event_status'
    }

    def __init__(self, group_id=None, service=None, dim_name=None, limit=None, offset=None, status=None, dim_value=None, tag=None, extend_relation_id=None, product_name=None, resource_name=None, event_status=None):
        r"""ListResourceGroupsServicesResourcesRequest

        The model defined in huaweicloud sdk

        :param group_id: 资源分组ID，以rg开头，后跟22位由字母或数字组成的字符串
        :type group_id: str
        :param service: 服务类别，如SYS.ECS
        :type service: str
        :param dim_name: 资源维度信息，多个维度按字母序使用逗号分割
        :type dim_name: str
        :param limit: 分页查询时每页的条目数，取值[1,100]，默认值为100
        :type limit: str
        :param offset: 分页查询时查询的起始位置，表示从第几条数据开始，默认为0
        :type offset: int
        :param status: 按状态信息进行过滤，取值只能为health（已设置告警规则且无告警触发的资源）、unhealthy（已设置告警规则且有告警触发的资源）、no_alarm_rule（未设置告警规则的资源）
        :type status: str
        :param dim_value: 资源维度值，不支持模糊匹配，但是多维度资源可以只指定一个维度值
        :type dim_value: str
        :param tag: 资源的标签信息，格式：\&quot;[key]\&quot;:\&quot;[value]\&quot;，样例参考：\&quot;ssss\&quot;:\&quot;1111\&quot;
        :type tag: str
        :param extend_relation_id: 企业项目ID
        :type extend_relation_id: str
        :param product_name: 资源分组的云产品，一般由\&quot;服务命名空间,服务首层维度名称\&quot;组成，如\&quot;SYS.ECS,instance_id\&quot;
        :type product_name: str
        :param resource_name: 资源名称
        :type resource_name: str
        :param event_status: 按事件告警状态信息进行过滤，取值只能为health（已设置事件告警规则且无事件告警触发的资源）、unhealthy（已设置事件告警规则且有事件告警触发的资源）、no_alarm_rule（未设置事件告警规则的资源）
        :type event_status: str
        """
        
        

        self._group_id = None
        self._service = None
        self._dim_name = None
        self._limit = None
        self._offset = None
        self._status = None
        self._dim_value = None
        self._tag = None
        self._extend_relation_id = None
        self._product_name = None
        self._resource_name = None
        self._event_status = None
        self.discriminator = None

        self.group_id = group_id
        self.service = service
        if dim_name is not None:
            self.dim_name = dim_name
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if status is not None:
            self.status = status
        if dim_value is not None:
            self.dim_value = dim_value
        if tag is not None:
            self.tag = tag
        if extend_relation_id is not None:
            self.extend_relation_id = extend_relation_id
        if product_name is not None:
            self.product_name = product_name
        if resource_name is not None:
            self.resource_name = resource_name
        if event_status is not None:
            self.event_status = event_status

    @property
    def group_id(self):
        r"""Gets the group_id of this ListResourceGroupsServicesResourcesRequest.

        资源分组ID，以rg开头，后跟22位由字母或数字组成的字符串

        :return: The group_id of this ListResourceGroupsServicesResourcesRequest.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this ListResourceGroupsServicesResourcesRequest.

        资源分组ID，以rg开头，后跟22位由字母或数字组成的字符串

        :param group_id: The group_id of this ListResourceGroupsServicesResourcesRequest.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def service(self):
        r"""Gets the service of this ListResourceGroupsServicesResourcesRequest.

        服务类别，如SYS.ECS

        :return: The service of this ListResourceGroupsServicesResourcesRequest.
        :rtype: str
        """
        return self._service

    @service.setter
    def service(self, service):
        r"""Sets the service of this ListResourceGroupsServicesResourcesRequest.

        服务类别，如SYS.ECS

        :param service: The service of this ListResourceGroupsServicesResourcesRequest.
        :type service: str
        """
        self._service = service

    @property
    def dim_name(self):
        r"""Gets the dim_name of this ListResourceGroupsServicesResourcesRequest.

        资源维度信息，多个维度按字母序使用逗号分割

        :return: The dim_name of this ListResourceGroupsServicesResourcesRequest.
        :rtype: str
        """
        return self._dim_name

    @dim_name.setter
    def dim_name(self, dim_name):
        r"""Sets the dim_name of this ListResourceGroupsServicesResourcesRequest.

        资源维度信息，多个维度按字母序使用逗号分割

        :param dim_name: The dim_name of this ListResourceGroupsServicesResourcesRequest.
        :type dim_name: str
        """
        self._dim_name = dim_name

    @property
    def limit(self):
        r"""Gets the limit of this ListResourceGroupsServicesResourcesRequest.

        分页查询时每页的条目数，取值[1,100]，默认值为100

        :return: The limit of this ListResourceGroupsServicesResourcesRequest.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListResourceGroupsServicesResourcesRequest.

        分页查询时每页的条目数，取值[1,100]，默认值为100

        :param limit: The limit of this ListResourceGroupsServicesResourcesRequest.
        :type limit: str
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListResourceGroupsServicesResourcesRequest.

        分页查询时查询的起始位置，表示从第几条数据开始，默认为0

        :return: The offset of this ListResourceGroupsServicesResourcesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListResourceGroupsServicesResourcesRequest.

        分页查询时查询的起始位置，表示从第几条数据开始，默认为0

        :param offset: The offset of this ListResourceGroupsServicesResourcesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def status(self):
        r"""Gets the status of this ListResourceGroupsServicesResourcesRequest.

        按状态信息进行过滤，取值只能为health（已设置告警规则且无告警触发的资源）、unhealthy（已设置告警规则且有告警触发的资源）、no_alarm_rule（未设置告警规则的资源）

        :return: The status of this ListResourceGroupsServicesResourcesRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListResourceGroupsServicesResourcesRequest.

        按状态信息进行过滤，取值只能为health（已设置告警规则且无告警触发的资源）、unhealthy（已设置告警规则且有告警触发的资源）、no_alarm_rule（未设置告警规则的资源）

        :param status: The status of this ListResourceGroupsServicesResourcesRequest.
        :type status: str
        """
        self._status = status

    @property
    def dim_value(self):
        r"""Gets the dim_value of this ListResourceGroupsServicesResourcesRequest.

        资源维度值，不支持模糊匹配，但是多维度资源可以只指定一个维度值

        :return: The dim_value of this ListResourceGroupsServicesResourcesRequest.
        :rtype: str
        """
        return self._dim_value

    @dim_value.setter
    def dim_value(self, dim_value):
        r"""Sets the dim_value of this ListResourceGroupsServicesResourcesRequest.

        资源维度值，不支持模糊匹配，但是多维度资源可以只指定一个维度值

        :param dim_value: The dim_value of this ListResourceGroupsServicesResourcesRequest.
        :type dim_value: str
        """
        self._dim_value = dim_value

    @property
    def tag(self):
        r"""Gets the tag of this ListResourceGroupsServicesResourcesRequest.

        资源的标签信息，格式：\"[key]\":\"[value]\"，样例参考：\"ssss\":\"1111\"

        :return: The tag of this ListResourceGroupsServicesResourcesRequest.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        r"""Sets the tag of this ListResourceGroupsServicesResourcesRequest.

        资源的标签信息，格式：\"[key]\":\"[value]\"，样例参考：\"ssss\":\"1111\"

        :param tag: The tag of this ListResourceGroupsServicesResourcesRequest.
        :type tag: str
        """
        self._tag = tag

    @property
    def extend_relation_id(self):
        r"""Gets the extend_relation_id of this ListResourceGroupsServicesResourcesRequest.

        企业项目ID

        :return: The extend_relation_id of this ListResourceGroupsServicesResourcesRequest.
        :rtype: str
        """
        return self._extend_relation_id

    @extend_relation_id.setter
    def extend_relation_id(self, extend_relation_id):
        r"""Sets the extend_relation_id of this ListResourceGroupsServicesResourcesRequest.

        企业项目ID

        :param extend_relation_id: The extend_relation_id of this ListResourceGroupsServicesResourcesRequest.
        :type extend_relation_id: str
        """
        self._extend_relation_id = extend_relation_id

    @property
    def product_name(self):
        r"""Gets the product_name of this ListResourceGroupsServicesResourcesRequest.

        资源分组的云产品，一般由\"服务命名空间,服务首层维度名称\"组成，如\"SYS.ECS,instance_id\"

        :return: The product_name of this ListResourceGroupsServicesResourcesRequest.
        :rtype: str
        """
        return self._product_name

    @product_name.setter
    def product_name(self, product_name):
        r"""Sets the product_name of this ListResourceGroupsServicesResourcesRequest.

        资源分组的云产品，一般由\"服务命名空间,服务首层维度名称\"组成，如\"SYS.ECS,instance_id\"

        :param product_name: The product_name of this ListResourceGroupsServicesResourcesRequest.
        :type product_name: str
        """
        self._product_name = product_name

    @property
    def resource_name(self):
        r"""Gets the resource_name of this ListResourceGroupsServicesResourcesRequest.

        资源名称

        :return: The resource_name of this ListResourceGroupsServicesResourcesRequest.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        r"""Sets the resource_name of this ListResourceGroupsServicesResourcesRequest.

        资源名称

        :param resource_name: The resource_name of this ListResourceGroupsServicesResourcesRequest.
        :type resource_name: str
        """
        self._resource_name = resource_name

    @property
    def event_status(self):
        r"""Gets the event_status of this ListResourceGroupsServicesResourcesRequest.

        按事件告警状态信息进行过滤，取值只能为health（已设置事件告警规则且无事件告警触发的资源）、unhealthy（已设置事件告警规则且有事件告警触发的资源）、no_alarm_rule（未设置事件告警规则的资源）

        :return: The event_status of this ListResourceGroupsServicesResourcesRequest.
        :rtype: str
        """
        return self._event_status

    @event_status.setter
    def event_status(self, event_status):
        r"""Sets the event_status of this ListResourceGroupsServicesResourcesRequest.

        按事件告警状态信息进行过滤，取值只能为health（已设置事件告警规则且无事件告警触发的资源）、unhealthy（已设置事件告警规则且有事件告警触发的资源）、no_alarm_rule（未设置事件告警规则的资源）

        :param event_status: The event_status of this ListResourceGroupsServicesResourcesRequest.
        :type event_status: str
        """
        self._event_status = event_status

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
        if not isinstance(other, ListResourceGroupsServicesResourcesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
