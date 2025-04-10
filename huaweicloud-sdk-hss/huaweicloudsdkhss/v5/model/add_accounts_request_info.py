# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddAccountsRequestInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'organization_id': 'str',
        'account_id': 'str',
        'account_name': 'str'
    }

    attribute_map = {
        'organization_id': 'organization_id',
        'account_id': 'account_id',
        'account_name': 'account_name'
    }

    def __init__(self, organization_id=None, account_id=None, account_name=None):
        r"""AddAccountsRequestInfo

        The model defined in huaweicloud sdk

        :param organization_id: 组织Id
        :type organization_id: str
        :param account_id: 账号ID
        :type account_id: str
        :param account_name: 账号名称
        :type account_name: str
        """
        
        

        self._organization_id = None
        self._account_id = None
        self._account_name = None
        self.discriminator = None

        self.organization_id = organization_id
        self.account_id = account_id
        self.account_name = account_name

    @property
    def organization_id(self):
        r"""Gets the organization_id of this AddAccountsRequestInfo.

        组织Id

        :return: The organization_id of this AddAccountsRequestInfo.
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        r"""Sets the organization_id of this AddAccountsRequestInfo.

        组织Id

        :param organization_id: The organization_id of this AddAccountsRequestInfo.
        :type organization_id: str
        """
        self._organization_id = organization_id

    @property
    def account_id(self):
        r"""Gets the account_id of this AddAccountsRequestInfo.

        账号ID

        :return: The account_id of this AddAccountsRequestInfo.
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        r"""Sets the account_id of this AddAccountsRequestInfo.

        账号ID

        :param account_id: The account_id of this AddAccountsRequestInfo.
        :type account_id: str
        """
        self._account_id = account_id

    @property
    def account_name(self):
        r"""Gets the account_name of this AddAccountsRequestInfo.

        账号名称

        :return: The account_name of this AddAccountsRequestInfo.
        :rtype: str
        """
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        r"""Sets the account_name of this AddAccountsRequestInfo.

        账号名称

        :param account_name: The account_name of this AddAccountsRequestInfo.
        :type account_name: str
        """
        self._account_name = account_name

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
        if not isinstance(other, AddAccountsRequestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
