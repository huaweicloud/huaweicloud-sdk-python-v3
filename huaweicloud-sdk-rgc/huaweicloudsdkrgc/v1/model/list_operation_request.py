# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListOperationRequest:

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
        'organizational_unit_id': 'str'
    }

    attribute_map = {
        'account_id': 'account_id',
        'organizational_unit_id': 'organizational_unit_id'
    }

    def __init__(self, account_id=None, organizational_unit_id=None):
        r"""ListOperationRequest

        The model defined in huaweicloud sdk

        :param account_id: 纳管账号ID。
        :type account_id: str
        :param organizational_unit_id: 注册OU ID。
        :type organizational_unit_id: str
        """
        
        

        self._account_id = None
        self._organizational_unit_id = None
        self.discriminator = None

        if account_id is not None:
            self.account_id = account_id
        if organizational_unit_id is not None:
            self.organizational_unit_id = organizational_unit_id

    @property
    def account_id(self):
        r"""Gets the account_id of this ListOperationRequest.

        纳管账号ID。

        :return: The account_id of this ListOperationRequest.
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        r"""Sets the account_id of this ListOperationRequest.

        纳管账号ID。

        :param account_id: The account_id of this ListOperationRequest.
        :type account_id: str
        """
        self._account_id = account_id

    @property
    def organizational_unit_id(self):
        r"""Gets the organizational_unit_id of this ListOperationRequest.

        注册OU ID。

        :return: The organizational_unit_id of this ListOperationRequest.
        :rtype: str
        """
        return self._organizational_unit_id

    @organizational_unit_id.setter
    def organizational_unit_id(self, organizational_unit_id):
        r"""Sets the organizational_unit_id of this ListOperationRequest.

        注册OU ID。

        :param organizational_unit_id: The organizational_unit_id of this ListOperationRequest.
        :type organizational_unit_id: str
        """
        self._organizational_unit_id = organizational_unit_id

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
        if not isinstance(other, ListOperationRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
