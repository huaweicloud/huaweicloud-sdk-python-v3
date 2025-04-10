# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApiTestRequestHeader:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'path': 'str',
        'user_agent': 'str',
        'x_apig_mode': 'str',
        'x_app_identity': 'int'
    }

    attribute_map = {
        'path': 'path',
        'user_agent': 'user_agent',
        'x_apig_mode': 'x_apig_mode',
        'x_app_identity': 'x_app_identity'
    }

    def __init__(self, path=None, user_agent=None, x_apig_mode=None, x_app_identity=None):
        r"""ApiTestRequestHeader

        The model defined in huaweicloud sdk

        :param path: 请求路径
        :type path: str
        :param user_agent: 代理（固定值）
        :type user_agent: str
        :param x_apig_mode: 请求方式（固定值）
        :type x_apig_mode: str
        :param x_app_identity: 识别编号（固定值）
        :type x_app_identity: int
        """
        
        

        self._path = None
        self._user_agent = None
        self._x_apig_mode = None
        self._x_app_identity = None
        self.discriminator = None

        if path is not None:
            self.path = path
        if user_agent is not None:
            self.user_agent = user_agent
        if x_apig_mode is not None:
            self.x_apig_mode = x_apig_mode
        if x_app_identity is not None:
            self.x_app_identity = x_app_identity

    @property
    def path(self):
        r"""Gets the path of this ApiTestRequestHeader.

        请求路径

        :return: The path of this ApiTestRequestHeader.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        r"""Sets the path of this ApiTestRequestHeader.

        请求路径

        :param path: The path of this ApiTestRequestHeader.
        :type path: str
        """
        self._path = path

    @property
    def user_agent(self):
        r"""Gets the user_agent of this ApiTestRequestHeader.

        代理（固定值）

        :return: The user_agent of this ApiTestRequestHeader.
        :rtype: str
        """
        return self._user_agent

    @user_agent.setter
    def user_agent(self, user_agent):
        r"""Sets the user_agent of this ApiTestRequestHeader.

        代理（固定值）

        :param user_agent: The user_agent of this ApiTestRequestHeader.
        :type user_agent: str
        """
        self._user_agent = user_agent

    @property
    def x_apig_mode(self):
        r"""Gets the x_apig_mode of this ApiTestRequestHeader.

        请求方式（固定值）

        :return: The x_apig_mode of this ApiTestRequestHeader.
        :rtype: str
        """
        return self._x_apig_mode

    @x_apig_mode.setter
    def x_apig_mode(self, x_apig_mode):
        r"""Sets the x_apig_mode of this ApiTestRequestHeader.

        请求方式（固定值）

        :param x_apig_mode: The x_apig_mode of this ApiTestRequestHeader.
        :type x_apig_mode: str
        """
        self._x_apig_mode = x_apig_mode

    @property
    def x_app_identity(self):
        r"""Gets the x_app_identity of this ApiTestRequestHeader.

        识别编号（固定值）

        :return: The x_app_identity of this ApiTestRequestHeader.
        :rtype: int
        """
        return self._x_app_identity

    @x_app_identity.setter
    def x_app_identity(self, x_app_identity):
        r"""Sets the x_app_identity of this ApiTestRequestHeader.

        识别编号（固定值）

        :param x_app_identity: The x_app_identity of this ApiTestRequestHeader.
        :type x_app_identity: int
        """
        self._x_app_identity = x_app_identity

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
        if not isinstance(other, ApiTestRequestHeader):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
