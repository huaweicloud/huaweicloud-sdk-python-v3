# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LoginWhiteIpResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enabled': 'bool',
        'white_ip': 'str',
        'total_num': 'int',
        'host_id_list': 'list[str]'
    }

    attribute_map = {
        'enabled': 'enabled',
        'white_ip': 'white_ip',
        'total_num': 'total_num',
        'host_id_list': 'host_id_list'
    }

    def __init__(self, enabled=None, white_ip=None, total_num=None, host_id_list=None):
        r"""LoginWhiteIpResponseInfo

        The model defined in huaweicloud sdk

        :param enabled: 白名单启用状态，包含如下：   - true：已启用   - false：已禁用
        :type enabled: bool
        :param white_ip: 白名单IP或IP网段，IP网段由IP地址和掩码组成，以‘/’连接。
        :type white_ip: str
        :param total_num: 服务器ID总数
        :type total_num: int
        :param host_id_list: 服务器ID列表
        :type host_id_list: list[str]
        """
        
        

        self._enabled = None
        self._white_ip = None
        self._total_num = None
        self._host_id_list = None
        self.discriminator = None

        if enabled is not None:
            self.enabled = enabled
        if white_ip is not None:
            self.white_ip = white_ip
        if total_num is not None:
            self.total_num = total_num
        if host_id_list is not None:
            self.host_id_list = host_id_list

    @property
    def enabled(self):
        r"""Gets the enabled of this LoginWhiteIpResponseInfo.

        白名单启用状态，包含如下：   - true：已启用   - false：已禁用

        :return: The enabled of this LoginWhiteIpResponseInfo.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this LoginWhiteIpResponseInfo.

        白名单启用状态，包含如下：   - true：已启用   - false：已禁用

        :param enabled: The enabled of this LoginWhiteIpResponseInfo.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def white_ip(self):
        r"""Gets the white_ip of this LoginWhiteIpResponseInfo.

        白名单IP或IP网段，IP网段由IP地址和掩码组成，以‘/’连接。

        :return: The white_ip of this LoginWhiteIpResponseInfo.
        :rtype: str
        """
        return self._white_ip

    @white_ip.setter
    def white_ip(self, white_ip):
        r"""Sets the white_ip of this LoginWhiteIpResponseInfo.

        白名单IP或IP网段，IP网段由IP地址和掩码组成，以‘/’连接。

        :param white_ip: The white_ip of this LoginWhiteIpResponseInfo.
        :type white_ip: str
        """
        self._white_ip = white_ip

    @property
    def total_num(self):
        r"""Gets the total_num of this LoginWhiteIpResponseInfo.

        服务器ID总数

        :return: The total_num of this LoginWhiteIpResponseInfo.
        :rtype: int
        """
        return self._total_num

    @total_num.setter
    def total_num(self, total_num):
        r"""Sets the total_num of this LoginWhiteIpResponseInfo.

        服务器ID总数

        :param total_num: The total_num of this LoginWhiteIpResponseInfo.
        :type total_num: int
        """
        self._total_num = total_num

    @property
    def host_id_list(self):
        r"""Gets the host_id_list of this LoginWhiteIpResponseInfo.

        服务器ID列表

        :return: The host_id_list of this LoginWhiteIpResponseInfo.
        :rtype: list[str]
        """
        return self._host_id_list

    @host_id_list.setter
    def host_id_list(self, host_id_list):
        r"""Sets the host_id_list of this LoginWhiteIpResponseInfo.

        服务器ID列表

        :param host_id_list: The host_id_list of this LoginWhiteIpResponseInfo.
        :type host_id_list: list[str]
        """
        self._host_id_list = host_id_list

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
        if not isinstance(other, LoginWhiteIpResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
