# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DesktopRunStatisticsRsp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'stop_num': 'int',
        'active_num': 'int',
        'error_num': 'int',
        'hibernated_num': 'int'
    }

    attribute_map = {
        'stop_num': 'stop_num',
        'active_num': 'active_num',
        'error_num': 'error_num',
        'hibernated_num': 'hibernated_num'
    }

    def __init__(self, stop_num=None, active_num=None, error_num=None, hibernated_num=None):
        r"""DesktopRunStatisticsRsp

        The model defined in huaweicloud sdk

        :param stop_num: 停止个数。
        :type stop_num: int
        :param active_num: 运行中个数。
        :type active_num: int
        :param error_num: 故障个数。
        :type error_num: int
        :param hibernated_num: 休眠个数。
        :type hibernated_num: int
        """
        
        

        self._stop_num = None
        self._active_num = None
        self._error_num = None
        self._hibernated_num = None
        self.discriminator = None

        self.stop_num = stop_num
        self.active_num = active_num
        self.error_num = error_num
        self.hibernated_num = hibernated_num

    @property
    def stop_num(self):
        r"""Gets the stop_num of this DesktopRunStatisticsRsp.

        停止个数。

        :return: The stop_num of this DesktopRunStatisticsRsp.
        :rtype: int
        """
        return self._stop_num

    @stop_num.setter
    def stop_num(self, stop_num):
        r"""Sets the stop_num of this DesktopRunStatisticsRsp.

        停止个数。

        :param stop_num: The stop_num of this DesktopRunStatisticsRsp.
        :type stop_num: int
        """
        self._stop_num = stop_num

    @property
    def active_num(self):
        r"""Gets the active_num of this DesktopRunStatisticsRsp.

        运行中个数。

        :return: The active_num of this DesktopRunStatisticsRsp.
        :rtype: int
        """
        return self._active_num

    @active_num.setter
    def active_num(self, active_num):
        r"""Sets the active_num of this DesktopRunStatisticsRsp.

        运行中个数。

        :param active_num: The active_num of this DesktopRunStatisticsRsp.
        :type active_num: int
        """
        self._active_num = active_num

    @property
    def error_num(self):
        r"""Gets the error_num of this DesktopRunStatisticsRsp.

        故障个数。

        :return: The error_num of this DesktopRunStatisticsRsp.
        :rtype: int
        """
        return self._error_num

    @error_num.setter
    def error_num(self, error_num):
        r"""Sets the error_num of this DesktopRunStatisticsRsp.

        故障个数。

        :param error_num: The error_num of this DesktopRunStatisticsRsp.
        :type error_num: int
        """
        self._error_num = error_num

    @property
    def hibernated_num(self):
        r"""Gets the hibernated_num of this DesktopRunStatisticsRsp.

        休眠个数。

        :return: The hibernated_num of this DesktopRunStatisticsRsp.
        :rtype: int
        """
        return self._hibernated_num

    @hibernated_num.setter
    def hibernated_num(self, hibernated_num):
        r"""Sets the hibernated_num of this DesktopRunStatisticsRsp.

        休眠个数。

        :param hibernated_num: The hibernated_num of this DesktopRunStatisticsRsp.
        :type hibernated_num: int
        """
        self._hibernated_num = hibernated_num

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
        if not isinstance(other, DesktopRunStatisticsRsp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
