# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddonCheckRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'kind': 'str',
        'api_version': 'str',
        'spec': 'AddonCheckSpec'
    }

    attribute_map = {
        'kind': 'kind',
        'api_version': 'apiVersion',
        'spec': 'spec'
    }

    def __init__(self, kind=None, api_version=None, spec=None):
        r"""AddonCheckRequest

        The model defined in huaweicloud sdk

        :param kind: **参数解释：** API类型 **约束限制：** 该值不可修改 **取值范围：** 固定值\&quot;AddonCheck\&quot; **默认取值：** AddonCheck 
        :type kind: str
        :param api_version: **参数解释：** API版本 **约束限制：** 该值不可修改 **取值范围：** 固定值\&quot;v3\&quot; **默认取值：** v3 
        :type api_version: str
        :param spec: 
        :type spec: :class:`huaweicloudsdkcce.v3.AddonCheckSpec`
        """
        
        

        self._kind = None
        self._api_version = None
        self._spec = None
        self.discriminator = None

        self.kind = kind
        self.api_version = api_version
        self.spec = spec

    @property
    def kind(self):
        r"""Gets the kind of this AddonCheckRequest.

        **参数解释：** API类型 **约束限制：** 该值不可修改 **取值范围：** 固定值\"AddonCheck\" **默认取值：** AddonCheck 

        :return: The kind of this AddonCheckRequest.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        r"""Sets the kind of this AddonCheckRequest.

        **参数解释：** API类型 **约束限制：** 该值不可修改 **取值范围：** 固定值\"AddonCheck\" **默认取值：** AddonCheck 

        :param kind: The kind of this AddonCheckRequest.
        :type kind: str
        """
        self._kind = kind

    @property
    def api_version(self):
        r"""Gets the api_version of this AddonCheckRequest.

        **参数解释：** API版本 **约束限制：** 该值不可修改 **取值范围：** 固定值\"v3\" **默认取值：** v3 

        :return: The api_version of this AddonCheckRequest.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        r"""Sets the api_version of this AddonCheckRequest.

        **参数解释：** API版本 **约束限制：** 该值不可修改 **取值范围：** 固定值\"v3\" **默认取值：** v3 

        :param api_version: The api_version of this AddonCheckRequest.
        :type api_version: str
        """
        self._api_version = api_version

    @property
    def spec(self):
        r"""Gets the spec of this AddonCheckRequest.

        :return: The spec of this AddonCheckRequest.
        :rtype: :class:`huaweicloudsdkcce.v3.AddonCheckSpec`
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        r"""Sets the spec of this AddonCheckRequest.

        :param spec: The spec of this AddonCheckRequest.
        :type spec: :class:`huaweicloudsdkcce.v3.AddonCheckSpec`
        """
        self._spec = spec

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
        if not isinstance(other, AddonCheckRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
