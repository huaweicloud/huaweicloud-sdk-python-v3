# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdatePolicyDefinationRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'policydefinitionid': 'str',
        'body': 'UCSConstraintTemplateTagRequest'
    }

    attribute_map = {
        'policydefinitionid': 'policydefinitionid',
        'body': 'body'
    }

    def __init__(self, policydefinitionid=None, body=None):
        r"""UpdatePolicyDefinationRequest

        The model defined in huaweicloud sdk

        :param policydefinitionid: 策略定义id
        :type policydefinitionid: str
        :param body: Body of the UpdatePolicyDefinationRequest
        :type body: :class:`huaweicloudsdkucs.v1.UCSConstraintTemplateTagRequest`
        """
        
        

        self._policydefinitionid = None
        self._body = None
        self.discriminator = None

        self.policydefinitionid = policydefinitionid
        if body is not None:
            self.body = body

    @property
    def policydefinitionid(self):
        r"""Gets the policydefinitionid of this UpdatePolicyDefinationRequest.

        策略定义id

        :return: The policydefinitionid of this UpdatePolicyDefinationRequest.
        :rtype: str
        """
        return self._policydefinitionid

    @policydefinitionid.setter
    def policydefinitionid(self, policydefinitionid):
        r"""Sets the policydefinitionid of this UpdatePolicyDefinationRequest.

        策略定义id

        :param policydefinitionid: The policydefinitionid of this UpdatePolicyDefinationRequest.
        :type policydefinitionid: str
        """
        self._policydefinitionid = policydefinitionid

    @property
    def body(self):
        r"""Gets the body of this UpdatePolicyDefinationRequest.

        :return: The body of this UpdatePolicyDefinationRequest.
        :rtype: :class:`huaweicloudsdkucs.v1.UCSConstraintTemplateTagRequest`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdatePolicyDefinationRequest.

        :param body: The body of this UpdatePolicyDefinationRequest.
        :type body: :class:`huaweicloudsdkucs.v1.UCSConstraintTemplateTagRequest`
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
        if not isinstance(other, UpdatePolicyDefinationRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
