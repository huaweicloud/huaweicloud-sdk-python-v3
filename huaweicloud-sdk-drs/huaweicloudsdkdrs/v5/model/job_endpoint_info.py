# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobEndpointInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'db_type': 'str',
        'endpoint_type': 'str',
        'endpoint_role': 'str',
        'endpoint': 'BaseEndpoint',
        'cloud': 'CloudBaseInfo',
        'vpc': 'CloudVpcInfo',
        'config': 'BaseEndpointConfig',
        'ssl': 'EndpointSslConfig'
    }

    attribute_map = {
        'db_type': 'db_type',
        'endpoint_type': 'endpoint_type',
        'endpoint_role': 'endpoint_role',
        'endpoint': 'endpoint',
        'cloud': 'cloud',
        'vpc': 'vpc',
        'config': 'config',
        'ssl': 'ssl'
    }

    def __init__(self, db_type=None, endpoint_type=None, endpoint_role=None, endpoint=None, cloud=None, vpc=None, config=None, ssl=None):
        """JobEndpointInfo

        The model defined in huaweicloud sdk

        :param db_type: 数据库类型。取值：  - oracle：Oracle。 - gaussdbv5：GaussDB分布式版。
        :type db_type: str
        :param endpoint_type: 数据库实例类型。取值：  - offline：自建数据库。 - ecs：华为云ECS自建数据库。 - cloud：华为云数据库。
        :type endpoint_type: str
        :param endpoint_role: 数据库实例角色。取值： - so：源库。 - ta：目标库。
        :type endpoint_role: str
        :param endpoint: 
        :type endpoint: :class:`huaweicloudsdkdrs.v5.BaseEndpoint`
        :param cloud: 
        :type cloud: :class:`huaweicloudsdkdrs.v5.CloudBaseInfo`
        :param vpc: 
        :type vpc: :class:`huaweicloudsdkdrs.v5.CloudVpcInfo`
        :param config: 
        :type config: :class:`huaweicloudsdkdrs.v5.BaseEndpointConfig`
        :param ssl: 
        :type ssl: :class:`huaweicloudsdkdrs.v5.EndpointSslConfig`
        """
        
        

        self._db_type = None
        self._endpoint_type = None
        self._endpoint_role = None
        self._endpoint = None
        self._cloud = None
        self._vpc = None
        self._config = None
        self._ssl = None
        self.discriminator = None

        self.db_type = db_type
        self.endpoint_type = endpoint_type
        self.endpoint_role = endpoint_role
        self.endpoint = endpoint
        if cloud is not None:
            self.cloud = cloud
        if vpc is not None:
            self.vpc = vpc
        if config is not None:
            self.config = config
        if ssl is not None:
            self.ssl = ssl

    @property
    def db_type(self):
        """Gets the db_type of this JobEndpointInfo.

        数据库类型。取值：  - oracle：Oracle。 - gaussdbv5：GaussDB分布式版。

        :return: The db_type of this JobEndpointInfo.
        :rtype: str
        """
        return self._db_type

    @db_type.setter
    def db_type(self, db_type):
        """Sets the db_type of this JobEndpointInfo.

        数据库类型。取值：  - oracle：Oracle。 - gaussdbv5：GaussDB分布式版。

        :param db_type: The db_type of this JobEndpointInfo.
        :type db_type: str
        """
        self._db_type = db_type

    @property
    def endpoint_type(self):
        """Gets the endpoint_type of this JobEndpointInfo.

        数据库实例类型。取值：  - offline：自建数据库。 - ecs：华为云ECS自建数据库。 - cloud：华为云数据库。

        :return: The endpoint_type of this JobEndpointInfo.
        :rtype: str
        """
        return self._endpoint_type

    @endpoint_type.setter
    def endpoint_type(self, endpoint_type):
        """Sets the endpoint_type of this JobEndpointInfo.

        数据库实例类型。取值：  - offline：自建数据库。 - ecs：华为云ECS自建数据库。 - cloud：华为云数据库。

        :param endpoint_type: The endpoint_type of this JobEndpointInfo.
        :type endpoint_type: str
        """
        self._endpoint_type = endpoint_type

    @property
    def endpoint_role(self):
        """Gets the endpoint_role of this JobEndpointInfo.

        数据库实例角色。取值： - so：源库。 - ta：目标库。

        :return: The endpoint_role of this JobEndpointInfo.
        :rtype: str
        """
        return self._endpoint_role

    @endpoint_role.setter
    def endpoint_role(self, endpoint_role):
        """Sets the endpoint_role of this JobEndpointInfo.

        数据库实例角色。取值： - so：源库。 - ta：目标库。

        :param endpoint_role: The endpoint_role of this JobEndpointInfo.
        :type endpoint_role: str
        """
        self._endpoint_role = endpoint_role

    @property
    def endpoint(self):
        """Gets the endpoint of this JobEndpointInfo.

        :return: The endpoint of this JobEndpointInfo.
        :rtype: :class:`huaweicloudsdkdrs.v5.BaseEndpoint`
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint):
        """Sets the endpoint of this JobEndpointInfo.

        :param endpoint: The endpoint of this JobEndpointInfo.
        :type endpoint: :class:`huaweicloudsdkdrs.v5.BaseEndpoint`
        """
        self._endpoint = endpoint

    @property
    def cloud(self):
        """Gets the cloud of this JobEndpointInfo.

        :return: The cloud of this JobEndpointInfo.
        :rtype: :class:`huaweicloudsdkdrs.v5.CloudBaseInfo`
        """
        return self._cloud

    @cloud.setter
    def cloud(self, cloud):
        """Sets the cloud of this JobEndpointInfo.

        :param cloud: The cloud of this JobEndpointInfo.
        :type cloud: :class:`huaweicloudsdkdrs.v5.CloudBaseInfo`
        """
        self._cloud = cloud

    @property
    def vpc(self):
        """Gets the vpc of this JobEndpointInfo.

        :return: The vpc of this JobEndpointInfo.
        :rtype: :class:`huaweicloudsdkdrs.v5.CloudVpcInfo`
        """
        return self._vpc

    @vpc.setter
    def vpc(self, vpc):
        """Sets the vpc of this JobEndpointInfo.

        :param vpc: The vpc of this JobEndpointInfo.
        :type vpc: :class:`huaweicloudsdkdrs.v5.CloudVpcInfo`
        """
        self._vpc = vpc

    @property
    def config(self):
        """Gets the config of this JobEndpointInfo.

        :return: The config of this JobEndpointInfo.
        :rtype: :class:`huaweicloudsdkdrs.v5.BaseEndpointConfig`
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this JobEndpointInfo.

        :param config: The config of this JobEndpointInfo.
        :type config: :class:`huaweicloudsdkdrs.v5.BaseEndpointConfig`
        """
        self._config = config

    @property
    def ssl(self):
        """Gets the ssl of this JobEndpointInfo.

        :return: The ssl of this JobEndpointInfo.
        :rtype: :class:`huaweicloudsdkdrs.v5.EndpointSslConfig`
        """
        return self._ssl

    @ssl.setter
    def ssl(self, ssl):
        """Sets the ssl of this JobEndpointInfo.

        :param ssl: The ssl of this JobEndpointInfo.
        :type ssl: :class:`huaweicloudsdkdrs.v5.EndpointSslConfig`
        """
        self._ssl = ssl

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
        if not isinstance(other, JobEndpointInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
