# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ShowResourceByIdResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'provider': 'str',
        'type': 'str',
        'region_id': 'str',
        'project_id': 'str',
        'project_name': 'str',
        'ep_id': 'str',
        'ep_name': 'str',
        'checksum': 'str',
        'created': 'str',
        'updated': 'str',
        'provisioning_state': 'str',
        'tags': 'dict(str, str)',
        'properties': 'dict(str, object)'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'provider': 'provider',
        'type': 'type',
        'region_id': 'region_id',
        'project_id': 'project_id',
        'project_name': 'project_name',
        'ep_id': 'ep_id',
        'ep_name': 'ep_name',
        'checksum': 'checksum',
        'created': 'created',
        'updated': 'updated',
        'provisioning_state': 'provisioning_state',
        'tags': 'tags',
        'properties': 'properties'
    }

    def __init__(self, id=None, name=None, provider=None, type=None, region_id=None, project_id=None, project_name=None, ep_id=None, ep_name=None, checksum=None, created=None, updated=None, provisioning_state=None, tags=None, properties=None):
        """ShowResourceByIdResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._id = None
        self._name = None
        self._provider = None
        self._type = None
        self._region_id = None
        self._project_id = None
        self._project_name = None
        self._ep_id = None
        self._ep_name = None
        self._checksum = None
        self._created = None
        self._updated = None
        self._provisioning_state = None
        self._tags = None
        self._properties = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if provider is not None:
            self.provider = provider
        if type is not None:
            self.type = type
        if region_id is not None:
            self.region_id = region_id
        if project_id is not None:
            self.project_id = project_id
        if project_name is not None:
            self.project_name = project_name
        if ep_id is not None:
            self.ep_id = ep_id
        if ep_name is not None:
            self.ep_name = ep_name
        if checksum is not None:
            self.checksum = checksum
        if created is not None:
            self.created = created
        if updated is not None:
            self.updated = updated
        if provisioning_state is not None:
            self.provisioning_state = provisioning_state
        if tags is not None:
            self.tags = tags
        if properties is not None:
            self.properties = properties

    @property
    def id(self):
        """Gets the id of this ShowResourceByIdResponse.

        资源id

        :return: The id of this ShowResourceByIdResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowResourceByIdResponse.

        资源id

        :param id: The id of this ShowResourceByIdResponse.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ShowResourceByIdResponse.

        资源名称

        :return: The name of this ShowResourceByIdResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowResourceByIdResponse.

        资源名称

        :param name: The name of this ShowResourceByIdResponse.
        :type: str
        """
        self._name = name

    @property
    def provider(self):
        """Gets the provider of this ShowResourceByIdResponse.

        云服务名称

        :return: The provider of this ShowResourceByIdResponse.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this ShowResourceByIdResponse.

        云服务名称

        :param provider: The provider of this ShowResourceByIdResponse.
        :type: str
        """
        self._provider = provider

    @property
    def type(self):
        """Gets the type of this ShowResourceByIdResponse.

        资源类型

        :return: The type of this ShowResourceByIdResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ShowResourceByIdResponse.

        资源类型

        :param type: The type of this ShowResourceByIdResponse.
        :type: str
        """
        self._type = type

    @property
    def region_id(self):
        """Gets the region_id of this ShowResourceByIdResponse.

        region id

        :return: The region_id of this ShowResourceByIdResponse.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this ShowResourceByIdResponse.

        region id

        :param region_id: The region_id of this ShowResourceByIdResponse.
        :type: str
        """
        self._region_id = region_id

    @property
    def project_id(self):
        """Gets the project_id of this ShowResourceByIdResponse.

        Openstack中的project id

        :return: The project_id of this ShowResourceByIdResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ShowResourceByIdResponse.

        Openstack中的project id

        :param project_id: The project_id of this ShowResourceByIdResponse.
        :type: str
        """
        self._project_id = project_id

    @property
    def project_name(self):
        """Gets the project_name of this ShowResourceByIdResponse.

        Openstack中的project名称

        :return: The project_name of this ShowResourceByIdResponse.
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this ShowResourceByIdResponse.

        Openstack中的project名称

        :param project_name: The project_name of this ShowResourceByIdResponse.
        :type: str
        """
        self._project_name = project_name

    @property
    def ep_id(self):
        """Gets the ep_id of this ShowResourceByIdResponse.

        企业项目id

        :return: The ep_id of this ShowResourceByIdResponse.
        :rtype: str
        """
        return self._ep_id

    @ep_id.setter
    def ep_id(self, ep_id):
        """Sets the ep_id of this ShowResourceByIdResponse.

        企业项目id

        :param ep_id: The ep_id of this ShowResourceByIdResponse.
        :type: str
        """
        self._ep_id = ep_id

    @property
    def ep_name(self):
        """Gets the ep_name of this ShowResourceByIdResponse.

        企业项目名称

        :return: The ep_name of this ShowResourceByIdResponse.
        :rtype: str
        """
        return self._ep_name

    @ep_name.setter
    def ep_name(self, ep_name):
        """Sets the ep_name of this ShowResourceByIdResponse.

        企业项目名称

        :param ep_name: The ep_name of this ShowResourceByIdResponse.
        :type: str
        """
        self._ep_name = ep_name

    @property
    def checksum(self):
        """Gets the checksum of this ShowResourceByIdResponse.

        资源详情摘要

        :return: The checksum of this ShowResourceByIdResponse.
        :rtype: str
        """
        return self._checksum

    @checksum.setter
    def checksum(self, checksum):
        """Sets the checksum of this ShowResourceByIdResponse.

        资源详情摘要

        :param checksum: The checksum of this ShowResourceByIdResponse.
        :type: str
        """
        self._checksum = checksum

    @property
    def created(self):
        """Gets the created of this ShowResourceByIdResponse.

        资源创建时间

        :return: The created of this ShowResourceByIdResponse.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this ShowResourceByIdResponse.

        资源创建时间

        :param created: The created of this ShowResourceByIdResponse.
        :type: str
        """
        self._created = created

    @property
    def updated(self):
        """Gets the updated of this ShowResourceByIdResponse.

        资源更新时间

        :return: The updated of this ShowResourceByIdResponse.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this ShowResourceByIdResponse.

        资源更新时间

        :param updated: The updated of this ShowResourceByIdResponse.
        :type: str
        """
        self._updated = updated

    @property
    def provisioning_state(self):
        """Gets the provisioning_state of this ShowResourceByIdResponse.

        资源发放状态

        :return: The provisioning_state of this ShowResourceByIdResponse.
        :rtype: str
        """
        return self._provisioning_state

    @provisioning_state.setter
    def provisioning_state(self, provisioning_state):
        """Sets the provisioning_state of this ShowResourceByIdResponse.

        资源发放状态

        :param provisioning_state: The provisioning_state of this ShowResourceByIdResponse.
        :type: str
        """
        self._provisioning_state = provisioning_state

    @property
    def tags(self):
        """Gets the tags of this ShowResourceByIdResponse.

        资源Tag

        :return: The tags of this ShowResourceByIdResponse.
        :rtype: dict(str, str)
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ShowResourceByIdResponse.

        资源Tag

        :param tags: The tags of this ShowResourceByIdResponse.
        :type: dict(str, str)
        """
        self._tags = tags

    @property
    def properties(self):
        """Gets the properties of this ShowResourceByIdResponse.

        资源详细属性

        :return: The properties of this ShowResourceByIdResponse.
        :rtype: dict(str, object)
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this ShowResourceByIdResponse.

        资源详细属性

        :param properties: The properties of this ShowResourceByIdResponse.
        :type: dict(str, object)
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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ShowResourceByIdResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
