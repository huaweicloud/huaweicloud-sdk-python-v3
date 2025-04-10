# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListWorkitemStatusRecordsV4Response(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'records': 'list[WorkitemStatusRecords]',
        'total': 'int'
    }

    attribute_map = {
        'records': 'records',
        'total': 'total'
    }

    def __init__(self, records=None, total=None):
        r"""ListWorkitemStatusRecordsV4Response

        The model defined in huaweicloud sdk

        :param records: 操作历史
        :type records: list[:class:`huaweicloudsdkprojectman.v4.WorkitemStatusRecords`]
        :param total: 总数
        :type total: int
        """
        
        super(ListWorkitemStatusRecordsV4Response, self).__init__()

        self._records = None
        self._total = None
        self.discriminator = None

        if records is not None:
            self.records = records
        if total is not None:
            self.total = total

    @property
    def records(self):
        r"""Gets the records of this ListWorkitemStatusRecordsV4Response.

        操作历史

        :return: The records of this ListWorkitemStatusRecordsV4Response.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.WorkitemStatusRecords`]
        """
        return self._records

    @records.setter
    def records(self, records):
        r"""Sets the records of this ListWorkitemStatusRecordsV4Response.

        操作历史

        :param records: The records of this ListWorkitemStatusRecordsV4Response.
        :type records: list[:class:`huaweicloudsdkprojectman.v4.WorkitemStatusRecords`]
        """
        self._records = records

    @property
    def total(self):
        r"""Gets the total of this ListWorkitemStatusRecordsV4Response.

        总数

        :return: The total of this ListWorkitemStatusRecordsV4Response.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListWorkitemStatusRecordsV4Response.

        总数

        :param total: The total of this ListWorkitemStatusRecordsV4Response.
        :type total: int
        """
        self._total = total

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
        if not isinstance(other, ListWorkitemStatusRecordsV4Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
