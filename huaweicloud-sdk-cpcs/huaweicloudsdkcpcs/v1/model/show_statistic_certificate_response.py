# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowStatisticCertificateResponse(SdkResponse):

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
        'certificate_classified_counts': 'list[VendorCertificateStatistic]',
        'certificate_counts_by_server_type': 'list[VendorCertificateStatistic]'
    }

    attribute_map = {
        'metric_name': 'metric_name',
        'certificate_classified_counts': 'certificate_classified_counts',
        'certificate_counts_by_server_type': 'certificate_counts_by_server_type'
    }

    def __init__(self, metric_name=None, certificate_classified_counts=None, certificate_counts_by_server_type=None):
        r"""ShowStatisticCertificateResponse

        The model defined in huaweicloud sdk

        :param metric_name: 资源名称
        :type metric_name: str
        :param certificate_classified_counts: 证书分布按算法和证书类型统计
        :type certificate_classified_counts: list[:class:`huaweicloudsdkcpcs.v1.VendorCertificateStatistic`]
        :param certificate_counts_by_server_type: 证书分布按服务类型统计
        :type certificate_counts_by_server_type: list[:class:`huaweicloudsdkcpcs.v1.VendorCertificateStatistic`]
        """
        
        super().__init__()

        self._metric_name = None
        self._certificate_classified_counts = None
        self._certificate_counts_by_server_type = None
        self.discriminator = None

        if metric_name is not None:
            self.metric_name = metric_name
        if certificate_classified_counts is not None:
            self.certificate_classified_counts = certificate_classified_counts
        if certificate_counts_by_server_type is not None:
            self.certificate_counts_by_server_type = certificate_counts_by_server_type

    @property
    def metric_name(self):
        r"""Gets the metric_name of this ShowStatisticCertificateResponse.

        资源名称

        :return: The metric_name of this ShowStatisticCertificateResponse.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        r"""Sets the metric_name of this ShowStatisticCertificateResponse.

        资源名称

        :param metric_name: The metric_name of this ShowStatisticCertificateResponse.
        :type metric_name: str
        """
        self._metric_name = metric_name

    @property
    def certificate_classified_counts(self):
        r"""Gets the certificate_classified_counts of this ShowStatisticCertificateResponse.

        证书分布按算法和证书类型统计

        :return: The certificate_classified_counts of this ShowStatisticCertificateResponse.
        :rtype: list[:class:`huaweicloudsdkcpcs.v1.VendorCertificateStatistic`]
        """
        return self._certificate_classified_counts

    @certificate_classified_counts.setter
    def certificate_classified_counts(self, certificate_classified_counts):
        r"""Sets the certificate_classified_counts of this ShowStatisticCertificateResponse.

        证书分布按算法和证书类型统计

        :param certificate_classified_counts: The certificate_classified_counts of this ShowStatisticCertificateResponse.
        :type certificate_classified_counts: list[:class:`huaweicloudsdkcpcs.v1.VendorCertificateStatistic`]
        """
        self._certificate_classified_counts = certificate_classified_counts

    @property
    def certificate_counts_by_server_type(self):
        r"""Gets the certificate_counts_by_server_type of this ShowStatisticCertificateResponse.

        证书分布按服务类型统计

        :return: The certificate_counts_by_server_type of this ShowStatisticCertificateResponse.
        :rtype: list[:class:`huaweicloudsdkcpcs.v1.VendorCertificateStatistic`]
        """
        return self._certificate_counts_by_server_type

    @certificate_counts_by_server_type.setter
    def certificate_counts_by_server_type(self, certificate_counts_by_server_type):
        r"""Sets the certificate_counts_by_server_type of this ShowStatisticCertificateResponse.

        证书分布按服务类型统计

        :param certificate_counts_by_server_type: The certificate_counts_by_server_type of this ShowStatisticCertificateResponse.
        :type certificate_counts_by_server_type: list[:class:`huaweicloudsdkcpcs.v1.VendorCertificateStatistic`]
        """
        self._certificate_counts_by_server_type = certificate_counts_by_server_type

    def to_dict(self):
        import warnings
        warnings.warn("ShowStatisticCertificateResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowStatisticCertificateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
