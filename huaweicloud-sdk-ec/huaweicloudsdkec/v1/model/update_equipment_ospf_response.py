# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateEquipmentOspfResponse(SdkResponse):

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
        'block_list': 'list[str]',
        'cloud_subnet_list': 'list[str]'
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
        'block_list': 'block_list',
        'cloud_subnet_list': 'cloud_subnet_list'
    }

    def __init__(self, ospf_enabled=None, area_id=None, post_to_cloud=None, hello_timer=None, router_id=None, interfaces=None, filter_enabled=None, trust_list=None, block_list=None, cloud_subnet_list=None):
        r"""UpdateEquipmentOspfResponse

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
        :param cloud_subnet_list: 上云子网列表
        :type cloud_subnet_list: list[str]
        """
        
        super(UpdateEquipmentOspfResponse, self).__init__()

        self._ospf_enabled = None
        self._area_id = None
        self._post_to_cloud = None
        self._hello_timer = None
        self._router_id = None
        self._interfaces = None
        self._filter_enabled = None
        self._trust_list = None
        self._block_list = None
        self._cloud_subnet_list = None
        self.discriminator = None

        if ospf_enabled is not None:
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
        if cloud_subnet_list is not None:
            self.cloud_subnet_list = cloud_subnet_list

    @property
    def ospf_enabled(self):
        r"""Gets the ospf_enabled of this UpdateEquipmentOspfResponse.

        是否启用OSPF

        :return: The ospf_enabled of this UpdateEquipmentOspfResponse.
        :rtype: bool
        """
        return self._ospf_enabled

    @ospf_enabled.setter
    def ospf_enabled(self, ospf_enabled):
        r"""Sets the ospf_enabled of this UpdateEquipmentOspfResponse.

        是否启用OSPF

        :param ospf_enabled: The ospf_enabled of this UpdateEquipmentOspfResponse.
        :type ospf_enabled: bool
        """
        self._ospf_enabled = ospf_enabled

    @property
    def area_id(self):
        r"""Gets the area_id of this UpdateEquipmentOspfResponse.

        区域标识

        :return: The area_id of this UpdateEquipmentOspfResponse.
        :rtype: int
        """
        return self._area_id

    @area_id.setter
    def area_id(self, area_id):
        r"""Sets the area_id of this UpdateEquipmentOspfResponse.

        区域标识

        :param area_id: The area_id of this UpdateEquipmentOspfResponse.
        :type area_id: int
        """
        self._area_id = area_id

    @property
    def post_to_cloud(self):
        r"""Gets the post_to_cloud of this UpdateEquipmentOspfResponse.

        发布到企业连接网络

        :return: The post_to_cloud of this UpdateEquipmentOspfResponse.
        :rtype: bool
        """
        return self._post_to_cloud

    @post_to_cloud.setter
    def post_to_cloud(self, post_to_cloud):
        r"""Sets the post_to_cloud of this UpdateEquipmentOspfResponse.

        发布到企业连接网络

        :param post_to_cloud: The post_to_cloud of this UpdateEquipmentOspfResponse.
        :type post_to_cloud: bool
        """
        self._post_to_cloud = post_to_cloud

    @property
    def hello_timer(self):
        r"""Gets the hello_timer of this UpdateEquipmentOspfResponse.

        发送Hello报文的时间间隔，单位是秒

        :return: The hello_timer of this UpdateEquipmentOspfResponse.
        :rtype: int
        """
        return self._hello_timer

    @hello_timer.setter
    def hello_timer(self, hello_timer):
        r"""Sets the hello_timer of this UpdateEquipmentOspfResponse.

        发送Hello报文的时间间隔，单位是秒

        :param hello_timer: The hello_timer of this UpdateEquipmentOspfResponse.
        :type hello_timer: int
        """
        self._hello_timer = hello_timer

    @property
    def router_id(self):
        r"""Gets the router_id of this UpdateEquipmentOspfResponse.

        点分十进制格式，OSPF协议使用全网唯一的Router ID

        :return: The router_id of this UpdateEquipmentOspfResponse.
        :rtype: str
        """
        return self._router_id

    @router_id.setter
    def router_id(self, router_id):
        r"""Sets the router_id of this UpdateEquipmentOspfResponse.

        点分十进制格式，OSPF协议使用全网唯一的Router ID

        :param router_id: The router_id of this UpdateEquipmentOspfResponse.
        :type router_id: str
        """
        self._router_id = router_id

    @property
    def interfaces(self):
        r"""Gets the interfaces of this UpdateEquipmentOspfResponse.

        启用OSPF协议的接口列表

        :return: The interfaces of this UpdateEquipmentOspfResponse.
        :rtype: list[str]
        """
        return self._interfaces

    @interfaces.setter
    def interfaces(self, interfaces):
        r"""Sets the interfaces of this UpdateEquipmentOspfResponse.

        启用OSPF协议的接口列表

        :param interfaces: The interfaces of this UpdateEquipmentOspfResponse.
        :type interfaces: list[str]
        """
        self._interfaces = interfaces

    @property
    def filter_enabled(self):
        r"""Gets the filter_enabled of this UpdateEquipmentOspfResponse.

        是否启用前缀过滤

        :return: The filter_enabled of this UpdateEquipmentOspfResponse.
        :rtype: bool
        """
        return self._filter_enabled

    @filter_enabled.setter
    def filter_enabled(self, filter_enabled):
        r"""Sets the filter_enabled of this UpdateEquipmentOspfResponse.

        是否启用前缀过滤

        :param filter_enabled: The filter_enabled of this UpdateEquipmentOspfResponse.
        :type filter_enabled: bool
        """
        self._filter_enabled = filter_enabled

    @property
    def trust_list(self):
        r"""Gets the trust_list of this UpdateEquipmentOspfResponse.

        白名单列表

        :return: The trust_list of this UpdateEquipmentOspfResponse.
        :rtype: list[str]
        """
        return self._trust_list

    @trust_list.setter
    def trust_list(self, trust_list):
        r"""Sets the trust_list of this UpdateEquipmentOspfResponse.

        白名单列表

        :param trust_list: The trust_list of this UpdateEquipmentOspfResponse.
        :type trust_list: list[str]
        """
        self._trust_list = trust_list

    @property
    def block_list(self):
        r"""Gets the block_list of this UpdateEquipmentOspfResponse.

        黑名单列表

        :return: The block_list of this UpdateEquipmentOspfResponse.
        :rtype: list[str]
        """
        return self._block_list

    @block_list.setter
    def block_list(self, block_list):
        r"""Sets the block_list of this UpdateEquipmentOspfResponse.

        黑名单列表

        :param block_list: The block_list of this UpdateEquipmentOspfResponse.
        :type block_list: list[str]
        """
        self._block_list = block_list

    @property
    def cloud_subnet_list(self):
        r"""Gets the cloud_subnet_list of this UpdateEquipmentOspfResponse.

        上云子网列表

        :return: The cloud_subnet_list of this UpdateEquipmentOspfResponse.
        :rtype: list[str]
        """
        return self._cloud_subnet_list

    @cloud_subnet_list.setter
    def cloud_subnet_list(self, cloud_subnet_list):
        r"""Sets the cloud_subnet_list of this UpdateEquipmentOspfResponse.

        上云子网列表

        :param cloud_subnet_list: The cloud_subnet_list of this UpdateEquipmentOspfResponse.
        :type cloud_subnet_list: list[str]
        """
        self._cloud_subnet_list = cloud_subnet_list

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
        if not isinstance(other, UpdateEquipmentOspfResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
