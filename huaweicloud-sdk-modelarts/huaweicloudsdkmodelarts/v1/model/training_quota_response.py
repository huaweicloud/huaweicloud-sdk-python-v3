# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TrainingQuotaResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource': 'str',
        'quota': 'int',
        'used': 'int'
    }

    attribute_map = {
        'resource': 'resource',
        'quota': 'quota',
        'used': 'used'
    }

    def __init__(self, resource=None, quota=None, used=None):
        r"""TrainingQuotaResponse

        The model defined in huaweicloud sdk

        :param resource: **参数解释**：配额的资源类型，当前支持：job-num，作业的个数配额。 **取值范围**：不涉及。
        :type resource: str
        :param quota: **参数解释**：配额个数。 **取值范围**：不涉及。
        :type quota: int
        :param used: **参数解释**：已使用的个数。 **取值范围**：不涉及。
        :type used: int
        """
        
        

        self._resource = None
        self._quota = None
        self._used = None
        self.discriminator = None

        if resource is not None:
            self.resource = resource
        if quota is not None:
            self.quota = quota
        if used is not None:
            self.used = used

    @property
    def resource(self):
        r"""Gets the resource of this TrainingQuotaResponse.

        **参数解释**：配额的资源类型，当前支持：job-num，作业的个数配额。 **取值范围**：不涉及。

        :return: The resource of this TrainingQuotaResponse.
        :rtype: str
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        r"""Sets the resource of this TrainingQuotaResponse.

        **参数解释**：配额的资源类型，当前支持：job-num，作业的个数配额。 **取值范围**：不涉及。

        :param resource: The resource of this TrainingQuotaResponse.
        :type resource: str
        """
        self._resource = resource

    @property
    def quota(self):
        r"""Gets the quota of this TrainingQuotaResponse.

        **参数解释**：配额个数。 **取值范围**：不涉及。

        :return: The quota of this TrainingQuotaResponse.
        :rtype: int
        """
        return self._quota

    @quota.setter
    def quota(self, quota):
        r"""Sets the quota of this TrainingQuotaResponse.

        **参数解释**：配额个数。 **取值范围**：不涉及。

        :param quota: The quota of this TrainingQuotaResponse.
        :type quota: int
        """
        self._quota = quota

    @property
    def used(self):
        r"""Gets the used of this TrainingQuotaResponse.

        **参数解释**：已使用的个数。 **取值范围**：不涉及。

        :return: The used of this TrainingQuotaResponse.
        :rtype: int
        """
        return self._used

    @used.setter
    def used(self, used):
        r"""Sets the used of this TrainingQuotaResponse.

        **参数解释**：已使用的个数。 **取值范围**：不涉及。

        :param used: The used of this TrainingQuotaResponse.
        :type used: int
        """
        self._used = used

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
        if not isinstance(other, TrainingQuotaResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
