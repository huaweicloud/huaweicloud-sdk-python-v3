# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateTrafficMirrorSessionOption:

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
        'description': 'str',
        'traffic_mirror_filter_id': 'str',
        'traffic_mirror_target_id': 'str',
        'traffic_mirror_target_type': 'str',
        'virtual_network_id': 'int',
        'packet_length': 'int',
        'priority': 'int',
        'enabled': 'str',
        'type': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'traffic_mirror_filter_id': 'traffic_mirror_filter_id',
        'traffic_mirror_target_id': 'traffic_mirror_target_id',
        'traffic_mirror_target_type': 'traffic_mirror_target_type',
        'virtual_network_id': 'virtual_network_id',
        'packet_length': 'packet_length',
        'priority': 'priority',
        'enabled': 'enabled',
        'type': 'type'
    }

    def __init__(self, name=None, description=None, traffic_mirror_filter_id=None, traffic_mirror_target_id=None, traffic_mirror_target_type=None, virtual_network_id=None, packet_length=None, priority=None, enabled=None, type=None):
        """UpdateTrafficMirrorSessionOption

        The model defined in huaweicloud sdk

        :param name: 功能说明：流量镜像会话名称 取值范围：1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）
        :type name: str
        :param description: 功能说明：流量镜像会话的描述信息 取值范围：0-255个字符，不能包含“&lt;”和“&gt;”
        :type description: str
        :param traffic_mirror_filter_id: 功能说明：流量镜像筛选条件ID
        :type traffic_mirror_filter_id: str
        :param traffic_mirror_target_id: 功能说明：镜像目标ID
        :type traffic_mirror_target_id: str
        :param traffic_mirror_target_type: 功能说明：镜像目的类型 取值范围：     eni：弹性网卡     elb：私网弹性负载均衡
        :type traffic_mirror_target_type: str
        :param virtual_network_id: 功能说明：指定VNI，用于在镜像目的区分不同会话的镜像流量 取值范围：0~16777215
        :type virtual_network_id: int
        :param packet_length: 功能说明：最大传输单元MTU 取值范围：1~1460
        :type packet_length: int
        :param priority: 功能说明：会话优先级 取值范围：1~32766
        :type priority: int
        :param enabled: 功能说明：是否开启会话 取值范围：true、false
        :type enabled: str
        :param type: 功能说明：支持的镜像源类型 取值范围：     eni：弹性网卡
        :type type: str
        """
        
        

        self._name = None
        self._description = None
        self._traffic_mirror_filter_id = None
        self._traffic_mirror_target_id = None
        self._traffic_mirror_target_type = None
        self._virtual_network_id = None
        self._packet_length = None
        self._priority = None
        self._enabled = None
        self._type = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if traffic_mirror_filter_id is not None:
            self.traffic_mirror_filter_id = traffic_mirror_filter_id
        if traffic_mirror_target_id is not None:
            self.traffic_mirror_target_id = traffic_mirror_target_id
        if traffic_mirror_target_type is not None:
            self.traffic_mirror_target_type = traffic_mirror_target_type
        if virtual_network_id is not None:
            self.virtual_network_id = virtual_network_id
        if packet_length is not None:
            self.packet_length = packet_length
        if priority is not None:
            self.priority = priority
        if enabled is not None:
            self.enabled = enabled
        if type is not None:
            self.type = type

    @property
    def name(self):
        """Gets the name of this UpdateTrafficMirrorSessionOption.

        功能说明：流量镜像会话名称 取值范围：1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）

        :return: The name of this UpdateTrafficMirrorSessionOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateTrafficMirrorSessionOption.

        功能说明：流量镜像会话名称 取值范围：1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）

        :param name: The name of this UpdateTrafficMirrorSessionOption.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this UpdateTrafficMirrorSessionOption.

        功能说明：流量镜像会话的描述信息 取值范围：0-255个字符，不能包含“<”和“>”

        :return: The description of this UpdateTrafficMirrorSessionOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateTrafficMirrorSessionOption.

        功能说明：流量镜像会话的描述信息 取值范围：0-255个字符，不能包含“<”和“>”

        :param description: The description of this UpdateTrafficMirrorSessionOption.
        :type description: str
        """
        self._description = description

    @property
    def traffic_mirror_filter_id(self):
        """Gets the traffic_mirror_filter_id of this UpdateTrafficMirrorSessionOption.

        功能说明：流量镜像筛选条件ID

        :return: The traffic_mirror_filter_id of this UpdateTrafficMirrorSessionOption.
        :rtype: str
        """
        return self._traffic_mirror_filter_id

    @traffic_mirror_filter_id.setter
    def traffic_mirror_filter_id(self, traffic_mirror_filter_id):
        """Sets the traffic_mirror_filter_id of this UpdateTrafficMirrorSessionOption.

        功能说明：流量镜像筛选条件ID

        :param traffic_mirror_filter_id: The traffic_mirror_filter_id of this UpdateTrafficMirrorSessionOption.
        :type traffic_mirror_filter_id: str
        """
        self._traffic_mirror_filter_id = traffic_mirror_filter_id

    @property
    def traffic_mirror_target_id(self):
        """Gets the traffic_mirror_target_id of this UpdateTrafficMirrorSessionOption.

        功能说明：镜像目标ID

        :return: The traffic_mirror_target_id of this UpdateTrafficMirrorSessionOption.
        :rtype: str
        """
        return self._traffic_mirror_target_id

    @traffic_mirror_target_id.setter
    def traffic_mirror_target_id(self, traffic_mirror_target_id):
        """Sets the traffic_mirror_target_id of this UpdateTrafficMirrorSessionOption.

        功能说明：镜像目标ID

        :param traffic_mirror_target_id: The traffic_mirror_target_id of this UpdateTrafficMirrorSessionOption.
        :type traffic_mirror_target_id: str
        """
        self._traffic_mirror_target_id = traffic_mirror_target_id

    @property
    def traffic_mirror_target_type(self):
        """Gets the traffic_mirror_target_type of this UpdateTrafficMirrorSessionOption.

        功能说明：镜像目的类型 取值范围：     eni：弹性网卡     elb：私网弹性负载均衡

        :return: The traffic_mirror_target_type of this UpdateTrafficMirrorSessionOption.
        :rtype: str
        """
        return self._traffic_mirror_target_type

    @traffic_mirror_target_type.setter
    def traffic_mirror_target_type(self, traffic_mirror_target_type):
        """Sets the traffic_mirror_target_type of this UpdateTrafficMirrorSessionOption.

        功能说明：镜像目的类型 取值范围：     eni：弹性网卡     elb：私网弹性负载均衡

        :param traffic_mirror_target_type: The traffic_mirror_target_type of this UpdateTrafficMirrorSessionOption.
        :type traffic_mirror_target_type: str
        """
        self._traffic_mirror_target_type = traffic_mirror_target_type

    @property
    def virtual_network_id(self):
        """Gets the virtual_network_id of this UpdateTrafficMirrorSessionOption.

        功能说明：指定VNI，用于在镜像目的区分不同会话的镜像流量 取值范围：0~16777215

        :return: The virtual_network_id of this UpdateTrafficMirrorSessionOption.
        :rtype: int
        """
        return self._virtual_network_id

    @virtual_network_id.setter
    def virtual_network_id(self, virtual_network_id):
        """Sets the virtual_network_id of this UpdateTrafficMirrorSessionOption.

        功能说明：指定VNI，用于在镜像目的区分不同会话的镜像流量 取值范围：0~16777215

        :param virtual_network_id: The virtual_network_id of this UpdateTrafficMirrorSessionOption.
        :type virtual_network_id: int
        """
        self._virtual_network_id = virtual_network_id

    @property
    def packet_length(self):
        """Gets the packet_length of this UpdateTrafficMirrorSessionOption.

        功能说明：最大传输单元MTU 取值范围：1~1460

        :return: The packet_length of this UpdateTrafficMirrorSessionOption.
        :rtype: int
        """
        return self._packet_length

    @packet_length.setter
    def packet_length(self, packet_length):
        """Sets the packet_length of this UpdateTrafficMirrorSessionOption.

        功能说明：最大传输单元MTU 取值范围：1~1460

        :param packet_length: The packet_length of this UpdateTrafficMirrorSessionOption.
        :type packet_length: int
        """
        self._packet_length = packet_length

    @property
    def priority(self):
        """Gets the priority of this UpdateTrafficMirrorSessionOption.

        功能说明：会话优先级 取值范围：1~32766

        :return: The priority of this UpdateTrafficMirrorSessionOption.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this UpdateTrafficMirrorSessionOption.

        功能说明：会话优先级 取值范围：1~32766

        :param priority: The priority of this UpdateTrafficMirrorSessionOption.
        :type priority: int
        """
        self._priority = priority

    @property
    def enabled(self):
        """Gets the enabled of this UpdateTrafficMirrorSessionOption.

        功能说明：是否开启会话 取值范围：true、false

        :return: The enabled of this UpdateTrafficMirrorSessionOption.
        :rtype: str
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this UpdateTrafficMirrorSessionOption.

        功能说明：是否开启会话 取值范围：true、false

        :param enabled: The enabled of this UpdateTrafficMirrorSessionOption.
        :type enabled: str
        """
        self._enabled = enabled

    @property
    def type(self):
        """Gets the type of this UpdateTrafficMirrorSessionOption.

        功能说明：支持的镜像源类型 取值范围：     eni：弹性网卡

        :return: The type of this UpdateTrafficMirrorSessionOption.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this UpdateTrafficMirrorSessionOption.

        功能说明：支持的镜像源类型 取值范围：     eni：弹性网卡

        :param type: The type of this UpdateTrafficMirrorSessionOption.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, UpdateTrafficMirrorSessionOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
