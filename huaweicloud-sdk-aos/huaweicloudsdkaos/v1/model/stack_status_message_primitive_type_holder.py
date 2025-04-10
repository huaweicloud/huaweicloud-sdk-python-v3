# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StackStatusMessagePrimitiveTypeHolder:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status_message': 'str'
    }

    attribute_map = {
        'status_message': 'status_message'
    }

    def __init__(self, status_message=None):
        r"""StackStatusMessagePrimitiveTypeHolder

        The model defined in huaweicloud sdk

        :param status_message: 当资源栈的状态为任意失败状态（即以 &#x60;FAILED&#x60; 结尾时），将会展示简要的错误信息总结以供debug
        :type status_message: str
        """
        
        

        self._status_message = None
        self.discriminator = None

        if status_message is not None:
            self.status_message = status_message

    @property
    def status_message(self):
        r"""Gets the status_message of this StackStatusMessagePrimitiveTypeHolder.

        当资源栈的状态为任意失败状态（即以 `FAILED` 结尾时），将会展示简要的错误信息总结以供debug

        :return: The status_message of this StackStatusMessagePrimitiveTypeHolder.
        :rtype: str
        """
        return self._status_message

    @status_message.setter
    def status_message(self, status_message):
        r"""Sets the status_message of this StackStatusMessagePrimitiveTypeHolder.

        当资源栈的状态为任意失败状态（即以 `FAILED` 结尾时），将会展示简要的错误信息总结以供debug

        :param status_message: The status_message of this StackStatusMessagePrimitiveTypeHolder.
        :type status_message: str
        """
        self._status_message = status_message

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
        if not isinstance(other, StackStatusMessagePrimitiveTypeHolder):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
