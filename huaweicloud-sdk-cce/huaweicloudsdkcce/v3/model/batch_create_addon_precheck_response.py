# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchCreateAddonPrecheckResponse(SdkResponse):

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
        'spec': 'AddonCheckSpec',
        'status': 'AddonCheckStatus'
    }

    attribute_map = {
        'kind': 'kind',
        'api_version': 'apiVersion',
        'spec': 'spec',
        'status': 'status'
    }

    def __init__(self, kind=None, api_version=None, spec=None, status=None):
        r"""BatchCreateAddonPrecheckResponse

        The model defined in huaweicloud sdk

        :param kind: **参数解释：** API类型 **约束限制：** 该值不可修改 **取值范围：** 固定值\&quot;AddonCheck\&quot; **默认取值：** AddonCheck 
        :type kind: str
        :param api_version: **参数解释：** API版本 **约束限制：** 该值不可修改 **取值范围：** 固定值\&quot;v3\&quot; **默认取值：** v3 
        :type api_version: str
        :param spec: 
        :type spec: :class:`huaweicloudsdkcce.v3.AddonCheckSpec`
        :param status: 
        :type status: :class:`huaweicloudsdkcce.v3.AddonCheckStatus`
        """
        
        super().__init__()

        self._kind = None
        self._api_version = None
        self._spec = None
        self._status = None
        self.discriminator = None

        if kind is not None:
            self.kind = kind
        if api_version is not None:
            self.api_version = api_version
        if spec is not None:
            self.spec = spec
        if status is not None:
            self.status = status

    @property
    def kind(self):
        r"""Gets the kind of this BatchCreateAddonPrecheckResponse.

        **参数解释：** API类型 **约束限制：** 该值不可修改 **取值范围：** 固定值\"AddonCheck\" **默认取值：** AddonCheck 

        :return: The kind of this BatchCreateAddonPrecheckResponse.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        r"""Sets the kind of this BatchCreateAddonPrecheckResponse.

        **参数解释：** API类型 **约束限制：** 该值不可修改 **取值范围：** 固定值\"AddonCheck\" **默认取值：** AddonCheck 

        :param kind: The kind of this BatchCreateAddonPrecheckResponse.
        :type kind: str
        """
        self._kind = kind

    @property
    def api_version(self):
        r"""Gets the api_version of this BatchCreateAddonPrecheckResponse.

        **参数解释：** API版本 **约束限制：** 该值不可修改 **取值范围：** 固定值\"v3\" **默认取值：** v3 

        :return: The api_version of this BatchCreateAddonPrecheckResponse.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        r"""Sets the api_version of this BatchCreateAddonPrecheckResponse.

        **参数解释：** API版本 **约束限制：** 该值不可修改 **取值范围：** 固定值\"v3\" **默认取值：** v3 

        :param api_version: The api_version of this BatchCreateAddonPrecheckResponse.
        :type api_version: str
        """
        self._api_version = api_version

    @property
    def spec(self):
        r"""Gets the spec of this BatchCreateAddonPrecheckResponse.

        :return: The spec of this BatchCreateAddonPrecheckResponse.
        :rtype: :class:`huaweicloudsdkcce.v3.AddonCheckSpec`
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        r"""Sets the spec of this BatchCreateAddonPrecheckResponse.

        :param spec: The spec of this BatchCreateAddonPrecheckResponse.
        :type spec: :class:`huaweicloudsdkcce.v3.AddonCheckSpec`
        """
        self._spec = spec

    @property
    def status(self):
        r"""Gets the status of this BatchCreateAddonPrecheckResponse.

        :return: The status of this BatchCreateAddonPrecheckResponse.
        :rtype: :class:`huaweicloudsdkcce.v3.AddonCheckStatus`
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this BatchCreateAddonPrecheckResponse.

        :param status: The status of this BatchCreateAddonPrecheckResponse.
        :type status: :class:`huaweicloudsdkcce.v3.AddonCheckStatus`
        """
        self._status = status

    def to_dict(self):
        import warnings
        warnings.warn("BatchCreateAddonPrecheckResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, BatchCreateAddonPrecheckResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
