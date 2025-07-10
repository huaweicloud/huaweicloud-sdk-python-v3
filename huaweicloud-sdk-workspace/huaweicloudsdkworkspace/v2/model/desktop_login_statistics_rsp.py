# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DesktopLoginStatisticsRsp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'in_use_num': 'int',
        'unregistered_num': 'int',
        'unable_to_connect_num': 'int',
        'ready_num': 'int',
        'disconnected_num': 'int'
    }

    attribute_map = {
        'in_use_num': 'in_use_num',
        'unregistered_num': 'unregistered_num',
        'unable_to_connect_num': 'unable_to_connect_num',
        'ready_num': 'ready_num',
        'disconnected_num': 'disconnected_num'
    }

    def __init__(self, in_use_num=None, unregistered_num=None, unable_to_connect_num=None, ready_num=None, disconnected_num=None):
        r"""DesktopLoginStatisticsRsp

        The model defined in huaweicloud sdk

        :param in_use_num: 使用中。
        :type in_use_num: int
        :param unregistered_num: 未注册数目。
        :type unregistered_num: int
        :param unable_to_connect_num: 未注册数目。
        :type unable_to_connect_num: int
        :param ready_num: 空闲数目。
        :type ready_num: int
        :param disconnected_num: 断开连接数目。
        :type disconnected_num: int
        """
        
        

        self._in_use_num = None
        self._unregistered_num = None
        self._unable_to_connect_num = None
        self._ready_num = None
        self._disconnected_num = None
        self.discriminator = None

        self.in_use_num = in_use_num
        self.unregistered_num = unregistered_num
        if unable_to_connect_num is not None:
            self.unable_to_connect_num = unable_to_connect_num
        self.ready_num = ready_num
        self.disconnected_num = disconnected_num

    @property
    def in_use_num(self):
        r"""Gets the in_use_num of this DesktopLoginStatisticsRsp.

        使用中。

        :return: The in_use_num of this DesktopLoginStatisticsRsp.
        :rtype: int
        """
        return self._in_use_num

    @in_use_num.setter
    def in_use_num(self, in_use_num):
        r"""Sets the in_use_num of this DesktopLoginStatisticsRsp.

        使用中。

        :param in_use_num: The in_use_num of this DesktopLoginStatisticsRsp.
        :type in_use_num: int
        """
        self._in_use_num = in_use_num

    @property
    def unregistered_num(self):
        r"""Gets the unregistered_num of this DesktopLoginStatisticsRsp.

        未注册数目。

        :return: The unregistered_num of this DesktopLoginStatisticsRsp.
        :rtype: int
        """
        return self._unregistered_num

    @unregistered_num.setter
    def unregistered_num(self, unregistered_num):
        r"""Sets the unregistered_num of this DesktopLoginStatisticsRsp.

        未注册数目。

        :param unregistered_num: The unregistered_num of this DesktopLoginStatisticsRsp.
        :type unregistered_num: int
        """
        self._unregistered_num = unregistered_num

    @property
    def unable_to_connect_num(self):
        r"""Gets the unable_to_connect_num of this DesktopLoginStatisticsRsp.

        未注册数目。

        :return: The unable_to_connect_num of this DesktopLoginStatisticsRsp.
        :rtype: int
        """
        return self._unable_to_connect_num

    @unable_to_connect_num.setter
    def unable_to_connect_num(self, unable_to_connect_num):
        r"""Sets the unable_to_connect_num of this DesktopLoginStatisticsRsp.

        未注册数目。

        :param unable_to_connect_num: The unable_to_connect_num of this DesktopLoginStatisticsRsp.
        :type unable_to_connect_num: int
        """
        self._unable_to_connect_num = unable_to_connect_num

    @property
    def ready_num(self):
        r"""Gets the ready_num of this DesktopLoginStatisticsRsp.

        空闲数目。

        :return: The ready_num of this DesktopLoginStatisticsRsp.
        :rtype: int
        """
        return self._ready_num

    @ready_num.setter
    def ready_num(self, ready_num):
        r"""Sets the ready_num of this DesktopLoginStatisticsRsp.

        空闲数目。

        :param ready_num: The ready_num of this DesktopLoginStatisticsRsp.
        :type ready_num: int
        """
        self._ready_num = ready_num

    @property
    def disconnected_num(self):
        r"""Gets the disconnected_num of this DesktopLoginStatisticsRsp.

        断开连接数目。

        :return: The disconnected_num of this DesktopLoginStatisticsRsp.
        :rtype: int
        """
        return self._disconnected_num

    @disconnected_num.setter
    def disconnected_num(self, disconnected_num):
        r"""Sets the disconnected_num of this DesktopLoginStatisticsRsp.

        断开连接数目。

        :param disconnected_num: The disconnected_num of this DesktopLoginStatisticsRsp.
        :type disconnected_num: int
        """
        self._disconnected_num = disconnected_num

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
        if not isinstance(other, DesktopLoginStatisticsRsp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
