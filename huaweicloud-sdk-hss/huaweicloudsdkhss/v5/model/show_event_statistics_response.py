# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowEventStatisticsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'risky_host_num': 'int',
        'risky_container_num': 'int',
        'unhandled_num': 'int',
        'processed_num': 'int',
        'auto_blocked_num': 'int',
        'blocked_ip_num': 'int',
        'isolated_file_num': 'int',
        'support_es': 'bool'
    }

    attribute_map = {
        'risky_host_num': 'risky_host_num',
        'risky_container_num': 'risky_container_num',
        'unhandled_num': 'unhandled_num',
        'processed_num': 'processed_num',
        'auto_blocked_num': 'auto_blocked_num',
        'blocked_ip_num': 'blocked_ip_num',
        'isolated_file_num': 'isolated_file_num',
        'support_es': 'support_ES'
    }

    def __init__(self, risky_host_num=None, risky_container_num=None, unhandled_num=None, processed_num=None, auto_blocked_num=None, blocked_ip_num=None, isolated_file_num=None, support_es=None):
        r"""ShowEventStatisticsResponse

        The model defined in huaweicloud sdk

        :param risky_host_num: **参数解释**: 存在告警的服务器数量 **取值范围**: 最小值0，最大值9223372036854775807 
        :type risky_host_num: int
        :param risky_container_num: **参数解释**: 存在告警的容器数量 **取值范围**: 最小值0，最大值9223372036854775807 
        :type risky_container_num: int
        :param unhandled_num: **参数解释**: 待处理告警事件数量 **取值范围**: 最小值0，最大值9223372036854775807 
        :type unhandled_num: int
        :param processed_num: **参数解释**: 已处理告警事件数量 **取值范围**: 最小值0，最大值9223372036854775807 
        :type processed_num: int
        :param auto_blocked_num: **参数解释**: 自动处置告警事件数量 **取值范围**: 最小值0，最大值9223372036854775807 
        :type auto_blocked_num: int
        :param blocked_ip_num: **参数解释**: 已拦截IP数量 **取值范围**: 最小值0，最大值9223372036854775807 
        :type blocked_ip_num: int
        :param isolated_file_num: **参数解释**: 已隔离文件数量 **取值范围**: 最小值0，最大值9223372036854775807 
        :type isolated_file_num: int
        :param support_es: **参数解释**: 是否支持ES查询 **取值范围**: - true：支持 - false：不支持 
        :type support_es: bool
        """
        
        super().__init__()

        self._risky_host_num = None
        self._risky_container_num = None
        self._unhandled_num = None
        self._processed_num = None
        self._auto_blocked_num = None
        self._blocked_ip_num = None
        self._isolated_file_num = None
        self._support_es = None
        self.discriminator = None

        if risky_host_num is not None:
            self.risky_host_num = risky_host_num
        if risky_container_num is not None:
            self.risky_container_num = risky_container_num
        if unhandled_num is not None:
            self.unhandled_num = unhandled_num
        if processed_num is not None:
            self.processed_num = processed_num
        if auto_blocked_num is not None:
            self.auto_blocked_num = auto_blocked_num
        if blocked_ip_num is not None:
            self.blocked_ip_num = blocked_ip_num
        if isolated_file_num is not None:
            self.isolated_file_num = isolated_file_num
        if support_es is not None:
            self.support_es = support_es

    @property
    def risky_host_num(self):
        r"""Gets the risky_host_num of this ShowEventStatisticsResponse.

        **参数解释**: 存在告警的服务器数量 **取值范围**: 最小值0，最大值9223372036854775807 

        :return: The risky_host_num of this ShowEventStatisticsResponse.
        :rtype: int
        """
        return self._risky_host_num

    @risky_host_num.setter
    def risky_host_num(self, risky_host_num):
        r"""Sets the risky_host_num of this ShowEventStatisticsResponse.

        **参数解释**: 存在告警的服务器数量 **取值范围**: 最小值0，最大值9223372036854775807 

        :param risky_host_num: The risky_host_num of this ShowEventStatisticsResponse.
        :type risky_host_num: int
        """
        self._risky_host_num = risky_host_num

    @property
    def risky_container_num(self):
        r"""Gets the risky_container_num of this ShowEventStatisticsResponse.

        **参数解释**: 存在告警的容器数量 **取值范围**: 最小值0，最大值9223372036854775807 

        :return: The risky_container_num of this ShowEventStatisticsResponse.
        :rtype: int
        """
        return self._risky_container_num

    @risky_container_num.setter
    def risky_container_num(self, risky_container_num):
        r"""Sets the risky_container_num of this ShowEventStatisticsResponse.

        **参数解释**: 存在告警的容器数量 **取值范围**: 最小值0，最大值9223372036854775807 

        :param risky_container_num: The risky_container_num of this ShowEventStatisticsResponse.
        :type risky_container_num: int
        """
        self._risky_container_num = risky_container_num

    @property
    def unhandled_num(self):
        r"""Gets the unhandled_num of this ShowEventStatisticsResponse.

        **参数解释**: 待处理告警事件数量 **取值范围**: 最小值0，最大值9223372036854775807 

        :return: The unhandled_num of this ShowEventStatisticsResponse.
        :rtype: int
        """
        return self._unhandled_num

    @unhandled_num.setter
    def unhandled_num(self, unhandled_num):
        r"""Sets the unhandled_num of this ShowEventStatisticsResponse.

        **参数解释**: 待处理告警事件数量 **取值范围**: 最小值0，最大值9223372036854775807 

        :param unhandled_num: The unhandled_num of this ShowEventStatisticsResponse.
        :type unhandled_num: int
        """
        self._unhandled_num = unhandled_num

    @property
    def processed_num(self):
        r"""Gets the processed_num of this ShowEventStatisticsResponse.

        **参数解释**: 已处理告警事件数量 **取值范围**: 最小值0，最大值9223372036854775807 

        :return: The processed_num of this ShowEventStatisticsResponse.
        :rtype: int
        """
        return self._processed_num

    @processed_num.setter
    def processed_num(self, processed_num):
        r"""Sets the processed_num of this ShowEventStatisticsResponse.

        **参数解释**: 已处理告警事件数量 **取值范围**: 最小值0，最大值9223372036854775807 

        :param processed_num: The processed_num of this ShowEventStatisticsResponse.
        :type processed_num: int
        """
        self._processed_num = processed_num

    @property
    def auto_blocked_num(self):
        r"""Gets the auto_blocked_num of this ShowEventStatisticsResponse.

        **参数解释**: 自动处置告警事件数量 **取值范围**: 最小值0，最大值9223372036854775807 

        :return: The auto_blocked_num of this ShowEventStatisticsResponse.
        :rtype: int
        """
        return self._auto_blocked_num

    @auto_blocked_num.setter
    def auto_blocked_num(self, auto_blocked_num):
        r"""Sets the auto_blocked_num of this ShowEventStatisticsResponse.

        **参数解释**: 自动处置告警事件数量 **取值范围**: 最小值0，最大值9223372036854775807 

        :param auto_blocked_num: The auto_blocked_num of this ShowEventStatisticsResponse.
        :type auto_blocked_num: int
        """
        self._auto_blocked_num = auto_blocked_num

    @property
    def blocked_ip_num(self):
        r"""Gets the blocked_ip_num of this ShowEventStatisticsResponse.

        **参数解释**: 已拦截IP数量 **取值范围**: 最小值0，最大值9223372036854775807 

        :return: The blocked_ip_num of this ShowEventStatisticsResponse.
        :rtype: int
        """
        return self._blocked_ip_num

    @blocked_ip_num.setter
    def blocked_ip_num(self, blocked_ip_num):
        r"""Sets the blocked_ip_num of this ShowEventStatisticsResponse.

        **参数解释**: 已拦截IP数量 **取值范围**: 最小值0，最大值9223372036854775807 

        :param blocked_ip_num: The blocked_ip_num of this ShowEventStatisticsResponse.
        :type blocked_ip_num: int
        """
        self._blocked_ip_num = blocked_ip_num

    @property
    def isolated_file_num(self):
        r"""Gets the isolated_file_num of this ShowEventStatisticsResponse.

        **参数解释**: 已隔离文件数量 **取值范围**: 最小值0，最大值9223372036854775807 

        :return: The isolated_file_num of this ShowEventStatisticsResponse.
        :rtype: int
        """
        return self._isolated_file_num

    @isolated_file_num.setter
    def isolated_file_num(self, isolated_file_num):
        r"""Sets the isolated_file_num of this ShowEventStatisticsResponse.

        **参数解释**: 已隔离文件数量 **取值范围**: 最小值0，最大值9223372036854775807 

        :param isolated_file_num: The isolated_file_num of this ShowEventStatisticsResponse.
        :type isolated_file_num: int
        """
        self._isolated_file_num = isolated_file_num

    @property
    def support_es(self):
        r"""Gets the support_es of this ShowEventStatisticsResponse.

        **参数解释**: 是否支持ES查询 **取值范围**: - true：支持 - false：不支持 

        :return: The support_es of this ShowEventStatisticsResponse.
        :rtype: bool
        """
        return self._support_es

    @support_es.setter
    def support_es(self, support_es):
        r"""Sets the support_es of this ShowEventStatisticsResponse.

        **参数解释**: 是否支持ES查询 **取值范围**: - true：支持 - false：不支持 

        :param support_es: The support_es of this ShowEventStatisticsResponse.
        :type support_es: bool
        """
        self._support_es = support_es

    def to_dict(self):
        import warnings
        warnings.warn("ShowEventStatisticsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowEventStatisticsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
