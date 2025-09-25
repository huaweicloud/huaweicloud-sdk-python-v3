# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProtectInfoConfigInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'un_upgrade_agent_host_num': 'int',
        'auto_upgrade_agent_enable': 'bool',
        'user_open_auto_upgrade_agent_rate': 'float',
        'un_open_ransomware_policy_host_num': 'int',
        'to_be_optimized_ransomware_policy_host_num': 'int',
        'user_open_ransomware_backup_rate': 'float',
        'un_open_two_factor_login_host_num': 'int',
        'user_open_two_factor_login_rate': 'float',
        'un_virus_kill_host_num': 'int',
        'virus_kill_host_num': 'int',
        'malware_collect_enable': 'bool',
        'user_open_malware_collect_rate': 'float',
        'container_image_scan_freq': 'float',
        'container_image_scan_freq_beat_rate': 'float',
        'need_open_config_num': 'int',
        'container_image_scan_total_num': 'int'
    }

    attribute_map = {
        'un_upgrade_agent_host_num': 'un_upgrade_agent_host_num',
        'auto_upgrade_agent_enable': 'auto_upgrade_agent_enable',
        'user_open_auto_upgrade_agent_rate': 'user_open_auto_upgrade_agent_rate',
        'un_open_ransomware_policy_host_num': 'un_open_ransomware_policy_host_num',
        'to_be_optimized_ransomware_policy_host_num': 'to_be_optimized_ransomware_policy_host_num',
        'user_open_ransomware_backup_rate': 'user_open_ransomware_backup_rate',
        'un_open_two_factor_login_host_num': 'un_open_two_factor_login_host_num',
        'user_open_two_factor_login_rate': 'user_open_two_factor_login_rate',
        'un_virus_kill_host_num': 'un_virus_kill_host_num',
        'virus_kill_host_num': 'virus_kill_host_num',
        'malware_collect_enable': 'malware_collect_enable',
        'user_open_malware_collect_rate': 'user_open_malware_collect_rate',
        'container_image_scan_freq': 'container_image_scan_freq',
        'container_image_scan_freq_beat_rate': 'container_image_scan_freq_beat_rate',
        'need_open_config_num': 'need_open_config_num',
        'container_image_scan_total_num': 'container_image_scan_total_num'
    }

    def __init__(self, un_upgrade_agent_host_num=None, auto_upgrade_agent_enable=None, user_open_auto_upgrade_agent_rate=None, un_open_ransomware_policy_host_num=None, to_be_optimized_ransomware_policy_host_num=None, user_open_ransomware_backup_rate=None, un_open_two_factor_login_host_num=None, user_open_two_factor_login_rate=None, un_virus_kill_host_num=None, virus_kill_host_num=None, malware_collect_enable=None, user_open_malware_collect_rate=None, container_image_scan_freq=None, container_image_scan_freq_beat_rate=None, need_open_config_num=None, container_image_scan_total_num=None):
        r"""ProtectInfoConfigInfo

        The model defined in huaweicloud sdk

        :param un_upgrade_agent_host_num: **参数解释**: 未升级agent的主机数 **取值范围**: 最小值0，最大值2147483647 
        :type un_upgrade_agent_host_num: int
        :param auto_upgrade_agent_enable: **参数解释**: 是否开启自动升级 **取值范围**:   - true：是。   - false：否。 
        :type auto_upgrade_agent_enable: bool
        :param user_open_auto_upgrade_agent_rate: **参数解释**: 开启自动升级的用户率 **取值范围**: 最小值0，最大值1 
        :type user_open_auto_upgrade_agent_rate: float
        :param un_open_ransomware_policy_host_num: **参数解释**: 未开启勒索策略的主机数 **取值范围**: 最小值0，最大值2147483647 
        :type un_open_ransomware_policy_host_num: int
        :param to_be_optimized_ransomware_policy_host_num: **参数解释**: 未待开启（待优化）勒索病毒防护的主机数 **取值范围**: 最小值0，最大值2147483647 
        :type to_be_optimized_ransomware_policy_host_num: int
        :param user_open_ransomware_backup_rate: **参数解释**: 开启勒索备份的用户率 **取值范围**: 最小值0，最大值1 
        :type user_open_ransomware_backup_rate: float
        :param un_open_two_factor_login_host_num: **参数解释**: 未开启双因子的主机数 **取值范围**: 最小值0，最大值2147483647 
        :type un_open_two_factor_login_host_num: int
        :param user_open_two_factor_login_rate: **参数解释**: 开启双因子的用户率 **取值范围**: 最小值0，最大值1 
        :type user_open_two_factor_login_rate: float
        :param un_virus_kill_host_num: **参数解释**: 未执行病毒查杀的主机数 **取值范围**: 最小值0，最大值2147483647 
        :type un_virus_kill_host_num: int
        :param virus_kill_host_num: **参数解释**: 执行过病毒查杀的主机数 **取值范围**: 最小值0，最大值2147483647 
        :type virus_kill_host_num: int
        :param malware_collect_enable: **参数解释**: 是否开启云查 **取值范围**:   - true：是。   - false：否。 
        :type malware_collect_enable: bool
        :param user_open_malware_collect_rate: **参数解释**: 开启云查的用户率 **取值范围**: 最小值0，最大值1 
        :type user_open_malware_collect_rate: float
        :param container_image_scan_freq: **参数解释**: 容器镜像扫描频率 **取值范围**: 最小值0，最大值128 
        :type container_image_scan_freq: float
        :param container_image_scan_freq_beat_rate: **参数解释**: 容器镜像扫描频率击败的用户率 **取值范围**: 最小值0，最大值1 
        :type container_image_scan_freq_beat_rate: float
        :param need_open_config_num: **参数解释**: 用户开启的配置数量 **取值范围**: 最小值0，最大值2147483647 
        :type need_open_config_num: int
        :param container_image_scan_total_num: **参数解释**: 扫描的镜像数 **取值范围**: 最小值0，最大值2147483647 
        :type container_image_scan_total_num: int
        """
        
        

        self._un_upgrade_agent_host_num = None
        self._auto_upgrade_agent_enable = None
        self._user_open_auto_upgrade_agent_rate = None
        self._un_open_ransomware_policy_host_num = None
        self._to_be_optimized_ransomware_policy_host_num = None
        self._user_open_ransomware_backup_rate = None
        self._un_open_two_factor_login_host_num = None
        self._user_open_two_factor_login_rate = None
        self._un_virus_kill_host_num = None
        self._virus_kill_host_num = None
        self._malware_collect_enable = None
        self._user_open_malware_collect_rate = None
        self._container_image_scan_freq = None
        self._container_image_scan_freq_beat_rate = None
        self._need_open_config_num = None
        self._container_image_scan_total_num = None
        self.discriminator = None

        if un_upgrade_agent_host_num is not None:
            self.un_upgrade_agent_host_num = un_upgrade_agent_host_num
        if auto_upgrade_agent_enable is not None:
            self.auto_upgrade_agent_enable = auto_upgrade_agent_enable
        if user_open_auto_upgrade_agent_rate is not None:
            self.user_open_auto_upgrade_agent_rate = user_open_auto_upgrade_agent_rate
        if un_open_ransomware_policy_host_num is not None:
            self.un_open_ransomware_policy_host_num = un_open_ransomware_policy_host_num
        if to_be_optimized_ransomware_policy_host_num is not None:
            self.to_be_optimized_ransomware_policy_host_num = to_be_optimized_ransomware_policy_host_num
        if user_open_ransomware_backup_rate is not None:
            self.user_open_ransomware_backup_rate = user_open_ransomware_backup_rate
        if un_open_two_factor_login_host_num is not None:
            self.un_open_two_factor_login_host_num = un_open_two_factor_login_host_num
        if user_open_two_factor_login_rate is not None:
            self.user_open_two_factor_login_rate = user_open_two_factor_login_rate
        if un_virus_kill_host_num is not None:
            self.un_virus_kill_host_num = un_virus_kill_host_num
        if virus_kill_host_num is not None:
            self.virus_kill_host_num = virus_kill_host_num
        if malware_collect_enable is not None:
            self.malware_collect_enable = malware_collect_enable
        if user_open_malware_collect_rate is not None:
            self.user_open_malware_collect_rate = user_open_malware_collect_rate
        if container_image_scan_freq is not None:
            self.container_image_scan_freq = container_image_scan_freq
        if container_image_scan_freq_beat_rate is not None:
            self.container_image_scan_freq_beat_rate = container_image_scan_freq_beat_rate
        if need_open_config_num is not None:
            self.need_open_config_num = need_open_config_num
        if container_image_scan_total_num is not None:
            self.container_image_scan_total_num = container_image_scan_total_num

    @property
    def un_upgrade_agent_host_num(self):
        r"""Gets the un_upgrade_agent_host_num of this ProtectInfoConfigInfo.

        **参数解释**: 未升级agent的主机数 **取值范围**: 最小值0，最大值2147483647 

        :return: The un_upgrade_agent_host_num of this ProtectInfoConfigInfo.
        :rtype: int
        """
        return self._un_upgrade_agent_host_num

    @un_upgrade_agent_host_num.setter
    def un_upgrade_agent_host_num(self, un_upgrade_agent_host_num):
        r"""Sets the un_upgrade_agent_host_num of this ProtectInfoConfigInfo.

        **参数解释**: 未升级agent的主机数 **取值范围**: 最小值0，最大值2147483647 

        :param un_upgrade_agent_host_num: The un_upgrade_agent_host_num of this ProtectInfoConfigInfo.
        :type un_upgrade_agent_host_num: int
        """
        self._un_upgrade_agent_host_num = un_upgrade_agent_host_num

    @property
    def auto_upgrade_agent_enable(self):
        r"""Gets the auto_upgrade_agent_enable of this ProtectInfoConfigInfo.

        **参数解释**: 是否开启自动升级 **取值范围**:   - true：是。   - false：否。 

        :return: The auto_upgrade_agent_enable of this ProtectInfoConfigInfo.
        :rtype: bool
        """
        return self._auto_upgrade_agent_enable

    @auto_upgrade_agent_enable.setter
    def auto_upgrade_agent_enable(self, auto_upgrade_agent_enable):
        r"""Sets the auto_upgrade_agent_enable of this ProtectInfoConfigInfo.

        **参数解释**: 是否开启自动升级 **取值范围**:   - true：是。   - false：否。 

        :param auto_upgrade_agent_enable: The auto_upgrade_agent_enable of this ProtectInfoConfigInfo.
        :type auto_upgrade_agent_enable: bool
        """
        self._auto_upgrade_agent_enable = auto_upgrade_agent_enable

    @property
    def user_open_auto_upgrade_agent_rate(self):
        r"""Gets the user_open_auto_upgrade_agent_rate of this ProtectInfoConfigInfo.

        **参数解释**: 开启自动升级的用户率 **取值范围**: 最小值0，最大值1 

        :return: The user_open_auto_upgrade_agent_rate of this ProtectInfoConfigInfo.
        :rtype: float
        """
        return self._user_open_auto_upgrade_agent_rate

    @user_open_auto_upgrade_agent_rate.setter
    def user_open_auto_upgrade_agent_rate(self, user_open_auto_upgrade_agent_rate):
        r"""Sets the user_open_auto_upgrade_agent_rate of this ProtectInfoConfigInfo.

        **参数解释**: 开启自动升级的用户率 **取值范围**: 最小值0，最大值1 

        :param user_open_auto_upgrade_agent_rate: The user_open_auto_upgrade_agent_rate of this ProtectInfoConfigInfo.
        :type user_open_auto_upgrade_agent_rate: float
        """
        self._user_open_auto_upgrade_agent_rate = user_open_auto_upgrade_agent_rate

    @property
    def un_open_ransomware_policy_host_num(self):
        r"""Gets the un_open_ransomware_policy_host_num of this ProtectInfoConfigInfo.

        **参数解释**: 未开启勒索策略的主机数 **取值范围**: 最小值0，最大值2147483647 

        :return: The un_open_ransomware_policy_host_num of this ProtectInfoConfigInfo.
        :rtype: int
        """
        return self._un_open_ransomware_policy_host_num

    @un_open_ransomware_policy_host_num.setter
    def un_open_ransomware_policy_host_num(self, un_open_ransomware_policy_host_num):
        r"""Sets the un_open_ransomware_policy_host_num of this ProtectInfoConfigInfo.

        **参数解释**: 未开启勒索策略的主机数 **取值范围**: 最小值0，最大值2147483647 

        :param un_open_ransomware_policy_host_num: The un_open_ransomware_policy_host_num of this ProtectInfoConfigInfo.
        :type un_open_ransomware_policy_host_num: int
        """
        self._un_open_ransomware_policy_host_num = un_open_ransomware_policy_host_num

    @property
    def to_be_optimized_ransomware_policy_host_num(self):
        r"""Gets the to_be_optimized_ransomware_policy_host_num of this ProtectInfoConfigInfo.

        **参数解释**: 未待开启（待优化）勒索病毒防护的主机数 **取值范围**: 最小值0，最大值2147483647 

        :return: The to_be_optimized_ransomware_policy_host_num of this ProtectInfoConfigInfo.
        :rtype: int
        """
        return self._to_be_optimized_ransomware_policy_host_num

    @to_be_optimized_ransomware_policy_host_num.setter
    def to_be_optimized_ransomware_policy_host_num(self, to_be_optimized_ransomware_policy_host_num):
        r"""Sets the to_be_optimized_ransomware_policy_host_num of this ProtectInfoConfigInfo.

        **参数解释**: 未待开启（待优化）勒索病毒防护的主机数 **取值范围**: 最小值0，最大值2147483647 

        :param to_be_optimized_ransomware_policy_host_num: The to_be_optimized_ransomware_policy_host_num of this ProtectInfoConfigInfo.
        :type to_be_optimized_ransomware_policy_host_num: int
        """
        self._to_be_optimized_ransomware_policy_host_num = to_be_optimized_ransomware_policy_host_num

    @property
    def user_open_ransomware_backup_rate(self):
        r"""Gets the user_open_ransomware_backup_rate of this ProtectInfoConfigInfo.

        **参数解释**: 开启勒索备份的用户率 **取值范围**: 最小值0，最大值1 

        :return: The user_open_ransomware_backup_rate of this ProtectInfoConfigInfo.
        :rtype: float
        """
        return self._user_open_ransomware_backup_rate

    @user_open_ransomware_backup_rate.setter
    def user_open_ransomware_backup_rate(self, user_open_ransomware_backup_rate):
        r"""Sets the user_open_ransomware_backup_rate of this ProtectInfoConfigInfo.

        **参数解释**: 开启勒索备份的用户率 **取值范围**: 最小值0，最大值1 

        :param user_open_ransomware_backup_rate: The user_open_ransomware_backup_rate of this ProtectInfoConfigInfo.
        :type user_open_ransomware_backup_rate: float
        """
        self._user_open_ransomware_backup_rate = user_open_ransomware_backup_rate

    @property
    def un_open_two_factor_login_host_num(self):
        r"""Gets the un_open_two_factor_login_host_num of this ProtectInfoConfigInfo.

        **参数解释**: 未开启双因子的主机数 **取值范围**: 最小值0，最大值2147483647 

        :return: The un_open_two_factor_login_host_num of this ProtectInfoConfigInfo.
        :rtype: int
        """
        return self._un_open_two_factor_login_host_num

    @un_open_two_factor_login_host_num.setter
    def un_open_two_factor_login_host_num(self, un_open_two_factor_login_host_num):
        r"""Sets the un_open_two_factor_login_host_num of this ProtectInfoConfigInfo.

        **参数解释**: 未开启双因子的主机数 **取值范围**: 最小值0，最大值2147483647 

        :param un_open_two_factor_login_host_num: The un_open_two_factor_login_host_num of this ProtectInfoConfigInfo.
        :type un_open_two_factor_login_host_num: int
        """
        self._un_open_two_factor_login_host_num = un_open_two_factor_login_host_num

    @property
    def user_open_two_factor_login_rate(self):
        r"""Gets the user_open_two_factor_login_rate of this ProtectInfoConfigInfo.

        **参数解释**: 开启双因子的用户率 **取值范围**: 最小值0，最大值1 

        :return: The user_open_two_factor_login_rate of this ProtectInfoConfigInfo.
        :rtype: float
        """
        return self._user_open_two_factor_login_rate

    @user_open_two_factor_login_rate.setter
    def user_open_two_factor_login_rate(self, user_open_two_factor_login_rate):
        r"""Sets the user_open_two_factor_login_rate of this ProtectInfoConfigInfo.

        **参数解释**: 开启双因子的用户率 **取值范围**: 最小值0，最大值1 

        :param user_open_two_factor_login_rate: The user_open_two_factor_login_rate of this ProtectInfoConfigInfo.
        :type user_open_two_factor_login_rate: float
        """
        self._user_open_two_factor_login_rate = user_open_two_factor_login_rate

    @property
    def un_virus_kill_host_num(self):
        r"""Gets the un_virus_kill_host_num of this ProtectInfoConfigInfo.

        **参数解释**: 未执行病毒查杀的主机数 **取值范围**: 最小值0，最大值2147483647 

        :return: The un_virus_kill_host_num of this ProtectInfoConfigInfo.
        :rtype: int
        """
        return self._un_virus_kill_host_num

    @un_virus_kill_host_num.setter
    def un_virus_kill_host_num(self, un_virus_kill_host_num):
        r"""Sets the un_virus_kill_host_num of this ProtectInfoConfigInfo.

        **参数解释**: 未执行病毒查杀的主机数 **取值范围**: 最小值0，最大值2147483647 

        :param un_virus_kill_host_num: The un_virus_kill_host_num of this ProtectInfoConfigInfo.
        :type un_virus_kill_host_num: int
        """
        self._un_virus_kill_host_num = un_virus_kill_host_num

    @property
    def virus_kill_host_num(self):
        r"""Gets the virus_kill_host_num of this ProtectInfoConfigInfo.

        **参数解释**: 执行过病毒查杀的主机数 **取值范围**: 最小值0，最大值2147483647 

        :return: The virus_kill_host_num of this ProtectInfoConfigInfo.
        :rtype: int
        """
        return self._virus_kill_host_num

    @virus_kill_host_num.setter
    def virus_kill_host_num(self, virus_kill_host_num):
        r"""Sets the virus_kill_host_num of this ProtectInfoConfigInfo.

        **参数解释**: 执行过病毒查杀的主机数 **取值范围**: 最小值0，最大值2147483647 

        :param virus_kill_host_num: The virus_kill_host_num of this ProtectInfoConfigInfo.
        :type virus_kill_host_num: int
        """
        self._virus_kill_host_num = virus_kill_host_num

    @property
    def malware_collect_enable(self):
        r"""Gets the malware_collect_enable of this ProtectInfoConfigInfo.

        **参数解释**: 是否开启云查 **取值范围**:   - true：是。   - false：否。 

        :return: The malware_collect_enable of this ProtectInfoConfigInfo.
        :rtype: bool
        """
        return self._malware_collect_enable

    @malware_collect_enable.setter
    def malware_collect_enable(self, malware_collect_enable):
        r"""Sets the malware_collect_enable of this ProtectInfoConfigInfo.

        **参数解释**: 是否开启云查 **取值范围**:   - true：是。   - false：否。 

        :param malware_collect_enable: The malware_collect_enable of this ProtectInfoConfigInfo.
        :type malware_collect_enable: bool
        """
        self._malware_collect_enable = malware_collect_enable

    @property
    def user_open_malware_collect_rate(self):
        r"""Gets the user_open_malware_collect_rate of this ProtectInfoConfigInfo.

        **参数解释**: 开启云查的用户率 **取值范围**: 最小值0，最大值1 

        :return: The user_open_malware_collect_rate of this ProtectInfoConfigInfo.
        :rtype: float
        """
        return self._user_open_malware_collect_rate

    @user_open_malware_collect_rate.setter
    def user_open_malware_collect_rate(self, user_open_malware_collect_rate):
        r"""Sets the user_open_malware_collect_rate of this ProtectInfoConfigInfo.

        **参数解释**: 开启云查的用户率 **取值范围**: 最小值0，最大值1 

        :param user_open_malware_collect_rate: The user_open_malware_collect_rate of this ProtectInfoConfigInfo.
        :type user_open_malware_collect_rate: float
        """
        self._user_open_malware_collect_rate = user_open_malware_collect_rate

    @property
    def container_image_scan_freq(self):
        r"""Gets the container_image_scan_freq of this ProtectInfoConfigInfo.

        **参数解释**: 容器镜像扫描频率 **取值范围**: 最小值0，最大值128 

        :return: The container_image_scan_freq of this ProtectInfoConfigInfo.
        :rtype: float
        """
        return self._container_image_scan_freq

    @container_image_scan_freq.setter
    def container_image_scan_freq(self, container_image_scan_freq):
        r"""Sets the container_image_scan_freq of this ProtectInfoConfigInfo.

        **参数解释**: 容器镜像扫描频率 **取值范围**: 最小值0，最大值128 

        :param container_image_scan_freq: The container_image_scan_freq of this ProtectInfoConfigInfo.
        :type container_image_scan_freq: float
        """
        self._container_image_scan_freq = container_image_scan_freq

    @property
    def container_image_scan_freq_beat_rate(self):
        r"""Gets the container_image_scan_freq_beat_rate of this ProtectInfoConfigInfo.

        **参数解释**: 容器镜像扫描频率击败的用户率 **取值范围**: 最小值0，最大值1 

        :return: The container_image_scan_freq_beat_rate of this ProtectInfoConfigInfo.
        :rtype: float
        """
        return self._container_image_scan_freq_beat_rate

    @container_image_scan_freq_beat_rate.setter
    def container_image_scan_freq_beat_rate(self, container_image_scan_freq_beat_rate):
        r"""Sets the container_image_scan_freq_beat_rate of this ProtectInfoConfigInfo.

        **参数解释**: 容器镜像扫描频率击败的用户率 **取值范围**: 最小值0，最大值1 

        :param container_image_scan_freq_beat_rate: The container_image_scan_freq_beat_rate of this ProtectInfoConfigInfo.
        :type container_image_scan_freq_beat_rate: float
        """
        self._container_image_scan_freq_beat_rate = container_image_scan_freq_beat_rate

    @property
    def need_open_config_num(self):
        r"""Gets the need_open_config_num of this ProtectInfoConfigInfo.

        **参数解释**: 用户开启的配置数量 **取值范围**: 最小值0，最大值2147483647 

        :return: The need_open_config_num of this ProtectInfoConfigInfo.
        :rtype: int
        """
        return self._need_open_config_num

    @need_open_config_num.setter
    def need_open_config_num(self, need_open_config_num):
        r"""Sets the need_open_config_num of this ProtectInfoConfigInfo.

        **参数解释**: 用户开启的配置数量 **取值范围**: 最小值0，最大值2147483647 

        :param need_open_config_num: The need_open_config_num of this ProtectInfoConfigInfo.
        :type need_open_config_num: int
        """
        self._need_open_config_num = need_open_config_num

    @property
    def container_image_scan_total_num(self):
        r"""Gets the container_image_scan_total_num of this ProtectInfoConfigInfo.

        **参数解释**: 扫描的镜像数 **取值范围**: 最小值0，最大值2147483647 

        :return: The container_image_scan_total_num of this ProtectInfoConfigInfo.
        :rtype: int
        """
        return self._container_image_scan_total_num

    @container_image_scan_total_num.setter
    def container_image_scan_total_num(self, container_image_scan_total_num):
        r"""Sets the container_image_scan_total_num of this ProtectInfoConfigInfo.

        **参数解释**: 扫描的镜像数 **取值范围**: 最小值0，最大值2147483647 

        :param container_image_scan_total_num: The container_image_scan_total_num of this ProtectInfoConfigInfo.
        :type container_image_scan_total_num: int
        """
        self._container_image_scan_total_num = container_image_scan_total_num

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
        if not isinstance(other, ProtectInfoConfigInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
