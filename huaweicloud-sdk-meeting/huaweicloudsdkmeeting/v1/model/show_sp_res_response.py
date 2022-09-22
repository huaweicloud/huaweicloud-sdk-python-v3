# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSpResResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'used_accounts_count': 'int'
    }

    attribute_map = {
        'used_accounts_count': 'usedAccountsCount'
    }

    def __init__(self, used_accounts_count=None):
        """ShowSpResResponse

        The model defined in huaweicloud sdk

        :param used_accounts_count: SP下所有企业已使用的会议并发数量。
        :type used_accounts_count: int
        """
        
        super(ShowSpResResponse, self).__init__()

        self._used_accounts_count = None
        self.discriminator = None

        if used_accounts_count is not None:
            self.used_accounts_count = used_accounts_count

    @property
    def used_accounts_count(self):
        """Gets the used_accounts_count of this ShowSpResResponse.

        SP下所有企业已使用的会议并发数量。

        :return: The used_accounts_count of this ShowSpResResponse.
        :rtype: int
        """
        return self._used_accounts_count

    @used_accounts_count.setter
    def used_accounts_count(self, used_accounts_count):
        """Sets the used_accounts_count of this ShowSpResResponse.

        SP下所有企业已使用的会议并发数量。

        :param used_accounts_count: The used_accounts_count of this ShowSpResResponse.
        :type used_accounts_count: int
        """
        self._used_accounts_count = used_accounts_count

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
        if not isinstance(other, ShowSpResResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
