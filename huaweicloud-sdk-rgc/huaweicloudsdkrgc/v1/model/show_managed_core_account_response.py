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
        'core_resource_mappings': 'dict(str, str)'
    }

    attribute_map = {
        'account_id': 'account_id',
        'account_name': 'account_name',
        'core_resource_mappings': 'core_resource_mappings'
    }

    def __init__(self, account_id=None, account_name=None, core_resource_mappings=None):
        r"""ShowManagedCoreAccountResponse

        The model defined in huaweicloud sdk

        :param account_id: 纳管账号ID。
        :type account_id: str
        :param account_name: 纳管账号名称。
        :type account_name: str
        :param core_resource_mappings: 核心资源映射。
        :type core_resource_mappings: dict(str, str)
        """
        
        super(ShowManagedCoreAccountResponse, self).__init__()

        self._account_id = None
        self._account_name = None
        self._core_resource_mappings = None
        self.discriminator = None

        if account_id is not None:
            self.account_id = account_id
        if account_name is not None:
            self.account_name = account_name
        if core_resource_mappings is not None:
            self.core_resource_mappings = core_resource_mappings

    @property
    def account_id(self):
        r"""Gets the account_id of this ShowManagedCoreAccountResponse.

        纳管账号ID。

        :return: The account_id of this ShowManagedCoreAccountResponse.
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        r"""Sets the account_id of this ShowManagedCoreAccountResponse.

        纳管账号ID。

        :param account_id: The account_id of this ShowManagedCoreAccountResponse.
        :type account_id: str
        """
        self._account_id = account_id

    @property
    def account_name(self):
        r"""Gets the account_name of this ShowManagedCoreAccountResponse.

        纳管账号名称。

        :return: The account_name of this ShowManagedCoreAccountResponse.
        :rtype: str
        """
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        r"""Sets the account_name of this ShowManagedCoreAccountResponse.

        纳管账号名称。

        :param account_name: The account_name of this ShowManagedCoreAccountResponse.
        :type account_name: str
        """
        self._account_name = account_name

    @property
    def core_resource_mappings(self):
        r"""Gets the core_resource_mappings of this ShowManagedCoreAccountResponse.

        核心资源映射。

        :return: The core_resource_mappings of this ShowManagedCoreAccountResponse.
        :rtype: dict(str, str)
        """
        return self._core_resource_mappings

    @core_resource_mappings.setter
    def core_resource_mappings(self, core_resource_mappings):
        r"""Sets the core_resource_mappings of this ShowManagedCoreAccountResponse.

        核心资源映射。

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
