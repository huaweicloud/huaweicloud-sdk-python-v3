# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowLogsCountRequest:

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
        'start_time': 'int',
        'end_time': 'int',
        'vgw_id': 'list[str]',
        'item': 'str'
    }

    attribute_map = {
        'fw_instance_id': 'fw_instance_id',
        'range': 'range',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'vgw_id': 'vgw_id',
        'item': 'item'
    }

    def __init__(self, fw_instance_id=None, range=None, start_time=None, end_time=None, vgw_id=None, item=None):
        r"""ShowLogsCountRequest

        The model defined in huaweicloud sdk

        :param fw_instance_id: **参数解释**： 防火墙ID，用户创建防火墙实例后产生的唯一ID，配置后可区分不同防火墙，可通过[防火墙ID获取方式](cfw_02_0028.xml)获取 **约束限制**： 不涉及 **取值范围**： 32位UUID **默认取值**： 不涉及
        :type fw_instance_id: str
        :param range: **参数解释**： 时间范围  **约束限制**： 不涉及 **取值范围**： 0为近一时 1近一天 2近七天   **默认取值**： 不涉及
        :type range: int
        :param start_time: **参数解释**： 开始时间 **约束限制**： 不涉及 **取值范围**： 毫秒级时间戳 **默认取值**： 不涉及
        :type start_time: int
        :param end_time: **参数解释**： 结束时间 **约束限制**： 不涉及 **取值范围**： 毫秒级时间戳 **默认取值**： 不涉及
        :type end_time: int
        :param vgw_id: **参数解释**： VGW ID **约束限制**： 不涉及 **取值范围**： 32位UUID **默认取值**： 不涉及
        :type vgw_id: list[str]
        :param item: **参数解释**： 聚合类型 **约束限制**： 不涉及 **取值范围**： risk_ip 访问风险IP数量 risk_host 访问风险域名数量  open_port 开放端口的数量 **默认取值**： 不涉及
        :type item: str
        """
        
        

        self._fw_instance_id = None
        self._range = None
        self._start_time = None
        self._end_time = None
        self._vgw_id = None
        self._item = None
        self.discriminator = None

        self.fw_instance_id = fw_instance_id
        if range is not None:
            self.range = range
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if vgw_id is not None:
            self.vgw_id = vgw_id
        self.item = item

    @property
    def fw_instance_id(self):
        r"""Gets the fw_instance_id of this ShowLogsCountRequest.

        **参数解释**： 防火墙ID，用户创建防火墙实例后产生的唯一ID，配置后可区分不同防火墙，可通过[防火墙ID获取方式](cfw_02_0028.xml)获取 **约束限制**： 不涉及 **取值范围**： 32位UUID **默认取值**： 不涉及

        :return: The fw_instance_id of this ShowLogsCountRequest.
        :rtype: str
        """
        return self._fw_instance_id

    @fw_instance_id.setter
    def fw_instance_id(self, fw_instance_id):
        r"""Sets the fw_instance_id of this ShowLogsCountRequest.

        **参数解释**： 防火墙ID，用户创建防火墙实例后产生的唯一ID，配置后可区分不同防火墙，可通过[防火墙ID获取方式](cfw_02_0028.xml)获取 **约束限制**： 不涉及 **取值范围**： 32位UUID **默认取值**： 不涉及

        :param fw_instance_id: The fw_instance_id of this ShowLogsCountRequest.
        :type fw_instance_id: str
        """
        self._fw_instance_id = fw_instance_id

    @property
    def range(self):
        r"""Gets the range of this ShowLogsCountRequest.

        **参数解释**： 时间范围  **约束限制**： 不涉及 **取值范围**： 0为近一时 1近一天 2近七天   **默认取值**： 不涉及

        :return: The range of this ShowLogsCountRequest.
        :rtype: int
        """
        return self._range

    @range.setter
    def range(self, range):
        r"""Sets the range of this ShowLogsCountRequest.

        **参数解释**： 时间范围  **约束限制**： 不涉及 **取值范围**： 0为近一时 1近一天 2近七天   **默认取值**： 不涉及

        :param range: The range of this ShowLogsCountRequest.
        :type range: int
        """
        self._range = range

    @property
    def start_time(self):
        r"""Gets the start_time of this ShowLogsCountRequest.

        **参数解释**： 开始时间 **约束限制**： 不涉及 **取值范围**： 毫秒级时间戳 **默认取值**： 不涉及

        :return: The start_time of this ShowLogsCountRequest.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ShowLogsCountRequest.

        **参数解释**： 开始时间 **约束限制**： 不涉及 **取值范围**： 毫秒级时间戳 **默认取值**： 不涉及

        :param start_time: The start_time of this ShowLogsCountRequest.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ShowLogsCountRequest.

        **参数解释**： 结束时间 **约束限制**： 不涉及 **取值范围**： 毫秒级时间戳 **默认取值**： 不涉及

        :return: The end_time of this ShowLogsCountRequest.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ShowLogsCountRequest.

        **参数解释**： 结束时间 **约束限制**： 不涉及 **取值范围**： 毫秒级时间戳 **默认取值**： 不涉及

        :param end_time: The end_time of this ShowLogsCountRequest.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def vgw_id(self):
        r"""Gets the vgw_id of this ShowLogsCountRequest.

        **参数解释**： VGW ID **约束限制**： 不涉及 **取值范围**： 32位UUID **默认取值**： 不涉及

        :return: The vgw_id of this ShowLogsCountRequest.
        :rtype: list[str]
        """
        return self._vgw_id

    @vgw_id.setter
    def vgw_id(self, vgw_id):
        r"""Sets the vgw_id of this ShowLogsCountRequest.

        **参数解释**： VGW ID **约束限制**： 不涉及 **取值范围**： 32位UUID **默认取值**： 不涉及

        :param vgw_id: The vgw_id of this ShowLogsCountRequest.
        :type vgw_id: list[str]
        """
        self._vgw_id = vgw_id

    @property
    def item(self):
        r"""Gets the item of this ShowLogsCountRequest.

        **参数解释**： 聚合类型 **约束限制**： 不涉及 **取值范围**： risk_ip 访问风险IP数量 risk_host 访问风险域名数量  open_port 开放端口的数量 **默认取值**： 不涉及

        :return: The item of this ShowLogsCountRequest.
        :rtype: str
        """
        return self._item

    @item.setter
    def item(self, item):
        r"""Sets the item of this ShowLogsCountRequest.

        **参数解释**： 聚合类型 **约束限制**： 不涉及 **取值范围**： risk_ip 访问风险IP数量 risk_host 访问风险域名数量  open_port 开放端口的数量 **默认取值**： 不涉及

        :param item: The item of this ShowLogsCountRequest.
        :type item: str
        """
        self._item = item

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
        if not isinstance(other, ShowLogsCountRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
