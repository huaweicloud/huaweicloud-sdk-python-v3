# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NeutronListRoutersRequest:

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
        'status': 'str',
        'tenant_id': 'str',
        'admin_state_up': 'bool'
    }

    attribute_map = {
        'limit': 'limit',
        'marker': 'marker',
        'id': 'id',
        'status': 'status',
        'tenant_id': 'tenant_id',
        'admin_state_up': 'admin_state_up'
    }

    def __init__(self, limit=None, marker=None, id=None, status=None, tenant_id=None, admin_state_up=None):
        """NeutronListRoutersRequest

        The model defined in huaweicloud sdk

        :param limit: 每页返回的个数
        :type limit: int
        :param marker: 分页查询起始的资源ID，为空时查询第一页
        :type marker: str
        :param id: 按照路由器的ID过滤查询
        :type id: str
        :param status: 按照路由器的状态过滤查询，取值范围：ACTIVE， DOWN，ERROR
        :type status: str
        :param tenant_id: 按照路由器所属的项目ID过滤查询
        :type tenant_id: str
        :param admin_state_up: 按照路由器的管理状态过滤查询，取值范围：true or false
        :type admin_state_up: bool
        """
        
        

        self._limit = None
        self._marker = None
        self._id = None
        self._status = None
        self._tenant_id = None
        self._admin_state_up = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if id is not None:
            self.id = id
        if status is not None:
            self.status = status
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if admin_state_up is not None:
            self.admin_state_up = admin_state_up

    @property
    def limit(self):
        """Gets the limit of this NeutronListRoutersRequest.

        每页返回的个数

        :return: The limit of this NeutronListRoutersRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this NeutronListRoutersRequest.

        每页返回的个数

        :param limit: The limit of this NeutronListRoutersRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this NeutronListRoutersRequest.

        分页查询起始的资源ID，为空时查询第一页

        :return: The marker of this NeutronListRoutersRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this NeutronListRoutersRequest.

        分页查询起始的资源ID，为空时查询第一页

        :param marker: The marker of this NeutronListRoutersRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def id(self):
        """Gets the id of this NeutronListRoutersRequest.

        按照路由器的ID过滤查询

        :return: The id of this NeutronListRoutersRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NeutronListRoutersRequest.

        按照路由器的ID过滤查询

        :param id: The id of this NeutronListRoutersRequest.
        :type id: str
        """
        self._id = id

    @property
    def status(self):
        """Gets the status of this NeutronListRoutersRequest.

        按照路由器的状态过滤查询，取值范围：ACTIVE， DOWN，ERROR

        :return: The status of this NeutronListRoutersRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this NeutronListRoutersRequest.

        按照路由器的状态过滤查询，取值范围：ACTIVE， DOWN，ERROR

        :param status: The status of this NeutronListRoutersRequest.
        :type status: str
        """
        self._status = status

    @property
    def tenant_id(self):
        """Gets the tenant_id of this NeutronListRoutersRequest.

        按照路由器所属的项目ID过滤查询

        :return: The tenant_id of this NeutronListRoutersRequest.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this NeutronListRoutersRequest.

        按照路由器所属的项目ID过滤查询

        :param tenant_id: The tenant_id of this NeutronListRoutersRequest.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this NeutronListRoutersRequest.

        按照路由器的管理状态过滤查询，取值范围：true or false

        :return: The admin_state_up of this NeutronListRoutersRequest.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this NeutronListRoutersRequest.

        按照路由器的管理状态过滤查询，取值范围：true or false

        :param admin_state_up: The admin_state_up of this NeutronListRoutersRequest.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

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
        if not isinstance(other, NeutronListRoutersRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
