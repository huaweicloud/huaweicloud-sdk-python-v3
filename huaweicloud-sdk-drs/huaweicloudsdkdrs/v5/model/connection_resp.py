# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConnectionResp:

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
        'name': 'str',
        'create_time': 'int',
        'db_type': 'str',
        'config': 'ConnectionConfig',
        'endpoint': 'BaseEndpoint',
        'vpc': 'CloudVpcInfo',
        'ssl': 'EndpointSslConfig',
        'enterprise_project_id': 'str',
        'description': 'str'
    }

    attribute_map = {
        'connection_id': 'connection_id',
        'name': 'name',
        'create_time': 'create_time',
        'db_type': 'db_type',
        'config': 'config',
        'endpoint': 'endpoint',
        'vpc': 'vpc',
        'ssl': 'ssl',
        'enterprise_project_id': 'enterprise_project_id',
        'description': 'description'
    }

    def __init__(self, connection_id=None, name=None, create_time=None, db_type=None, config=None, endpoint=None, vpc=None, ssl=None, enterprise_project_id=None, description=None):
        r"""ConnectionResp

        The model defined in huaweicloud sdk

        :param connection_id: 连接ID。
        :type connection_id: str
        :param name: 连接名称。
        :type name: str
        :param create_time: 连接创建时间，格式为时间戳。
        :type create_time: int
        :param db_type: 连接类型。
        :type db_type: str
        :param config: 
        :type config: :class:`huaweicloudsdkdrs.v5.ConnectionConfig`
        :param endpoint: 
        :type endpoint: :class:`huaweicloudsdkdrs.v5.BaseEndpoint`
        :param vpc: 
        :type vpc: :class:`huaweicloudsdkdrs.v5.CloudVpcInfo`
        :param ssl: 
        :type ssl: :class:`huaweicloudsdkdrs.v5.EndpointSslConfig`
        :param enterprise_project_id: 企业项目ID。
        :type enterprise_project_id: str
        :param description: 描述。
        :type description: str
        """
        
        

        self._connection_id = None
        self._name = None
        self._create_time = None
        self._db_type = None
        self._config = None
        self._endpoint = None
        self._vpc = None
        self._ssl = None
        self._enterprise_project_id = None
        self._description = None
        self.discriminator = None

        self.connection_id = connection_id
        self.name = name
        self.create_time = create_time
        self.db_type = db_type
        if config is not None:
            self.config = config
        self.endpoint = endpoint
        if vpc is not None:
            self.vpc = vpc
        if ssl is not None:
            self.ssl = ssl
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if description is not None:
            self.description = description

    @property
    def connection_id(self):
        r"""Gets the connection_id of this ConnectionResp.

        连接ID。

        :return: The connection_id of this ConnectionResp.
        :rtype: str
        """
        return self._connection_id

    @connection_id.setter
    def connection_id(self, connection_id):
        r"""Sets the connection_id of this ConnectionResp.

        连接ID。

        :param connection_id: The connection_id of this ConnectionResp.
        :type connection_id: str
        """
        self._connection_id = connection_id

    @property
    def name(self):
        r"""Gets the name of this ConnectionResp.

        连接名称。

        :return: The name of this ConnectionResp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ConnectionResp.

        连接名称。

        :param name: The name of this ConnectionResp.
        :type name: str
        """
        self._name = name

    @property
    def create_time(self):
        r"""Gets the create_time of this ConnectionResp.

        连接创建时间，格式为时间戳。

        :return: The create_time of this ConnectionResp.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ConnectionResp.

        连接创建时间，格式为时间戳。

        :param create_time: The create_time of this ConnectionResp.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def db_type(self):
        r"""Gets the db_type of this ConnectionResp.

        连接类型。

        :return: The db_type of this ConnectionResp.
        :rtype: str
        """
        return self._db_type

    @db_type.setter
    def db_type(self, db_type):
        r"""Sets the db_type of this ConnectionResp.

        连接类型。

        :param db_type: The db_type of this ConnectionResp.
        :type db_type: str
        """
        self._db_type = db_type

    @property
    def config(self):
        r"""Gets the config of this ConnectionResp.

        :return: The config of this ConnectionResp.
        :rtype: :class:`huaweicloudsdkdrs.v5.ConnectionConfig`
        """
        return self._config

    @config.setter
    def config(self, config):
        r"""Sets the config of this ConnectionResp.

        :param config: The config of this ConnectionResp.
        :type config: :class:`huaweicloudsdkdrs.v5.ConnectionConfig`
        """
        self._config = config

    @property
    def endpoint(self):
        r"""Gets the endpoint of this ConnectionResp.

        :return: The endpoint of this ConnectionResp.
        :rtype: :class:`huaweicloudsdkdrs.v5.BaseEndpoint`
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint):
        r"""Sets the endpoint of this ConnectionResp.

        :param endpoint: The endpoint of this ConnectionResp.
        :type endpoint: :class:`huaweicloudsdkdrs.v5.BaseEndpoint`
        """
        self._endpoint = endpoint

    @property
    def vpc(self):
        r"""Gets the vpc of this ConnectionResp.

        :return: The vpc of this ConnectionResp.
        :rtype: :class:`huaweicloudsdkdrs.v5.CloudVpcInfo`
        """
        return self._vpc

    @vpc.setter
    def vpc(self, vpc):
        r"""Sets the vpc of this ConnectionResp.

        :param vpc: The vpc of this ConnectionResp.
        :type vpc: :class:`huaweicloudsdkdrs.v5.CloudVpcInfo`
        """
        self._vpc = vpc

    @property
    def ssl(self):
        r"""Gets the ssl of this ConnectionResp.

        :return: The ssl of this ConnectionResp.
        :rtype: :class:`huaweicloudsdkdrs.v5.EndpointSslConfig`
        """
        return self._ssl

    @ssl.setter
    def ssl(self, ssl):
        r"""Sets the ssl of this ConnectionResp.

        :param ssl: The ssl of this ConnectionResp.
        :type ssl: :class:`huaweicloudsdkdrs.v5.EndpointSslConfig`
        """
        self._ssl = ssl

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ConnectionResp.

        企业项目ID。

        :return: The enterprise_project_id of this ConnectionResp.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ConnectionResp.

        企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this ConnectionResp.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def description(self):
        r"""Gets the description of this ConnectionResp.

        描述。

        :return: The description of this ConnectionResp.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ConnectionResp.

        描述。

        :param description: The description of this ConnectionResp.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, ConnectionResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
