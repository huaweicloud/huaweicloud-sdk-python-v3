# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResponseInfoResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'status': 'int',
        'body': 'str',
        'default': 'bool'
    }

    attribute_map = {
        'status': 'status',
        'body': 'body',
        'default': 'default'
    }

    def __init__(self, status=None, body=None, default=None):
        """ResponseInfoResp

        The model defined in huaweicloud sdk

        :param status: 响应的HTTP状态码
        :type status: int
        :param body: 响应的Body模板
        :type body: str
        :param default: 是否为默认响应
        :type default: bool
        """
        
        

        self._status = None
        self._body = None
        self._default = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if body is not None:
            self.body = body
        if default is not None:
            self.default = default

    @property
    def status(self):
        """Gets the status of this ResponseInfoResp.

        响应的HTTP状态码

        :return: The status of this ResponseInfoResp.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ResponseInfoResp.

        响应的HTTP状态码

        :param status: The status of this ResponseInfoResp.
        :type status: int
        """
        self._status = status

    @property
    def body(self):
        """Gets the body of this ResponseInfoResp.

        响应的Body模板

        :return: The body of this ResponseInfoResp.
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this ResponseInfoResp.

        响应的Body模板

        :param body: The body of this ResponseInfoResp.
        :type body: str
        """
        self._body = body

    @property
    def default(self):
        """Gets the default of this ResponseInfoResp.

        是否为默认响应

        :return: The default of this ResponseInfoResp.
        :rtype: bool
        """
        return self._default

    @default.setter
    def default(self, default):
        """Sets the default of this ResponseInfoResp.

        是否为默认响应

        :param default: The default of this ResponseInfoResp.
        :type default: bool
        """
        self._default = default

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
        if not isinstance(other, ResponseInfoResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
