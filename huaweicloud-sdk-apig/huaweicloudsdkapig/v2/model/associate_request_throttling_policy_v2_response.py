# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class AssociateRequestThrottlingPolicyV2Response(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'throttle_applys': 'list[ThrottleBindingResp]'
    }

    attribute_map = {
        'throttle_applys': 'throttle_applys'
    }

    def __init__(self, throttle_applys=None):
        """AssociateRequestThrottlingPolicyV2Response - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._throttle_applys = None
        self.discriminator = None

        if throttle_applys is not None:
            self.throttle_applys = throttle_applys

    @property
    def throttle_applys(self):
        """Gets the throttle_applys of this AssociateRequestThrottlingPolicyV2Response.

        API与流控策略的绑定关系列表

        :return: The throttle_applys of this AssociateRequestThrottlingPolicyV2Response.
        :rtype: list[ThrottleBindingResp]
        """
        return self._throttle_applys

    @throttle_applys.setter
    def throttle_applys(self, throttle_applys):
        """Sets the throttle_applys of this AssociateRequestThrottlingPolicyV2Response.

        API与流控策略的绑定关系列表

        :param throttle_applys: The throttle_applys of this AssociateRequestThrottlingPolicyV2Response.
        :type: list[ThrottleBindingResp]
        """
        self._throttle_applys = throttle_applys

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AssociateRequestThrottlingPolicyV2Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
