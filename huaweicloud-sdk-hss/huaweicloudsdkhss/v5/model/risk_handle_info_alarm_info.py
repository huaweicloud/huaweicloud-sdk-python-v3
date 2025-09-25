# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RiskHandleInfoAlarmInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'alarm_num': 'int',
        'malware_file_num': 'int',
        'auto_block_num': 'int',
        'manual_handle_num': 'int',
        'auto_handle_num': 'int',
        'handle_rate': 'float',
        'beat_rate': 'float',
        'virus_kill_config_enable': 'bool',
        'user_open_virus_kill_rate': 'float',
        'alarm_notify_config_enable': 'bool',
        'user_open_alarm_notify_rate': 'float',
        'ransomware_event_num': 'int',
        'ransomware_event_host_list': 'list[str]'
    }

    attribute_map = {
        'alarm_num': 'alarm_num',
        'malware_file_num': 'malware_file_num',
        'auto_block_num': 'auto_block_num',
        'manual_handle_num': 'manual_handle_num',
        'auto_handle_num': 'auto_handle_num',
        'handle_rate': 'handle_rate',
        'beat_rate': 'beat_rate',
        'virus_kill_config_enable': 'virus_kill_config_enable',
        'user_open_virus_kill_rate': 'user_open_virus_kill_rate',
        'alarm_notify_config_enable': 'alarm_notify_config_enable',
        'user_open_alarm_notify_rate': 'user_open_alarm_notify_rate',
        'ransomware_event_num': 'ransomware_event_num',
        'ransomware_event_host_list': 'ransomware_event_host_list'
    }

    def __init__(self, alarm_num=None, malware_file_num=None, auto_block_num=None, manual_handle_num=None, auto_handle_num=None, handle_rate=None, beat_rate=None, virus_kill_config_enable=None, user_open_virus_kill_rate=None, alarm_notify_config_enable=None, user_open_alarm_notify_rate=None, ransomware_event_num=None, ransomware_event_host_list=None):
        r"""RiskHandleInfoAlarmInfo

        The model defined in huaweicloud sdk

        :param alarm_num: **参数解释**: 攻击、异常行为数 **取值范围**: 最小值0，最大值2147483647 
        :type alarm_num: int
        :param malware_file_num: **参数解释**: 病毒文件数 **取值范围**: 最小值0，最大值2147483647 
        :type malware_file_num: int
        :param auto_block_num: **参数解释**: 阻断的数量 **取值范围**: 最小值0，最大值2147483647 
        :type auto_block_num: int
        :param manual_handle_num: **参数解释**: 手工处置数量 **取值范围**: 最小值0，最大值2147483647 
        :type manual_handle_num: int
        :param auto_handle_num: **参数解释**: 自动处置数量 **取值范围**: 最小值0，最大值2147483647 
        :type auto_handle_num: int
        :param handle_rate: **参数解释**: 平均处置率 **取值范围**: 最小值0，最大值1 
        :type handle_rate: float
        :param beat_rate: **参数解释**: 平均处置率击败的用户率 **取值范围**: 最小值0，最大值1 
        :type beat_rate: float
        :param virus_kill_config_enable: **参数解释**: 是否开启隔离查杀 **取值范围**:  - true：是。  - false：否。 
        :type virus_kill_config_enable: bool
        :param user_open_virus_kill_rate: **参数解释**: 开启隔离查杀的用户率 **取值范围**: 最小值0，最大值1 
        :type user_open_virus_kill_rate: float
        :param alarm_notify_config_enable: **参数解释**: 是否开启告警通知 **取值范围**:  - true：是。  - false：否。 
        :type alarm_notify_config_enable: bool
        :param user_open_alarm_notify_rate: **参数解释**: 开启告警通知的用户率 **取值范围**: 最小值0，最大值1 
        :type user_open_alarm_notify_rate: float
        :param ransomware_event_num: **参数解释**: 勒索病毒攻击数量 **取值范围**: 最小值0，最大值2147483647 
        :type ransomware_event_num: int
        :param ransomware_event_host_list: **参数解释**: 存在勒索病毒攻击的主机列表 **取值范围**: 最小值0，最大值10000 
        :type ransomware_event_host_list: list[str]
        """
        
        

        self._alarm_num = None
        self._malware_file_num = None
        self._auto_block_num = None
        self._manual_handle_num = None
        self._auto_handle_num = None
        self._handle_rate = None
        self._beat_rate = None
        self._virus_kill_config_enable = None
        self._user_open_virus_kill_rate = None
        self._alarm_notify_config_enable = None
        self._user_open_alarm_notify_rate = None
        self._ransomware_event_num = None
        self._ransomware_event_host_list = None
        self.discriminator = None

        if alarm_num is not None:
            self.alarm_num = alarm_num
        if malware_file_num is not None:
            self.malware_file_num = malware_file_num
        if auto_block_num is not None:
            self.auto_block_num = auto_block_num
        if manual_handle_num is not None:
            self.manual_handle_num = manual_handle_num
        if auto_handle_num is not None:
            self.auto_handle_num = auto_handle_num
        if handle_rate is not None:
            self.handle_rate = handle_rate
        if beat_rate is not None:
            self.beat_rate = beat_rate
        if virus_kill_config_enable is not None:
            self.virus_kill_config_enable = virus_kill_config_enable
        if user_open_virus_kill_rate is not None:
            self.user_open_virus_kill_rate = user_open_virus_kill_rate
        if alarm_notify_config_enable is not None:
            self.alarm_notify_config_enable = alarm_notify_config_enable
        if user_open_alarm_notify_rate is not None:
            self.user_open_alarm_notify_rate = user_open_alarm_notify_rate
        if ransomware_event_num is not None:
            self.ransomware_event_num = ransomware_event_num
        if ransomware_event_host_list is not None:
            self.ransomware_event_host_list = ransomware_event_host_list

    @property
    def alarm_num(self):
        r"""Gets the alarm_num of this RiskHandleInfoAlarmInfo.

        **参数解释**: 攻击、异常行为数 **取值范围**: 最小值0，最大值2147483647 

        :return: The alarm_num of this RiskHandleInfoAlarmInfo.
        :rtype: int
        """
        return self._alarm_num

    @alarm_num.setter
    def alarm_num(self, alarm_num):
        r"""Sets the alarm_num of this RiskHandleInfoAlarmInfo.

        **参数解释**: 攻击、异常行为数 **取值范围**: 最小值0，最大值2147483647 

        :param alarm_num: The alarm_num of this RiskHandleInfoAlarmInfo.
        :type alarm_num: int
        """
        self._alarm_num = alarm_num

    @property
    def malware_file_num(self):
        r"""Gets the malware_file_num of this RiskHandleInfoAlarmInfo.

        **参数解释**: 病毒文件数 **取值范围**: 最小值0，最大值2147483647 

        :return: The malware_file_num of this RiskHandleInfoAlarmInfo.
        :rtype: int
        """
        return self._malware_file_num

    @malware_file_num.setter
    def malware_file_num(self, malware_file_num):
        r"""Sets the malware_file_num of this RiskHandleInfoAlarmInfo.

        **参数解释**: 病毒文件数 **取值范围**: 最小值0，最大值2147483647 

        :param malware_file_num: The malware_file_num of this RiskHandleInfoAlarmInfo.
        :type malware_file_num: int
        """
        self._malware_file_num = malware_file_num

    @property
    def auto_block_num(self):
        r"""Gets the auto_block_num of this RiskHandleInfoAlarmInfo.

        **参数解释**: 阻断的数量 **取值范围**: 最小值0，最大值2147483647 

        :return: The auto_block_num of this RiskHandleInfoAlarmInfo.
        :rtype: int
        """
        return self._auto_block_num

    @auto_block_num.setter
    def auto_block_num(self, auto_block_num):
        r"""Sets the auto_block_num of this RiskHandleInfoAlarmInfo.

        **参数解释**: 阻断的数量 **取值范围**: 最小值0，最大值2147483647 

        :param auto_block_num: The auto_block_num of this RiskHandleInfoAlarmInfo.
        :type auto_block_num: int
        """
        self._auto_block_num = auto_block_num

    @property
    def manual_handle_num(self):
        r"""Gets the manual_handle_num of this RiskHandleInfoAlarmInfo.

        **参数解释**: 手工处置数量 **取值范围**: 最小值0，最大值2147483647 

        :return: The manual_handle_num of this RiskHandleInfoAlarmInfo.
        :rtype: int
        """
        return self._manual_handle_num

    @manual_handle_num.setter
    def manual_handle_num(self, manual_handle_num):
        r"""Sets the manual_handle_num of this RiskHandleInfoAlarmInfo.

        **参数解释**: 手工处置数量 **取值范围**: 最小值0，最大值2147483647 

        :param manual_handle_num: The manual_handle_num of this RiskHandleInfoAlarmInfo.
        :type manual_handle_num: int
        """
        self._manual_handle_num = manual_handle_num

    @property
    def auto_handle_num(self):
        r"""Gets the auto_handle_num of this RiskHandleInfoAlarmInfo.

        **参数解释**: 自动处置数量 **取值范围**: 最小值0，最大值2147483647 

        :return: The auto_handle_num of this RiskHandleInfoAlarmInfo.
        :rtype: int
        """
        return self._auto_handle_num

    @auto_handle_num.setter
    def auto_handle_num(self, auto_handle_num):
        r"""Sets the auto_handle_num of this RiskHandleInfoAlarmInfo.

        **参数解释**: 自动处置数量 **取值范围**: 最小值0，最大值2147483647 

        :param auto_handle_num: The auto_handle_num of this RiskHandleInfoAlarmInfo.
        :type auto_handle_num: int
        """
        self._auto_handle_num = auto_handle_num

    @property
    def handle_rate(self):
        r"""Gets the handle_rate of this RiskHandleInfoAlarmInfo.

        **参数解释**: 平均处置率 **取值范围**: 最小值0，最大值1 

        :return: The handle_rate of this RiskHandleInfoAlarmInfo.
        :rtype: float
        """
        return self._handle_rate

    @handle_rate.setter
    def handle_rate(self, handle_rate):
        r"""Sets the handle_rate of this RiskHandleInfoAlarmInfo.

        **参数解释**: 平均处置率 **取值范围**: 最小值0，最大值1 

        :param handle_rate: The handle_rate of this RiskHandleInfoAlarmInfo.
        :type handle_rate: float
        """
        self._handle_rate = handle_rate

    @property
    def beat_rate(self):
        r"""Gets the beat_rate of this RiskHandleInfoAlarmInfo.

        **参数解释**: 平均处置率击败的用户率 **取值范围**: 最小值0，最大值1 

        :return: The beat_rate of this RiskHandleInfoAlarmInfo.
        :rtype: float
        """
        return self._beat_rate

    @beat_rate.setter
    def beat_rate(self, beat_rate):
        r"""Sets the beat_rate of this RiskHandleInfoAlarmInfo.

        **参数解释**: 平均处置率击败的用户率 **取值范围**: 最小值0，最大值1 

        :param beat_rate: The beat_rate of this RiskHandleInfoAlarmInfo.
        :type beat_rate: float
        """
        self._beat_rate = beat_rate

    @property
    def virus_kill_config_enable(self):
        r"""Gets the virus_kill_config_enable of this RiskHandleInfoAlarmInfo.

        **参数解释**: 是否开启隔离查杀 **取值范围**:  - true：是。  - false：否。 

        :return: The virus_kill_config_enable of this RiskHandleInfoAlarmInfo.
        :rtype: bool
        """
        return self._virus_kill_config_enable

    @virus_kill_config_enable.setter
    def virus_kill_config_enable(self, virus_kill_config_enable):
        r"""Sets the virus_kill_config_enable of this RiskHandleInfoAlarmInfo.

        **参数解释**: 是否开启隔离查杀 **取值范围**:  - true：是。  - false：否。 

        :param virus_kill_config_enable: The virus_kill_config_enable of this RiskHandleInfoAlarmInfo.
        :type virus_kill_config_enable: bool
        """
        self._virus_kill_config_enable = virus_kill_config_enable

    @property
    def user_open_virus_kill_rate(self):
        r"""Gets the user_open_virus_kill_rate of this RiskHandleInfoAlarmInfo.

        **参数解释**: 开启隔离查杀的用户率 **取值范围**: 最小值0，最大值1 

        :return: The user_open_virus_kill_rate of this RiskHandleInfoAlarmInfo.
        :rtype: float
        """
        return self._user_open_virus_kill_rate

    @user_open_virus_kill_rate.setter
    def user_open_virus_kill_rate(self, user_open_virus_kill_rate):
        r"""Sets the user_open_virus_kill_rate of this RiskHandleInfoAlarmInfo.

        **参数解释**: 开启隔离查杀的用户率 **取值范围**: 最小值0，最大值1 

        :param user_open_virus_kill_rate: The user_open_virus_kill_rate of this RiskHandleInfoAlarmInfo.
        :type user_open_virus_kill_rate: float
        """
        self._user_open_virus_kill_rate = user_open_virus_kill_rate

    @property
    def alarm_notify_config_enable(self):
        r"""Gets the alarm_notify_config_enable of this RiskHandleInfoAlarmInfo.

        **参数解释**: 是否开启告警通知 **取值范围**:  - true：是。  - false：否。 

        :return: The alarm_notify_config_enable of this RiskHandleInfoAlarmInfo.
        :rtype: bool
        """
        return self._alarm_notify_config_enable

    @alarm_notify_config_enable.setter
    def alarm_notify_config_enable(self, alarm_notify_config_enable):
        r"""Sets the alarm_notify_config_enable of this RiskHandleInfoAlarmInfo.

        **参数解释**: 是否开启告警通知 **取值范围**:  - true：是。  - false：否。 

        :param alarm_notify_config_enable: The alarm_notify_config_enable of this RiskHandleInfoAlarmInfo.
        :type alarm_notify_config_enable: bool
        """
        self._alarm_notify_config_enable = alarm_notify_config_enable

    @property
    def user_open_alarm_notify_rate(self):
        r"""Gets the user_open_alarm_notify_rate of this RiskHandleInfoAlarmInfo.

        **参数解释**: 开启告警通知的用户率 **取值范围**: 最小值0，最大值1 

        :return: The user_open_alarm_notify_rate of this RiskHandleInfoAlarmInfo.
        :rtype: float
        """
        return self._user_open_alarm_notify_rate

    @user_open_alarm_notify_rate.setter
    def user_open_alarm_notify_rate(self, user_open_alarm_notify_rate):
        r"""Sets the user_open_alarm_notify_rate of this RiskHandleInfoAlarmInfo.

        **参数解释**: 开启告警通知的用户率 **取值范围**: 最小值0，最大值1 

        :param user_open_alarm_notify_rate: The user_open_alarm_notify_rate of this RiskHandleInfoAlarmInfo.
        :type user_open_alarm_notify_rate: float
        """
        self._user_open_alarm_notify_rate = user_open_alarm_notify_rate

    @property
    def ransomware_event_num(self):
        r"""Gets the ransomware_event_num of this RiskHandleInfoAlarmInfo.

        **参数解释**: 勒索病毒攻击数量 **取值范围**: 最小值0，最大值2147483647 

        :return: The ransomware_event_num of this RiskHandleInfoAlarmInfo.
        :rtype: int
        """
        return self._ransomware_event_num

    @ransomware_event_num.setter
    def ransomware_event_num(self, ransomware_event_num):
        r"""Sets the ransomware_event_num of this RiskHandleInfoAlarmInfo.

        **参数解释**: 勒索病毒攻击数量 **取值范围**: 最小值0，最大值2147483647 

        :param ransomware_event_num: The ransomware_event_num of this RiskHandleInfoAlarmInfo.
        :type ransomware_event_num: int
        """
        self._ransomware_event_num = ransomware_event_num

    @property
    def ransomware_event_host_list(self):
        r"""Gets the ransomware_event_host_list of this RiskHandleInfoAlarmInfo.

        **参数解释**: 存在勒索病毒攻击的主机列表 **取值范围**: 最小值0，最大值10000 

        :return: The ransomware_event_host_list of this RiskHandleInfoAlarmInfo.
        :rtype: list[str]
        """
        return self._ransomware_event_host_list

    @ransomware_event_host_list.setter
    def ransomware_event_host_list(self, ransomware_event_host_list):
        r"""Sets the ransomware_event_host_list of this RiskHandleInfoAlarmInfo.

        **参数解释**: 存在勒索病毒攻击的主机列表 **取值范围**: 最小值0，最大值10000 

        :param ransomware_event_host_list: The ransomware_event_host_list of this RiskHandleInfoAlarmInfo.
        :type ransomware_event_host_list: list[str]
        """
        self._ransomware_event_host_list = ransomware_event_host_list

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
        if not isinstance(other, RiskHandleInfoAlarmInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
