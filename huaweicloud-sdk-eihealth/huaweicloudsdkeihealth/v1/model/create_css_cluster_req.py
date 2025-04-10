# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateCssClusterReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'css_id': 'str',
        'user_name': 'str',
        'user_pwd': 'str'
    }

    attribute_map = {
        'css_id': 'css_id',
        'user_name': 'user_name',
        'user_pwd': 'user_pwd'
    }

    def __init__(self, css_id=None, user_name=None, user_pwd=None):
        r"""CreateCssClusterReq

        The model defined in huaweicloud sdk

        :param css_id: 集群id
        :type css_id: str
        :param user_name: 集群用户账号
        :type user_name: str
        :param user_pwd: 集群用户密码，长度限制为[8,32]
        :type user_pwd: str
        """
        
        

        self._css_id = None
        self._user_name = None
        self._user_pwd = None
        self.discriminator = None

        self.css_id = css_id
        self.user_name = user_name
        self.user_pwd = user_pwd

    @property
    def css_id(self):
        r"""Gets the css_id of this CreateCssClusterReq.

        集群id

        :return: The css_id of this CreateCssClusterReq.
        :rtype: str
        """
        return self._css_id

    @css_id.setter
    def css_id(self, css_id):
        r"""Sets the css_id of this CreateCssClusterReq.

        集群id

        :param css_id: The css_id of this CreateCssClusterReq.
        :type css_id: str
        """
        self._css_id = css_id

    @property
    def user_name(self):
        r"""Gets the user_name of this CreateCssClusterReq.

        集群用户账号

        :return: The user_name of this CreateCssClusterReq.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this CreateCssClusterReq.

        集群用户账号

        :param user_name: The user_name of this CreateCssClusterReq.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def user_pwd(self):
        r"""Gets the user_pwd of this CreateCssClusterReq.

        集群用户密码，长度限制为[8,32]

        :return: The user_pwd of this CreateCssClusterReq.
        :rtype: str
        """
        return self._user_pwd

    @user_pwd.setter
    def user_pwd(self, user_pwd):
        r"""Sets the user_pwd of this CreateCssClusterReq.

        集群用户密码，长度限制为[8,32]

        :param user_pwd: The user_pwd of this CreateCssClusterReq.
        :type user_pwd: str
        """
        self._user_pwd = user_pwd

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
        if not isinstance(other, CreateCssClusterReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
