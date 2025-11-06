# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowResourceDetailCertificateResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'metric_name': 'str',
        'certificate_list': 'list[ShowResourceDetailCertificateResponseBodyCertificateList]',
        'total_count': 'int',
        'expired_count': 'int',
        'expiring_count': 'int'
    }

    attribute_map = {
        'metric_name': 'metric_name',
        'certificate_list': 'certificate_list',
        'total_count': 'total_count',
        'expired_count': 'expired_count',
        'expiring_count': 'expiring_count'
    }

    def __init__(self, metric_name=None, certificate_list=None, total_count=None, expired_count=None, expiring_count=None):
        r"""ShowResourceDetailCertificateResponse

        The model defined in huaweicloud sdk

        :param metric_name: 资源名称
        :type metric_name: str
        :param certificate_list: 证书详情列表
        :type certificate_list: list[:class:`huaweicloudsdkcpcs.v1.ShowResourceDetailCertificateResponseBodyCertificateList`]
        :param total_count: 证书总数
        :type total_count: int
        :param expired_count: 证书过期数量
        :type expired_count: int
        :param expiring_count: 证书即将过期数量
        :type expiring_count: int
        """
        
        super().__init__()

        self._metric_name = None
        self._certificate_list = None
        self._total_count = None
        self._expired_count = None
        self._expiring_count = None
        self.discriminator = None

        if metric_name is not None:
            self.metric_name = metric_name
        if certificate_list is not None:
            self.certificate_list = certificate_list
        if total_count is not None:
            self.total_count = total_count
        if expired_count is not None:
            self.expired_count = expired_count
        if expiring_count is not None:
            self.expiring_count = expiring_count

    @property
    def metric_name(self):
        r"""Gets the metric_name of this ShowResourceDetailCertificateResponse.

        资源名称

        :return: The metric_name of this ShowResourceDetailCertificateResponse.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        r"""Sets the metric_name of this ShowResourceDetailCertificateResponse.

        资源名称

        :param metric_name: The metric_name of this ShowResourceDetailCertificateResponse.
        :type metric_name: str
        """
        self._metric_name = metric_name

    @property
    def certificate_list(self):
        r"""Gets the certificate_list of this ShowResourceDetailCertificateResponse.

        证书详情列表

        :return: The certificate_list of this ShowResourceDetailCertificateResponse.
        :rtype: list[:class:`huaweicloudsdkcpcs.v1.ShowResourceDetailCertificateResponseBodyCertificateList`]
        """
        return self._certificate_list

    @certificate_list.setter
    def certificate_list(self, certificate_list):
        r"""Sets the certificate_list of this ShowResourceDetailCertificateResponse.

        证书详情列表

        :param certificate_list: The certificate_list of this ShowResourceDetailCertificateResponse.
        :type certificate_list: list[:class:`huaweicloudsdkcpcs.v1.ShowResourceDetailCertificateResponseBodyCertificateList`]
        """
        self._certificate_list = certificate_list

    @property
    def total_count(self):
        r"""Gets the total_count of this ShowResourceDetailCertificateResponse.

        证书总数

        :return: The total_count of this ShowResourceDetailCertificateResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ShowResourceDetailCertificateResponse.

        证书总数

        :param total_count: The total_count of this ShowResourceDetailCertificateResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def expired_count(self):
        r"""Gets the expired_count of this ShowResourceDetailCertificateResponse.

        证书过期数量

        :return: The expired_count of this ShowResourceDetailCertificateResponse.
        :rtype: int
        """
        return self._expired_count

    @expired_count.setter
    def expired_count(self, expired_count):
        r"""Sets the expired_count of this ShowResourceDetailCertificateResponse.

        证书过期数量

        :param expired_count: The expired_count of this ShowResourceDetailCertificateResponse.
        :type expired_count: int
        """
        self._expired_count = expired_count

    @property
    def expiring_count(self):
        r"""Gets the expiring_count of this ShowResourceDetailCertificateResponse.

        证书即将过期数量

        :return: The expiring_count of this ShowResourceDetailCertificateResponse.
        :rtype: int
        """
        return self._expiring_count

    @expiring_count.setter
    def expiring_count(self, expiring_count):
        r"""Sets the expiring_count of this ShowResourceDetailCertificateResponse.

        证书即将过期数量

        :param expiring_count: The expiring_count of this ShowResourceDetailCertificateResponse.
        :type expiring_count: int
        """
        self._expiring_count = expiring_count

    def to_dict(self):
        import warnings
        warnings.warn("ShowResourceDetailCertificateResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ShowResourceDetailCertificateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
