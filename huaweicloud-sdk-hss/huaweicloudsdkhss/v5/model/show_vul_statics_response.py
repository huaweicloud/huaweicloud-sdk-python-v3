# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowVulStaticsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'need_urgent_repair': 'int',
        'unrepair': 'int',
        'existed_vul_hosts': 'int',
        'today_handle': 'int',
        'all_handle': 'int',
        'supported': 'int',
        'vul_library_update_time': 'int'
    }

    attribute_map = {
        'need_urgent_repair': 'need_urgent_repair',
        'unrepair': 'unrepair',
        'existed_vul_hosts': 'existed_vul_hosts',
        'today_handle': 'today_handle',
        'all_handle': 'all_handle',
        'supported': 'supported',
        'vul_library_update_time': 'vul_library_update_time'
    }

    def __init__(self, need_urgent_repair=None, unrepair=None, existed_vul_hosts=None, today_handle=None, all_handle=None, supported=None, vul_library_update_time=None):
        r"""ShowVulStaticsResponse

        The model defined in huaweicloud sdk

        :param need_urgent_repair: 需紧急修复的漏洞数
        :type need_urgent_repair: int
        :param unrepair: 未完成修复的漏洞数
        :type unrepair: int
        :param existed_vul_hosts: 存在漏洞的服务器数
        :type existed_vul_hosts: int
        :param today_handle: 今日处理漏洞数
        :type today_handle: int
        :param all_handle: 累计处理漏洞数
        :type all_handle: int
        :param supported: 已支持漏洞数
        :type supported: int
        :param vul_library_update_time: 漏洞库更新时间
        :type vul_library_update_time: int
        """
        
        super(ShowVulStaticsResponse, self).__init__()

        self._need_urgent_repair = None
        self._unrepair = None
        self._existed_vul_hosts = None
        self._today_handle = None
        self._all_handle = None
        self._supported = None
        self._vul_library_update_time = None
        self.discriminator = None

        if need_urgent_repair is not None:
            self.need_urgent_repair = need_urgent_repair
        if unrepair is not None:
            self.unrepair = unrepair
        if existed_vul_hosts is not None:
            self.existed_vul_hosts = existed_vul_hosts
        if today_handle is not None:
            self.today_handle = today_handle
        if all_handle is not None:
            self.all_handle = all_handle
        if supported is not None:
            self.supported = supported
        if vul_library_update_time is not None:
            self.vul_library_update_time = vul_library_update_time

    @property
    def need_urgent_repair(self):
        r"""Gets the need_urgent_repair of this ShowVulStaticsResponse.

        需紧急修复的漏洞数

        :return: The need_urgent_repair of this ShowVulStaticsResponse.
        :rtype: int
        """
        return self._need_urgent_repair

    @need_urgent_repair.setter
    def need_urgent_repair(self, need_urgent_repair):
        r"""Sets the need_urgent_repair of this ShowVulStaticsResponse.

        需紧急修复的漏洞数

        :param need_urgent_repair: The need_urgent_repair of this ShowVulStaticsResponse.
        :type need_urgent_repair: int
        """
        self._need_urgent_repair = need_urgent_repair

    @property
    def unrepair(self):
        r"""Gets the unrepair of this ShowVulStaticsResponse.

        未完成修复的漏洞数

        :return: The unrepair of this ShowVulStaticsResponse.
        :rtype: int
        """
        return self._unrepair

    @unrepair.setter
    def unrepair(self, unrepair):
        r"""Sets the unrepair of this ShowVulStaticsResponse.

        未完成修复的漏洞数

        :param unrepair: The unrepair of this ShowVulStaticsResponse.
        :type unrepair: int
        """
        self._unrepair = unrepair

    @property
    def existed_vul_hosts(self):
        r"""Gets the existed_vul_hosts of this ShowVulStaticsResponse.

        存在漏洞的服务器数

        :return: The existed_vul_hosts of this ShowVulStaticsResponse.
        :rtype: int
        """
        return self._existed_vul_hosts

    @existed_vul_hosts.setter
    def existed_vul_hosts(self, existed_vul_hosts):
        r"""Sets the existed_vul_hosts of this ShowVulStaticsResponse.

        存在漏洞的服务器数

        :param existed_vul_hosts: The existed_vul_hosts of this ShowVulStaticsResponse.
        :type existed_vul_hosts: int
        """
        self._existed_vul_hosts = existed_vul_hosts

    @property
    def today_handle(self):
        r"""Gets the today_handle of this ShowVulStaticsResponse.

        今日处理漏洞数

        :return: The today_handle of this ShowVulStaticsResponse.
        :rtype: int
        """
        return self._today_handle

    @today_handle.setter
    def today_handle(self, today_handle):
        r"""Sets the today_handle of this ShowVulStaticsResponse.

        今日处理漏洞数

        :param today_handle: The today_handle of this ShowVulStaticsResponse.
        :type today_handle: int
        """
        self._today_handle = today_handle

    @property
    def all_handle(self):
        r"""Gets the all_handle of this ShowVulStaticsResponse.

        累计处理漏洞数

        :return: The all_handle of this ShowVulStaticsResponse.
        :rtype: int
        """
        return self._all_handle

    @all_handle.setter
    def all_handle(self, all_handle):
        r"""Sets the all_handle of this ShowVulStaticsResponse.

        累计处理漏洞数

        :param all_handle: The all_handle of this ShowVulStaticsResponse.
        :type all_handle: int
        """
        self._all_handle = all_handle

    @property
    def supported(self):
        r"""Gets the supported of this ShowVulStaticsResponse.

        已支持漏洞数

        :return: The supported of this ShowVulStaticsResponse.
        :rtype: int
        """
        return self._supported

    @supported.setter
    def supported(self, supported):
        r"""Sets the supported of this ShowVulStaticsResponse.

        已支持漏洞数

        :param supported: The supported of this ShowVulStaticsResponse.
        :type supported: int
        """
        self._supported = supported

    @property
    def vul_library_update_time(self):
        r"""Gets the vul_library_update_time of this ShowVulStaticsResponse.

        漏洞库更新时间

        :return: The vul_library_update_time of this ShowVulStaticsResponse.
        :rtype: int
        """
        return self._vul_library_update_time

    @vul_library_update_time.setter
    def vul_library_update_time(self, vul_library_update_time):
        r"""Sets the vul_library_update_time of this ShowVulStaticsResponse.

        漏洞库更新时间

        :param vul_library_update_time: The vul_library_update_time of this ShowVulStaticsResponse.
        :type vul_library_update_time: int
        """
        self._vul_library_update_time = vul_library_update_time

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
        if not isinstance(other, ShowVulStaticsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
