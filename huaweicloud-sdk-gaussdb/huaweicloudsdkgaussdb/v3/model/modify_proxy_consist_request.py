# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModifyProxyConsistRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'session_consistence': 'str',
        'consistence_mode': 'str'
    }

    attribute_map = {
        'session_consistence': 'session_consistence',
        'consistence_mode': 'consistence_mode'
    }

    def __init__(self, session_consistence=None, consistence_mode=None):
        r"""ModifyProxyConsistRequest

        The model defined in huaweicloud sdk

        :param session_consistence: 会话一致性。 - 取值\&quot;true\&quot;时表示会话一致性开启。 - 取值\&quot;false\&quot;时表示会话一致性关闭。
        :type session_consistence: str
        :param consistence_mode: 一致性模式。默认值为空，此时以会话一致性参数session_consistence为准。 - session: 会话一致性 - global: 全局一致性 - eventual: 最终一致性
        :type consistence_mode: str
        """
        
        

        self._session_consistence = None
        self._consistence_mode = None
        self.discriminator = None

        self.session_consistence = session_consistence
        if consistence_mode is not None:
            self.consistence_mode = consistence_mode

    @property
    def session_consistence(self):
        r"""Gets the session_consistence of this ModifyProxyConsistRequest.

        会话一致性。 - 取值\"true\"时表示会话一致性开启。 - 取值\"false\"时表示会话一致性关闭。

        :return: The session_consistence of this ModifyProxyConsistRequest.
        :rtype: str
        """
        return self._session_consistence

    @session_consistence.setter
    def session_consistence(self, session_consistence):
        r"""Sets the session_consistence of this ModifyProxyConsistRequest.

        会话一致性。 - 取值\"true\"时表示会话一致性开启。 - 取值\"false\"时表示会话一致性关闭。

        :param session_consistence: The session_consistence of this ModifyProxyConsistRequest.
        :type session_consistence: str
        """
        self._session_consistence = session_consistence

    @property
    def consistence_mode(self):
        r"""Gets the consistence_mode of this ModifyProxyConsistRequest.

        一致性模式。默认值为空，此时以会话一致性参数session_consistence为准。 - session: 会话一致性 - global: 全局一致性 - eventual: 最终一致性

        :return: The consistence_mode of this ModifyProxyConsistRequest.
        :rtype: str
        """
        return self._consistence_mode

    @consistence_mode.setter
    def consistence_mode(self, consistence_mode):
        r"""Sets the consistence_mode of this ModifyProxyConsistRequest.

        一致性模式。默认值为空，此时以会话一致性参数session_consistence为准。 - session: 会话一致性 - global: 全局一致性 - eventual: 最终一致性

        :param consistence_mode: The consistence_mode of this ModifyProxyConsistRequest.
        :type consistence_mode: str
        """
        self._consistence_mode = consistence_mode

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
        if not isinstance(other, ModifyProxyConsistRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
