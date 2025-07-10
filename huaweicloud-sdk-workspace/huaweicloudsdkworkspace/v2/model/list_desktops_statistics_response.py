# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDesktopsStatisticsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_num': 'int',
        'attach_statistics': 'AttachStatistics',
        'run_state_statistics': 'DesktopRunStatisticsRsp',
        'login_state_statistics': 'DesktopLoginStatisticsRsp',
        'desktop_pool_statistics': 'list[DesktopPoolStatistics]'
    }

    attribute_map = {
        'total_num': 'total_num',
        'attach_statistics': 'attach_statistics',
        'run_state_statistics': 'run_state_statistics',
        'login_state_statistics': 'login_state_statistics',
        'desktop_pool_statistics': 'desktop_pool_statistics'
    }

    def __init__(self, total_num=None, attach_statistics=None, run_state_statistics=None, login_state_statistics=None, desktop_pool_statistics=None):
        r"""ListDesktopsStatisticsResponse

        The model defined in huaweicloud sdk

        :param total_num: 桌面总数。
        :type total_num: int
        :param attach_statistics: 
        :type attach_statistics: :class:`huaweicloudsdkworkspace.v2.AttachStatistics`
        :param run_state_statistics: 
        :type run_state_statistics: :class:`huaweicloudsdkworkspace.v2.DesktopRunStatisticsRsp`
        :param login_state_statistics: 
        :type login_state_statistics: :class:`huaweicloudsdkworkspace.v2.DesktopLoginStatisticsRsp`
        :param desktop_pool_statistics: 每个桌面池的情况统计，当desktop_type指定为POOL时返回。
        :type desktop_pool_statistics: list[:class:`huaweicloudsdkworkspace.v2.DesktopPoolStatistics`]
        """
        
        super(ListDesktopsStatisticsResponse, self).__init__()

        self._total_num = None
        self._attach_statistics = None
        self._run_state_statistics = None
        self._login_state_statistics = None
        self._desktop_pool_statistics = None
        self.discriminator = None

        if total_num is not None:
            self.total_num = total_num
        if attach_statistics is not None:
            self.attach_statistics = attach_statistics
        if run_state_statistics is not None:
            self.run_state_statistics = run_state_statistics
        if login_state_statistics is not None:
            self.login_state_statistics = login_state_statistics
        if desktop_pool_statistics is not None:
            self.desktop_pool_statistics = desktop_pool_statistics

    @property
    def total_num(self):
        r"""Gets the total_num of this ListDesktopsStatisticsResponse.

        桌面总数。

        :return: The total_num of this ListDesktopsStatisticsResponse.
        :rtype: int
        """
        return self._total_num

    @total_num.setter
    def total_num(self, total_num):
        r"""Sets the total_num of this ListDesktopsStatisticsResponse.

        桌面总数。

        :param total_num: The total_num of this ListDesktopsStatisticsResponse.
        :type total_num: int
        """
        self._total_num = total_num

    @property
    def attach_statistics(self):
        r"""Gets the attach_statistics of this ListDesktopsStatisticsResponse.

        :return: The attach_statistics of this ListDesktopsStatisticsResponse.
        :rtype: :class:`huaweicloudsdkworkspace.v2.AttachStatistics`
        """
        return self._attach_statistics

    @attach_statistics.setter
    def attach_statistics(self, attach_statistics):
        r"""Sets the attach_statistics of this ListDesktopsStatisticsResponse.

        :param attach_statistics: The attach_statistics of this ListDesktopsStatisticsResponse.
        :type attach_statistics: :class:`huaweicloudsdkworkspace.v2.AttachStatistics`
        """
        self._attach_statistics = attach_statistics

    @property
    def run_state_statistics(self):
        r"""Gets the run_state_statistics of this ListDesktopsStatisticsResponse.

        :return: The run_state_statistics of this ListDesktopsStatisticsResponse.
        :rtype: :class:`huaweicloudsdkworkspace.v2.DesktopRunStatisticsRsp`
        """
        return self._run_state_statistics

    @run_state_statistics.setter
    def run_state_statistics(self, run_state_statistics):
        r"""Sets the run_state_statistics of this ListDesktopsStatisticsResponse.

        :param run_state_statistics: The run_state_statistics of this ListDesktopsStatisticsResponse.
        :type run_state_statistics: :class:`huaweicloudsdkworkspace.v2.DesktopRunStatisticsRsp`
        """
        self._run_state_statistics = run_state_statistics

    @property
    def login_state_statistics(self):
        r"""Gets the login_state_statistics of this ListDesktopsStatisticsResponse.

        :return: The login_state_statistics of this ListDesktopsStatisticsResponse.
        :rtype: :class:`huaweicloudsdkworkspace.v2.DesktopLoginStatisticsRsp`
        """
        return self._login_state_statistics

    @login_state_statistics.setter
    def login_state_statistics(self, login_state_statistics):
        r"""Sets the login_state_statistics of this ListDesktopsStatisticsResponse.

        :param login_state_statistics: The login_state_statistics of this ListDesktopsStatisticsResponse.
        :type login_state_statistics: :class:`huaweicloudsdkworkspace.v2.DesktopLoginStatisticsRsp`
        """
        self._login_state_statistics = login_state_statistics

    @property
    def desktop_pool_statistics(self):
        r"""Gets the desktop_pool_statistics of this ListDesktopsStatisticsResponse.

        每个桌面池的情况统计，当desktop_type指定为POOL时返回。

        :return: The desktop_pool_statistics of this ListDesktopsStatisticsResponse.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.DesktopPoolStatistics`]
        """
        return self._desktop_pool_statistics

    @desktop_pool_statistics.setter
    def desktop_pool_statistics(self, desktop_pool_statistics):
        r"""Sets the desktop_pool_statistics of this ListDesktopsStatisticsResponse.

        每个桌面池的情况统计，当desktop_type指定为POOL时返回。

        :param desktop_pool_statistics: The desktop_pool_statistics of this ListDesktopsStatisticsResponse.
        :type desktop_pool_statistics: list[:class:`huaweicloudsdkworkspace.v2.DesktopPoolStatistics`]
        """
        self._desktop_pool_statistics = desktop_pool_statistics

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
        if not isinstance(other, ListDesktopsStatisticsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
