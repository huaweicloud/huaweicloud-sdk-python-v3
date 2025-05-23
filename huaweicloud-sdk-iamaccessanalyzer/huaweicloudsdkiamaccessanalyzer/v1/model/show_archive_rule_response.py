# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowArchiveRuleResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'archive_rule': 'ArchiveRuleSummary'
    }

    attribute_map = {
        'archive_rule': 'archive_rule'
    }

    def __init__(self, archive_rule=None):
        r"""ShowArchiveRuleResponse

        The model defined in huaweicloud sdk

        :param archive_rule: 
        :type archive_rule: :class:`huaweicloudsdkiamaccessanalyzer.v1.ArchiveRuleSummary`
        """
        
        super(ShowArchiveRuleResponse, self).__init__()

        self._archive_rule = None
        self.discriminator = None

        if archive_rule is not None:
            self.archive_rule = archive_rule

    @property
    def archive_rule(self):
        r"""Gets the archive_rule of this ShowArchiveRuleResponse.

        :return: The archive_rule of this ShowArchiveRuleResponse.
        :rtype: :class:`huaweicloudsdkiamaccessanalyzer.v1.ArchiveRuleSummary`
        """
        return self._archive_rule

    @archive_rule.setter
    def archive_rule(self, archive_rule):
        r"""Sets the archive_rule of this ShowArchiveRuleResponse.

        :param archive_rule: The archive_rule of this ShowArchiveRuleResponse.
        :type archive_rule: :class:`huaweicloudsdkiamaccessanalyzer.v1.ArchiveRuleSummary`
        """
        self._archive_rule = archive_rule

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
        if not isinstance(other, ShowArchiveRuleResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
