# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateWorkloadIdentityReqBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'allowed_resource_oauth2_return_urls': 'list[str]',
        'authorizer_configuration': 'AuthorizerConfiguration',
        'tags': 'list[Tag]'
    }

    attribute_map = {
        'allowed_resource_oauth2_return_urls': 'allowed_resource_oauth2_return_urls',
        'authorizer_configuration': 'authorizer_configuration',
        'tags': 'tags'
    }

    def __init__(self, allowed_resource_oauth2_return_urls=None, authorizer_configuration=None, tags=None):
        r"""UpdateWorkloadIdentityReqBody

        The model defined in huaweicloud sdk

        :param allowed_resource_oauth2_return_urls: 
        :type allowed_resource_oauth2_return_urls: list[str]
        :param authorizer_configuration: 
        :type authorizer_configuration: :class:`huaweicloudsdkagentidentity.v1.AuthorizerConfiguration`
        :param tags: 自定义标签列表。
        :type tags: list[:class:`huaweicloudsdkagentidentity.v1.Tag`]
        """
        
        

        self._allowed_resource_oauth2_return_urls = None
        self._authorizer_configuration = None
        self._tags = None
        self.discriminator = None

        if allowed_resource_oauth2_return_urls is not None:
            self.allowed_resource_oauth2_return_urls = allowed_resource_oauth2_return_urls
        if authorizer_configuration is not None:
            self.authorizer_configuration = authorizer_configuration
        if tags is not None:
            self.tags = tags

    @property
    def allowed_resource_oauth2_return_urls(self):
        r"""Gets the allowed_resource_oauth2_return_urls of this UpdateWorkloadIdentityReqBody.

        :return: The allowed_resource_oauth2_return_urls of this UpdateWorkloadIdentityReqBody.
        :rtype: list[str]
        """
        return self._allowed_resource_oauth2_return_urls

    @allowed_resource_oauth2_return_urls.setter
    def allowed_resource_oauth2_return_urls(self, allowed_resource_oauth2_return_urls):
        r"""Sets the allowed_resource_oauth2_return_urls of this UpdateWorkloadIdentityReqBody.

        :param allowed_resource_oauth2_return_urls: The allowed_resource_oauth2_return_urls of this UpdateWorkloadIdentityReqBody.
        :type allowed_resource_oauth2_return_urls: list[str]
        """
        self._allowed_resource_oauth2_return_urls = allowed_resource_oauth2_return_urls

    @property
    def authorizer_configuration(self):
        r"""Gets the authorizer_configuration of this UpdateWorkloadIdentityReqBody.

        :return: The authorizer_configuration of this UpdateWorkloadIdentityReqBody.
        :rtype: :class:`huaweicloudsdkagentidentity.v1.AuthorizerConfiguration`
        """
        return self._authorizer_configuration

    @authorizer_configuration.setter
    def authorizer_configuration(self, authorizer_configuration):
        r"""Sets the authorizer_configuration of this UpdateWorkloadIdentityReqBody.

        :param authorizer_configuration: The authorizer_configuration of this UpdateWorkloadIdentityReqBody.
        :type authorizer_configuration: :class:`huaweicloudsdkagentidentity.v1.AuthorizerConfiguration`
        """
        self._authorizer_configuration = authorizer_configuration

    @property
    def tags(self):
        r"""Gets the tags of this UpdateWorkloadIdentityReqBody.

        自定义标签列表。

        :return: The tags of this UpdateWorkloadIdentityReqBody.
        :rtype: list[:class:`huaweicloudsdkagentidentity.v1.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this UpdateWorkloadIdentityReqBody.

        自定义标签列表。

        :param tags: The tags of this UpdateWorkloadIdentityReqBody.
        :type tags: list[:class:`huaweicloudsdkagentidentity.v1.Tag`]
        """
        self._tags = tags

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
        if not isinstance(other, UpdateWorkloadIdentityReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
