# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowEffectivePoliciesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'last_updated_at': 'datetime',
        'policy_content': 'str',
        'policy_type': 'str',
        'entity_id': 'str'
    }

    attribute_map = {
        'last_updated_at': 'last_updated_at',
        'policy_content': 'policy_content',
        'policy_type': 'policy_type',
        'entity_id': 'entity_id'
    }

    def __init__(self, last_updated_at=None, policy_content=None, policy_type=None, entity_id=None):
        r"""ShowEffectivePoliciesResponse

        The model defined in huaweicloud sdk

        :param last_updated_at: 有效策略最后更新时间。
        :type last_updated_at: datetime
        :param policy_content: 有效策略文本内容。
        :type policy_content: str
        :param policy_type: 策略类型的名称。tag_policy标签策略。
        :type policy_type: str
        :param entity_id: 根、组织单元或账号的唯一标识符（ID）。
        :type entity_id: str
        """
        
        super(ShowEffectivePoliciesResponse, self).__init__()

        self._last_updated_at = None
        self._policy_content = None
        self._policy_type = None
        self._entity_id = None
        self.discriminator = None

        if last_updated_at is not None:
            self.last_updated_at = last_updated_at
        if policy_content is not None:
            self.policy_content = policy_content
        if policy_type is not None:
            self.policy_type = policy_type
        if entity_id is not None:
            self.entity_id = entity_id

    @property
    def last_updated_at(self):
        r"""Gets the last_updated_at of this ShowEffectivePoliciesResponse.

        有效策略最后更新时间。

        :return: The last_updated_at of this ShowEffectivePoliciesResponse.
        :rtype: datetime
        """
        return self._last_updated_at

    @last_updated_at.setter
    def last_updated_at(self, last_updated_at):
        r"""Sets the last_updated_at of this ShowEffectivePoliciesResponse.

        有效策略最后更新时间。

        :param last_updated_at: The last_updated_at of this ShowEffectivePoliciesResponse.
        :type last_updated_at: datetime
        """
        self._last_updated_at = last_updated_at

    @property
    def policy_content(self):
        r"""Gets the policy_content of this ShowEffectivePoliciesResponse.

        有效策略文本内容。

        :return: The policy_content of this ShowEffectivePoliciesResponse.
        :rtype: str
        """
        return self._policy_content

    @policy_content.setter
    def policy_content(self, policy_content):
        r"""Sets the policy_content of this ShowEffectivePoliciesResponse.

        有效策略文本内容。

        :param policy_content: The policy_content of this ShowEffectivePoliciesResponse.
        :type policy_content: str
        """
        self._policy_content = policy_content

    @property
    def policy_type(self):
        r"""Gets the policy_type of this ShowEffectivePoliciesResponse.

        策略类型的名称。tag_policy标签策略。

        :return: The policy_type of this ShowEffectivePoliciesResponse.
        :rtype: str
        """
        return self._policy_type

    @policy_type.setter
    def policy_type(self, policy_type):
        r"""Sets the policy_type of this ShowEffectivePoliciesResponse.

        策略类型的名称。tag_policy标签策略。

        :param policy_type: The policy_type of this ShowEffectivePoliciesResponse.
        :type policy_type: str
        """
        self._policy_type = policy_type

    @property
    def entity_id(self):
        r"""Gets the entity_id of this ShowEffectivePoliciesResponse.

        根、组织单元或账号的唯一标识符（ID）。

        :return: The entity_id of this ShowEffectivePoliciesResponse.
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        r"""Sets the entity_id of this ShowEffectivePoliciesResponse.

        根、组织单元或账号的唯一标识符（ID）。

        :param entity_id: The entity_id of this ShowEffectivePoliciesResponse.
        :type entity_id: str
        """
        self._entity_id = entity_id

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
        if not isinstance(other, ShowEffectivePoliciesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
