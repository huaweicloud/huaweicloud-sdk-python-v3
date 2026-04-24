# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetResourceApiKeyRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []
    sensitive_list.append('workload_access_token')

    openapi_types = {
        'resource_credential_provider_name': 'str',
        'workload_access_token': 'str'
    }

    attribute_map = {
        'resource_credential_provider_name': 'resource_credential_provider_name',
        'workload_access_token': 'workload_access_token'
    }

    def __init__(self, resource_credential_provider_name=None, workload_access_token=None):
        r"""GetResourceApiKeyRequestBody

        The model defined in huaweicloud sdk

        :param resource_credential_provider_name: Name of the resource credential provider to retrieve API key from
        :type resource_credential_provider_name: str
        :param workload_access_token: Identity token of the workload requesting the API key
        :type workload_access_token: str
        """
        
        

        self._resource_credential_provider_name = None
        self._workload_access_token = None
        self.discriminator = None

        self.resource_credential_provider_name = resource_credential_provider_name
        if workload_access_token is not None:
            self.workload_access_token = workload_access_token

    @property
    def resource_credential_provider_name(self):
        r"""Gets the resource_credential_provider_name of this GetResourceApiKeyRequestBody.

        Name of the resource credential provider to retrieve API key from

        :return: The resource_credential_provider_name of this GetResourceApiKeyRequestBody.
        :rtype: str
        """
        return self._resource_credential_provider_name

    @resource_credential_provider_name.setter
    def resource_credential_provider_name(self, resource_credential_provider_name):
        r"""Sets the resource_credential_provider_name of this GetResourceApiKeyRequestBody.

        Name of the resource credential provider to retrieve API key from

        :param resource_credential_provider_name: The resource_credential_provider_name of this GetResourceApiKeyRequestBody.
        :type resource_credential_provider_name: str
        """
        self._resource_credential_provider_name = resource_credential_provider_name

    @property
    def workload_access_token(self):
        r"""Gets the workload_access_token of this GetResourceApiKeyRequestBody.

        Identity token of the workload requesting the API key

        :return: The workload_access_token of this GetResourceApiKeyRequestBody.
        :rtype: str
        """
        return self._workload_access_token

    @workload_access_token.setter
    def workload_access_token(self, workload_access_token):
        r"""Sets the workload_access_token of this GetResourceApiKeyRequestBody.

        Identity token of the workload requesting the API key

        :param workload_access_token: The workload_access_token of this GetResourceApiKeyRequestBody.
        :type workload_access_token: str
        """
        self._workload_access_token = workload_access_token

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
        if not isinstance(other, GetResourceApiKeyRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
