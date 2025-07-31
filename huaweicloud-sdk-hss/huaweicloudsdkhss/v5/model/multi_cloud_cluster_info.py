# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MultiCloudClusterInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cluster_id': 'str',
        'cluster_name': 'str',
        'provider': 'str',
        'server': 'str',
        'image_repo': 'str',
        'status': 'str',
        'version': 'str',
        'current_expiration_date': 'int',
        'certificate_expiration_date': 'int'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'cluster_name': 'cluster_name',
        'provider': 'provider',
        'server': 'server',
        'image_repo': 'image_repo',
        'status': 'status',
        'version': 'version',
        'current_expiration_date': 'current_expiration_date',
        'certificate_expiration_date': 'certificate_expiration_date'
    }

    def __init__(self, cluster_id=None, cluster_name=None, provider=None, server=None, image_repo=None, status=None, version=None, current_expiration_date=None, certificate_expiration_date=None):
        r"""MultiCloudClusterInfo

        The model defined in huaweicloud sdk

        :param cluster_id: 集群id
        :type cluster_id: str
        :param cluster_name: 集群名称
        :type cluster_name: str
        :param provider: 集群服务商
        :type provider: str
        :param server: 集群apiserver地址
        :type server: str
        :param image_repo: 镜像仓地址
        :type image_repo: str
        :param status: anp-agent的连接状态
        :type status: str
        :param version: anp-agent的版本
        :type version: str
        :param current_expiration_date: 当前有效期结束时间
        :type current_expiration_date: int
        :param certificate_expiration_date: 证书有效期结束时间
        :type certificate_expiration_date: int
        """
        
        

        self._cluster_id = None
        self._cluster_name = None
        self._provider = None
        self._server = None
        self._image_repo = None
        self._status = None
        self._version = None
        self._current_expiration_date = None
        self._certificate_expiration_date = None
        self.discriminator = None

        if cluster_id is not None:
            self.cluster_id = cluster_id
        if cluster_name is not None:
            self.cluster_name = cluster_name
        if provider is not None:
            self.provider = provider
        if server is not None:
            self.server = server
        if image_repo is not None:
            self.image_repo = image_repo
        if status is not None:
            self.status = status
        if version is not None:
            self.version = version
        if current_expiration_date is not None:
            self.current_expiration_date = current_expiration_date
        if certificate_expiration_date is not None:
            self.certificate_expiration_date = certificate_expiration_date

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this MultiCloudClusterInfo.

        集群id

        :return: The cluster_id of this MultiCloudClusterInfo.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this MultiCloudClusterInfo.

        集群id

        :param cluster_id: The cluster_id of this MultiCloudClusterInfo.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def cluster_name(self):
        r"""Gets the cluster_name of this MultiCloudClusterInfo.

        集群名称

        :return: The cluster_name of this MultiCloudClusterInfo.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        r"""Sets the cluster_name of this MultiCloudClusterInfo.

        集群名称

        :param cluster_name: The cluster_name of this MultiCloudClusterInfo.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def provider(self):
        r"""Gets the provider of this MultiCloudClusterInfo.

        集群服务商

        :return: The provider of this MultiCloudClusterInfo.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        r"""Sets the provider of this MultiCloudClusterInfo.

        集群服务商

        :param provider: The provider of this MultiCloudClusterInfo.
        :type provider: str
        """
        self._provider = provider

    @property
    def server(self):
        r"""Gets the server of this MultiCloudClusterInfo.

        集群apiserver地址

        :return: The server of this MultiCloudClusterInfo.
        :rtype: str
        """
        return self._server

    @server.setter
    def server(self, server):
        r"""Sets the server of this MultiCloudClusterInfo.

        集群apiserver地址

        :param server: The server of this MultiCloudClusterInfo.
        :type server: str
        """
        self._server = server

    @property
    def image_repo(self):
        r"""Gets the image_repo of this MultiCloudClusterInfo.

        镜像仓地址

        :return: The image_repo of this MultiCloudClusterInfo.
        :rtype: str
        """
        return self._image_repo

    @image_repo.setter
    def image_repo(self, image_repo):
        r"""Sets the image_repo of this MultiCloudClusterInfo.

        镜像仓地址

        :param image_repo: The image_repo of this MultiCloudClusterInfo.
        :type image_repo: str
        """
        self._image_repo = image_repo

    @property
    def status(self):
        r"""Gets the status of this MultiCloudClusterInfo.

        anp-agent的连接状态

        :return: The status of this MultiCloudClusterInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this MultiCloudClusterInfo.

        anp-agent的连接状态

        :param status: The status of this MultiCloudClusterInfo.
        :type status: str
        """
        self._status = status

    @property
    def version(self):
        r"""Gets the version of this MultiCloudClusterInfo.

        anp-agent的版本

        :return: The version of this MultiCloudClusterInfo.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this MultiCloudClusterInfo.

        anp-agent的版本

        :param version: The version of this MultiCloudClusterInfo.
        :type version: str
        """
        self._version = version

    @property
    def current_expiration_date(self):
        r"""Gets the current_expiration_date of this MultiCloudClusterInfo.

        当前有效期结束时间

        :return: The current_expiration_date of this MultiCloudClusterInfo.
        :rtype: int
        """
        return self._current_expiration_date

    @current_expiration_date.setter
    def current_expiration_date(self, current_expiration_date):
        r"""Sets the current_expiration_date of this MultiCloudClusterInfo.

        当前有效期结束时间

        :param current_expiration_date: The current_expiration_date of this MultiCloudClusterInfo.
        :type current_expiration_date: int
        """
        self._current_expiration_date = current_expiration_date

    @property
    def certificate_expiration_date(self):
        r"""Gets the certificate_expiration_date of this MultiCloudClusterInfo.

        证书有效期结束时间

        :return: The certificate_expiration_date of this MultiCloudClusterInfo.
        :rtype: int
        """
        return self._certificate_expiration_date

    @certificate_expiration_date.setter
    def certificate_expiration_date(self, certificate_expiration_date):
        r"""Sets the certificate_expiration_date of this MultiCloudClusterInfo.

        证书有效期结束时间

        :param certificate_expiration_date: The certificate_expiration_date of this MultiCloudClusterInfo.
        :type certificate_expiration_date: int
        """
        self._certificate_expiration_date = certificate_expiration_date

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
        if not isinstance(other, MultiCloudClusterInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
