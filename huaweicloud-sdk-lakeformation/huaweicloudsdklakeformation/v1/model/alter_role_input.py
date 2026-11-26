# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AlterRoleInput:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'description': 'str',
        'role_name': 'str',
        'external_role_id': 'str',
        'parameters': 'dict(str, str)'
    }

    attribute_map = {
        'description': 'description',
        'role_name': 'role_name',
        'external_role_id': 'external_role_id',
        'parameters': 'parameters'
    }

    def __init__(self, description=None, role_name=None, external_role_id=None, parameters=None):
        r"""AlterRoleInput

        The model defined in huaweicloud sdk

        :param description: 描述信息。最大长度为4000个字符。
        :type description: str
        :param role_name: 角色名称。只能包含字母、数字和下划线，且长度为1~255个字符。
        :type role_name: str
        :param external_role_id: 用户端角色id，创建时指定，不可修改。
        :type external_role_id: str
        :param parameters: 参数。
        :type parameters: dict(str, str)
        """
        
        

        self._description = None
        self._role_name = None
        self._external_role_id = None
        self._parameters = None
        self.discriminator = None

        if description is not None:
            self.description = description
        self.role_name = role_name
        if external_role_id is not None:
            self.external_role_id = external_role_id
        if parameters is not None:
            self.parameters = parameters

    @property
    def description(self):
        r"""Gets the description of this AlterRoleInput.

        描述信息。最大长度为4000个字符。

        :return: The description of this AlterRoleInput.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this AlterRoleInput.

        描述信息。最大长度为4000个字符。

        :param description: The description of this AlterRoleInput.
        :type description: str
        """
        self._description = description

    @property
    def role_name(self):
        r"""Gets the role_name of this AlterRoleInput.

        角色名称。只能包含字母、数字和下划线，且长度为1~255个字符。

        :return: The role_name of this AlterRoleInput.
        :rtype: str
        """
        return self._role_name

    @role_name.setter
    def role_name(self, role_name):
        r"""Sets the role_name of this AlterRoleInput.

        角色名称。只能包含字母、数字和下划线，且长度为1~255个字符。

        :param role_name: The role_name of this AlterRoleInput.
        :type role_name: str
        """
        self._role_name = role_name

    @property
    def external_role_id(self):
        r"""Gets the external_role_id of this AlterRoleInput.

        用户端角色id，创建时指定，不可修改。

        :return: The external_role_id of this AlterRoleInput.
        :rtype: str
        """
        return self._external_role_id

    @external_role_id.setter
    def external_role_id(self, external_role_id):
        r"""Sets the external_role_id of this AlterRoleInput.

        用户端角色id，创建时指定，不可修改。

        :param external_role_id: The external_role_id of this AlterRoleInput.
        :type external_role_id: str
        """
        self._external_role_id = external_role_id

    @property
    def parameters(self):
        r"""Gets the parameters of this AlterRoleInput.

        参数。

        :return: The parameters of this AlterRoleInput.
        :rtype: dict(str, str)
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        r"""Sets the parameters of this AlterRoleInput.

        参数。

        :param parameters: The parameters of this AlterRoleInput.
        :type parameters: dict(str, str)
        """
        self._parameters = parameters

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
        if not isinstance(other, AlterRoleInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
