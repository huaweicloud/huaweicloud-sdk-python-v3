# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SpecialAgreementSignReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'agreement_type': 'str',
        'to_sign': 'bool'
    }

    attribute_map = {
        'agreement_type': 'agreement_type',
        'to_sign': 'to_sign'
    }

    def __init__(self, agreement_type=None, to_sign=None):
        r"""SpecialAgreementSignReq

        The model defined in huaweicloud sdk

        :param agreement_type: 当前服务协议类型: AUTO_PAY: 自动支付协议
        :type agreement_type: str
        :param to_sign: 是否为去签署,true:签署;false:取消签署
        :type to_sign: bool
        """
        
        

        self._agreement_type = None
        self._to_sign = None
        self.discriminator = None

        self.agreement_type = agreement_type
        self.to_sign = to_sign

    @property
    def agreement_type(self):
        r"""Gets the agreement_type of this SpecialAgreementSignReq.

        当前服务协议类型: AUTO_PAY: 自动支付协议

        :return: The agreement_type of this SpecialAgreementSignReq.
        :rtype: str
        """
        return self._agreement_type

    @agreement_type.setter
    def agreement_type(self, agreement_type):
        r"""Sets the agreement_type of this SpecialAgreementSignReq.

        当前服务协议类型: AUTO_PAY: 自动支付协议

        :param agreement_type: The agreement_type of this SpecialAgreementSignReq.
        :type agreement_type: str
        """
        self._agreement_type = agreement_type

    @property
    def to_sign(self):
        r"""Gets the to_sign of this SpecialAgreementSignReq.

        是否为去签署,true:签署;false:取消签署

        :return: The to_sign of this SpecialAgreementSignReq.
        :rtype: bool
        """
        return self._to_sign

    @to_sign.setter
    def to_sign(self, to_sign):
        r"""Sets the to_sign of this SpecialAgreementSignReq.

        是否为去签署,true:签署;false:取消签署

        :param to_sign: The to_sign of this SpecialAgreementSignReq.
        :type to_sign: bool
        """
        self._to_sign = to_sign

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
        if not isinstance(other, SpecialAgreementSignReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
