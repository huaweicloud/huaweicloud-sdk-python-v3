# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpenGaussResizeRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'flavor_ref': 'str',
        'is_auto_pay': 'bool'
    }

    attribute_map = {
        'flavor_ref': 'flavor_ref',
        'is_auto_pay': 'is_auto_pay'
    }

    def __init__(self, flavor_ref=None, is_auto_pay=None):
        """OpenGaussResizeRequest

        The model defined in huaweicloud sdk

        :param flavor_ref: 规格变更时选定的目标规格。新规格的资源规格编码。参考表1中GaussDB(for openGauss)的“规格编码”列内容获取。
        :type flavor_ref: str
        :param is_auto_pay: 创建包周期实例时可指定，表示是否自动从账户中支付，此字段不影响自动续订的支付方式。true，表示自动从账户中支付。false，表示手动从账户中支付，默认为该方式。
        :type is_auto_pay: bool
        """
        
        

        self._flavor_ref = None
        self._is_auto_pay = None
        self.discriminator = None

        self.flavor_ref = flavor_ref
        if is_auto_pay is not None:
            self.is_auto_pay = is_auto_pay

    @property
    def flavor_ref(self):
        """Gets the flavor_ref of this OpenGaussResizeRequest.

        规格变更时选定的目标规格。新规格的资源规格编码。参考表1中GaussDB(for openGauss)的“规格编码”列内容获取。

        :return: The flavor_ref of this OpenGaussResizeRequest.
        :rtype: str
        """
        return self._flavor_ref

    @flavor_ref.setter
    def flavor_ref(self, flavor_ref):
        """Sets the flavor_ref of this OpenGaussResizeRequest.

        规格变更时选定的目标规格。新规格的资源规格编码。参考表1中GaussDB(for openGauss)的“规格编码”列内容获取。

        :param flavor_ref: The flavor_ref of this OpenGaussResizeRequest.
        :type flavor_ref: str
        """
        self._flavor_ref = flavor_ref

    @property
    def is_auto_pay(self):
        """Gets the is_auto_pay of this OpenGaussResizeRequest.

        创建包周期实例时可指定，表示是否自动从账户中支付，此字段不影响自动续订的支付方式。true，表示自动从账户中支付。false，表示手动从账户中支付，默认为该方式。

        :return: The is_auto_pay of this OpenGaussResizeRequest.
        :rtype: bool
        """
        return self._is_auto_pay

    @is_auto_pay.setter
    def is_auto_pay(self, is_auto_pay):
        """Sets the is_auto_pay of this OpenGaussResizeRequest.

        创建包周期实例时可指定，表示是否自动从账户中支付，此字段不影响自动续订的支付方式。true，表示自动从账户中支付。false，表示手动从账户中支付，默认为该方式。

        :param is_auto_pay: The is_auto_pay of this OpenGaussResizeRequest.
        :type is_auto_pay: bool
        """
        self._is_auto_pay = is_auto_pay

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
        if not isinstance(other, OpenGaussResizeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
