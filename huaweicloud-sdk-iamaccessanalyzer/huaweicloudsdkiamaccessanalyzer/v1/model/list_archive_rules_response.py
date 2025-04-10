# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListArchiveRulesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'archive_rules': 'list[ArchiveRuleSummary]',
        'page_info': 'PageInfo'
    }

    attribute_map = {
        'archive_rules': 'archive_rules',
        'page_info': 'page_info'
    }

    def __init__(self, archive_rules=None, page_info=None):
        r"""ListArchiveRulesResponse

        The model defined in huaweicloud sdk

        :param archive_rules: 为指定分析器创建的存档规则的列表。
        :type archive_rules: list[:class:`huaweicloudsdkiamaccessanalyzer.v1.ArchiveRuleSummary`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkiamaccessanalyzer.v1.PageInfo`
        """
        
        super(ListArchiveRulesResponse, self).__init__()

        self._archive_rules = None
        self._page_info = None
        self.discriminator = None

        if archive_rules is not None:
            self.archive_rules = archive_rules
        if page_info is not None:
            self.page_info = page_info

    @property
    def archive_rules(self):
        r"""Gets the archive_rules of this ListArchiveRulesResponse.

        为指定分析器创建的存档规则的列表。

        :return: The archive_rules of this ListArchiveRulesResponse.
        :rtype: list[:class:`huaweicloudsdkiamaccessanalyzer.v1.ArchiveRuleSummary`]
        """
        return self._archive_rules

    @archive_rules.setter
    def archive_rules(self, archive_rules):
        r"""Sets the archive_rules of this ListArchiveRulesResponse.

        为指定分析器创建的存档规则的列表。

        :param archive_rules: The archive_rules of this ListArchiveRulesResponse.
        :type archive_rules: list[:class:`huaweicloudsdkiamaccessanalyzer.v1.ArchiveRuleSummary`]
        """
        self._archive_rules = archive_rules

    @property
    def page_info(self):
        r"""Gets the page_info of this ListArchiveRulesResponse.

        :return: The page_info of this ListArchiveRulesResponse.
        :rtype: :class:`huaweicloudsdkiamaccessanalyzer.v1.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this ListArchiveRulesResponse.

        :param page_info: The page_info of this ListArchiveRulesResponse.
        :type page_info: :class:`huaweicloudsdkiamaccessanalyzer.v1.PageInfo`
        """
        self._page_info = page_info

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListArchiveRulesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
