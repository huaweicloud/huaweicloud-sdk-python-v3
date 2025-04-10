# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAggregateResourceConfigResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_id': 'str',
        'aggregator_id': 'str',
        'aggregator_domain_id': 'str',
        'domain_id': 'str',
        'ep_id': 'str',
        'provider': 'str',
        'type': 'str',
        'name': 'str',
        'region_id': 'str',
        'project_id': 'str',
        'created': 'str',
        'updated': 'str',
        'tags': 'dict(str, str)',
        'properties': 'dict(str, object)'
    }

    attribute_map = {
        'resource_id': 'resource_id',
        'aggregator_id': 'aggregator_id',
        'aggregator_domain_id': 'aggregator_domain_id',
        'domain_id': 'domain_id',
        'ep_id': 'ep_id',
        'provider': 'provider',
        'type': 'type',
        'name': 'name',
        'region_id': 'region_id',
        'project_id': 'project_id',
        'created': 'created',
        'updated': 'updated',
        'tags': 'tags',
        'properties': 'properties'
    }

    def __init__(self, resource_id=None, aggregator_id=None, aggregator_domain_id=None, domain_id=None, ep_id=None, provider=None, type=None, name=None, region_id=None, project_id=None, created=None, updated=None, tags=None, properties=None):
        r"""ShowAggregateResourceConfigResponse

        The model defined in huaweicloud sdk

        :param resource_id: 资源ID。
        :type resource_id: str
        :param aggregator_id: 聚合器ID。
        :type aggregator_id: str
        :param aggregator_domain_id: 聚合器帐号。
        :type aggregator_domain_id: str
        :param domain_id: 聚合资源所属帐号的ID。
        :type domain_id: str
        :param ep_id: 企业项目ID。
        :type ep_id: str
        :param provider: 云服务名称。
        :type provider: str
        :param type: 资源类型。
        :type type: str
        :param name: 资源名称。
        :type name: str
        :param region_id: 区域ID。
        :type region_id: str
        :param project_id: Openstack中的项目ID。
        :type project_id: str
        :param created: 资源创建时间。
        :type created: str
        :param updated: 资源更新时间。
        :type updated: str
        :param tags: 资源标签。
        :type tags: dict(str, str)
        :param properties: 资源详细属性。
        :type properties: dict(str, object)
        """
        
        super(ShowAggregateResourceConfigResponse, self).__init__()

        self._resource_id = None
        self._aggregator_id = None
        self._aggregator_domain_id = None
        self._domain_id = None
        self._ep_id = None
        self._provider = None
        self._type = None
        self._name = None
        self._region_id = None
        self._project_id = None
        self._created = None
        self._updated = None
        self._tags = None
        self._properties = None
        self.discriminator = None

        if resource_id is not None:
            self.resource_id = resource_id
        if aggregator_id is not None:
            self.aggregator_id = aggregator_id
        if aggregator_domain_id is not None:
            self.aggregator_domain_id = aggregator_domain_id
        if domain_id is not None:
            self.domain_id = domain_id
        if ep_id is not None:
            self.ep_id = ep_id
        if provider is not None:
            self.provider = provider
        if type is not None:
            self.type = type
        if name is not None:
            self.name = name
        if region_id is not None:
            self.region_id = region_id
        if project_id is not None:
            self.project_id = project_id
        if created is not None:
            self.created = created
        if updated is not None:
            self.updated = updated
        if tags is not None:
            self.tags = tags
        if properties is not None:
            self.properties = properties

    @property
    def resource_id(self):
        r"""Gets the resource_id of this ShowAggregateResourceConfigResponse.

        资源ID。

        :return: The resource_id of this ShowAggregateResourceConfigResponse.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this ShowAggregateResourceConfigResponse.

        资源ID。

        :param resource_id: The resource_id of this ShowAggregateResourceConfigResponse.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def aggregator_id(self):
        r"""Gets the aggregator_id of this ShowAggregateResourceConfigResponse.

        聚合器ID。

        :return: The aggregator_id of this ShowAggregateResourceConfigResponse.
        :rtype: str
        """
        return self._aggregator_id

    @aggregator_id.setter
    def aggregator_id(self, aggregator_id):
        r"""Sets the aggregator_id of this ShowAggregateResourceConfigResponse.

        聚合器ID。

        :param aggregator_id: The aggregator_id of this ShowAggregateResourceConfigResponse.
        :type aggregator_id: str
        """
        self._aggregator_id = aggregator_id

    @property
    def aggregator_domain_id(self):
        r"""Gets the aggregator_domain_id of this ShowAggregateResourceConfigResponse.

        聚合器帐号。

        :return: The aggregator_domain_id of this ShowAggregateResourceConfigResponse.
        :rtype: str
        """
        return self._aggregator_domain_id

    @aggregator_domain_id.setter
    def aggregator_domain_id(self, aggregator_domain_id):
        r"""Sets the aggregator_domain_id of this ShowAggregateResourceConfigResponse.

        聚合器帐号。

        :param aggregator_domain_id: The aggregator_domain_id of this ShowAggregateResourceConfigResponse.
        :type aggregator_domain_id: str
        """
        self._aggregator_domain_id = aggregator_domain_id

    @property
    def domain_id(self):
        r"""Gets the domain_id of this ShowAggregateResourceConfigResponse.

        聚合资源所属帐号的ID。

        :return: The domain_id of this ShowAggregateResourceConfigResponse.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this ShowAggregateResourceConfigResponse.

        聚合资源所属帐号的ID。

        :param domain_id: The domain_id of this ShowAggregateResourceConfigResponse.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def ep_id(self):
        r"""Gets the ep_id of this ShowAggregateResourceConfigResponse.

        企业项目ID。

        :return: The ep_id of this ShowAggregateResourceConfigResponse.
        :rtype: str
        """
        return self._ep_id

    @ep_id.setter
    def ep_id(self, ep_id):
        r"""Sets the ep_id of this ShowAggregateResourceConfigResponse.

        企业项目ID。

        :param ep_id: The ep_id of this ShowAggregateResourceConfigResponse.
        :type ep_id: str
        """
        self._ep_id = ep_id

    @property
    def provider(self):
        r"""Gets the provider of this ShowAggregateResourceConfigResponse.

        云服务名称。

        :return: The provider of this ShowAggregateResourceConfigResponse.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        r"""Sets the provider of this ShowAggregateResourceConfigResponse.

        云服务名称。

        :param provider: The provider of this ShowAggregateResourceConfigResponse.
        :type provider: str
        """
        self._provider = provider

    @property
    def type(self):
        r"""Gets the type of this ShowAggregateResourceConfigResponse.

        资源类型。

        :return: The type of this ShowAggregateResourceConfigResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ShowAggregateResourceConfigResponse.

        资源类型。

        :param type: The type of this ShowAggregateResourceConfigResponse.
        :type type: str
        """
        self._type = type

    @property
    def name(self):
        r"""Gets the name of this ShowAggregateResourceConfigResponse.

        资源名称。

        :return: The name of this ShowAggregateResourceConfigResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowAggregateResourceConfigResponse.

        资源名称。

        :param name: The name of this ShowAggregateResourceConfigResponse.
        :type name: str
        """
        self._name = name

    @property
    def region_id(self):
        r"""Gets the region_id of this ShowAggregateResourceConfigResponse.

        区域ID。

        :return: The region_id of this ShowAggregateResourceConfigResponse.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this ShowAggregateResourceConfigResponse.

        区域ID。

        :param region_id: The region_id of this ShowAggregateResourceConfigResponse.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def project_id(self):
        r"""Gets the project_id of this ShowAggregateResourceConfigResponse.

        Openstack中的项目ID。

        :return: The project_id of this ShowAggregateResourceConfigResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ShowAggregateResourceConfigResponse.

        Openstack中的项目ID。

        :param project_id: The project_id of this ShowAggregateResourceConfigResponse.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def created(self):
        r"""Gets the created of this ShowAggregateResourceConfigResponse.

        资源创建时间。

        :return: The created of this ShowAggregateResourceConfigResponse.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        r"""Sets the created of this ShowAggregateResourceConfigResponse.

        资源创建时间。

        :param created: The created of this ShowAggregateResourceConfigResponse.
        :type created: str
        """
        self._created = created

    @property
    def updated(self):
        r"""Gets the updated of this ShowAggregateResourceConfigResponse.

        资源更新时间。

        :return: The updated of this ShowAggregateResourceConfigResponse.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        r"""Sets the updated of this ShowAggregateResourceConfigResponse.

        资源更新时间。

        :param updated: The updated of this ShowAggregateResourceConfigResponse.
        :type updated: str
        """
        self._updated = updated

    @property
    def tags(self):
        r"""Gets the tags of this ShowAggregateResourceConfigResponse.

        资源标签。

        :return: The tags of this ShowAggregateResourceConfigResponse.
        :rtype: dict(str, str)
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ShowAggregateResourceConfigResponse.

        资源标签。

        :param tags: The tags of this ShowAggregateResourceConfigResponse.
        :type tags: dict(str, str)
        """
        self._tags = tags

    @property
    def properties(self):
        r"""Gets the properties of this ShowAggregateResourceConfigResponse.

        资源详细属性。

        :return: The properties of this ShowAggregateResourceConfigResponse.
        :rtype: dict(str, object)
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        r"""Sets the properties of this ShowAggregateResourceConfigResponse.

        资源详细属性。

        :param properties: The properties of this ShowAggregateResourceConfigResponse.
        :type properties: dict(str, object)
        """
        self._properties = properties

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
        if not isinstance(other, ShowAggregateResourceConfigResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
