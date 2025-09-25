# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSqlLimitTaskResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit_count': 'int'
    }

    attribute_map = {
        'limit_count': 'limit_count'
    }

    def __init__(self, limit_count=None):
        r"""ShowSqlLimitTaskResponse

        The model defined in huaweicloud sdk

        :param limit_count: **参数解释**: 限流任务拦截次数。 **取值范围**: 不涉及。
        :type limit_count: int
        """
        
        super(ShowSqlLimitTaskResponse, self).__init__()

        self._limit_count = None
        self.discriminator = None

        if limit_count is not None:
            self.limit_count = limit_count

    @property
    def limit_count(self):
        r"""Gets the limit_count of this ShowSqlLimitTaskResponse.

        **参数解释**: 限流任务拦截次数。 **取值范围**: 不涉及。

        :return: The limit_count of this ShowSqlLimitTaskResponse.
        :rtype: int
        """
        return self._limit_count

    @limit_count.setter
    def limit_count(self, limit_count):
        r"""Sets the limit_count of this ShowSqlLimitTaskResponse.

        **参数解释**: 限流任务拦截次数。 **取值范围**: 不涉及。

        :param limit_count: The limit_count of this ShowSqlLimitTaskResponse.
        :type limit_count: int
        """
        self._limit_count = limit_count

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
        if not isinstance(other, ShowSqlLimitTaskResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
