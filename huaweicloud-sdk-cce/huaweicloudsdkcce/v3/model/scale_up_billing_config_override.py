# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ScaleUpBillingConfigOverride:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'billing_mode': 'int',
        'extend_param': 'ScaleUpExtendParam'
    }

    attribute_map = {
        'billing_mode': 'billingMode',
        'extend_param': 'extendParam'
    }

    def __init__(self, billing_mode=None, extend_param=None):
        r"""ScaleUpBillingConfigOverride

        The model defined in huaweicloud sdk

        :param billing_mode: 节点计费类型，0(按需)，1(包周期)
        :type billing_mode: int
        :param extend_param: 
        :type extend_param: :class:`huaweicloudsdkcce.v3.ScaleUpExtendParam`
        """
        
        

        self._billing_mode = None
        self._extend_param = None
        self.discriminator = None

        self.billing_mode = billing_mode
        if extend_param is not None:
            self.extend_param = extend_param

    @property
    def billing_mode(self):
        r"""Gets the billing_mode of this ScaleUpBillingConfigOverride.

        节点计费类型，0(按需)，1(包周期)

        :return: The billing_mode of this ScaleUpBillingConfigOverride.
        :rtype: int
        """
        return self._billing_mode

    @billing_mode.setter
    def billing_mode(self, billing_mode):
        r"""Sets the billing_mode of this ScaleUpBillingConfigOverride.

        节点计费类型，0(按需)，1(包周期)

        :param billing_mode: The billing_mode of this ScaleUpBillingConfigOverride.
        :type billing_mode: int
        """
        self._billing_mode = billing_mode

    @property
    def extend_param(self):
        r"""Gets the extend_param of this ScaleUpBillingConfigOverride.

        :return: The extend_param of this ScaleUpBillingConfigOverride.
        :rtype: :class:`huaweicloudsdkcce.v3.ScaleUpExtendParam`
        """
        return self._extend_param

    @extend_param.setter
    def extend_param(self, extend_param):
        r"""Sets the extend_param of this ScaleUpBillingConfigOverride.

        :param extend_param: The extend_param of this ScaleUpBillingConfigOverride.
        :type extend_param: :class:`huaweicloudsdkcce.v3.ScaleUpExtendParam`
        """
        self._extend_param = extend_param

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
        if not isinstance(other, ScaleUpBillingConfigOverride):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
