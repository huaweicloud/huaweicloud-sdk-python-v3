# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPolicyEnginesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'policy_engines': 'list[PolicyEngineSummary]',
        'page_info': 'PageInfo'
    }

    attribute_map = {
        'policy_engines': 'policy_engines',
        'page_info': 'page_info'
    }

    def __init__(self, policy_engines=None, page_info=None):
        r"""ListPolicyEnginesResponse

        The model defined in huaweicloud sdk

        :param policy_engines: 
        :type policy_engines: list[:class:`huaweicloudsdkagentidentity.v1.PolicyEngineSummary`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkagentidentity.v1.PageInfo`
        """
        
        super().__init__()

        self._policy_engines = None
        self._page_info = None
        self.discriminator = None

        if policy_engines is not None:
            self.policy_engines = policy_engines
        if page_info is not None:
            self.page_info = page_info

    @property
    def policy_engines(self):
        r"""Gets the policy_engines of this ListPolicyEnginesResponse.

        :return: The policy_engines of this ListPolicyEnginesResponse.
        :rtype: list[:class:`huaweicloudsdkagentidentity.v1.PolicyEngineSummary`]
        """
        return self._policy_engines

    @policy_engines.setter
    def policy_engines(self, policy_engines):
        r"""Sets the policy_engines of this ListPolicyEnginesResponse.

        :param policy_engines: The policy_engines of this ListPolicyEnginesResponse.
        :type policy_engines: list[:class:`huaweicloudsdkagentidentity.v1.PolicyEngineSummary`]
        """
        self._policy_engines = policy_engines

    @property
    def page_info(self):
        r"""Gets the page_info of this ListPolicyEnginesResponse.

        :return: The page_info of this ListPolicyEnginesResponse.
        :rtype: :class:`huaweicloudsdkagentidentity.v1.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this ListPolicyEnginesResponse.

        :param page_info: The page_info of this ListPolicyEnginesResponse.
        :type page_info: :class:`huaweicloudsdkagentidentity.v1.PageInfo`
        """
        self._page_info = page_info

    def to_dict(self):
        import warnings
        warnings.warn("ListPolicyEnginesResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListPolicyEnginesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
