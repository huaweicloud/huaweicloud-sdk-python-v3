# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RegisterServerAutoRecoveryRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'support_auto_recovery': 'str'
    }

    attribute_map = {
        'support_auto_recovery': 'support_auto_recovery'
    }

    def __init__(self, support_auto_recovery=None):
        """RegisterServerAutoRecoveryRequestBody

        The model defined in huaweicloud sdk

        :param support_auto_recovery: 云服务器是否配置了自动恢复动作。  - true：表示配置自动恢复。 - false：表示删除自动恢复。
        :type support_auto_recovery: str
        """
        
        

        self._support_auto_recovery = None
        self.discriminator = None

        self.support_auto_recovery = support_auto_recovery

    @property
    def support_auto_recovery(self):
        """Gets the support_auto_recovery of this RegisterServerAutoRecoveryRequestBody.

        云服务器是否配置了自动恢复动作。  - true：表示配置自动恢复。 - false：表示删除自动恢复。

        :return: The support_auto_recovery of this RegisterServerAutoRecoveryRequestBody.
        :rtype: str
        """
        return self._support_auto_recovery

    @support_auto_recovery.setter
    def support_auto_recovery(self, support_auto_recovery):
        """Sets the support_auto_recovery of this RegisterServerAutoRecoveryRequestBody.

        云服务器是否配置了自动恢复动作。  - true：表示配置自动恢复。 - false：表示删除自动恢复。

        :param support_auto_recovery: The support_auto_recovery of this RegisterServerAutoRecoveryRequestBody.
        :type support_auto_recovery: str
        """
        self._support_auto_recovery = support_auto_recovery

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
        if not isinstance(other, RegisterServerAutoRecoveryRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
