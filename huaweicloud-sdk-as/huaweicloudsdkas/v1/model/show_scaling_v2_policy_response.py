# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowScalingV2PolicyResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'scaling_policy': 'ScalingV2PolicyDetail'
    }

    attribute_map = {
        'scaling_policy': 'scaling_policy'
    }

    def __init__(self, scaling_policy=None):
        r"""ShowScalingV2PolicyResponse

        The model defined in huaweicloud sdk

        :param scaling_policy: 
        :type scaling_policy: :class:`huaweicloudsdkas.v1.ScalingV2PolicyDetail`
        """
        
        super(ShowScalingV2PolicyResponse, self).__init__()

        self._scaling_policy = None
        self.discriminator = None

        if scaling_policy is not None:
            self.scaling_policy = scaling_policy

    @property
    def scaling_policy(self):
        r"""Gets the scaling_policy of this ShowScalingV2PolicyResponse.

        :return: The scaling_policy of this ShowScalingV2PolicyResponse.
        :rtype: :class:`huaweicloudsdkas.v1.ScalingV2PolicyDetail`
        """
        return self._scaling_policy

    @scaling_policy.setter
    def scaling_policy(self, scaling_policy):
        r"""Sets the scaling_policy of this ShowScalingV2PolicyResponse.

        :param scaling_policy: The scaling_policy of this ShowScalingV2PolicyResponse.
        :type scaling_policy: :class:`huaweicloudsdkas.v1.ScalingV2PolicyDetail`
        """
        self._scaling_policy = scaling_policy

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
        if not isinstance(other, ShowScalingV2PolicyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
