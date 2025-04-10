# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListMembersRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'pool_id': 'str',
        'limit': 'int',
        'marker': 'str',
        'page_reverse': 'bool',
        'id': 'str',
        'name': 'str',
        'address': 'str',
        'protocol_port': 'int',
        'subnet_id': 'str',
        'admin_state_up': 'bool',
        'weight': 'int',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'pool_id': 'pool_id',
        'limit': 'limit',
        'marker': 'marker',
        'page_reverse': 'page_reverse',
        'id': 'id',
        'name': 'name',
        'address': 'address',
        'protocol_port': 'protocol_port',
        'subnet_id': 'subnet_id',
        'admin_state_up': 'admin_state_up',
        'weight': 'weight',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, pool_id=None, limit=None, marker=None, page_reverse=None, id=None, name=None, address=None, protocol_port=None, subnet_id=None, admin_state_up=None, weight=None, enterprise_project_id=None):
        r"""ListMembersRequest

        The model defined in huaweicloud sdk

        :param pool_id: 后端云服务器组id
        :type pool_id: str
        :param limit: 分页查询中每页的后端服务器个数
        :type limit: int
        :param marker: 分页查询的起始的资源id，表示上一页最后一条查询记录的后端服务器的id。不指定时表示查询第一页。
        :type marker: str
        :param page_reverse: 分页的顺序，true表示从后往前分页，false表示从前往后分页，默认为false。
        :type page_reverse: bool
        :param id: 后端云服务器的ID。
        :type id: str
        :param name: 后端云服务器的名称。
        :type name: str
        :param address: 后端云服务器对应的IP地址。
        :type address: str
        :param protocol_port: 后端云服务器后端端口的协议号。
        :type protocol_port: int
        :param subnet_id: 后端云服务器所在的子网ID。
        :type subnet_id: str
        :param admin_state_up: 后端云服务器的管理状态。取值范围：true/false。
        :type admin_state_up: bool
        :param weight: 后端云服务器的权重。
        :type weight: int
        :param enterprise_project_id: 企业项目ID。 不传时查询default企业项目（即enterprise_project_id&#x3D;0）下的资源，鉴权按照default企业项目鉴权。 如果传值enterprise_project_id&#x3D;all_granted_eps，则表示查询所有有权限的企业项目下的资源。 其他情况则传已存在的企业项目ID。此时会校验ID，若不存在或格式错误则报错。
        :type enterprise_project_id: str
        """
        
        

        self._pool_id = None
        self._limit = None
        self._marker = None
        self._page_reverse = None
        self._id = None
        self._name = None
        self._address = None
        self._protocol_port = None
        self._subnet_id = None
        self._admin_state_up = None
        self._weight = None
        self._enterprise_project_id = None
        self.discriminator = None

        self.pool_id = pool_id
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if page_reverse is not None:
            self.page_reverse = page_reverse
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if address is not None:
            self.address = address
        if protocol_port is not None:
            self.protocol_port = protocol_port
        if subnet_id is not None:
            self.subnet_id = subnet_id
        if admin_state_up is not None:
            self.admin_state_up = admin_state_up
        if weight is not None:
            self.weight = weight
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def pool_id(self):
        r"""Gets the pool_id of this ListMembersRequest.

        后端云服务器组id

        :return: The pool_id of this ListMembersRequest.
        :rtype: str
        """
        return self._pool_id

    @pool_id.setter
    def pool_id(self, pool_id):
        r"""Sets the pool_id of this ListMembersRequest.

        后端云服务器组id

        :param pool_id: The pool_id of this ListMembersRequest.
        :type pool_id: str
        """
        self._pool_id = pool_id

    @property
    def limit(self):
        r"""Gets the limit of this ListMembersRequest.

        分页查询中每页的后端服务器个数

        :return: The limit of this ListMembersRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListMembersRequest.

        分页查询中每页的后端服务器个数

        :param limit: The limit of this ListMembersRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ListMembersRequest.

        分页查询的起始的资源id，表示上一页最后一条查询记录的后端服务器的id。不指定时表示查询第一页。

        :return: The marker of this ListMembersRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListMembersRequest.

        分页查询的起始的资源id，表示上一页最后一条查询记录的后端服务器的id。不指定时表示查询第一页。

        :param marker: The marker of this ListMembersRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def page_reverse(self):
        r"""Gets the page_reverse of this ListMembersRequest.

        分页的顺序，true表示从后往前分页，false表示从前往后分页，默认为false。

        :return: The page_reverse of this ListMembersRequest.
        :rtype: bool
        """
        return self._page_reverse

    @page_reverse.setter
    def page_reverse(self, page_reverse):
        r"""Sets the page_reverse of this ListMembersRequest.

        分页的顺序，true表示从后往前分页，false表示从前往后分页，默认为false。

        :param page_reverse: The page_reverse of this ListMembersRequest.
        :type page_reverse: bool
        """
        self._page_reverse = page_reverse

    @property
    def id(self):
        r"""Gets the id of this ListMembersRequest.

        后端云服务器的ID。

        :return: The id of this ListMembersRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListMembersRequest.

        后端云服务器的ID。

        :param id: The id of this ListMembersRequest.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ListMembersRequest.

        后端云服务器的名称。

        :return: The name of this ListMembersRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListMembersRequest.

        后端云服务器的名称。

        :param name: The name of this ListMembersRequest.
        :type name: str
        """
        self._name = name

    @property
    def address(self):
        r"""Gets the address of this ListMembersRequest.

        后端云服务器对应的IP地址。

        :return: The address of this ListMembersRequest.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        r"""Sets the address of this ListMembersRequest.

        后端云服务器对应的IP地址。

        :param address: The address of this ListMembersRequest.
        :type address: str
        """
        self._address = address

    @property
    def protocol_port(self):
        r"""Gets the protocol_port of this ListMembersRequest.

        后端云服务器后端端口的协议号。

        :return: The protocol_port of this ListMembersRequest.
        :rtype: int
        """
        return self._protocol_port

    @protocol_port.setter
    def protocol_port(self, protocol_port):
        r"""Sets the protocol_port of this ListMembersRequest.

        后端云服务器后端端口的协议号。

        :param protocol_port: The protocol_port of this ListMembersRequest.
        :type protocol_port: int
        """
        self._protocol_port = protocol_port

    @property
    def subnet_id(self):
        r"""Gets the subnet_id of this ListMembersRequest.

        后端云服务器所在的子网ID。

        :return: The subnet_id of this ListMembersRequest.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        r"""Sets the subnet_id of this ListMembersRequest.

        后端云服务器所在的子网ID。

        :param subnet_id: The subnet_id of this ListMembersRequest.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def admin_state_up(self):
        r"""Gets the admin_state_up of this ListMembersRequest.

        后端云服务器的管理状态。取值范围：true/false。

        :return: The admin_state_up of this ListMembersRequest.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        r"""Sets the admin_state_up of this ListMembersRequest.

        后端云服务器的管理状态。取值范围：true/false。

        :param admin_state_up: The admin_state_up of this ListMembersRequest.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def weight(self):
        r"""Gets the weight of this ListMembersRequest.

        后端云服务器的权重。

        :return: The weight of this ListMembersRequest.
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        r"""Sets the weight of this ListMembersRequest.

        后端云服务器的权重。

        :param weight: The weight of this ListMembersRequest.
        :type weight: int
        """
        self._weight = weight

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListMembersRequest.

        企业项目ID。 不传时查询default企业项目（即enterprise_project_id=0）下的资源，鉴权按照default企业项目鉴权。 如果传值enterprise_project_id=all_granted_eps，则表示查询所有有权限的企业项目下的资源。 其他情况则传已存在的企业项目ID。此时会校验ID，若不存在或格式错误则报错。

        :return: The enterprise_project_id of this ListMembersRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListMembersRequest.

        企业项目ID。 不传时查询default企业项目（即enterprise_project_id=0）下的资源，鉴权按照default企业项目鉴权。 如果传值enterprise_project_id=all_granted_eps，则表示查询所有有权限的企业项目下的资源。 其他情况则传已存在的企业项目ID。此时会校验ID，若不存在或格式错误则报错。

        :param enterprise_project_id: The enterprise_project_id of this ListMembersRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, ListMembersRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
