# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRemoteDbRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'server_ip': 'str',
        'server_port': 'str',
        'login_user_name': 'str',
        'login_user_password': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'server_ip': 'server_ip',
        'server_port': 'server_port',
        'login_user_name': 'login_user_name',
        'login_user_password': 'login_user_password',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, server_ip=None, server_port=None, login_user_name=None, login_user_password=None, offset=None, limit=None):
        r"""ListRemoteDbRequestBody

        The model defined in huaweicloud sdk

        :param server_ip: 服务器ip。
        :type server_ip: str
        :param server_port: 端口号。
        :type server_port: str
        :param login_user_name: 登录名。
        :type login_user_name: str
        :param login_user_password: 登录密码。要求密码长度在5~64位之间。
        :type login_user_password: str
        :param offset: 索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。
        :type offset: int
        :param limit: 查询记录数。默认为10，不能为负数，最小值为1，最大值为100。
        :type limit: int
        """
        
        

        self._server_ip = None
        self._server_port = None
        self._login_user_name = None
        self._login_user_password = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.server_ip = server_ip
        self.server_port = server_port
        self.login_user_name = login_user_name
        self.login_user_password = login_user_password
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def server_ip(self):
        r"""Gets the server_ip of this ListRemoteDbRequestBody.

        服务器ip。

        :return: The server_ip of this ListRemoteDbRequestBody.
        :rtype: str
        """
        return self._server_ip

    @server_ip.setter
    def server_ip(self, server_ip):
        r"""Sets the server_ip of this ListRemoteDbRequestBody.

        服务器ip。

        :param server_ip: The server_ip of this ListRemoteDbRequestBody.
        :type server_ip: str
        """
        self._server_ip = server_ip

    @property
    def server_port(self):
        r"""Gets the server_port of this ListRemoteDbRequestBody.

        端口号。

        :return: The server_port of this ListRemoteDbRequestBody.
        :rtype: str
        """
        return self._server_port

    @server_port.setter
    def server_port(self, server_port):
        r"""Sets the server_port of this ListRemoteDbRequestBody.

        端口号。

        :param server_port: The server_port of this ListRemoteDbRequestBody.
        :type server_port: str
        """
        self._server_port = server_port

    @property
    def login_user_name(self):
        r"""Gets the login_user_name of this ListRemoteDbRequestBody.

        登录名。

        :return: The login_user_name of this ListRemoteDbRequestBody.
        :rtype: str
        """
        return self._login_user_name

    @login_user_name.setter
    def login_user_name(self, login_user_name):
        r"""Sets the login_user_name of this ListRemoteDbRequestBody.

        登录名。

        :param login_user_name: The login_user_name of this ListRemoteDbRequestBody.
        :type login_user_name: str
        """
        self._login_user_name = login_user_name

    @property
    def login_user_password(self):
        r"""Gets the login_user_password of this ListRemoteDbRequestBody.

        登录密码。要求密码长度在5~64位之间。

        :return: The login_user_password of this ListRemoteDbRequestBody.
        :rtype: str
        """
        return self._login_user_password

    @login_user_password.setter
    def login_user_password(self, login_user_password):
        r"""Sets the login_user_password of this ListRemoteDbRequestBody.

        登录密码。要求密码长度在5~64位之间。

        :param login_user_password: The login_user_password of this ListRemoteDbRequestBody.
        :type login_user_password: str
        """
        self._login_user_password = login_user_password

    @property
    def offset(self):
        r"""Gets the offset of this ListRemoteDbRequestBody.

        索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。

        :return: The offset of this ListRemoteDbRequestBody.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListRemoteDbRequestBody.

        索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。

        :param offset: The offset of this ListRemoteDbRequestBody.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListRemoteDbRequestBody.

        查询记录数。默认为10，不能为负数，最小值为1，最大值为100。

        :return: The limit of this ListRemoteDbRequestBody.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListRemoteDbRequestBody.

        查询记录数。默认为10，不能为负数，最小值为1，最大值为100。

        :param limit: The limit of this ListRemoteDbRequestBody.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListRemoteDbRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
