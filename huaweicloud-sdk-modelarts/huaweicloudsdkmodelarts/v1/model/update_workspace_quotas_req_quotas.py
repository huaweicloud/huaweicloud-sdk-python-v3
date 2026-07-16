# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateWorkspaceQuotasReqQuotas:

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
        'quota': 'int'
    }

    attribute_map = {
        'resource': 'resource',
        'quota': 'quota'
    }

    def __init__(self, resource=None, quota=None):
        r"""UpdateWorkspaceQuotasReqQuotas

        The model defined in huaweicloud sdk

        :param resource: 资源标识。
        :type resource: str
        :param quota: 要修改的配额值。配额值为正整数或-1，-1代表不限制配额。配额值范围不能超过配额的最大值与最小值。可通过调用查询工作空间配额接口查询配额的最大值。
        :type quota: int
        """
        
        

        self._resource = None
        self._quota = None
        self.discriminator = None

        self.resource = resource
        self.quota = quota

    @property
    def resource(self):
        r"""Gets the resource of this UpdateWorkspaceQuotasReqQuotas.

        资源标识。

        :return: The resource of this UpdateWorkspaceQuotasReqQuotas.
        :rtype: str
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        r"""Sets the resource of this UpdateWorkspaceQuotasReqQuotas.

        资源标识。

        :param resource: The resource of this UpdateWorkspaceQuotasReqQuotas.
        :type resource: str
        """
        self._resource = resource

    @property
    def quota(self):
        r"""Gets the quota of this UpdateWorkspaceQuotasReqQuotas.

        要修改的配额值。配额值为正整数或-1，-1代表不限制配额。配额值范围不能超过配额的最大值与最小值。可通过调用查询工作空间配额接口查询配额的最大值。

        :return: The quota of this UpdateWorkspaceQuotasReqQuotas.
        :rtype: int
        """
        return self._quota

    @quota.setter
    def quota(self, quota):
        r"""Sets the quota of this UpdateWorkspaceQuotasReqQuotas.

        要修改的配额值。配额值为正整数或-1，-1代表不限制配额。配额值范围不能超过配额的最大值与最小值。可通过调用查询工作空间配额接口查询配额的最大值。

        :param quota: The quota of this UpdateWorkspaceQuotasReqQuotas.
        :type quota: int
        """
        self._quota = quota

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
        if not isinstance(other, UpdateWorkspaceQuotasReqQuotas):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
