# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCloseAccountStatusesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'close_account_statuses': 'list[CloseAccountStatusDto]'
    }

    attribute_map = {
        'close_account_statuses': 'close_account_statuses'
    }

    def __init__(self, close_account_statuses=None):
        r"""ListCloseAccountStatusesResponse

        The model defined in huaweicloud sdk

        :param close_account_statuses: 包含有关请求的详细信息的对象列表。
        :type close_account_statuses: list[:class:`huaweicloudsdkorganizations.v1.CloseAccountStatusDto`]
        """
        
        super(ListCloseAccountStatusesResponse, self).__init__()

        self._close_account_statuses = None
        self.discriminator = None

        if close_account_statuses is not None:
            self.close_account_statuses = close_account_statuses

    @property
    def close_account_statuses(self):
        r"""Gets the close_account_statuses of this ListCloseAccountStatusesResponse.

        包含有关请求的详细信息的对象列表。

        :return: The close_account_statuses of this ListCloseAccountStatusesResponse.
        :rtype: list[:class:`huaweicloudsdkorganizations.v1.CloseAccountStatusDto`]
        """
        return self._close_account_statuses

    @close_account_statuses.setter
    def close_account_statuses(self, close_account_statuses):
        r"""Sets the close_account_statuses of this ListCloseAccountStatusesResponse.

        包含有关请求的详细信息的对象列表。

        :param close_account_statuses: The close_account_statuses of this ListCloseAccountStatusesResponse.
        :type close_account_statuses: list[:class:`huaweicloudsdkorganizations.v1.CloseAccountStatusDto`]
        """
        self._close_account_statuses = close_account_statuses

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
        if not isinstance(other, ListCloseAccountStatusesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
