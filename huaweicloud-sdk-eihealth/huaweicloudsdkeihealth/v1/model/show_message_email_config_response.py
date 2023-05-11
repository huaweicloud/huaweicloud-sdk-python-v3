# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowMessageEmailConfigResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'server': 'str',
        'subject_prefix': 'str',
        'user_name': 'str',
        'email': 'str',
        'language': 'LanguageEnum'
    }

    attribute_map = {
        'server': 'server',
        'subject_prefix': 'subject_prefix',
        'user_name': 'user_name',
        'email': 'email',
        'language': 'language'
    }

    def __init__(self, server=None, subject_prefix=None, user_name=None, email=None, language=None):
        """ShowMessageEmailConfigResponse

        The model defined in huaweicloud sdk

        :param server: 服务器地址
        :type server: str
        :param subject_prefix: 展示名
        :type subject_prefix: str
        :param user_name: 用户名
        :type user_name: str
        :param email: 邮箱
        :type email: str
        :param language: 
        :type language: :class:`huaweicloudsdkeihealth.v1.LanguageEnum`
        """
        
        super(ShowMessageEmailConfigResponse, self).__init__()

        self._server = None
        self._subject_prefix = None
        self._user_name = None
        self._email = None
        self._language = None
        self.discriminator = None

        if server is not None:
            self.server = server
        if subject_prefix is not None:
            self.subject_prefix = subject_prefix
        if user_name is not None:
            self.user_name = user_name
        if email is not None:
            self.email = email
        if language is not None:
            self.language = language

    @property
    def server(self):
        """Gets the server of this ShowMessageEmailConfigResponse.

        服务器地址

        :return: The server of this ShowMessageEmailConfigResponse.
        :rtype: str
        """
        return self._server

    @server.setter
    def server(self, server):
        """Sets the server of this ShowMessageEmailConfigResponse.

        服务器地址

        :param server: The server of this ShowMessageEmailConfigResponse.
        :type server: str
        """
        self._server = server

    @property
    def subject_prefix(self):
        """Gets the subject_prefix of this ShowMessageEmailConfigResponse.

        展示名

        :return: The subject_prefix of this ShowMessageEmailConfigResponse.
        :rtype: str
        """
        return self._subject_prefix

    @subject_prefix.setter
    def subject_prefix(self, subject_prefix):
        """Sets the subject_prefix of this ShowMessageEmailConfigResponse.

        展示名

        :param subject_prefix: The subject_prefix of this ShowMessageEmailConfigResponse.
        :type subject_prefix: str
        """
        self._subject_prefix = subject_prefix

    @property
    def user_name(self):
        """Gets the user_name of this ShowMessageEmailConfigResponse.

        用户名

        :return: The user_name of this ShowMessageEmailConfigResponse.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this ShowMessageEmailConfigResponse.

        用户名

        :param user_name: The user_name of this ShowMessageEmailConfigResponse.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def email(self):
        """Gets the email of this ShowMessageEmailConfigResponse.

        邮箱

        :return: The email of this ShowMessageEmailConfigResponse.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this ShowMessageEmailConfigResponse.

        邮箱

        :param email: The email of this ShowMessageEmailConfigResponse.
        :type email: str
        """
        self._email = email

    @property
    def language(self):
        """Gets the language of this ShowMessageEmailConfigResponse.

        :return: The language of this ShowMessageEmailConfigResponse.
        :rtype: :class:`huaweicloudsdkeihealth.v1.LanguageEnum`
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this ShowMessageEmailConfigResponse.

        :param language: The language of this ShowMessageEmailConfigResponse.
        :type language: :class:`huaweicloudsdkeihealth.v1.LanguageEnum`
        """
        self._language = language

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
        if not isinstance(other, ShowMessageEmailConfigResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
