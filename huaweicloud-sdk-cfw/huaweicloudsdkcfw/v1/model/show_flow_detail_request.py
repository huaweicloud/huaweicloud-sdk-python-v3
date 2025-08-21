# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowFlowDetailRequest:

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
        'direction': 'str',
        'start_time': 'int',
        'end_time': 'int',
        'vgw_id': 'list[str]',
        'asset_type': 'str',
        'item': 'str',
        'value': 'str'
    }

    attribute_map = {
        'fw_instance_id': 'fw_instance_id',
        'range': 'range',
        'log_type': 'log_type',
        'direction': 'direction',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'vgw_id': 'vgw_id',
        'asset_type': 'asset_type',
        'item': 'item',
        'value': 'value'
    }

    def __init__(self, fw_instance_id=None, range=None, log_type=None, direction=None, start_time=None, end_time=None, vgw_id=None, asset_type=None, item=None, value=None):
        r"""ShowFlowDetailRequest

        The model defined in huaweicloud sdk

        :param fw_instance_id: **参数解释**： 防火墙ID，用户创建防火墙实例后产生的唯一ID，配置后可区分不同防火墙，可通过[防火墙ID获取方式](cfw_02_0028.xml)获取 **约束限制**： 不涉及 **取值范围**： 32位UUID **默认取值**： 不涉及
        :type fw_instance_id: str
        :param range: **参数解释**： 时间范围  **约束限制**： 不涉及 **取值范围**： 0为近一时 1近一天 2近七天   **默认取值**： 不涉及
        :type range: int
        :param log_type: **参数解释**： 日志类型 **约束限制**： 不涉及 **取值范围**： internet为南北向日志、nat为nat场景日志，vpc为东西向日志，vgw为vgw场景日志 **默认取值**： 不涉及
        :type log_type: str
        :param direction: **参数解释**： 会话方向 **约束限制**： 不涉及 **取值范围**： in2out为出云方向 out2in为入云方向 **默认取值**： 不涉及
        :type direction: str
        :param start_time: **参数解释**： 开始时间 **约束限制**： 不涉及 **取值范围**： 毫秒级时间戳 **默认取值**： 不涉及
        :type start_time: int
        :param end_time: **参数解释**： 结束时间 **约束限制**： 不涉及 **取值范围**： 毫秒级时间戳 **默认取值**： 不涉及
        :type end_time: int
        :param vgw_id: **参数解释**： VGW ID **约束限制**： 不涉及 **取值范围**： 32位UUID **默认取值**： 不涉及
        :type vgw_id: list[str]
        :param asset_type: **参数解释**： IP类型 **约束限制**： 不涉及 **取值范围**： public 公网IP private 私网IP open_port **默认取值**： 不涉及
        :type asset_type: str
        :param item: **参数解释**： 聚合类型 **约束限制**： 不涉及 **取值范围**： src_ip 源IP dst_ip 目的IP dst_port 目的端口 protocol　协议 dst_host　目的域名 app　应用 dst_region_name　目的地区 src_region_name　源地区 **默认取值**： 不涉及
        :type item: str
        :param value: **参数解释**： 统计对象 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及
        :type value: str
        """
        
        

        self._fw_instance_id = None
        self._range = None
        self._log_type = None
        self._direction = None
        self._start_time = None
        self._end_time = None
        self._vgw_id = None
        self._asset_type = None
        self._item = None
        self._value = None
        self.discriminator = None

        self.fw_instance_id = fw_instance_id
        if range is not None:
            self.range = range
        self.log_type = log_type
        if direction is not None:
            self.direction = direction
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if vgw_id is not None:
            self.vgw_id = vgw_id
        if asset_type is not None:
            self.asset_type = asset_type
        self.item = item
        self.value = value

    @property
    def fw_instance_id(self):
        r"""Gets the fw_instance_id of this ShowFlowDetailRequest.

        **参数解释**： 防火墙ID，用户创建防火墙实例后产生的唯一ID，配置后可区分不同防火墙，可通过[防火墙ID获取方式](cfw_02_0028.xml)获取 **约束限制**： 不涉及 **取值范围**： 32位UUID **默认取值**： 不涉及

        :return: The fw_instance_id of this ShowFlowDetailRequest.
        :rtype: str
        """
        return self._fw_instance_id

    @fw_instance_id.setter
    def fw_instance_id(self, fw_instance_id):
        r"""Sets the fw_instance_id of this ShowFlowDetailRequest.

        **参数解释**： 防火墙ID，用户创建防火墙实例后产生的唯一ID，配置后可区分不同防火墙，可通过[防火墙ID获取方式](cfw_02_0028.xml)获取 **约束限制**： 不涉及 **取值范围**： 32位UUID **默认取值**： 不涉及

        :param fw_instance_id: The fw_instance_id of this ShowFlowDetailRequest.
        :type fw_instance_id: str
        """
        self._fw_instance_id = fw_instance_id

    @property
    def range(self):
        r"""Gets the range of this ShowFlowDetailRequest.

        **参数解释**： 时间范围  **约束限制**： 不涉及 **取值范围**： 0为近一时 1近一天 2近七天   **默认取值**： 不涉及

        :return: The range of this ShowFlowDetailRequest.
        :rtype: int
        """
        return self._range

    @range.setter
    def range(self, range):
        r"""Sets the range of this ShowFlowDetailRequest.

        **参数解释**： 时间范围  **约束限制**： 不涉及 **取值范围**： 0为近一时 1近一天 2近七天   **默认取值**： 不涉及

        :param range: The range of this ShowFlowDetailRequest.
        :type range: int
        """
        self._range = range

    @property
    def log_type(self):
        r"""Gets the log_type of this ShowFlowDetailRequest.

        **参数解释**： 日志类型 **约束限制**： 不涉及 **取值范围**： internet为南北向日志、nat为nat场景日志，vpc为东西向日志，vgw为vgw场景日志 **默认取值**： 不涉及

        :return: The log_type of this ShowFlowDetailRequest.
        :rtype: str
        """
        return self._log_type

    @log_type.setter
    def log_type(self, log_type):
        r"""Sets the log_type of this ShowFlowDetailRequest.

        **参数解释**： 日志类型 **约束限制**： 不涉及 **取值范围**： internet为南北向日志、nat为nat场景日志，vpc为东西向日志，vgw为vgw场景日志 **默认取值**： 不涉及

        :param log_type: The log_type of this ShowFlowDetailRequest.
        :type log_type: str
        """
        self._log_type = log_type

    @property
    def direction(self):
        r"""Gets the direction of this ShowFlowDetailRequest.

        **参数解释**： 会话方向 **约束限制**： 不涉及 **取值范围**： in2out为出云方向 out2in为入云方向 **默认取值**： 不涉及

        :return: The direction of this ShowFlowDetailRequest.
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        r"""Sets the direction of this ShowFlowDetailRequest.

        **参数解释**： 会话方向 **约束限制**： 不涉及 **取值范围**： in2out为出云方向 out2in为入云方向 **默认取值**： 不涉及

        :param direction: The direction of this ShowFlowDetailRequest.
        :type direction: str
        """
        self._direction = direction

    @property
    def start_time(self):
        r"""Gets the start_time of this ShowFlowDetailRequest.

        **参数解释**： 开始时间 **约束限制**： 不涉及 **取值范围**： 毫秒级时间戳 **默认取值**： 不涉及

        :return: The start_time of this ShowFlowDetailRequest.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ShowFlowDetailRequest.

        **参数解释**： 开始时间 **约束限制**： 不涉及 **取值范围**： 毫秒级时间戳 **默认取值**： 不涉及

        :param start_time: The start_time of this ShowFlowDetailRequest.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ShowFlowDetailRequest.

        **参数解释**： 结束时间 **约束限制**： 不涉及 **取值范围**： 毫秒级时间戳 **默认取值**： 不涉及

        :return: The end_time of this ShowFlowDetailRequest.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ShowFlowDetailRequest.

        **参数解释**： 结束时间 **约束限制**： 不涉及 **取值范围**： 毫秒级时间戳 **默认取值**： 不涉及

        :param end_time: The end_time of this ShowFlowDetailRequest.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def vgw_id(self):
        r"""Gets the vgw_id of this ShowFlowDetailRequest.

        **参数解释**： VGW ID **约束限制**： 不涉及 **取值范围**： 32位UUID **默认取值**： 不涉及

        :return: The vgw_id of this ShowFlowDetailRequest.
        :rtype: list[str]
        """
        return self._vgw_id

    @vgw_id.setter
    def vgw_id(self, vgw_id):
        r"""Sets the vgw_id of this ShowFlowDetailRequest.

        **参数解释**： VGW ID **约束限制**： 不涉及 **取值范围**： 32位UUID **默认取值**： 不涉及

        :param vgw_id: The vgw_id of this ShowFlowDetailRequest.
        :type vgw_id: list[str]
        """
        self._vgw_id = vgw_id

    @property
    def asset_type(self):
        r"""Gets the asset_type of this ShowFlowDetailRequest.

        **参数解释**： IP类型 **约束限制**： 不涉及 **取值范围**： public 公网IP private 私网IP open_port **默认取值**： 不涉及

        :return: The asset_type of this ShowFlowDetailRequest.
        :rtype: str
        """
        return self._asset_type

    @asset_type.setter
    def asset_type(self, asset_type):
        r"""Sets the asset_type of this ShowFlowDetailRequest.

        **参数解释**： IP类型 **约束限制**： 不涉及 **取值范围**： public 公网IP private 私网IP open_port **默认取值**： 不涉及

        :param asset_type: The asset_type of this ShowFlowDetailRequest.
        :type asset_type: str
        """
        self._asset_type = asset_type

    @property
    def item(self):
        r"""Gets the item of this ShowFlowDetailRequest.

        **参数解释**： 聚合类型 **约束限制**： 不涉及 **取值范围**： src_ip 源IP dst_ip 目的IP dst_port 目的端口 protocol　协议 dst_host　目的域名 app　应用 dst_region_name　目的地区 src_region_name　源地区 **默认取值**： 不涉及

        :return: The item of this ShowFlowDetailRequest.
        :rtype: str
        """
        return self._item

    @item.setter
    def item(self, item):
        r"""Sets the item of this ShowFlowDetailRequest.

        **参数解释**： 聚合类型 **约束限制**： 不涉及 **取值范围**： src_ip 源IP dst_ip 目的IP dst_port 目的端口 protocol　协议 dst_host　目的域名 app　应用 dst_region_name　目的地区 src_region_name　源地区 **默认取值**： 不涉及

        :param item: The item of this ShowFlowDetailRequest.
        :type item: str
        """
        self._item = item

    @property
    def value(self):
        r"""Gets the value of this ShowFlowDetailRequest.

        **参数解释**： 统计对象 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :return: The value of this ShowFlowDetailRequest.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this ShowFlowDetailRequest.

        **参数解释**： 统计对象 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :param value: The value of this ShowFlowDetailRequest.
        :type value: str
        """
        self._value = value

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
        if not isinstance(other, ShowFlowDetailRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
