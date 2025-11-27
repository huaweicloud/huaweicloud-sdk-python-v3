# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdatePremiumInstanceProgressRequest:

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
        'body': 'AccessProgress'
    }

    attribute_map = {
        'host_id': 'host_id',
        'body': 'body'
    }

    def __init__(self, host_id=None, body=None):
        r"""UpdatePremiumInstanceProgressRequest

        The model defined in huaweicloud sdk

        :param host_id: **参数解释：** 独享模式域名Id，通过 查询独享模式域名列表(ListPremiumHost) 接口获取 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type host_id: str
        :param body: Body of the UpdatePremiumInstanceProgressRequest
        :type body: :class:`huaweicloudsdkwaf.v1.AccessProgress`
        """
        
        

        self._host_id = None
        self._body = None
        self.discriminator = None

        self.host_id = host_id
        if body is not None:
            self.body = body

    @property
    def host_id(self):
        r"""Gets the host_id of this UpdatePremiumInstanceProgressRequest.

        **参数解释：** 独享模式域名Id，通过 查询独享模式域名列表(ListPremiumHost) 接口获取 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The host_id of this UpdatePremiumInstanceProgressRequest.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this UpdatePremiumInstanceProgressRequest.

        **参数解释：** 独享模式域名Id，通过 查询独享模式域名列表(ListPremiumHost) 接口获取 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param host_id: The host_id of this UpdatePremiumInstanceProgressRequest.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def body(self):
        r"""Gets the body of this UpdatePremiumInstanceProgressRequest.

        :return: The body of this UpdatePremiumInstanceProgressRequest.
        :rtype: :class:`huaweicloudsdkwaf.v1.AccessProgress`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdatePremiumInstanceProgressRequest.

        :param body: The body of this UpdatePremiumInstanceProgressRequest.
        :type body: :class:`huaweicloudsdkwaf.v1.AccessProgress`
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
        if not isinstance(other, UpdatePremiumInstanceProgressRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
