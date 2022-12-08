# coding: utf-8

import re
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
        'session_consistence': 'str'
    }

    attribute_map = {
        'session_consistence': 'session_consistence'
    }

    def __init__(self, session_consistence=None):
        """ModifyProxyConsistRequest

        The model defined in huaweicloud sdk

        :param session_consistence: 会话一致性。 - 取值\&quot;true\&quot;时表示会话一致性开启。 - 取值\&quot;false\&quot;时表示会话一致性关闭。
        :type session_consistence: str
        """
        
        

        self._session_consistence = None
        self.discriminator = None

        self.session_consistence = session_consistence

    @property
    def session_consistence(self):
        """Gets the session_consistence of this ModifyProxyConsistRequest.

        会话一致性。 - 取值\"true\"时表示会话一致性开启。 - 取值\"false\"时表示会话一致性关闭。

        :return: The session_consistence of this ModifyProxyConsistRequest.
        :rtype: str
        """
        return self._session_consistence

    @session_consistence.setter
    def session_consistence(self, session_consistence):
        """Sets the session_consistence of this ModifyProxyConsistRequest.

        会话一致性。 - 取值\"true\"时表示会话一致性开启。 - 取值\"false\"时表示会话一致性关闭。

        :param session_consistence: The session_consistence of this ModifyProxyConsistRequest.
        :type session_consistence: str
        """
        self._session_consistence = session_consistence

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
