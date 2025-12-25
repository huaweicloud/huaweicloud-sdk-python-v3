# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListServiceAgencyResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'create_agency': 'bool',
        'role_descriptions': 'list[Role]'
    }

    attribute_map = {
        'create_agency': 'create_agency',
        'role_descriptions': 'role_descriptions'
    }

    def __init__(self, create_agency=None, role_descriptions=None):
        r"""ListServiceAgencyResponse

        The model defined in huaweicloud sdk

        :param create_agency: 当前账号是否已创建云服务关联委托
        :type create_agency: bool
        :param role_descriptions: 角色列表
        :type role_descriptions: list[:class:`huaweicloudsdksecmaster.v1.Role`]
        """
        
        super().__init__()

        self._create_agency = None
        self._role_descriptions = None
        self.discriminator = None

        if create_agency is not None:
            self.create_agency = create_agency
        if role_descriptions is not None:
            self.role_descriptions = role_descriptions

    @property
    def create_agency(self):
        r"""Gets the create_agency of this ListServiceAgencyResponse.

        当前账号是否已创建云服务关联委托

        :return: The create_agency of this ListServiceAgencyResponse.
        :rtype: bool
        """
        return self._create_agency

    @create_agency.setter
    def create_agency(self, create_agency):
        r"""Sets the create_agency of this ListServiceAgencyResponse.

        当前账号是否已创建云服务关联委托

        :param create_agency: The create_agency of this ListServiceAgencyResponse.
        :type create_agency: bool
        """
        self._create_agency = create_agency

    @property
    def role_descriptions(self):
        r"""Gets the role_descriptions of this ListServiceAgencyResponse.

        角色列表

        :return: The role_descriptions of this ListServiceAgencyResponse.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.Role`]
        """
        return self._role_descriptions

    @role_descriptions.setter
    def role_descriptions(self, role_descriptions):
        r"""Sets the role_descriptions of this ListServiceAgencyResponse.

        角色列表

        :param role_descriptions: The role_descriptions of this ListServiceAgencyResponse.
        :type role_descriptions: list[:class:`huaweicloudsdksecmaster.v1.Role`]
        """
        self._role_descriptions = role_descriptions

    def to_dict(self):
        import warnings
        warnings.warn("ListServiceAgencyResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ListServiceAgencyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
