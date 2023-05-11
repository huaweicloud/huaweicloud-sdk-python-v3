# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SecurityCheckHostInfoResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'host_id': 'str',
        'host_name': 'str',
        'host_public_ip': 'str',
        'host_private_ip': 'str',
        'scan_time': 'int',
        'failed_num': 'int',
        'passed_num': 'int'
    }

    attribute_map = {
        'host_id': 'host_id',
        'host_name': 'host_name',
        'host_public_ip': 'host_public_ip',
        'host_private_ip': 'host_private_ip',
        'scan_time': 'scan_time',
        'failed_num': 'failed_num',
        'passed_num': 'passed_num'
    }

    def __init__(self, host_id=None, host_name=None, host_public_ip=None, host_private_ip=None, scan_time=None, failed_num=None, passed_num=None):
        """SecurityCheckHostInfoResponseInfo

        The model defined in huaweicloud sdk

        :param host_id: 服务器ID
        :type host_id: str
        :param host_name: 服务器名称
        :type host_name: str
        :param host_public_ip: 服务器公网IP
        :type host_public_ip: str
        :param host_private_ip: 服务器私网IP
        :type host_private_ip: str
        :param scan_time: 扫描时间
        :type scan_time: int
        :param failed_num: 风险项数量
        :type failed_num: int
        :param passed_num: 通过项数量
        :type passed_num: int
        """
        
        

        self._host_id = None
        self._host_name = None
        self._host_public_ip = None
        self._host_private_ip = None
        self._scan_time = None
        self._failed_num = None
        self._passed_num = None
        self.discriminator = None

        if host_id is not None:
            self.host_id = host_id
        if host_name is not None:
            self.host_name = host_name
        if host_public_ip is not None:
            self.host_public_ip = host_public_ip
        if host_private_ip is not None:
            self.host_private_ip = host_private_ip
        if scan_time is not None:
            self.scan_time = scan_time
        if failed_num is not None:
            self.failed_num = failed_num
        if passed_num is not None:
            self.passed_num = passed_num

    @property
    def host_id(self):
        """Gets the host_id of this SecurityCheckHostInfoResponseInfo.

        服务器ID

        :return: The host_id of this SecurityCheckHostInfoResponseInfo.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        """Sets the host_id of this SecurityCheckHostInfoResponseInfo.

        服务器ID

        :param host_id: The host_id of this SecurityCheckHostInfoResponseInfo.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def host_name(self):
        """Gets the host_name of this SecurityCheckHostInfoResponseInfo.

        服务器名称

        :return: The host_name of this SecurityCheckHostInfoResponseInfo.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """Sets the host_name of this SecurityCheckHostInfoResponseInfo.

        服务器名称

        :param host_name: The host_name of this SecurityCheckHostInfoResponseInfo.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def host_public_ip(self):
        """Gets the host_public_ip of this SecurityCheckHostInfoResponseInfo.

        服务器公网IP

        :return: The host_public_ip of this SecurityCheckHostInfoResponseInfo.
        :rtype: str
        """
        return self._host_public_ip

    @host_public_ip.setter
    def host_public_ip(self, host_public_ip):
        """Sets the host_public_ip of this SecurityCheckHostInfoResponseInfo.

        服务器公网IP

        :param host_public_ip: The host_public_ip of this SecurityCheckHostInfoResponseInfo.
        :type host_public_ip: str
        """
        self._host_public_ip = host_public_ip

    @property
    def host_private_ip(self):
        """Gets the host_private_ip of this SecurityCheckHostInfoResponseInfo.

        服务器私网IP

        :return: The host_private_ip of this SecurityCheckHostInfoResponseInfo.
        :rtype: str
        """
        return self._host_private_ip

    @host_private_ip.setter
    def host_private_ip(self, host_private_ip):
        """Sets the host_private_ip of this SecurityCheckHostInfoResponseInfo.

        服务器私网IP

        :param host_private_ip: The host_private_ip of this SecurityCheckHostInfoResponseInfo.
        :type host_private_ip: str
        """
        self._host_private_ip = host_private_ip

    @property
    def scan_time(self):
        """Gets the scan_time of this SecurityCheckHostInfoResponseInfo.

        扫描时间

        :return: The scan_time of this SecurityCheckHostInfoResponseInfo.
        :rtype: int
        """
        return self._scan_time

    @scan_time.setter
    def scan_time(self, scan_time):
        """Sets the scan_time of this SecurityCheckHostInfoResponseInfo.

        扫描时间

        :param scan_time: The scan_time of this SecurityCheckHostInfoResponseInfo.
        :type scan_time: int
        """
        self._scan_time = scan_time

    @property
    def failed_num(self):
        """Gets the failed_num of this SecurityCheckHostInfoResponseInfo.

        风险项数量

        :return: The failed_num of this SecurityCheckHostInfoResponseInfo.
        :rtype: int
        """
        return self._failed_num

    @failed_num.setter
    def failed_num(self, failed_num):
        """Sets the failed_num of this SecurityCheckHostInfoResponseInfo.

        风险项数量

        :param failed_num: The failed_num of this SecurityCheckHostInfoResponseInfo.
        :type failed_num: int
        """
        self._failed_num = failed_num

    @property
    def passed_num(self):
        """Gets the passed_num of this SecurityCheckHostInfoResponseInfo.

        通过项数量

        :return: The passed_num of this SecurityCheckHostInfoResponseInfo.
        :rtype: int
        """
        return self._passed_num

    @passed_num.setter
    def passed_num(self, passed_num):
        """Sets the passed_num of this SecurityCheckHostInfoResponseInfo.

        通过项数量

        :param passed_num: The passed_num of this SecurityCheckHostInfoResponseInfo.
        :type passed_num: int
        """
        self._passed_num = passed_num

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
        if not isinstance(other, SecurityCheckHostInfoResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
