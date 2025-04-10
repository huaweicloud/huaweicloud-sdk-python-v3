# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AgencyInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'account_id': 'str',
        'agency_name': 'str',
        'permission_set_name': 'str',
        'agency_urn': 'str',
        'description': 'str'
    }

    attribute_map = {
        'account_id': 'account_id',
        'agency_name': 'agency_name',
        'permission_set_name': 'permission_set_name',
        'agency_urn': 'agency_urn',
        'description': 'description'
    }

    def __init__(self, account_id=None, agency_name=None, permission_set_name=None, agency_urn=None, description=None):
        r"""AgencyInfo

        The model defined in huaweicloud sdk

        :param account_id: 分配给用户的账号的全局唯一标识符（ID）
        :type account_id: str
        :param agency_name: 分配给用户的委托或信任委托的名称
        :type agency_name: str
        :param permission_set_name: 权限集名称
        :type permission_set_name: str
        :param agency_urn: 委托或信任委托的统一资源名称（URN）
        :type agency_urn: str
        :param description: 描述信息
        :type description: str
        """
        
        

        self._account_id = None
        self._agency_name = None
        self._permission_set_name = None
        self._agency_urn = None
        self._description = None
        self.discriminator = None

        if account_id is not None:
            self.account_id = account_id
        if agency_name is not None:
            self.agency_name = agency_name
        if permission_set_name is not None:
            self.permission_set_name = permission_set_name
        if agency_urn is not None:
            self.agency_urn = agency_urn
        if description is not None:
            self.description = description

    @property
    def account_id(self):
        r"""Gets the account_id of this AgencyInfo.

        分配给用户的账号的全局唯一标识符（ID）

        :return: The account_id of this AgencyInfo.
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        r"""Sets the account_id of this AgencyInfo.

        分配给用户的账号的全局唯一标识符（ID）

        :param account_id: The account_id of this AgencyInfo.
        :type account_id: str
        """
        self._account_id = account_id

    @property
    def agency_name(self):
        r"""Gets the agency_name of this AgencyInfo.

        分配给用户的委托或信任委托的名称

        :return: The agency_name of this AgencyInfo.
        :rtype: str
        """
        return self._agency_name

    @agency_name.setter
    def agency_name(self, agency_name):
        r"""Sets the agency_name of this AgencyInfo.

        分配给用户的委托或信任委托的名称

        :param agency_name: The agency_name of this AgencyInfo.
        :type agency_name: str
        """
        self._agency_name = agency_name

    @property
    def permission_set_name(self):
        r"""Gets the permission_set_name of this AgencyInfo.

        权限集名称

        :return: The permission_set_name of this AgencyInfo.
        :rtype: str
        """
        return self._permission_set_name

    @permission_set_name.setter
    def permission_set_name(self, permission_set_name):
        r"""Sets the permission_set_name of this AgencyInfo.

        权限集名称

        :param permission_set_name: The permission_set_name of this AgencyInfo.
        :type permission_set_name: str
        """
        self._permission_set_name = permission_set_name

    @property
    def agency_urn(self):
        r"""Gets the agency_urn of this AgencyInfo.

        委托或信任委托的统一资源名称（URN）

        :return: The agency_urn of this AgencyInfo.
        :rtype: str
        """
        return self._agency_urn

    @agency_urn.setter
    def agency_urn(self, agency_urn):
        r"""Sets the agency_urn of this AgencyInfo.

        委托或信任委托的统一资源名称（URN）

        :param agency_urn: The agency_urn of this AgencyInfo.
        :type agency_urn: str
        """
        self._agency_urn = agency_urn

    @property
    def description(self):
        r"""Gets the description of this AgencyInfo.

        描述信息

        :return: The description of this AgencyInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this AgencyInfo.

        描述信息

        :param description: The description of this AgencyInfo.
        :type description: str
        """
        self._description = description

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AgencyInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
