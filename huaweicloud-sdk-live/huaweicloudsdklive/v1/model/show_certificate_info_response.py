# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowCertificateInfoResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total': 'float',
        'certificates_info': 'list[CertInfoResp]'
    }

    attribute_map = {
        'total': 'total',
        'certificates_info': 'certificates_info'
    }

    def __init__(self, total=None, certificates_info=None):
        r"""ShowCertificateInfoResponse

        The model defined in huaweicloud sdk

        :param total: 查询结果的总数量
        :type total: float
        :param certificates_info: 证书信息列表
        :type certificates_info: list[:class:`huaweicloudsdklive.v1.CertInfoResp`]
        """
        
        super().__init__()

        self._total = None
        self._certificates_info = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if certificates_info is not None:
            self.certificates_info = certificates_info

    @property
    def total(self):
        r"""Gets the total of this ShowCertificateInfoResponse.

        查询结果的总数量

        :return: The total of this ShowCertificateInfoResponse.
        :rtype: float
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ShowCertificateInfoResponse.

        查询结果的总数量

        :param total: The total of this ShowCertificateInfoResponse.
        :type total: float
        """
        self._total = total

    @property
    def certificates_info(self):
        r"""Gets the certificates_info of this ShowCertificateInfoResponse.

        证书信息列表

        :return: The certificates_info of this ShowCertificateInfoResponse.
        :rtype: list[:class:`huaweicloudsdklive.v1.CertInfoResp`]
        """
        return self._certificates_info

    @certificates_info.setter
    def certificates_info(self, certificates_info):
        r"""Sets the certificates_info of this ShowCertificateInfoResponse.

        证书信息列表

        :param certificates_info: The certificates_info of this ShowCertificateInfoResponse.
        :type certificates_info: list[:class:`huaweicloudsdklive.v1.CertInfoResp`]
        """
        self._certificates_info = certificates_info

    def to_dict(self):
        import warnings
        warnings.warn("ShowCertificateInfoResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowCertificateInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
