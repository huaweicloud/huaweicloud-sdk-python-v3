# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShareInfoFeature:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_support': 'bool',
        'message': 'str',
        'msg_code': 'str'
    }

    attribute_map = {
        'is_support': 'is_support',
        'message': 'message',
        'msg_code': 'msg_code'
    }

    def __init__(self, is_support=None, message=None, msg_code=None):
        r"""ShareInfoFeature

        The model defined in huaweicloud sdk

        :param is_support: 文件系统是否支持该特性
        :type is_support: bool
        :param message: 文件系统是否支持该特性的详细信息
        :type message: str
        :param msg_code: 文件系统是否支持该特性的详细信息
        :type msg_code: str
        """
        
        

        self._is_support = None
        self._message = None
        self._msg_code = None
        self.discriminator = None

        if is_support is not None:
            self.is_support = is_support
        if message is not None:
            self.message = message
        if msg_code is not None:
            self.msg_code = msg_code

    @property
    def is_support(self):
        r"""Gets the is_support of this ShareInfoFeature.

        文件系统是否支持该特性

        :return: The is_support of this ShareInfoFeature.
        :rtype: bool
        """
        return self._is_support

    @is_support.setter
    def is_support(self, is_support):
        r"""Sets the is_support of this ShareInfoFeature.

        文件系统是否支持该特性

        :param is_support: The is_support of this ShareInfoFeature.
        :type is_support: bool
        """
        self._is_support = is_support

    @property
    def message(self):
        r"""Gets the message of this ShareInfoFeature.

        文件系统是否支持该特性的详细信息

        :return: The message of this ShareInfoFeature.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this ShareInfoFeature.

        文件系统是否支持该特性的详细信息

        :param message: The message of this ShareInfoFeature.
        :type message: str
        """
        self._message = message

    @property
    def msg_code(self):
        r"""Gets the msg_code of this ShareInfoFeature.

        文件系统是否支持该特性的详细信息

        :return: The msg_code of this ShareInfoFeature.
        :rtype: str
        """
        return self._msg_code

    @msg_code.setter
    def msg_code(self, msg_code):
        r"""Sets the msg_code of this ShareInfoFeature.

        文件系统是否支持该特性的详细信息

        :param msg_code: The msg_code of this ShareInfoFeature.
        :type msg_code: str
        """
        self._msg_code = msg_code

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
        if not isinstance(other, ShareInfoFeature):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
