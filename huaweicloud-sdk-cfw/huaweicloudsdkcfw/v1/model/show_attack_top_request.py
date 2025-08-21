# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAttackTopRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'fw_instance_id': 'str',
        'range': 'int',
        'log_type': 'str',
        'start_time': 'int',
        'end_time': 'int',
        'vgw_id': 'list[str]',
        'action': 'int',
        'item': 'list[str]',
        'size': 'int'
    }

    attribute_map = {
        'fw_instance_id': 'fw_instance_id',
        'range': 'range',
        'log_type': 'log_type',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'vgw_id': 'vgw_id',
        'action': 'action',
        'item': 'item',
        'size': 'size'
    }

    def __init__(self, fw_instance_id=None, range=None, log_type=None, start_time=None, end_time=None, vgw_id=None, action=None, item=None, size=None):
        r"""ShowAttackTopRequest

        The model defined in huaweicloud sdk

        :param fw_instance_id: **参数解释**： 防火墙ID，用户创建防火墙实例后产生的唯一ID，配置后可区分不同防火墙，可通过[防火墙ID获取方式](cfw_02_0028.xml)获取 **约束限制**： 不涉及 **取值范围**： 32位UUID **默认取值**： 不涉及
        :type fw_instance_id: str
        :param range: **参数解释**： 时间范围  **约束限制**： 不涉及 **取值范围**： 0为近一时 1近一天 2近七天   **默认取值**： 不涉及
        :type range: int
        :param log_type: **参数解释**： 日志类型 **约束限制**： 不涉及 **取值范围**： internet为南北向日志、nat为nat场景日志，vpc为东西向日志，vgw为vgw场景日志 **默认取值**： 不涉及
        :type log_type: str
        :param start_time: **参数解释**： 开始时间 **约束限制**： 不涉及 **取值范围**： 毫秒级时间戳 **默认取值**： 不涉及
        :type start_time: int
        :param end_time: **参数解释**： 结束时间 **约束限制**： 不涉及 **取值范围**： 毫秒级时间戳 **默认取值**： 不涉及
        :type end_time: int
        :param vgw_id: **参数解释**： VGW ID **约束限制**： 不涉及 **取值范围**： 32位UUID **默认取值**： 不涉及
        :type vgw_id: list[str]
        :param action: **参数解释**： 动作 **约束限制**： 不涉及 **取值范围**： 0 全部 1 拦截 **默认取值**： 不涉及
        :type action: int
        :param item: **参数解释**： 聚合类型 **约束限制**： 不涉及 **取值范围**： src_region_id TOP外部攻击来源地区 attack_type 攻击类型 in_src_ip TOP内部攻击来源IP out_src_ip TOP外部攻击来源IP dst_port TOP被攻击端口 dst_ip TOP攻击目的IP attack_rule TOP攻击规则 src_ip TOP攻击来源IP level TOP威胁等级 **默认取值**： 不涉及
        :type item: list[str]
        :param size: **参数解释**： 聚合条数 **约束限制**： 不涉及 **取值范围**： 0到10条 **默认取值**： 5
        :type size: int
        """
        
        

        self._fw_instance_id = None
        self._range = None
        self._log_type = None
        self._start_time = None
        self._end_time = None
        self._vgw_id = None
        self._action = None
        self._item = None
        self._size = None
        self.discriminator = None

        self.fw_instance_id = fw_instance_id
        if range is not None:
            self.range = range
        self.log_type = log_type
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if vgw_id is not None:
            self.vgw_id = vgw_id
        self.action = action
        self.item = item
        if size is not None:
            self.size = size

    @property
    def fw_instance_id(self):
        r"""Gets the fw_instance_id of this ShowAttackTopRequest.

        **参数解释**： 防火墙ID，用户创建防火墙实例后产生的唯一ID，配置后可区分不同防火墙，可通过[防火墙ID获取方式](cfw_02_0028.xml)获取 **约束限制**： 不涉及 **取值范围**： 32位UUID **默认取值**： 不涉及

        :return: The fw_instance_id of this ShowAttackTopRequest.
        :rtype: str
        """
        return self._fw_instance_id

    @fw_instance_id.setter
    def fw_instance_id(self, fw_instance_id):
        r"""Sets the fw_instance_id of this ShowAttackTopRequest.

        **参数解释**： 防火墙ID，用户创建防火墙实例后产生的唯一ID，配置后可区分不同防火墙，可通过[防火墙ID获取方式](cfw_02_0028.xml)获取 **约束限制**： 不涉及 **取值范围**： 32位UUID **默认取值**： 不涉及

        :param fw_instance_id: The fw_instance_id of this ShowAttackTopRequest.
        :type fw_instance_id: str
        """
        self._fw_instance_id = fw_instance_id

    @property
    def range(self):
        r"""Gets the range of this ShowAttackTopRequest.

        **参数解释**： 时间范围  **约束限制**： 不涉及 **取值范围**： 0为近一时 1近一天 2近七天   **默认取值**： 不涉及

        :return: The range of this ShowAttackTopRequest.
        :rtype: int
        """
        return self._range

    @range.setter
    def range(self, range):
        r"""Sets the range of this ShowAttackTopRequest.

        **参数解释**： 时间范围  **约束限制**： 不涉及 **取值范围**： 0为近一时 1近一天 2近七天   **默认取值**： 不涉及

        :param range: The range of this ShowAttackTopRequest.
        :type range: int
        """
        self._range = range

    @property
    def log_type(self):
        r"""Gets the log_type of this ShowAttackTopRequest.

        **参数解释**： 日志类型 **约束限制**： 不涉及 **取值范围**： internet为南北向日志、nat为nat场景日志，vpc为东西向日志，vgw为vgw场景日志 **默认取值**： 不涉及

        :return: The log_type of this ShowAttackTopRequest.
        :rtype: str
        """
        return self._log_type

    @log_type.setter
    def log_type(self, log_type):
        r"""Sets the log_type of this ShowAttackTopRequest.

        **参数解释**： 日志类型 **约束限制**： 不涉及 **取值范围**： internet为南北向日志、nat为nat场景日志，vpc为东西向日志，vgw为vgw场景日志 **默认取值**： 不涉及

        :param log_type: The log_type of this ShowAttackTopRequest.
        :type log_type: str
        """
        self._log_type = log_type

    @property
    def start_time(self):
        r"""Gets the start_time of this ShowAttackTopRequest.

        **参数解释**： 开始时间 **约束限制**： 不涉及 **取值范围**： 毫秒级时间戳 **默认取值**： 不涉及

        :return: The start_time of this ShowAttackTopRequest.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ShowAttackTopRequest.

        **参数解释**： 开始时间 **约束限制**： 不涉及 **取值范围**： 毫秒级时间戳 **默认取值**： 不涉及

        :param start_time: The start_time of this ShowAttackTopRequest.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ShowAttackTopRequest.

        **参数解释**： 结束时间 **约束限制**： 不涉及 **取值范围**： 毫秒级时间戳 **默认取值**： 不涉及

        :return: The end_time of this ShowAttackTopRequest.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ShowAttackTopRequest.

        **参数解释**： 结束时间 **约束限制**： 不涉及 **取值范围**： 毫秒级时间戳 **默认取值**： 不涉及

        :param end_time: The end_time of this ShowAttackTopRequest.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def vgw_id(self):
        r"""Gets the vgw_id of this ShowAttackTopRequest.

        **参数解释**： VGW ID **约束限制**： 不涉及 **取值范围**： 32位UUID **默认取值**： 不涉及

        :return: The vgw_id of this ShowAttackTopRequest.
        :rtype: list[str]
        """
        return self._vgw_id

    @vgw_id.setter
    def vgw_id(self, vgw_id):
        r"""Sets the vgw_id of this ShowAttackTopRequest.

        **参数解释**： VGW ID **约束限制**： 不涉及 **取值范围**： 32位UUID **默认取值**： 不涉及

        :param vgw_id: The vgw_id of this ShowAttackTopRequest.
        :type vgw_id: list[str]
        """
        self._vgw_id = vgw_id

    @property
    def action(self):
        r"""Gets the action of this ShowAttackTopRequest.

        **参数解释**： 动作 **约束限制**： 不涉及 **取值范围**： 0 全部 1 拦截 **默认取值**： 不涉及

        :return: The action of this ShowAttackTopRequest.
        :rtype: int
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this ShowAttackTopRequest.

        **参数解释**： 动作 **约束限制**： 不涉及 **取值范围**： 0 全部 1 拦截 **默认取值**： 不涉及

        :param action: The action of this ShowAttackTopRequest.
        :type action: int
        """
        self._action = action

    @property
    def item(self):
        r"""Gets the item of this ShowAttackTopRequest.

        **参数解释**： 聚合类型 **约束限制**： 不涉及 **取值范围**： src_region_id TOP外部攻击来源地区 attack_type 攻击类型 in_src_ip TOP内部攻击来源IP out_src_ip TOP外部攻击来源IP dst_port TOP被攻击端口 dst_ip TOP攻击目的IP attack_rule TOP攻击规则 src_ip TOP攻击来源IP level TOP威胁等级 **默认取值**： 不涉及

        :return: The item of this ShowAttackTopRequest.
        :rtype: list[str]
        """
        return self._item

    @item.setter
    def item(self, item):
        r"""Sets the item of this ShowAttackTopRequest.

        **参数解释**： 聚合类型 **约束限制**： 不涉及 **取值范围**： src_region_id TOP外部攻击来源地区 attack_type 攻击类型 in_src_ip TOP内部攻击来源IP out_src_ip TOP外部攻击来源IP dst_port TOP被攻击端口 dst_ip TOP攻击目的IP attack_rule TOP攻击规则 src_ip TOP攻击来源IP level TOP威胁等级 **默认取值**： 不涉及

        :param item: The item of this ShowAttackTopRequest.
        :type item: list[str]
        """
        self._item = item

    @property
    def size(self):
        r"""Gets the size of this ShowAttackTopRequest.

        **参数解释**： 聚合条数 **约束限制**： 不涉及 **取值范围**： 0到10条 **默认取值**： 5

        :return: The size of this ShowAttackTopRequest.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this ShowAttackTopRequest.

        **参数解释**： 聚合条数 **约束限制**： 不涉及 **取值范围**： 0到10条 **默认取值**： 5

        :param size: The size of this ShowAttackTopRequest.
        :type size: int
        """
        self._size = size

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
        if not isinstance(other, ShowAttackTopRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
