# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImportExternalIdPCertificateRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []
    sensitive_list.append('x_security_token')

    openapi_types = {
        'identity_store_id': 'str',
        'idp_id': 'str',
        'x_security_token': 'str',
        'body': 'ImportExternalIdPCertificateReqBody'
    }

    attribute_map = {
        'identity_store_id': 'identity_store_id',
        'idp_id': 'idp_id',
        'x_security_token': 'X-Security-Token',
        'body': 'body'
    }

    def __init__(self, identity_store_id=None, idp_id=None, x_security_token=None, body=None):
        r"""ImportExternalIdPCertificateRequest

        The model defined in huaweicloud sdk

        :param identity_store_id: 身份源的全局唯一标识符（ID）
        :type identity_store_id: str
        :param idp_id: 外部身份提供商的全局唯一标识符（ID）
        :type idp_id: str
        :param x_security_token: 如果正在使用临时安全凭据，则此header是必需的，该值是临时安全凭据的安全令牌（会话令牌）。
        :type x_security_token: str
        :param body: Body of the ImportExternalIdPCertificateRequest
        :type body: :class:`huaweicloudsdkidentitycenterstore.v1.ImportExternalIdPCertificateReqBody`
        """
        
        

        self._identity_store_id = None
        self._idp_id = None
        self._x_security_token = None
        self._body = None
        self.discriminator = None

        self.identity_store_id = identity_store_id
        self.idp_id = idp_id
        if x_security_token is not None:
            self.x_security_token = x_security_token
        if body is not None:
            self.body = body

    @property
    def identity_store_id(self):
        r"""Gets the identity_store_id of this ImportExternalIdPCertificateRequest.

        身份源的全局唯一标识符（ID）

        :return: The identity_store_id of this ImportExternalIdPCertificateRequest.
        :rtype: str
        """
        return self._identity_store_id

    @identity_store_id.setter
    def identity_store_id(self, identity_store_id):
        r"""Sets the identity_store_id of this ImportExternalIdPCertificateRequest.

        身份源的全局唯一标识符（ID）

        :param identity_store_id: The identity_store_id of this ImportExternalIdPCertificateRequest.
        :type identity_store_id: str
        """
        self._identity_store_id = identity_store_id

    @property
    def idp_id(self):
        r"""Gets the idp_id of this ImportExternalIdPCertificateRequest.

        外部身份提供商的全局唯一标识符（ID）

        :return: The idp_id of this ImportExternalIdPCertificateRequest.
        :rtype: str
        """
        return self._idp_id

    @idp_id.setter
    def idp_id(self, idp_id):
        r"""Sets the idp_id of this ImportExternalIdPCertificateRequest.

        外部身份提供商的全局唯一标识符（ID）

        :param idp_id: The idp_id of this ImportExternalIdPCertificateRequest.
        :type idp_id: str
        """
        self._idp_id = idp_id

    @property
    def x_security_token(self):
        r"""Gets the x_security_token of this ImportExternalIdPCertificateRequest.

        如果正在使用临时安全凭据，则此header是必需的，该值是临时安全凭据的安全令牌（会话令牌）。

        :return: The x_security_token of this ImportExternalIdPCertificateRequest.
        :rtype: str
        """
        return self._x_security_token

    @x_security_token.setter
    def x_security_token(self, x_security_token):
        r"""Sets the x_security_token of this ImportExternalIdPCertificateRequest.

        如果正在使用临时安全凭据，则此header是必需的，该值是临时安全凭据的安全令牌（会话令牌）。

        :param x_security_token: The x_security_token of this ImportExternalIdPCertificateRequest.
        :type x_security_token: str
        """
        self._x_security_token = x_security_token

    @property
    def body(self):
        r"""Gets the body of this ImportExternalIdPCertificateRequest.

        :return: The body of this ImportExternalIdPCertificateRequest.
        :rtype: :class:`huaweicloudsdkidentitycenterstore.v1.ImportExternalIdPCertificateReqBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this ImportExternalIdPCertificateRequest.

        :param body: The body of this ImportExternalIdPCertificateRequest.
        :type body: :class:`huaweicloudsdkidentitycenterstore.v1.ImportExternalIdPCertificateReqBody`
        """
        self._body = body

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
        if not isinstance(other, ImportExternalIdPCertificateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
