# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Privilege:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'role_id': 'str',
        'role_name': 'str',
        'role_chinese_name': 'str',
        'project_id': 'str',
        'area_service_id': 'str',
        'granted_object_path': 'str',
        'granted_object_type_id': 'str',
        'operations': 'str',
        'operations_index': 'list[int]'
    }

    attribute_map = {
        'role_id': 'role_id',
        'role_name': 'role_name',
        'role_chinese_name': 'role_chinese_name',
        'project_id': 'project_id',
        'area_service_id': 'area_service_id',
        'granted_object_path': 'granted_object_path',
        'granted_object_type_id': 'granted_object_type_id',
        'operations': 'operations',
        'operations_index': 'operations_index'
    }

    def __init__(self, role_id=None, role_name=None, role_chinese_name=None, project_id=None, area_service_id=None, granted_object_path=None, granted_object_type_id=None, operations=None, operations_index=None):
        r"""Privilege

        The model defined in huaweicloud sdk

        :param role_id: **参数解释**: 角色id。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 无。 
        :type role_id: str
        :param role_name: **参数解释**: 角色名称。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 无。 
        :type role_name: str
        :param role_chinese_name: **参数解释**: 角色中文名。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 无。 
        :type role_chinese_name: str
        :param project_id: **参数解释**: 项目id。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 无。 
        :type project_id: str
        :param area_service_id: **参数解释**: 地域服务id。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 无。 
        :type area_service_id: str
        :param granted_object_path: **参数解释**: 授权对象路径。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 无。 
        :type granted_object_path: str
        :param granted_object_type_id: **参数解释**: 授权对象id。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 无。 
        :type granted_object_type_id: str
        :param operations: **参数解释**: 操作权限，多个权限以英文逗号隔开。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 无。 
        :type operations: str
        :param operations_index: **参数解释**: 操作权限索引。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 无。 
        :type operations_index: list[int]
        """
        
        

        self._role_id = None
        self._role_name = None
        self._role_chinese_name = None
        self._project_id = None
        self._area_service_id = None
        self._granted_object_path = None
        self._granted_object_type_id = None
        self._operations = None
        self._operations_index = None
        self.discriminator = None

        self.role_id = role_id
        if role_name is not None:
            self.role_name = role_name
        if role_chinese_name is not None:
            self.role_chinese_name = role_chinese_name
        self.project_id = project_id
        self.area_service_id = area_service_id
        self.granted_object_path = granted_object_path
        self.granted_object_type_id = granted_object_type_id
        self.operations = operations
        if operations_index is not None:
            self.operations_index = operations_index

    @property
    def role_id(self):
        r"""Gets the role_id of this Privilege.

        **参数解释**: 角色id。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 无。 

        :return: The role_id of this Privilege.
        :rtype: str
        """
        return self._role_id

    @role_id.setter
    def role_id(self, role_id):
        r"""Sets the role_id of this Privilege.

        **参数解释**: 角色id。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 无。 

        :param role_id: The role_id of this Privilege.
        :type role_id: str
        """
        self._role_id = role_id

    @property
    def role_name(self):
        r"""Gets the role_name of this Privilege.

        **参数解释**: 角色名称。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 无。 

        :return: The role_name of this Privilege.
        :rtype: str
        """
        return self._role_name

    @role_name.setter
    def role_name(self, role_name):
        r"""Sets the role_name of this Privilege.

        **参数解释**: 角色名称。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 无。 

        :param role_name: The role_name of this Privilege.
        :type role_name: str
        """
        self._role_name = role_name

    @property
    def role_chinese_name(self):
        r"""Gets the role_chinese_name of this Privilege.

        **参数解释**: 角色中文名。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 无。 

        :return: The role_chinese_name of this Privilege.
        :rtype: str
        """
        return self._role_chinese_name

    @role_chinese_name.setter
    def role_chinese_name(self, role_chinese_name):
        r"""Sets the role_chinese_name of this Privilege.

        **参数解释**: 角色中文名。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 无。 

        :param role_chinese_name: The role_chinese_name of this Privilege.
        :type role_chinese_name: str
        """
        self._role_chinese_name = role_chinese_name

    @property
    def project_id(self):
        r"""Gets the project_id of this Privilege.

        **参数解释**: 项目id。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 无。 

        :return: The project_id of this Privilege.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this Privilege.

        **参数解释**: 项目id。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 无。 

        :param project_id: The project_id of this Privilege.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def area_service_id(self):
        r"""Gets the area_service_id of this Privilege.

        **参数解释**: 地域服务id。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 无。 

        :return: The area_service_id of this Privilege.
        :rtype: str
        """
        return self._area_service_id

    @area_service_id.setter
    def area_service_id(self, area_service_id):
        r"""Sets the area_service_id of this Privilege.

        **参数解释**: 地域服务id。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 无。 

        :param area_service_id: The area_service_id of this Privilege.
        :type area_service_id: str
        """
        self._area_service_id = area_service_id

    @property
    def granted_object_path(self):
        r"""Gets the granted_object_path of this Privilege.

        **参数解释**: 授权对象路径。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 无。 

        :return: The granted_object_path of this Privilege.
        :rtype: str
        """
        return self._granted_object_path

    @granted_object_path.setter
    def granted_object_path(self, granted_object_path):
        r"""Sets the granted_object_path of this Privilege.

        **参数解释**: 授权对象路径。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 无。 

        :param granted_object_path: The granted_object_path of this Privilege.
        :type granted_object_path: str
        """
        self._granted_object_path = granted_object_path

    @property
    def granted_object_type_id(self):
        r"""Gets the granted_object_type_id of this Privilege.

        **参数解释**: 授权对象id。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 无。 

        :return: The granted_object_type_id of this Privilege.
        :rtype: str
        """
        return self._granted_object_type_id

    @granted_object_type_id.setter
    def granted_object_type_id(self, granted_object_type_id):
        r"""Sets the granted_object_type_id of this Privilege.

        **参数解释**: 授权对象id。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 无。 

        :param granted_object_type_id: The granted_object_type_id of this Privilege.
        :type granted_object_type_id: str
        """
        self._granted_object_type_id = granted_object_type_id

    @property
    def operations(self):
        r"""Gets the operations of this Privilege.

        **参数解释**: 操作权限，多个权限以英文逗号隔开。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 无。 

        :return: The operations of this Privilege.
        :rtype: str
        """
        return self._operations

    @operations.setter
    def operations(self, operations):
        r"""Sets the operations of this Privilege.

        **参数解释**: 操作权限，多个权限以英文逗号隔开。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 无。 

        :param operations: The operations of this Privilege.
        :type operations: str
        """
        self._operations = operations

    @property
    def operations_index(self):
        r"""Gets the operations_index of this Privilege.

        **参数解释**: 操作权限索引。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 无。 

        :return: The operations_index of this Privilege.
        :rtype: list[int]
        """
        return self._operations_index

    @operations_index.setter
    def operations_index(self, operations_index):
        r"""Sets the operations_index of this Privilege.

        **参数解释**: 操作权限索引。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 无。 

        :param operations_index: The operations_index of this Privilege.
        :type operations_index: list[int]
        """
        self._operations_index = operations_index

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
        if not isinstance(other, Privilege):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
