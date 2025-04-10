# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DesktopPoolStatistics:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'desktop_pool_id': 'str',
        'desktop_pool_name': 'str',
        'total_num': 'int',
        'attach_statistics': 'AttachStatistics',
        'run_state_statistics': 'DesktopRunStatisticsRsp',
        'login_state_statistics': 'DesktopLoginStatisticsRsp'
    }

    attribute_map = {
        'desktop_pool_id': 'desktop_pool_id',
        'desktop_pool_name': 'desktop_pool_name',
        'total_num': 'total_num',
        'attach_statistics': 'attach_statistics',
        'run_state_statistics': 'run_state_statistics',
        'login_state_statistics': 'login_state_statistics'
    }

    def __init__(self, desktop_pool_id=None, desktop_pool_name=None, total_num=None, attach_statistics=None, run_state_statistics=None, login_state_statistics=None):
        r"""DesktopPoolStatistics

        The model defined in huaweicloud sdk

        :param desktop_pool_id: 桌面池id。
        :type desktop_pool_id: str
        :param desktop_pool_name: 桌面池名称。
        :type desktop_pool_name: str
        :param total_num: 桌面总数。
        :type total_num: int
        :param attach_statistics: 
        :type attach_statistics: :class:`huaweicloudsdkworkspace.v2.AttachStatistics`
        :param run_state_statistics: 
        :type run_state_statistics: :class:`huaweicloudsdkworkspace.v2.DesktopRunStatisticsRsp`
        :param login_state_statistics: 
        :type login_state_statistics: :class:`huaweicloudsdkworkspace.v2.DesktopLoginStatisticsRsp`
        """
        
        

        self._desktop_pool_id = None
        self._desktop_pool_name = None
        self._total_num = None
        self._attach_statistics = None
        self._run_state_statistics = None
        self._login_state_statistics = None
        self.discriminator = None

        if desktop_pool_id is not None:
            self.desktop_pool_id = desktop_pool_id
        if desktop_pool_name is not None:
            self.desktop_pool_name = desktop_pool_name
        if total_num is not None:
            self.total_num = total_num
        if attach_statistics is not None:
            self.attach_statistics = attach_statistics
        if run_state_statistics is not None:
            self.run_state_statistics = run_state_statistics
        if login_state_statistics is not None:
            self.login_state_statistics = login_state_statistics

    @property
    def desktop_pool_id(self):
        r"""Gets the desktop_pool_id of this DesktopPoolStatistics.

        桌面池id。

        :return: The desktop_pool_id of this DesktopPoolStatistics.
        :rtype: str
        """
        return self._desktop_pool_id

    @desktop_pool_id.setter
    def desktop_pool_id(self, desktop_pool_id):
        r"""Sets the desktop_pool_id of this DesktopPoolStatistics.

        桌面池id。

        :param desktop_pool_id: The desktop_pool_id of this DesktopPoolStatistics.
        :type desktop_pool_id: str
        """
        self._desktop_pool_id = desktop_pool_id

    @property
    def desktop_pool_name(self):
        r"""Gets the desktop_pool_name of this DesktopPoolStatistics.

        桌面池名称。

        :return: The desktop_pool_name of this DesktopPoolStatistics.
        :rtype: str
        """
        return self._desktop_pool_name

    @desktop_pool_name.setter
    def desktop_pool_name(self, desktop_pool_name):
        r"""Sets the desktop_pool_name of this DesktopPoolStatistics.

        桌面池名称。

        :param desktop_pool_name: The desktop_pool_name of this DesktopPoolStatistics.
        :type desktop_pool_name: str
        """
        self._desktop_pool_name = desktop_pool_name

    @property
    def total_num(self):
        r"""Gets the total_num of this DesktopPoolStatistics.

        桌面总数。

        :return: The total_num of this DesktopPoolStatistics.
        :rtype: int
        """
        return self._total_num

    @total_num.setter
    def total_num(self, total_num):
        r"""Sets the total_num of this DesktopPoolStatistics.

        桌面总数。

        :param total_num: The total_num of this DesktopPoolStatistics.
        :type total_num: int
        """
        self._total_num = total_num

    @property
    def attach_statistics(self):
        r"""Gets the attach_statistics of this DesktopPoolStatistics.

        :return: The attach_statistics of this DesktopPoolStatistics.
        :rtype: :class:`huaweicloudsdkworkspace.v2.AttachStatistics`
        """
        return self._attach_statistics

    @attach_statistics.setter
    def attach_statistics(self, attach_statistics):
        r"""Sets the attach_statistics of this DesktopPoolStatistics.

        :param attach_statistics: The attach_statistics of this DesktopPoolStatistics.
        :type attach_statistics: :class:`huaweicloudsdkworkspace.v2.AttachStatistics`
        """
        self._attach_statistics = attach_statistics

    @property
    def run_state_statistics(self):
        r"""Gets the run_state_statistics of this DesktopPoolStatistics.

        :return: The run_state_statistics of this DesktopPoolStatistics.
        :rtype: :class:`huaweicloudsdkworkspace.v2.DesktopRunStatisticsRsp`
        """
        return self._run_state_statistics

    @run_state_statistics.setter
    def run_state_statistics(self, run_state_statistics):
        r"""Sets the run_state_statistics of this DesktopPoolStatistics.

        :param run_state_statistics: The run_state_statistics of this DesktopPoolStatistics.
        :type run_state_statistics: :class:`huaweicloudsdkworkspace.v2.DesktopRunStatisticsRsp`
        """
        self._run_state_statistics = run_state_statistics

    @property
    def login_state_statistics(self):
        r"""Gets the login_state_statistics of this DesktopPoolStatistics.

        :return: The login_state_statistics of this DesktopPoolStatistics.
        :rtype: :class:`huaweicloudsdkworkspace.v2.DesktopLoginStatisticsRsp`
        """
        return self._login_state_statistics

    @login_state_statistics.setter
    def login_state_statistics(self, login_state_statistics):
        r"""Sets the login_state_statistics of this DesktopPoolStatistics.

        :param login_state_statistics: The login_state_statistics of this DesktopPoolStatistics.
        :type login_state_statistics: :class:`huaweicloudsdkworkspace.v2.DesktopLoginStatisticsRsp`
        """
        self._login_state_statistics = login_state_statistics

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
        if not isinstance(other, DesktopPoolStatistics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
