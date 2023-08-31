# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EquipmentOspfItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ospf_enabled': 'bool',
        'area_id': 'int',
        'post_to_cloud': 'bool',
        'hello_timer': 'int',
        'router_id': 'str',
        'interfaces': 'list[str]',
        'filter_enabled': 'bool',
        'trust_list': 'list[str]',
        'block_list': 'list[str]'
    }

    attribute_map = {
        'ospf_enabled': 'ospf_enabled',
        'area_id': 'area_id',
        'post_to_cloud': 'post_to_cloud',
        'hello_timer': 'hello_timer',
        'router_id': 'router_id',
        'interfaces': 'interfaces',
        'filter_enabled': 'filter_enabled',
        'trust_list': 'trust_list',
        'block_list': 'block_list'
    }

    def __init__(self, ospf_enabled=None, area_id=None, post_to_cloud=None, hello_timer=None, router_id=None, interfaces=None, filter_enabled=None, trust_list=None, block_list=None):
        """EquipmentOspfItem

        The model defined in huaweicloud sdk

        :param ospf_enabled: 是否启用OSPF
        :type ospf_enabled: bool
        :param area_id: 区域标识
        :type area_id: int
        :param post_to_cloud: 发布到企业连接网络
        :type post_to_cloud: bool
        :param hello_timer: 发送Hello报文的时间间隔，单位是秒
        :type hello_timer: int
        :param router_id: 点分十进制格式，OSPF协议使用全网唯一的Router ID
        :type router_id: str
        :param interfaces: 启用OSPF协议的接口列表
        :type interfaces: list[str]
        :param filter_enabled: 是否启用前缀过滤
        :type filter_enabled: bool
        :param trust_list: 白名单列表
        :type trust_list: list[str]
        :param block_list: 黑名单列表
        :type block_list: list[str]
        """
        
        

        self._ospf_enabled = None
        self._area_id = None
        self._post_to_cloud = None
        self._hello_timer = None
        self._router_id = None
        self._interfaces = None
        self._filter_enabled = None
        self._trust_list = None
        self._block_list = None
        self.discriminator = None

        self.ospf_enabled = ospf_enabled
        if area_id is not None:
            self.area_id = area_id
        if post_to_cloud is not None:
            self.post_to_cloud = post_to_cloud
        if hello_timer is not None:
            self.hello_timer = hello_timer
        if router_id is not None:
            self.router_id = router_id
        if interfaces is not None:
            self.interfaces = interfaces
        if filter_enabled is not None:
            self.filter_enabled = filter_enabled
        if trust_list is not None:
            self.trust_list = trust_list
        if block_list is not None:
            self.block_list = block_list

    @property
    def ospf_enabled(self):
        """Gets the ospf_enabled of this EquipmentOspfItem.

        是否启用OSPF

        :return: The ospf_enabled of this EquipmentOspfItem.
        :rtype: bool
        """
        return self._ospf_enabled

    @ospf_enabled.setter
    def ospf_enabled(self, ospf_enabled):
        """Sets the ospf_enabled of this EquipmentOspfItem.

        是否启用OSPF

        :param ospf_enabled: The ospf_enabled of this EquipmentOspfItem.
        :type ospf_enabled: bool
        """
        self._ospf_enabled = ospf_enabled

    @property
    def area_id(self):
        """Gets the area_id of this EquipmentOspfItem.

        区域标识

        :return: The area_id of this EquipmentOspfItem.
        :rtype: int
        """
        return self._area_id

    @area_id.setter
    def area_id(self, area_id):
        """Sets the area_id of this EquipmentOspfItem.

        区域标识

        :param area_id: The area_id of this EquipmentOspfItem.
        :type area_id: int
        """
        self._area_id = area_id

    @property
    def post_to_cloud(self):
        """Gets the post_to_cloud of this EquipmentOspfItem.

        发布到企业连接网络

        :return: The post_to_cloud of this EquipmentOspfItem.
        :rtype: bool
        """
        return self._post_to_cloud

    @post_to_cloud.setter
    def post_to_cloud(self, post_to_cloud):
        """Sets the post_to_cloud of this EquipmentOspfItem.

        发布到企业连接网络

        :param post_to_cloud: The post_to_cloud of this EquipmentOspfItem.
        :type post_to_cloud: bool
        """
        self._post_to_cloud = post_to_cloud

    @property
    def hello_timer(self):
        """Gets the hello_timer of this EquipmentOspfItem.

        发送Hello报文的时间间隔，单位是秒

        :return: The hello_timer of this EquipmentOspfItem.
        :rtype: int
        """
        return self._hello_timer

    @hello_timer.setter
    def hello_timer(self, hello_timer):
        """Sets the hello_timer of this EquipmentOspfItem.

        发送Hello报文的时间间隔，单位是秒

        :param hello_timer: The hello_timer of this EquipmentOspfItem.
        :type hello_timer: int
        """
        self._hello_timer = hello_timer

    @property
    def router_id(self):
        """Gets the router_id of this EquipmentOspfItem.

        点分十进制格式，OSPF协议使用全网唯一的Router ID

        :return: The router_id of this EquipmentOspfItem.
        :rtype: str
        """
        return self._router_id

    @router_id.setter
    def router_id(self, router_id):
        """Sets the router_id of this EquipmentOspfItem.

        点分十进制格式，OSPF协议使用全网唯一的Router ID

        :param router_id: The router_id of this EquipmentOspfItem.
        :type router_id: str
        """
        self._router_id = router_id

    @property
    def interfaces(self):
        """Gets the interfaces of this EquipmentOspfItem.

        启用OSPF协议的接口列表

        :return: The interfaces of this EquipmentOspfItem.
        :rtype: list[str]
        """
        return self._interfaces

    @interfaces.setter
    def interfaces(self, interfaces):
        """Sets the interfaces of this EquipmentOspfItem.

        启用OSPF协议的接口列表

        :param interfaces: The interfaces of this EquipmentOspfItem.
        :type interfaces: list[str]
        """
        self._interfaces = interfaces

    @property
    def filter_enabled(self):
        """Gets the filter_enabled of this EquipmentOspfItem.

        是否启用前缀过滤

        :return: The filter_enabled of this EquipmentOspfItem.
        :rtype: bool
        """
        return self._filter_enabled

    @filter_enabled.setter
    def filter_enabled(self, filter_enabled):
        """Sets the filter_enabled of this EquipmentOspfItem.

        是否启用前缀过滤

        :param filter_enabled: The filter_enabled of this EquipmentOspfItem.
        :type filter_enabled: bool
        """
        self._filter_enabled = filter_enabled

    @property
    def trust_list(self):
        """Gets the trust_list of this EquipmentOspfItem.

        白名单列表

        :return: The trust_list of this EquipmentOspfItem.
        :rtype: list[str]
        """
        return self._trust_list

    @trust_list.setter
    def trust_list(self, trust_list):
        """Sets the trust_list of this EquipmentOspfItem.

        白名单列表

        :param trust_list: The trust_list of this EquipmentOspfItem.
        :type trust_list: list[str]
        """
        self._trust_list = trust_list

    @property
    def block_list(self):
        """Gets the block_list of this EquipmentOspfItem.

        黑名单列表

        :return: The block_list of this EquipmentOspfItem.
        :rtype: list[str]
        """
        return self._block_list

    @block_list.setter
    def block_list(self, block_list):
        """Sets the block_list of this EquipmentOspfItem.

        黑名单列表

        :param block_list: The block_list of this EquipmentOspfItem.
        :type block_list: list[str]
        """
        self._block_list = block_list

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
        if not isinstance(other, EquipmentOspfItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
