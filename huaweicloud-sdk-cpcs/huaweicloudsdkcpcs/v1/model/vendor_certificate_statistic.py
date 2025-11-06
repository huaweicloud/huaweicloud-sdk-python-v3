# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VendorCertificateStatistic:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'tenant_id': 'str',
        'cluster_id': 'str',
        'server_type': 'str',
        'certificate_type': 'int',
        'algorithm_type': 'int'
    }

    attribute_map = {
        'count': 'count',
        'tenant_id': 'tenant_id',
        'cluster_id': 'cluster_id',
        'server_type': 'server_type',
        'certificate_type': 'certificate_type',
        'algorithm_type': 'algorithm_type'
    }

    def __init__(self, count=None, tenant_id=None, cluster_id=None, server_type=None, certificate_type=None, algorithm_type=None):
        r"""VendorCertificateStatistic

        The model defined in huaweicloud sdk

        :param count: 总数量
        :type count: int
        :param tenant_id: 租户ID
        :type tenant_id: str
        :param cluster_id: 集群ID
        :type cluster_id: str
        :param server_type: 服务类型
        :type server_type: str
        :param certificate_type: 证书类型
        :type certificate_type: int
        :param algorithm_type: 算法类型
        :type algorithm_type: int
        """
        
        

        self._count = None
        self._tenant_id = None
        self._cluster_id = None
        self._server_type = None
        self._certificate_type = None
        self._algorithm_type = None
        self.discriminator = None

        if count is not None:
            self.count = count
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

    @property
    def count(self):
        r"""Gets the count of this VendorCertificateStatistic.

        总数量

        :return: The count of this VendorCertificateStatistic.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this VendorCertificateStatistic.

        总数量

        :param count: The count of this VendorCertificateStatistic.
        :type count: int
        """
        self._count = count

    @property
    def tenant_id(self):
        r"""Gets the tenant_id of this VendorCertificateStatistic.

        租户ID

        :return: The tenant_id of this VendorCertificateStatistic.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        r"""Sets the tenant_id of this VendorCertificateStatistic.

        租户ID

        :param tenant_id: The tenant_id of this VendorCertificateStatistic.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this VendorCertificateStatistic.

        集群ID

        :return: The cluster_id of this VendorCertificateStatistic.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this VendorCertificateStatistic.

        集群ID

        :param cluster_id: The cluster_id of this VendorCertificateStatistic.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def server_type(self):
        r"""Gets the server_type of this VendorCertificateStatistic.

        服务类型

        :return: The server_type of this VendorCertificateStatistic.
        :rtype: str
        """
        return self._server_type

    @server_type.setter
    def server_type(self, server_type):
        r"""Sets the server_type of this VendorCertificateStatistic.

        服务类型

        :param server_type: The server_type of this VendorCertificateStatistic.
        :type server_type: str
        """
        self._server_type = server_type

    @property
    def certificate_type(self):
        r"""Gets the certificate_type of this VendorCertificateStatistic.

        证书类型

        :return: The certificate_type of this VendorCertificateStatistic.
        :rtype: int
        """
        return self._certificate_type

    @certificate_type.setter
    def certificate_type(self, certificate_type):
        r"""Sets the certificate_type of this VendorCertificateStatistic.

        证书类型

        :param certificate_type: The certificate_type of this VendorCertificateStatistic.
        :type certificate_type: int
        """
        self._certificate_type = certificate_type

    @property
    def algorithm_type(self):
        r"""Gets the algorithm_type of this VendorCertificateStatistic.

        算法类型

        :return: The algorithm_type of this VendorCertificateStatistic.
        :rtype: int
        """
        return self._algorithm_type

    @algorithm_type.setter
    def algorithm_type(self, algorithm_type):
        r"""Sets the algorithm_type of this VendorCertificateStatistic.

        算法类型

        :param algorithm_type: The algorithm_type of this VendorCertificateStatistic.
        :type algorithm_type: int
        """
        self._algorithm_type = algorithm_type

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
        if not isinstance(other, VendorCertificateStatistic):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
