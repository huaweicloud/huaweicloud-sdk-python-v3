# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateRuleRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ruleid': 'str',
        'body': 'UpdateRuleRequestBody'
    }

    attribute_map = {
        'ruleid': 'ruleid',
        'body': 'body'
    }

    def __init__(self, ruleid=None, body=None):
        r"""UpdateRuleRequest

        The model defined in huaweicloud sdk

        :param ruleid: 权限策略id
        :type ruleid: str
        :param body: Body of the UpdateRuleRequest
        :type body: :class:`huaweicloudsdkucs.v1.UpdateRuleRequestBody`
        """
        
        

        self._ruleid = None
        self._body = None
        self.discriminator = None

        self.ruleid = ruleid
        if body is not None:
            self.body = body

    @property
    def ruleid(self):
        r"""Gets the ruleid of this UpdateRuleRequest.

        权限策略id

        :return: The ruleid of this UpdateRuleRequest.
        :rtype: str
        """
        return self._ruleid

    @ruleid.setter
    def ruleid(self, ruleid):
        r"""Sets the ruleid of this UpdateRuleRequest.

        权限策略id

        :param ruleid: The ruleid of this UpdateRuleRequest.
        :type ruleid: str
        """
        self._ruleid = ruleid

    @property
    def body(self):
        r"""Gets the body of this UpdateRuleRequest.

        :return: The body of this UpdateRuleRequest.
        :rtype: :class:`huaweicloudsdkucs.v1.UpdateRuleRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateRuleRequest.

        :param body: The body of this UpdateRuleRequest.
        :type body: :class:`huaweicloudsdkucs.v1.UpdateRuleRequestBody`
        """
        self._body = body

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UpdateRuleRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
