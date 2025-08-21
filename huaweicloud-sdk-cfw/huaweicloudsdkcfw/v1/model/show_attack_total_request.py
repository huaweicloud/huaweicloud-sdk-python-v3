# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAttackTotalRequest:

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
        'vgw_id': 'list[str]'
    }

    attribute_map = {
        'fw_instance_id': 'fw_instance_id',
        'range': 'range',
        'log_type': 'log_type',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'vgw_id': 'vgw_id'
    }

    def __init__(self, fw_instance_id=None, range=None, log_type=None, start_time=None, end_time=None, vgw_id=None):
        r"""ShowAttackTotalRequest

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
        """
        
        

        self._fw_instance_id = None
        self._range = None
        self._log_type = None
        self._start_time = None
        self._end_time = None
        self._vgw_id = None
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

    @property
    def fw_instance_id(self):
        r"""Gets the fw_instance_id of this ShowAttackTotalRequest.

        **参数解释**： 防火墙ID，用户创建防火墙实例后产生的唯一ID，配置后可区分不同防火墙，可通过[防火墙ID获取方式](cfw_02_0028.xml)获取 **约束限制**： 不涉及 **取值范围**： 32位UUID **默认取值**： 不涉及

        :return: The fw_instance_id of this ShowAttackTotalRequest.
        :rtype: str
        """
        return self._fw_instance_id

    @fw_instance_id.setter
    def fw_instance_id(self, fw_instance_id):
        r"""Sets the fw_instance_id of this ShowAttackTotalRequest.

        **参数解释**： 防火墙ID，用户创建防火墙实例后产生的唯一ID，配置后可区分不同防火墙，可通过[防火墙ID获取方式](cfw_02_0028.xml)获取 **约束限制**： 不涉及 **取值范围**： 32位UUID **默认取值**： 不涉及

        :param fw_instance_id: The fw_instance_id of this ShowAttackTotalRequest.
        :type fw_instance_id: str
        """
        self._fw_instance_id = fw_instance_id

    @property
    def range(self):
        r"""Gets the range of this ShowAttackTotalRequest.

        **参数解释**： 时间范围  **约束限制**： 不涉及 **取值范围**： 0为近一时 1近一天 2近七天   **默认取值**： 不涉及

        :return: The range of this ShowAttackTotalRequest.
        :rtype: int
        """
        return self._range

    @range.setter
    def range(self, range):
        r"""Sets the range of this ShowAttackTotalRequest.

        **参数解释**： 时间范围  **约束限制**： 不涉及 **取值范围**： 0为近一时 1近一天 2近七天   **默认取值**： 不涉及

        :param range: The range of this ShowAttackTotalRequest.
        :type range: int
        """
        self._range = range

    @property
    def log_type(self):
        r"""Gets the log_type of this ShowAttackTotalRequest.

        **参数解释**： 日志类型 **约束限制**： 不涉及 **取值范围**： internet为南北向日志、nat为nat场景日志，vpc为东西向日志，vgw为vgw场景日志 **默认取值**： 不涉及

        :return: The log_type of this ShowAttackTotalRequest.
        :rtype: str
        """
        return self._log_type

    @log_type.setter
    def log_type(self, log_type):
        r"""Sets the log_type of this ShowAttackTotalRequest.

        **参数解释**： 日志类型 **约束限制**： 不涉及 **取值范围**： internet为南北向日志、nat为nat场景日志，vpc为东西向日志，vgw为vgw场景日志 **默认取值**： 不涉及

        :param log_type: The log_type of this ShowAttackTotalRequest.
        :type log_type: str
        """
        self._log_type = log_type

    @property
    def start_time(self):
        r"""Gets the start_time of this ShowAttackTotalRequest.

        **参数解释**： 开始时间 **约束限制**： 不涉及 **取值范围**： 毫秒级时间戳 **默认取值**： 不涉及

        :return: The start_time of this ShowAttackTotalRequest.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ShowAttackTotalRequest.

        **参数解释**： 开始时间 **约束限制**： 不涉及 **取值范围**： 毫秒级时间戳 **默认取值**： 不涉及

        :param start_time: The start_time of this ShowAttackTotalRequest.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ShowAttackTotalRequest.

        **参数解释**： 结束时间 **约束限制**： 不涉及 **取值范围**： 毫秒级时间戳 **默认取值**： 不涉及

        :return: The end_time of this ShowAttackTotalRequest.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ShowAttackTotalRequest.

        **参数解释**： 结束时间 **约束限制**： 不涉及 **取值范围**： 毫秒级时间戳 **默认取值**： 不涉及

        :param end_time: The end_time of this ShowAttackTotalRequest.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def vgw_id(self):
        r"""Gets the vgw_id of this ShowAttackTotalRequest.

        **参数解释**： VGW ID **约束限制**： 不涉及 **取值范围**： 32位UUID **默认取值**： 不涉及

        :return: The vgw_id of this ShowAttackTotalRequest.
        :rtype: list[str]
        """
        return self._vgw_id

    @vgw_id.setter
    def vgw_id(self, vgw_id):
        r"""Sets the vgw_id of this ShowAttackTotalRequest.

        **参数解释**： VGW ID **约束限制**： 不涉及 **取值范围**： 32位UUID **默认取值**： 不涉及

        :param vgw_id: The vgw_id of this ShowAttackTotalRequest.
        :type vgw_id: list[str]
        """
        self._vgw_id = vgw_id

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
        if not isinstance(other, ShowAttackTotalRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
