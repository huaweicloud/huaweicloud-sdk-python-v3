# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VendorKeyStatistic:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_count': 'int',
        'valid_count': 'int',
        'invalid_count': 'int',
        'tenant_id': 'str',
        'cluster_id': 'str',
        'cluster_name': 'str',
        'server_type': 'str',
        'algorithm': 'str'
    }

    attribute_map = {
        'total_count': 'total_count',
        'valid_count': 'valid_count',
        'invalid_count': 'invalid_count',
        'tenant_id': 'tenant_id',
        'cluster_id': 'cluster_id',
        'cluster_name': 'cluster_name',
        'server_type': 'server_type',
        'algorithm': 'algorithm'
    }

    def __init__(self, total_count=None, valid_count=None, invalid_count=None, tenant_id=None, cluster_id=None, cluster_name=None, server_type=None, algorithm=None):
        r"""VendorKeyStatistic

        The model defined in huaweicloud sdk

        :param total_count: 总数
        :type total_count: int
        :param valid_count: 有效数量
        :type valid_count: int
        :param invalid_count: 无效数量
        :type invalid_count: int
        :param tenant_id: 租户ID
        :type tenant_id: str
        :param cluster_id: 集群ID
        :type cluster_id: str
        :param cluster_name: 集群名称
        :type cluster_name: str
        :param server_type: 服务类型
        :type server_type: str
        :param algorithm: 算法
        :type algorithm: str
        """
        
        

        self._total_count = None
        self._valid_count = None
        self._invalid_count = None
        self._tenant_id = None
        self._cluster_id = None
        self._cluster_name = None
        self._server_type = None
        self._algorithm = None
        self.discriminator = None

        if total_count is not None:
            self.total_count = total_count
        if valid_count is not None:
            self.valid_count = valid_count
        if invalid_count is not None:
            self.invalid_count = invalid_count
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if cluster_name is not None:
            self.cluster_name = cluster_name
        if server_type is not None:
            self.server_type = server_type
        if algorithm is not None:
            self.algorithm = algorithm

    @property
    def total_count(self):
        r"""Gets the total_count of this VendorKeyStatistic.

        总数

        :return: The total_count of this VendorKeyStatistic.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this VendorKeyStatistic.

        总数

        :param total_count: The total_count of this VendorKeyStatistic.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def valid_count(self):
        r"""Gets the valid_count of this VendorKeyStatistic.

        有效数量

        :return: The valid_count of this VendorKeyStatistic.
        :rtype: int
        """
        return self._valid_count

    @valid_count.setter
    def valid_count(self, valid_count):
        r"""Sets the valid_count of this VendorKeyStatistic.

        有效数量

        :param valid_count: The valid_count of this VendorKeyStatistic.
        :type valid_count: int
        """
        self._valid_count = valid_count

    @property
    def invalid_count(self):
        r"""Gets the invalid_count of this VendorKeyStatistic.

        无效数量

        :return: The invalid_count of this VendorKeyStatistic.
        :rtype: int
        """
        return self._invalid_count

    @invalid_count.setter
    def invalid_count(self, invalid_count):
        r"""Sets the invalid_count of this VendorKeyStatistic.

        无效数量

        :param invalid_count: The invalid_count of this VendorKeyStatistic.
        :type invalid_count: int
        """
        self._invalid_count = invalid_count

    @property
    def tenant_id(self):
        r"""Gets the tenant_id of this VendorKeyStatistic.

        租户ID

        :return: The tenant_id of this VendorKeyStatistic.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        r"""Sets the tenant_id of this VendorKeyStatistic.

        租户ID

        :param tenant_id: The tenant_id of this VendorKeyStatistic.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this VendorKeyStatistic.

        集群ID

        :return: The cluster_id of this VendorKeyStatistic.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this VendorKeyStatistic.

        集群ID

        :param cluster_id: The cluster_id of this VendorKeyStatistic.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def cluster_name(self):
        r"""Gets the cluster_name of this VendorKeyStatistic.

        集群名称

        :return: The cluster_name of this VendorKeyStatistic.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        r"""Sets the cluster_name of this VendorKeyStatistic.

        集群名称

        :param cluster_name: The cluster_name of this VendorKeyStatistic.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def server_type(self):
        r"""Gets the server_type of this VendorKeyStatistic.

        服务类型

        :return: The server_type of this VendorKeyStatistic.
        :rtype: str
        """
        return self._server_type

    @server_type.setter
    def server_type(self, server_type):
        r"""Sets the server_type of this VendorKeyStatistic.

        服务类型

        :param server_type: The server_type of this VendorKeyStatistic.
        :type server_type: str
        """
        self._server_type = server_type

    @property
    def algorithm(self):
        r"""Gets the algorithm of this VendorKeyStatistic.

        算法

        :return: The algorithm of this VendorKeyStatistic.
        :rtype: str
        """
        return self._algorithm

    @algorithm.setter
    def algorithm(self, algorithm):
        r"""Sets the algorithm of this VendorKeyStatistic.

        算法

        :param algorithm: The algorithm of this VendorKeyStatistic.
        :type algorithm: str
        """
        self._algorithm = algorithm

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
        if not isinstance(other, VendorKeyStatistic):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
