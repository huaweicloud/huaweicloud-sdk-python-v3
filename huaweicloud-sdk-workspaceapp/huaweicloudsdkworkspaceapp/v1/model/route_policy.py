# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RoutePolicy:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'max_session': 'int'
    }

    attribute_map = {
        'max_session': 'max_session'
    }

    def __init__(self, max_session=None):
        """RoutePolicy

        The model defined in huaweicloud sdk

        :param max_session: 单台服务器最大的链接会话数
        :type max_session: int
        """
        
        

        self._max_session = None
        self.discriminator = None

        if max_session is not None:
            self.max_session = max_session

    @property
    def max_session(self):
        """Gets the max_session of this RoutePolicy.

        单台服务器最大的链接会话数

        :return: The max_session of this RoutePolicy.
        :rtype: int
        """
        return self._max_session

    @max_session.setter
    def max_session(self, max_session):
        """Sets the max_session of this RoutePolicy.

        单台服务器最大的链接会话数

        :param max_session: The max_session of this RoutePolicy.
        :type max_session: int
        """
        self._max_session = max_session

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
        if not isinstance(other, RoutePolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
