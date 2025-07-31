# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WebSiteHostInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'agent_id': 'str',
        'host_id': 'str',
        'host_name': 'str',
        'host_ip': 'str',
        'domain': 'str',
        'app_name': 'str',
        'path': 'str',
        'port': 'int',
        'bind_addr': 'str',
        'url_path': 'str',
        'uid': 'int',
        'gid': 'int',
        'mode': 'str',
        'pid': 'int',
        'proc_path': 'str',
        'is_https': 'bool',
        'cert_issuer': 'str',
        'cert_user': 'str',
        'cert_issue_time': 'str',
        'cert_expired_time': 'str',
        'record_time': 'int',
        'container_id': 'str',
        'container_name': 'str'
    }

    attribute_map = {
        'agent_id': 'agent_id',
        'host_id': 'host_id',
        'host_name': 'host_name',
        'host_ip': 'host_ip',
        'domain': 'domain',
        'app_name': 'app_name',
        'path': 'path',
        'port': 'port',
        'bind_addr': 'bind_addr',
        'url_path': 'url_path',
        'uid': 'uid',
        'gid': 'gid',
        'mode': 'mode',
        'pid': 'pid',
        'proc_path': 'proc_path',
        'is_https': 'is_https',
        'cert_issuer': 'cert_issuer',
        'cert_user': 'cert_user',
        'cert_issue_time': 'cert_issue_time',
        'cert_expired_time': 'cert_expired_time',
        'record_time': 'record_time',
        'container_id': 'container_id',
        'container_name': 'container_name'
    }

    def __init__(self, agent_id=None, host_id=None, host_name=None, host_ip=None, domain=None, app_name=None, path=None, port=None, bind_addr=None, url_path=None, uid=None, gid=None, mode=None, pid=None, proc_path=None, is_https=None, cert_issuer=None, cert_user=None, cert_issue_time=None, cert_expired_time=None, record_time=None, container_id=None, container_name=None):
        r"""WebSiteHostInfo

        The model defined in huaweicloud sdk

        :param agent_id: agent_id
        :type agent_id: str
        :param host_id: 主机id
        :type host_id: str
        :param host_name: 服务器名称
        :type host_name: str
        :param host_ip: 服务器ip
        :type host_ip: str
        :param domain: 域名
        :type domain: str
        :param app_name: 应用名称
        :type app_name: str
        :param path: 路径
        :type path: str
        :param port: 端口
        :type port: int
        :param bind_addr: 绑定地址
        :type bind_addr: str
        :param url_path: url路径
        :type url_path: str
        :param uid: 用户id
        :type uid: int
        :param gid: 用户组id
        :type gid: int
        :param mode: 文件权限
        :type mode: str
        :param pid: 进程id
        :type pid: int
        :param proc_path: 进程路径
        :type proc_path: str
        :param is_https: 是否是https
        :type is_https: bool
        :param cert_issuer: SSL证书颁发者
        :type cert_issuer: str
        :param cert_user: SSL证书使用者
        :type cert_user: str
        :param cert_issue_time: SSL证书颁发时间
        :type cert_issue_time: str
        :param cert_expired_time: SSL证书截止时间
        :type cert_expired_time: str
        :param record_time: 扫描时间
        :type record_time: int
        :param container_id: 容器id
        :type container_id: str
        :param container_name: 容器名称
        :type container_name: str
        """
        
        

        self._agent_id = None
        self._host_id = None
        self._host_name = None
        self._host_ip = None
        self._domain = None
        self._app_name = None
        self._path = None
        self._port = None
        self._bind_addr = None
        self._url_path = None
        self._uid = None
        self._gid = None
        self._mode = None
        self._pid = None
        self._proc_path = None
        self._is_https = None
        self._cert_issuer = None
        self._cert_user = None
        self._cert_issue_time = None
        self._cert_expired_time = None
        self._record_time = None
        self._container_id = None
        self._container_name = None
        self.discriminator = None

        if agent_id is not None:
            self.agent_id = agent_id
        if host_id is not None:
            self.host_id = host_id
        if host_name is not None:
            self.host_name = host_name
        if host_ip is not None:
            self.host_ip = host_ip
        if domain is not None:
            self.domain = domain
        if app_name is not None:
            self.app_name = app_name
        if path is not None:
            self.path = path
        if port is not None:
            self.port = port
        if bind_addr is not None:
            self.bind_addr = bind_addr
        if url_path is not None:
            self.url_path = url_path
        if uid is not None:
            self.uid = uid
        if gid is not None:
            self.gid = gid
        if mode is not None:
            self.mode = mode
        if pid is not None:
            self.pid = pid
        if proc_path is not None:
            self.proc_path = proc_path
        if is_https is not None:
            self.is_https = is_https
        if cert_issuer is not None:
            self.cert_issuer = cert_issuer
        if cert_user is not None:
            self.cert_user = cert_user
        if cert_issue_time is not None:
            self.cert_issue_time = cert_issue_time
        if cert_expired_time is not None:
            self.cert_expired_time = cert_expired_time
        if record_time is not None:
            self.record_time = record_time
        if container_id is not None:
            self.container_id = container_id
        if container_name is not None:
            self.container_name = container_name

    @property
    def agent_id(self):
        r"""Gets the agent_id of this WebSiteHostInfo.

        agent_id

        :return: The agent_id of this WebSiteHostInfo.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        r"""Sets the agent_id of this WebSiteHostInfo.

        agent_id

        :param agent_id: The agent_id of this WebSiteHostInfo.
        :type agent_id: str
        """
        self._agent_id = agent_id

    @property
    def host_id(self):
        r"""Gets the host_id of this WebSiteHostInfo.

        主机id

        :return: The host_id of this WebSiteHostInfo.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this WebSiteHostInfo.

        主机id

        :param host_id: The host_id of this WebSiteHostInfo.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def host_name(self):
        r"""Gets the host_name of this WebSiteHostInfo.

        服务器名称

        :return: The host_name of this WebSiteHostInfo.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this WebSiteHostInfo.

        服务器名称

        :param host_name: The host_name of this WebSiteHostInfo.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def host_ip(self):
        r"""Gets the host_ip of this WebSiteHostInfo.

        服务器ip

        :return: The host_ip of this WebSiteHostInfo.
        :rtype: str
        """
        return self._host_ip

    @host_ip.setter
    def host_ip(self, host_ip):
        r"""Sets the host_ip of this WebSiteHostInfo.

        服务器ip

        :param host_ip: The host_ip of this WebSiteHostInfo.
        :type host_ip: str
        """
        self._host_ip = host_ip

    @property
    def domain(self):
        r"""Gets the domain of this WebSiteHostInfo.

        域名

        :return: The domain of this WebSiteHostInfo.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        r"""Sets the domain of this WebSiteHostInfo.

        域名

        :param domain: The domain of this WebSiteHostInfo.
        :type domain: str
        """
        self._domain = domain

    @property
    def app_name(self):
        r"""Gets the app_name of this WebSiteHostInfo.

        应用名称

        :return: The app_name of this WebSiteHostInfo.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        r"""Sets the app_name of this WebSiteHostInfo.

        应用名称

        :param app_name: The app_name of this WebSiteHostInfo.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def path(self):
        r"""Gets the path of this WebSiteHostInfo.

        路径

        :return: The path of this WebSiteHostInfo.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        r"""Sets the path of this WebSiteHostInfo.

        路径

        :param path: The path of this WebSiteHostInfo.
        :type path: str
        """
        self._path = path

    @property
    def port(self):
        r"""Gets the port of this WebSiteHostInfo.

        端口

        :return: The port of this WebSiteHostInfo.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        r"""Sets the port of this WebSiteHostInfo.

        端口

        :param port: The port of this WebSiteHostInfo.
        :type port: int
        """
        self._port = port

    @property
    def bind_addr(self):
        r"""Gets the bind_addr of this WebSiteHostInfo.

        绑定地址

        :return: The bind_addr of this WebSiteHostInfo.
        :rtype: str
        """
        return self._bind_addr

    @bind_addr.setter
    def bind_addr(self, bind_addr):
        r"""Sets the bind_addr of this WebSiteHostInfo.

        绑定地址

        :param bind_addr: The bind_addr of this WebSiteHostInfo.
        :type bind_addr: str
        """
        self._bind_addr = bind_addr

    @property
    def url_path(self):
        r"""Gets the url_path of this WebSiteHostInfo.

        url路径

        :return: The url_path of this WebSiteHostInfo.
        :rtype: str
        """
        return self._url_path

    @url_path.setter
    def url_path(self, url_path):
        r"""Sets the url_path of this WebSiteHostInfo.

        url路径

        :param url_path: The url_path of this WebSiteHostInfo.
        :type url_path: str
        """
        self._url_path = url_path

    @property
    def uid(self):
        r"""Gets the uid of this WebSiteHostInfo.

        用户id

        :return: The uid of this WebSiteHostInfo.
        :rtype: int
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        r"""Sets the uid of this WebSiteHostInfo.

        用户id

        :param uid: The uid of this WebSiteHostInfo.
        :type uid: int
        """
        self._uid = uid

    @property
    def gid(self):
        r"""Gets the gid of this WebSiteHostInfo.

        用户组id

        :return: The gid of this WebSiteHostInfo.
        :rtype: int
        """
        return self._gid

    @gid.setter
    def gid(self, gid):
        r"""Sets the gid of this WebSiteHostInfo.

        用户组id

        :param gid: The gid of this WebSiteHostInfo.
        :type gid: int
        """
        self._gid = gid

    @property
    def mode(self):
        r"""Gets the mode of this WebSiteHostInfo.

        文件权限

        :return: The mode of this WebSiteHostInfo.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        r"""Sets the mode of this WebSiteHostInfo.

        文件权限

        :param mode: The mode of this WebSiteHostInfo.
        :type mode: str
        """
        self._mode = mode

    @property
    def pid(self):
        r"""Gets the pid of this WebSiteHostInfo.

        进程id

        :return: The pid of this WebSiteHostInfo.
        :rtype: int
        """
        return self._pid

    @pid.setter
    def pid(self, pid):
        r"""Sets the pid of this WebSiteHostInfo.

        进程id

        :param pid: The pid of this WebSiteHostInfo.
        :type pid: int
        """
        self._pid = pid

    @property
    def proc_path(self):
        r"""Gets the proc_path of this WebSiteHostInfo.

        进程路径

        :return: The proc_path of this WebSiteHostInfo.
        :rtype: str
        """
        return self._proc_path

    @proc_path.setter
    def proc_path(self, proc_path):
        r"""Sets the proc_path of this WebSiteHostInfo.

        进程路径

        :param proc_path: The proc_path of this WebSiteHostInfo.
        :type proc_path: str
        """
        self._proc_path = proc_path

    @property
    def is_https(self):
        r"""Gets the is_https of this WebSiteHostInfo.

        是否是https

        :return: The is_https of this WebSiteHostInfo.
        :rtype: bool
        """
        return self._is_https

    @is_https.setter
    def is_https(self, is_https):
        r"""Sets the is_https of this WebSiteHostInfo.

        是否是https

        :param is_https: The is_https of this WebSiteHostInfo.
        :type is_https: bool
        """
        self._is_https = is_https

    @property
    def cert_issuer(self):
        r"""Gets the cert_issuer of this WebSiteHostInfo.

        SSL证书颁发者

        :return: The cert_issuer of this WebSiteHostInfo.
        :rtype: str
        """
        return self._cert_issuer

    @cert_issuer.setter
    def cert_issuer(self, cert_issuer):
        r"""Sets the cert_issuer of this WebSiteHostInfo.

        SSL证书颁发者

        :param cert_issuer: The cert_issuer of this WebSiteHostInfo.
        :type cert_issuer: str
        """
        self._cert_issuer = cert_issuer

    @property
    def cert_user(self):
        r"""Gets the cert_user of this WebSiteHostInfo.

        SSL证书使用者

        :return: The cert_user of this WebSiteHostInfo.
        :rtype: str
        """
        return self._cert_user

    @cert_user.setter
    def cert_user(self, cert_user):
        r"""Sets the cert_user of this WebSiteHostInfo.

        SSL证书使用者

        :param cert_user: The cert_user of this WebSiteHostInfo.
        :type cert_user: str
        """
        self._cert_user = cert_user

    @property
    def cert_issue_time(self):
        r"""Gets the cert_issue_time of this WebSiteHostInfo.

        SSL证书颁发时间

        :return: The cert_issue_time of this WebSiteHostInfo.
        :rtype: str
        """
        return self._cert_issue_time

    @cert_issue_time.setter
    def cert_issue_time(self, cert_issue_time):
        r"""Sets the cert_issue_time of this WebSiteHostInfo.

        SSL证书颁发时间

        :param cert_issue_time: The cert_issue_time of this WebSiteHostInfo.
        :type cert_issue_time: str
        """
        self._cert_issue_time = cert_issue_time

    @property
    def cert_expired_time(self):
        r"""Gets the cert_expired_time of this WebSiteHostInfo.

        SSL证书截止时间

        :return: The cert_expired_time of this WebSiteHostInfo.
        :rtype: str
        """
        return self._cert_expired_time

    @cert_expired_time.setter
    def cert_expired_time(self, cert_expired_time):
        r"""Sets the cert_expired_time of this WebSiteHostInfo.

        SSL证书截止时间

        :param cert_expired_time: The cert_expired_time of this WebSiteHostInfo.
        :type cert_expired_time: str
        """
        self._cert_expired_time = cert_expired_time

    @property
    def record_time(self):
        r"""Gets the record_time of this WebSiteHostInfo.

        扫描时间

        :return: The record_time of this WebSiteHostInfo.
        :rtype: int
        """
        return self._record_time

    @record_time.setter
    def record_time(self, record_time):
        r"""Sets the record_time of this WebSiteHostInfo.

        扫描时间

        :param record_time: The record_time of this WebSiteHostInfo.
        :type record_time: int
        """
        self._record_time = record_time

    @property
    def container_id(self):
        r"""Gets the container_id of this WebSiteHostInfo.

        容器id

        :return: The container_id of this WebSiteHostInfo.
        :rtype: str
        """
        return self._container_id

    @container_id.setter
    def container_id(self, container_id):
        r"""Sets the container_id of this WebSiteHostInfo.

        容器id

        :param container_id: The container_id of this WebSiteHostInfo.
        :type container_id: str
        """
        self._container_id = container_id

    @property
    def container_name(self):
        r"""Gets the container_name of this WebSiteHostInfo.

        容器名称

        :return: The container_name of this WebSiteHostInfo.
        :rtype: str
        """
        return self._container_name

    @container_name.setter
    def container_name(self, container_name):
        r"""Sets the container_name of this WebSiteHostInfo.

        容器名称

        :param container_name: The container_name of this WebSiteHostInfo.
        :type container_name: str
        """
        self._container_name = container_name

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
        if not isinstance(other, WebSiteHostInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
