# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ErrorCodeCache:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'code': 'int',
        'ttl': 'int'
    }

    attribute_map = {
        'code': 'code',
        'ttl': 'ttl'
    }

    def __init__(self, code=None, ttl=None):
        """ErrorCodeCache

        The model defined in huaweicloud sdk

        :param code: 允许配置的错误码: 400, 403, 404, 405, 414, 500, 501, 502, 503, 504
        :type code: int
        :param ttl: 错误码缓存时间，单位为秒，范围0-31,536,000(一年默认为365天)
        :type ttl: int
        """
        
        

        self._code = None
        self._ttl = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if ttl is not None:
            self.ttl = ttl

    @property
    def code(self):
        """Gets the code of this ErrorCodeCache.

        允许配置的错误码: 400, 403, 404, 405, 414, 500, 501, 502, 503, 504

        :return: The code of this ErrorCodeCache.
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this ErrorCodeCache.

        允许配置的错误码: 400, 403, 404, 405, 414, 500, 501, 502, 503, 504

        :param code: The code of this ErrorCodeCache.
        :type code: int
        """
        self._code = code

    @property
    def ttl(self):
        """Gets the ttl of this ErrorCodeCache.

        错误码缓存时间，单位为秒，范围0-31,536,000(一年默认为365天)

        :return: The ttl of this ErrorCodeCache.
        :rtype: int
        """
        return self._ttl

    @ttl.setter
    def ttl(self, ttl):
        """Sets the ttl of this ErrorCodeCache.

        错误码缓存时间，单位为秒，范围0-31,536,000(一年默认为365天)

        :param ttl: The ttl of this ErrorCodeCache.
        :type ttl: int
        """
        self._ttl = ttl

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
        if not isinstance(other, ErrorCodeCache):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
