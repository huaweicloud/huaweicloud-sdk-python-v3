# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListIssueRecordsV4Response(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'created_time': 'int',
        'records': 'list[IssueRecordV4]',
        'total': 'int'
    }

    attribute_map = {
        'id': 'id',
        'created_time': 'created_time',
        'records': 'records',
        'total': 'total'
    }

    def __init__(self, id=None, created_time=None, records=None, total=None):
        """ListIssueRecordsV4Response

        The model defined in huaweicloud sdk

        :param id: 操作记录id (已废弃)
        :type id: int
        :param created_time: 创建时间 (已废弃)
        :type created_time: int
        :param records: 
        :type records: list[:class:`huaweicloudsdkprojectman.v4.IssueRecordV4`]
        :param total: 操作记录总数
        :type total: int
        """
        
        super(ListIssueRecordsV4Response, self).__init__()

        self._id = None
        self._created_time = None
        self._records = None
        self._total = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if created_time is not None:
            self.created_time = created_time
        if records is not None:
            self.records = records
        if total is not None:
            self.total = total

    @property
    def id(self):
        """Gets the id of this ListIssueRecordsV4Response.

        操作记录id (已废弃)

        :return: The id of this ListIssueRecordsV4Response.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListIssueRecordsV4Response.

        操作记录id (已废弃)

        :param id: The id of this ListIssueRecordsV4Response.
        :type id: int
        """
        self._id = id

    @property
    def created_time(self):
        """Gets the created_time of this ListIssueRecordsV4Response.

        创建时间 (已废弃)

        :return: The created_time of this ListIssueRecordsV4Response.
        :rtype: int
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this ListIssueRecordsV4Response.

        创建时间 (已废弃)

        :param created_time: The created_time of this ListIssueRecordsV4Response.
        :type created_time: int
        """
        self._created_time = created_time

    @property
    def records(self):
        """Gets the records of this ListIssueRecordsV4Response.


        :return: The records of this ListIssueRecordsV4Response.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.IssueRecordV4`]
        """
        return self._records

    @records.setter
    def records(self, records):
        """Sets the records of this ListIssueRecordsV4Response.


        :param records: The records of this ListIssueRecordsV4Response.
        :type records: list[:class:`huaweicloudsdkprojectman.v4.IssueRecordV4`]
        """
        self._records = records

    @property
    def total(self):
        """Gets the total of this ListIssueRecordsV4Response.

        操作记录总数

        :return: The total of this ListIssueRecordsV4Response.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListIssueRecordsV4Response.

        操作记录总数

        :param total: The total of this ListIssueRecordsV4Response.
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
        if not isinstance(other, ListIssueRecordsV4Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
