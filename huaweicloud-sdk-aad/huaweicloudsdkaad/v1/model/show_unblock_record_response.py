# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowUnblockRecordResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'unblock_record': 'list[UnblockRecordResponseUnblockRecord]',
        'total': 'int',
        'domain_id': 'str'
    }

    attribute_map = {
        'unblock_record': 'unblock_record',
        'total': 'total',
        'domain_id': 'domain_id'
    }

    def __init__(self, unblock_record=None, total=None, domain_id=None):
        r"""ShowUnblockRecordResponse

        The model defined in huaweicloud sdk

        :param unblock_record: 解封记录
        :type unblock_record: list[:class:`huaweicloudsdkaad.v1.UnblockRecordResponseUnblockRecord`]
        :param total: 总数
        :type total: int
        :param domain_id: 租户id
        :type domain_id: str
        """
        
        super(ShowUnblockRecordResponse, self).__init__()

        self._unblock_record = None
        self._total = None
        self._domain_id = None
        self.discriminator = None

        if unblock_record is not None:
            self.unblock_record = unblock_record
        if total is not None:
            self.total = total
        if domain_id is not None:
            self.domain_id = domain_id

    @property
    def unblock_record(self):
        r"""Gets the unblock_record of this ShowUnblockRecordResponse.

        解封记录

        :return: The unblock_record of this ShowUnblockRecordResponse.
        :rtype: list[:class:`huaweicloudsdkaad.v1.UnblockRecordResponseUnblockRecord`]
        """
        return self._unblock_record

    @unblock_record.setter
    def unblock_record(self, unblock_record):
        r"""Sets the unblock_record of this ShowUnblockRecordResponse.

        解封记录

        :param unblock_record: The unblock_record of this ShowUnblockRecordResponse.
        :type unblock_record: list[:class:`huaweicloudsdkaad.v1.UnblockRecordResponseUnblockRecord`]
        """
        self._unblock_record = unblock_record

    @property
    def total(self):
        r"""Gets the total of this ShowUnblockRecordResponse.

        总数

        :return: The total of this ShowUnblockRecordResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ShowUnblockRecordResponse.

        总数

        :param total: The total of this ShowUnblockRecordResponse.
        :type total: int
        """
        self._total = total

    @property
    def domain_id(self):
        r"""Gets the domain_id of this ShowUnblockRecordResponse.

        租户id

        :return: The domain_id of this ShowUnblockRecordResponse.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this ShowUnblockRecordResponse.

        租户id

        :param domain_id: The domain_id of this ShowUnblockRecordResponse.
        :type domain_id: str
        """
        self._domain_id = domain_id

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
        if not isinstance(other, ShowUnblockRecordResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
