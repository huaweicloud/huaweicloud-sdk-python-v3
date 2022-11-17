# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPortsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'id': 'str',
        'limit': 'int',
        'admin_state_up': 'bool',
        'network_id': 'str',
        'mac_address': 'str',
        'device_id': 'str',
        'device_owner': 'str',
        'status': 'str',
        'marker': 'str',
        'fixed_ips': 'str',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'limit': 'limit',
        'admin_state_up': 'admin_state_up',
        'network_id': 'network_id',
        'mac_address': 'mac_address',
        'device_id': 'device_id',
        'device_owner': 'device_owner',
        'status': 'status',
        'marker': 'marker',
        'fixed_ips': 'fixed_ips',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, name=None, id=None, limit=None, admin_state_up=None, network_id=None, mac_address=None, device_id=None, device_owner=None, status=None, marker=None, fixed_ips=None, enterprise_project_id=None):
        """ListPortsRequest

        The model defined in huaweicloud sdk

        :param name: 功能说明：按照name过滤查询  取值范围：最大长度不超过255
        :type name: str
        :param id: 按照port_id过滤查询
        :type id: str
        :param limit: 每页返回的个数
        :type limit: int
        :param admin_state_up: 按照admin_state_up进行过滤
        :type admin_state_up: bool
        :param network_id: 按照network_id过滤查询
        :type network_id: str
        :param mac_address: 按照mac_address过滤查询
        :type mac_address: str
        :param device_id: 按照device_id过滤查询
        :type device_id: str
        :param device_owner: 按照device_owner过滤查询
        :type device_owner: str
        :param status: 功能说明：按照status过滤查询  取值范围：ACTIVE、BUILD、DOWN
        :type status: str
        :param marker: 分页查询起始的资源ID，为空时查询第一页
        :type marker: str
        :param fixed_ips: 按照fixed_ips&#x3D;ip_address或者fixed_ips&#x3D;subnet_id过滤查询
        :type fixed_ips: str
        :param enterprise_project_id: 功能说明：企业项目ID，用于基于企业项目的权限管理。  取值范围：最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。“0”表示默认企业项目。  若需要查询当前用户所有企业项目绑定的端口，请传参all_granted_eps。
        :type enterprise_project_id: str
        """
        
        

        self._name = None
        self._id = None
        self._limit = None
        self._admin_state_up = None
        self._network_id = None
        self._mac_address = None
        self._device_id = None
        self._device_owner = None
        self._status = None
        self._marker = None
        self._fixed_ips = None
        self._enterprise_project_id = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if limit is not None:
            self.limit = limit
        if admin_state_up is not None:
            self.admin_state_up = admin_state_up
        if network_id is not None:
            self.network_id = network_id
        if mac_address is not None:
            self.mac_address = mac_address
        if device_id is not None:
            self.device_id = device_id
        if device_owner is not None:
            self.device_owner = device_owner
        if status is not None:
            self.status = status
        if marker is not None:
            self.marker = marker
        if fixed_ips is not None:
            self.fixed_ips = fixed_ips
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def name(self):
        """Gets the name of this ListPortsRequest.

        功能说明：按照name过滤查询  取值范围：最大长度不超过255

        :return: The name of this ListPortsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListPortsRequest.

        功能说明：按照name过滤查询  取值范围：最大长度不超过255

        :param name: The name of this ListPortsRequest.
        :type name: str
        """
        self._name = name

    @property
    def id(self):
        """Gets the id of this ListPortsRequest.

        按照port_id过滤查询

        :return: The id of this ListPortsRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListPortsRequest.

        按照port_id过滤查询

        :param id: The id of this ListPortsRequest.
        :type id: str
        """
        self._id = id

    @property
    def limit(self):
        """Gets the limit of this ListPortsRequest.

        每页返回的个数

        :return: The limit of this ListPortsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListPortsRequest.

        每页返回的个数

        :param limit: The limit of this ListPortsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this ListPortsRequest.

        按照admin_state_up进行过滤

        :return: The admin_state_up of this ListPortsRequest.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this ListPortsRequest.

        按照admin_state_up进行过滤

        :param admin_state_up: The admin_state_up of this ListPortsRequest.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def network_id(self):
        """Gets the network_id of this ListPortsRequest.

        按照network_id过滤查询

        :return: The network_id of this ListPortsRequest.
        :rtype: str
        """
        return self._network_id

    @network_id.setter
    def network_id(self, network_id):
        """Sets the network_id of this ListPortsRequest.

        按照network_id过滤查询

        :param network_id: The network_id of this ListPortsRequest.
        :type network_id: str
        """
        self._network_id = network_id

    @property
    def mac_address(self):
        """Gets the mac_address of this ListPortsRequest.

        按照mac_address过滤查询

        :return: The mac_address of this ListPortsRequest.
        :rtype: str
        """
        return self._mac_address

    @mac_address.setter
    def mac_address(self, mac_address):
        """Sets the mac_address of this ListPortsRequest.

        按照mac_address过滤查询

        :param mac_address: The mac_address of this ListPortsRequest.
        :type mac_address: str
        """
        self._mac_address = mac_address

    @property
    def device_id(self):
        """Gets the device_id of this ListPortsRequest.

        按照device_id过滤查询

        :return: The device_id of this ListPortsRequest.
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this ListPortsRequest.

        按照device_id过滤查询

        :param device_id: The device_id of this ListPortsRequest.
        :type device_id: str
        """
        self._device_id = device_id

    @property
    def device_owner(self):
        """Gets the device_owner of this ListPortsRequest.

        按照device_owner过滤查询

        :return: The device_owner of this ListPortsRequest.
        :rtype: str
        """
        return self._device_owner

    @device_owner.setter
    def device_owner(self, device_owner):
        """Sets the device_owner of this ListPortsRequest.

        按照device_owner过滤查询

        :param device_owner: The device_owner of this ListPortsRequest.
        :type device_owner: str
        """
        self._device_owner = device_owner

    @property
    def status(self):
        """Gets the status of this ListPortsRequest.

        功能说明：按照status过滤查询  取值范围：ACTIVE、BUILD、DOWN

        :return: The status of this ListPortsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListPortsRequest.

        功能说明：按照status过滤查询  取值范围：ACTIVE、BUILD、DOWN

        :param status: The status of this ListPortsRequest.
        :type status: str
        """
        self._status = status

    @property
    def marker(self):
        """Gets the marker of this ListPortsRequest.

        分页查询起始的资源ID，为空时查询第一页

        :return: The marker of this ListPortsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListPortsRequest.

        分页查询起始的资源ID，为空时查询第一页

        :param marker: The marker of this ListPortsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def fixed_ips(self):
        """Gets the fixed_ips of this ListPortsRequest.

        按照fixed_ips=ip_address或者fixed_ips=subnet_id过滤查询

        :return: The fixed_ips of this ListPortsRequest.
        :rtype: str
        """
        return self._fixed_ips

    @fixed_ips.setter
    def fixed_ips(self, fixed_ips):
        """Sets the fixed_ips of this ListPortsRequest.

        按照fixed_ips=ip_address或者fixed_ips=subnet_id过滤查询

        :param fixed_ips: The fixed_ips of this ListPortsRequest.
        :type fixed_ips: str
        """
        self._fixed_ips = fixed_ips

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListPortsRequest.

        功能说明：企业项目ID，用于基于企业项目的权限管理。  取值范围：最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。“0”表示默认企业项目。  若需要查询当前用户所有企业项目绑定的端口，请传参all_granted_eps。

        :return: The enterprise_project_id of this ListPortsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListPortsRequest.

        功能说明：企业项目ID，用于基于企业项目的权限管理。  取值范围：最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。“0”表示默认企业项目。  若需要查询当前用户所有企业项目绑定的端口，请传参all_granted_eps。

        :param enterprise_project_id: The enterprise_project_id of this ListPortsRequest.
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
        if not isinstance(other, ListPortsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
