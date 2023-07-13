# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReportFilter:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'creator_ids': 'str',
        'owner_ids': 'str',
        'ranks': 'str',
        'release_ids': 'str',
        'status': 'str',
        'module_ids': 'str',
        'results': 'str',
        'label_ids': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'is_associate_issue': 'str'
    }

    attribute_map = {
        'creator_ids': 'creatorIds',
        'owner_ids': 'ownerIds',
        'ranks': 'ranks',
        'release_ids': 'releaseIds',
        'status': 'status',
        'module_ids': 'moduleIds',
        'results': 'results',
        'label_ids': 'labelIds',
        'start_time': 'startTime',
        'end_time': 'endTime',
        'is_associate_issue': 'isAssociateIssue'
    }

    def __init__(self, creator_ids=None, owner_ids=None, ranks=None, release_ids=None, status=None, module_ids=None, results=None, label_ids=None, start_time=None, end_time=None, is_associate_issue=None):
        """ReportFilter

        The model defined in huaweicloud sdk

        :param creator_ids: 创建人
        :type creator_ids: str
        :param owner_ids: 所属人
        :type owner_ids: str
        :param ranks: 级别
        :type ranks: str
        :param release_ids: releaseId
        :type release_ids: str
        :param status: 状态
        :type status: str
        :param module_ids: 级别
        :type module_ids: str
        :param results: 结果
        :type results: str
        :param label_ids: 标签
        :type label_ids: str
        :param start_time: 开始时间
        :type start_time: str
        :param end_time: 结束时间
        :type end_time: str
        :param is_associate_issue: 是否关联需求
        :type is_associate_issue: str
        """
        
        

        self._creator_ids = None
        self._owner_ids = None
        self._ranks = None
        self._release_ids = None
        self._status = None
        self._module_ids = None
        self._results = None
        self._label_ids = None
        self._start_time = None
        self._end_time = None
        self._is_associate_issue = None
        self.discriminator = None

        if creator_ids is not None:
            self.creator_ids = creator_ids
        if owner_ids is not None:
            self.owner_ids = owner_ids
        if ranks is not None:
            self.ranks = ranks
        if release_ids is not None:
            self.release_ids = release_ids
        if status is not None:
            self.status = status
        if module_ids is not None:
            self.module_ids = module_ids
        if results is not None:
            self.results = results
        if label_ids is not None:
            self.label_ids = label_ids
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if is_associate_issue is not None:
            self.is_associate_issue = is_associate_issue

    @property
    def creator_ids(self):
        """Gets the creator_ids of this ReportFilter.

        创建人

        :return: The creator_ids of this ReportFilter.
        :rtype: str
        """
        return self._creator_ids

    @creator_ids.setter
    def creator_ids(self, creator_ids):
        """Sets the creator_ids of this ReportFilter.

        创建人

        :param creator_ids: The creator_ids of this ReportFilter.
        :type creator_ids: str
        """
        self._creator_ids = creator_ids

    @property
    def owner_ids(self):
        """Gets the owner_ids of this ReportFilter.

        所属人

        :return: The owner_ids of this ReportFilter.
        :rtype: str
        """
        return self._owner_ids

    @owner_ids.setter
    def owner_ids(self, owner_ids):
        """Sets the owner_ids of this ReportFilter.

        所属人

        :param owner_ids: The owner_ids of this ReportFilter.
        :type owner_ids: str
        """
        self._owner_ids = owner_ids

    @property
    def ranks(self):
        """Gets the ranks of this ReportFilter.

        级别

        :return: The ranks of this ReportFilter.
        :rtype: str
        """
        return self._ranks

    @ranks.setter
    def ranks(self, ranks):
        """Sets the ranks of this ReportFilter.

        级别

        :param ranks: The ranks of this ReportFilter.
        :type ranks: str
        """
        self._ranks = ranks

    @property
    def release_ids(self):
        """Gets the release_ids of this ReportFilter.

        releaseId

        :return: The release_ids of this ReportFilter.
        :rtype: str
        """
        return self._release_ids

    @release_ids.setter
    def release_ids(self, release_ids):
        """Sets the release_ids of this ReportFilter.

        releaseId

        :param release_ids: The release_ids of this ReportFilter.
        :type release_ids: str
        """
        self._release_ids = release_ids

    @property
    def status(self):
        """Gets the status of this ReportFilter.

        状态

        :return: The status of this ReportFilter.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ReportFilter.

        状态

        :param status: The status of this ReportFilter.
        :type status: str
        """
        self._status = status

    @property
    def module_ids(self):
        """Gets the module_ids of this ReportFilter.

        级别

        :return: The module_ids of this ReportFilter.
        :rtype: str
        """
        return self._module_ids

    @module_ids.setter
    def module_ids(self, module_ids):
        """Sets the module_ids of this ReportFilter.

        级别

        :param module_ids: The module_ids of this ReportFilter.
        :type module_ids: str
        """
        self._module_ids = module_ids

    @property
    def results(self):
        """Gets the results of this ReportFilter.

        结果

        :return: The results of this ReportFilter.
        :rtype: str
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this ReportFilter.

        结果

        :param results: The results of this ReportFilter.
        :type results: str
        """
        self._results = results

    @property
    def label_ids(self):
        """Gets the label_ids of this ReportFilter.

        标签

        :return: The label_ids of this ReportFilter.
        :rtype: str
        """
        return self._label_ids

    @label_ids.setter
    def label_ids(self, label_ids):
        """Sets the label_ids of this ReportFilter.

        标签

        :param label_ids: The label_ids of this ReportFilter.
        :type label_ids: str
        """
        self._label_ids = label_ids

    @property
    def start_time(self):
        """Gets the start_time of this ReportFilter.

        开始时间

        :return: The start_time of this ReportFilter.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ReportFilter.

        开始时间

        :param start_time: The start_time of this ReportFilter.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ReportFilter.

        结束时间

        :return: The end_time of this ReportFilter.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ReportFilter.

        结束时间

        :param end_time: The end_time of this ReportFilter.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def is_associate_issue(self):
        """Gets the is_associate_issue of this ReportFilter.

        是否关联需求

        :return: The is_associate_issue of this ReportFilter.
        :rtype: str
        """
        return self._is_associate_issue

    @is_associate_issue.setter
    def is_associate_issue(self, is_associate_issue):
        """Sets the is_associate_issue of this ReportFilter.

        是否关联需求

        :param is_associate_issue: The is_associate_issue of this ReportFilter.
        :type is_associate_issue: str
        """
        self._is_associate_issue = is_associate_issue

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
        if not isinstance(other, ReportFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
