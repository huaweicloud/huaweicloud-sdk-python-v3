# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListOpRecordResponse(SdkResponse):

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
        'operation_records': 'list[RecordDetailInfo]'
    }

    attribute_map = {
        'count': 'count',
        'operation_records': 'operation_records'
    }

    def __init__(self, count=None, operation_records=None):
        """ListOpRecordResponse

        The model defined in huaweicloud sdk

        :param count: 操作记录总数
        :type count: int
        :param operation_records: 操作记录列表
        :type operation_records: list[:class:`huaweicloudsdkbcs.v2.RecordDetailInfo`]
        """
        
        super(ListOpRecordResponse, self).__init__()

        self._count = None
        self._operation_records = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if operation_records is not None:
            self.operation_records = operation_records

    @property
    def count(self):
        """Gets the count of this ListOpRecordResponse.

        操作记录总数

        :return: The count of this ListOpRecordResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListOpRecordResponse.

        操作记录总数

        :param count: The count of this ListOpRecordResponse.
        :type count: int
        """
        self._count = count

    @property
    def operation_records(self):
        """Gets the operation_records of this ListOpRecordResponse.

        操作记录列表

        :return: The operation_records of this ListOpRecordResponse.
        :rtype: list[:class:`huaweicloudsdkbcs.v2.RecordDetailInfo`]
        """
        return self._operation_records

    @operation_records.setter
    def operation_records(self, operation_records):
        """Sets the operation_records of this ListOpRecordResponse.

        操作记录列表

        :param operation_records: The operation_records of this ListOpRecordResponse.
        :type operation_records: list[:class:`huaweicloudsdkbcs.v2.RecordDetailInfo`]
        """
        self._operation_records = operation_records

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
        if not isinstance(other, ListOpRecordResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
