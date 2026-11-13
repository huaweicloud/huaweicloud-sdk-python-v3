# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListResourceAssociationsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_id': 'list[str]',
        'resource_type': 'list[str]',
        'resource_project_id': 'str',
        'instance_id': 'list[str]',
        'instance_type': 'list[str]',
        'instance_project_id': 'str'
    }

    attribute_map = {
        'resource_id': 'resource_id',
        'resource_type': 'resource_type',
        'resource_project_id': 'resource_project_id',
        'instance_id': 'instance_id',
        'instance_type': 'instance_type',
        'instance_project_id': 'instance_project_id'
    }

    def __init__(self, resource_id=None, resource_type=None, resource_project_id=None, instance_id=None, instance_type=None, instance_project_id=None):
        r"""ListResourceAssociationsRequest

        The model defined in huaweicloud sdk

        :param resource_id: **参数解释**： 资源ID，填写后按照ID进行过滤，支持传入多个ID过滤。 **取值范围**： 弹性网卡/辅助弹性网卡的资源ID。
        :type resource_id: list[str]
        :param resource_type: **参数解释**： 资源的类型，填写后按照资源类型进行过滤，支持传入多个资源类型过滤。 **取值范围**： - port：弹性网卡。 - subeni：辅助弹性网卡。
        :type resource_type: list[str]
        :param resource_project_id: **参数解释**： 资源所属的项目ID，填写后按照项目ID进行过滤。 **取值范围**： 不涉及。
        :type resource_project_id: str
        :param instance_id: **参数解释**： 实例ID，填写后按照ID进行过滤，支持传入多个ID过滤。 **取值范围**： ELB实例的ID。
        :type instance_id: list[str]
        :param instance_type: **参数解释**： 实例的类型，填写后按照实例类型进行过滤，支持传入多个实例类型过滤。 **取值范围**： - ELB：ELB实例。
        :type instance_type: list[str]
        :param instance_project_id: **参数解释**： 实例所属的项目ID，填写后按照项目ID进行过滤。 **取值范围**： 不涉及。
        :type instance_project_id: str
        """
        
        

        self._resource_id = None
        self._resource_type = None
        self._resource_project_id = None
        self._instance_id = None
        self._instance_type = None
        self._instance_project_id = None
        self.discriminator = None

        if resource_id is not None:
            self.resource_id = resource_id
        if resource_type is not None:
            self.resource_type = resource_type
        if resource_project_id is not None:
            self.resource_project_id = resource_project_id
        if instance_id is not None:
            self.instance_id = instance_id
        if instance_type is not None:
            self.instance_type = instance_type
        if instance_project_id is not None:
            self.instance_project_id = instance_project_id

    @property
    def resource_id(self):
        r"""Gets the resource_id of this ListResourceAssociationsRequest.

        **参数解释**： 资源ID，填写后按照ID进行过滤，支持传入多个ID过滤。 **取值范围**： 弹性网卡/辅助弹性网卡的资源ID。

        :return: The resource_id of this ListResourceAssociationsRequest.
        :rtype: list[str]
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this ListResourceAssociationsRequest.

        **参数解释**： 资源ID，填写后按照ID进行过滤，支持传入多个ID过滤。 **取值范围**： 弹性网卡/辅助弹性网卡的资源ID。

        :param resource_id: The resource_id of this ListResourceAssociationsRequest.
        :type resource_id: list[str]
        """
        self._resource_id = resource_id

    @property
    def resource_type(self):
        r"""Gets the resource_type of this ListResourceAssociationsRequest.

        **参数解释**： 资源的类型，填写后按照资源类型进行过滤，支持传入多个资源类型过滤。 **取值范围**： - port：弹性网卡。 - subeni：辅助弹性网卡。

        :return: The resource_type of this ListResourceAssociationsRequest.
        :rtype: list[str]
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this ListResourceAssociationsRequest.

        **参数解释**： 资源的类型，填写后按照资源类型进行过滤，支持传入多个资源类型过滤。 **取值范围**： - port：弹性网卡。 - subeni：辅助弹性网卡。

        :param resource_type: The resource_type of this ListResourceAssociationsRequest.
        :type resource_type: list[str]
        """
        self._resource_type = resource_type

    @property
    def resource_project_id(self):
        r"""Gets the resource_project_id of this ListResourceAssociationsRequest.

        **参数解释**： 资源所属的项目ID，填写后按照项目ID进行过滤。 **取值范围**： 不涉及。

        :return: The resource_project_id of this ListResourceAssociationsRequest.
        :rtype: str
        """
        return self._resource_project_id

    @resource_project_id.setter
    def resource_project_id(self, resource_project_id):
        r"""Sets the resource_project_id of this ListResourceAssociationsRequest.

        **参数解释**： 资源所属的项目ID，填写后按照项目ID进行过滤。 **取值范围**： 不涉及。

        :param resource_project_id: The resource_project_id of this ListResourceAssociationsRequest.
        :type resource_project_id: str
        """
        self._resource_project_id = resource_project_id

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListResourceAssociationsRequest.

        **参数解释**： 实例ID，填写后按照ID进行过滤，支持传入多个ID过滤。 **取值范围**： ELB实例的ID。

        :return: The instance_id of this ListResourceAssociationsRequest.
        :rtype: list[str]
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListResourceAssociationsRequest.

        **参数解释**： 实例ID，填写后按照ID进行过滤，支持传入多个ID过滤。 **取值范围**： ELB实例的ID。

        :param instance_id: The instance_id of this ListResourceAssociationsRequest.
        :type instance_id: list[str]
        """
        self._instance_id = instance_id

    @property
    def instance_type(self):
        r"""Gets the instance_type of this ListResourceAssociationsRequest.

        **参数解释**： 实例的类型，填写后按照实例类型进行过滤，支持传入多个实例类型过滤。 **取值范围**： - ELB：ELB实例。

        :return: The instance_type of this ListResourceAssociationsRequest.
        :rtype: list[str]
        """
        return self._instance_type

    @instance_type.setter
    def instance_type(self, instance_type):
        r"""Sets the instance_type of this ListResourceAssociationsRequest.

        **参数解释**： 实例的类型，填写后按照实例类型进行过滤，支持传入多个实例类型过滤。 **取值范围**： - ELB：ELB实例。

        :param instance_type: The instance_type of this ListResourceAssociationsRequest.
        :type instance_type: list[str]
        """
        self._instance_type = instance_type

    @property
    def instance_project_id(self):
        r"""Gets the instance_project_id of this ListResourceAssociationsRequest.

        **参数解释**： 实例所属的项目ID，填写后按照项目ID进行过滤。 **取值范围**： 不涉及。

        :return: The instance_project_id of this ListResourceAssociationsRequest.
        :rtype: str
        """
        return self._instance_project_id

    @instance_project_id.setter
    def instance_project_id(self, instance_project_id):
        r"""Sets the instance_project_id of this ListResourceAssociationsRequest.

        **参数解释**： 实例所属的项目ID，填写后按照项目ID进行过滤。 **取值范围**： 不涉及。

        :param instance_project_id: The instance_project_id of this ListResourceAssociationsRequest.
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
        if not isinstance(other, ListResourceAssociationsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
