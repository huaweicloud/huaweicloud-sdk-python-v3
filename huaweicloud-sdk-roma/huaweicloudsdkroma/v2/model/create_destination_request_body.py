# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateDestinationRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'destination_type': 'int',
        'app_id': 'str',
        'destination_name': 'str',
        'topic': 'str',
        'server': 'str',
        'token': 'str',
        'tag': 'str',
        'mqs_sasl_ssl': 'bool',
        'user_name': 'str',
        'password': 'str'
    }

    attribute_map = {
        'destination_type': 'destination_type',
        'app_id': 'app_id',
        'destination_name': 'destination_name',
        'topic': 'topic',
        'server': 'server',
        'token': 'token',
        'tag': 'tag',
        'mqs_sasl_ssl': 'mqs_sasl_ssl',
        'user_name': 'user_name',
        'password': 'password'
    }

    def __init__(self, destination_type=None, app_id=None, destination_name=None, topic=None, server=None, token=None, tag=None, mqs_sasl_ssl=None, user_name=None, password=None):
        """CreateDestinationRequestBody

        The model defined in huaweicloud sdk

        :param destination_type: 操作类型，枚举值:0-目标端为本ROMA实例内MQS，； 7-目标端为设备
        :type destination_type: int
        :param app_id: 应用ID，目标端为0时需明确对方的APP_ID
        :type app_id: str
        :param destination_name: 目标数据源名称
        :type destination_name: str
        :param topic: 目标数据源主题，从MQS服务中获取已有topic
        :type topic: str
        :param server: 目标端数据源服务，连接地址
        :type server: str
        :param token: 目标端数据源token
        :type token: str
        :param tag: 目标数据源标签
        :type tag: str
        :param mqs_sasl_ssl: 目标端数据源MQS的SASL字段是否需要支持SSL加密
        :type mqs_sasl_ssl: bool
        :param user_name: 目标数据源用户名
        :type user_name: str
        :param password: 目标数据源密码
        :type password: str
        """
        
        

        self._destination_type = None
        self._app_id = None
        self._destination_name = None
        self._topic = None
        self._server = None
        self._token = None
        self._tag = None
        self._mqs_sasl_ssl = None
        self._user_name = None
        self._password = None
        self.discriminator = None

        self.destination_type = destination_type
        if app_id is not None:
            self.app_id = app_id
        if destination_name is not None:
            self.destination_name = destination_name
        self.topic = topic
        if server is not None:
            self.server = server
        if token is not None:
            self.token = token
        if tag is not None:
            self.tag = tag
        if mqs_sasl_ssl is not None:
            self.mqs_sasl_ssl = mqs_sasl_ssl
        if user_name is not None:
            self.user_name = user_name
        if password is not None:
            self.password = password

    @property
    def destination_type(self):
        """Gets the destination_type of this CreateDestinationRequestBody.

        操作类型，枚举值:0-目标端为本ROMA实例内MQS，； 7-目标端为设备

        :return: The destination_type of this CreateDestinationRequestBody.
        :rtype: int
        """
        return self._destination_type

    @destination_type.setter
    def destination_type(self, destination_type):
        """Sets the destination_type of this CreateDestinationRequestBody.

        操作类型，枚举值:0-目标端为本ROMA实例内MQS，； 7-目标端为设备

        :param destination_type: The destination_type of this CreateDestinationRequestBody.
        :type destination_type: int
        """
        self._destination_type = destination_type

    @property
    def app_id(self):
        """Gets the app_id of this CreateDestinationRequestBody.

        应用ID，目标端为0时需明确对方的APP_ID

        :return: The app_id of this CreateDestinationRequestBody.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this CreateDestinationRequestBody.

        应用ID，目标端为0时需明确对方的APP_ID

        :param app_id: The app_id of this CreateDestinationRequestBody.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def destination_name(self):
        """Gets the destination_name of this CreateDestinationRequestBody.

        目标数据源名称

        :return: The destination_name of this CreateDestinationRequestBody.
        :rtype: str
        """
        return self._destination_name

    @destination_name.setter
    def destination_name(self, destination_name):
        """Sets the destination_name of this CreateDestinationRequestBody.

        目标数据源名称

        :param destination_name: The destination_name of this CreateDestinationRequestBody.
        :type destination_name: str
        """
        self._destination_name = destination_name

    @property
    def topic(self):
        """Gets the topic of this CreateDestinationRequestBody.

        目标数据源主题，从MQS服务中获取已有topic

        :return: The topic of this CreateDestinationRequestBody.
        :rtype: str
        """
        return self._topic

    @topic.setter
    def topic(self, topic):
        """Sets the topic of this CreateDestinationRequestBody.

        目标数据源主题，从MQS服务中获取已有topic

        :param topic: The topic of this CreateDestinationRequestBody.
        :type topic: str
        """
        self._topic = topic

    @property
    def server(self):
        """Gets the server of this CreateDestinationRequestBody.

        目标端数据源服务，连接地址

        :return: The server of this CreateDestinationRequestBody.
        :rtype: str
        """
        return self._server

    @server.setter
    def server(self, server):
        """Sets the server of this CreateDestinationRequestBody.

        目标端数据源服务，连接地址

        :param server: The server of this CreateDestinationRequestBody.
        :type server: str
        """
        self._server = server

    @property
    def token(self):
        """Gets the token of this CreateDestinationRequestBody.

        目标端数据源token

        :return: The token of this CreateDestinationRequestBody.
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this CreateDestinationRequestBody.

        目标端数据源token

        :param token: The token of this CreateDestinationRequestBody.
        :type token: str
        """
        self._token = token

    @property
    def tag(self):
        """Gets the tag of this CreateDestinationRequestBody.

        目标数据源标签

        :return: The tag of this CreateDestinationRequestBody.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this CreateDestinationRequestBody.

        目标数据源标签

        :param tag: The tag of this CreateDestinationRequestBody.
        :type tag: str
        """
        self._tag = tag

    @property
    def mqs_sasl_ssl(self):
        """Gets the mqs_sasl_ssl of this CreateDestinationRequestBody.

        目标端数据源MQS的SASL字段是否需要支持SSL加密

        :return: The mqs_sasl_ssl of this CreateDestinationRequestBody.
        :rtype: bool
        """
        return self._mqs_sasl_ssl

    @mqs_sasl_ssl.setter
    def mqs_sasl_ssl(self, mqs_sasl_ssl):
        """Sets the mqs_sasl_ssl of this CreateDestinationRequestBody.

        目标端数据源MQS的SASL字段是否需要支持SSL加密

        :param mqs_sasl_ssl: The mqs_sasl_ssl of this CreateDestinationRequestBody.
        :type mqs_sasl_ssl: bool
        """
        self._mqs_sasl_ssl = mqs_sasl_ssl

    @property
    def user_name(self):
        """Gets the user_name of this CreateDestinationRequestBody.

        目标数据源用户名

        :return: The user_name of this CreateDestinationRequestBody.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this CreateDestinationRequestBody.

        目标数据源用户名

        :param user_name: The user_name of this CreateDestinationRequestBody.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def password(self):
        """Gets the password of this CreateDestinationRequestBody.

        目标数据源密码

        :return: The password of this CreateDestinationRequestBody.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this CreateDestinationRequestBody.

        目标数据源密码

        :param password: The password of this CreateDestinationRequestBody.
        :type password: str
        """
        self._password = password

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
        if not isinstance(other, CreateDestinationRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
