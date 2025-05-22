# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSyncRecordsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'sync_records': 'list[IdentitySourceSyncRecordVo]'
    }

    attribute_map = {
        'count': 'count',
        'sync_records': 'sync_records'
    }

    def __init__(self, count=None, sync_records=None):
        r"""ListSyncRecordsResponse

        The model defined in huaweicloud sdk

        :param count: **参数解释**： 同步记录条数。 **取值范围**： 大于等于0的整数。
        :type count: int
        :param sync_records: **参数解释**： 同步记录详细信息。 **取值范围**： 不涉及。
        :type sync_records: list[:class:`huaweicloudsdkdws.v2.IdentitySourceSyncRecordVo`]
        """
        
        super(ListSyncRecordsResponse, self).__init__()

        self._count = None
        self._sync_records = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if sync_records is not None:
            self.sync_records = sync_records

    @property
    def count(self):
        r"""Gets the count of this ListSyncRecordsResponse.

        **参数解释**： 同步记录条数。 **取值范围**： 大于等于0的整数。

        :return: The count of this ListSyncRecordsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListSyncRecordsResponse.

        **参数解释**： 同步记录条数。 **取值范围**： 大于等于0的整数。

        :param count: The count of this ListSyncRecordsResponse.
        :type count: int
        """
        self._count = count

    @property
    def sync_records(self):
        r"""Gets the sync_records of this ListSyncRecordsResponse.

        **参数解释**： 同步记录详细信息。 **取值范围**： 不涉及。

        :return: The sync_records of this ListSyncRecordsResponse.
        :rtype: list[:class:`huaweicloudsdkdws.v2.IdentitySourceSyncRecordVo`]
        """
        return self._sync_records

    @sync_records.setter
    def sync_records(self, sync_records):
        r"""Sets the sync_records of this ListSyncRecordsResponse.

        **参数解释**： 同步记录详细信息。 **取值范围**： 不涉及。

        :param sync_records: The sync_records of this ListSyncRecordsResponse.
        :type sync_records: list[:class:`huaweicloudsdkdws.v2.IdentitySourceSyncRecordVo`]
        """
        self._sync_records = sync_records

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
        if not isinstance(other, ListSyncRecordsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
