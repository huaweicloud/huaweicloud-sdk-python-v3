# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowRestartPolicyResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'restart_server': 'bool',
        'restart_policy': 'object'
    }

    attribute_map = {
        'restart_server': 'restart_server',
        'restart_policy': 'restart_policy'
    }

    def __init__(self, restart_server=None, restart_policy=None):
        r"""ShowRestartPolicyResponse

        The model defined in huaweicloud sdk

        :param restart_server: 是否重启虚拟机。
        :type restart_server: bool
        :param restart_policy: 重启策略。
        :type restart_policy: object
        """
        
        super().__init__()

        self._restart_server = None
        self._restart_policy = None
        self.discriminator = None

        if restart_server is not None:
            self.restart_server = restart_server
        if restart_policy is not None:
            self.restart_policy = restart_policy

    @property
    def restart_server(self):
        r"""Gets the restart_server of this ShowRestartPolicyResponse.

        是否重启虚拟机。

        :return: The restart_server of this ShowRestartPolicyResponse.
        :rtype: bool
        """
        return self._restart_server

    @restart_server.setter
    def restart_server(self, restart_server):
        r"""Sets the restart_server of this ShowRestartPolicyResponse.

        是否重启虚拟机。

        :param restart_server: The restart_server of this ShowRestartPolicyResponse.
        :type restart_server: bool
        """
        self._restart_server = restart_server

    @property
    def restart_policy(self):
        r"""Gets the restart_policy of this ShowRestartPolicyResponse.

        重启策略。

        :return: The restart_policy of this ShowRestartPolicyResponse.
        :rtype: object
        """
        return self._restart_policy

    @restart_policy.setter
    def restart_policy(self, restart_policy):
        r"""Sets the restart_policy of this ShowRestartPolicyResponse.

        重启策略。

        :param restart_policy: The restart_policy of this ShowRestartPolicyResponse.
        :type restart_policy: object
        """
        self._restart_policy = restart_policy

    def to_dict(self):
        import warnings
        warnings.warn("ShowRestartPolicyResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ShowRestartPolicyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
