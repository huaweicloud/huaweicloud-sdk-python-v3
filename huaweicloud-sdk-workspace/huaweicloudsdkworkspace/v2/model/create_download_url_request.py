# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateDownloadUrlRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []
    sensitive_list.append('x_client_token')

    openapi_types = {
        'x_language': 'str',
        'x_client_token': 'str',
        'skill_id': 'str',
        'package_id': 'str',
        'body': 'CreateDownloadUrlReq'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'x_client_token': 'X-Client-Token',
        'skill_id': 'skill_id',
        'package_id': 'package_id',
        'body': 'body'
    }

    def __init__(self, x_language=None, x_client_token=None, skill_id=None, package_id=None, body=None):
        r"""CreateDownloadUrlRequest

        The model defined in huaweicloud sdk

        :param x_language: 语言，用于国际化。 - en-us：英文 - zh-cn：中文
        :type x_language: str
        :param x_client_token: 幂等性标识，UUID格式。 创建类接口携带该请求头，服务端据此实现幂等控制；响应头返回相同值。
        :type x_client_token: str
        :param skill_id: 技能标识。
        :type skill_id: str
        :param package_id: 技能包标识。
        :type package_id: str
        :param body: Body of the CreateDownloadUrlRequest
        :type body: :class:`huaweicloudsdkworkspace.v2.CreateDownloadUrlReq`
        """
        
        

        self._x_language = None
        self._x_client_token = None
        self._skill_id = None
        self._package_id = None
        self._body = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        if x_client_token is not None:
            self.x_client_token = x_client_token
        self.skill_id = skill_id
        self.package_id = package_id
        if body is not None:
            self.body = body

    @property
    def x_language(self):
        r"""Gets the x_language of this CreateDownloadUrlRequest.

        语言，用于国际化。 - en-us：英文 - zh-cn：中文

        :return: The x_language of this CreateDownloadUrlRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this CreateDownloadUrlRequest.

        语言，用于国际化。 - en-us：英文 - zh-cn：中文

        :param x_language: The x_language of this CreateDownloadUrlRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def x_client_token(self):
        r"""Gets the x_client_token of this CreateDownloadUrlRequest.

        幂等性标识，UUID格式。 创建类接口携带该请求头，服务端据此实现幂等控制；响应头返回相同值。

        :return: The x_client_token of this CreateDownloadUrlRequest.
        :rtype: str
        """
        return self._x_client_token

    @x_client_token.setter
    def x_client_token(self, x_client_token):
        r"""Sets the x_client_token of this CreateDownloadUrlRequest.

        幂等性标识，UUID格式。 创建类接口携带该请求头，服务端据此实现幂等控制；响应头返回相同值。

        :param x_client_token: The x_client_token of this CreateDownloadUrlRequest.
        :type x_client_token: str
        """
        self._x_client_token = x_client_token

    @property
    def skill_id(self):
        r"""Gets the skill_id of this CreateDownloadUrlRequest.

        技能标识。

        :return: The skill_id of this CreateDownloadUrlRequest.
        :rtype: str
        """
        return self._skill_id

    @skill_id.setter
    def skill_id(self, skill_id):
        r"""Sets the skill_id of this CreateDownloadUrlRequest.

        技能标识。

        :param skill_id: The skill_id of this CreateDownloadUrlRequest.
        :type skill_id: str
        """
        self._skill_id = skill_id

    @property
    def package_id(self):
        r"""Gets the package_id of this CreateDownloadUrlRequest.

        技能包标识。

        :return: The package_id of this CreateDownloadUrlRequest.
        :rtype: str
        """
        return self._package_id

    @package_id.setter
    def package_id(self, package_id):
        r"""Sets the package_id of this CreateDownloadUrlRequest.

        技能包标识。

        :param package_id: The package_id of this CreateDownloadUrlRequest.
        :type package_id: str
        """
        self._package_id = package_id

    @property
    def body(self):
        r"""Gets the body of this CreateDownloadUrlRequest.

        :return: The body of this CreateDownloadUrlRequest.
        :rtype: :class:`huaweicloudsdkworkspace.v2.CreateDownloadUrlReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this CreateDownloadUrlRequest.

        :param body: The body of this CreateDownloadUrlRequest.
        :type body: :class:`huaweicloudsdkworkspace.v2.CreateDownloadUrlReq`
        """
        self._body = body

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
        if not isinstance(other, CreateDownloadUrlRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
