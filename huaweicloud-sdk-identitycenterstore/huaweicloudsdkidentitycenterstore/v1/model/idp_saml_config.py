# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IdpSAMLConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'entity_id': 'str',
        'login_url': 'str',
        'want_request_signed': 'bool'
    }

    attribute_map = {
        'entity_id': 'entity_id',
        'login_url': 'login_url',
        'want_request_signed': 'want_request_signed'
    }

    def __init__(self, entity_id=None, login_url=None, want_request_signed=None):
        r"""IdpSAMLConfig

        The model defined in huaweicloud sdk

        :param entity_id: 身份提供商发布者标识
        :type entity_id: str
        :param login_url: 身份提供商登录链接
        :type login_url: str
        :param want_request_signed: 是否要求SAML请求签名验证
        :type want_request_signed: bool
        """
        
        

        self._entity_id = None
        self._login_url = None
        self._want_request_signed = None
        self.discriminator = None

        self.entity_id = entity_id
        self.login_url = login_url
        self.want_request_signed = want_request_signed

    @property
    def entity_id(self):
        r"""Gets the entity_id of this IdpSAMLConfig.

        身份提供商发布者标识

        :return: The entity_id of this IdpSAMLConfig.
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        r"""Sets the entity_id of this IdpSAMLConfig.

        身份提供商发布者标识

        :param entity_id: The entity_id of this IdpSAMLConfig.
        :type entity_id: str
        """
        self._entity_id = entity_id

    @property
    def login_url(self):
        r"""Gets the login_url of this IdpSAMLConfig.

        身份提供商登录链接

        :return: The login_url of this IdpSAMLConfig.
        :rtype: str
        """
        return self._login_url

    @login_url.setter
    def login_url(self, login_url):
        r"""Sets the login_url of this IdpSAMLConfig.

        身份提供商登录链接

        :param login_url: The login_url of this IdpSAMLConfig.
        :type login_url: str
        """
        self._login_url = login_url

    @property
    def want_request_signed(self):
        r"""Gets the want_request_signed of this IdpSAMLConfig.

        是否要求SAML请求签名验证

        :return: The want_request_signed of this IdpSAMLConfig.
        :rtype: bool
        """
        return self._want_request_signed

    @want_request_signed.setter
    def want_request_signed(self, want_request_signed):
        r"""Sets the want_request_signed of this IdpSAMLConfig.

        是否要求SAML请求签名验证

        :param want_request_signed: The want_request_signed of this IdpSAMLConfig.
        :type want_request_signed: bool
        """
        self._want_request_signed = want_request_signed

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
        if not isinstance(other, IdpSAMLConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
