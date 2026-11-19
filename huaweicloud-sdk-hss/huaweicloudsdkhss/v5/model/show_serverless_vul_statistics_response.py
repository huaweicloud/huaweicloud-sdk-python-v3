# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowServerlessVulStatisticsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_app_vul_num': 'int',
        'high_risky_app_vul': 'int',
        'total_linux_vul_num': 'int',
        'high_risky_linux_vul': 'int',
        'risky_pod_num': 'int',
        'total_scan_num': 'int',
        'last_update_time': 'int',
        'scanning_task_num': 'int'
    }

    attribute_map = {
        'total_app_vul_num': 'total_app_vul_num',
        'high_risky_app_vul': 'high_risky_app_vul',
        'total_linux_vul_num': 'total_linux_vul_num',
        'high_risky_linux_vul': 'high_risky_linux_vul',
        'risky_pod_num': 'risky_pod_num',
        'total_scan_num': 'total_scan_num',
        'last_update_time': 'last_update_time',
        'scanning_task_num': 'scanning_task_num'
    }

    def __init__(self, total_app_vul_num=None, high_risky_app_vul=None, total_linux_vul_num=None, high_risky_linux_vul=None, risky_pod_num=None, total_scan_num=None, last_update_time=None, scanning_task_num=None):
        r"""ShowServerlessVulStatisticsResponse

        The model defined in huaweicloud sdk

        :param total_app_vul_num: **参数解释**: 应用漏洞总数 **取值范围**: 最小值0，最大值2147483647 
        :type total_app_vul_num: int
        :param high_risky_app_vul: **参数解释**: 高风险应用漏洞数 **取值范围**: 最小值0，最大值2147483647 
        :type high_risky_app_vul: int
        :param total_linux_vul_num: **参数解释**: linux漏洞总数 **取值范围**: 最小值0，最大值2147483647 
        :type total_linux_vul_num: int
        :param high_risky_linux_vul: **参数解释**: 高风险应用漏洞数 **取值范围**: 最小值0，最大值2147483647 
        :type high_risky_linux_vul: int
        :param risky_pod_num: **参数解释**: 存在漏洞的实例数 **取值范围**: 最小值0，最大值2147483647 
        :type risky_pod_num: int
        :param total_scan_num: **参数解释**: 累计手动漏洞扫描次数 **取值范围**: 最小值0，最大值2147483647 
        :type total_scan_num: int
        :param last_update_time: **参数解释**: 最近检测时间 **取值范围**: 最小值0，最大值4071095999000 
        :type last_update_time: int
        :param scanning_task_num: **参数解释**: 正在扫描数 **取值范围**: 最小值0，最大值4071095999000 
        :type scanning_task_num: int
        """
        
        super().__init__()

        self._total_app_vul_num = None
        self._high_risky_app_vul = None
        self._total_linux_vul_num = None
        self._high_risky_linux_vul = None
        self._risky_pod_num = None
        self._total_scan_num = None
        self._last_update_time = None
        self._scanning_task_num = None
        self.discriminator = None

        if total_app_vul_num is not None:
            self.total_app_vul_num = total_app_vul_num
        if high_risky_app_vul is not None:
            self.high_risky_app_vul = high_risky_app_vul
        if total_linux_vul_num is not None:
            self.total_linux_vul_num = total_linux_vul_num
        if high_risky_linux_vul is not None:
            self.high_risky_linux_vul = high_risky_linux_vul
        if risky_pod_num is not None:
            self.risky_pod_num = risky_pod_num
        if total_scan_num is not None:
            self.total_scan_num = total_scan_num
        if last_update_time is not None:
            self.last_update_time = last_update_time
        if scanning_task_num is not None:
            self.scanning_task_num = scanning_task_num

    @property
    def total_app_vul_num(self):
        r"""Gets the total_app_vul_num of this ShowServerlessVulStatisticsResponse.

        **参数解释**: 应用漏洞总数 **取值范围**: 最小值0，最大值2147483647 

        :return: The total_app_vul_num of this ShowServerlessVulStatisticsResponse.
        :rtype: int
        """
        return self._total_app_vul_num

    @total_app_vul_num.setter
    def total_app_vul_num(self, total_app_vul_num):
        r"""Sets the total_app_vul_num of this ShowServerlessVulStatisticsResponse.

        **参数解释**: 应用漏洞总数 **取值范围**: 最小值0，最大值2147483647 

        :param total_app_vul_num: The total_app_vul_num of this ShowServerlessVulStatisticsResponse.
        :type total_app_vul_num: int
        """
        self._total_app_vul_num = total_app_vul_num

    @property
    def high_risky_app_vul(self):
        r"""Gets the high_risky_app_vul of this ShowServerlessVulStatisticsResponse.

        **参数解释**: 高风险应用漏洞数 **取值范围**: 最小值0，最大值2147483647 

        :return: The high_risky_app_vul of this ShowServerlessVulStatisticsResponse.
        :rtype: int
        """
        return self._high_risky_app_vul

    @high_risky_app_vul.setter
    def high_risky_app_vul(self, high_risky_app_vul):
        r"""Sets the high_risky_app_vul of this ShowServerlessVulStatisticsResponse.

        **参数解释**: 高风险应用漏洞数 **取值范围**: 最小值0，最大值2147483647 

        :param high_risky_app_vul: The high_risky_app_vul of this ShowServerlessVulStatisticsResponse.
        :type high_risky_app_vul: int
        """
        self._high_risky_app_vul = high_risky_app_vul

    @property
    def total_linux_vul_num(self):
        r"""Gets the total_linux_vul_num of this ShowServerlessVulStatisticsResponse.

        **参数解释**: linux漏洞总数 **取值范围**: 最小值0，最大值2147483647 

        :return: The total_linux_vul_num of this ShowServerlessVulStatisticsResponse.
        :rtype: int
        """
        return self._total_linux_vul_num

    @total_linux_vul_num.setter
    def total_linux_vul_num(self, total_linux_vul_num):
        r"""Sets the total_linux_vul_num of this ShowServerlessVulStatisticsResponse.

        **参数解释**: linux漏洞总数 **取值范围**: 最小值0，最大值2147483647 

        :param total_linux_vul_num: The total_linux_vul_num of this ShowServerlessVulStatisticsResponse.
        :type total_linux_vul_num: int
        """
        self._total_linux_vul_num = total_linux_vul_num

    @property
    def high_risky_linux_vul(self):
        r"""Gets the high_risky_linux_vul of this ShowServerlessVulStatisticsResponse.

        **参数解释**: 高风险应用漏洞数 **取值范围**: 最小值0，最大值2147483647 

        :return: The high_risky_linux_vul of this ShowServerlessVulStatisticsResponse.
        :rtype: int
        """
        return self._high_risky_linux_vul

    @high_risky_linux_vul.setter
    def high_risky_linux_vul(self, high_risky_linux_vul):
        r"""Sets the high_risky_linux_vul of this ShowServerlessVulStatisticsResponse.

        **参数解释**: 高风险应用漏洞数 **取值范围**: 最小值0，最大值2147483647 

        :param high_risky_linux_vul: The high_risky_linux_vul of this ShowServerlessVulStatisticsResponse.
        :type high_risky_linux_vul: int
        """
        self._high_risky_linux_vul = high_risky_linux_vul

    @property
    def risky_pod_num(self):
        r"""Gets the risky_pod_num of this ShowServerlessVulStatisticsResponse.

        **参数解释**: 存在漏洞的实例数 **取值范围**: 最小值0，最大值2147483647 

        :return: The risky_pod_num of this ShowServerlessVulStatisticsResponse.
        :rtype: int
        """
        return self._risky_pod_num

    @risky_pod_num.setter
    def risky_pod_num(self, risky_pod_num):
        r"""Sets the risky_pod_num of this ShowServerlessVulStatisticsResponse.

        **参数解释**: 存在漏洞的实例数 **取值范围**: 最小值0，最大值2147483647 

        :param risky_pod_num: The risky_pod_num of this ShowServerlessVulStatisticsResponse.
        :type risky_pod_num: int
        """
        self._risky_pod_num = risky_pod_num

    @property
    def total_scan_num(self):
        r"""Gets the total_scan_num of this ShowServerlessVulStatisticsResponse.

        **参数解释**: 累计手动漏洞扫描次数 **取值范围**: 最小值0，最大值2147483647 

        :return: The total_scan_num of this ShowServerlessVulStatisticsResponse.
        :rtype: int
        """
        return self._total_scan_num

    @total_scan_num.setter
    def total_scan_num(self, total_scan_num):
        r"""Sets the total_scan_num of this ShowServerlessVulStatisticsResponse.

        **参数解释**: 累计手动漏洞扫描次数 **取值范围**: 最小值0，最大值2147483647 

        :param total_scan_num: The total_scan_num of this ShowServerlessVulStatisticsResponse.
        :type total_scan_num: int
        """
        self._total_scan_num = total_scan_num

    @property
    def last_update_time(self):
        r"""Gets the last_update_time of this ShowServerlessVulStatisticsResponse.

        **参数解释**: 最近检测时间 **取值范围**: 最小值0，最大值4071095999000 

        :return: The last_update_time of this ShowServerlessVulStatisticsResponse.
        :rtype: int
        """
        return self._last_update_time

    @last_update_time.setter
    def last_update_time(self, last_update_time):
        r"""Sets the last_update_time of this ShowServerlessVulStatisticsResponse.

        **参数解释**: 最近检测时间 **取值范围**: 最小值0，最大值4071095999000 

        :param last_update_time: The last_update_time of this ShowServerlessVulStatisticsResponse.
        :type last_update_time: int
        """
        self._last_update_time = last_update_time

    @property
    def scanning_task_num(self):
        r"""Gets the scanning_task_num of this ShowServerlessVulStatisticsResponse.

        **参数解释**: 正在扫描数 **取值范围**: 最小值0，最大值4071095999000 

        :return: The scanning_task_num of this ShowServerlessVulStatisticsResponse.
        :rtype: int
        """
        return self._scanning_task_num

    @scanning_task_num.setter
    def scanning_task_num(self, scanning_task_num):
        r"""Sets the scanning_task_num of this ShowServerlessVulStatisticsResponse.

        **参数解释**: 正在扫描数 **取值范围**: 最小值0，最大值4071095999000 

        :param scanning_task_num: The scanning_task_num of this ShowServerlessVulStatisticsResponse.
        :type scanning_task_num: int
        """
        self._scanning_task_num = scanning_task_num

    def to_dict(self):
        import warnings
        warnings.warn("ShowServerlessVulStatisticsResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ShowServerlessVulStatisticsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
