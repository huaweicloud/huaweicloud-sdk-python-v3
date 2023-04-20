# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ErrorCodeRedirectRules:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'error_code': 'int',
        'target_code': 'int',
        'target_link': 'str'
    }

    attribute_map = {
        'error_code': 'error_code',
        'target_code': 'target_code',
        'target_link': 'target_link'
    }

    def __init__(self, error_code=None, target_code=None, target_link=None):
        """ErrorCodeRedirectRules

        The model defined in huaweicloud sdk

        :param error_code: 重定向的错误码，当前支持以下状态码 4xx:400, 403, 404, 405, 414, 416, 451 5xx:500, 501, 502, 503, 504
        :type error_code: int
        :param target_code: 重定向状态码，取值为301或302
        :type target_code: int
        :param target_link: 重定向的目标链接
        :type target_link: str
        """
        
        

        self._error_code = None
        self._target_code = None
        self._target_link = None
        self.discriminator = None

        self.error_code = error_code
        self.target_code = target_code
        self.target_link = target_link

    @property
    def error_code(self):
        """Gets the error_code of this ErrorCodeRedirectRules.

        重定向的错误码，当前支持以下状态码 4xx:400, 403, 404, 405, 414, 416, 451 5xx:500, 501, 502, 503, 504

        :return: The error_code of this ErrorCodeRedirectRules.
        :rtype: int
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this ErrorCodeRedirectRules.

        重定向的错误码，当前支持以下状态码 4xx:400, 403, 404, 405, 414, 416, 451 5xx:500, 501, 502, 503, 504

        :param error_code: The error_code of this ErrorCodeRedirectRules.
        :type error_code: int
        """
        self._error_code = error_code

    @property
    def target_code(self):
        """Gets the target_code of this ErrorCodeRedirectRules.

        重定向状态码，取值为301或302

        :return: The target_code of this ErrorCodeRedirectRules.
        :rtype: int
        """
        return self._target_code

    @target_code.setter
    def target_code(self, target_code):
        """Sets the target_code of this ErrorCodeRedirectRules.

        重定向状态码，取值为301或302

        :param target_code: The target_code of this ErrorCodeRedirectRules.
        :type target_code: int
        """
        self._target_code = target_code

    @property
    def target_link(self):
        """Gets the target_link of this ErrorCodeRedirectRules.

        重定向的目标链接

        :return: The target_link of this ErrorCodeRedirectRules.
        :rtype: str
        """
        return self._target_link

    @target_link.setter
    def target_link(self, target_link):
        """Sets the target_link of this ErrorCodeRedirectRules.

        重定向的目标链接

        :param target_link: The target_link of this ErrorCodeRedirectRules.
        :type target_link: str
        """
        self._target_link = target_link

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
        if not isinstance(other, ErrorCodeRedirectRules):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
