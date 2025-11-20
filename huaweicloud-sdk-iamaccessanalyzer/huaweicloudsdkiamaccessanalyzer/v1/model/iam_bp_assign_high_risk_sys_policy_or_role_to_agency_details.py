# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IamBpAssignHighRiskSysPolicyOrRoleToAgencyDetails:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'agency_id': 'str',
        'permission_name': 'str'
    }

    attribute_map = {
        'agency_id': 'agency_id',
        'permission_name': 'permission_name'
    }

    def __init__(self, agency_id=None, permission_name=None):
        r"""IamBpAssignHighRiskSysPolicyOrRoleToAgencyDetails

        The model defined in huaweicloud sdk

        :param agency_id: 委托的唯一标识符（ID）。
        :type agency_id: str
        :param permission_name: 权限名称。
        :type permission_name: str
        """
        
        

        self._agency_id = None
        self._permission_name = None
        self.discriminator = None

        self.agency_id = agency_id
        self.permission_name = permission_name

    @property
    def agency_id(self):
        r"""Gets the agency_id of this IamBpAssignHighRiskSysPolicyOrRoleToAgencyDetails.

        委托的唯一标识符（ID）。

        :return: The agency_id of this IamBpAssignHighRiskSysPolicyOrRoleToAgencyDetails.
        :rtype: str
        """
        return self._agency_id

    @agency_id.setter
    def agency_id(self, agency_id):
        r"""Sets the agency_id of this IamBpAssignHighRiskSysPolicyOrRoleToAgencyDetails.

        委托的唯一标识符（ID）。

        :param agency_id: The agency_id of this IamBpAssignHighRiskSysPolicyOrRoleToAgencyDetails.
        :type agency_id: str
        """
        self._agency_id = agency_id

    @property
    def permission_name(self):
        r"""Gets the permission_name of this IamBpAssignHighRiskSysPolicyOrRoleToAgencyDetails.

        权限名称。

        :return: The permission_name of this IamBpAssignHighRiskSysPolicyOrRoleToAgencyDetails.
        :rtype: str
        """
        return self._permission_name

    @permission_name.setter
    def permission_name(self, permission_name):
        r"""Sets the permission_name of this IamBpAssignHighRiskSysPolicyOrRoleToAgencyDetails.

        权限名称。

        :param permission_name: The permission_name of this IamBpAssignHighRiskSysPolicyOrRoleToAgencyDetails.
        :type permission_name: str
        """
        self._permission_name = permission_name

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
        if not isinstance(other, IamBpAssignHighRiskSysPolicyOrRoleToAgencyDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
