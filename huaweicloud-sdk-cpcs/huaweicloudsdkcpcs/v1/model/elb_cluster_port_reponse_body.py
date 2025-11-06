# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ElbClusterPortReponseBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'cluster_id': 'str',
        'elb_id': 'str',
        'elb_ip': 'str',
        'mode': 'str',
        'listener_port': 'int',
        'listener_id': 'str',
        'server_group_port': 'int',
        'server_group_id': 'str',
        'project_id': 'str',
        'validate_time': 'str',
        'wrong': 'bool',
        'wrong_msg': 'str'
    }

    attribute_map = {
        'id': 'id',
        'cluster_id': 'cluster_id',
        'elb_id': 'elb_id',
        'elb_ip': 'elb_ip',
        'mode': 'mode',
        'listener_port': 'listener_port',
        'listener_id': 'listener_id',
        'server_group_port': 'server_group_port',
        'server_group_id': 'server_group_id',
        'project_id': 'project_id',
        'validate_time': 'validate_time',
        'wrong': 'wrong',
        'wrong_msg': 'wrong_msg'
    }

    def __init__(self, id=None, cluster_id=None, elb_id=None, elb_ip=None, mode=None, listener_port=None, listener_id=None, server_group_port=None, server_group_id=None, project_id=None, validate_time=None, wrong=None, wrong_msg=None):
        r"""ElbClusterPortReponseBody

        The model defined in huaweicloud sdk

        :param id: uuid
        :type id: str
        :param cluster_id: 该端口归属的集群id
        :type cluster_id: str
        :param elb_id: 租户的elbId
        :type elb_id: str
        :param elb_ip: 租户的elb的ip
        :type elb_ip: str
        :param mode: PROXY：代理模式端口 TUNNEL：隧道模式自定端口 TUNNEL_FIXED：隧道模式的固定隧道端口
        :type mode: str
        :param listener_port: elb监听端口
        :type listener_port: int
        :param listener_id: elb监听器id
        :type listener_id: str
        :param server_group_port: 后端服务组绑定的后端服务器的业务端口
        :type server_group_port: int
        :param server_group_id: 后端服务组id
        :type server_group_id: str
        :param project_id: 项目id
        :type project_id: str
        :param validate_time: 最后验证时间
        :type validate_time: str
        :param wrong: 资源是否异常。 由于该接口功能是cpcs操作租户的elb。而租户是可以二次操作cpcs创建的端口映射的。cpcs提供了一个检测接口，用以检测cpcs创建的这一套监听端口是否有误。
        :type wrong: bool
        :param wrong_msg: 若端口有误。即wrong&#x3D;true时。该字段描述错误的地方
        :type wrong_msg: str
        """
        
        

        self._id = None
        self._cluster_id = None
        self._elb_id = None
        self._elb_ip = None
        self._mode = None
        self._listener_port = None
        self._listener_id = None
        self._server_group_port = None
        self._server_group_id = None
        self._project_id = None
        self._validate_time = None
        self._wrong = None
        self._wrong_msg = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if elb_id is not None:
            self.elb_id = elb_id
        if elb_ip is not None:
            self.elb_ip = elb_ip
        if mode is not None:
            self.mode = mode
        if listener_port is not None:
            self.listener_port = listener_port
        if listener_id is not None:
            self.listener_id = listener_id
        if server_group_port is not None:
            self.server_group_port = server_group_port
        if server_group_id is not None:
            self.server_group_id = server_group_id
        if project_id is not None:
            self.project_id = project_id
        if validate_time is not None:
            self.validate_time = validate_time
        if wrong is not None:
            self.wrong = wrong
        if wrong_msg is not None:
            self.wrong_msg = wrong_msg

    @property
    def id(self):
        r"""Gets the id of this ElbClusterPortReponseBody.

        uuid

        :return: The id of this ElbClusterPortReponseBody.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ElbClusterPortReponseBody.

        uuid

        :param id: The id of this ElbClusterPortReponseBody.
        :type id: str
        """
        self._id = id

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this ElbClusterPortReponseBody.

        该端口归属的集群id

        :return: The cluster_id of this ElbClusterPortReponseBody.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this ElbClusterPortReponseBody.

        该端口归属的集群id

        :param cluster_id: The cluster_id of this ElbClusterPortReponseBody.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def elb_id(self):
        r"""Gets the elb_id of this ElbClusterPortReponseBody.

        租户的elbId

        :return: The elb_id of this ElbClusterPortReponseBody.
        :rtype: str
        """
        return self._elb_id

    @elb_id.setter
    def elb_id(self, elb_id):
        r"""Sets the elb_id of this ElbClusterPortReponseBody.

        租户的elbId

        :param elb_id: The elb_id of this ElbClusterPortReponseBody.
        :type elb_id: str
        """
        self._elb_id = elb_id

    @property
    def elb_ip(self):
        r"""Gets the elb_ip of this ElbClusterPortReponseBody.

        租户的elb的ip

        :return: The elb_ip of this ElbClusterPortReponseBody.
        :rtype: str
        """
        return self._elb_ip

    @elb_ip.setter
    def elb_ip(self, elb_ip):
        r"""Sets the elb_ip of this ElbClusterPortReponseBody.

        租户的elb的ip

        :param elb_ip: The elb_ip of this ElbClusterPortReponseBody.
        :type elb_ip: str
        """
        self._elb_ip = elb_ip

    @property
    def mode(self):
        r"""Gets the mode of this ElbClusterPortReponseBody.

        PROXY：代理模式端口 TUNNEL：隧道模式自定端口 TUNNEL_FIXED：隧道模式的固定隧道端口

        :return: The mode of this ElbClusterPortReponseBody.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        r"""Sets the mode of this ElbClusterPortReponseBody.

        PROXY：代理模式端口 TUNNEL：隧道模式自定端口 TUNNEL_FIXED：隧道模式的固定隧道端口

        :param mode: The mode of this ElbClusterPortReponseBody.
        :type mode: str
        """
        self._mode = mode

    @property
    def listener_port(self):
        r"""Gets the listener_port of this ElbClusterPortReponseBody.

        elb监听端口

        :return: The listener_port of this ElbClusterPortReponseBody.
        :rtype: int
        """
        return self._listener_port

    @listener_port.setter
    def listener_port(self, listener_port):
        r"""Sets the listener_port of this ElbClusterPortReponseBody.

        elb监听端口

        :param listener_port: The listener_port of this ElbClusterPortReponseBody.
        :type listener_port: int
        """
        self._listener_port = listener_port

    @property
    def listener_id(self):
        r"""Gets the listener_id of this ElbClusterPortReponseBody.

        elb监听器id

        :return: The listener_id of this ElbClusterPortReponseBody.
        :rtype: str
        """
        return self._listener_id

    @listener_id.setter
    def listener_id(self, listener_id):
        r"""Sets the listener_id of this ElbClusterPortReponseBody.

        elb监听器id

        :param listener_id: The listener_id of this ElbClusterPortReponseBody.
        :type listener_id: str
        """
        self._listener_id = listener_id

    @property
    def server_group_port(self):
        r"""Gets the server_group_port of this ElbClusterPortReponseBody.

        后端服务组绑定的后端服务器的业务端口

        :return: The server_group_port of this ElbClusterPortReponseBody.
        :rtype: int
        """
        return self._server_group_port

    @server_group_port.setter
    def server_group_port(self, server_group_port):
        r"""Sets the server_group_port of this ElbClusterPortReponseBody.

        后端服务组绑定的后端服务器的业务端口

        :param server_group_port: The server_group_port of this ElbClusterPortReponseBody.
        :type server_group_port: int
        """
        self._server_group_port = server_group_port

    @property
    def server_group_id(self):
        r"""Gets the server_group_id of this ElbClusterPortReponseBody.

        后端服务组id

        :return: The server_group_id of this ElbClusterPortReponseBody.
        :rtype: str
        """
        return self._server_group_id

    @server_group_id.setter
    def server_group_id(self, server_group_id):
        r"""Sets the server_group_id of this ElbClusterPortReponseBody.

        后端服务组id

        :param server_group_id: The server_group_id of this ElbClusterPortReponseBody.
        :type server_group_id: str
        """
        self._server_group_id = server_group_id

    @property
    def project_id(self):
        r"""Gets the project_id of this ElbClusterPortReponseBody.

        项目id

        :return: The project_id of this ElbClusterPortReponseBody.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ElbClusterPortReponseBody.

        项目id

        :param project_id: The project_id of this ElbClusterPortReponseBody.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def validate_time(self):
        r"""Gets the validate_time of this ElbClusterPortReponseBody.

        最后验证时间

        :return: The validate_time of this ElbClusterPortReponseBody.
        :rtype: str
        """
        return self._validate_time

    @validate_time.setter
    def validate_time(self, validate_time):
        r"""Sets the validate_time of this ElbClusterPortReponseBody.

        最后验证时间

        :param validate_time: The validate_time of this ElbClusterPortReponseBody.
        :type validate_time: str
        """
        self._validate_time = validate_time

    @property
    def wrong(self):
        r"""Gets the wrong of this ElbClusterPortReponseBody.

        资源是否异常。 由于该接口功能是cpcs操作租户的elb。而租户是可以二次操作cpcs创建的端口映射的。cpcs提供了一个检测接口，用以检测cpcs创建的这一套监听端口是否有误。

        :return: The wrong of this ElbClusterPortReponseBody.
        :rtype: bool
        """
        return self._wrong

    @wrong.setter
    def wrong(self, wrong):
        r"""Sets the wrong of this ElbClusterPortReponseBody.

        资源是否异常。 由于该接口功能是cpcs操作租户的elb。而租户是可以二次操作cpcs创建的端口映射的。cpcs提供了一个检测接口，用以检测cpcs创建的这一套监听端口是否有误。

        :param wrong: The wrong of this ElbClusterPortReponseBody.
        :type wrong: bool
        """
        self._wrong = wrong

    @property
    def wrong_msg(self):
        r"""Gets the wrong_msg of this ElbClusterPortReponseBody.

        若端口有误。即wrong=true时。该字段描述错误的地方

        :return: The wrong_msg of this ElbClusterPortReponseBody.
        :rtype: str
        """
        return self._wrong_msg

    @wrong_msg.setter
    def wrong_msg(self, wrong_msg):
        r"""Sets the wrong_msg of this ElbClusterPortReponseBody.

        若端口有误。即wrong=true时。该字段描述错误的地方

        :param wrong_msg: The wrong_msg of this ElbClusterPortReponseBody.
        :type wrong_msg: str
        """
        self._wrong_msg = wrong_msg

    def to_dict(self):
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
        if not isinstance(other, ElbClusterPortReponseBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
