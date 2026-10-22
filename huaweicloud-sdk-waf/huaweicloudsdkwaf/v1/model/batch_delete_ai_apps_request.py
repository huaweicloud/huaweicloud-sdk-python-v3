# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchDeleteAiAppsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'keep_policy': 'bool',
        'body': 'BatchDeleteRequest'
    }

    attribute_map = {
        'keep_policy': 'keep_policy',
        'body': 'body'
    }

    def __init__(self, keep_policy=None, body=None):
        r"""BatchDeleteAiAppsRequest

        The model defined in huaweicloud sdk

        :param keep_policy: **参数解释：** 是否保留关联的策略 **约束限制：** 不涉及 **取值范围：** true, false **默认取值：** 不涉及
        :type keep_policy: bool
        :param body: Body of the BatchDeleteAiAppsRequest
        :type body: :class:`huaweicloudsdkwaf.v1.BatchDeleteRequest`
        """
        
        

        self._keep_policy = None
        self._body = None
        self.discriminator = None

        self.keep_policy = keep_policy
        if body is not None:
            self.body = body

    @property
    def keep_policy(self):
        r"""Gets the keep_policy of this BatchDeleteAiAppsRequest.

        **参数解释：** 是否保留关联的策略 **约束限制：** 不涉及 **取值范围：** true, false **默认取值：** 不涉及

        :return: The keep_policy of this BatchDeleteAiAppsRequest.
        :rtype: bool
        """
        return self._keep_policy

    @keep_policy.setter
    def keep_policy(self, keep_policy):
        r"""Sets the keep_policy of this BatchDeleteAiAppsRequest.

        **参数解释：** 是否保留关联的策略 **约束限制：** 不涉及 **取值范围：** true, false **默认取值：** 不涉及

        :param keep_policy: The keep_policy of this BatchDeleteAiAppsRequest.
        :type keep_policy: bool
        """
        self._keep_policy = keep_policy

    @property
    def body(self):
        r"""Gets the body of this BatchDeleteAiAppsRequest.

        :return: The body of this BatchDeleteAiAppsRequest.
        :rtype: :class:`huaweicloudsdkwaf.v1.BatchDeleteRequest`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this BatchDeleteAiAppsRequest.

        :param body: The body of this BatchDeleteAiAppsRequest.
        :type body: :class:`huaweicloudsdkwaf.v1.BatchDeleteRequest`
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
        if not isinstance(other, BatchDeleteAiAppsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
