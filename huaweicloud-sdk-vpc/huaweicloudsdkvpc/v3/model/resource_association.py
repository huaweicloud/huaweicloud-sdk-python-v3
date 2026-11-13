# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourceAssociation:

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
        'resource_id': 'str',
        'resource_type': 'str',
        'resource_project_id': 'str',
        'instance_id': 'str',
        'instance_type': 'str',
        'instance_project_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'resource_id': 'resource_id',
        'resource_type': 'resource_type',
        'resource_project_id': 'resource_project_id',
        'instance_id': 'instance_id',
        'instance_type': 'instance_type',
        'instance_project_id': 'instance_project_id'
    }

    def __init__(self, id=None, resource_id=None, resource_type=None, resource_project_id=None, instance_id=None, instance_type=None, instance_project_id=None):
        r"""ResourceAssociation

        The model defined in huaweicloud sdk

        :param id: **参数解释**： 资源和实例关联关系的ID。 **取值范围**： 不涉及。
        :type id: str
        :param resource_id: **参数解释**： 资源ID。 **取值范围**： 不涉及。
        :type resource_id: str
        :param resource_type: **参数解释**： 资源类型。 **取值范围**： - port：弹性网卡。 - subeni：辅助弹性网卡。
        :type resource_type: str
        :param resource_project_id: **参数解释**： 资源所属的项目ID。 **取值范围**： 不涉及。
        :type resource_project_id: str
        :param instance_id: **参数解释**： 实例ID。 **取值范围**： 不涉及。
        :type instance_id: str
        :param instance_type: **参数解释**： 实例类型。 **取值范围**： - ELB：ELB实例。
        :type instance_type: str
        :param instance_project_id: **参数解释**： 实例所属的项目ID。 **取值范围**： 不涉及。
        :type instance_project_id: str
        """
        
        

        self._id = None
        self._resource_id = None
        self._resource_type = None
        self._resource_project_id = None
        self._instance_id = None
        self._instance_type = None
        self._instance_project_id = None
        self.discriminator = None

        self.id = id
        self.resource_id = resource_id
        self.resource_type = resource_type
        self.resource_project_id = resource_project_id
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.instance_project_id = instance_project_id

    @property
    def id(self):
        r"""Gets the id of this ResourceAssociation.

        **参数解释**： 资源和实例关联关系的ID。 **取值范围**： 不涉及。

        :return: The id of this ResourceAssociation.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ResourceAssociation.

        **参数解释**： 资源和实例关联关系的ID。 **取值范围**： 不涉及。

        :param id: The id of this ResourceAssociation.
        :type id: str
        """
        self._id = id

    @property
    def resource_id(self):
        r"""Gets the resource_id of this ResourceAssociation.

        **参数解释**： 资源ID。 **取值范围**： 不涉及。

        :return: The resource_id of this ResourceAssociation.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this ResourceAssociation.

        **参数解释**： 资源ID。 **取值范围**： 不涉及。

        :param resource_id: The resource_id of this ResourceAssociation.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def resource_type(self):
        r"""Gets the resource_type of this ResourceAssociation.

        **参数解释**： 资源类型。 **取值范围**： - port：弹性网卡。 - subeni：辅助弹性网卡。

        :return: The resource_type of this ResourceAssociation.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this ResourceAssociation.

        **参数解释**： 资源类型。 **取值范围**： - port：弹性网卡。 - subeni：辅助弹性网卡。

        :param resource_type: The resource_type of this ResourceAssociation.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def resource_project_id(self):
        r"""Gets the resource_project_id of this ResourceAssociation.

        **参数解释**： 资源所属的项目ID。 **取值范围**： 不涉及。

        :return: The resource_project_id of this ResourceAssociation.
        :rtype: str
        """
        return self._resource_project_id

    @resource_project_id.setter
    def resource_project_id(self, resource_project_id):
        r"""Sets the resource_project_id of this ResourceAssociation.

        **参数解释**： 资源所属的项目ID。 **取值范围**： 不涉及。

        :param resource_project_id: The resource_project_id of this ResourceAssociation.
        :type resource_project_id: str
        """
        self._resource_project_id = resource_project_id

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ResourceAssociation.

        **参数解释**： 实例ID。 **取值范围**： 不涉及。

        :return: The instance_id of this ResourceAssociation.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ResourceAssociation.

        **参数解释**： 实例ID。 **取值范围**： 不涉及。

        :param instance_id: The instance_id of this ResourceAssociation.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def instance_type(self):
        r"""Gets the instance_type of this ResourceAssociation.

        **参数解释**： 实例类型。 **取值范围**： - ELB：ELB实例。

        :return: The instance_type of this ResourceAssociation.
        :rtype: str
        """
        return self._instance_type

    @instance_type.setter
    def instance_type(self, instance_type):
        r"""Sets the instance_type of this ResourceAssociation.

        **参数解释**： 实例类型。 **取值范围**： - ELB：ELB实例。

        :param instance_type: The instance_type of this ResourceAssociation.
        :type instance_type: str
        """
        self._instance_type = instance_type

    @property
    def instance_project_id(self):
        r"""Gets the instance_project_id of this ResourceAssociation.

        **参数解释**： 实例所属的项目ID。 **取值范围**： 不涉及。

        :return: The instance_project_id of this ResourceAssociation.
        :rtype: str
        """
        return self._instance_project_id

    @instance_project_id.setter
    def instance_project_id(self, instance_project_id):
        r"""Sets the instance_project_id of this ResourceAssociation.

        **参数解释**： 实例所属的项目ID。 **取值范围**： 不涉及。

        :param instance_project_id: The instance_project_id of this ResourceAssociation.
        :type instance_project_id: str
        """
        self._instance_project_id = instance_project_id

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
        if not isinstance(other, ResourceAssociation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
