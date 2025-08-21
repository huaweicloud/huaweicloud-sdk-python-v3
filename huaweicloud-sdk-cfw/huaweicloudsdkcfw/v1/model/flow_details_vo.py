# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FlowDetailsVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'apps': 'list[ItemVO]',
        'associate_instance_type': 'str',
        'device_name': 'str',
        'item': 'str',
        'last_time': 'int',
        'ports': 'list[ItemVO]',
        'region': 'str',
        'request_byte': 'float',
        'response_byte': 'float',
        'sessions': 'int',
        'tags': 'str',
        'src_ip': 'list[ItemVO]',
        'dst_ip': 'list[ItemVO]',
        'protocol': 'str'
    }

    attribute_map = {
        'apps': 'apps',
        'associate_instance_type': 'associate_instance_type',
        'device_name': 'device_name',
        'item': 'item',
        'last_time': 'last_time',
        'ports': 'ports',
        'region': 'region',
        'request_byte': 'request_byte',
        'response_byte': 'response_byte',
        'sessions': 'sessions',
        'tags': 'tags',
        'src_ip': 'src_ip',
        'dst_ip': 'dst_ip',
        'protocol': 'protocol'
    }

    def __init__(self, apps=None, associate_instance_type=None, device_name=None, item=None, last_time=None, ports=None, region=None, request_byte=None, response_byte=None, sessions=None, tags=None, src_ip=None, dst_ip=None, protocol=None):
        r"""FlowDetailsVO

        The model defined in huaweicloud sdk

        :param apps: **参数解释**： 应用统计 **取值范围**： 不涉及
        :type apps: list[:class:`huaweicloudsdkcfw.v1.ItemVO`]
        :param associate_instance_type: **参数解释**： 关联资产类型 **取值范围**： 不涉及
        :type associate_instance_type: str
        :param device_name: **参数解释**： 关联资产名称 **取值范围**： 不涉及
        :type device_name: str
        :param item: **参数解释**： 聚合项 **取值范围**： 不涉及
        :type item: str
        :param last_time: **参数解释**： 最近访问时间 **取值范围**： 不涉及
        :type last_time: int
        :param ports: **参数解释**： 端口统计 **取值范围**： 不涉及
        :type ports: list[:class:`huaweicloudsdkcfw.v1.ItemVO`]
        :param region: **参数解释**： 地区 **取值范围**： 不涉及
        :type region: str
        :param request_byte: **参数解释**： 请求字节数 **取值范围**： 不涉及
        :type request_byte: float
        :param response_byte: **参数解释**： 响应字节数 **取值范围**： 不涉及
        :type response_byte: float
        :param sessions: **参数解释**： 会话数量 **取值范围**： 不涉及
        :type sessions: int
        :param tags: **参数解释**： 标签 **取值范围**： 不涉及
        :type tags: str
        :param src_ip: **参数解释**： 源IP **取值范围**： 不涉及
        :type src_ip: list[:class:`huaweicloudsdkcfw.v1.ItemVO`]
        :param dst_ip: **参数解释**： 目的IP **取值范围**： 不涉及
        :type dst_ip: list[:class:`huaweicloudsdkcfw.v1.ItemVO`]
        :param protocol: **参数解释**： 协议 **取值范围**： 不涉及
        :type protocol: str
        """
        
        

        self._apps = None
        self._associate_instance_type = None
        self._device_name = None
        self._item = None
        self._last_time = None
        self._ports = None
        self._region = None
        self._request_byte = None
        self._response_byte = None
        self._sessions = None
        self._tags = None
        self._src_ip = None
        self._dst_ip = None
        self._protocol = None
        self.discriminator = None

        if apps is not None:
            self.apps = apps
        if associate_instance_type is not None:
            self.associate_instance_type = associate_instance_type
        if device_name is not None:
            self.device_name = device_name
        if item is not None:
            self.item = item
        if last_time is not None:
            self.last_time = last_time
        if ports is not None:
            self.ports = ports
        if region is not None:
            self.region = region
        if request_byte is not None:
            self.request_byte = request_byte
        if response_byte is not None:
            self.response_byte = response_byte
        if sessions is not None:
            self.sessions = sessions
        if tags is not None:
            self.tags = tags
        if src_ip is not None:
            self.src_ip = src_ip
        if dst_ip is not None:
            self.dst_ip = dst_ip
        if protocol is not None:
            self.protocol = protocol

    @property
    def apps(self):
        r"""Gets the apps of this FlowDetailsVO.

        **参数解释**： 应用统计 **取值范围**： 不涉及

        :return: The apps of this FlowDetailsVO.
        :rtype: list[:class:`huaweicloudsdkcfw.v1.ItemVO`]
        """
        return self._apps

    @apps.setter
    def apps(self, apps):
        r"""Sets the apps of this FlowDetailsVO.

        **参数解释**： 应用统计 **取值范围**： 不涉及

        :param apps: The apps of this FlowDetailsVO.
        :type apps: list[:class:`huaweicloudsdkcfw.v1.ItemVO`]
        """
        self._apps = apps

    @property
    def associate_instance_type(self):
        r"""Gets the associate_instance_type of this FlowDetailsVO.

        **参数解释**： 关联资产类型 **取值范围**： 不涉及

        :return: The associate_instance_type of this FlowDetailsVO.
        :rtype: str
        """
        return self._associate_instance_type

    @associate_instance_type.setter
    def associate_instance_type(self, associate_instance_type):
        r"""Sets the associate_instance_type of this FlowDetailsVO.

        **参数解释**： 关联资产类型 **取值范围**： 不涉及

        :param associate_instance_type: The associate_instance_type of this FlowDetailsVO.
        :type associate_instance_type: str
        """
        self._associate_instance_type = associate_instance_type

    @property
    def device_name(self):
        r"""Gets the device_name of this FlowDetailsVO.

        **参数解释**： 关联资产名称 **取值范围**： 不涉及

        :return: The device_name of this FlowDetailsVO.
        :rtype: str
        """
        return self._device_name

    @device_name.setter
    def device_name(self, device_name):
        r"""Sets the device_name of this FlowDetailsVO.

        **参数解释**： 关联资产名称 **取值范围**： 不涉及

        :param device_name: The device_name of this FlowDetailsVO.
        :type device_name: str
        """
        self._device_name = device_name

    @property
    def item(self):
        r"""Gets the item of this FlowDetailsVO.

        **参数解释**： 聚合项 **取值范围**： 不涉及

        :return: The item of this FlowDetailsVO.
        :rtype: str
        """
        return self._item

    @item.setter
    def item(self, item):
        r"""Sets the item of this FlowDetailsVO.

        **参数解释**： 聚合项 **取值范围**： 不涉及

        :param item: The item of this FlowDetailsVO.
        :type item: str
        """
        self._item = item

    @property
    def last_time(self):
        r"""Gets the last_time of this FlowDetailsVO.

        **参数解释**： 最近访问时间 **取值范围**： 不涉及

        :return: The last_time of this FlowDetailsVO.
        :rtype: int
        """
        return self._last_time

    @last_time.setter
    def last_time(self, last_time):
        r"""Sets the last_time of this FlowDetailsVO.

        **参数解释**： 最近访问时间 **取值范围**： 不涉及

        :param last_time: The last_time of this FlowDetailsVO.
        :type last_time: int
        """
        self._last_time = last_time

    @property
    def ports(self):
        r"""Gets the ports of this FlowDetailsVO.

        **参数解释**： 端口统计 **取值范围**： 不涉及

        :return: The ports of this FlowDetailsVO.
        :rtype: list[:class:`huaweicloudsdkcfw.v1.ItemVO`]
        """
        return self._ports

    @ports.setter
    def ports(self, ports):
        r"""Sets the ports of this FlowDetailsVO.

        **参数解释**： 端口统计 **取值范围**： 不涉及

        :param ports: The ports of this FlowDetailsVO.
        :type ports: list[:class:`huaweicloudsdkcfw.v1.ItemVO`]
        """
        self._ports = ports

    @property
    def region(self):
        r"""Gets the region of this FlowDetailsVO.

        **参数解释**： 地区 **取值范围**： 不涉及

        :return: The region of this FlowDetailsVO.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this FlowDetailsVO.

        **参数解释**： 地区 **取值范围**： 不涉及

        :param region: The region of this FlowDetailsVO.
        :type region: str
        """
        self._region = region

    @property
    def request_byte(self):
        r"""Gets the request_byte of this FlowDetailsVO.

        **参数解释**： 请求字节数 **取值范围**： 不涉及

        :return: The request_byte of this FlowDetailsVO.
        :rtype: float
        """
        return self._request_byte

    @request_byte.setter
    def request_byte(self, request_byte):
        r"""Sets the request_byte of this FlowDetailsVO.

        **参数解释**： 请求字节数 **取值范围**： 不涉及

        :param request_byte: The request_byte of this FlowDetailsVO.
        :type request_byte: float
        """
        self._request_byte = request_byte

    @property
    def response_byte(self):
        r"""Gets the response_byte of this FlowDetailsVO.

        **参数解释**： 响应字节数 **取值范围**： 不涉及

        :return: The response_byte of this FlowDetailsVO.
        :rtype: float
        """
        return self._response_byte

    @response_byte.setter
    def response_byte(self, response_byte):
        r"""Sets the response_byte of this FlowDetailsVO.

        **参数解释**： 响应字节数 **取值范围**： 不涉及

        :param response_byte: The response_byte of this FlowDetailsVO.
        :type response_byte: float
        """
        self._response_byte = response_byte

    @property
    def sessions(self):
        r"""Gets the sessions of this FlowDetailsVO.

        **参数解释**： 会话数量 **取值范围**： 不涉及

        :return: The sessions of this FlowDetailsVO.
        :rtype: int
        """
        return self._sessions

    @sessions.setter
    def sessions(self, sessions):
        r"""Sets the sessions of this FlowDetailsVO.

        **参数解释**： 会话数量 **取值范围**： 不涉及

        :param sessions: The sessions of this FlowDetailsVO.
        :type sessions: int
        """
        self._sessions = sessions

    @property
    def tags(self):
        r"""Gets the tags of this FlowDetailsVO.

        **参数解释**： 标签 **取值范围**： 不涉及

        :return: The tags of this FlowDetailsVO.
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this FlowDetailsVO.

        **参数解释**： 标签 **取值范围**： 不涉及

        :param tags: The tags of this FlowDetailsVO.
        :type tags: str
        """
        self._tags = tags

    @property
    def src_ip(self):
        r"""Gets the src_ip of this FlowDetailsVO.

        **参数解释**： 源IP **取值范围**： 不涉及

        :return: The src_ip of this FlowDetailsVO.
        :rtype: list[:class:`huaweicloudsdkcfw.v1.ItemVO`]
        """
        return self._src_ip

    @src_ip.setter
    def src_ip(self, src_ip):
        r"""Sets the src_ip of this FlowDetailsVO.

        **参数解释**： 源IP **取值范围**： 不涉及

        :param src_ip: The src_ip of this FlowDetailsVO.
        :type src_ip: list[:class:`huaweicloudsdkcfw.v1.ItemVO`]
        """
        self._src_ip = src_ip

    @property
    def dst_ip(self):
        r"""Gets the dst_ip of this FlowDetailsVO.

        **参数解释**： 目的IP **取值范围**： 不涉及

        :return: The dst_ip of this FlowDetailsVO.
        :rtype: list[:class:`huaweicloudsdkcfw.v1.ItemVO`]
        """
        return self._dst_ip

    @dst_ip.setter
    def dst_ip(self, dst_ip):
        r"""Sets the dst_ip of this FlowDetailsVO.

        **参数解释**： 目的IP **取值范围**： 不涉及

        :param dst_ip: The dst_ip of this FlowDetailsVO.
        :type dst_ip: list[:class:`huaweicloudsdkcfw.v1.ItemVO`]
        """
        self._dst_ip = dst_ip

    @property
    def protocol(self):
        r"""Gets the protocol of this FlowDetailsVO.

        **参数解释**： 协议 **取值范围**： 不涉及

        :return: The protocol of this FlowDetailsVO.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        r"""Sets the protocol of this FlowDetailsVO.

        **参数解释**： 协议 **取值范围**： 不涉及

        :param protocol: The protocol of this FlowDetailsVO.
        :type protocol: str
        """
        self._protocol = protocol

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
        if not isinstance(other, FlowDetailsVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
