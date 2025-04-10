# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateConnectionReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'db_type': 'str',
        'config': 'ConnectionConfig',
        'description': 'str',
        'endpoint': 'BaseEndpoint',
        'vpc': 'CloudVpcInfo',
        'ssl': 'EndpointSslConfig',
        'cloud': 'CloudBaseInfo',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'db_type': 'db_type',
        'config': 'config',
        'description': 'description',
        'endpoint': 'endpoint',
        'vpc': 'vpc',
        'ssl': 'ssl',
        'cloud': 'cloud',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, name=None, db_type=None, config=None, description=None, endpoint=None, vpc=None, ssl=None, cloud=None, enterprise_project_id=None):
        r"""CreateConnectionReq

        The model defined in huaweicloud sdk

        :param name: 连接名称。 约束：连接名称在4位到50位之间，不区分大小写，可以包含字母、数字、中划线或下划线，不能包括其他特殊字符。
        :type name: str
        :param db_type: 连接类型，包含： - mysql - postgresql - mongodb - oracle
        :type db_type: str
        :param config: 
        :type config: :class:`huaweicloudsdkdrs.v5.ConnectionConfig`
        :param description: 描述，长度不能超过255个字符。
        :type description: str
        :param endpoint: 
        :type endpoint: :class:`huaweicloudsdkdrs.v5.BaseEndpoint`
        :param vpc: 
        :type vpc: :class:`huaweicloudsdkdrs.v5.CloudVpcInfo`
        :param ssl: 
        :type ssl: :class:`huaweicloudsdkdrs.v5.EndpointSslConfig`
        :param cloud: 
        :type cloud: :class:`huaweicloudsdkdrs.v5.CloudBaseInfo`
        :param enterprise_project_id: 企业项目ID。
        :type enterprise_project_id: str
        """
        
        

        self._name = None
        self._db_type = None
        self._config = None
        self._description = None
        self._endpoint = None
        self._vpc = None
        self._ssl = None
        self._cloud = None
        self._enterprise_project_id = None
        self.discriminator = None

        self.name = name
        self.db_type = db_type
        if config is not None:
            self.config = config
        if description is not None:
            self.description = description
        self.endpoint = endpoint
        if vpc is not None:
            self.vpc = vpc
        if ssl is not None:
            self.ssl = ssl
        if cloud is not None:
            self.cloud = cloud
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def name(self):
        r"""Gets the name of this CreateConnectionReq.

        连接名称。 约束：连接名称在4位到50位之间，不区分大小写，可以包含字母、数字、中划线或下划线，不能包括其他特殊字符。

        :return: The name of this CreateConnectionReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateConnectionReq.

        连接名称。 约束：连接名称在4位到50位之间，不区分大小写，可以包含字母、数字、中划线或下划线，不能包括其他特殊字符。

        :param name: The name of this CreateConnectionReq.
        :type name: str
        """
        self._name = name

    @property
    def db_type(self):
        r"""Gets the db_type of this CreateConnectionReq.

        连接类型，包含： - mysql - postgresql - mongodb - oracle

        :return: The db_type of this CreateConnectionReq.
        :rtype: str
        """
        return self._db_type

    @db_type.setter
    def db_type(self, db_type):
        r"""Sets the db_type of this CreateConnectionReq.

        连接类型，包含： - mysql - postgresql - mongodb - oracle

        :param db_type: The db_type of this CreateConnectionReq.
        :type db_type: str
        """
        self._db_type = db_type

    @property
    def config(self):
        r"""Gets the config of this CreateConnectionReq.

        :return: The config of this CreateConnectionReq.
        :rtype: :class:`huaweicloudsdkdrs.v5.ConnectionConfig`
        """
        return self._config

    @config.setter
    def config(self, config):
        r"""Sets the config of this CreateConnectionReq.

        :param config: The config of this CreateConnectionReq.
        :type config: :class:`huaweicloudsdkdrs.v5.ConnectionConfig`
        """
        self._config = config

    @property
    def description(self):
        r"""Gets the description of this CreateConnectionReq.

        描述，长度不能超过255个字符。

        :return: The description of this CreateConnectionReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateConnectionReq.

        描述，长度不能超过255个字符。

        :param description: The description of this CreateConnectionReq.
        :type description: str
        """
        self._description = description

    @property
    def endpoint(self):
        r"""Gets the endpoint of this CreateConnectionReq.

        :return: The endpoint of this CreateConnectionReq.
        :rtype: :class:`huaweicloudsdkdrs.v5.BaseEndpoint`
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint):
        r"""Sets the endpoint of this CreateConnectionReq.

        :param endpoint: The endpoint of this CreateConnectionReq.
        :type endpoint: :class:`huaweicloudsdkdrs.v5.BaseEndpoint`
        """
        self._endpoint = endpoint

    @property
    def vpc(self):
        r"""Gets the vpc of this CreateConnectionReq.

        :return: The vpc of this CreateConnectionReq.
        :rtype: :class:`huaweicloudsdkdrs.v5.CloudVpcInfo`
        """
        return self._vpc

    @vpc.setter
    def vpc(self, vpc):
        r"""Sets the vpc of this CreateConnectionReq.

        :param vpc: The vpc of this CreateConnectionReq.
        :type vpc: :class:`huaweicloudsdkdrs.v5.CloudVpcInfo`
        """
        self._vpc = vpc

    @property
    def ssl(self):
        r"""Gets the ssl of this CreateConnectionReq.

        :return: The ssl of this CreateConnectionReq.
        :rtype: :class:`huaweicloudsdkdrs.v5.EndpointSslConfig`
        """
        return self._ssl

    @ssl.setter
    def ssl(self, ssl):
        r"""Sets the ssl of this CreateConnectionReq.

        :param ssl: The ssl of this CreateConnectionReq.
        :type ssl: :class:`huaweicloudsdkdrs.v5.EndpointSslConfig`
        """
        self._ssl = ssl

    @property
    def cloud(self):
        r"""Gets the cloud of this CreateConnectionReq.

        :return: The cloud of this CreateConnectionReq.
        :rtype: :class:`huaweicloudsdkdrs.v5.CloudBaseInfo`
        """
        return self._cloud

    @cloud.setter
    def cloud(self, cloud):
        r"""Sets the cloud of this CreateConnectionReq.

        :param cloud: The cloud of this CreateConnectionReq.
        :type cloud: :class:`huaweicloudsdkdrs.v5.CloudBaseInfo`
        """
        self._cloud = cloud

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this CreateConnectionReq.

        企业项目ID。

        :return: The enterprise_project_id of this CreateConnectionReq.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this CreateConnectionReq.

        企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this CreateConnectionReq.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, CreateConnectionReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
