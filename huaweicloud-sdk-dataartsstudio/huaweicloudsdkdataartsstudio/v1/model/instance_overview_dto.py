# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstanceOverviewDTO:

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
        'name': 'str',
        'description': 'str',
        'external_address': 'str',
        'intranet_address': 'str',
        'intranet_address_ipv6': 'str',
        'public_zone_id': 'str',
        'public_zone_name': 'str',
        'private_zone_id': 'str',
        'private_zone_name': 'str',
        'enterprise_project_id': 'str',
        'create_time': 'int',
        'create_user': 'str',
        'current_namespace_publish_api_num': 'int',
        'all_namespace_publish_api_num': 'int',
        'api_publishable_num': 'int',
        'deletable': 'bool',
        'charge_status': 'str',
        'order_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'external_address': 'external_address',
        'intranet_address': 'intranet_address',
        'intranet_address_ipv6': 'intranet_address_ipv6',
        'public_zone_id': 'public_zone_id',
        'public_zone_name': 'public_zone_name',
        'private_zone_id': 'private_zone_id',
        'private_zone_name': 'private_zone_name',
        'enterprise_project_id': 'enterprise_project_id',
        'create_time': 'create_time',
        'create_user': 'create_user',
        'current_namespace_publish_api_num': 'current_namespace_publish_api_num',
        'all_namespace_publish_api_num': 'all_namespace_publish_api_num',
        'api_publishable_num': 'api_publishable_num',
        'deletable': 'deletable',
        'charge_status': 'charge_status',
        'order_id': 'order_id'
    }

    def __init__(self, id=None, name=None, description=None, external_address=None, intranet_address=None, intranet_address_ipv6=None, public_zone_id=None, public_zone_name=None, private_zone_id=None, private_zone_name=None, enterprise_project_id=None, create_time=None, create_user=None, current_namespace_publish_api_num=None, all_namespace_publish_api_num=None, api_publishable_num=None, deletable=None, charge_status=None, order_id=None):
        """InstanceOverviewDTO

        The model defined in huaweicloud sdk

        :param id: 集群ID。
        :type id: str
        :param name: 集群名称。
        :type name: str
        :param description: 集群描述信息。
        :type description: str
        :param external_address: 公网IP地址。
        :type external_address: str
        :param intranet_address: 内网IPv4地址。
        :type intranet_address: str
        :param intranet_address_ipv6: 内网IPv6地址。
        :type intranet_address_ipv6: str
        :param public_zone_id: 公网域名ID。
        :type public_zone_id: str
        :param public_zone_name: 公网域名名称。
        :type public_zone_name: str
        :param private_zone_id: 内网域名ID。
        :type private_zone_id: str
        :param private_zone_name: 内网域名名称。
        :type private_zone_name: str
        :param enterprise_project_id: 企业项目ID。
        :type enterprise_project_id: str
        :param create_time: 创建时间。
        :type create_time: int
        :param create_user: 创建人。
        :type create_user: str
        :param current_namespace_publish_api_num: 当前工作空间已发布的API数量。
        :type current_namespace_publish_api_num: int
        :param all_namespace_publish_api_num: 所有工作空间已发布的API数量。
        :type all_namespace_publish_api_num: int
        :param api_publishable_num: 集群API总配额。
        :type api_publishable_num: int
        :param deletable: 集群是否可以删除。
        :type deletable: bool
        :param charge_status: 集群计费状态，NO_CHARGE：未计费、CHARGED：已计费，GRACE：宽限期、RETENTION：保留期。
        :type charge_status: str
        :param order_id: 订单ID。
        :type order_id: str
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._external_address = None
        self._intranet_address = None
        self._intranet_address_ipv6 = None
        self._public_zone_id = None
        self._public_zone_name = None
        self._private_zone_id = None
        self._private_zone_name = None
        self._enterprise_project_id = None
        self._create_time = None
        self._create_user = None
        self._current_namespace_publish_api_num = None
        self._all_namespace_publish_api_num = None
        self._api_publishable_num = None
        self._deletable = None
        self._charge_status = None
        self._order_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if external_address is not None:
            self.external_address = external_address
        if intranet_address is not None:
            self.intranet_address = intranet_address
        if intranet_address_ipv6 is not None:
            self.intranet_address_ipv6 = intranet_address_ipv6
        if public_zone_id is not None:
            self.public_zone_id = public_zone_id
        if public_zone_name is not None:
            self.public_zone_name = public_zone_name
        if private_zone_id is not None:
            self.private_zone_id = private_zone_id
        if private_zone_name is not None:
            self.private_zone_name = private_zone_name
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if create_time is not None:
            self.create_time = create_time
        if create_user is not None:
            self.create_user = create_user
        if current_namespace_publish_api_num is not None:
            self.current_namespace_publish_api_num = current_namespace_publish_api_num
        if all_namespace_publish_api_num is not None:
            self.all_namespace_publish_api_num = all_namespace_publish_api_num
        if api_publishable_num is not None:
            self.api_publishable_num = api_publishable_num
        if deletable is not None:
            self.deletable = deletable
        if charge_status is not None:
            self.charge_status = charge_status
        if order_id is not None:
            self.order_id = order_id

    @property
    def id(self):
        """Gets the id of this InstanceOverviewDTO.

        集群ID。

        :return: The id of this InstanceOverviewDTO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InstanceOverviewDTO.

        集群ID。

        :param id: The id of this InstanceOverviewDTO.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this InstanceOverviewDTO.

        集群名称。

        :return: The name of this InstanceOverviewDTO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InstanceOverviewDTO.

        集群名称。

        :param name: The name of this InstanceOverviewDTO.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this InstanceOverviewDTO.

        集群描述信息。

        :return: The description of this InstanceOverviewDTO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this InstanceOverviewDTO.

        集群描述信息。

        :param description: The description of this InstanceOverviewDTO.
        :type description: str
        """
        self._description = description

    @property
    def external_address(self):
        """Gets the external_address of this InstanceOverviewDTO.

        公网IP地址。

        :return: The external_address of this InstanceOverviewDTO.
        :rtype: str
        """
        return self._external_address

    @external_address.setter
    def external_address(self, external_address):
        """Sets the external_address of this InstanceOverviewDTO.

        公网IP地址。

        :param external_address: The external_address of this InstanceOverviewDTO.
        :type external_address: str
        """
        self._external_address = external_address

    @property
    def intranet_address(self):
        """Gets the intranet_address of this InstanceOverviewDTO.

        内网IPv4地址。

        :return: The intranet_address of this InstanceOverviewDTO.
        :rtype: str
        """
        return self._intranet_address

    @intranet_address.setter
    def intranet_address(self, intranet_address):
        """Sets the intranet_address of this InstanceOverviewDTO.

        内网IPv4地址。

        :param intranet_address: The intranet_address of this InstanceOverviewDTO.
        :type intranet_address: str
        """
        self._intranet_address = intranet_address

    @property
    def intranet_address_ipv6(self):
        """Gets the intranet_address_ipv6 of this InstanceOverviewDTO.

        内网IPv6地址。

        :return: The intranet_address_ipv6 of this InstanceOverviewDTO.
        :rtype: str
        """
        return self._intranet_address_ipv6

    @intranet_address_ipv6.setter
    def intranet_address_ipv6(self, intranet_address_ipv6):
        """Sets the intranet_address_ipv6 of this InstanceOverviewDTO.

        内网IPv6地址。

        :param intranet_address_ipv6: The intranet_address_ipv6 of this InstanceOverviewDTO.
        :type intranet_address_ipv6: str
        """
        self._intranet_address_ipv6 = intranet_address_ipv6

    @property
    def public_zone_id(self):
        """Gets the public_zone_id of this InstanceOverviewDTO.

        公网域名ID。

        :return: The public_zone_id of this InstanceOverviewDTO.
        :rtype: str
        """
        return self._public_zone_id

    @public_zone_id.setter
    def public_zone_id(self, public_zone_id):
        """Sets the public_zone_id of this InstanceOverviewDTO.

        公网域名ID。

        :param public_zone_id: The public_zone_id of this InstanceOverviewDTO.
        :type public_zone_id: str
        """
        self._public_zone_id = public_zone_id

    @property
    def public_zone_name(self):
        """Gets the public_zone_name of this InstanceOverviewDTO.

        公网域名名称。

        :return: The public_zone_name of this InstanceOverviewDTO.
        :rtype: str
        """
        return self._public_zone_name

    @public_zone_name.setter
    def public_zone_name(self, public_zone_name):
        """Sets the public_zone_name of this InstanceOverviewDTO.

        公网域名名称。

        :param public_zone_name: The public_zone_name of this InstanceOverviewDTO.
        :type public_zone_name: str
        """
        self._public_zone_name = public_zone_name

    @property
    def private_zone_id(self):
        """Gets the private_zone_id of this InstanceOverviewDTO.

        内网域名ID。

        :return: The private_zone_id of this InstanceOverviewDTO.
        :rtype: str
        """
        return self._private_zone_id

    @private_zone_id.setter
    def private_zone_id(self, private_zone_id):
        """Sets the private_zone_id of this InstanceOverviewDTO.

        内网域名ID。

        :param private_zone_id: The private_zone_id of this InstanceOverviewDTO.
        :type private_zone_id: str
        """
        self._private_zone_id = private_zone_id

    @property
    def private_zone_name(self):
        """Gets the private_zone_name of this InstanceOverviewDTO.

        内网域名名称。

        :return: The private_zone_name of this InstanceOverviewDTO.
        :rtype: str
        """
        return self._private_zone_name

    @private_zone_name.setter
    def private_zone_name(self, private_zone_name):
        """Sets the private_zone_name of this InstanceOverviewDTO.

        内网域名名称。

        :param private_zone_name: The private_zone_name of this InstanceOverviewDTO.
        :type private_zone_name: str
        """
        self._private_zone_name = private_zone_name

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this InstanceOverviewDTO.

        企业项目ID。

        :return: The enterprise_project_id of this InstanceOverviewDTO.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this InstanceOverviewDTO.

        企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this InstanceOverviewDTO.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def create_time(self):
        """Gets the create_time of this InstanceOverviewDTO.

        创建时间。

        :return: The create_time of this InstanceOverviewDTO.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this InstanceOverviewDTO.

        创建时间。

        :param create_time: The create_time of this InstanceOverviewDTO.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def create_user(self):
        """Gets the create_user of this InstanceOverviewDTO.

        创建人。

        :return: The create_user of this InstanceOverviewDTO.
        :rtype: str
        """
        return self._create_user

    @create_user.setter
    def create_user(self, create_user):
        """Sets the create_user of this InstanceOverviewDTO.

        创建人。

        :param create_user: The create_user of this InstanceOverviewDTO.
        :type create_user: str
        """
        self._create_user = create_user

    @property
    def current_namespace_publish_api_num(self):
        """Gets the current_namespace_publish_api_num of this InstanceOverviewDTO.

        当前工作空间已发布的API数量。

        :return: The current_namespace_publish_api_num of this InstanceOverviewDTO.
        :rtype: int
        """
        return self._current_namespace_publish_api_num

    @current_namespace_publish_api_num.setter
    def current_namespace_publish_api_num(self, current_namespace_publish_api_num):
        """Sets the current_namespace_publish_api_num of this InstanceOverviewDTO.

        当前工作空间已发布的API数量。

        :param current_namespace_publish_api_num: The current_namespace_publish_api_num of this InstanceOverviewDTO.
        :type current_namespace_publish_api_num: int
        """
        self._current_namespace_publish_api_num = current_namespace_publish_api_num

    @property
    def all_namespace_publish_api_num(self):
        """Gets the all_namespace_publish_api_num of this InstanceOverviewDTO.

        所有工作空间已发布的API数量。

        :return: The all_namespace_publish_api_num of this InstanceOverviewDTO.
        :rtype: int
        """
        return self._all_namespace_publish_api_num

    @all_namespace_publish_api_num.setter
    def all_namespace_publish_api_num(self, all_namespace_publish_api_num):
        """Sets the all_namespace_publish_api_num of this InstanceOverviewDTO.

        所有工作空间已发布的API数量。

        :param all_namespace_publish_api_num: The all_namespace_publish_api_num of this InstanceOverviewDTO.
        :type all_namespace_publish_api_num: int
        """
        self._all_namespace_publish_api_num = all_namespace_publish_api_num

    @property
    def api_publishable_num(self):
        """Gets the api_publishable_num of this InstanceOverviewDTO.

        集群API总配额。

        :return: The api_publishable_num of this InstanceOverviewDTO.
        :rtype: int
        """
        return self._api_publishable_num

    @api_publishable_num.setter
    def api_publishable_num(self, api_publishable_num):
        """Sets the api_publishable_num of this InstanceOverviewDTO.

        集群API总配额。

        :param api_publishable_num: The api_publishable_num of this InstanceOverviewDTO.
        :type api_publishable_num: int
        """
        self._api_publishable_num = api_publishable_num

    @property
    def deletable(self):
        """Gets the deletable of this InstanceOverviewDTO.

        集群是否可以删除。

        :return: The deletable of this InstanceOverviewDTO.
        :rtype: bool
        """
        return self._deletable

    @deletable.setter
    def deletable(self, deletable):
        """Sets the deletable of this InstanceOverviewDTO.

        集群是否可以删除。

        :param deletable: The deletable of this InstanceOverviewDTO.
        :type deletable: bool
        """
        self._deletable = deletable

    @property
    def charge_status(self):
        """Gets the charge_status of this InstanceOverviewDTO.

        集群计费状态，NO_CHARGE：未计费、CHARGED：已计费，GRACE：宽限期、RETENTION：保留期。

        :return: The charge_status of this InstanceOverviewDTO.
        :rtype: str
        """
        return self._charge_status

    @charge_status.setter
    def charge_status(self, charge_status):
        """Sets the charge_status of this InstanceOverviewDTO.

        集群计费状态，NO_CHARGE：未计费、CHARGED：已计费，GRACE：宽限期、RETENTION：保留期。

        :param charge_status: The charge_status of this InstanceOverviewDTO.
        :type charge_status: str
        """
        self._charge_status = charge_status

    @property
    def order_id(self):
        """Gets the order_id of this InstanceOverviewDTO.

        订单ID。

        :return: The order_id of this InstanceOverviewDTO.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this InstanceOverviewDTO.

        订单ID。

        :param order_id: The order_id of this InstanceOverviewDTO.
        :type order_id: str
        """
        self._order_id = order_id

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
        if not isinstance(other, InstanceOverviewDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
