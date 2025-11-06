# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowResourceDetailCertificateRequest:

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
        'service_type': 'str',
        'algorithm_type': 'str',
        'certificate_type': 'str',
        'page_size': 'int',
        'page_num': 'int',
        '_from': 'int',
        'to': 'int'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'app_id': 'app_id',
        'service_type': 'service_type',
        'algorithm_type': 'algorithm_type',
        'certificate_type': 'certificate_type',
        'page_size': 'page_size',
        'page_num': 'page_num',
        '_from': 'from',
        'to': 'to'
    }

    def __init__(self, cluster_id=None, app_id=None, service_type=None, algorithm_type=None, certificate_type=None, page_size=None, page_num=None, _from=None, to=None):
        r"""ShowResourceDetailCertificateRequest

        The model defined in huaweicloud sdk

        :param cluster_id: 集群id，默认空字符串，默认查询所有集群
        :type cluster_id: str
        :param app_id: 应用id，默认空字符串，默认查询所有的应用
        :type app_id: str
        :param service_type: 密码服务类型，默认空字符串，默认查询所有密码服务类型
        :type service_type: str
        :param algorithm_type: 算法类型，默认空字符串，0：国密，1：国际
        :type algorithm_type: str
        :param certificate_type: 证书类型，默认空字符串，0：根证书，1：业务证书
        :type certificate_type: str
        :param page_size: 页面大小，不超过1500
        :type page_size: int
        :param page_num: 页数，默认1
        :type page_num: int
        :param _from: 查询起始时间戳，毫秒级时间戳，默认为0，默认从三天前查询
        :type _from: int
        :param to: 查询终止时间戳，毫秒级时间戳，默认为0，默认查询到当前时间
        :type to: int
        """
        
        

        self._cluster_id = None
        self._app_id = None
        self._service_type = None
        self._algorithm_type = None
        self._certificate_type = None
        self._page_size = None
        self._page_num = None
        self.__from = None
        self._to = None
        self.discriminator = None

        if cluster_id is not None:
            self.cluster_id = cluster_id
        if app_id is not None:
            self.app_id = app_id
        if service_type is not None:
            self.service_type = service_type
        if algorithm_type is not None:
            self.algorithm_type = algorithm_type
        if certificate_type is not None:
            self.certificate_type = certificate_type
        if page_size is not None:
            self.page_size = page_size
        if page_num is not None:
            self.page_num = page_num
        if _from is not None:
            self._from = _from
        if to is not None:
            self.to = to

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this ShowResourceDetailCertificateRequest.

        集群id，默认空字符串，默认查询所有集群

        :return: The cluster_id of this ShowResourceDetailCertificateRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this ShowResourceDetailCertificateRequest.

        集群id，默认空字符串，默认查询所有集群

        :param cluster_id: The cluster_id of this ShowResourceDetailCertificateRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def app_id(self):
        r"""Gets the app_id of this ShowResourceDetailCertificateRequest.

        应用id，默认空字符串，默认查询所有的应用

        :return: The app_id of this ShowResourceDetailCertificateRequest.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        r"""Sets the app_id of this ShowResourceDetailCertificateRequest.

        应用id，默认空字符串，默认查询所有的应用

        :param app_id: The app_id of this ShowResourceDetailCertificateRequest.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def service_type(self):
        r"""Gets the service_type of this ShowResourceDetailCertificateRequest.

        密码服务类型，默认空字符串，默认查询所有密码服务类型

        :return: The service_type of this ShowResourceDetailCertificateRequest.
        :rtype: str
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        r"""Sets the service_type of this ShowResourceDetailCertificateRequest.

        密码服务类型，默认空字符串，默认查询所有密码服务类型

        :param service_type: The service_type of this ShowResourceDetailCertificateRequest.
        :type service_type: str
        """
        self._service_type = service_type

    @property
    def algorithm_type(self):
        r"""Gets the algorithm_type of this ShowResourceDetailCertificateRequest.

        算法类型，默认空字符串，0：国密，1：国际

        :return: The algorithm_type of this ShowResourceDetailCertificateRequest.
        :rtype: str
        """
        return self._algorithm_type

    @algorithm_type.setter
    def algorithm_type(self, algorithm_type):
        r"""Sets the algorithm_type of this ShowResourceDetailCertificateRequest.

        算法类型，默认空字符串，0：国密，1：国际

        :param algorithm_type: The algorithm_type of this ShowResourceDetailCertificateRequest.
        :type algorithm_type: str
        """
        self._algorithm_type = algorithm_type

    @property
    def certificate_type(self):
        r"""Gets the certificate_type of this ShowResourceDetailCertificateRequest.

        证书类型，默认空字符串，0：根证书，1：业务证书

        :return: The certificate_type of this ShowResourceDetailCertificateRequest.
        :rtype: str
        """
        return self._certificate_type

    @certificate_type.setter
    def certificate_type(self, certificate_type):
        r"""Sets the certificate_type of this ShowResourceDetailCertificateRequest.

        证书类型，默认空字符串，0：根证书，1：业务证书

        :param certificate_type: The certificate_type of this ShowResourceDetailCertificateRequest.
        :type certificate_type: str
        """
        self._certificate_type = certificate_type

    @property
    def page_size(self):
        r"""Gets the page_size of this ShowResourceDetailCertificateRequest.

        页面大小，不超过1500

        :return: The page_size of this ShowResourceDetailCertificateRequest.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        r"""Sets the page_size of this ShowResourceDetailCertificateRequest.

        页面大小，不超过1500

        :param page_size: The page_size of this ShowResourceDetailCertificateRequest.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def page_num(self):
        r"""Gets the page_num of this ShowResourceDetailCertificateRequest.

        页数，默认1

        :return: The page_num of this ShowResourceDetailCertificateRequest.
        :rtype: int
        """
        return self._page_num

    @page_num.setter
    def page_num(self, page_num):
        r"""Sets the page_num of this ShowResourceDetailCertificateRequest.

        页数，默认1

        :param page_num: The page_num of this ShowResourceDetailCertificateRequest.
        :type page_num: int
        """
        self._page_num = page_num

    @property
    def _from(self):
        r"""Gets the _from of this ShowResourceDetailCertificateRequest.

        查询起始时间戳，毫秒级时间戳，默认为0，默认从三天前查询

        :return: The _from of this ShowResourceDetailCertificateRequest.
        :rtype: int
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        r"""Sets the _from of this ShowResourceDetailCertificateRequest.

        查询起始时间戳，毫秒级时间戳，默认为0，默认从三天前查询

        :param _from: The _from of this ShowResourceDetailCertificateRequest.
        :type _from: int
        """
        self.__from = _from

    @property
    def to(self):
        r"""Gets the to of this ShowResourceDetailCertificateRequest.

        查询终止时间戳，毫秒级时间戳，默认为0，默认查询到当前时间

        :return: The to of this ShowResourceDetailCertificateRequest.
        :rtype: int
        """
        return self._to

    @to.setter
    def to(self, to):
        r"""Sets the to of this ShowResourceDetailCertificateRequest.

        查询终止时间戳，毫秒级时间戳，默认为0，默认查询到当前时间

        :param to: The to of this ShowResourceDetailCertificateRequest.
        :type to: int
        """
        self._to = to

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
        if not isinstance(other, ShowResourceDetailCertificateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
