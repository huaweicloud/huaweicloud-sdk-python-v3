# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAssociatedResourceRulesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'rules': 'list[AssociatedResourceRule]',
        'total_count': 'int',
        'page_info': 'PageInfo'
    }

    attribute_map = {
        'rules': 'rules',
        'total_count': 'total_count',
        'page_info': 'page_info'
    }

    def __init__(self, rules=None, total_count=None, page_info=None):
        r"""ListAssociatedResourceRulesResponse

        The model defined in huaweicloud sdk

        :param rules: 规则信息
        :type rules: list[:class:`huaweicloudsdktms.v1.AssociatedResourceRule`]
        :param total_count: 记录总数
        :type total_count: int
        :param page_info: 
        :type page_info: :class:`huaweicloudsdktms.v1.PageInfo`
        """
        
        super().__init__()

        self._rules = None
        self._total_count = None
        self._page_info = None
        self.discriminator = None

        if rules is not None:
            self.rules = rules
        if total_count is not None:
            self.total_count = total_count
        if page_info is not None:
            self.page_info = page_info

    @property
    def rules(self):
        r"""Gets the rules of this ListAssociatedResourceRulesResponse.

        规则信息

        :return: The rules of this ListAssociatedResourceRulesResponse.
        :rtype: list[:class:`huaweicloudsdktms.v1.AssociatedResourceRule`]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        r"""Sets the rules of this ListAssociatedResourceRulesResponse.

        规则信息

        :param rules: The rules of this ListAssociatedResourceRulesResponse.
        :type rules: list[:class:`huaweicloudsdktms.v1.AssociatedResourceRule`]
        """
        self._rules = rules

    @property
    def total_count(self):
        r"""Gets the total_count of this ListAssociatedResourceRulesResponse.

        记录总数

        :return: The total_count of this ListAssociatedResourceRulesResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ListAssociatedResourceRulesResponse.

        记录总数

        :param total_count: The total_count of this ListAssociatedResourceRulesResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def page_info(self):
        r"""Gets the page_info of this ListAssociatedResourceRulesResponse.

        :return: The page_info of this ListAssociatedResourceRulesResponse.
        :rtype: :class:`huaweicloudsdktms.v1.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this ListAssociatedResourceRulesResponse.

        :param page_info: The page_info of this ListAssociatedResourceRulesResponse.
        :type page_info: :class:`huaweicloudsdktms.v1.PageInfo`
        """
        self._page_info = page_info

    def to_dict(self):
        import warnings
        warnings.warn("ListAssociatedResourceRulesResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListAssociatedResourceRulesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
