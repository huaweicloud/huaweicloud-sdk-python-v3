# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowManagedCoreAccountResponse(SdkResponse):

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
        'account_name': 'str',
        'account_email': 'str',
        'core_resource_mappings': 'dict(str, str)'
    }

    attribute_map = {
        'account_id': 'account_id',
        'account_name': 'account_name',
        'account_email': 'account_email',
        'core_resource_mappings': 'core_resource_mappings'
    }

    def __init__(self, account_id=None, account_name=None, account_email=None, core_resource_mappings=None):
        """ShowManagedCoreAccountResponse

        The model defined in huaweicloud sdk

        :param account_id: 账号ID。
        :type account_id: str
        :param account_name: 账号名称。
        :type account_name: str
        :param account_email: 账号邮箱。
        :type account_email: str
        :param core_resource_mappings: 
        :type core_resource_mappings: dict(str, str)
        """
        
        super(ShowManagedCoreAccountResponse, self).__init__()

        self._account_id = None
        self._account_name = None
        self._account_email = None
        self._core_resource_mappings = None
        self.discriminator = None

        if account_id is not None:
            self.account_id = account_id
        if account_name is not None:
            self.account_name = account_name
        if account_email is not None:
            self.account_email = account_email
        if core_resource_mappings is not None:
            self.core_resource_mappings = core_resource_mappings

    @property
    def account_id(self):
        """Gets the account_id of this ShowManagedCoreAccountResponse.

        账号ID。

        :return: The account_id of this ShowManagedCoreAccountResponse.
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this ShowManagedCoreAccountResponse.

        账号ID。

        :param account_id: The account_id of this ShowManagedCoreAccountResponse.
        :type account_id: str
        """
        self._account_id = account_id

    @property
    def account_name(self):
        """Gets the account_name of this ShowManagedCoreAccountResponse.

        账号名称。

        :return: The account_name of this ShowManagedCoreAccountResponse.
        :rtype: str
        """
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        """Sets the account_name of this ShowManagedCoreAccountResponse.

        账号名称。

        :param account_name: The account_name of this ShowManagedCoreAccountResponse.
        :type account_name: str
        """
        self._account_name = account_name

    @property
    def account_email(self):
        """Gets the account_email of this ShowManagedCoreAccountResponse.

        账号邮箱。

        :return: The account_email of this ShowManagedCoreAccountResponse.
        :rtype: str
        """
        return self._account_email

    @account_email.setter
    def account_email(self, account_email):
        """Sets the account_email of this ShowManagedCoreAccountResponse.

        账号邮箱。

        :param account_email: The account_email of this ShowManagedCoreAccountResponse.
        :type account_email: str
        """
        self._account_email = account_email

    @property
    def core_resource_mappings(self):
        """Gets the core_resource_mappings of this ShowManagedCoreAccountResponse.

        :return: The core_resource_mappings of this ShowManagedCoreAccountResponse.
        :rtype: dict(str, str)
        """
        return self._core_resource_mappings

    @core_resource_mappings.setter
    def core_resource_mappings(self, core_resource_mappings):
        """Sets the core_resource_mappings of this ShowManagedCoreAccountResponse.

        :param core_resource_mappings: The core_resource_mappings of this ShowManagedCoreAccountResponse.
        :type core_resource_mappings: dict(str, str)
        """
        self._core_resource_mappings = core_resource_mappings

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
        if not isinstance(other, ShowManagedCoreAccountResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
