# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckRecordDataInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'check_time': 'str',
        'check_end_time': 'str',
        'issue_counts': 'CheckRecordIssueCountsInfo'
    }

    attribute_map = {
        'check_time': 'check_time',
        'check_end_time': 'check_end_time',
        'issue_counts': 'issue_counts'
    }

    def __init__(self, check_time=None, check_end_time=None, issue_counts=None):
        """CheckRecordDataInfo

        The model defined in huaweicloud sdk

        :param check_time: 检查任务执行开始时间
        :type check_time: str
        :param check_end_time: 检查任务执行结束时间
        :type check_end_time: str
        :param issue_counts: 
        :type issue_counts: :class:`huaweicloudsdkcodecheck.v2.CheckRecordIssueCountsInfo`
        """
        
        

        self._check_time = None
        self._check_end_time = None
        self._issue_counts = None
        self.discriminator = None

        if check_time is not None:
            self.check_time = check_time
        if check_end_time is not None:
            self.check_end_time = check_end_time
        if issue_counts is not None:
            self.issue_counts = issue_counts

    @property
    def check_time(self):
        """Gets the check_time of this CheckRecordDataInfo.

        检查任务执行开始时间

        :return: The check_time of this CheckRecordDataInfo.
        :rtype: str
        """
        return self._check_time

    @check_time.setter
    def check_time(self, check_time):
        """Sets the check_time of this CheckRecordDataInfo.

        检查任务执行开始时间

        :param check_time: The check_time of this CheckRecordDataInfo.
        :type check_time: str
        """
        self._check_time = check_time

    @property
    def check_end_time(self):
        """Gets the check_end_time of this CheckRecordDataInfo.

        检查任务执行结束时间

        :return: The check_end_time of this CheckRecordDataInfo.
        :rtype: str
        """
        return self._check_end_time

    @check_end_time.setter
    def check_end_time(self, check_end_time):
        """Sets the check_end_time of this CheckRecordDataInfo.

        检查任务执行结束时间

        :param check_end_time: The check_end_time of this CheckRecordDataInfo.
        :type check_end_time: str
        """
        self._check_end_time = check_end_time

    @property
    def issue_counts(self):
        """Gets the issue_counts of this CheckRecordDataInfo.


        :return: The issue_counts of this CheckRecordDataInfo.
        :rtype: :class:`huaweicloudsdkcodecheck.v2.CheckRecordIssueCountsInfo`
        """
        return self._issue_counts

    @issue_counts.setter
    def issue_counts(self, issue_counts):
        """Sets the issue_counts of this CheckRecordDataInfo.


        :param issue_counts: The issue_counts of this CheckRecordDataInfo.
        :type issue_counts: :class:`huaweicloudsdkcodecheck.v2.CheckRecordIssueCountsInfo`
        """
        self._issue_counts = issue_counts

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
        if not isinstance(other, CheckRecordDataInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
