# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAccountResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'account_list': 'list[AccountRsp]'
    }

    attribute_map = {
        'count': 'count',
        'account_list': 'account_list'
    }

    def __init__(self, count=None, account_list=None):
        r"""ShowAccountResponse

        The model defined in huaweicloud sdk

        :param count: 数量
        :type count: int
        :param account_list: 账号list
        :type account_list: list[:class:`huaweicloudsdkcoc.v1.AccountRsp`]
        """
        
        super(ShowAccountResponse, self).__init__()

        self._count = None
        self._account_list = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if account_list is not None:
            self.account_list = account_list

    @property
    def count(self):
        r"""Gets the count of this ShowAccountResponse.

        数量

        :return: The count of this ShowAccountResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ShowAccountResponse.

        数量

        :param count: The count of this ShowAccountResponse.
        :type count: int
        """
        self._count = count

    @property
    def account_list(self):
        r"""Gets the account_list of this ShowAccountResponse.

        账号list

        :return: The account_list of this ShowAccountResponse.
        :rtype: list[:class:`huaweicloudsdkcoc.v1.AccountRsp`]
        """
        return self._account_list

    @account_list.setter
    def account_list(self, account_list):
        r"""Sets the account_list of this ShowAccountResponse.

        账号list

        :param account_list: The account_list of this ShowAccountResponse.
        :type account_list: list[:class:`huaweicloudsdkcoc.v1.AccountRsp`]
        """
        self._account_list = account_list

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
        if not isinstance(other, ShowAccountResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
