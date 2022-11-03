# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EndpointDetail:

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
        'resource_id': 'str',
        'endpoint_group_id': 'str',
        'resource_type': 'EndpointType',
        'status': 'ConfigStatus',
        'weight': 'int',
        'health_state': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'domain_id': 'str',
        'ip_address': 'str',
        'frozen_info': 'FrozenInfo'
    }

    attribute_map = {
        'id': 'id',
        'resource_id': 'resource_id',
        'endpoint_group_id': 'endpoint_group_id',
        'resource_type': 'resource_type',
        'status': 'status',
        'weight': 'weight',
        'health_state': 'health_state',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'domain_id': 'domain_id',
        'ip_address': 'ip_address',
        'frozen_info': 'frozen_info'
    }

    def __init__(self, id=None, resource_id=None, endpoint_group_id=None, resource_type=None, status=None, weight=None, health_state=None, created_at=None, updated_at=None, domain_id=None, ip_address=None, frozen_info=None):
        """EndpointDetail

        The model defined in huaweicloud sdk

        :param id: 终端节点ID。
        :type id: str
        :param resource_id: 对应后端资源ID。
        :type resource_id: str
        :param endpoint_group_id: 终端节点组ID。
        :type endpoint_group_id: str
        :param resource_type: 
        :type resource_type: :class:`huaweicloudsdkga.v1.EndpointType`
        :param status: 
        :type status: :class:`huaweicloudsdkga.v1.ConfigStatus`
        :param weight: 终端节点权重。
        :type weight: int
        :param health_state: 终端的健康状态，取值： - INITIAL：初始 - HEALTHY：正常 - UNHEALTHY：异常 - NO_MONITOR：未监控
        :type health_state: str
        :param created_at: 创建时间。
        :type created_at: datetime
        :param updated_at: 更新时间。
        :type updated_at: datetime
        :param domain_id: 租户ID。
        :type domain_id: str
        :param ip_address: IP地址。
        :type ip_address: str
        :param frozen_info: 
        :type frozen_info: :class:`huaweicloudsdkga.v1.FrozenInfo`
        """
        
        

        self._id = None
        self._resource_id = None
        self._endpoint_group_id = None
        self._resource_type = None
        self._status = None
        self._weight = None
        self._health_state = None
        self._created_at = None
        self._updated_at = None
        self._domain_id = None
        self._ip_address = None
        self._frozen_info = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if resource_id is not None:
            self.resource_id = resource_id
        if endpoint_group_id is not None:
            self.endpoint_group_id = endpoint_group_id
        if resource_type is not None:
            self.resource_type = resource_type
        if status is not None:
            self.status = status
        if weight is not None:
            self.weight = weight
        if health_state is not None:
            self.health_state = health_state
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if domain_id is not None:
            self.domain_id = domain_id
        if ip_address is not None:
            self.ip_address = ip_address
        if frozen_info is not None:
            self.frozen_info = frozen_info

    @property
    def id(self):
        """Gets the id of this EndpointDetail.

        终端节点ID。

        :return: The id of this EndpointDetail.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EndpointDetail.

        终端节点ID。

        :param id: The id of this EndpointDetail.
        :type id: str
        """
        self._id = id

    @property
    def resource_id(self):
        """Gets the resource_id of this EndpointDetail.

        对应后端资源ID。

        :return: The resource_id of this EndpointDetail.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this EndpointDetail.

        对应后端资源ID。

        :param resource_id: The resource_id of this EndpointDetail.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def endpoint_group_id(self):
        """Gets the endpoint_group_id of this EndpointDetail.

        终端节点组ID。

        :return: The endpoint_group_id of this EndpointDetail.
        :rtype: str
        """
        return self._endpoint_group_id

    @endpoint_group_id.setter
    def endpoint_group_id(self, endpoint_group_id):
        """Sets the endpoint_group_id of this EndpointDetail.

        终端节点组ID。

        :param endpoint_group_id: The endpoint_group_id of this EndpointDetail.
        :type endpoint_group_id: str
        """
        self._endpoint_group_id = endpoint_group_id

    @property
    def resource_type(self):
        """Gets the resource_type of this EndpointDetail.


        :return: The resource_type of this EndpointDetail.
        :rtype: :class:`huaweicloudsdkga.v1.EndpointType`
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this EndpointDetail.


        :param resource_type: The resource_type of this EndpointDetail.
        :type resource_type: :class:`huaweicloudsdkga.v1.EndpointType`
        """
        self._resource_type = resource_type

    @property
    def status(self):
        """Gets the status of this EndpointDetail.


        :return: The status of this EndpointDetail.
        :rtype: :class:`huaweicloudsdkga.v1.ConfigStatus`
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this EndpointDetail.


        :param status: The status of this EndpointDetail.
        :type status: :class:`huaweicloudsdkga.v1.ConfigStatus`
        """
        self._status = status

    @property
    def weight(self):
        """Gets the weight of this EndpointDetail.

        终端节点权重。

        :return: The weight of this EndpointDetail.
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this EndpointDetail.

        终端节点权重。

        :param weight: The weight of this EndpointDetail.
        :type weight: int
        """
        self._weight = weight

    @property
    def health_state(self):
        """Gets the health_state of this EndpointDetail.

        终端的健康状态，取值： - INITIAL：初始 - HEALTHY：正常 - UNHEALTHY：异常 - NO_MONITOR：未监控

        :return: The health_state of this EndpointDetail.
        :rtype: str
        """
        return self._health_state

    @health_state.setter
    def health_state(self, health_state):
        """Sets the health_state of this EndpointDetail.

        终端的健康状态，取值： - INITIAL：初始 - HEALTHY：正常 - UNHEALTHY：异常 - NO_MONITOR：未监控

        :param health_state: The health_state of this EndpointDetail.
        :type health_state: str
        """
        self._health_state = health_state

    @property
    def created_at(self):
        """Gets the created_at of this EndpointDetail.

        创建时间。

        :return: The created_at of this EndpointDetail.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this EndpointDetail.

        创建时间。

        :param created_at: The created_at of this EndpointDetail.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this EndpointDetail.

        更新时间。

        :return: The updated_at of this EndpointDetail.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this EndpointDetail.

        更新时间。

        :param updated_at: The updated_at of this EndpointDetail.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

    @property
    def domain_id(self):
        """Gets the domain_id of this EndpointDetail.

        租户ID。

        :return: The domain_id of this EndpointDetail.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this EndpointDetail.

        租户ID。

        :param domain_id: The domain_id of this EndpointDetail.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def ip_address(self):
        """Gets the ip_address of this EndpointDetail.

        IP地址。

        :return: The ip_address of this EndpointDetail.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this EndpointDetail.

        IP地址。

        :param ip_address: The ip_address of this EndpointDetail.
        :type ip_address: str
        """
        self._ip_address = ip_address

    @property
    def frozen_info(self):
        """Gets the frozen_info of this EndpointDetail.


        :return: The frozen_info of this EndpointDetail.
        :rtype: :class:`huaweicloudsdkga.v1.FrozenInfo`
        """
        return self._frozen_info

    @frozen_info.setter
    def frozen_info(self, frozen_info):
        """Sets the frozen_info of this EndpointDetail.


        :param frozen_info: The frozen_info of this EndpointDetail.
        :type frozen_info: :class:`huaweicloudsdkga.v1.FrozenInfo`
        """
        self._frozen_info = frozen_info

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
        if not isinstance(other, EndpointDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
