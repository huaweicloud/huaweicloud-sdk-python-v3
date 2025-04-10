# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReclaimEnterpriseMultiAccountCouponResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'real_retrieve_amout': 'str'
    }

    attribute_map = {
        'real_retrieve_amout': 'real_retrieve_amout'
    }

    def __init__(self, real_retrieve_amout=None):
        r"""ReclaimEnterpriseMultiAccountCouponResponse

        The model defined in huaweicloud sdk

        :param real_retrieve_amout: |参数名称：实际回收金额。| |参数的约束及描述：成功时返回|
        :type real_retrieve_amout: str
        """
        
        super(ReclaimEnterpriseMultiAccountCouponResponse, self).__init__()

        self._real_retrieve_amout = None
        self.discriminator = None

        if real_retrieve_amout is not None:
            self.real_retrieve_amout = real_retrieve_amout

    @property
    def real_retrieve_amout(self):
        r"""Gets the real_retrieve_amout of this ReclaimEnterpriseMultiAccountCouponResponse.

        |参数名称：实际回收金额。| |参数的约束及描述：成功时返回|

        :return: The real_retrieve_amout of this ReclaimEnterpriseMultiAccountCouponResponse.
        :rtype: str
        """
        return self._real_retrieve_amout

    @real_retrieve_amout.setter
    def real_retrieve_amout(self, real_retrieve_amout):
        r"""Sets the real_retrieve_amout of this ReclaimEnterpriseMultiAccountCouponResponse.

        |参数名称：实际回收金额。| |参数的约束及描述：成功时返回|

        :param real_retrieve_amout: The real_retrieve_amout of this ReclaimEnterpriseMultiAccountCouponResponse.
        :type real_retrieve_amout: str
        """
        self._real_retrieve_amout = real_retrieve_amout

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
        if not isinstance(other, ReclaimEnterpriseMultiAccountCouponResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
