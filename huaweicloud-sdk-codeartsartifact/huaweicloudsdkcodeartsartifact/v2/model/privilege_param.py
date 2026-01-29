# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PrivilegeParam:

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
        'project_id': 'str',
        'area_service_id': 'str',
        'granted_object_path': 'str',
        'granted_object_type_id': 'str',
        'operations': 'str'
    }

    attribute_map = {
        'role_id': 'role_id',
        'project_id': 'project_id',
        'area_service_id': 'area_service_id',
        'granted_object_path': 'granted_object_path',
        'granted_object_type_id': 'granted_object_type_id',
        'operations': 'operations'
    }

    def __init__(self, role_id=None, project_id=None, area_service_id=None, granted_object_path=None, granted_object_type_id=None, operations=None):
        r"""PrivilegeParam

        The model defined in huaweicloud sdk

        :param role_id: **参数解释**: 角色id。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 无。 
        :type role_id: str
        :param project_id: **参数解释**: 项目ID，可以从调用API处获取，也可以从控制台获取。获取方式请参考[获取项目ID](CloudArtifact_api_0015.xml)。 **约束限制**: 只能由英文字母、数字组成，且长度为32个字符。 **取值范围**: 不涉及。 **默认取值**: 无。
        :type project_id: str
        :param area_service_id: **参数解释**: 地域服务id。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 无。 
        :type area_service_id: str
        :param granted_object_path: **参数解释**: 授权对象路径。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 无。 
        :type granted_object_path: str
        :param granted_object_type_id: **参数解释**: 授权对象id。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 无。 
        :type granted_object_type_id: str
        :param operations: **参数解释**: 操作权限，多个权限以英文逗号隔开。 **约束限制**: 不涉及。 **取值范围**: 可选值：createrepository,editrepository,restore,deleterepository,physicdelete,restoreall,clearall,deleteorredeploy,downloadorview,import,upload,export。 **默认取值**: 无。 
        :type operations: str
        """
        
        

        self._role_id = None
        self._project_id = None
        self._area_service_id = None
        self._granted_object_path = None
        self._granted_object_type_id = None
        self._operations = None
        self.discriminator = None

        self.role_id = role_id
        self.project_id = project_id
        self.area_service_id = area_service_id
        self.granted_object_path = granted_object_path
        self.granted_object_type_id = granted_object_type_id
        self.operations = operations

    @property
    def role_id(self):
        r"""Gets the role_id of this PrivilegeParam.

        **参数解释**: 角色id。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 无。 

        :return: The role_id of this PrivilegeParam.
        :rtype: str
        """
        return self._role_id

    @role_id.setter
    def role_id(self, role_id):
        r"""Sets the role_id of this PrivilegeParam.

        **参数解释**: 角色id。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 无。 

        :param role_id: The role_id of this PrivilegeParam.
        :type role_id: str
        """
        self._role_id = role_id

    @property
    def project_id(self):
        r"""Gets the project_id of this PrivilegeParam.

        **参数解释**: 项目ID，可以从调用API处获取，也可以从控制台获取。获取方式请参考[获取项目ID](CloudArtifact_api_0015.xml)。 **约束限制**: 只能由英文字母、数字组成，且长度为32个字符。 **取值范围**: 不涉及。 **默认取值**: 无。

        :return: The project_id of this PrivilegeParam.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this PrivilegeParam.

        **参数解释**: 项目ID，可以从调用API处获取，也可以从控制台获取。获取方式请参考[获取项目ID](CloudArtifact_api_0015.xml)。 **约束限制**: 只能由英文字母、数字组成，且长度为32个字符。 **取值范围**: 不涉及。 **默认取值**: 无。

        :param project_id: The project_id of this PrivilegeParam.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def area_service_id(self):
        r"""Gets the area_service_id of this PrivilegeParam.

        **参数解释**: 地域服务id。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 无。 

        :return: The area_service_id of this PrivilegeParam.
        :rtype: str
        """
        return self._area_service_id

    @area_service_id.setter
    def area_service_id(self, area_service_id):
        r"""Sets the area_service_id of this PrivilegeParam.

        **参数解释**: 地域服务id。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 无。 

        :param area_service_id: The area_service_id of this PrivilegeParam.
        :type area_service_id: str
        """
        self._area_service_id = area_service_id

    @property
    def granted_object_path(self):
        r"""Gets the granted_object_path of this PrivilegeParam.

        **参数解释**: 授权对象路径。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 无。 

        :return: The granted_object_path of this PrivilegeParam.
        :rtype: str
        """
        return self._granted_object_path

    @granted_object_path.setter
    def granted_object_path(self, granted_object_path):
        r"""Sets the granted_object_path of this PrivilegeParam.

        **参数解释**: 授权对象路径。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 无。 

        :param granted_object_path: The granted_object_path of this PrivilegeParam.
        :type granted_object_path: str
        """
        self._granted_object_path = granted_object_path

    @property
    def granted_object_type_id(self):
        r"""Gets the granted_object_type_id of this PrivilegeParam.

        **参数解释**: 授权对象id。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 无。 

        :return: The granted_object_type_id of this PrivilegeParam.
        :rtype: str
        """
        return self._granted_object_type_id

    @granted_object_type_id.setter
    def granted_object_type_id(self, granted_object_type_id):
        r"""Sets the granted_object_type_id of this PrivilegeParam.

        **参数解释**: 授权对象id。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 无。 

        :param granted_object_type_id: The granted_object_type_id of this PrivilegeParam.
        :type granted_object_type_id: str
        """
        self._granted_object_type_id = granted_object_type_id

    @property
    def operations(self):
        r"""Gets the operations of this PrivilegeParam.

        **参数解释**: 操作权限，多个权限以英文逗号隔开。 **约束限制**: 不涉及。 **取值范围**: 可选值：createrepository,editrepository,restore,deleterepository,physicdelete,restoreall,clearall,deleteorredeploy,downloadorview,import,upload,export。 **默认取值**: 无。 

        :return: The operations of this PrivilegeParam.
        :rtype: str
        """
        return self._operations

    @operations.setter
    def operations(self, operations):
        r"""Sets the operations of this PrivilegeParam.

        **参数解释**: 操作权限，多个权限以英文逗号隔开。 **约束限制**: 不涉及。 **取值范围**: 可选值：createrepository,editrepository,restore,deleterepository,physicdelete,restoreall,clearall,deleteorredeploy,downloadorview,import,upload,export。 **默认取值**: 无。 

        :param operations: The operations of this PrivilegeParam.
        :type operations: str
        """
        self._operations = operations

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
        if not isinstance(other, PrivilegeParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
