# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateConnectionReq:

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
        r"""UpdateConnectionReq

        The model defined in huaweicloud sdk

        :param name: 连接名称。
        :type name: str
        :param db_type: 数据库类型。
        :type db_type: str
        :param config: 
        :type config: :class:`huaweicloudsdkdrs.v5.ConnectionConfig`
        :param description: 连接描述。
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

        if name is not None:
            self.name = name
        if db_type is not None:
            self.db_type = db_type
        if config is not None:
            self.config = config
        if description is not None:
            self.description = description
        if endpoint is not None:
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
        r"""Gets the name of this UpdateConnectionReq.

        连接名称。

        :return: The name of this UpdateConnectionReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateConnectionReq.

        连接名称。

        :param name: The name of this UpdateConnectionReq.
        :type name: str
        """
        self._name = name

    @property
    def db_type(self):
        r"""Gets the db_type of this UpdateConnectionReq.

        数据库类型。

        :return: The db_type of this UpdateConnectionReq.
        :rtype: str
        """
        return self._db_type

    @db_type.setter
    def db_type(self, db_type):
        r"""Sets the db_type of this UpdateConnectionReq.

        数据库类型。

        :param db_type: The db_type of this UpdateConnectionReq.
        :type db_type: str
        """
        self._db_type = db_type

    @property
    def config(self):
        r"""Gets the config of this UpdateConnectionReq.

        :return: The config of this UpdateConnectionReq.
        :rtype: :class:`huaweicloudsdkdrs.v5.ConnectionConfig`
        """
        return self._config

    @config.setter
    def config(self, config):
        r"""Sets the config of this UpdateConnectionReq.

        :param config: The config of this UpdateConnectionReq.
        :type config: :class:`huaweicloudsdkdrs.v5.ConnectionConfig`
        """
        self._config = config

    @property
    def description(self):
        r"""Gets the description of this UpdateConnectionReq.

        连接描述。

        :return: The description of this UpdateConnectionReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateConnectionReq.

        连接描述。

        :param description: The description of this UpdateConnectionReq.
        :type description: str
        """
        self._description = description

    @property
    def endpoint(self):
        r"""Gets the endpoint of this UpdateConnectionReq.

        :return: The endpoint of this UpdateConnectionReq.
        :rtype: :class:`huaweicloudsdkdrs.v5.BaseEndpoint`
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint):
        r"""Sets the endpoint of this UpdateConnectionReq.

        :param endpoint: The endpoint of this UpdateConnectionReq.
        :type endpoint: :class:`huaweicloudsdkdrs.v5.BaseEndpoint`
        """
        self._endpoint = endpoint

    @property
    def vpc(self):
        r"""Gets the vpc of this UpdateConnectionReq.

        :return: The vpc of this UpdateConnectionReq.
        :rtype: :class:`huaweicloudsdkdrs.v5.CloudVpcInfo`
        """
        return self._vpc

    @vpc.setter
    def vpc(self, vpc):
        r"""Sets the vpc of this UpdateConnectionReq.

        :param vpc: The vpc of this UpdateConnectionReq.
        :type vpc: :class:`huaweicloudsdkdrs.v5.CloudVpcInfo`
        """
        self._vpc = vpc

    @property
    def ssl(self):
        r"""Gets the ssl of this UpdateConnectionReq.

        :return: The ssl of this UpdateConnectionReq.
        :rtype: :class:`huaweicloudsdkdrs.v5.EndpointSslConfig`
        """
        return self._ssl

    @ssl.setter
    def ssl(self, ssl):
        r"""Sets the ssl of this UpdateConnectionReq.

        :param ssl: The ssl of this UpdateConnectionReq.
        :type ssl: :class:`huaweicloudsdkdrs.v5.EndpointSslConfig`
        """
        self._ssl = ssl

    @property
    def cloud(self):
        r"""Gets the cloud of this UpdateConnectionReq.

        :return: The cloud of this UpdateConnectionReq.
        :rtype: :class:`huaweicloudsdkdrs.v5.CloudBaseInfo`
        """
        return self._cloud

    @cloud.setter
    def cloud(self, cloud):
        r"""Sets the cloud of this UpdateConnectionReq.

        :param cloud: The cloud of this UpdateConnectionReq.
        :type cloud: :class:`huaweicloudsdkdrs.v5.CloudBaseInfo`
        """
        self._cloud = cloud

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this UpdateConnectionReq.

        企业项目ID。

        :return: The enterprise_project_id of this UpdateConnectionReq.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this UpdateConnectionReq.

        企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this UpdateConnectionReq.
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
        if not isinstance(other, UpdateConnectionReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
