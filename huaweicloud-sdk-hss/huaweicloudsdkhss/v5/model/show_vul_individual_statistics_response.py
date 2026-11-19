# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowVulIndividualStatisticsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'need_urgent_repair_num': 'int',
        'unhandled_num': 'int',
        'existed_vul_host_num': 'int',
        'today_handled_num': 'int',
        'all_handled_num': 'int',
        'vul_library_supported_num': 'int',
        'vul_library_update_time': 'int',
        'linux_vul_unhandled_num': 'int',
        'windows_vul_unhandled_num': 'int',
        'web_cms_vul_unhandled_num': 'int',
        'app_vul_unhandled_num': 'int',
        'urgent_vul_unhandled_num': 'int',
        'need_reboot_host_num': 'int',
        'max_vul_handle_num': 'int'
    }

    attribute_map = {
        'need_urgent_repair_num': 'need_urgent_repair_num',
        'unhandled_num': 'unhandled_num',
        'existed_vul_host_num': 'existed_vul_host_num',
        'today_handled_num': 'today_handled_num',
        'all_handled_num': 'all_handled_num',
        'vul_library_supported_num': 'vul_library_supported_num',
        'vul_library_update_time': 'vul_library_update_time',
        'linux_vul_unhandled_num': 'linux_vul_unhandled_num',
        'windows_vul_unhandled_num': 'windows_vul_unhandled_num',
        'web_cms_vul_unhandled_num': 'web_cms_vul_unhandled_num',
        'app_vul_unhandled_num': 'app_vul_unhandled_num',
        'urgent_vul_unhandled_num': 'urgent_vul_unhandled_num',
        'need_reboot_host_num': 'need_reboot_host_num',
        'max_vul_handle_num': 'max_vul_handle_num'
    }

    def __init__(self, need_urgent_repair_num=None, unhandled_num=None, existed_vul_host_num=None, today_handled_num=None, all_handled_num=None, vul_library_supported_num=None, vul_library_update_time=None, linux_vul_unhandled_num=None, windows_vul_unhandled_num=None, web_cms_vul_unhandled_num=None, app_vul_unhandled_num=None, urgent_vul_unhandled_num=None, need_reboot_host_num=None, max_vul_handle_num=None):
        r"""ShowVulIndividualStatisticsResponse

        The model defined in huaweicloud sdk

        :param need_urgent_repair_num: **参数解释**: 需要紧急修复的漏洞数量 **取值范围**: 最小值0，最大值2147483647 
        :type need_urgent_repair_num: int
        :param unhandled_num: **参数解释**: 未完成修复的漏洞数量 **取值范围**: 最小值0，最大值2147483647 
        :type unhandled_num: int
        :param existed_vul_host_num: **参数解释**: 存在漏洞的服务器数量 **取值范围**: 最小值0，最大值2147483647 
        :type existed_vul_host_num: int
        :param today_handled_num: **参数解释**: 今日处理的漏洞数量 **取值范围**: 最小值0，最大值2147483647 
        :type today_handled_num: int
        :param all_handled_num: **参数解释**: 累计处理的漏洞数量 **取值范围**: 最小值0，最大值2147483647 
        :type all_handled_num: int
        :param vul_library_supported_num: **参数解释**: 漏洞库已支持漏洞数 **取值范围**: 最小值0，最大值2147483647 
        :type vul_library_supported_num: int
        :param vul_library_update_time: **参数解释**: 漏洞库更新时间，Unix时间戳格式，单位为毫秒 **取值范围**: 最小值0，最大值9223372036854775807 
        :type vul_library_update_time: int
        :param linux_vul_unhandled_num: **参数解释**: 未处置的Linux漏洞数量 **取值范围**: 最小值0，最大值2147483647 
        :type linux_vul_unhandled_num: int
        :param windows_vul_unhandled_num: **参数解释**: 未处置的Windows漏洞数量 **取值范围**: 最小值0，最大值2147483647 
        :type windows_vul_unhandled_num: int
        :param web_cms_vul_unhandled_num: **参数解释**: 未处置的Web CMS漏洞数量 **取值范围**: 最小值0，最大值2147483647 
        :type web_cms_vul_unhandled_num: int
        :param app_vul_unhandled_num: **参数解释**: 未处置的应用漏洞数量 **取值范围**: 最小值0，最大值2147483647 
        :type app_vul_unhandled_num: int
        :param urgent_vul_unhandled_num: **参数解释**: 未处置的应急漏洞数量 **取值范围**: 最小值0，最大值2147483647 
        :type urgent_vul_unhandled_num: int
        :param need_reboot_host_num: **参数解释**: 修复成功待重启的主机数量 **取值范围**: 最小值0，最大值2147483647 
        :type need_reboot_host_num: int
        :param max_vul_handle_num: **参数解释**: 单次最大可处置的漏洞数量 **取值范围**: 最小值0，最大值2147483647 
        :type max_vul_handle_num: int
        """
        
        super().__init__()

        self._need_urgent_repair_num = None
        self._unhandled_num = None
        self._existed_vul_host_num = None
        self._today_handled_num = None
        self._all_handled_num = None
        self._vul_library_supported_num = None
        self._vul_library_update_time = None
        self._linux_vul_unhandled_num = None
        self._windows_vul_unhandled_num = None
        self._web_cms_vul_unhandled_num = None
        self._app_vul_unhandled_num = None
        self._urgent_vul_unhandled_num = None
        self._need_reboot_host_num = None
        self._max_vul_handle_num = None
        self.discriminator = None

        if need_urgent_repair_num is not None:
            self.need_urgent_repair_num = need_urgent_repair_num
        if unhandled_num is not None:
            self.unhandled_num = unhandled_num
        if existed_vul_host_num is not None:
            self.existed_vul_host_num = existed_vul_host_num
        if today_handled_num is not None:
            self.today_handled_num = today_handled_num
        if all_handled_num is not None:
            self.all_handled_num = all_handled_num
        if vul_library_supported_num is not None:
            self.vul_library_supported_num = vul_library_supported_num
        if vul_library_update_time is not None:
            self.vul_library_update_time = vul_library_update_time
        if linux_vul_unhandled_num is not None:
            self.linux_vul_unhandled_num = linux_vul_unhandled_num
        if windows_vul_unhandled_num is not None:
            self.windows_vul_unhandled_num = windows_vul_unhandled_num
        if web_cms_vul_unhandled_num is not None:
            self.web_cms_vul_unhandled_num = web_cms_vul_unhandled_num
        if app_vul_unhandled_num is not None:
            self.app_vul_unhandled_num = app_vul_unhandled_num
        if urgent_vul_unhandled_num is not None:
            self.urgent_vul_unhandled_num = urgent_vul_unhandled_num
        if need_reboot_host_num is not None:
            self.need_reboot_host_num = need_reboot_host_num
        if max_vul_handle_num is not None:
            self.max_vul_handle_num = max_vul_handle_num

    @property
    def need_urgent_repair_num(self):
        r"""Gets the need_urgent_repair_num of this ShowVulIndividualStatisticsResponse.

        **参数解释**: 需要紧急修复的漏洞数量 **取值范围**: 最小值0，最大值2147483647 

        :return: The need_urgent_repair_num of this ShowVulIndividualStatisticsResponse.
        :rtype: int
        """
        return self._need_urgent_repair_num

    @need_urgent_repair_num.setter
    def need_urgent_repair_num(self, need_urgent_repair_num):
        r"""Sets the need_urgent_repair_num of this ShowVulIndividualStatisticsResponse.

        **参数解释**: 需要紧急修复的漏洞数量 **取值范围**: 最小值0，最大值2147483647 

        :param need_urgent_repair_num: The need_urgent_repair_num of this ShowVulIndividualStatisticsResponse.
        :type need_urgent_repair_num: int
        """
        self._need_urgent_repair_num = need_urgent_repair_num

    @property
    def unhandled_num(self):
        r"""Gets the unhandled_num of this ShowVulIndividualStatisticsResponse.

        **参数解释**: 未完成修复的漏洞数量 **取值范围**: 最小值0，最大值2147483647 

        :return: The unhandled_num of this ShowVulIndividualStatisticsResponse.
        :rtype: int
        """
        return self._unhandled_num

    @unhandled_num.setter
    def unhandled_num(self, unhandled_num):
        r"""Sets the unhandled_num of this ShowVulIndividualStatisticsResponse.

        **参数解释**: 未完成修复的漏洞数量 **取值范围**: 最小值0，最大值2147483647 

        :param unhandled_num: The unhandled_num of this ShowVulIndividualStatisticsResponse.
        :type unhandled_num: int
        """
        self._unhandled_num = unhandled_num

    @property
    def existed_vul_host_num(self):
        r"""Gets the existed_vul_host_num of this ShowVulIndividualStatisticsResponse.

        **参数解释**: 存在漏洞的服务器数量 **取值范围**: 最小值0，最大值2147483647 

        :return: The existed_vul_host_num of this ShowVulIndividualStatisticsResponse.
        :rtype: int
        """
        return self._existed_vul_host_num

    @existed_vul_host_num.setter
    def existed_vul_host_num(self, existed_vul_host_num):
        r"""Sets the existed_vul_host_num of this ShowVulIndividualStatisticsResponse.

        **参数解释**: 存在漏洞的服务器数量 **取值范围**: 最小值0，最大值2147483647 

        :param existed_vul_host_num: The existed_vul_host_num of this ShowVulIndividualStatisticsResponse.
        :type existed_vul_host_num: int
        """
        self._existed_vul_host_num = existed_vul_host_num

    @property
    def today_handled_num(self):
        r"""Gets the today_handled_num of this ShowVulIndividualStatisticsResponse.

        **参数解释**: 今日处理的漏洞数量 **取值范围**: 最小值0，最大值2147483647 

        :return: The today_handled_num of this ShowVulIndividualStatisticsResponse.
        :rtype: int
        """
        return self._today_handled_num

    @today_handled_num.setter
    def today_handled_num(self, today_handled_num):
        r"""Sets the today_handled_num of this ShowVulIndividualStatisticsResponse.

        **参数解释**: 今日处理的漏洞数量 **取值范围**: 最小值0，最大值2147483647 

        :param today_handled_num: The today_handled_num of this ShowVulIndividualStatisticsResponse.
        :type today_handled_num: int
        """
        self._today_handled_num = today_handled_num

    @property
    def all_handled_num(self):
        r"""Gets the all_handled_num of this ShowVulIndividualStatisticsResponse.

        **参数解释**: 累计处理的漏洞数量 **取值范围**: 最小值0，最大值2147483647 

        :return: The all_handled_num of this ShowVulIndividualStatisticsResponse.
        :rtype: int
        """
        return self._all_handled_num

    @all_handled_num.setter
    def all_handled_num(self, all_handled_num):
        r"""Sets the all_handled_num of this ShowVulIndividualStatisticsResponse.

        **参数解释**: 累计处理的漏洞数量 **取值范围**: 最小值0，最大值2147483647 

        :param all_handled_num: The all_handled_num of this ShowVulIndividualStatisticsResponse.
        :type all_handled_num: int
        """
        self._all_handled_num = all_handled_num

    @property
    def vul_library_supported_num(self):
        r"""Gets the vul_library_supported_num of this ShowVulIndividualStatisticsResponse.

        **参数解释**: 漏洞库已支持漏洞数 **取值范围**: 最小值0，最大值2147483647 

        :return: The vul_library_supported_num of this ShowVulIndividualStatisticsResponse.
        :rtype: int
        """
        return self._vul_library_supported_num

    @vul_library_supported_num.setter
    def vul_library_supported_num(self, vul_library_supported_num):
        r"""Sets the vul_library_supported_num of this ShowVulIndividualStatisticsResponse.

        **参数解释**: 漏洞库已支持漏洞数 **取值范围**: 最小值0，最大值2147483647 

        :param vul_library_supported_num: The vul_library_supported_num of this ShowVulIndividualStatisticsResponse.
        :type vul_library_supported_num: int
        """
        self._vul_library_supported_num = vul_library_supported_num

    @property
    def vul_library_update_time(self):
        r"""Gets the vul_library_update_time of this ShowVulIndividualStatisticsResponse.

        **参数解释**: 漏洞库更新时间，Unix时间戳格式，单位为毫秒 **取值范围**: 最小值0，最大值9223372036854775807 

        :return: The vul_library_update_time of this ShowVulIndividualStatisticsResponse.
        :rtype: int
        """
        return self._vul_library_update_time

    @vul_library_update_time.setter
    def vul_library_update_time(self, vul_library_update_time):
        r"""Sets the vul_library_update_time of this ShowVulIndividualStatisticsResponse.

        **参数解释**: 漏洞库更新时间，Unix时间戳格式，单位为毫秒 **取值范围**: 最小值0，最大值9223372036854775807 

        :param vul_library_update_time: The vul_library_update_time of this ShowVulIndividualStatisticsResponse.
        :type vul_library_update_time: int
        """
        self._vul_library_update_time = vul_library_update_time

    @property
    def linux_vul_unhandled_num(self):
        r"""Gets the linux_vul_unhandled_num of this ShowVulIndividualStatisticsResponse.

        **参数解释**: 未处置的Linux漏洞数量 **取值范围**: 最小值0，最大值2147483647 

        :return: The linux_vul_unhandled_num of this ShowVulIndividualStatisticsResponse.
        :rtype: int
        """
        return self._linux_vul_unhandled_num

    @linux_vul_unhandled_num.setter
    def linux_vul_unhandled_num(self, linux_vul_unhandled_num):
        r"""Sets the linux_vul_unhandled_num of this ShowVulIndividualStatisticsResponse.

        **参数解释**: 未处置的Linux漏洞数量 **取值范围**: 最小值0，最大值2147483647 

        :param linux_vul_unhandled_num: The linux_vul_unhandled_num of this ShowVulIndividualStatisticsResponse.
        :type linux_vul_unhandled_num: int
        """
        self._linux_vul_unhandled_num = linux_vul_unhandled_num

    @property
    def windows_vul_unhandled_num(self):
        r"""Gets the windows_vul_unhandled_num of this ShowVulIndividualStatisticsResponse.

        **参数解释**: 未处置的Windows漏洞数量 **取值范围**: 最小值0，最大值2147483647 

        :return: The windows_vul_unhandled_num of this ShowVulIndividualStatisticsResponse.
        :rtype: int
        """
        return self._windows_vul_unhandled_num

    @windows_vul_unhandled_num.setter
    def windows_vul_unhandled_num(self, windows_vul_unhandled_num):
        r"""Sets the windows_vul_unhandled_num of this ShowVulIndividualStatisticsResponse.

        **参数解释**: 未处置的Windows漏洞数量 **取值范围**: 最小值0，最大值2147483647 

        :param windows_vul_unhandled_num: The windows_vul_unhandled_num of this ShowVulIndividualStatisticsResponse.
        :type windows_vul_unhandled_num: int
        """
        self._windows_vul_unhandled_num = windows_vul_unhandled_num

    @property
    def web_cms_vul_unhandled_num(self):
        r"""Gets the web_cms_vul_unhandled_num of this ShowVulIndividualStatisticsResponse.

        **参数解释**: 未处置的Web CMS漏洞数量 **取值范围**: 最小值0，最大值2147483647 

        :return: The web_cms_vul_unhandled_num of this ShowVulIndividualStatisticsResponse.
        :rtype: int
        """
        return self._web_cms_vul_unhandled_num

    @web_cms_vul_unhandled_num.setter
    def web_cms_vul_unhandled_num(self, web_cms_vul_unhandled_num):
        r"""Sets the web_cms_vul_unhandled_num of this ShowVulIndividualStatisticsResponse.

        **参数解释**: 未处置的Web CMS漏洞数量 **取值范围**: 最小值0，最大值2147483647 

        :param web_cms_vul_unhandled_num: The web_cms_vul_unhandled_num of this ShowVulIndividualStatisticsResponse.
        :type web_cms_vul_unhandled_num: int
        """
        self._web_cms_vul_unhandled_num = web_cms_vul_unhandled_num

    @property
    def app_vul_unhandled_num(self):
        r"""Gets the app_vul_unhandled_num of this ShowVulIndividualStatisticsResponse.

        **参数解释**: 未处置的应用漏洞数量 **取值范围**: 最小值0，最大值2147483647 

        :return: The app_vul_unhandled_num of this ShowVulIndividualStatisticsResponse.
        :rtype: int
        """
        return self._app_vul_unhandled_num

    @app_vul_unhandled_num.setter
    def app_vul_unhandled_num(self, app_vul_unhandled_num):
        r"""Sets the app_vul_unhandled_num of this ShowVulIndividualStatisticsResponse.

        **参数解释**: 未处置的应用漏洞数量 **取值范围**: 最小值0，最大值2147483647 

        :param app_vul_unhandled_num: The app_vul_unhandled_num of this ShowVulIndividualStatisticsResponse.
        :type app_vul_unhandled_num: int
        """
        self._app_vul_unhandled_num = app_vul_unhandled_num

    @property
    def urgent_vul_unhandled_num(self):
        r"""Gets the urgent_vul_unhandled_num of this ShowVulIndividualStatisticsResponse.

        **参数解释**: 未处置的应急漏洞数量 **取值范围**: 最小值0，最大值2147483647 

        :return: The urgent_vul_unhandled_num of this ShowVulIndividualStatisticsResponse.
        :rtype: int
        """
        return self._urgent_vul_unhandled_num

    @urgent_vul_unhandled_num.setter
    def urgent_vul_unhandled_num(self, urgent_vul_unhandled_num):
        r"""Sets the urgent_vul_unhandled_num of this ShowVulIndividualStatisticsResponse.

        **参数解释**: 未处置的应急漏洞数量 **取值范围**: 最小值0，最大值2147483647 

        :param urgent_vul_unhandled_num: The urgent_vul_unhandled_num of this ShowVulIndividualStatisticsResponse.
        :type urgent_vul_unhandled_num: int
        """
        self._urgent_vul_unhandled_num = urgent_vul_unhandled_num

    @property
    def need_reboot_host_num(self):
        r"""Gets the need_reboot_host_num of this ShowVulIndividualStatisticsResponse.

        **参数解释**: 修复成功待重启的主机数量 **取值范围**: 最小值0，最大值2147483647 

        :return: The need_reboot_host_num of this ShowVulIndividualStatisticsResponse.
        :rtype: int
        """
        return self._need_reboot_host_num

    @need_reboot_host_num.setter
    def need_reboot_host_num(self, need_reboot_host_num):
        r"""Sets the need_reboot_host_num of this ShowVulIndividualStatisticsResponse.

        **参数解释**: 修复成功待重启的主机数量 **取值范围**: 最小值0，最大值2147483647 

        :param need_reboot_host_num: The need_reboot_host_num of this ShowVulIndividualStatisticsResponse.
        :type need_reboot_host_num: int
        """
        self._need_reboot_host_num = need_reboot_host_num

    @property
    def max_vul_handle_num(self):
        r"""Gets the max_vul_handle_num of this ShowVulIndividualStatisticsResponse.

        **参数解释**: 单次最大可处置的漏洞数量 **取值范围**: 最小值0，最大值2147483647 

        :return: The max_vul_handle_num of this ShowVulIndividualStatisticsResponse.
        :rtype: int
        """
        return self._max_vul_handle_num

    @max_vul_handle_num.setter
    def max_vul_handle_num(self, max_vul_handle_num):
        r"""Sets the max_vul_handle_num of this ShowVulIndividualStatisticsResponse.

        **参数解释**: 单次最大可处置的漏洞数量 **取值范围**: 最小值0，最大值2147483647 

        :param max_vul_handle_num: The max_vul_handle_num of this ShowVulIndividualStatisticsResponse.
        :type max_vul_handle_num: int
        """
        self._max_vul_handle_num = max_vul_handle_num

    def to_dict(self):
        import warnings
        warnings.warn("ShowVulIndividualStatisticsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowVulIndividualStatisticsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
