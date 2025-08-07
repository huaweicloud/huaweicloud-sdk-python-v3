# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdatePremiumHostAccessStatusRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'host_id': 'str',
        'body': 'UpdatePremiumHostAccessStatusRequestBody'
    }

    attribute_map = {
        'host_id': 'host_id',
        'body': 'body'
    }

    def __init__(self, host_id=None, body=None):
        r"""UpdatePremiumHostAccessStatusRequest

        The model defined in huaweicloud sdk

        :param host_id: **参数解释：** 独享模式域名ID **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type host_id: str
        :param body: Body of the UpdatePremiumHostAccessStatusRequest
        :type body: :class:`huaweicloudsdkwaf.v1.UpdatePremiumHostAccessStatusRequestBody`
        """
        
        

        self._host_id = None
        self._body = None
        self.discriminator = None

        self.host_id = host_id
        if body is not None:
            self.body = body

    @property
    def host_id(self):
        r"""Gets the host_id of this UpdatePremiumHostAccessStatusRequest.

        **参数解释：** 独享模式域名ID **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The host_id of this UpdatePremiumHostAccessStatusRequest.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this UpdatePremiumHostAccessStatusRequest.

        **参数解释：** 独享模式域名ID **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param host_id: The host_id of this UpdatePremiumHostAccessStatusRequest.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def body(self):
        r"""Gets the body of this UpdatePremiumHostAccessStatusRequest.

        :return: The body of this UpdatePremiumHostAccessStatusRequest.
        :rtype: :class:`huaweicloudsdkwaf.v1.UpdatePremiumHostAccessStatusRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdatePremiumHostAccessStatusRequest.

        :param body: The body of this UpdatePremiumHostAccessStatusRequest.
        :type body: :class:`huaweicloudsdkwaf.v1.UpdatePremiumHostAccessStatusRequestBody`
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
        if not isinstance(other, UpdatePremiumHostAccessStatusRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
