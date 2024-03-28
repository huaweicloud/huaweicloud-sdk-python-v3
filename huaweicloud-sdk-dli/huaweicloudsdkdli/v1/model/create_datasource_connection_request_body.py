# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateDatasourceConnectionRequestBody:

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
        'service': 'str',
        'security_group_id': 'str',
        'network_id': 'str',
        'url': 'str',
        'tags': 'list[Tag]'
    }

    attribute_map = {
        'name': 'name',
        'service': 'service',
        'security_group_id': 'security_group_id',
        'network_id': 'network_id',
        'url': 'url',
        'tags': 'tags'
    }

    def __init__(self, name=None, service=None, security_group_id=None, network_id=None, url=None, tags=None):
        """CreateDatasourceConnectionRequestBody

        The model defined in huaweicloud sdk

        :param name: 连接名称。
        :type name: str
        :param service: 服务名称，目前为CloudTable.OpenTSDB/CloudTable，MRS.OPENTSDB，DWS，RDS，CSS。 说明： 大小写不敏感。
        :type service: str
        :param security_group_id: 用户指定安全组ID，即为需要建立连接的服务所在的安全组。
        :type security_group_id: str
        :param network_id: 对应服务的子网网络ID，即为需要建立连接的服务所在的子网。
        :type network_id: str
        :param url: 对应服务对外提供的访问url。长度不能超过512个字符。
        :type url: str
        :param tags: 标签
        :type tags: list[:class:`huaweicloudsdkdli.v1.Tag`]
        """
        
        

        self._name = None
        self._service = None
        self._security_group_id = None
        self._network_id = None
        self._url = None
        self._tags = None
        self.discriminator = None

        self.name = name
        self.service = service
        self.security_group_id = security_group_id
        self.network_id = network_id
        self.url = url
        if tags is not None:
            self.tags = tags

    @property
    def name(self):
        """Gets the name of this CreateDatasourceConnectionRequestBody.

        连接名称。

        :return: The name of this CreateDatasourceConnectionRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateDatasourceConnectionRequestBody.

        连接名称。

        :param name: The name of this CreateDatasourceConnectionRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def service(self):
        """Gets the service of this CreateDatasourceConnectionRequestBody.

        服务名称，目前为CloudTable.OpenTSDB/CloudTable，MRS.OPENTSDB，DWS，RDS，CSS。 说明： 大小写不敏感。

        :return: The service of this CreateDatasourceConnectionRequestBody.
        :rtype: str
        """
        return self._service

    @service.setter
    def service(self, service):
        """Sets the service of this CreateDatasourceConnectionRequestBody.

        服务名称，目前为CloudTable.OpenTSDB/CloudTable，MRS.OPENTSDB，DWS，RDS，CSS。 说明： 大小写不敏感。

        :param service: The service of this CreateDatasourceConnectionRequestBody.
        :type service: str
        """
        self._service = service

    @property
    def security_group_id(self):
        """Gets the security_group_id of this CreateDatasourceConnectionRequestBody.

        用户指定安全组ID，即为需要建立连接的服务所在的安全组。

        :return: The security_group_id of this CreateDatasourceConnectionRequestBody.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        """Sets the security_group_id of this CreateDatasourceConnectionRequestBody.

        用户指定安全组ID，即为需要建立连接的服务所在的安全组。

        :param security_group_id: The security_group_id of this CreateDatasourceConnectionRequestBody.
        :type security_group_id: str
        """
        self._security_group_id = security_group_id

    @property
    def network_id(self):
        """Gets the network_id of this CreateDatasourceConnectionRequestBody.

        对应服务的子网网络ID，即为需要建立连接的服务所在的子网。

        :return: The network_id of this CreateDatasourceConnectionRequestBody.
        :rtype: str
        """
        return self._network_id

    @network_id.setter
    def network_id(self, network_id):
        """Sets the network_id of this CreateDatasourceConnectionRequestBody.

        对应服务的子网网络ID，即为需要建立连接的服务所在的子网。

        :param network_id: The network_id of this CreateDatasourceConnectionRequestBody.
        :type network_id: str
        """
        self._network_id = network_id

    @property
    def url(self):
        """Gets the url of this CreateDatasourceConnectionRequestBody.

        对应服务对外提供的访问url。长度不能超过512个字符。

        :return: The url of this CreateDatasourceConnectionRequestBody.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this CreateDatasourceConnectionRequestBody.

        对应服务对外提供的访问url。长度不能超过512个字符。

        :param url: The url of this CreateDatasourceConnectionRequestBody.
        :type url: str
        """
        self._url = url

    @property
    def tags(self):
        """Gets the tags of this CreateDatasourceConnectionRequestBody.

        标签

        :return: The tags of this CreateDatasourceConnectionRequestBody.
        :rtype: list[:class:`huaweicloudsdkdli.v1.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CreateDatasourceConnectionRequestBody.

        标签

        :param tags: The tags of this CreateDatasourceConnectionRequestBody.
        :type tags: list[:class:`huaweicloudsdkdli.v1.Tag`]
        """
        self._tags = tags

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
        if not isinstance(other, CreateDatasourceConnectionRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
