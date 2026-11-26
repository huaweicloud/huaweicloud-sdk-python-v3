# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RoleInput:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'role_name': 'str',
        'description': 'str',
        'external_role_id': 'str',
        'parameters': 'dict(str, str)'
    }

    attribute_map = {
        'role_name': 'role_name',
        'description': 'description',
        'external_role_id': 'external_role_id',
        'parameters': 'parameters'
    }

    def __init__(self, role_name=None, description=None, external_role_id=None, parameters=None):
        r"""RoleInput

        The model defined in huaweicloud sdk

        :param role_name: role名字
        :type role_name: str
        :param description: 描述信息
        :type description: str
        :param external_role_id: 用户端角色id，创建时指定，不可修改。
        :type external_role_id: str
        :param parameters: 参数。
        :type parameters: dict(str, str)
        """
        
        

        self._role_name = None
        self._description = None
        self._external_role_id = None
        self._parameters = None
        self.discriminator = None

        self.role_name = role_name
        if description is not None:
            self.description = description
        if external_role_id is not None:
            self.external_role_id = external_role_id
        if parameters is not None:
            self.parameters = parameters

    @property
    def role_name(self):
        r"""Gets the role_name of this RoleInput.

        role名字

        :return: The role_name of this RoleInput.
        :rtype: str
        """
        return self._role_name

    @role_name.setter
    def role_name(self, role_name):
        r"""Sets the role_name of this RoleInput.

        role名字

        :param role_name: The role_name of this RoleInput.
        :type role_name: str
        """
        self._role_name = role_name

    @property
    def description(self):
        r"""Gets the description of this RoleInput.

        描述信息

        :return: The description of this RoleInput.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this RoleInput.

        描述信息

        :param description: The description of this RoleInput.
        :type description: str
        """
        self._description = description

    @property
    def external_role_id(self):
        r"""Gets the external_role_id of this RoleInput.

        用户端角色id，创建时指定，不可修改。

        :return: The external_role_id of this RoleInput.
        :rtype: str
        """
        return self._external_role_id

    @external_role_id.setter
    def external_role_id(self, external_role_id):
        r"""Sets the external_role_id of this RoleInput.

        用户端角色id，创建时指定，不可修改。

        :param external_role_id: The external_role_id of this RoleInput.
        :type external_role_id: str
        """
        self._external_role_id = external_role_id

    @property
    def parameters(self):
        r"""Gets the parameters of this RoleInput.

        参数。

        :return: The parameters of this RoleInput.
        :rtype: dict(str, str)
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        r"""Sets the parameters of this RoleInput.

        参数。

        :param parameters: The parameters of this RoleInput.
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
        if not isinstance(other, RoleInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
