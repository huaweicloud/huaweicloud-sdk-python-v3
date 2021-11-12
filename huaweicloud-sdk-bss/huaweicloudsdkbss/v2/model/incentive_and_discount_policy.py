# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IncentiveAndDiscountPolicy:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'service_type_code': 'str',
        'incentive_policy': 'str',
        'allow_discount': 'str'
    }

    attribute_map = {
        'service_type_code': 'service_type_code',
        'incentive_policy': 'incentive_policy',
        'allow_discount': 'allow_discount'
    }

    def __init__(self, service_type_code=None, incentive_policy=None, allow_discount=None):
        """IncentiveAndDiscountPolicy - a model defined in huaweicloud sdk"""
        
        

        self._service_type_code = None
        self._incentive_policy = None
        self._allow_discount = None
        self.discriminator = None

        if service_type_code is not None:
            self.service_type_code = service_type_code
        if incentive_policy is not None:
            self.incentive_policy = incentive_policy
        if allow_discount is not None:
            self.allow_discount = allow_discount

    @property
    def service_type_code(self):
        """Gets the service_type_code of this IncentiveAndDiscountPolicy.

        云服务类型列表。

        :return: The service_type_code of this IncentiveAndDiscountPolicy.
        :rtype: str
        """
        return self._service_type_code

    @service_type_code.setter
    def service_type_code(self, service_type_code):
        """Sets the service_type_code of this IncentiveAndDiscountPolicy.

        云服务类型列表。

        :param service_type_code: The service_type_code of this IncentiveAndDiscountPolicy.
        :type: str
        """
        self._service_type_code = service_type_code

    @property
    def incentive_policy(self):
        """Gets the incentive_policy of this IncentiveAndDiscountPolicy.

        激励策略。 0：非特定产品1：特定产品2：无业绩无返点13：有业绩无返点

        :return: The incentive_policy of this IncentiveAndDiscountPolicy.
        :rtype: str
        """
        return self._incentive_policy

    @incentive_policy.setter
    def incentive_policy(self, incentive_policy):
        """Sets the incentive_policy of this IncentiveAndDiscountPolicy.

        激励策略。 0：非特定产品1：特定产品2：无业绩无返点13：有业绩无返点

        :param incentive_policy: The incentive_policy of this IncentiveAndDiscountPolicy.
        :type: str
        """
        self._incentive_policy = incentive_policy

    @property
    def allow_discount(self):
        """Gets the allow_discount of this IncentiveAndDiscountPolicy.

        是否允许应用伙伴授予折扣。 YES：允许应用NO：不许应用

        :return: The allow_discount of this IncentiveAndDiscountPolicy.
        :rtype: str
        """
        return self._allow_discount

    @allow_discount.setter
    def allow_discount(self, allow_discount):
        """Sets the allow_discount of this IncentiveAndDiscountPolicy.

        是否允许应用伙伴授予折扣。 YES：允许应用NO：不许应用

        :param allow_discount: The allow_discount of this IncentiveAndDiscountPolicy.
        :type: str
        """
        self._allow_discount = allow_discount

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
        if not isinstance(other, IncentiveAndDiscountPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
