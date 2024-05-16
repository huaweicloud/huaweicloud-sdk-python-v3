# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CountTrackedResourcesRequest:

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
        'type': 'list[str]',
        'region_id': 'list[str]',
        'ep_id': 'list[str]',
        'project_id': 'list[str]',
        'tags': 'list[str]',
        'resource_deleted': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'type': 'type',
        'region_id': 'region_id',
        'ep_id': 'ep_id',
        'project_id': 'project_id',
        'tags': 'tags',
        'resource_deleted': 'resource_deleted'
    }

    def __init__(self, id=None, name=None, type=None, region_id=None, ep_id=None, project_id=None, tags=None, resource_deleted=None):
        """CountTrackedResourcesRequest

        The model defined in huaweicloud sdk

        :param id: 资源ID
        :type id: str
        :param name: 资源名称
        :type name: str
        :param type: 资源类型（provider.type）
        :type type: list[str]
        :param region_id: 区域ID列表
        :type region_id: list[str]
        :param ep_id: 企业项目ID列表
        :type ep_id: list[str]
        :param project_id: 项目ID
        :type project_id: list[str]
        :param tags: 标签列表
        :type tags: list[str]
        :param resource_deleted: 是否查询已删除的资源。默认为false，不查询已删除的资源
        :type resource_deleted: bool
        """
        
        

        self._id = None
        self._name = None
        self._type = None
        self._region_id = None
        self._ep_id = None
        self._project_id = None
        self._tags = None
        self._resource_deleted = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if region_id is not None:
            self.region_id = region_id
        if ep_id is not None:
            self.ep_id = ep_id
        if project_id is not None:
            self.project_id = project_id
        if tags is not None:
            self.tags = tags
        if resource_deleted is not None:
            self.resource_deleted = resource_deleted

    @property
    def id(self):
        """Gets the id of this CountTrackedResourcesRequest.

        资源ID

        :return: The id of this CountTrackedResourcesRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CountTrackedResourcesRequest.

        资源ID

        :param id: The id of this CountTrackedResourcesRequest.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this CountTrackedResourcesRequest.

        资源名称

        :return: The name of this CountTrackedResourcesRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CountTrackedResourcesRequest.

        资源名称

        :param name: The name of this CountTrackedResourcesRequest.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        """Gets the type of this CountTrackedResourcesRequest.

        资源类型（provider.type）

        :return: The type of this CountTrackedResourcesRequest.
        :rtype: list[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CountTrackedResourcesRequest.

        资源类型（provider.type）

        :param type: The type of this CountTrackedResourcesRequest.
        :type type: list[str]
        """
        self._type = type

    @property
    def region_id(self):
        """Gets the region_id of this CountTrackedResourcesRequest.

        区域ID列表

        :return: The region_id of this CountTrackedResourcesRequest.
        :rtype: list[str]
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this CountTrackedResourcesRequest.

        区域ID列表

        :param region_id: The region_id of this CountTrackedResourcesRequest.
        :type region_id: list[str]
        """
        self._region_id = region_id

    @property
    def ep_id(self):
        """Gets the ep_id of this CountTrackedResourcesRequest.

        企业项目ID列表

        :return: The ep_id of this CountTrackedResourcesRequest.
        :rtype: list[str]
        """
        return self._ep_id

    @ep_id.setter
    def ep_id(self, ep_id):
        """Sets the ep_id of this CountTrackedResourcesRequest.

        企业项目ID列表

        :param ep_id: The ep_id of this CountTrackedResourcesRequest.
        :type ep_id: list[str]
        """
        self._ep_id = ep_id

    @property
    def project_id(self):
        """Gets the project_id of this CountTrackedResourcesRequest.

        项目ID

        :return: The project_id of this CountTrackedResourcesRequest.
        :rtype: list[str]
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this CountTrackedResourcesRequest.

        项目ID

        :param project_id: The project_id of this CountTrackedResourcesRequest.
        :type project_id: list[str]
        """
        self._project_id = project_id

    @property
    def tags(self):
        """Gets the tags of this CountTrackedResourcesRequest.

        标签列表

        :return: The tags of this CountTrackedResourcesRequest.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CountTrackedResourcesRequest.

        标签列表

        :param tags: The tags of this CountTrackedResourcesRequest.
        :type tags: list[str]
        """
        self._tags = tags

    @property
    def resource_deleted(self):
        """Gets the resource_deleted of this CountTrackedResourcesRequest.

        是否查询已删除的资源。默认为false，不查询已删除的资源

        :return: The resource_deleted of this CountTrackedResourcesRequest.
        :rtype: bool
        """
        return self._resource_deleted

    @resource_deleted.setter
    def resource_deleted(self, resource_deleted):
        """Sets the resource_deleted of this CountTrackedResourcesRequest.

        是否查询已删除的资源。默认为false，不查询已删除的资源

        :param resource_deleted: The resource_deleted of this CountTrackedResourcesRequest.
        :type resource_deleted: bool
        """
        self._resource_deleted = resource_deleted

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
        if not isinstance(other, CountTrackedResourcesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
