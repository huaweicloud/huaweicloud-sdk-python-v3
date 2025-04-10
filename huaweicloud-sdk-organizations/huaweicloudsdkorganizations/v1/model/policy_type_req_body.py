# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PolicyTypeReqBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'policy_type': 'str',
        'root_id': 'str'
    }

    attribute_map = {
        'policy_type': 'policy_type',
        'root_id': 'root_id'
    }

    def __init__(self, policy_type=None, root_id=None):
        r"""PolicyTypeReqBody

        The model defined in huaweicloud sdk

        :param policy_type: 策略类型的名称，service_control_policy服务控制策略；tag_policy：标签策略。
        :type policy_type: str
        :param root_id: 根的唯一标识符（ID）。
        :type root_id: str
        """
        
        

        self._policy_type = None
        self._root_id = None
        self.discriminator = None

        self.policy_type = policy_type
        self.root_id = root_id

    @property
    def policy_type(self):
        r"""Gets the policy_type of this PolicyTypeReqBody.

        策略类型的名称，service_control_policy服务控制策略；tag_policy：标签策略。

        :return: The policy_type of this PolicyTypeReqBody.
        :rtype: str
        """
        return self._policy_type

    @policy_type.setter
    def policy_type(self, policy_type):
        r"""Sets the policy_type of this PolicyTypeReqBody.

        策略类型的名称，service_control_policy服务控制策略；tag_policy：标签策略。

        :param policy_type: The policy_type of this PolicyTypeReqBody.
        :type policy_type: str
        """
        self._policy_type = policy_type

    @property
    def root_id(self):
        r"""Gets the root_id of this PolicyTypeReqBody.

        根的唯一标识符（ID）。

        :return: The root_id of this PolicyTypeReqBody.
        :rtype: str
        """
        return self._root_id

    @root_id.setter
    def root_id(self, root_id):
        r"""Sets the root_id of this PolicyTypeReqBody.

        根的唯一标识符（ID）。

        :param root_id: The root_id of this PolicyTypeReqBody.
        :type root_id: str
        """
        self._root_id = root_id

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
        if not isinstance(other, PolicyTypeReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
