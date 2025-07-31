# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateCustomerIpsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ips_cfw_id': 'str',
        'body': 'CustomerIpsSaveDto'
    }

    attribute_map = {
        'ips_cfw_id': 'ips_cfw_id',
        'body': 'body'
    }

    def __init__(self, ips_cfw_id=None, body=None):
        r"""UpdateCustomerIpsRequest

        The model defined in huaweicloud sdk

        :param ips_cfw_id: **参数解释**： cfw侧自定义IPS规则id **约束限制**： 不涉及 **取值范围**： 32位UUID **默认取值**： 不涉及
        :type ips_cfw_id: str
        :param body: Body of the UpdateCustomerIpsRequest
        :type body: :class:`huaweicloudsdkcfw.v1.CustomerIpsSaveDto`
        """
        
        

        self._ips_cfw_id = None
        self._body = None
        self.discriminator = None

        self.ips_cfw_id = ips_cfw_id
        if body is not None:
            self.body = body

    @property
    def ips_cfw_id(self):
        r"""Gets the ips_cfw_id of this UpdateCustomerIpsRequest.

        **参数解释**： cfw侧自定义IPS规则id **约束限制**： 不涉及 **取值范围**： 32位UUID **默认取值**： 不涉及

        :return: The ips_cfw_id of this UpdateCustomerIpsRequest.
        :rtype: str
        """
        return self._ips_cfw_id

    @ips_cfw_id.setter
    def ips_cfw_id(self, ips_cfw_id):
        r"""Sets the ips_cfw_id of this UpdateCustomerIpsRequest.

        **参数解释**： cfw侧自定义IPS规则id **约束限制**： 不涉及 **取值范围**： 32位UUID **默认取值**： 不涉及

        :param ips_cfw_id: The ips_cfw_id of this UpdateCustomerIpsRequest.
        :type ips_cfw_id: str
        """
        self._ips_cfw_id = ips_cfw_id

    @property
    def body(self):
        r"""Gets the body of this UpdateCustomerIpsRequest.

        :return: The body of this UpdateCustomerIpsRequest.
        :rtype: :class:`huaweicloudsdkcfw.v1.CustomerIpsSaveDto`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateCustomerIpsRequest.

        :param body: The body of this UpdateCustomerIpsRequest.
        :type body: :class:`huaweicloudsdkcfw.v1.CustomerIpsSaveDto`
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
        if not isinstance(other, UpdateCustomerIpsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
