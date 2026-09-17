# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LoginResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'connection_id': 'str',
        'instance_name': 'str',
        'instance_id': 'str',
        'login_user': 'str',
        'database_name': 'str',
        'engine_type': 'str'
    }

    attribute_map = {
        'connection_id': 'connection_id',
        'instance_name': 'instance_name',
        'instance_id': 'instance_id',
        'login_user': 'login_user',
        'database_name': 'database_name',
        'engine_type': 'engine_type'
    }

    def __init__(self, connection_id=None, instance_name=None, instance_id=None, login_user=None, database_name=None, engine_type=None):
        r"""LoginResponse

        The model defined in huaweicloud sdk

        :param connection_id: 连接ID
        :type connection_id: str
        :param instance_name: 实例名
        :type instance_name: str
        :param instance_id: 实例ID
        :type instance_id: str
        :param login_user: 登录名
        :type login_user: str
        :param database_name: 登录的数据库名
        :type database_name: str
        :param engine_type: 引擎类型
        :type engine_type: str
        """
        
        super().__init__()

        self._connection_id = None
        self._instance_name = None
        self._instance_id = None
        self._login_user = None
        self._database_name = None
        self._engine_type = None
        self.discriminator = None

        if connection_id is not None:
            self.connection_id = connection_id
        if instance_name is not None:
            self.instance_name = instance_name
        if instance_id is not None:
            self.instance_id = instance_id
        if login_user is not None:
            self.login_user = login_user
        if database_name is not None:
            self.database_name = database_name
        if engine_type is not None:
            self.engine_type = engine_type

    @property
    def connection_id(self):
        r"""Gets the connection_id of this LoginResponse.

        连接ID

        :return: The connection_id of this LoginResponse.
        :rtype: str
        """
        return self._connection_id

    @connection_id.setter
    def connection_id(self, connection_id):
        r"""Sets the connection_id of this LoginResponse.

        连接ID

        :param connection_id: The connection_id of this LoginResponse.
        :type connection_id: str
        """
        self._connection_id = connection_id

    @property
    def instance_name(self):
        r"""Gets the instance_name of this LoginResponse.

        实例名

        :return: The instance_name of this LoginResponse.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        r"""Sets the instance_name of this LoginResponse.

        实例名

        :param instance_name: The instance_name of this LoginResponse.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def instance_id(self):
        r"""Gets the instance_id of this LoginResponse.

        实例ID

        :return: The instance_id of this LoginResponse.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this LoginResponse.

        实例ID

        :param instance_id: The instance_id of this LoginResponse.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def login_user(self):
        r"""Gets the login_user of this LoginResponse.

        登录名

        :return: The login_user of this LoginResponse.
        :rtype: str
        """
        return self._login_user

    @login_user.setter
    def login_user(self, login_user):
        r"""Sets the login_user of this LoginResponse.

        登录名

        :param login_user: The login_user of this LoginResponse.
        :type login_user: str
        """
        self._login_user = login_user

    @property
    def database_name(self):
        r"""Gets the database_name of this LoginResponse.

        登录的数据库名

        :return: The database_name of this LoginResponse.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        r"""Sets the database_name of this LoginResponse.

        登录的数据库名

        :param database_name: The database_name of this LoginResponse.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def engine_type(self):
        r"""Gets the engine_type of this LoginResponse.

        引擎类型

        :return: The engine_type of this LoginResponse.
        :rtype: str
        """
        return self._engine_type

    @engine_type.setter
    def engine_type(self, engine_type):
        r"""Sets the engine_type of this LoginResponse.

        引擎类型

        :param engine_type: The engine_type of this LoginResponse.
        :type engine_type: str
        """
        self._engine_type = engine_type

    def to_dict(self):
        import warnings
        warnings.warn("LoginResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, LoginResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
