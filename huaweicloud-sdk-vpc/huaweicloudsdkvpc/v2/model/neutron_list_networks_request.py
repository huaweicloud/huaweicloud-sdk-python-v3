# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NeutronListNetworksRequest:

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
        'marker': 'str',
        'id': 'str',
        'name': 'str',
        'status': 'str',
        'shared': 'bool',
        'routerexternal': 'bool',
        'admin_state_up': 'bool',
        'providernetwork_type': 'str',
        'tenant_id': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'marker': 'marker',
        'id': 'id',
        'name': 'name',
        'status': 'status',
        'shared': 'shared',
        'routerexternal': 'router:external',
        'admin_state_up': 'admin_state_up',
        'providernetwork_type': 'provider:network_type',
        'tenant_id': 'tenant_id'
    }

    def __init__(self, limit=None, marker=None, id=None, name=None, status=None, shared=None, routerexternal=None, admin_state_up=None, providernetwork_type=None, tenant_id=None):
        """NeutronListNetworksRequest

        The model defined in huaweicloud sdk

        :param limit: 每页返回的个数
        :type limit: int
        :param marker: 分页查询起始的资源ID，为空时查询第一页
        :type marker: str
        :param id: 按照网络对应的ID过滤查询
        :type id: str
        :param name: 按照网络的名称过滤查询
        :type name: str
        :param status: 按照网络的状态过滤查询，取值范围：ACTIVE、ERROR、DOWN
        :type status: str
        :param shared: 按照网络是否支持跨租户共享过滤查询，取值范围：true or false
        :type shared: bool
        :param routerexternal: 按照网络是否外部网络过滤查询，取值范围：true or false
        :type routerexternal: bool
        :param admin_state_up: 按照网络的管理状态过滤查询，取值范围：true or false
        :type admin_state_up: bool
        :param providernetwork_type: 按照网络的类型过滤查询
        :type providernetwork_type: str
        :param tenant_id: 按照network所属的项目ID过滤
        :type tenant_id: str
        """
        
        

        self._limit = None
        self._marker = None
        self._id = None
        self._name = None
        self._status = None
        self._shared = None
        self._routerexternal = None
        self._admin_state_up = None
        self._providernetwork_type = None
        self._tenant_id = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if shared is not None:
            self.shared = shared
        if routerexternal is not None:
            self.routerexternal = routerexternal
        if admin_state_up is not None:
            self.admin_state_up = admin_state_up
        if providernetwork_type is not None:
            self.providernetwork_type = providernetwork_type
        if tenant_id is not None:
            self.tenant_id = tenant_id

    @property
    def limit(self):
        """Gets the limit of this NeutronListNetworksRequest.

        每页返回的个数

        :return: The limit of this NeutronListNetworksRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this NeutronListNetworksRequest.

        每页返回的个数

        :param limit: The limit of this NeutronListNetworksRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this NeutronListNetworksRequest.

        分页查询起始的资源ID，为空时查询第一页

        :return: The marker of this NeutronListNetworksRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this NeutronListNetworksRequest.

        分页查询起始的资源ID，为空时查询第一页

        :param marker: The marker of this NeutronListNetworksRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def id(self):
        """Gets the id of this NeutronListNetworksRequest.

        按照网络对应的ID过滤查询

        :return: The id of this NeutronListNetworksRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NeutronListNetworksRequest.

        按照网络对应的ID过滤查询

        :param id: The id of this NeutronListNetworksRequest.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this NeutronListNetworksRequest.

        按照网络的名称过滤查询

        :return: The name of this NeutronListNetworksRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NeutronListNetworksRequest.

        按照网络的名称过滤查询

        :param name: The name of this NeutronListNetworksRequest.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        """Gets the status of this NeutronListNetworksRequest.

        按照网络的状态过滤查询，取值范围：ACTIVE、ERROR、DOWN

        :return: The status of this NeutronListNetworksRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this NeutronListNetworksRequest.

        按照网络的状态过滤查询，取值范围：ACTIVE、ERROR、DOWN

        :param status: The status of this NeutronListNetworksRequest.
        :type status: str
        """
        self._status = status

    @property
    def shared(self):
        """Gets the shared of this NeutronListNetworksRequest.

        按照网络是否支持跨租户共享过滤查询，取值范围：true or false

        :return: The shared of this NeutronListNetworksRequest.
        :rtype: bool
        """
        return self._shared

    @shared.setter
    def shared(self, shared):
        """Sets the shared of this NeutronListNetworksRequest.

        按照网络是否支持跨租户共享过滤查询，取值范围：true or false

        :param shared: The shared of this NeutronListNetworksRequest.
        :type shared: bool
        """
        self._shared = shared

    @property
    def routerexternal(self):
        """Gets the routerexternal of this NeutronListNetworksRequest.

        按照网络是否外部网络过滤查询，取值范围：true or false

        :return: The routerexternal of this NeutronListNetworksRequest.
        :rtype: bool
        """
        return self._routerexternal

    @routerexternal.setter
    def routerexternal(self, routerexternal):
        """Sets the routerexternal of this NeutronListNetworksRequest.

        按照网络是否外部网络过滤查询，取值范围：true or false

        :param routerexternal: The routerexternal of this NeutronListNetworksRequest.
        :type routerexternal: bool
        """
        self._routerexternal = routerexternal

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this NeutronListNetworksRequest.

        按照网络的管理状态过滤查询，取值范围：true or false

        :return: The admin_state_up of this NeutronListNetworksRequest.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this NeutronListNetworksRequest.

        按照网络的管理状态过滤查询，取值范围：true or false

        :param admin_state_up: The admin_state_up of this NeutronListNetworksRequest.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def providernetwork_type(self):
        """Gets the providernetwork_type of this NeutronListNetworksRequest.

        按照网络的类型过滤查询

        :return: The providernetwork_type of this NeutronListNetworksRequest.
        :rtype: str
        """
        return self._providernetwork_type

    @providernetwork_type.setter
    def providernetwork_type(self, providernetwork_type):
        """Sets the providernetwork_type of this NeutronListNetworksRequest.

        按照网络的类型过滤查询

        :param providernetwork_type: The providernetwork_type of this NeutronListNetworksRequest.
        :type providernetwork_type: str
        """
        self._providernetwork_type = providernetwork_type

    @property
    def tenant_id(self):
        """Gets the tenant_id of this NeutronListNetworksRequest.

        按照network所属的项目ID过滤

        :return: The tenant_id of this NeutronListNetworksRequest.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this NeutronListNetworksRequest.

        按照network所属的项目ID过滤

        :param tenant_id: The tenant_id of this NeutronListNetworksRequest.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

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
        if not isinstance(other, NeutronListNetworksRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
