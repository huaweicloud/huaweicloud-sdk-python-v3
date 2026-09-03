# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPoliciesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'policy_engine_id': 'str',
        'limit': 'int',
        'marker': 'str'
    }

    attribute_map = {
        'policy_engine_id': 'policy_engine_id',
        'limit': 'limit',
        'marker': 'marker'
    }

    def __init__(self, policy_engine_id=None, limit=None, marker=None):
        r"""ListPoliciesRequest

        The model defined in huaweicloud sdk

        :param policy_engine_id: System-generated unique identifier for the policy engine.
        :type policy_engine_id: str
        :param limit: 每页显示的条目数量。
        :type limit: int
        :param marker: 分页标记。
        :type marker: str
        """
        
        

        self._policy_engine_id = None
        self._limit = None
        self._marker = None
        self.discriminator = None

        self.policy_engine_id = policy_engine_id
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker

    @property
    def policy_engine_id(self):
        r"""Gets the policy_engine_id of this ListPoliciesRequest.

        System-generated unique identifier for the policy engine.

        :return: The policy_engine_id of this ListPoliciesRequest.
        :rtype: str
        """
        return self._policy_engine_id

    @policy_engine_id.setter
    def policy_engine_id(self, policy_engine_id):
        r"""Sets the policy_engine_id of this ListPoliciesRequest.

        System-generated unique identifier for the policy engine.

        :param policy_engine_id: The policy_engine_id of this ListPoliciesRequest.
        :type policy_engine_id: str
        """
        self._policy_engine_id = policy_engine_id

    @property
    def limit(self):
        r"""Gets the limit of this ListPoliciesRequest.

        每页显示的条目数量。

        :return: The limit of this ListPoliciesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListPoliciesRequest.

        每页显示的条目数量。

        :param limit: The limit of this ListPoliciesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ListPoliciesRequest.

        分页标记。

        :return: The marker of this ListPoliciesRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListPoliciesRequest.

        分页标记。

        :param marker: The marker of this ListPoliciesRequest.
        :type marker: str
        """
        self._marker = marker

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
        if not isinstance(other, ListPoliciesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
