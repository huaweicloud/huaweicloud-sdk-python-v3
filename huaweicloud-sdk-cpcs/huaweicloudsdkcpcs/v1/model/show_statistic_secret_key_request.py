# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowStatisticSecretKeyRequest:

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
        'app_id': 'str',
        '_from': 'int',
        'to': 'int',
        'period': 'int',
        'filter': 'str',
        'algorithm': 'str',
        'algorithm_type': 'str',
        'certificate_type': 'str',
        'server_type': 'str'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'app_id': 'app_id',
        '_from': 'from',
        'to': 'to',
        'period': 'period',
        'filter': 'filter',
        'algorithm': 'algorithm',
        'algorithm_type': 'algorithm_type',
        'certificate_type': 'certificate_type',
        'server_type': 'server_type'
    }

    def __init__(self, cluster_id=None, app_id=None, _from=None, to=None, period=None, filter=None, algorithm=None, algorithm_type=None, certificate_type=None, server_type=None):
        r"""ShowStatisticSecretKeyRequest

        The model defined in huaweicloud sdk

        :param cluster_id: 集群id，默认为空，默认查询所有集群
        :type cluster_id: str
        :param app_id: 应用id，默认为空，默认查询所有app
        :type app_id: str
        :param _from: 查询的初始时间戳，毫秒级时间戳，默认查询前三天
        :type _from: int
        :param to: 查询的终止时间戳，毫秒级时间戳，默认查询到当前时间
        :type to: int
        :param period: 统计周期，默认为1，五分钟为一个周期
        :type period: int
        :param filter: 统计值，默认为min:最小值
        :type filter: str
        :param algorithm: 算法，有：“sm2”,\&quot;rsa\&quot;
        :type algorithm: str
        :param algorithm_type: 算法类型，0：国密算法，1：国际算法
        :type algorithm_type: str
        :param certificate_type: 证书类型，0：根证书，1：业务证书
        :type certificate_type: str
        :param server_type: 密码服务类型
        :type server_type: str
        """
        
        

        self._cluster_id = None
        self._app_id = None
        self.__from = None
        self._to = None
        self._period = None
        self._filter = None
        self._algorithm = None
        self._algorithm_type = None
        self._certificate_type = None
        self._server_type = None
        self.discriminator = None

        if cluster_id is not None:
            self.cluster_id = cluster_id
        if app_id is not None:
            self.app_id = app_id
        if _from is not None:
            self._from = _from
        if to is not None:
            self.to = to
        if period is not None:
            self.period = period
        if filter is not None:
            self.filter = filter
        if algorithm is not None:
            self.algorithm = algorithm
        if algorithm_type is not None:
            self.algorithm_type = algorithm_type
        if certificate_type is not None:
            self.certificate_type = certificate_type
        if server_type is not None:
            self.server_type = server_type

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this ShowStatisticSecretKeyRequest.

        集群id，默认为空，默认查询所有集群

        :return: The cluster_id of this ShowStatisticSecretKeyRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this ShowStatisticSecretKeyRequest.

        集群id，默认为空，默认查询所有集群

        :param cluster_id: The cluster_id of this ShowStatisticSecretKeyRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def app_id(self):
        r"""Gets the app_id of this ShowStatisticSecretKeyRequest.

        应用id，默认为空，默认查询所有app

        :return: The app_id of this ShowStatisticSecretKeyRequest.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        r"""Sets the app_id of this ShowStatisticSecretKeyRequest.

        应用id，默认为空，默认查询所有app

        :param app_id: The app_id of this ShowStatisticSecretKeyRequest.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def _from(self):
        r"""Gets the _from of this ShowStatisticSecretKeyRequest.

        查询的初始时间戳，毫秒级时间戳，默认查询前三天

        :return: The _from of this ShowStatisticSecretKeyRequest.
        :rtype: int
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        r"""Sets the _from of this ShowStatisticSecretKeyRequest.

        查询的初始时间戳，毫秒级时间戳，默认查询前三天

        :param _from: The _from of this ShowStatisticSecretKeyRequest.
        :type _from: int
        """
        self.__from = _from

    @property
    def to(self):
        r"""Gets the to of this ShowStatisticSecretKeyRequest.

        查询的终止时间戳，毫秒级时间戳，默认查询到当前时间

        :return: The to of this ShowStatisticSecretKeyRequest.
        :rtype: int
        """
        return self._to

    @to.setter
    def to(self, to):
        r"""Sets the to of this ShowStatisticSecretKeyRequest.

        查询的终止时间戳，毫秒级时间戳，默认查询到当前时间

        :param to: The to of this ShowStatisticSecretKeyRequest.
        :type to: int
        """
        self._to = to

    @property
    def period(self):
        r"""Gets the period of this ShowStatisticSecretKeyRequest.

        统计周期，默认为1，五分钟为一个周期

        :return: The period of this ShowStatisticSecretKeyRequest.
        :rtype: int
        """
        return self._period

    @period.setter
    def period(self, period):
        r"""Sets the period of this ShowStatisticSecretKeyRequest.

        统计周期，默认为1，五分钟为一个周期

        :param period: The period of this ShowStatisticSecretKeyRequest.
        :type period: int
        """
        self._period = period

    @property
    def filter(self):
        r"""Gets the filter of this ShowStatisticSecretKeyRequest.

        统计值，默认为min:最小值

        :return: The filter of this ShowStatisticSecretKeyRequest.
        :rtype: str
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        r"""Sets the filter of this ShowStatisticSecretKeyRequest.

        统计值，默认为min:最小值

        :param filter: The filter of this ShowStatisticSecretKeyRequest.
        :type filter: str
        """
        self._filter = filter

    @property
    def algorithm(self):
        r"""Gets the algorithm of this ShowStatisticSecretKeyRequest.

        算法，有：“sm2”,\"rsa\"

        :return: The algorithm of this ShowStatisticSecretKeyRequest.
        :rtype: str
        """
        return self._algorithm

    @algorithm.setter
    def algorithm(self, algorithm):
        r"""Sets the algorithm of this ShowStatisticSecretKeyRequest.

        算法，有：“sm2”,\"rsa\"

        :param algorithm: The algorithm of this ShowStatisticSecretKeyRequest.
        :type algorithm: str
        """
        self._algorithm = algorithm

    @property
    def algorithm_type(self):
        r"""Gets the algorithm_type of this ShowStatisticSecretKeyRequest.

        算法类型，0：国密算法，1：国际算法

        :return: The algorithm_type of this ShowStatisticSecretKeyRequest.
        :rtype: str
        """
        return self._algorithm_type

    @algorithm_type.setter
    def algorithm_type(self, algorithm_type):
        r"""Sets the algorithm_type of this ShowStatisticSecretKeyRequest.

        算法类型，0：国密算法，1：国际算法

        :param algorithm_type: The algorithm_type of this ShowStatisticSecretKeyRequest.
        :type algorithm_type: str
        """
        self._algorithm_type = algorithm_type

    @property
    def certificate_type(self):
        r"""Gets the certificate_type of this ShowStatisticSecretKeyRequest.

        证书类型，0：根证书，1：业务证书

        :return: The certificate_type of this ShowStatisticSecretKeyRequest.
        :rtype: str
        """
        return self._certificate_type

    @certificate_type.setter
    def certificate_type(self, certificate_type):
        r"""Sets the certificate_type of this ShowStatisticSecretKeyRequest.

        证书类型，0：根证书，1：业务证书

        :param certificate_type: The certificate_type of this ShowStatisticSecretKeyRequest.
        :type certificate_type: str
        """
        self._certificate_type = certificate_type

    @property
    def server_type(self):
        r"""Gets the server_type of this ShowStatisticSecretKeyRequest.

        密码服务类型

        :return: The server_type of this ShowStatisticSecretKeyRequest.
        :rtype: str
        """
        return self._server_type

    @server_type.setter
    def server_type(self, server_type):
        r"""Sets the server_type of this ShowStatisticSecretKeyRequest.

        密码服务类型

        :param server_type: The server_type of this ShowStatisticSecretKeyRequest.
        :type server_type: str
        """
        self._server_type = server_type

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
        if not isinstance(other, ShowStatisticSecretKeyRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
