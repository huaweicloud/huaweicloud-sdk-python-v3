# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListWorkTableIssueRequestV4RequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'offset': 'int',
        'limit': 'int',
        'subject': 'str',
        'created_on': 'str',
        'updated_on': 'str',
        'closed_on': 'str',
        'start_date': 'str',
        'due_date': 'str',
        'tracker_id': 'str',
        'status_id': 'str',
        'author_id': 'str',
        'developer_id': 'str',
        'priority_id': 'str'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'subject': 'subject',
        'created_on': 'created_on',
        'updated_on': 'updated_on',
        'closed_on': 'closed_on',
        'start_date': 'start_date',
        'due_date': 'due_date',
        'tracker_id': 'tracker_id',
        'status_id': 'status_id',
        'author_id': 'author_id',
        'developer_id': 'developer_id',
        'priority_id': 'priority_id'
    }

    def __init__(self, offset=None, limit=None, subject=None, created_on=None, updated_on=None, closed_on=None, start_date=None, due_date=None, tracker_id=None, status_id=None, author_id=None, developer_id=None, priority_id=None):
        r"""ListWorkTableIssueRequestV4RequestBody

        The model defined in huaweicloud sdk

        :param offset: 偏移量,offset是limit的整数倍，limit&#x3D;10,offset&#x3D;0,10,20...
        :type offset: int
        :param limit: 每页显示数量
        :type limit: int
        :param subject: 搜索关键词
        :type subject: str
        :param created_on: 工作项创建时间区间
        :type created_on: str
        :param updated_on: 工作项更新时间区间
        :type updated_on: str
        :param closed_on: 工作项结束时间区间
        :type closed_on: str
        :param start_date: 工作项预计开始日期区间
        :type start_date: str
        :param due_date: 工作项预计结束日期区间
        :type due_date: str
        :param tracker_id: 工作项类型
        :type tracker_id: str
        :param status_id: 工作项状态
        :type status_id: str
        :param author_id: 工作项创建人id
        :type author_id: str
        :param developer_id: 工作项开发人员id
        :type developer_id: str
        :param priority_id: 工作项优先级id
        :type priority_id: str
        """
        
        

        self._offset = None
        self._limit = None
        self._subject = None
        self._created_on = None
        self._updated_on = None
        self._closed_on = None
        self._start_date = None
        self._due_date = None
        self._tracker_id = None
        self._status_id = None
        self._author_id = None
        self._developer_id = None
        self._priority_id = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if subject is not None:
            self.subject = subject
        if created_on is not None:
            self.created_on = created_on
        if updated_on is not None:
            self.updated_on = updated_on
        if closed_on is not None:
            self.closed_on = closed_on
        if start_date is not None:
            self.start_date = start_date
        if due_date is not None:
            self.due_date = due_date
        if tracker_id is not None:
            self.tracker_id = tracker_id
        if status_id is not None:
            self.status_id = status_id
        if author_id is not None:
            self.author_id = author_id
        if developer_id is not None:
            self.developer_id = developer_id
        if priority_id is not None:
            self.priority_id = priority_id

    @property
    def offset(self):
        r"""Gets the offset of this ListWorkTableIssueRequestV4RequestBody.

        偏移量,offset是limit的整数倍，limit=10,offset=0,10,20...

        :return: The offset of this ListWorkTableIssueRequestV4RequestBody.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListWorkTableIssueRequestV4RequestBody.

        偏移量,offset是limit的整数倍，limit=10,offset=0,10,20...

        :param offset: The offset of this ListWorkTableIssueRequestV4RequestBody.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListWorkTableIssueRequestV4RequestBody.

        每页显示数量

        :return: The limit of this ListWorkTableIssueRequestV4RequestBody.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListWorkTableIssueRequestV4RequestBody.

        每页显示数量

        :param limit: The limit of this ListWorkTableIssueRequestV4RequestBody.
        :type limit: int
        """
        self._limit = limit

    @property
    def subject(self):
        r"""Gets the subject of this ListWorkTableIssueRequestV4RequestBody.

        搜索关键词

        :return: The subject of this ListWorkTableIssueRequestV4RequestBody.
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        r"""Sets the subject of this ListWorkTableIssueRequestV4RequestBody.

        搜索关键词

        :param subject: The subject of this ListWorkTableIssueRequestV4RequestBody.
        :type subject: str
        """
        self._subject = subject

    @property
    def created_on(self):
        r"""Gets the created_on of this ListWorkTableIssueRequestV4RequestBody.

        工作项创建时间区间

        :return: The created_on of this ListWorkTableIssueRequestV4RequestBody.
        :rtype: str
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        r"""Sets the created_on of this ListWorkTableIssueRequestV4RequestBody.

        工作项创建时间区间

        :param created_on: The created_on of this ListWorkTableIssueRequestV4RequestBody.
        :type created_on: str
        """
        self._created_on = created_on

    @property
    def updated_on(self):
        r"""Gets the updated_on of this ListWorkTableIssueRequestV4RequestBody.

        工作项更新时间区间

        :return: The updated_on of this ListWorkTableIssueRequestV4RequestBody.
        :rtype: str
        """
        return self._updated_on

    @updated_on.setter
    def updated_on(self, updated_on):
        r"""Sets the updated_on of this ListWorkTableIssueRequestV4RequestBody.

        工作项更新时间区间

        :param updated_on: The updated_on of this ListWorkTableIssueRequestV4RequestBody.
        :type updated_on: str
        """
        self._updated_on = updated_on

    @property
    def closed_on(self):
        r"""Gets the closed_on of this ListWorkTableIssueRequestV4RequestBody.

        工作项结束时间区间

        :return: The closed_on of this ListWorkTableIssueRequestV4RequestBody.
        :rtype: str
        """
        return self._closed_on

    @closed_on.setter
    def closed_on(self, closed_on):
        r"""Sets the closed_on of this ListWorkTableIssueRequestV4RequestBody.

        工作项结束时间区间

        :param closed_on: The closed_on of this ListWorkTableIssueRequestV4RequestBody.
        :type closed_on: str
        """
        self._closed_on = closed_on

    @property
    def start_date(self):
        r"""Gets the start_date of this ListWorkTableIssueRequestV4RequestBody.

        工作项预计开始日期区间

        :return: The start_date of this ListWorkTableIssueRequestV4RequestBody.
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        r"""Sets the start_date of this ListWorkTableIssueRequestV4RequestBody.

        工作项预计开始日期区间

        :param start_date: The start_date of this ListWorkTableIssueRequestV4RequestBody.
        :type start_date: str
        """
        self._start_date = start_date

    @property
    def due_date(self):
        r"""Gets the due_date of this ListWorkTableIssueRequestV4RequestBody.

        工作项预计结束日期区间

        :return: The due_date of this ListWorkTableIssueRequestV4RequestBody.
        :rtype: str
        """
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        r"""Sets the due_date of this ListWorkTableIssueRequestV4RequestBody.

        工作项预计结束日期区间

        :param due_date: The due_date of this ListWorkTableIssueRequestV4RequestBody.
        :type due_date: str
        """
        self._due_date = due_date

    @property
    def tracker_id(self):
        r"""Gets the tracker_id of this ListWorkTableIssueRequestV4RequestBody.

        工作项类型

        :return: The tracker_id of this ListWorkTableIssueRequestV4RequestBody.
        :rtype: str
        """
        return self._tracker_id

    @tracker_id.setter
    def tracker_id(self, tracker_id):
        r"""Sets the tracker_id of this ListWorkTableIssueRequestV4RequestBody.

        工作项类型

        :param tracker_id: The tracker_id of this ListWorkTableIssueRequestV4RequestBody.
        :type tracker_id: str
        """
        self._tracker_id = tracker_id

    @property
    def status_id(self):
        r"""Gets the status_id of this ListWorkTableIssueRequestV4RequestBody.

        工作项状态

        :return: The status_id of this ListWorkTableIssueRequestV4RequestBody.
        :rtype: str
        """
        return self._status_id

    @status_id.setter
    def status_id(self, status_id):
        r"""Sets the status_id of this ListWorkTableIssueRequestV4RequestBody.

        工作项状态

        :param status_id: The status_id of this ListWorkTableIssueRequestV4RequestBody.
        :type status_id: str
        """
        self._status_id = status_id

    @property
    def author_id(self):
        r"""Gets the author_id of this ListWorkTableIssueRequestV4RequestBody.

        工作项创建人id

        :return: The author_id of this ListWorkTableIssueRequestV4RequestBody.
        :rtype: str
        """
        return self._author_id

    @author_id.setter
    def author_id(self, author_id):
        r"""Sets the author_id of this ListWorkTableIssueRequestV4RequestBody.

        工作项创建人id

        :param author_id: The author_id of this ListWorkTableIssueRequestV4RequestBody.
        :type author_id: str
        """
        self._author_id = author_id

    @property
    def developer_id(self):
        r"""Gets the developer_id of this ListWorkTableIssueRequestV4RequestBody.

        工作项开发人员id

        :return: The developer_id of this ListWorkTableIssueRequestV4RequestBody.
        :rtype: str
        """
        return self._developer_id

    @developer_id.setter
    def developer_id(self, developer_id):
        r"""Sets the developer_id of this ListWorkTableIssueRequestV4RequestBody.

        工作项开发人员id

        :param developer_id: The developer_id of this ListWorkTableIssueRequestV4RequestBody.
        :type developer_id: str
        """
        self._developer_id = developer_id

    @property
    def priority_id(self):
        r"""Gets the priority_id of this ListWorkTableIssueRequestV4RequestBody.

        工作项优先级id

        :return: The priority_id of this ListWorkTableIssueRequestV4RequestBody.
        :rtype: str
        """
        return self._priority_id

    @priority_id.setter
    def priority_id(self, priority_id):
        r"""Sets the priority_id of this ListWorkTableIssueRequestV4RequestBody.

        工作项优先级id

        :param priority_id: The priority_id of this ListWorkTableIssueRequestV4RequestBody.
        :type priority_id: str
        """
        self._priority_id = priority_id

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
        if not isinstance(other, ListWorkTableIssueRequestV4RequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
