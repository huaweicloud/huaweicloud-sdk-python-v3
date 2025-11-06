# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateDrClusterDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cluster_name': 'str',
        'cluster_id': 'str',
        'cidr': 'str',
        'gateway_ip': 'str',
        'internal_ips': 'str',
        'private_ips': 'str',
        'endpoint': 'str',
        'db_admin_pwd': 'str',
        'disaster_recovery_id': 'str',
        'kernel_version': 'str'
    }

    attribute_map = {
        'cluster_name': 'cluster_name',
        'cluster_id': 'cluster_id',
        'cidr': 'cidr',
        'gateway_ip': 'gateway_ip',
        'internal_ips': 'internal_ips',
        'private_ips': 'private_ips',
        'endpoint': 'endpoint',
        'db_admin_pwd': 'db_admin_pwd',
        'disaster_recovery_id': 'disaster_recovery_id',
        'kernel_version': 'kernel_version'
    }

    def __init__(self, cluster_name=None, cluster_id=None, cidr=None, gateway_ip=None, internal_ips=None, private_ips=None, endpoint=None, db_admin_pwd=None, disaster_recovery_id=None, kernel_version=None):
        r"""CreateDrClusterDto

        The model defined in huaweicloud sdk

        :param cluster_name: **参数解释**： 集群名称。 **取值范围**： 不涉及。
        :type cluster_name: str
        :param cluster_id: **参数解释**： 集群ID。 **取值范围**： 不涉及。
        :type cluster_id: str
        :param cidr: **参数解释**： 子网的网段。 **取值范围**： 不涉及。
        :type cidr: str
        :param gateway_ip: **参数解释**： 子网的网关。 **取值范围**： 不涉及。
        :type gateway_ip: str
        :param internal_ips: **参数解释**： 主网卡IP。 **取值范围**： 不涉及。
        :type internal_ips: str
        :param private_ips: **参数解释**： 内网IP。 **取值范围**： 不涉及。
        :type private_ips: str
        :param endpoint: **参数解释**： 域名。 **取值范围**： 不涉及。
        :type endpoint: str
        :param db_admin_pwd: **参数解释**： 数据库管理员密码。 **取值范围**： 不涉及。
        :type db_admin_pwd: str
        :param disaster_recovery_id: **参数解释**： 容灾ID。 **取值范围**： 不涉及。
        :type disaster_recovery_id: str
        :param kernel_version: **参数解释**： 内核的版本。 **取值范围**： 不涉及。
        :type kernel_version: str
        """
        
        

        self._cluster_name = None
        self._cluster_id = None
        self._cidr = None
        self._gateway_ip = None
        self._internal_ips = None
        self._private_ips = None
        self._endpoint = None
        self._db_admin_pwd = None
        self._disaster_recovery_id = None
        self._kernel_version = None
        self.discriminator = None

        if cluster_name is not None:
            self.cluster_name = cluster_name
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if cidr is not None:
            self.cidr = cidr
        if gateway_ip is not None:
            self.gateway_ip = gateway_ip
        if internal_ips is not None:
            self.internal_ips = internal_ips
        if private_ips is not None:
            self.private_ips = private_ips
        if endpoint is not None:
            self.endpoint = endpoint
        if db_admin_pwd is not None:
            self.db_admin_pwd = db_admin_pwd
        if disaster_recovery_id is not None:
            self.disaster_recovery_id = disaster_recovery_id
        if kernel_version is not None:
            self.kernel_version = kernel_version

    @property
    def cluster_name(self):
        r"""Gets the cluster_name of this CreateDrClusterDto.

        **参数解释**： 集群名称。 **取值范围**： 不涉及。

        :return: The cluster_name of this CreateDrClusterDto.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        r"""Sets the cluster_name of this CreateDrClusterDto.

        **参数解释**： 集群名称。 **取值范围**： 不涉及。

        :param cluster_name: The cluster_name of this CreateDrClusterDto.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this CreateDrClusterDto.

        **参数解释**： 集群ID。 **取值范围**： 不涉及。

        :return: The cluster_id of this CreateDrClusterDto.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this CreateDrClusterDto.

        **参数解释**： 集群ID。 **取值范围**： 不涉及。

        :param cluster_id: The cluster_id of this CreateDrClusterDto.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def cidr(self):
        r"""Gets the cidr of this CreateDrClusterDto.

        **参数解释**： 子网的网段。 **取值范围**： 不涉及。

        :return: The cidr of this CreateDrClusterDto.
        :rtype: str
        """
        return self._cidr

    @cidr.setter
    def cidr(self, cidr):
        r"""Sets the cidr of this CreateDrClusterDto.

        **参数解释**： 子网的网段。 **取值范围**： 不涉及。

        :param cidr: The cidr of this CreateDrClusterDto.
        :type cidr: str
        """
        self._cidr = cidr

    @property
    def gateway_ip(self):
        r"""Gets the gateway_ip of this CreateDrClusterDto.

        **参数解释**： 子网的网关。 **取值范围**： 不涉及。

        :return: The gateway_ip of this CreateDrClusterDto.
        :rtype: str
        """
        return self._gateway_ip

    @gateway_ip.setter
    def gateway_ip(self, gateway_ip):
        r"""Sets the gateway_ip of this CreateDrClusterDto.

        **参数解释**： 子网的网关。 **取值范围**： 不涉及。

        :param gateway_ip: The gateway_ip of this CreateDrClusterDto.
        :type gateway_ip: str
        """
        self._gateway_ip = gateway_ip

    @property
    def internal_ips(self):
        r"""Gets the internal_ips of this CreateDrClusterDto.

        **参数解释**： 主网卡IP。 **取值范围**： 不涉及。

        :return: The internal_ips of this CreateDrClusterDto.
        :rtype: str
        """
        return self._internal_ips

    @internal_ips.setter
    def internal_ips(self, internal_ips):
        r"""Sets the internal_ips of this CreateDrClusterDto.

        **参数解释**： 主网卡IP。 **取值范围**： 不涉及。

        :param internal_ips: The internal_ips of this CreateDrClusterDto.
        :type internal_ips: str
        """
        self._internal_ips = internal_ips

    @property
    def private_ips(self):
        r"""Gets the private_ips of this CreateDrClusterDto.

        **参数解释**： 内网IP。 **取值范围**： 不涉及。

        :return: The private_ips of this CreateDrClusterDto.
        :rtype: str
        """
        return self._private_ips

    @private_ips.setter
    def private_ips(self, private_ips):
        r"""Sets the private_ips of this CreateDrClusterDto.

        **参数解释**： 内网IP。 **取值范围**： 不涉及。

        :param private_ips: The private_ips of this CreateDrClusterDto.
        :type private_ips: str
        """
        self._private_ips = private_ips

    @property
    def endpoint(self):
        r"""Gets the endpoint of this CreateDrClusterDto.

        **参数解释**： 域名。 **取值范围**： 不涉及。

        :return: The endpoint of this CreateDrClusterDto.
        :rtype: str
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint):
        r"""Sets the endpoint of this CreateDrClusterDto.

        **参数解释**： 域名。 **取值范围**： 不涉及。

        :param endpoint: The endpoint of this CreateDrClusterDto.
        :type endpoint: str
        """
        self._endpoint = endpoint

    @property
    def db_admin_pwd(self):
        r"""Gets the db_admin_pwd of this CreateDrClusterDto.

        **参数解释**： 数据库管理员密码。 **取值范围**： 不涉及。

        :return: The db_admin_pwd of this CreateDrClusterDto.
        :rtype: str
        """
        return self._db_admin_pwd

    @db_admin_pwd.setter
    def db_admin_pwd(self, db_admin_pwd):
        r"""Sets the db_admin_pwd of this CreateDrClusterDto.

        **参数解释**： 数据库管理员密码。 **取值范围**： 不涉及。

        :param db_admin_pwd: The db_admin_pwd of this CreateDrClusterDto.
        :type db_admin_pwd: str
        """
        self._db_admin_pwd = db_admin_pwd

    @property
    def disaster_recovery_id(self):
        r"""Gets the disaster_recovery_id of this CreateDrClusterDto.

        **参数解释**： 容灾ID。 **取值范围**： 不涉及。

        :return: The disaster_recovery_id of this CreateDrClusterDto.
        :rtype: str
        """
        return self._disaster_recovery_id

    @disaster_recovery_id.setter
    def disaster_recovery_id(self, disaster_recovery_id):
        r"""Sets the disaster_recovery_id of this CreateDrClusterDto.

        **参数解释**： 容灾ID。 **取值范围**： 不涉及。

        :param disaster_recovery_id: The disaster_recovery_id of this CreateDrClusterDto.
        :type disaster_recovery_id: str
        """
        self._disaster_recovery_id = disaster_recovery_id

    @property
    def kernel_version(self):
        r"""Gets the kernel_version of this CreateDrClusterDto.

        **参数解释**： 内核的版本。 **取值范围**： 不涉及。

        :return: The kernel_version of this CreateDrClusterDto.
        :rtype: str
        """
        return self._kernel_version

    @kernel_version.setter
    def kernel_version(self, kernel_version):
        r"""Sets the kernel_version of this CreateDrClusterDto.

        **参数解释**： 内核的版本。 **取值范围**： 不涉及。

        :param kernel_version: The kernel_version of this CreateDrClusterDto.
        :type kernel_version: str
        """
        self._kernel_version = kernel_version

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
        if not isinstance(other, CreateDrClusterDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
