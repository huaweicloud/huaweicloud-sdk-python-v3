# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DelegatedAdministratorReqBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'service_principal': 'str',
        'account_id': 'str'
    }

    attribute_map = {
        'service_principal': 'service_principal',
        'account_id': 'account_id'
    }

    def __init__(self, service_principal=None, account_id=None):
        r"""DelegatedAdministratorReqBody

        The model defined in huaweicloud sdk

        :param service_principal: 服务主体名称。
        :type service_principal: str
        :param account_id: 账号的唯一标识符（ID）。
        :type account_id: str
        """
        
        

        self._service_principal = None
        self._account_id = None
        self.discriminator = None

        self.service_principal = service_principal
        self.account_id = account_id

    @property
    def service_principal(self):
        r"""Gets the service_principal of this DelegatedAdministratorReqBody.

        服务主体名称。

        :return: The service_principal of this DelegatedAdministratorReqBody.
        :rtype: str
        """
        return self._service_principal

    @service_principal.setter
    def service_principal(self, service_principal):
        r"""Sets the service_principal of this DelegatedAdministratorReqBody.

        服务主体名称。

        :param service_principal: The service_principal of this DelegatedAdministratorReqBody.
        :type service_principal: str
        """
        self._service_principal = service_principal

    @property
    def account_id(self):
        r"""Gets the account_id of this DelegatedAdministratorReqBody.

        账号的唯一标识符（ID）。

        :return: The account_id of this DelegatedAdministratorReqBody.
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        r"""Sets the account_id of this DelegatedAdministratorReqBody.

        账号的唯一标识符（ID）。

        :param account_id: The account_id of this DelegatedAdministratorReqBody.
        :type account_id: str
        """
        self._account_id = account_id

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
        if not isinstance(other, DelegatedAdministratorReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
