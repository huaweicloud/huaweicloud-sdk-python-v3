# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateObsTargetPolicyResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'target_id': 'str',
        'policy': 'ObsDataRepositoryPolicy',
        'x_request_id': 'str'
    }

    attribute_map = {
        'target_id': 'target_id',
        'policy': 'policy',
        'x_request_id': 'X-request-id'
    }

    def __init__(self, target_id=None, policy=None, x_request_id=None):
        r"""UpdateObsTargetPolicyResponse

        The model defined in huaweicloud sdk

        :param target_id: 绑定关系ID
        :type target_id: str
        :param policy: 
        :type policy: :class:`huaweicloudsdksfsturbo.v1.ObsDataRepositoryPolicy`
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(UpdateObsTargetPolicyResponse, self).__init__()

        self._target_id = None
        self._policy = None
        self._x_request_id = None
        self.discriminator = None

        if target_id is not None:
            self.target_id = target_id
        if policy is not None:
            self.policy = policy
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def target_id(self):
        r"""Gets the target_id of this UpdateObsTargetPolicyResponse.

        绑定关系ID

        :return: The target_id of this UpdateObsTargetPolicyResponse.
        :rtype: str
        """
        return self._target_id

    @target_id.setter
    def target_id(self, target_id):
        r"""Sets the target_id of this UpdateObsTargetPolicyResponse.

        绑定关系ID

        :param target_id: The target_id of this UpdateObsTargetPolicyResponse.
        :type target_id: str
        """
        self._target_id = target_id

    @property
    def policy(self):
        r"""Gets the policy of this UpdateObsTargetPolicyResponse.

        :return: The policy of this UpdateObsTargetPolicyResponse.
        :rtype: :class:`huaweicloudsdksfsturbo.v1.ObsDataRepositoryPolicy`
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        r"""Sets the policy of this UpdateObsTargetPolicyResponse.

        :param policy: The policy of this UpdateObsTargetPolicyResponse.
        :type policy: :class:`huaweicloudsdksfsturbo.v1.ObsDataRepositoryPolicy`
        """
        self._policy = policy

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this UpdateObsTargetPolicyResponse.

        :return: The x_request_id of this UpdateObsTargetPolicyResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this UpdateObsTargetPolicyResponse.

        :param x_request_id: The x_request_id of this UpdateObsTargetPolicyResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, UpdateObsTargetPolicyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
