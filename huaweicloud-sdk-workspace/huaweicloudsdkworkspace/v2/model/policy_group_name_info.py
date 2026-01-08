# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PolicyGroupNameInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'policy_group_name': 'str',
        'description': 'str'
    }

    attribute_map = {
        'policy_group_name': 'policy_group_name',
        'description': 'description'
    }

    def __init__(self, policy_group_name=None, description=None):
        r"""PolicyGroupNameInfo

        The model defined in huaweicloud sdk

        :param policy_group_name: 策略组名。
        :type policy_group_name: str
        :param description: 描述。
        :type description: str
        """
        
        

        self._policy_group_name = None
        self._description = None
        self.discriminator = None

        if policy_group_name is not None:
            self.policy_group_name = policy_group_name
        if description is not None:
            self.description = description

    @property
    def policy_group_name(self):
        r"""Gets the policy_group_name of this PolicyGroupNameInfo.

        策略组名。

        :return: The policy_group_name of this PolicyGroupNameInfo.
        :rtype: str
        """
        return self._policy_group_name

    @policy_group_name.setter
    def policy_group_name(self, policy_group_name):
        r"""Sets the policy_group_name of this PolicyGroupNameInfo.

        策略组名。

        :param policy_group_name: The policy_group_name of this PolicyGroupNameInfo.
        :type policy_group_name: str
        """
        self._policy_group_name = policy_group_name

    @property
    def description(self):
        r"""Gets the description of this PolicyGroupNameInfo.

        描述。

        :return: The description of this PolicyGroupNameInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this PolicyGroupNameInfo.

        描述。

        :param description: The description of this PolicyGroupNameInfo.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, PolicyGroupNameInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
