# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateServiceAgencyRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'organizations': 'list[Organization]',
        'role_descriptions': 'list[Role]'
    }

    attribute_map = {
        'organizations': 'organizations',
        'role_descriptions': 'role_descriptions'
    }

    def __init__(self, organizations=None, role_descriptions=None):
        r"""CreateServiceAgencyRequestBody

        The model defined in huaweicloud sdk

        :param organizations: OU列表
        :type organizations: list[:class:`huaweicloudsdksecmaster.v1.Organization`]
        :param role_descriptions: 角色列表
        :type role_descriptions: list[:class:`huaweicloudsdksecmaster.v1.Role`]
        """
        
        

        self._organizations = None
        self._role_descriptions = None
        self.discriminator = None

        if organizations is not None:
            self.organizations = organizations
        if role_descriptions is not None:
            self.role_descriptions = role_descriptions

    @property
    def organizations(self):
        r"""Gets the organizations of this CreateServiceAgencyRequestBody.

        OU列表

        :return: The organizations of this CreateServiceAgencyRequestBody.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.Organization`]
        """
        return self._organizations

    @organizations.setter
    def organizations(self, organizations):
        r"""Sets the organizations of this CreateServiceAgencyRequestBody.

        OU列表

        :param organizations: The organizations of this CreateServiceAgencyRequestBody.
        :type organizations: list[:class:`huaweicloudsdksecmaster.v1.Organization`]
        """
        self._organizations = organizations

    @property
    def role_descriptions(self):
        r"""Gets the role_descriptions of this CreateServiceAgencyRequestBody.

        角色列表

        :return: The role_descriptions of this CreateServiceAgencyRequestBody.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.Role`]
        """
        return self._role_descriptions

    @role_descriptions.setter
    def role_descriptions(self, role_descriptions):
        r"""Sets the role_descriptions of this CreateServiceAgencyRequestBody.

        角色列表

        :param role_descriptions: The role_descriptions of this CreateServiceAgencyRequestBody.
        :type role_descriptions: list[:class:`huaweicloudsdksecmaster.v1.Role`]
        """
        self._role_descriptions = role_descriptions

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
        if not isinstance(other, CreateServiceAgencyRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
