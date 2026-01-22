# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CertInfoResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'play_domain': 'str',
        'project_id': 'str',
        'tenant_name': 'str',
        'start_time': 'str',
        'expire_time': 'str',
        'cert_type': 'int',
        'gm_cert_type': 'int',
        'source': 'str',
        'cert_name': 'str',
        'cert_id': 'str'
    }

    attribute_map = {
        'play_domain': 'play_domain',
        'project_id': 'project_id',
        'tenant_name': 'tenant_name',
        'start_time': 'start_time',
        'expire_time': 'expire_time',
        'cert_type': 'cert_type',
        'gm_cert_type': 'gm_cert_type',
        'source': 'source',
        'cert_name': 'cert_name',
        'cert_id': 'cert_id'
    }

    def __init__(self, play_domain=None, project_id=None, tenant_name=None, start_time=None, expire_time=None, cert_type=None, gm_cert_type=None, source=None, cert_name=None, cert_id=None):
        r"""CertInfoResp

        The model defined in huaweicloud sdk

        :param play_domain: 播放域名
        :type play_domain: str
        :param project_id: 租户ID
        :type project_id: str
        :param tenant_name: 租户名
        :type tenant_name: str
        :param start_time: 证书开始时间，格式：YYYY-MM-DDTHH:mm:ssZ，UTC时间
        :type start_time: str
        :param expire_time: 证书过期时间，格式：YYYY-MM-DDTHH:mm:ssZ，UTC时间
        :type expire_time: str
        :param cert_type: 证书类型, 1：国密证书， 0:默认，标准国际证书
        :type cert_type: int
        :param gm_cert_type: 国密证书类型, 1：签名证书， 2:加密证书
        :type gm_cert_type: int
        :param source: 证书来源。 - scm：云证书与管理服务CCM。 - user：自有证书。
        :type source: str
        :param cert_name: scm来源的证书名, 自有证书为空
        :type cert_name: str
        :param cert_id: scm来源的证书ID, 自有证书为空
        :type cert_id: str
        """
        
        

        self._play_domain = None
        self._project_id = None
        self._tenant_name = None
        self._start_time = None
        self._expire_time = None
        self._cert_type = None
        self._gm_cert_type = None
        self._source = None
        self._cert_name = None
        self._cert_id = None
        self.discriminator = None

        self.play_domain = play_domain
        self.project_id = project_id
        self.tenant_name = tenant_name
        self.start_time = start_time
        self.expire_time = expire_time
        if cert_type is not None:
            self.cert_type = cert_type
        if gm_cert_type is not None:
            self.gm_cert_type = gm_cert_type
        if source is not None:
            self.source = source
        if cert_name is not None:
            self.cert_name = cert_name
        if cert_id is not None:
            self.cert_id = cert_id

    @property
    def play_domain(self):
        r"""Gets the play_domain of this CertInfoResp.

        播放域名

        :return: The play_domain of this CertInfoResp.
        :rtype: str
        """
        return self._play_domain

    @play_domain.setter
    def play_domain(self, play_domain):
        r"""Sets the play_domain of this CertInfoResp.

        播放域名

        :param play_domain: The play_domain of this CertInfoResp.
        :type play_domain: str
        """
        self._play_domain = play_domain

    @property
    def project_id(self):
        r"""Gets the project_id of this CertInfoResp.

        租户ID

        :return: The project_id of this CertInfoResp.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this CertInfoResp.

        租户ID

        :param project_id: The project_id of this CertInfoResp.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def tenant_name(self):
        r"""Gets the tenant_name of this CertInfoResp.

        租户名

        :return: The tenant_name of this CertInfoResp.
        :rtype: str
        """
        return self._tenant_name

    @tenant_name.setter
    def tenant_name(self, tenant_name):
        r"""Sets the tenant_name of this CertInfoResp.

        租户名

        :param tenant_name: The tenant_name of this CertInfoResp.
        :type tenant_name: str
        """
        self._tenant_name = tenant_name

    @property
    def start_time(self):
        r"""Gets the start_time of this CertInfoResp.

        证书开始时间，格式：YYYY-MM-DDTHH:mm:ssZ，UTC时间

        :return: The start_time of this CertInfoResp.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this CertInfoResp.

        证书开始时间，格式：YYYY-MM-DDTHH:mm:ssZ，UTC时间

        :param start_time: The start_time of this CertInfoResp.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def expire_time(self):
        r"""Gets the expire_time of this CertInfoResp.

        证书过期时间，格式：YYYY-MM-DDTHH:mm:ssZ，UTC时间

        :return: The expire_time of this CertInfoResp.
        :rtype: str
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        r"""Sets the expire_time of this CertInfoResp.

        证书过期时间，格式：YYYY-MM-DDTHH:mm:ssZ，UTC时间

        :param expire_time: The expire_time of this CertInfoResp.
        :type expire_time: str
        """
        self._expire_time = expire_time

    @property
    def cert_type(self):
        r"""Gets the cert_type of this CertInfoResp.

        证书类型, 1：国密证书， 0:默认，标准国际证书

        :return: The cert_type of this CertInfoResp.
        :rtype: int
        """
        return self._cert_type

    @cert_type.setter
    def cert_type(self, cert_type):
        r"""Sets the cert_type of this CertInfoResp.

        证书类型, 1：国密证书， 0:默认，标准国际证书

        :param cert_type: The cert_type of this CertInfoResp.
        :type cert_type: int
        """
        self._cert_type = cert_type

    @property
    def gm_cert_type(self):
        r"""Gets the gm_cert_type of this CertInfoResp.

        国密证书类型, 1：签名证书， 2:加密证书

        :return: The gm_cert_type of this CertInfoResp.
        :rtype: int
        """
        return self._gm_cert_type

    @gm_cert_type.setter
    def gm_cert_type(self, gm_cert_type):
        r"""Sets the gm_cert_type of this CertInfoResp.

        国密证书类型, 1：签名证书， 2:加密证书

        :param gm_cert_type: The gm_cert_type of this CertInfoResp.
        :type gm_cert_type: int
        """
        self._gm_cert_type = gm_cert_type

    @property
    def source(self):
        r"""Gets the source of this CertInfoResp.

        证书来源。 - scm：云证书与管理服务CCM。 - user：自有证书。

        :return: The source of this CertInfoResp.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        r"""Sets the source of this CertInfoResp.

        证书来源。 - scm：云证书与管理服务CCM。 - user：自有证书。

        :param source: The source of this CertInfoResp.
        :type source: str
        """
        self._source = source

    @property
    def cert_name(self):
        r"""Gets the cert_name of this CertInfoResp.

        scm来源的证书名, 自有证书为空

        :return: The cert_name of this CertInfoResp.
        :rtype: str
        """
        return self._cert_name

    @cert_name.setter
    def cert_name(self, cert_name):
        r"""Sets the cert_name of this CertInfoResp.

        scm来源的证书名, 自有证书为空

        :param cert_name: The cert_name of this CertInfoResp.
        :type cert_name: str
        """
        self._cert_name = cert_name

    @property
    def cert_id(self):
        r"""Gets the cert_id of this CertInfoResp.

        scm来源的证书ID, 自有证书为空

        :return: The cert_id of this CertInfoResp.
        :rtype: str
        """
        return self._cert_id

    @cert_id.setter
    def cert_id(self, cert_id):
        r"""Sets the cert_id of this CertInfoResp.

        scm来源的证书ID, 自有证书为空

        :param cert_id: The cert_id of this CertInfoResp.
        :type cert_id: str
        """
        self._cert_id = cert_id

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
        if not isinstance(other, CertInfoResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
