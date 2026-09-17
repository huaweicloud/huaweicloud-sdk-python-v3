# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListServiceSpecificCredentialsV5Request:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_language': 'str',
        'user_id': 'str',
        'service_name': 'str',
        'limit': 'int',
        'marker': 'str'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'user_id': 'user_id',
        'service_name': 'service_name',
        'limit': 'limit',
        'marker': 'marker'
    }

    def __init__(self, x_language=None, user_id=None, service_name=None, limit=None, marker=None):
        r"""ListServiceSpecificCredentialsV5Request

        The model defined in huaweicloud sdk

        :param x_language: 选择接口返回的信息的语言，可以为中文（\&quot;zh-cn\&quot;）或英文（\&quot;en-us\&quot;），默认为中文。
        :type x_language: str
        :param user_id: IAM用户ID。
        :type user_id: str
        :param service_name: 将结果过滤为仅包含指定服务的凭证。
        :type service_name: str
        :param limit: 每页显示的条目数量，范围为1到200条，默认为100条。
        :type limit: int
        :param marker: 分页标记，长度为4到400个字符，只包含字母、数字、\&quot;+\&quot;、\&quot;/\&quot;、\&quot;&#x3D;\&quot;、\&quot;-\&quot;和\&quot;_\&quot;的字符串。
        :type marker: str
        """
        
        

        self._x_language = None
        self._user_id = None
        self._service_name = None
        self._limit = None
        self._marker = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        if user_id is not None:
            self.user_id = user_id
        if service_name is not None:
            self.service_name = service_name
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker

    @property
    def x_language(self):
        r"""Gets the x_language of this ListServiceSpecificCredentialsV5Request.

        选择接口返回的信息的语言，可以为中文（\"zh-cn\"）或英文（\"en-us\"），默认为中文。

        :return: The x_language of this ListServiceSpecificCredentialsV5Request.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ListServiceSpecificCredentialsV5Request.

        选择接口返回的信息的语言，可以为中文（\"zh-cn\"）或英文（\"en-us\"），默认为中文。

        :param x_language: The x_language of this ListServiceSpecificCredentialsV5Request.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def user_id(self):
        r"""Gets the user_id of this ListServiceSpecificCredentialsV5Request.

        IAM用户ID。

        :return: The user_id of this ListServiceSpecificCredentialsV5Request.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this ListServiceSpecificCredentialsV5Request.

        IAM用户ID。

        :param user_id: The user_id of this ListServiceSpecificCredentialsV5Request.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def service_name(self):
        r"""Gets the service_name of this ListServiceSpecificCredentialsV5Request.

        将结果过滤为仅包含指定服务的凭证。

        :return: The service_name of this ListServiceSpecificCredentialsV5Request.
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        r"""Sets the service_name of this ListServiceSpecificCredentialsV5Request.

        将结果过滤为仅包含指定服务的凭证。

        :param service_name: The service_name of this ListServiceSpecificCredentialsV5Request.
        :type service_name: str
        """
        self._service_name = service_name

    @property
    def limit(self):
        r"""Gets the limit of this ListServiceSpecificCredentialsV5Request.

        每页显示的条目数量，范围为1到200条，默认为100条。

        :return: The limit of this ListServiceSpecificCredentialsV5Request.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListServiceSpecificCredentialsV5Request.

        每页显示的条目数量，范围为1到200条，默认为100条。

        :param limit: The limit of this ListServiceSpecificCredentialsV5Request.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ListServiceSpecificCredentialsV5Request.

        分页标记，长度为4到400个字符，只包含字母、数字、\"+\"、\"/\"、\"=\"、\"-\"和\"_\"的字符串。

        :return: The marker of this ListServiceSpecificCredentialsV5Request.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListServiceSpecificCredentialsV5Request.

        分页标记，长度为4到400个字符，只包含字母、数字、\"+\"、\"/\"、\"=\"、\"-\"和\"_\"的字符串。

        :param marker: The marker of this ListServiceSpecificCredentialsV5Request.
        :type marker: str
        """
        self._marker = marker

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
        if not isinstance(other, ListServiceSpecificCredentialsV5Request):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
