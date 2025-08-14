# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BlockedIpResponseInfo:

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
        'src_ip': 'str',
        'login_type': 'str',
        'intercept_num': 'int',
        'intercept_status': 'str',
        'block_time': 'int',
        'latest_time': 'int'
    }

    attribute_map = {
        'host_id': 'host_id',
        'host_name': 'host_name',
        'src_ip': 'src_ip',
        'login_type': 'login_type',
        'intercept_num': 'intercept_num',
        'intercept_status': 'intercept_status',
        'block_time': 'block_time',
        'latest_time': 'latest_time'
    }

    def __init__(self, host_id=None, host_name=None, src_ip=None, login_type=None, intercept_num=None, intercept_status=None, block_time=None, latest_time=None):
        r"""BlockedIpResponseInfo

        The model defined in huaweicloud sdk

        :param host_id: **参数解释**： 主机ID **取值范围**： 字符长度1-64位 
        :type host_id: str
        :param host_name: **参数解释**: 服务器名称 **取值范围**: 字符长度1-256位 
        :type host_name: str
        :param src_ip: 攻击源IP
        :type src_ip: str
        :param login_type: 登录类型，包含如下: - \&quot;mysql\&quot; # mysql服务 - \&quot;rdp\&quot; # rdp服务 - \&quot;ssh\&quot; # ssh服务 - \&quot;vsftp\&quot; # vsftp服务
        :type login_type: str
        :param intercept_num: 拦截次数
        :type intercept_num: int
        :param intercept_status: 拦截状态，包含如下:   - \&quot;intercepted\&quot; # 已拦截   - \&quot;canceled\&quot; # 已解除拦截   - \&quot;cancelling\&quot; # 待解除拦截
        :type intercept_status: str
        :param block_time: 开始拦截时间，毫秒
        :type block_time: int
        :param latest_time: 最近拦截时间，毫秒
        :type latest_time: int
        """
        
        

        self._host_id = None
        self._host_name = None
        self._src_ip = None
        self._login_type = None
        self._intercept_num = None
        self._intercept_status = None
        self._block_time = None
        self._latest_time = None
        self.discriminator = None

        self.host_id = host_id
        self.host_name = host_name
        self.src_ip = src_ip
        self.login_type = login_type
        self.intercept_num = intercept_num
        self.intercept_status = intercept_status
        self.block_time = block_time
        self.latest_time = latest_time

    @property
    def host_id(self):
        r"""Gets the host_id of this BlockedIpResponseInfo.

        **参数解释**： 主机ID **取值范围**： 字符长度1-64位 

        :return: The host_id of this BlockedIpResponseInfo.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this BlockedIpResponseInfo.

        **参数解释**： 主机ID **取值范围**： 字符长度1-64位 

        :param host_id: The host_id of this BlockedIpResponseInfo.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def host_name(self):
        r"""Gets the host_name of this BlockedIpResponseInfo.

        **参数解释**: 服务器名称 **取值范围**: 字符长度1-256位 

        :return: The host_name of this BlockedIpResponseInfo.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this BlockedIpResponseInfo.

        **参数解释**: 服务器名称 **取值范围**: 字符长度1-256位 

        :param host_name: The host_name of this BlockedIpResponseInfo.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def src_ip(self):
        r"""Gets the src_ip of this BlockedIpResponseInfo.

        攻击源IP

        :return: The src_ip of this BlockedIpResponseInfo.
        :rtype: str
        """
        return self._src_ip

    @src_ip.setter
    def src_ip(self, src_ip):
        r"""Sets the src_ip of this BlockedIpResponseInfo.

        攻击源IP

        :param src_ip: The src_ip of this BlockedIpResponseInfo.
        :type src_ip: str
        """
        self._src_ip = src_ip

    @property
    def login_type(self):
        r"""Gets the login_type of this BlockedIpResponseInfo.

        登录类型，包含如下: - \"mysql\" # mysql服务 - \"rdp\" # rdp服务 - \"ssh\" # ssh服务 - \"vsftp\" # vsftp服务

        :return: The login_type of this BlockedIpResponseInfo.
        :rtype: str
        """
        return self._login_type

    @login_type.setter
    def login_type(self, login_type):
        r"""Sets the login_type of this BlockedIpResponseInfo.

        登录类型，包含如下: - \"mysql\" # mysql服务 - \"rdp\" # rdp服务 - \"ssh\" # ssh服务 - \"vsftp\" # vsftp服务

        :param login_type: The login_type of this BlockedIpResponseInfo.
        :type login_type: str
        """
        self._login_type = login_type

    @property
    def intercept_num(self):
        r"""Gets the intercept_num of this BlockedIpResponseInfo.

        拦截次数

        :return: The intercept_num of this BlockedIpResponseInfo.
        :rtype: int
        """
        return self._intercept_num

    @intercept_num.setter
    def intercept_num(self, intercept_num):
        r"""Sets the intercept_num of this BlockedIpResponseInfo.

        拦截次数

        :param intercept_num: The intercept_num of this BlockedIpResponseInfo.
        :type intercept_num: int
        """
        self._intercept_num = intercept_num

    @property
    def intercept_status(self):
        r"""Gets the intercept_status of this BlockedIpResponseInfo.

        拦截状态，包含如下:   - \"intercepted\" # 已拦截   - \"canceled\" # 已解除拦截   - \"cancelling\" # 待解除拦截

        :return: The intercept_status of this BlockedIpResponseInfo.
        :rtype: str
        """
        return self._intercept_status

    @intercept_status.setter
    def intercept_status(self, intercept_status):
        r"""Sets the intercept_status of this BlockedIpResponseInfo.

        拦截状态，包含如下:   - \"intercepted\" # 已拦截   - \"canceled\" # 已解除拦截   - \"cancelling\" # 待解除拦截

        :param intercept_status: The intercept_status of this BlockedIpResponseInfo.
        :type intercept_status: str
        """
        self._intercept_status = intercept_status

    @property
    def block_time(self):
        r"""Gets the block_time of this BlockedIpResponseInfo.

        开始拦截时间，毫秒

        :return: The block_time of this BlockedIpResponseInfo.
        :rtype: int
        """
        return self._block_time

    @block_time.setter
    def block_time(self, block_time):
        r"""Sets the block_time of this BlockedIpResponseInfo.

        开始拦截时间，毫秒

        :param block_time: The block_time of this BlockedIpResponseInfo.
        :type block_time: int
        """
        self._block_time = block_time

    @property
    def latest_time(self):
        r"""Gets the latest_time of this BlockedIpResponseInfo.

        最近拦截时间，毫秒

        :return: The latest_time of this BlockedIpResponseInfo.
        :rtype: int
        """
        return self._latest_time

    @latest_time.setter
    def latest_time(self, latest_time):
        r"""Sets the latest_time of this BlockedIpResponseInfo.

        最近拦截时间，毫秒

        :param latest_time: The latest_time of this BlockedIpResponseInfo.
        :type latest_time: int
        """
        self._latest_time = latest_time

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
        if not isinstance(other, BlockedIpResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
