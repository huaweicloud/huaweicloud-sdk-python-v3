# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAuditInfoResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'lists': 'list[TicsLeagueAuditLog]',
        'total': 'int'
    }

    attribute_map = {
        'lists': 'lists',
        'total': 'total'
    }

    def __init__(self, lists=None, total=None):
        """ListAuditInfoResponse

        The model defined in huaweicloud sdk

        :param lists: 实例集合
        :type lists: list[:class:`huaweicloudsdktics.v1.TicsLeagueAuditLog`]
        :param total: 总记录数
        :type total: int
        """
        
        super(ListAuditInfoResponse, self).__init__()

        self._lists = None
        self._total = None
        self.discriminator = None

        if lists is not None:
            self.lists = lists
        if total is not None:
            self.total = total

    @property
    def lists(self):
        """Gets the lists of this ListAuditInfoResponse.

        实例集合

        :return: The lists of this ListAuditInfoResponse.
        :rtype: list[:class:`huaweicloudsdktics.v1.TicsLeagueAuditLog`]
        """
        return self._lists

    @lists.setter
    def lists(self, lists):
        """Sets the lists of this ListAuditInfoResponse.

        实例集合

        :param lists: The lists of this ListAuditInfoResponse.
        :type lists: list[:class:`huaweicloudsdktics.v1.TicsLeagueAuditLog`]
        """
        self._lists = lists

    @property
    def total(self):
        """Gets the total of this ListAuditInfoResponse.

        总记录数

        :return: The total of this ListAuditInfoResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListAuditInfoResponse.

        总记录数

        :param total: The total of this ListAuditInfoResponse.
        :type total: int
        """
        self._total = total

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
        if not isinstance(other, ListAuditInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
