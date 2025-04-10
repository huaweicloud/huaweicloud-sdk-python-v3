# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ScaleNodePoolOptions:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'scalable_checking': 'str',
        'billing_config_override': 'ScaleUpBillingConfigOverride'
    }

    attribute_map = {
        'scalable_checking': 'scalableChecking',
        'billing_config_override': 'billingConfigOverride'
    }

    def __init__(self, scalable_checking=None, billing_config_override=None):
        r"""ScaleNodePoolOptions

        The model defined in huaweicloud sdk

        :param scalable_checking: 扩容状态检查策略: instant(同步检查), async(异步检查)。默认同步检查instant 
        :type scalable_checking: str
        :param billing_config_override: 
        :type billing_config_override: :class:`huaweicloudsdkcce.v3.ScaleUpBillingConfigOverride`
        """
        
        

        self._scalable_checking = None
        self._billing_config_override = None
        self.discriminator = None

        if scalable_checking is not None:
            self.scalable_checking = scalable_checking
        if billing_config_override is not None:
            self.billing_config_override = billing_config_override

    @property
    def scalable_checking(self):
        r"""Gets the scalable_checking of this ScaleNodePoolOptions.

        扩容状态检查策略: instant(同步检查), async(异步检查)。默认同步检查instant 

        :return: The scalable_checking of this ScaleNodePoolOptions.
        :rtype: str
        """
        return self._scalable_checking

    @scalable_checking.setter
    def scalable_checking(self, scalable_checking):
        r"""Sets the scalable_checking of this ScaleNodePoolOptions.

        扩容状态检查策略: instant(同步检查), async(异步检查)。默认同步检查instant 

        :param scalable_checking: The scalable_checking of this ScaleNodePoolOptions.
        :type scalable_checking: str
        """
        self._scalable_checking = scalable_checking

    @property
    def billing_config_override(self):
        r"""Gets the billing_config_override of this ScaleNodePoolOptions.

        :return: The billing_config_override of this ScaleNodePoolOptions.
        :rtype: :class:`huaweicloudsdkcce.v3.ScaleUpBillingConfigOverride`
        """
        return self._billing_config_override

    @billing_config_override.setter
    def billing_config_override(self, billing_config_override):
        r"""Sets the billing_config_override of this ScaleNodePoolOptions.

        :param billing_config_override: The billing_config_override of this ScaleNodePoolOptions.
        :type billing_config_override: :class:`huaweicloudsdkcce.v3.ScaleUpBillingConfigOverride`
        """
        self._billing_config_override = billing_config_override

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
        if not isinstance(other, ScaleNodePoolOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
