# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSecurityReportSendingRecordsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'report_name': 'str',
        'report_category': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'report_name': 'report_name',
        'report_category': 'report_category',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, report_name=None, report_category=None, limit=None, offset=None):
        r"""ListSecurityReportSendingRecordsRequest

        The model defined in huaweicloud sdk

        :param report_name: 报告名称
        :type report_name: str
        :param report_category: 报告类别
        :type report_category: str
        :param limit: 限制条目数量
        :type limit: int
        :param offset: 偏移量
        :type offset: int
        """
        
        

        self._report_name = None
        self._report_category = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        if report_name is not None:
            self.report_name = report_name
        if report_category is not None:
            self.report_category = report_category
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def report_name(self):
        r"""Gets the report_name of this ListSecurityReportSendingRecordsRequest.

        报告名称

        :return: The report_name of this ListSecurityReportSendingRecordsRequest.
        :rtype: str
        """
        return self._report_name

    @report_name.setter
    def report_name(self, report_name):
        r"""Sets the report_name of this ListSecurityReportSendingRecordsRequest.

        报告名称

        :param report_name: The report_name of this ListSecurityReportSendingRecordsRequest.
        :type report_name: str
        """
        self._report_name = report_name

    @property
    def report_category(self):
        r"""Gets the report_category of this ListSecurityReportSendingRecordsRequest.

        报告类别

        :return: The report_category of this ListSecurityReportSendingRecordsRequest.
        :rtype: str
        """
        return self._report_category

    @report_category.setter
    def report_category(self, report_category):
        r"""Sets the report_category of this ListSecurityReportSendingRecordsRequest.

        报告类别

        :param report_category: The report_category of this ListSecurityReportSendingRecordsRequest.
        :type report_category: str
        """
        self._report_category = report_category

    @property
    def limit(self):
        r"""Gets the limit of this ListSecurityReportSendingRecordsRequest.

        限制条目数量

        :return: The limit of this ListSecurityReportSendingRecordsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListSecurityReportSendingRecordsRequest.

        限制条目数量

        :param limit: The limit of this ListSecurityReportSendingRecordsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListSecurityReportSendingRecordsRequest.

        偏移量

        :return: The offset of this ListSecurityReportSendingRecordsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListSecurityReportSendingRecordsRequest.

        偏移量

        :param offset: The offset of this ListSecurityReportSendingRecordsRequest.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ListSecurityReportSendingRecordsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
