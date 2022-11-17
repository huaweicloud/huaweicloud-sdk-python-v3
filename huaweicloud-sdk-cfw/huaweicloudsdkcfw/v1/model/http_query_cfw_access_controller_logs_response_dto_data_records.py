# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HttpQueryCfwAccessControllerLogsResponseDTODataRecords:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'action': 'str',
        'rule_name': 'str',
        'rule_id': 'str',
        'hit_time': 'int',
        'log_id': 'str',
        'src_ip': 'str',
        'src_port': 'str',
        'dst_ip': 'str',
        'dst_port': 'str',
        'protocol': 'str',
        'app': 'str'
    }

    attribute_map = {
        'action': 'action',
        'rule_name': 'rule_name',
        'rule_id': 'rule_id',
        'hit_time': 'hit_time',
        'log_id': 'log_id',
        'src_ip': 'src_ip',
        'src_port': 'src_port',
        'dst_ip': 'dst_ip',
        'dst_port': 'dst_port',
        'protocol': 'protocol',
        'app': 'app'
    }

    def __init__(self, action=None, rule_name=None, rule_id=None, hit_time=None, log_id=None, src_ip=None, src_port=None, dst_ip=None, dst_port=None, protocol=None, app=None):
        """HttpQueryCfwAccessControllerLogsResponseDTODataRecords

        The model defined in huaweicloud sdk

        :param action: 动作0：permit,1：deny
        :type action: str
        :param rule_name: 规则名称
        :type rule_name: str
        :param rule_id: 规则ID
        :type rule_id: str
        :param hit_time: 命中时间
        :type hit_time: int
        :param log_id: 文档ID
        :type log_id: str
        :param src_ip: 源IP
        :type src_ip: str
        :param src_port: 源端口
        :type src_port: str
        :param dst_ip: 目的IP
        :type dst_ip: str
        :param dst_port: 目的端口
        :type dst_port: str
        :param protocol: 协议类型:TCP为6,UDP为17,ICMP为1,ICMPV6为58,ANY为-1,手动类型不为空，自动类型为空
        :type protocol: str
        :param app: 应用协议
        :type app: str
        """
        
        

        self._action = None
        self._rule_name = None
        self._rule_id = None
        self._hit_time = None
        self._log_id = None
        self._src_ip = None
        self._src_port = None
        self._dst_ip = None
        self._dst_port = None
        self._protocol = None
        self._app = None
        self.discriminator = None

        if action is not None:
            self.action = action
        if rule_name is not None:
            self.rule_name = rule_name
        if rule_id is not None:
            self.rule_id = rule_id
        if hit_time is not None:
            self.hit_time = hit_time
        if log_id is not None:
            self.log_id = log_id
        if src_ip is not None:
            self.src_ip = src_ip
        if src_port is not None:
            self.src_port = src_port
        if dst_ip is not None:
            self.dst_ip = dst_ip
        if dst_port is not None:
            self.dst_port = dst_port
        if protocol is not None:
            self.protocol = protocol
        if app is not None:
            self.app = app

    @property
    def action(self):
        """Gets the action of this HttpQueryCfwAccessControllerLogsResponseDTODataRecords.

        动作0：permit,1：deny

        :return: The action of this HttpQueryCfwAccessControllerLogsResponseDTODataRecords.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this HttpQueryCfwAccessControllerLogsResponseDTODataRecords.

        动作0：permit,1：deny

        :param action: The action of this HttpQueryCfwAccessControllerLogsResponseDTODataRecords.
        :type action: str
        """
        self._action = action

    @property
    def rule_name(self):
        """Gets the rule_name of this HttpQueryCfwAccessControllerLogsResponseDTODataRecords.

        规则名称

        :return: The rule_name of this HttpQueryCfwAccessControllerLogsResponseDTODataRecords.
        :rtype: str
        """
        return self._rule_name

    @rule_name.setter
    def rule_name(self, rule_name):
        """Sets the rule_name of this HttpQueryCfwAccessControllerLogsResponseDTODataRecords.

        规则名称

        :param rule_name: The rule_name of this HttpQueryCfwAccessControllerLogsResponseDTODataRecords.
        :type rule_name: str
        """
        self._rule_name = rule_name

    @property
    def rule_id(self):
        """Gets the rule_id of this HttpQueryCfwAccessControllerLogsResponseDTODataRecords.

        规则ID

        :return: The rule_id of this HttpQueryCfwAccessControllerLogsResponseDTODataRecords.
        :rtype: str
        """
        return self._rule_id

    @rule_id.setter
    def rule_id(self, rule_id):
        """Sets the rule_id of this HttpQueryCfwAccessControllerLogsResponseDTODataRecords.

        规则ID

        :param rule_id: The rule_id of this HttpQueryCfwAccessControllerLogsResponseDTODataRecords.
        :type rule_id: str
        """
        self._rule_id = rule_id

    @property
    def hit_time(self):
        """Gets the hit_time of this HttpQueryCfwAccessControllerLogsResponseDTODataRecords.

        命中时间

        :return: The hit_time of this HttpQueryCfwAccessControllerLogsResponseDTODataRecords.
        :rtype: int
        """
        return self._hit_time

    @hit_time.setter
    def hit_time(self, hit_time):
        """Sets the hit_time of this HttpQueryCfwAccessControllerLogsResponseDTODataRecords.

        命中时间

        :param hit_time: The hit_time of this HttpQueryCfwAccessControllerLogsResponseDTODataRecords.
        :type hit_time: int
        """
        self._hit_time = hit_time

    @property
    def log_id(self):
        """Gets the log_id of this HttpQueryCfwAccessControllerLogsResponseDTODataRecords.

        文档ID

        :return: The log_id of this HttpQueryCfwAccessControllerLogsResponseDTODataRecords.
        :rtype: str
        """
        return self._log_id

    @log_id.setter
    def log_id(self, log_id):
        """Sets the log_id of this HttpQueryCfwAccessControllerLogsResponseDTODataRecords.

        文档ID

        :param log_id: The log_id of this HttpQueryCfwAccessControllerLogsResponseDTODataRecords.
        :type log_id: str
        """
        self._log_id = log_id

    @property
    def src_ip(self):
        """Gets the src_ip of this HttpQueryCfwAccessControllerLogsResponseDTODataRecords.

        源IP

        :return: The src_ip of this HttpQueryCfwAccessControllerLogsResponseDTODataRecords.
        :rtype: str
        """
        return self._src_ip

    @src_ip.setter
    def src_ip(self, src_ip):
        """Sets the src_ip of this HttpQueryCfwAccessControllerLogsResponseDTODataRecords.

        源IP

        :param src_ip: The src_ip of this HttpQueryCfwAccessControllerLogsResponseDTODataRecords.
        :type src_ip: str
        """
        self._src_ip = src_ip

    @property
    def src_port(self):
        """Gets the src_port of this HttpQueryCfwAccessControllerLogsResponseDTODataRecords.

        源端口

        :return: The src_port of this HttpQueryCfwAccessControllerLogsResponseDTODataRecords.
        :rtype: str
        """
        return self._src_port

    @src_port.setter
    def src_port(self, src_port):
        """Sets the src_port of this HttpQueryCfwAccessControllerLogsResponseDTODataRecords.

        源端口

        :param src_port: The src_port of this HttpQueryCfwAccessControllerLogsResponseDTODataRecords.
        :type src_port: str
        """
        self._src_port = src_port

    @property
    def dst_ip(self):
        """Gets the dst_ip of this HttpQueryCfwAccessControllerLogsResponseDTODataRecords.

        目的IP

        :return: The dst_ip of this HttpQueryCfwAccessControllerLogsResponseDTODataRecords.
        :rtype: str
        """
        return self._dst_ip

    @dst_ip.setter
    def dst_ip(self, dst_ip):
        """Sets the dst_ip of this HttpQueryCfwAccessControllerLogsResponseDTODataRecords.

        目的IP

        :param dst_ip: The dst_ip of this HttpQueryCfwAccessControllerLogsResponseDTODataRecords.
        :type dst_ip: str
        """
        self._dst_ip = dst_ip

    @property
    def dst_port(self):
        """Gets the dst_port of this HttpQueryCfwAccessControllerLogsResponseDTODataRecords.

        目的端口

        :return: The dst_port of this HttpQueryCfwAccessControllerLogsResponseDTODataRecords.
        :rtype: str
        """
        return self._dst_port

    @dst_port.setter
    def dst_port(self, dst_port):
        """Sets the dst_port of this HttpQueryCfwAccessControllerLogsResponseDTODataRecords.

        目的端口

        :param dst_port: The dst_port of this HttpQueryCfwAccessControllerLogsResponseDTODataRecords.
        :type dst_port: str
        """
        self._dst_port = dst_port

    @property
    def protocol(self):
        """Gets the protocol of this HttpQueryCfwAccessControllerLogsResponseDTODataRecords.

        协议类型:TCP为6,UDP为17,ICMP为1,ICMPV6为58,ANY为-1,手动类型不为空，自动类型为空

        :return: The protocol of this HttpQueryCfwAccessControllerLogsResponseDTODataRecords.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this HttpQueryCfwAccessControllerLogsResponseDTODataRecords.

        协议类型:TCP为6,UDP为17,ICMP为1,ICMPV6为58,ANY为-1,手动类型不为空，自动类型为空

        :param protocol: The protocol of this HttpQueryCfwAccessControllerLogsResponseDTODataRecords.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def app(self):
        """Gets the app of this HttpQueryCfwAccessControllerLogsResponseDTODataRecords.

        应用协议

        :return: The app of this HttpQueryCfwAccessControllerLogsResponseDTODataRecords.
        :rtype: str
        """
        return self._app

    @app.setter
    def app(self, app):
        """Sets the app of this HttpQueryCfwAccessControllerLogsResponseDTODataRecords.

        应用协议

        :param app: The app of this HttpQueryCfwAccessControllerLogsResponseDTODataRecords.
        :type app: str
        """
        self._app = app

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
        if not isinstance(other, HttpQueryCfwAccessControllerLogsResponseDTODataRecords):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
