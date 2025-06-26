# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListConfigurationsAuditRecordsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'records': 'list[ConfigurationRecordResp]',
        'count': 'int'
    }

    attribute_map = {
        'records': 'records',
        'count': 'count'
    }

    def __init__(self, records=None, count=None):
        r"""ListConfigurationsAuditRecordsResponse

        The model defined in huaweicloud sdk

        :param records: **参数解释**： 记录。 **取值范围**： 不涉及。
        :type records: list[:class:`huaweicloudsdkdws.v2.ConfigurationRecordResp`]
        :param count: **参数解释**： 总数。 **取值范围**： 不涉及。
        :type count: int
        """
        
        super(ListConfigurationsAuditRecordsResponse, self).__init__()

        self._records = None
        self._count = None
        self.discriminator = None

        if records is not None:
            self.records = records
        if count is not None:
            self.count = count

    @property
    def records(self):
        r"""Gets the records of this ListConfigurationsAuditRecordsResponse.

        **参数解释**： 记录。 **取值范围**： 不涉及。

        :return: The records of this ListConfigurationsAuditRecordsResponse.
        :rtype: list[:class:`huaweicloudsdkdws.v2.ConfigurationRecordResp`]
        """
        return self._records

    @records.setter
    def records(self, records):
        r"""Sets the records of this ListConfigurationsAuditRecordsResponse.

        **参数解释**： 记录。 **取值范围**： 不涉及。

        :param records: The records of this ListConfigurationsAuditRecordsResponse.
        :type records: list[:class:`huaweicloudsdkdws.v2.ConfigurationRecordResp`]
        """
        self._records = records

    @property
    def count(self):
        r"""Gets the count of this ListConfigurationsAuditRecordsResponse.

        **参数解释**： 总数。 **取值范围**： 不涉及。

        :return: The count of this ListConfigurationsAuditRecordsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListConfigurationsAuditRecordsResponse.

        **参数解释**： 总数。 **取值范围**： 不涉及。

        :param count: The count of this ListConfigurationsAuditRecordsResponse.
        :type count: int
        """
        self._count = count

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
        if not isinstance(other, ListConfigurationsAuditRecordsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
