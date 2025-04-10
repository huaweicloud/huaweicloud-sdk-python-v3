# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowServerGroupRestrictResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'max_session': 'int',
        'max_group_count': 'int'
    }

    attribute_map = {
        'max_session': 'max_session',
        'max_group_count': 'max_group_count'
    }

    def __init__(self, max_session=None, max_group_count=None):
        r"""ShowServerGroupRestrictResponse

        The model defined in huaweicloud sdk

        :param max_session: 单台服务器最大的链接会话数。
        :type max_session: int
        :param max_group_count: 该租户可创建的最多服务器组数量。
        :type max_group_count: int
        """
        
        super(ShowServerGroupRestrictResponse, self).__init__()

        self._max_session = None
        self._max_group_count = None
        self.discriminator = None

        if max_session is not None:
            self.max_session = max_session
        if max_group_count is not None:
            self.max_group_count = max_group_count

    @property
    def max_session(self):
        r"""Gets the max_session of this ShowServerGroupRestrictResponse.

        单台服务器最大的链接会话数。

        :return: The max_session of this ShowServerGroupRestrictResponse.
        :rtype: int
        """
        return self._max_session

    @max_session.setter
    def max_session(self, max_session):
        r"""Sets the max_session of this ShowServerGroupRestrictResponse.

        单台服务器最大的链接会话数。

        :param max_session: The max_session of this ShowServerGroupRestrictResponse.
        :type max_session: int
        """
        self._max_session = max_session

    @property
    def max_group_count(self):
        r"""Gets the max_group_count of this ShowServerGroupRestrictResponse.

        该租户可创建的最多服务器组数量。

        :return: The max_group_count of this ShowServerGroupRestrictResponse.
        :rtype: int
        """
        return self._max_group_count

    @max_group_count.setter
    def max_group_count(self, max_group_count):
        r"""Sets the max_group_count of this ShowServerGroupRestrictResponse.

        该租户可创建的最多服务器组数量。

        :param max_group_count: The max_group_count of this ShowServerGroupRestrictResponse.
        :type max_group_count: int
        """
        self._max_group_count = max_group_count

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
        if not isinstance(other, ShowServerGroupRestrictResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
