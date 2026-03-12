# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDryRunConfigRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []
    sensitive_list.append('x_security_token')

    openapi_types = {
        'x_security_token': 'str',
        'root_id': 'str',
        'policy_type': 'str'
    }

    attribute_map = {
        'x_security_token': 'X-Security-Token',
        'root_id': 'root_id',
        'policy_type': 'policy_type'
    }

    def __init__(self, x_security_token=None, root_id=None, policy_type=None):
        r"""ShowDryRunConfigRequest

        The model defined in huaweicloud sdk

        :param x_security_token: 如果正在使用临时安全凭据，则此header是必需的，该值是临时安全凭据的安全令牌（会话令牌）。
        :type x_security_token: str
        :param root_id: 根的唯一标识符（ID）。
        :type root_id: str
        :param policy_type: 试运行策略的类型名称，service_control_policy：服务控制策略。
        :type policy_type: str
        """
        
        

        self._x_security_token = None
        self._root_id = None
        self._policy_type = None
        self.discriminator = None

        if x_security_token is not None:
            self.x_security_token = x_security_token
        self.root_id = root_id
        self.policy_type = policy_type

    @property
    def x_security_token(self):
        r"""Gets the x_security_token of this ShowDryRunConfigRequest.

        如果正在使用临时安全凭据，则此header是必需的，该值是临时安全凭据的安全令牌（会话令牌）。

        :return: The x_security_token of this ShowDryRunConfigRequest.
        :rtype: str
        """
        return self._x_security_token

    @x_security_token.setter
    def x_security_token(self, x_security_token):
        r"""Sets the x_security_token of this ShowDryRunConfigRequest.

        如果正在使用临时安全凭据，则此header是必需的，该值是临时安全凭据的安全令牌（会话令牌）。

        :param x_security_token: The x_security_token of this ShowDryRunConfigRequest.
        :type x_security_token: str
        """
        self._x_security_token = x_security_token

    @property
    def root_id(self):
        r"""Gets the root_id of this ShowDryRunConfigRequest.

        根的唯一标识符（ID）。

        :return: The root_id of this ShowDryRunConfigRequest.
        :rtype: str
        """
        return self._root_id

    @root_id.setter
    def root_id(self, root_id):
        r"""Sets the root_id of this ShowDryRunConfigRequest.

        根的唯一标识符（ID）。

        :param root_id: The root_id of this ShowDryRunConfigRequest.
        :type root_id: str
        """
        self._root_id = root_id

    @property
    def policy_type(self):
        r"""Gets the policy_type of this ShowDryRunConfigRequest.

        试运行策略的类型名称，service_control_policy：服务控制策略。

        :return: The policy_type of this ShowDryRunConfigRequest.
        :rtype: str
        """
        return self._policy_type

    @policy_type.setter
    def policy_type(self, policy_type):
        r"""Sets the policy_type of this ShowDryRunConfigRequest.

        试运行策略的类型名称，service_control_policy：服务控制策略。

        :param policy_type: The policy_type of this ShowDryRunConfigRequest.
        :type policy_type: str
        """
        self._policy_type = policy_type

    def to_dict(self):
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
        if not isinstance(other, ShowDryRunConfigRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
