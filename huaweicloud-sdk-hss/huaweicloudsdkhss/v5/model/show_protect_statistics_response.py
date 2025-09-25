# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowProtectStatisticsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vul_library_update_time': 'int',
        'protect_days': 'int',
        'threat_library_update_time': 'int',
        'vul_detected_total_num': 'int',
        'baseline_detected_total_num': 'int',
        'finger_scan_total_num': 'int',
        'alarm_detected_total_num': 'int',
        'ransomware_alarm_detected_total_num': 'int',
        'file_alarm_detected_total_num': 'int',
        'rasp_alarm_detected_total_num': 'int',
        'wtp_alarm_detected_total_num': 'int',
        'image_risk_total_num': 'int',
        'container_alarm_total_num': 'int',
        'container_firewall_policy_total_num': 'int',
        'auto_kill_virus_status': 'bool'
    }

    attribute_map = {
        'vul_library_update_time': 'vul_library_update_time',
        'protect_days': 'protect_days',
        'threat_library_update_time': 'threat_library_update_time',
        'vul_detected_total_num': 'vul_detected_total_num',
        'baseline_detected_total_num': 'baseline_detected_total_num',
        'finger_scan_total_num': 'finger_scan_total_num',
        'alarm_detected_total_num': 'alarm_detected_total_num',
        'ransomware_alarm_detected_total_num': 'ransomware_alarm_detected_total_num',
        'file_alarm_detected_total_num': 'file_alarm_detected_total_num',
        'rasp_alarm_detected_total_num': 'rasp_alarm_detected_total_num',
        'wtp_alarm_detected_total_num': 'wtp_alarm_detected_total_num',
        'image_risk_total_num': 'image_risk_total_num',
        'container_alarm_total_num': 'container_alarm_total_num',
        'container_firewall_policy_total_num': 'container_firewall_policy_total_num',
        'auto_kill_virus_status': 'auto_kill_virus_status'
    }

    def __init__(self, vul_library_update_time=None, protect_days=None, threat_library_update_time=None, vul_detected_total_num=None, baseline_detected_total_num=None, finger_scan_total_num=None, alarm_detected_total_num=None, ransomware_alarm_detected_total_num=None, file_alarm_detected_total_num=None, rasp_alarm_detected_total_num=None, wtp_alarm_detected_total_num=None, image_risk_total_num=None, container_alarm_total_num=None, container_firewall_policy_total_num=None, auto_kill_virus_status=None):
        r"""ShowProtectStatisticsResponse

        The model defined in huaweicloud sdk

        :param vul_library_update_time: **参数解释**: 漏洞库更新时间 **取值范围**: 最小值0，最大值4071095999000 
        :type vul_library_update_time: int
        :param protect_days: **参数解释**: 守护天数 **取值范围**: 最小值0，最大值4071095999000 
        :type protect_days: int
        :param threat_library_update_time: **参数解释**: 病毒库更新时间 **取值范围**: 最小值0，最大值4071095999000 
        :type threat_library_update_time: int
        :param vul_detected_total_num: **参数解释**: 漏洞累计已检测数量 **取值范围**: 最小值0，最大值4071095999000 
        :type vul_detected_total_num: int
        :param baseline_detected_total_num: **参数解释**: 累计检测基线总数量 **取值范围**: 最小值0，最大值4071095999000 
        :type baseline_detected_total_num: int
        :param finger_scan_total_num: **参数解释**: 累计扫描指纹数量 **取值范围**: 最小值0，最大值4071095999000 
        :type finger_scan_total_num: int
        :param alarm_detected_total_num: **参数解释**: 入侵检测累计检测告警总数量 **取值范围**: 最小值0，最大值4071095999000 
        :type alarm_detected_total_num: int
        :param ransomware_alarm_detected_total_num: **参数解释**: 累计防御勒索病毒告警次数 **取值范围**: 最小值0，最大值4071095999000 
        :type ransomware_alarm_detected_total_num: int
        :param file_alarm_detected_total_num: **参数解释**: 文件完整性监控累计检测文件变更告警总数 **取值范围**: 最小值0，最大值4071095999000 
        :type file_alarm_detected_total_num: int
        :param rasp_alarm_detected_total_num: **参数解释**: 应用防护累计检测告警总数 **取值范围**: 最小值0，最大值4071095999000 
        :type rasp_alarm_detected_total_num: int
        :param wtp_alarm_detected_total_num: **参数解释**: 网页防篡改累计抵御网页防篡改次数 **取值范围**: 最小值0，最大值4071095999000 
        :type wtp_alarm_detected_total_num: int
        :param image_risk_total_num: **参数解释**: 容器镜像安全累计检测风险个数 **取值范围**: 最小值0，最大值4071095999000 
        :type image_risk_total_num: int
        :param container_alarm_total_num: **参数解释**: 容器安全防护累计检测容器告警个数 **取值范围**: 最小值0，最大值4071095999000 
        :type container_alarm_total_num: int
        :param container_firewall_policy_total_num: **参数解释**: 容器防火墙累计设置策略条数 **取值范围**: 最小值0，最大值4071095999000 
        :type container_firewall_policy_total_num: int
        :param auto_kill_virus_status: **参数解释**: 是否开启恶意自动查杀 **取值范围**: - true：是。 - false：否。 
        :type auto_kill_virus_status: bool
        """
        
        super(ShowProtectStatisticsResponse, self).__init__()

        self._vul_library_update_time = None
        self._protect_days = None
        self._threat_library_update_time = None
        self._vul_detected_total_num = None
        self._baseline_detected_total_num = None
        self._finger_scan_total_num = None
        self._alarm_detected_total_num = None
        self._ransomware_alarm_detected_total_num = None
        self._file_alarm_detected_total_num = None
        self._rasp_alarm_detected_total_num = None
        self._wtp_alarm_detected_total_num = None
        self._image_risk_total_num = None
        self._container_alarm_total_num = None
        self._container_firewall_policy_total_num = None
        self._auto_kill_virus_status = None
        self.discriminator = None

        if vul_library_update_time is not None:
            self.vul_library_update_time = vul_library_update_time
        if protect_days is not None:
            self.protect_days = protect_days
        if threat_library_update_time is not None:
            self.threat_library_update_time = threat_library_update_time
        if vul_detected_total_num is not None:
            self.vul_detected_total_num = vul_detected_total_num
        if baseline_detected_total_num is not None:
            self.baseline_detected_total_num = baseline_detected_total_num
        if finger_scan_total_num is not None:
            self.finger_scan_total_num = finger_scan_total_num
        if alarm_detected_total_num is not None:
            self.alarm_detected_total_num = alarm_detected_total_num
        if ransomware_alarm_detected_total_num is not None:
            self.ransomware_alarm_detected_total_num = ransomware_alarm_detected_total_num
        if file_alarm_detected_total_num is not None:
            self.file_alarm_detected_total_num = file_alarm_detected_total_num
        if rasp_alarm_detected_total_num is not None:
            self.rasp_alarm_detected_total_num = rasp_alarm_detected_total_num
        if wtp_alarm_detected_total_num is not None:
            self.wtp_alarm_detected_total_num = wtp_alarm_detected_total_num
        if image_risk_total_num is not None:
            self.image_risk_total_num = image_risk_total_num
        if container_alarm_total_num is not None:
            self.container_alarm_total_num = container_alarm_total_num
        if container_firewall_policy_total_num is not None:
            self.container_firewall_policy_total_num = container_firewall_policy_total_num
        if auto_kill_virus_status is not None:
            self.auto_kill_virus_status = auto_kill_virus_status

    @property
    def vul_library_update_time(self):
        r"""Gets the vul_library_update_time of this ShowProtectStatisticsResponse.

        **参数解释**: 漏洞库更新时间 **取值范围**: 最小值0，最大值4071095999000 

        :return: The vul_library_update_time of this ShowProtectStatisticsResponse.
        :rtype: int
        """
        return self._vul_library_update_time

    @vul_library_update_time.setter
    def vul_library_update_time(self, vul_library_update_time):
        r"""Sets the vul_library_update_time of this ShowProtectStatisticsResponse.

        **参数解释**: 漏洞库更新时间 **取值范围**: 最小值0，最大值4071095999000 

        :param vul_library_update_time: The vul_library_update_time of this ShowProtectStatisticsResponse.
        :type vul_library_update_time: int
        """
        self._vul_library_update_time = vul_library_update_time

    @property
    def protect_days(self):
        r"""Gets the protect_days of this ShowProtectStatisticsResponse.

        **参数解释**: 守护天数 **取值范围**: 最小值0，最大值4071095999000 

        :return: The protect_days of this ShowProtectStatisticsResponse.
        :rtype: int
        """
        return self._protect_days

    @protect_days.setter
    def protect_days(self, protect_days):
        r"""Sets the protect_days of this ShowProtectStatisticsResponse.

        **参数解释**: 守护天数 **取值范围**: 最小值0，最大值4071095999000 

        :param protect_days: The protect_days of this ShowProtectStatisticsResponse.
        :type protect_days: int
        """
        self._protect_days = protect_days

    @property
    def threat_library_update_time(self):
        r"""Gets the threat_library_update_time of this ShowProtectStatisticsResponse.

        **参数解释**: 病毒库更新时间 **取值范围**: 最小值0，最大值4071095999000 

        :return: The threat_library_update_time of this ShowProtectStatisticsResponse.
        :rtype: int
        """
        return self._threat_library_update_time

    @threat_library_update_time.setter
    def threat_library_update_time(self, threat_library_update_time):
        r"""Sets the threat_library_update_time of this ShowProtectStatisticsResponse.

        **参数解释**: 病毒库更新时间 **取值范围**: 最小值0，最大值4071095999000 

        :param threat_library_update_time: The threat_library_update_time of this ShowProtectStatisticsResponse.
        :type threat_library_update_time: int
        """
        self._threat_library_update_time = threat_library_update_time

    @property
    def vul_detected_total_num(self):
        r"""Gets the vul_detected_total_num of this ShowProtectStatisticsResponse.

        **参数解释**: 漏洞累计已检测数量 **取值范围**: 最小值0，最大值4071095999000 

        :return: The vul_detected_total_num of this ShowProtectStatisticsResponse.
        :rtype: int
        """
        return self._vul_detected_total_num

    @vul_detected_total_num.setter
    def vul_detected_total_num(self, vul_detected_total_num):
        r"""Sets the vul_detected_total_num of this ShowProtectStatisticsResponse.

        **参数解释**: 漏洞累计已检测数量 **取值范围**: 最小值0，最大值4071095999000 

        :param vul_detected_total_num: The vul_detected_total_num of this ShowProtectStatisticsResponse.
        :type vul_detected_total_num: int
        """
        self._vul_detected_total_num = vul_detected_total_num

    @property
    def baseline_detected_total_num(self):
        r"""Gets the baseline_detected_total_num of this ShowProtectStatisticsResponse.

        **参数解释**: 累计检测基线总数量 **取值范围**: 最小值0，最大值4071095999000 

        :return: The baseline_detected_total_num of this ShowProtectStatisticsResponse.
        :rtype: int
        """
        return self._baseline_detected_total_num

    @baseline_detected_total_num.setter
    def baseline_detected_total_num(self, baseline_detected_total_num):
        r"""Sets the baseline_detected_total_num of this ShowProtectStatisticsResponse.

        **参数解释**: 累计检测基线总数量 **取值范围**: 最小值0，最大值4071095999000 

        :param baseline_detected_total_num: The baseline_detected_total_num of this ShowProtectStatisticsResponse.
        :type baseline_detected_total_num: int
        """
        self._baseline_detected_total_num = baseline_detected_total_num

    @property
    def finger_scan_total_num(self):
        r"""Gets the finger_scan_total_num of this ShowProtectStatisticsResponse.

        **参数解释**: 累计扫描指纹数量 **取值范围**: 最小值0，最大值4071095999000 

        :return: The finger_scan_total_num of this ShowProtectStatisticsResponse.
        :rtype: int
        """
        return self._finger_scan_total_num

    @finger_scan_total_num.setter
    def finger_scan_total_num(self, finger_scan_total_num):
        r"""Sets the finger_scan_total_num of this ShowProtectStatisticsResponse.

        **参数解释**: 累计扫描指纹数量 **取值范围**: 最小值0，最大值4071095999000 

        :param finger_scan_total_num: The finger_scan_total_num of this ShowProtectStatisticsResponse.
        :type finger_scan_total_num: int
        """
        self._finger_scan_total_num = finger_scan_total_num

    @property
    def alarm_detected_total_num(self):
        r"""Gets the alarm_detected_total_num of this ShowProtectStatisticsResponse.

        **参数解释**: 入侵检测累计检测告警总数量 **取值范围**: 最小值0，最大值4071095999000 

        :return: The alarm_detected_total_num of this ShowProtectStatisticsResponse.
        :rtype: int
        """
        return self._alarm_detected_total_num

    @alarm_detected_total_num.setter
    def alarm_detected_total_num(self, alarm_detected_total_num):
        r"""Sets the alarm_detected_total_num of this ShowProtectStatisticsResponse.

        **参数解释**: 入侵检测累计检测告警总数量 **取值范围**: 最小值0，最大值4071095999000 

        :param alarm_detected_total_num: The alarm_detected_total_num of this ShowProtectStatisticsResponse.
        :type alarm_detected_total_num: int
        """
        self._alarm_detected_total_num = alarm_detected_total_num

    @property
    def ransomware_alarm_detected_total_num(self):
        r"""Gets the ransomware_alarm_detected_total_num of this ShowProtectStatisticsResponse.

        **参数解释**: 累计防御勒索病毒告警次数 **取值范围**: 最小值0，最大值4071095999000 

        :return: The ransomware_alarm_detected_total_num of this ShowProtectStatisticsResponse.
        :rtype: int
        """
        return self._ransomware_alarm_detected_total_num

    @ransomware_alarm_detected_total_num.setter
    def ransomware_alarm_detected_total_num(self, ransomware_alarm_detected_total_num):
        r"""Sets the ransomware_alarm_detected_total_num of this ShowProtectStatisticsResponse.

        **参数解释**: 累计防御勒索病毒告警次数 **取值范围**: 最小值0，最大值4071095999000 

        :param ransomware_alarm_detected_total_num: The ransomware_alarm_detected_total_num of this ShowProtectStatisticsResponse.
        :type ransomware_alarm_detected_total_num: int
        """
        self._ransomware_alarm_detected_total_num = ransomware_alarm_detected_total_num

    @property
    def file_alarm_detected_total_num(self):
        r"""Gets the file_alarm_detected_total_num of this ShowProtectStatisticsResponse.

        **参数解释**: 文件完整性监控累计检测文件变更告警总数 **取值范围**: 最小值0，最大值4071095999000 

        :return: The file_alarm_detected_total_num of this ShowProtectStatisticsResponse.
        :rtype: int
        """
        return self._file_alarm_detected_total_num

    @file_alarm_detected_total_num.setter
    def file_alarm_detected_total_num(self, file_alarm_detected_total_num):
        r"""Sets the file_alarm_detected_total_num of this ShowProtectStatisticsResponse.

        **参数解释**: 文件完整性监控累计检测文件变更告警总数 **取值范围**: 最小值0，最大值4071095999000 

        :param file_alarm_detected_total_num: The file_alarm_detected_total_num of this ShowProtectStatisticsResponse.
        :type file_alarm_detected_total_num: int
        """
        self._file_alarm_detected_total_num = file_alarm_detected_total_num

    @property
    def rasp_alarm_detected_total_num(self):
        r"""Gets the rasp_alarm_detected_total_num of this ShowProtectStatisticsResponse.

        **参数解释**: 应用防护累计检测告警总数 **取值范围**: 最小值0，最大值4071095999000 

        :return: The rasp_alarm_detected_total_num of this ShowProtectStatisticsResponse.
        :rtype: int
        """
        return self._rasp_alarm_detected_total_num

    @rasp_alarm_detected_total_num.setter
    def rasp_alarm_detected_total_num(self, rasp_alarm_detected_total_num):
        r"""Sets the rasp_alarm_detected_total_num of this ShowProtectStatisticsResponse.

        **参数解释**: 应用防护累计检测告警总数 **取值范围**: 最小值0，最大值4071095999000 

        :param rasp_alarm_detected_total_num: The rasp_alarm_detected_total_num of this ShowProtectStatisticsResponse.
        :type rasp_alarm_detected_total_num: int
        """
        self._rasp_alarm_detected_total_num = rasp_alarm_detected_total_num

    @property
    def wtp_alarm_detected_total_num(self):
        r"""Gets the wtp_alarm_detected_total_num of this ShowProtectStatisticsResponse.

        **参数解释**: 网页防篡改累计抵御网页防篡改次数 **取值范围**: 最小值0，最大值4071095999000 

        :return: The wtp_alarm_detected_total_num of this ShowProtectStatisticsResponse.
        :rtype: int
        """
        return self._wtp_alarm_detected_total_num

    @wtp_alarm_detected_total_num.setter
    def wtp_alarm_detected_total_num(self, wtp_alarm_detected_total_num):
        r"""Sets the wtp_alarm_detected_total_num of this ShowProtectStatisticsResponse.

        **参数解释**: 网页防篡改累计抵御网页防篡改次数 **取值范围**: 最小值0，最大值4071095999000 

        :param wtp_alarm_detected_total_num: The wtp_alarm_detected_total_num of this ShowProtectStatisticsResponse.
        :type wtp_alarm_detected_total_num: int
        """
        self._wtp_alarm_detected_total_num = wtp_alarm_detected_total_num

    @property
    def image_risk_total_num(self):
        r"""Gets the image_risk_total_num of this ShowProtectStatisticsResponse.

        **参数解释**: 容器镜像安全累计检测风险个数 **取值范围**: 最小值0，最大值4071095999000 

        :return: The image_risk_total_num of this ShowProtectStatisticsResponse.
        :rtype: int
        """
        return self._image_risk_total_num

    @image_risk_total_num.setter
    def image_risk_total_num(self, image_risk_total_num):
        r"""Sets the image_risk_total_num of this ShowProtectStatisticsResponse.

        **参数解释**: 容器镜像安全累计检测风险个数 **取值范围**: 最小值0，最大值4071095999000 

        :param image_risk_total_num: The image_risk_total_num of this ShowProtectStatisticsResponse.
        :type image_risk_total_num: int
        """
        self._image_risk_total_num = image_risk_total_num

    @property
    def container_alarm_total_num(self):
        r"""Gets the container_alarm_total_num of this ShowProtectStatisticsResponse.

        **参数解释**: 容器安全防护累计检测容器告警个数 **取值范围**: 最小值0，最大值4071095999000 

        :return: The container_alarm_total_num of this ShowProtectStatisticsResponse.
        :rtype: int
        """
        return self._container_alarm_total_num

    @container_alarm_total_num.setter
    def container_alarm_total_num(self, container_alarm_total_num):
        r"""Sets the container_alarm_total_num of this ShowProtectStatisticsResponse.

        **参数解释**: 容器安全防护累计检测容器告警个数 **取值范围**: 最小值0，最大值4071095999000 

        :param container_alarm_total_num: The container_alarm_total_num of this ShowProtectStatisticsResponse.
        :type container_alarm_total_num: int
        """
        self._container_alarm_total_num = container_alarm_total_num

    @property
    def container_firewall_policy_total_num(self):
        r"""Gets the container_firewall_policy_total_num of this ShowProtectStatisticsResponse.

        **参数解释**: 容器防火墙累计设置策略条数 **取值范围**: 最小值0，最大值4071095999000 

        :return: The container_firewall_policy_total_num of this ShowProtectStatisticsResponse.
        :rtype: int
        """
        return self._container_firewall_policy_total_num

    @container_firewall_policy_total_num.setter
    def container_firewall_policy_total_num(self, container_firewall_policy_total_num):
        r"""Sets the container_firewall_policy_total_num of this ShowProtectStatisticsResponse.

        **参数解释**: 容器防火墙累计设置策略条数 **取值范围**: 最小值0，最大值4071095999000 

        :param container_firewall_policy_total_num: The container_firewall_policy_total_num of this ShowProtectStatisticsResponse.
        :type container_firewall_policy_total_num: int
        """
        self._container_firewall_policy_total_num = container_firewall_policy_total_num

    @property
    def auto_kill_virus_status(self):
        r"""Gets the auto_kill_virus_status of this ShowProtectStatisticsResponse.

        **参数解释**: 是否开启恶意自动查杀 **取值范围**: - true：是。 - false：否。 

        :return: The auto_kill_virus_status of this ShowProtectStatisticsResponse.
        :rtype: bool
        """
        return self._auto_kill_virus_status

    @auto_kill_virus_status.setter
    def auto_kill_virus_status(self, auto_kill_virus_status):
        r"""Sets the auto_kill_virus_status of this ShowProtectStatisticsResponse.

        **参数解释**: 是否开启恶意自动查杀 **取值范围**: - true：是。 - false：否。 

        :param auto_kill_virus_status: The auto_kill_virus_status of this ShowProtectStatisticsResponse.
        :type auto_kill_virus_status: bool
        """
        self._auto_kill_virus_status = auto_kill_virus_status

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
        if not isinstance(other, ShowProtectStatisticsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
