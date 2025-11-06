# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowResourceDetailCertificateResponseBodyCertificateList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'id': 'str',
        'tenant_id': 'str',
        'cluster_id': 'str',
        'server_type': 'str',
        'certificate_type': 'str',
        'algorithm_type': 'str',
        'algorithm': 'str',
        'start_time': 'int',
        'expired_time': 'int',
        'issuer': 'str',
        'user': 'str',
        'status': 'int',
        'create_time': 'str'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'tenant_id': 'tenant_id',
        'cluster_id': 'cluster_id',
        'server_type': 'server_type',
        'certificate_type': 'certificate_type',
        'algorithm_type': 'algorithm_type',
        'algorithm': 'algorithm',
        'start_time': 'start_time',
        'expired_time': 'expired_time',
        'issuer': 'issuer',
        'user': 'user',
        'status': 'status',
        'create_time': 'create_time'
    }

    def __init__(self, name=None, id=None, tenant_id=None, cluster_id=None, server_type=None, certificate_type=None, algorithm_type=None, algorithm=None, start_time=None, expired_time=None, issuer=None, user=None, status=None, create_time=None):
        r"""ShowResourceDetailCertificateResponseBodyCertificateList

        The model defined in huaweicloud sdk

        :param name: 证书名称
        :type name: str
        :param id: 证书ID
        :type id: str
        :param tenant_id: 租户ID
        :type tenant_id: str
        :param cluster_id: 集群ID
        :type cluster_id: str
        :param server_type: 密码服务类型
        :type server_type: str
        :param certificate_type: 证书类型，0：根证书，1：业务证书
        :type certificate_type: str
        :param algorithm_type: 算法类型，0：国密，1：国际
        :type algorithm_type: str
        :param algorithm: 算法名称
        :type algorithm: str
        :param start_time: 开始时间，UNIX时间戳，单位毫秒
        :type start_time: int
        :param expired_time: 过期时间，UNIX时间戳，单位毫秒
        :type expired_time: int
        :param issuer: 签发者
        :type issuer: str
        :param user: 用户
        :type user: str
        :param status: 证书状态，0：正常，2：过期，3：即将过期
        :type status: int
        :param create_time: 创建时间
        :type create_time: str
        """
        
        

        self._name = None
        self._id = None
        self._tenant_id = None
        self._cluster_id = None
        self._server_type = None
        self._certificate_type = None
        self._algorithm_type = None
        self._algorithm = None
        self._start_time = None
        self._expired_time = None
        self._issuer = None
        self._user = None
        self._status = None
        self._create_time = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if server_type is not None:
            self.server_type = server_type
        if certificate_type is not None:
            self.certificate_type = certificate_type
        if algorithm_type is not None:
            self.algorithm_type = algorithm_type
        if algorithm is not None:
            self.algorithm = algorithm
        if start_time is not None:
            self.start_time = start_time
        if expired_time is not None:
            self.expired_time = expired_time
        if issuer is not None:
            self.issuer = issuer
        if user is not None:
            self.user = user
        if status is not None:
            self.status = status
        if create_time is not None:
            self.create_time = create_time

    @property
    def name(self):
        r"""Gets the name of this ShowResourceDetailCertificateResponseBodyCertificateList.

        证书名称

        :return: The name of this ShowResourceDetailCertificateResponseBodyCertificateList.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowResourceDetailCertificateResponseBodyCertificateList.

        证书名称

        :param name: The name of this ShowResourceDetailCertificateResponseBodyCertificateList.
        :type name: str
        """
        self._name = name

    @property
    def id(self):
        r"""Gets the id of this ShowResourceDetailCertificateResponseBodyCertificateList.

        证书ID

        :return: The id of this ShowResourceDetailCertificateResponseBodyCertificateList.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowResourceDetailCertificateResponseBodyCertificateList.

        证书ID

        :param id: The id of this ShowResourceDetailCertificateResponseBodyCertificateList.
        :type id: str
        """
        self._id = id

    @property
    def tenant_id(self):
        r"""Gets the tenant_id of this ShowResourceDetailCertificateResponseBodyCertificateList.

        租户ID

        :return: The tenant_id of this ShowResourceDetailCertificateResponseBodyCertificateList.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        r"""Sets the tenant_id of this ShowResourceDetailCertificateResponseBodyCertificateList.

        租户ID

        :param tenant_id: The tenant_id of this ShowResourceDetailCertificateResponseBodyCertificateList.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this ShowResourceDetailCertificateResponseBodyCertificateList.

        集群ID

        :return: The cluster_id of this ShowResourceDetailCertificateResponseBodyCertificateList.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this ShowResourceDetailCertificateResponseBodyCertificateList.

        集群ID

        :param cluster_id: The cluster_id of this ShowResourceDetailCertificateResponseBodyCertificateList.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def server_type(self):
        r"""Gets the server_type of this ShowResourceDetailCertificateResponseBodyCertificateList.

        密码服务类型

        :return: The server_type of this ShowResourceDetailCertificateResponseBodyCertificateList.
        :rtype: str
        """
        return self._server_type

    @server_type.setter
    def server_type(self, server_type):
        r"""Sets the server_type of this ShowResourceDetailCertificateResponseBodyCertificateList.

        密码服务类型

        :param server_type: The server_type of this ShowResourceDetailCertificateResponseBodyCertificateList.
        :type server_type: str
        """
        self._server_type = server_type

    @property
    def certificate_type(self):
        r"""Gets the certificate_type of this ShowResourceDetailCertificateResponseBodyCertificateList.

        证书类型，0：根证书，1：业务证书

        :return: The certificate_type of this ShowResourceDetailCertificateResponseBodyCertificateList.
        :rtype: str
        """
        return self._certificate_type

    @certificate_type.setter
    def certificate_type(self, certificate_type):
        r"""Sets the certificate_type of this ShowResourceDetailCertificateResponseBodyCertificateList.

        证书类型，0：根证书，1：业务证书

        :param certificate_type: The certificate_type of this ShowResourceDetailCertificateResponseBodyCertificateList.
        :type certificate_type: str
        """
        self._certificate_type = certificate_type

    @property
    def algorithm_type(self):
        r"""Gets the algorithm_type of this ShowResourceDetailCertificateResponseBodyCertificateList.

        算法类型，0：国密，1：国际

        :return: The algorithm_type of this ShowResourceDetailCertificateResponseBodyCertificateList.
        :rtype: str
        """
        return self._algorithm_type

    @algorithm_type.setter
    def algorithm_type(self, algorithm_type):
        r"""Sets the algorithm_type of this ShowResourceDetailCertificateResponseBodyCertificateList.

        算法类型，0：国密，1：国际

        :param algorithm_type: The algorithm_type of this ShowResourceDetailCertificateResponseBodyCertificateList.
        :type algorithm_type: str
        """
        self._algorithm_type = algorithm_type

    @property
    def algorithm(self):
        r"""Gets the algorithm of this ShowResourceDetailCertificateResponseBodyCertificateList.

        算法名称

        :return: The algorithm of this ShowResourceDetailCertificateResponseBodyCertificateList.
        :rtype: str
        """
        return self._algorithm

    @algorithm.setter
    def algorithm(self, algorithm):
        r"""Sets the algorithm of this ShowResourceDetailCertificateResponseBodyCertificateList.

        算法名称

        :param algorithm: The algorithm of this ShowResourceDetailCertificateResponseBodyCertificateList.
        :type algorithm: str
        """
        self._algorithm = algorithm

    @property
    def start_time(self):
        r"""Gets the start_time of this ShowResourceDetailCertificateResponseBodyCertificateList.

        开始时间，UNIX时间戳，单位毫秒

        :return: The start_time of this ShowResourceDetailCertificateResponseBodyCertificateList.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ShowResourceDetailCertificateResponseBodyCertificateList.

        开始时间，UNIX时间戳，单位毫秒

        :param start_time: The start_time of this ShowResourceDetailCertificateResponseBodyCertificateList.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def expired_time(self):
        r"""Gets the expired_time of this ShowResourceDetailCertificateResponseBodyCertificateList.

        过期时间，UNIX时间戳，单位毫秒

        :return: The expired_time of this ShowResourceDetailCertificateResponseBodyCertificateList.
        :rtype: int
        """
        return self._expired_time

    @expired_time.setter
    def expired_time(self, expired_time):
        r"""Sets the expired_time of this ShowResourceDetailCertificateResponseBodyCertificateList.

        过期时间，UNIX时间戳，单位毫秒

        :param expired_time: The expired_time of this ShowResourceDetailCertificateResponseBodyCertificateList.
        :type expired_time: int
        """
        self._expired_time = expired_time

    @property
    def issuer(self):
        r"""Gets the issuer of this ShowResourceDetailCertificateResponseBodyCertificateList.

        签发者

        :return: The issuer of this ShowResourceDetailCertificateResponseBodyCertificateList.
        :rtype: str
        """
        return self._issuer

    @issuer.setter
    def issuer(self, issuer):
        r"""Sets the issuer of this ShowResourceDetailCertificateResponseBodyCertificateList.

        签发者

        :param issuer: The issuer of this ShowResourceDetailCertificateResponseBodyCertificateList.
        :type issuer: str
        """
        self._issuer = issuer

    @property
    def user(self):
        r"""Gets the user of this ShowResourceDetailCertificateResponseBodyCertificateList.

        用户

        :return: The user of this ShowResourceDetailCertificateResponseBodyCertificateList.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        r"""Sets the user of this ShowResourceDetailCertificateResponseBodyCertificateList.

        用户

        :param user: The user of this ShowResourceDetailCertificateResponseBodyCertificateList.
        :type user: str
        """
        self._user = user

    @property
    def status(self):
        r"""Gets the status of this ShowResourceDetailCertificateResponseBodyCertificateList.

        证书状态，0：正常，2：过期，3：即将过期

        :return: The status of this ShowResourceDetailCertificateResponseBodyCertificateList.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowResourceDetailCertificateResponseBodyCertificateList.

        证书状态，0：正常，2：过期，3：即将过期

        :param status: The status of this ShowResourceDetailCertificateResponseBodyCertificateList.
        :type status: int
        """
        self._status = status

    @property
    def create_time(self):
        r"""Gets the create_time of this ShowResourceDetailCertificateResponseBodyCertificateList.

        创建时间

        :return: The create_time of this ShowResourceDetailCertificateResponseBodyCertificateList.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ShowResourceDetailCertificateResponseBodyCertificateList.

        创建时间

        :param create_time: The create_time of this ShowResourceDetailCertificateResponseBodyCertificateList.
        :type create_time: str
        """
        self._create_time = create_time

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
        if not isinstance(other, ShowResourceDetailCertificateResponseBodyCertificateList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
