# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchUpdateRuleStatusRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain_name': 'str',
        'body': 'BatchUpdateRulesRequest'
    }

    attribute_map = {
        'domain_name': 'domain_name',
        'body': 'body'
    }

    def __init__(self, domain_name=None, body=None):
        r"""BatchUpdateRuleStatusRequest

        The model defined in huaweicloud sdk

        :param domain_name: **参数解释：** 加速域名 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type domain_name: str
        :param body: Body of the BatchUpdateRuleStatusRequest
        :type body: :class:`huaweicloudsdkcdn.v2.BatchUpdateRulesRequest`
        """
        
        

        self._domain_name = None
        self._body = None
        self.discriminator = None

        self.domain_name = domain_name
        if body is not None:
            self.body = body

    @property
    def domain_name(self):
        r"""Gets the domain_name of this BatchUpdateRuleStatusRequest.

        **参数解释：** 加速域名 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The domain_name of this BatchUpdateRuleStatusRequest.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        r"""Sets the domain_name of this BatchUpdateRuleStatusRequest.

        **参数解释：** 加速域名 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param domain_name: The domain_name of this BatchUpdateRuleStatusRequest.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def body(self):
        r"""Gets the body of this BatchUpdateRuleStatusRequest.

        :return: The body of this BatchUpdateRuleStatusRequest.
        :rtype: :class:`huaweicloudsdkcdn.v2.BatchUpdateRulesRequest`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this BatchUpdateRuleStatusRequest.

        :param body: The body of this BatchUpdateRuleStatusRequest.
        :type body: :class:`huaweicloudsdkcdn.v2.BatchUpdateRulesRequest`
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
        if not isinstance(other, BatchUpdateRuleStatusRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
