# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowOriginalPolicyInfoResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'policies': 'Policies'
    }

    attribute_map = {
        'policies': 'policies'
    }

    def __init__(self, policies=None):
        """ShowOriginalPolicyInfoResponse

        The model defined in huaweicloud sdk

        :param policies: 
        :type policies: :class:`huaweicloudsdkworkspaceapp.v1.Policies`
        """
        
        super(ShowOriginalPolicyInfoResponse, self).__init__()

        self._policies = None
        self.discriminator = None

        if policies is not None:
            self.policies = policies

    @property
    def policies(self):
        """Gets the policies of this ShowOriginalPolicyInfoResponse.

        :return: The policies of this ShowOriginalPolicyInfoResponse.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.Policies`
        """
        return self._policies

    @policies.setter
    def policies(self, policies):
        """Sets the policies of this ShowOriginalPolicyInfoResponse.

        :param policies: The policies of this ShowOriginalPolicyInfoResponse.
        :type policies: :class:`huaweicloudsdkworkspaceapp.v1.Policies`
        """
        self._policies = policies

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
        if not isinstance(other, ShowOriginalPolicyInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
