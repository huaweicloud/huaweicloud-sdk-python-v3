# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResumeScalingPolicyRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'scaling_policy_id': 'str',
        'body': 'ResumeScalingPolicyOption'
    }

    attribute_map = {
        'scaling_policy_id': 'scaling_policy_id',
        'body': 'body'
    }

    def __init__(self, scaling_policy_id=None, body=None):
        r"""ResumeScalingPolicyRequest

        The model defined in huaweicloud sdk

        :param scaling_policy_id: 伸缩策略ID。
        :type scaling_policy_id: str
        :param body: Body of the ResumeScalingPolicyRequest
        :type body: :class:`huaweicloudsdkas.v1.ResumeScalingPolicyOption`
        """
        
        

        self._scaling_policy_id = None
        self._body = None
        self.discriminator = None

        self.scaling_policy_id = scaling_policy_id
        if body is not None:
            self.body = body

    @property
    def scaling_policy_id(self):
        r"""Gets the scaling_policy_id of this ResumeScalingPolicyRequest.

        伸缩策略ID。

        :return: The scaling_policy_id of this ResumeScalingPolicyRequest.
        :rtype: str
        """
        return self._scaling_policy_id

    @scaling_policy_id.setter
    def scaling_policy_id(self, scaling_policy_id):
        r"""Sets the scaling_policy_id of this ResumeScalingPolicyRequest.

        伸缩策略ID。

        :param scaling_policy_id: The scaling_policy_id of this ResumeScalingPolicyRequest.
        :type scaling_policy_id: str
        """
        self._scaling_policy_id = scaling_policy_id

    @property
    def body(self):
        r"""Gets the body of this ResumeScalingPolicyRequest.

        :return: The body of this ResumeScalingPolicyRequest.
        :rtype: :class:`huaweicloudsdkas.v1.ResumeScalingPolicyOption`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this ResumeScalingPolicyRequest.

        :param body: The body of this ResumeScalingPolicyRequest.
        :type body: :class:`huaweicloudsdkas.v1.ResumeScalingPolicyOption`
        """
        self._body = body

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
        if not isinstance(other, ResumeScalingPolicyRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
