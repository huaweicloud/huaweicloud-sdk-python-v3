# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CancelCertificateRequestResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cert_id': 'str',
        'message': 'str'
    }

    attribute_map = {
        'cert_id': 'cert_id',
        'message': 'message'
    }

    def __init__(self, cert_id=None, message=None):
        r"""CancelCertificateRequestResponse

        The model defined in huaweicloud sdk

        :param cert_id: 证书ID。
        :type cert_id: str
        :param message: 执行结果。取值如下： success：申请成功。
        :type message: str
        """
        
        super(CancelCertificateRequestResponse, self).__init__()

        self._cert_id = None
        self._message = None
        self.discriminator = None

        if cert_id is not None:
            self.cert_id = cert_id
        if message is not None:
            self.message = message

    @property
    def cert_id(self):
        r"""Gets the cert_id of this CancelCertificateRequestResponse.

        证书ID。

        :return: The cert_id of this CancelCertificateRequestResponse.
        :rtype: str
        """
        return self._cert_id

    @cert_id.setter
    def cert_id(self, cert_id):
        r"""Sets the cert_id of this CancelCertificateRequestResponse.

        证书ID。

        :param cert_id: The cert_id of this CancelCertificateRequestResponse.
        :type cert_id: str
        """
        self._cert_id = cert_id

    @property
    def message(self):
        r"""Gets the message of this CancelCertificateRequestResponse.

        执行结果。取值如下： success：申请成功。

        :return: The message of this CancelCertificateRequestResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this CancelCertificateRequestResponse.

        执行结果。取值如下： success：申请成功。

        :param message: The message of this CancelCertificateRequestResponse.
        :type message: str
        """
        self._message = message

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
        if not isinstance(other, CancelCertificateRequestResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
