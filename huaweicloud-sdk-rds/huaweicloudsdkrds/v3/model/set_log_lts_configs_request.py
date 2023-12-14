# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SetLogLtsConfigsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'engine': 'str',
        'x_language': 'str',
        'body': 'AddLogConfigResponseBody'
    }

    attribute_map = {
        'engine': 'engine',
        'x_language': 'X-Language',
        'body': 'body'
    }

    def __init__(self, engine=None, x_language=None, body=None):
        """SetLogLtsConfigsRequest

        The model defined in huaweicloud sdk

        :param engine: 引擎。
        :type engine: str
        :param x_language: 语言。
        :type x_language: str
        :param body: Body of the SetLogLtsConfigsRequest
        :type body: :class:`huaweicloudsdkrds.v3.AddLogConfigResponseBody`
        """
        
        

        self._engine = None
        self._x_language = None
        self._body = None
        self.discriminator = None

        self.engine = engine
        if x_language is not None:
            self.x_language = x_language
        if body is not None:
            self.body = body

    @property
    def engine(self):
        """Gets the engine of this SetLogLtsConfigsRequest.

        引擎。

        :return: The engine of this SetLogLtsConfigsRequest.
        :rtype: str
        """
        return self._engine

    @engine.setter
    def engine(self, engine):
        """Sets the engine of this SetLogLtsConfigsRequest.

        引擎。

        :param engine: The engine of this SetLogLtsConfigsRequest.
        :type engine: str
        """
        self._engine = engine

    @property
    def x_language(self):
        """Gets the x_language of this SetLogLtsConfigsRequest.

        语言。

        :return: The x_language of this SetLogLtsConfigsRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this SetLogLtsConfigsRequest.

        语言。

        :param x_language: The x_language of this SetLogLtsConfigsRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def body(self):
        """Gets the body of this SetLogLtsConfigsRequest.

        :return: The body of this SetLogLtsConfigsRequest.
        :rtype: :class:`huaweicloudsdkrds.v3.AddLogConfigResponseBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this SetLogLtsConfigsRequest.

        :param body: The body of this SetLogLtsConfigsRequest.
        :type body: :class:`huaweicloudsdkrds.v3.AddLogConfigResponseBody`
        """
        self._body = body

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
        if not isinstance(other, SetLogLtsConfigsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
