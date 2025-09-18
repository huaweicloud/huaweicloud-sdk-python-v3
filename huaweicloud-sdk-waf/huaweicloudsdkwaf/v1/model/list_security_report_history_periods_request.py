# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSecurityReportHistoryPeriodsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'subscription_id': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'subscription_id': 'subscription_id',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, subscription_id=None, limit=None, offset=None):
        r"""ListSecurityReportHistoryPeriodsRequest

        The model defined in huaweicloud sdk

        :param subscription_id: 订阅ID
        :type subscription_id: str
        :param limit: 限制条目数量
        :type limit: int
        :param offset: 偏移量
        :type offset: int
        """
        
        

        self._subscription_id = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        self.subscription_id = subscription_id
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def subscription_id(self):
        r"""Gets the subscription_id of this ListSecurityReportHistoryPeriodsRequest.

        订阅ID

        :return: The subscription_id of this ListSecurityReportHistoryPeriodsRequest.
        :rtype: str
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        r"""Sets the subscription_id of this ListSecurityReportHistoryPeriodsRequest.

        订阅ID

        :param subscription_id: The subscription_id of this ListSecurityReportHistoryPeriodsRequest.
        :type subscription_id: str
        """
        self._subscription_id = subscription_id

    @property
    def limit(self):
        r"""Gets the limit of this ListSecurityReportHistoryPeriodsRequest.

        限制条目数量

        :return: The limit of this ListSecurityReportHistoryPeriodsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListSecurityReportHistoryPeriodsRequest.

        限制条目数量

        :param limit: The limit of this ListSecurityReportHistoryPeriodsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListSecurityReportHistoryPeriodsRequest.

        偏移量

        :return: The offset of this ListSecurityReportHistoryPeriodsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListSecurityReportHistoryPeriodsRequest.

        偏移量

        :param offset: The offset of this ListSecurityReportHistoryPeriodsRequest.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ListSecurityReportHistoryPeriodsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
