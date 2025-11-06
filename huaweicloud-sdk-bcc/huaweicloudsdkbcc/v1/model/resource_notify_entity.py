# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourceNotifyEntity:

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
        'region_id': 'str',
        'project_id': 'str',
        'ep_id': 'str',
        'created': 'str',
        'updated': 'str',
        'provisioning_state': 'str',
        'tags': 'dict(str, str)',
        'properties': 'dict(str, object)'
    }

    attribute_map = {
        'name': 'name',
        'region_id': 'region_id',
        'project_id': 'project_id',
        'ep_id': 'ep_id',
        'created': 'created',
        'updated': 'updated',
        'provisioning_state': 'provisioning_state',
        'tags': 'tags',
        'properties': 'properties'
    }

    def __init__(self, name=None, region_id=None, project_id=None, ep_id=None, created=None, updated=None, provisioning_state=None, tags=None, properties=None):
        r"""ResourceNotifyEntity

        The model defined in huaweicloud sdk

        :param name: 资源名称
        :type name: str
        :param region_id: 区域ID
        :type region_id: str
        :param project_id: Openstack中的项目ID
        :type project_id: str
        :param ep_id: 企业项目ID
        :type ep_id: str
        :param created: 资源创建时间
        :type created: str
        :param updated: 资源更新时间
        :type updated: str
        :param provisioning_state: 资源操作状态
        :type provisioning_state: str
        :param tags: 资源标签
        :type tags: dict(str, str)
        :param properties: 资源详细属性
        :type properties: dict(str, object)
        """
        
        

        self._name = None
        self._region_id = None
        self._project_id = None
        self._ep_id = None
        self._created = None
        self._updated = None
        self._provisioning_state = None
        self._tags = None
        self._properties = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if region_id is not None:
            self.region_id = region_id
        if project_id is not None:
            self.project_id = project_id
        if ep_id is not None:
            self.ep_id = ep_id
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
    def name(self):
        r"""Gets the name of this ResourceNotifyEntity.

        资源名称

        :return: The name of this ResourceNotifyEntity.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ResourceNotifyEntity.

        资源名称

        :param name: The name of this ResourceNotifyEntity.
        :type name: str
        """
        self._name = name

    @property
    def region_id(self):
        r"""Gets the region_id of this ResourceNotifyEntity.

        区域ID

        :return: The region_id of this ResourceNotifyEntity.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this ResourceNotifyEntity.

        区域ID

        :param region_id: The region_id of this ResourceNotifyEntity.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def project_id(self):
        r"""Gets the project_id of this ResourceNotifyEntity.

        Openstack中的项目ID

        :return: The project_id of this ResourceNotifyEntity.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ResourceNotifyEntity.

        Openstack中的项目ID

        :param project_id: The project_id of this ResourceNotifyEntity.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def ep_id(self):
        r"""Gets the ep_id of this ResourceNotifyEntity.

        企业项目ID

        :return: The ep_id of this ResourceNotifyEntity.
        :rtype: str
        """
        return self._ep_id

    @ep_id.setter
    def ep_id(self, ep_id):
        r"""Sets the ep_id of this ResourceNotifyEntity.

        企业项目ID

        :param ep_id: The ep_id of this ResourceNotifyEntity.
        :type ep_id: str
        """
        self._ep_id = ep_id

    @property
    def created(self):
        r"""Gets the created of this ResourceNotifyEntity.

        资源创建时间

        :return: The created of this ResourceNotifyEntity.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        r"""Sets the created of this ResourceNotifyEntity.

        资源创建时间

        :param created: The created of this ResourceNotifyEntity.
        :type created: str
        """
        self._created = created

    @property
    def updated(self):
        r"""Gets the updated of this ResourceNotifyEntity.

        资源更新时间

        :return: The updated of this ResourceNotifyEntity.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        r"""Sets the updated of this ResourceNotifyEntity.

        资源更新时间

        :param updated: The updated of this ResourceNotifyEntity.
        :type updated: str
        """
        self._updated = updated

    @property
    def provisioning_state(self):
        r"""Gets the provisioning_state of this ResourceNotifyEntity.

        资源操作状态

        :return: The provisioning_state of this ResourceNotifyEntity.
        :rtype: str
        """
        return self._provisioning_state

    @provisioning_state.setter
    def provisioning_state(self, provisioning_state):
        r"""Sets the provisioning_state of this ResourceNotifyEntity.

        资源操作状态

        :param provisioning_state: The provisioning_state of this ResourceNotifyEntity.
        :type provisioning_state: str
        """
        self._provisioning_state = provisioning_state

    @property
    def tags(self):
        r"""Gets the tags of this ResourceNotifyEntity.

        资源标签

        :return: The tags of this ResourceNotifyEntity.
        :rtype: dict(str, str)
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ResourceNotifyEntity.

        资源标签

        :param tags: The tags of this ResourceNotifyEntity.
        :type tags: dict(str, str)
        """
        self._tags = tags

    @property
    def properties(self):
        r"""Gets the properties of this ResourceNotifyEntity.

        资源详细属性

        :return: The properties of this ResourceNotifyEntity.
        :rtype: dict(str, object)
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        r"""Sets the properties of this ResourceNotifyEntity.

        资源详细属性

        :param properties: The properties of this ResourceNotifyEntity.
        :type properties: dict(str, object)
        """
        self._properties = properties

    def to_dict(self):
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
        if not isinstance(other, ResourceNotifyEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
