# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WebSiteInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
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
        'cert_user': 'int',
        'cert_issue_time': 'str',
        'cert_expired_time': 'str',
        'record_time': 'int',
        'container_id': 'str',
        'container_name': 'str'
    }

    attribute_map = {
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

    def __init__(self, domain=None, app_name=None, path=None, port=None, bind_addr=None, url_path=None, uid=None, gid=None, mode=None, pid=None, proc_path=None, is_https=None, cert_issuer=None, cert_user=None, cert_issue_time=None, cert_expired_time=None, record_time=None, container_id=None, container_name=None):
        r"""WebSiteInfo

        The model defined in huaweicloud sdk

        :param domain: **参数解释**: 域名 **取值范围**: 字符长度1-256 
        :type domain: str
        :param app_name: **参数解释**: 软件名称 **取值范围**: 字符长度1-256 
        :type app_name: str
        :param path: **参数解释**: web目录路径 **取值范围**: 字符长度1-512 
        :type path: str
        :param port: **参数解释**: web站点对外端口 **取值范围**: 最小值0，最大值2147483647 
        :type port: int
        :param bind_addr: **参数解释**: web站点绑定IP **取值范围**: 字符长度1-512 
        :type bind_addr: str
        :param url_path: **参数解释**: web站点url路径 **取值范围**: 字符长度1-128 
        :type url_path: str
        :param uid: **参数解释**: web站点进程uid **取值范围**: 最小值0，最大值2147483647 
        :type uid: int
        :param gid: **参数解释**: web站点进程gid **取值范围**: 最小值0，最大值2147483647 
        :type gid: int
        :param mode: **参数解释**: web站点文件权限 **取值范围**: 字符长度1-32 
        :type mode: str
        :param pid: **参数解释**: web站点进程pid **取值范围**: 最小值0，最大值2147483647 
        :type pid: int
        :param proc_path: **参数解释**: web站点进程路径 **取值范围**: 字符长度1-1024 
        :type proc_path: str
        :param is_https: **参数解释**: web站点是否为https **取值范围**: -true：是。 -false：否。 
        :type is_https: bool
        :param cert_issuer: **参数解释**: web站点SSL证书颁发者 **取值范围**: 字符长度0-256 
        :type cert_issuer: str
        :param cert_user: **参数解释**: web站点SSL证书使用者 **取值范围**: 字符长度0-256 
        :type cert_user: int
        :param cert_issue_time: **参数解释**: web站点SSL证书颁发时间 **取值范围**: 字符长度0-32 
        :type cert_issue_time: str
        :param cert_expired_time: **参数解释**: web站点SSL证书截止时间 **取值范围**: 字符长度0-32 
        :type cert_expired_time: str
        :param record_time: **参数解释**: web框架扫描时间 **取值范围**: 最小值0，最大值2^63-1 
        :type record_time: int
        :param container_id: **参数解释**: 容器id **取值范围**: 字符长度1-128 
        :type container_id: str
        :param container_name: **参数解释**: 容器名称 **取值范围**: 字符长度1-256 
        :type container_name: str
        """
        
        

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
    def domain(self):
        r"""Gets the domain of this WebSiteInfo.

        **参数解释**: 域名 **取值范围**: 字符长度1-256 

        :return: The domain of this WebSiteInfo.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        r"""Sets the domain of this WebSiteInfo.

        **参数解释**: 域名 **取值范围**: 字符长度1-256 

        :param domain: The domain of this WebSiteInfo.
        :type domain: str
        """
        self._domain = domain

    @property
    def app_name(self):
        r"""Gets the app_name of this WebSiteInfo.

        **参数解释**: 软件名称 **取值范围**: 字符长度1-256 

        :return: The app_name of this WebSiteInfo.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        r"""Sets the app_name of this WebSiteInfo.

        **参数解释**: 软件名称 **取值范围**: 字符长度1-256 

        :param app_name: The app_name of this WebSiteInfo.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def path(self):
        r"""Gets the path of this WebSiteInfo.

        **参数解释**: web目录路径 **取值范围**: 字符长度1-512 

        :return: The path of this WebSiteInfo.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        r"""Sets the path of this WebSiteInfo.

        **参数解释**: web目录路径 **取值范围**: 字符长度1-512 

        :param path: The path of this WebSiteInfo.
        :type path: str
        """
        self._path = path

    @property
    def port(self):
        r"""Gets the port of this WebSiteInfo.

        **参数解释**: web站点对外端口 **取值范围**: 最小值0，最大值2147483647 

        :return: The port of this WebSiteInfo.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        r"""Sets the port of this WebSiteInfo.

        **参数解释**: web站点对外端口 **取值范围**: 最小值0，最大值2147483647 

        :param port: The port of this WebSiteInfo.
        :type port: int
        """
        self._port = port

    @property
    def bind_addr(self):
        r"""Gets the bind_addr of this WebSiteInfo.

        **参数解释**: web站点绑定IP **取值范围**: 字符长度1-512 

        :return: The bind_addr of this WebSiteInfo.
        :rtype: str
        """
        return self._bind_addr

    @bind_addr.setter
    def bind_addr(self, bind_addr):
        r"""Sets the bind_addr of this WebSiteInfo.

        **参数解释**: web站点绑定IP **取值范围**: 字符长度1-512 

        :param bind_addr: The bind_addr of this WebSiteInfo.
        :type bind_addr: str
        """
        self._bind_addr = bind_addr

    @property
    def url_path(self):
        r"""Gets the url_path of this WebSiteInfo.

        **参数解释**: web站点url路径 **取值范围**: 字符长度1-128 

        :return: The url_path of this WebSiteInfo.
        :rtype: str
        """
        return self._url_path

    @url_path.setter
    def url_path(self, url_path):
        r"""Sets the url_path of this WebSiteInfo.

        **参数解释**: web站点url路径 **取值范围**: 字符长度1-128 

        :param url_path: The url_path of this WebSiteInfo.
        :type url_path: str
        """
        self._url_path = url_path

    @property
    def uid(self):
        r"""Gets the uid of this WebSiteInfo.

        **参数解释**: web站点进程uid **取值范围**: 最小值0，最大值2147483647 

        :return: The uid of this WebSiteInfo.
        :rtype: int
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        r"""Sets the uid of this WebSiteInfo.

        **参数解释**: web站点进程uid **取值范围**: 最小值0，最大值2147483647 

        :param uid: The uid of this WebSiteInfo.
        :type uid: int
        """
        self._uid = uid

    @property
    def gid(self):
        r"""Gets the gid of this WebSiteInfo.

        **参数解释**: web站点进程gid **取值范围**: 最小值0，最大值2147483647 

        :return: The gid of this WebSiteInfo.
        :rtype: int
        """
        return self._gid

    @gid.setter
    def gid(self, gid):
        r"""Sets the gid of this WebSiteInfo.

        **参数解释**: web站点进程gid **取值范围**: 最小值0，最大值2147483647 

        :param gid: The gid of this WebSiteInfo.
        :type gid: int
        """
        self._gid = gid

    @property
    def mode(self):
        r"""Gets the mode of this WebSiteInfo.

        **参数解释**: web站点文件权限 **取值范围**: 字符长度1-32 

        :return: The mode of this WebSiteInfo.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        r"""Sets the mode of this WebSiteInfo.

        **参数解释**: web站点文件权限 **取值范围**: 字符长度1-32 

        :param mode: The mode of this WebSiteInfo.
        :type mode: str
        """
        self._mode = mode

    @property
    def pid(self):
        r"""Gets the pid of this WebSiteInfo.

        **参数解释**: web站点进程pid **取值范围**: 最小值0，最大值2147483647 

        :return: The pid of this WebSiteInfo.
        :rtype: int
        """
        return self._pid

    @pid.setter
    def pid(self, pid):
        r"""Sets the pid of this WebSiteInfo.

        **参数解释**: web站点进程pid **取值范围**: 最小值0，最大值2147483647 

        :param pid: The pid of this WebSiteInfo.
        :type pid: int
        """
        self._pid = pid

    @property
    def proc_path(self):
        r"""Gets the proc_path of this WebSiteInfo.

        **参数解释**: web站点进程路径 **取值范围**: 字符长度1-1024 

        :return: The proc_path of this WebSiteInfo.
        :rtype: str
        """
        return self._proc_path

    @proc_path.setter
    def proc_path(self, proc_path):
        r"""Sets the proc_path of this WebSiteInfo.

        **参数解释**: web站点进程路径 **取值范围**: 字符长度1-1024 

        :param proc_path: The proc_path of this WebSiteInfo.
        :type proc_path: str
        """
        self._proc_path = proc_path

    @property
    def is_https(self):
        r"""Gets the is_https of this WebSiteInfo.

        **参数解释**: web站点是否为https **取值范围**: -true：是。 -false：否。 

        :return: The is_https of this WebSiteInfo.
        :rtype: bool
        """
        return self._is_https

    @is_https.setter
    def is_https(self, is_https):
        r"""Sets the is_https of this WebSiteInfo.

        **参数解释**: web站点是否为https **取值范围**: -true：是。 -false：否。 

        :param is_https: The is_https of this WebSiteInfo.
        :type is_https: bool
        """
        self._is_https = is_https

    @property
    def cert_issuer(self):
        r"""Gets the cert_issuer of this WebSiteInfo.

        **参数解释**: web站点SSL证书颁发者 **取值范围**: 字符长度0-256 

        :return: The cert_issuer of this WebSiteInfo.
        :rtype: str
        """
        return self._cert_issuer

    @cert_issuer.setter
    def cert_issuer(self, cert_issuer):
        r"""Sets the cert_issuer of this WebSiteInfo.

        **参数解释**: web站点SSL证书颁发者 **取值范围**: 字符长度0-256 

        :param cert_issuer: The cert_issuer of this WebSiteInfo.
        :type cert_issuer: str
        """
        self._cert_issuer = cert_issuer

    @property
    def cert_user(self):
        r"""Gets the cert_user of this WebSiteInfo.

        **参数解释**: web站点SSL证书使用者 **取值范围**: 字符长度0-256 

        :return: The cert_user of this WebSiteInfo.
        :rtype: int
        """
        return self._cert_user

    @cert_user.setter
    def cert_user(self, cert_user):
        r"""Sets the cert_user of this WebSiteInfo.

        **参数解释**: web站点SSL证书使用者 **取值范围**: 字符长度0-256 

        :param cert_user: The cert_user of this WebSiteInfo.
        :type cert_user: int
        """
        self._cert_user = cert_user

    @property
    def cert_issue_time(self):
        r"""Gets the cert_issue_time of this WebSiteInfo.

        **参数解释**: web站点SSL证书颁发时间 **取值范围**: 字符长度0-32 

        :return: The cert_issue_time of this WebSiteInfo.
        :rtype: str
        """
        return self._cert_issue_time

    @cert_issue_time.setter
    def cert_issue_time(self, cert_issue_time):
        r"""Sets the cert_issue_time of this WebSiteInfo.

        **参数解释**: web站点SSL证书颁发时间 **取值范围**: 字符长度0-32 

        :param cert_issue_time: The cert_issue_time of this WebSiteInfo.
        :type cert_issue_time: str
        """
        self._cert_issue_time = cert_issue_time

    @property
    def cert_expired_time(self):
        r"""Gets the cert_expired_time of this WebSiteInfo.

        **参数解释**: web站点SSL证书截止时间 **取值范围**: 字符长度0-32 

        :return: The cert_expired_time of this WebSiteInfo.
        :rtype: str
        """
        return self._cert_expired_time

    @cert_expired_time.setter
    def cert_expired_time(self, cert_expired_time):
        r"""Sets the cert_expired_time of this WebSiteInfo.

        **参数解释**: web站点SSL证书截止时间 **取值范围**: 字符长度0-32 

        :param cert_expired_time: The cert_expired_time of this WebSiteInfo.
        :type cert_expired_time: str
        """
        self._cert_expired_time = cert_expired_time

    @property
    def record_time(self):
        r"""Gets the record_time of this WebSiteInfo.

        **参数解释**: web框架扫描时间 **取值范围**: 最小值0，最大值2^63-1 

        :return: The record_time of this WebSiteInfo.
        :rtype: int
        """
        return self._record_time

    @record_time.setter
    def record_time(self, record_time):
        r"""Sets the record_time of this WebSiteInfo.

        **参数解释**: web框架扫描时间 **取值范围**: 最小值0，最大值2^63-1 

        :param record_time: The record_time of this WebSiteInfo.
        :type record_time: int
        """
        self._record_time = record_time

    @property
    def container_id(self):
        r"""Gets the container_id of this WebSiteInfo.

        **参数解释**: 容器id **取值范围**: 字符长度1-128 

        :return: The container_id of this WebSiteInfo.
        :rtype: str
        """
        return self._container_id

    @container_id.setter
    def container_id(self, container_id):
        r"""Sets the container_id of this WebSiteInfo.

        **参数解释**: 容器id **取值范围**: 字符长度1-128 

        :param container_id: The container_id of this WebSiteInfo.
        :type container_id: str
        """
        self._container_id = container_id

    @property
    def container_name(self):
        r"""Gets the container_name of this WebSiteInfo.

        **参数解释**: 容器名称 **取值范围**: 字符长度1-256 

        :return: The container_name of this WebSiteInfo.
        :rtype: str
        """
        return self._container_name

    @container_name.setter
    def container_name(self, container_name):
        r"""Sets the container_name of this WebSiteInfo.

        **参数解释**: 容器名称 **取值范围**: 字符长度1-256 

        :param container_name: The container_name of this WebSiteInfo.
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
        if not isinstance(other, WebSiteInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
