# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CancelAuraDataframeJobResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'status': 'str',
        'x_request_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'status': 'status',
        'x_request_id': 'X-request-id'
    }

    def __init__(self, id=None, status=None, x_request_id=None):
        r"""CancelAuraDataframeJobResponse

        The model defined in huaweicloud sdk

        :param id: **参数解释**：作业ID。 **约束限制**：不涉及。 **取值范围**：长度为1~128的任意字符组合。 **默认取值**：不涉及。
        :type id: str
        :param status: **参数解释**：作业状态。 **约束限制**：不涉及。 **取值范围**：长度为1~128的任意字符组合。 **默认取值**：不涉及。
        :type status: str
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super().__init__()

        self._id = None
        self._status = None
        self._x_request_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if status is not None:
            self.status = status
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def id(self):
        r"""Gets the id of this CancelAuraDataframeJobResponse.

        **参数解释**：作业ID。 **约束限制**：不涉及。 **取值范围**：长度为1~128的任意字符组合。 **默认取值**：不涉及。

        :return: The id of this CancelAuraDataframeJobResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CancelAuraDataframeJobResponse.

        **参数解释**：作业ID。 **约束限制**：不涉及。 **取值范围**：长度为1~128的任意字符组合。 **默认取值**：不涉及。

        :param id: The id of this CancelAuraDataframeJobResponse.
        :type id: str
        """
        self._id = id

    @property
    def status(self):
        r"""Gets the status of this CancelAuraDataframeJobResponse.

        **参数解释**：作业状态。 **约束限制**：不涉及。 **取值范围**：长度为1~128的任意字符组合。 **默认取值**：不涉及。

        :return: The status of this CancelAuraDataframeJobResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this CancelAuraDataframeJobResponse.

        **参数解释**：作业状态。 **约束限制**：不涉及。 **取值范围**：长度为1~128的任意字符组合。 **默认取值**：不涉及。

        :param status: The status of this CancelAuraDataframeJobResponse.
        :type status: str
        """
        self._status = status

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this CancelAuraDataframeJobResponse.

        :return: The x_request_id of this CancelAuraDataframeJobResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this CancelAuraDataframeJobResponse.

        :param x_request_id: The x_request_id of this CancelAuraDataframeJobResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

    def to_dict(self):
        import warnings
        warnings.warn("CancelAuraDataframeJobResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, CancelAuraDataframeJobResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
