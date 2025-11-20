# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UnusedAnalysisRuleCriteria:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'account_ids': 'list[str]',
        'resource_tags': 'list[Tag]'
    }

    attribute_map = {
        'account_ids': 'account_ids',
        'resource_tags': 'resource_tags'
    }

    def __init__(self, account_ids=None, resource_tags=None):
        r"""UnusedAnalysisRuleCriteria

        The model defined in huaweicloud sdk

        :param account_ids: 账号ID列表。
        :type account_ids: list[str]
        :param resource_tags: 资源标签列表。
        :type resource_tags: list[:class:`huaweicloudsdkiamaccessanalyzer.v1.Tag`]
        """
        
        

        self._account_ids = None
        self._resource_tags = None
        self.discriminator = None

        if account_ids is not None:
            self.account_ids = account_ids
        if resource_tags is not None:
            self.resource_tags = resource_tags

    @property
    def account_ids(self):
        r"""Gets the account_ids of this UnusedAnalysisRuleCriteria.

        账号ID列表。

        :return: The account_ids of this UnusedAnalysisRuleCriteria.
        :rtype: list[str]
        """
        return self._account_ids

    @account_ids.setter
    def account_ids(self, account_ids):
        r"""Sets the account_ids of this UnusedAnalysisRuleCriteria.

        账号ID列表。

        :param account_ids: The account_ids of this UnusedAnalysisRuleCriteria.
        :type account_ids: list[str]
        """
        self._account_ids = account_ids

    @property
    def resource_tags(self):
        r"""Gets the resource_tags of this UnusedAnalysisRuleCriteria.

        资源标签列表。

        :return: The resource_tags of this UnusedAnalysisRuleCriteria.
        :rtype: list[:class:`huaweicloudsdkiamaccessanalyzer.v1.Tag`]
        """
        return self._resource_tags

    @resource_tags.setter
    def resource_tags(self, resource_tags):
        r"""Sets the resource_tags of this UnusedAnalysisRuleCriteria.

        资源标签列表。

        :param resource_tags: The resource_tags of this UnusedAnalysisRuleCriteria.
        :type resource_tags: list[:class:`huaweicloudsdkiamaccessanalyzer.v1.Tag`]
        """
        self._resource_tags = resource_tags

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
        if not isinstance(other, UnusedAnalysisRuleCriteria):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
