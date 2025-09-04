# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDeviceCertificateResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'certificate_id': 'str',
        'common_name': 'str',
        'expiry_date': 'str',
        'fingerprint': 'str',
        'status': 'str',
        'certificate_pem': 'str'
    }

    attribute_map = {
        'certificate_id': 'certificate_id',
        'common_name': 'common_name',
        'expiry_date': 'expiry_date',
        'fingerprint': 'fingerprint',
        'status': 'status',
        'certificate_pem': 'certificate_pem'
    }

    def __init__(self, certificate_id=None, common_name=None, expiry_date=None, fingerprint=None, status=None, certificate_pem=None):
        r"""ShowDeviceCertificateResponse

        The model defined in huaweicloud sdk

        :param certificate_id: **参数说明**：设备证书ID。用来唯一标识一个设备证书
        :type certificate_id: str
        :param common_name: **参数说明**：设备证书通用名称。
        :type common_name: str
        :param expiry_date: **参数说明**：设备证书过期时间。
        :type expiry_date: str
        :param fingerprint: **参数说明**：设备证书SHA256指纹。
        :type fingerprint: str
        :param status: **参数说明**：设备证书状态，默认状态为激活 - ACTIVE：激活状态。 - INACTIVE：停用状态。
        :type status: str
        :param certificate_pem: **参数说明**：设备证书PEM格式内容。
        :type certificate_pem: str
        """
        
        super(ShowDeviceCertificateResponse, self).__init__()

        self._certificate_id = None
        self._common_name = None
        self._expiry_date = None
        self._fingerprint = None
        self._status = None
        self._certificate_pem = None
        self.discriminator = None

        if certificate_id is not None:
            self.certificate_id = certificate_id
        if common_name is not None:
            self.common_name = common_name
        if expiry_date is not None:
            self.expiry_date = expiry_date
        if fingerprint is not None:
            self.fingerprint = fingerprint
        if status is not None:
            self.status = status
        if certificate_pem is not None:
            self.certificate_pem = certificate_pem

    @property
    def certificate_id(self):
        r"""Gets the certificate_id of this ShowDeviceCertificateResponse.

        **参数说明**：设备证书ID。用来唯一标识一个设备证书

        :return: The certificate_id of this ShowDeviceCertificateResponse.
        :rtype: str
        """
        return self._certificate_id

    @certificate_id.setter
    def certificate_id(self, certificate_id):
        r"""Sets the certificate_id of this ShowDeviceCertificateResponse.

        **参数说明**：设备证书ID。用来唯一标识一个设备证书

        :param certificate_id: The certificate_id of this ShowDeviceCertificateResponse.
        :type certificate_id: str
        """
        self._certificate_id = certificate_id

    @property
    def common_name(self):
        r"""Gets the common_name of this ShowDeviceCertificateResponse.

        **参数说明**：设备证书通用名称。

        :return: The common_name of this ShowDeviceCertificateResponse.
        :rtype: str
        """
        return self._common_name

    @common_name.setter
    def common_name(self, common_name):
        r"""Sets the common_name of this ShowDeviceCertificateResponse.

        **参数说明**：设备证书通用名称。

        :param common_name: The common_name of this ShowDeviceCertificateResponse.
        :type common_name: str
        """
        self._common_name = common_name

    @property
    def expiry_date(self):
        r"""Gets the expiry_date of this ShowDeviceCertificateResponse.

        **参数说明**：设备证书过期时间。

        :return: The expiry_date of this ShowDeviceCertificateResponse.
        :rtype: str
        """
        return self._expiry_date

    @expiry_date.setter
    def expiry_date(self, expiry_date):
        r"""Sets the expiry_date of this ShowDeviceCertificateResponse.

        **参数说明**：设备证书过期时间。

        :param expiry_date: The expiry_date of this ShowDeviceCertificateResponse.
        :type expiry_date: str
        """
        self._expiry_date = expiry_date

    @property
    def fingerprint(self):
        r"""Gets the fingerprint of this ShowDeviceCertificateResponse.

        **参数说明**：设备证书SHA256指纹。

        :return: The fingerprint of this ShowDeviceCertificateResponse.
        :rtype: str
        """
        return self._fingerprint

    @fingerprint.setter
    def fingerprint(self, fingerprint):
        r"""Sets the fingerprint of this ShowDeviceCertificateResponse.

        **参数说明**：设备证书SHA256指纹。

        :param fingerprint: The fingerprint of this ShowDeviceCertificateResponse.
        :type fingerprint: str
        """
        self._fingerprint = fingerprint

    @property
    def status(self):
        r"""Gets the status of this ShowDeviceCertificateResponse.

        **参数说明**：设备证书状态，默认状态为激活 - ACTIVE：激活状态。 - INACTIVE：停用状态。

        :return: The status of this ShowDeviceCertificateResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowDeviceCertificateResponse.

        **参数说明**：设备证书状态，默认状态为激活 - ACTIVE：激活状态。 - INACTIVE：停用状态。

        :param status: The status of this ShowDeviceCertificateResponse.
        :type status: str
        """
        self._status = status

    @property
    def certificate_pem(self):
        r"""Gets the certificate_pem of this ShowDeviceCertificateResponse.

        **参数说明**：设备证书PEM格式内容。

        :return: The certificate_pem of this ShowDeviceCertificateResponse.
        :rtype: str
        """
        return self._certificate_pem

    @certificate_pem.setter
    def certificate_pem(self, certificate_pem):
        r"""Sets the certificate_pem of this ShowDeviceCertificateResponse.

        **参数说明**：设备证书PEM格式内容。

        :param certificate_pem: The certificate_pem of this ShowDeviceCertificateResponse.
        :type certificate_pem: str
        """
        self._certificate_pem = certificate_pem

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
        if not isinstance(other, ShowDeviceCertificateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
