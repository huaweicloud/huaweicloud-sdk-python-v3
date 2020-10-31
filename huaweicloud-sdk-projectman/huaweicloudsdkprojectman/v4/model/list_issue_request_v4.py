# coding: utf-8

import pprint
import re

import six





class ListIssueRequestV4:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'assigned_ids': 'list[int]',
        'creator_ids': 'list[int]',
        'developer_ids': 'list[int]',
        'domain_ids': 'list[int]',
        'done_ratios': 'list[int]',
        'iteration_ids': 'list[int]',
        'limit': 'int',
        'module_ids': 'list[int]',
        'offset': 'int',
        'priority_ids': 'list[int]',
        'query_type': 'str',
        'severity_ids': 'list[int]',
        'status_ids': 'list[int]',
        'story_point_ids': 'list[int]',
        'tracker_ids': 'list[int]'
    }

    attribute_map = {
        'assigned_ids': 'assigned_ids',
        'creator_ids': 'creator_ids',
        'developer_ids': 'developer_ids',
        'domain_ids': 'domain_ids',
        'done_ratios': 'done_ratios',
        'iteration_ids': 'iteration_ids',
        'limit': 'limit',
        'module_ids': 'module_ids',
        'offset': 'offset',
        'priority_ids': 'priority_ids',
        'query_type': 'query_type',
        'severity_ids': 'severity_ids',
        'status_ids': 'status_ids',
        'story_point_ids': 'story_point_ids',
        'tracker_ids': 'tracker_ids'
    }

    def __init__(self, assigned_ids=None, creator_ids=None, developer_ids=None, domain_ids=None, done_ratios=None, iteration_ids=None, limit=None, module_ids=None, offset=None, priority_ids=None, query_type=None, severity_ids=None, status_ids=None, story_point_ids=None, tracker_ids=None):
        """ListIssueRequestV4 - a model defined in huaweicloud sdk"""
        
        

        self._assigned_ids = None
        self._creator_ids = None
        self._developer_ids = None
        self._domain_ids = None
        self._done_ratios = None
        self._iteration_ids = None
        self._limit = None
        self._module_ids = None
        self._offset = None
        self._priority_ids = None
        self._query_type = None
        self._severity_ids = None
        self._status_ids = None
        self._story_point_ids = None
        self._tracker_ids = None
        self.discriminator = None

        if assigned_ids is not None:
            self.assigned_ids = assigned_ids
        if creator_ids is not None:
            self.creator_ids = creator_ids
        if developer_ids is not None:
            self.developer_ids = developer_ids
        if domain_ids is not None:
            self.domain_ids = domain_ids
        if done_ratios is not None:
            self.done_ratios = done_ratios
        if iteration_ids is not None:
            self.iteration_ids = iteration_ids
        if limit is not None:
            self.limit = limit
        if module_ids is not None:
            self.module_ids = module_ids
        if offset is not None:
            self.offset = offset
        if priority_ids is not None:
            self.priority_ids = priority_ids
        if query_type is not None:
            self.query_type = query_type
        if severity_ids is not None:
            self.severity_ids = severity_ids
        if status_ids is not None:
            self.status_ids = status_ids
        if story_point_ids is not None:
            self.story_point_ids = story_point_ids
        if tracker_ids is not None:
            self.tracker_ids = tracker_ids

    @property
    def assigned_ids(self):
        """Gets the assigned_ids of this ListIssueRequestV4.

        处理人id

        :return: The assigned_ids of this ListIssueRequestV4.
        :rtype: list[int]
        """
        return self._assigned_ids

    @assigned_ids.setter
    def assigned_ids(self, assigned_ids):
        """Sets the assigned_ids of this ListIssueRequestV4.

        处理人id

        :param assigned_ids: The assigned_ids of this ListIssueRequestV4.
        :type: list[int]
        """
        self._assigned_ids = assigned_ids

    @property
    def creator_ids(self):
        """Gets the creator_ids of this ListIssueRequestV4.

        创建者id

        :return: The creator_ids of this ListIssueRequestV4.
        :rtype: list[int]
        """
        return self._creator_ids

    @creator_ids.setter
    def creator_ids(self, creator_ids):
        """Sets the creator_ids of this ListIssueRequestV4.

        创建者id

        :param creator_ids: The creator_ids of this ListIssueRequestV4.
        :type: list[int]
        """
        self._creator_ids = creator_ids

    @property
    def developer_ids(self):
        """Gets the developer_ids of this ListIssueRequestV4.

        开发人id,对应用户信息的数字id

        :return: The developer_ids of this ListIssueRequestV4.
        :rtype: list[int]
        """
        return self._developer_ids

    @developer_ids.setter
    def developer_ids(self, developer_ids):
        """Sets the developer_ids of this ListIssueRequestV4.

        开发人id,对应用户信息的数字id

        :param developer_ids: The developer_ids of this ListIssueRequestV4.
        :type: list[int]
        """
        self._developer_ids = developer_ids

    @property
    def domain_ids(self):
        """Gets the domain_ids of this ListIssueRequestV4.

        id, 领域 14, '性能', 15, '功能', 16, '可靠性' 17, '网络安全' 18, '可维护性' 19, '其他DFX' 20, '可用性'

        :return: The domain_ids of this ListIssueRequestV4.
        :rtype: list[int]
        """
        return self._domain_ids

    @domain_ids.setter
    def domain_ids(self, domain_ids):
        """Sets the domain_ids of this ListIssueRequestV4.

        id, 领域 14, '性能', 15, '功能', 16, '可靠性' 17, '网络安全' 18, '可维护性' 19, '其他DFX' 20, '可用性'

        :param domain_ids: The domain_ids of this ListIssueRequestV4.
        :type: list[int]
        """
        self._domain_ids = domain_ids

    @property
    def done_ratios(self):
        """Gets the done_ratios of this ListIssueRequestV4.

        完成度

        :return: The done_ratios of this ListIssueRequestV4.
        :rtype: list[int]
        """
        return self._done_ratios

    @done_ratios.setter
    def done_ratios(self, done_ratios):
        """Sets the done_ratios of this ListIssueRequestV4.

        完成度

        :param done_ratios: The done_ratios of this ListIssueRequestV4.
        :type: list[int]
        """
        self._done_ratios = done_ratios

    @property
    def iteration_ids(self):
        """Gets the iteration_ids of this ListIssueRequestV4.

        迭代id

        :return: The iteration_ids of this ListIssueRequestV4.
        :rtype: list[int]
        """
        return self._iteration_ids

    @iteration_ids.setter
    def iteration_ids(self, iteration_ids):
        """Sets the iteration_ids of this ListIssueRequestV4.

        迭代id

        :param iteration_ids: The iteration_ids of this ListIssueRequestV4.
        :type: list[int]
        """
        self._iteration_ids = iteration_ids

    @property
    def limit(self):
        """Gets the limit of this ListIssueRequestV4.

        每页显示数量

        :return: The limit of this ListIssueRequestV4.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListIssueRequestV4.

        每页显示数量

        :param limit: The limit of this ListIssueRequestV4.
        :type: int
        """
        self._limit = limit

    @property
    def module_ids(self):
        """Gets the module_ids of this ListIssueRequestV4.

        模块id

        :return: The module_ids of this ListIssueRequestV4.
        :rtype: list[int]
        """
        return self._module_ids

    @module_ids.setter
    def module_ids(self, module_ids):
        """Sets the module_ids of this ListIssueRequestV4.

        模块id

        :param module_ids: The module_ids of this ListIssueRequestV4.
        :type: list[int]
        """
        self._module_ids = module_ids

    @property
    def offset(self):
        """Gets the offset of this ListIssueRequestV4.

        分页索引，偏移量

        :return: The offset of this ListIssueRequestV4.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListIssueRequestV4.

        分页索引，偏移量

        :param offset: The offset of this ListIssueRequestV4.
        :type: int
        """
        self._offset = offset

    @property
    def priority_ids(self):
        """Gets the priority_ids of this ListIssueRequestV4.

        优先级

        :return: The priority_ids of this ListIssueRequestV4.
        :rtype: list[int]
        """
        return self._priority_ids

    @priority_ids.setter
    def priority_ids(self, priority_ids):
        """Sets the priority_ids of this ListIssueRequestV4.

        优先级

        :param priority_ids: The priority_ids of this ListIssueRequestV4.
        :type: list[int]
        """
        self._priority_ids = priority_ids

    @property
    def query_type(self):
        """Gets the query_type of this ListIssueRequestV4.

        查询类型 backlog feature epic

        :return: The query_type of this ListIssueRequestV4.
        :rtype: str
        """
        return self._query_type

    @query_type.setter
    def query_type(self, query_type):
        """Sets the query_type of this ListIssueRequestV4.

        查询类型 backlog feature epic

        :param query_type: The query_type of this ListIssueRequestV4.
        :type: str
        """
        self._query_type = query_type

    @property
    def severity_ids(self):
        """Gets the severity_ids of this ListIssueRequestV4.

        查询类型

        :return: The severity_ids of this ListIssueRequestV4.
        :rtype: list[int]
        """
        return self._severity_ids

    @severity_ids.setter
    def severity_ids(self, severity_ids):
        """Sets the severity_ids of this ListIssueRequestV4.

        查询类型

        :param severity_ids: The severity_ids of this ListIssueRequestV4.
        :type: list[int]
        """
        self._severity_ids = severity_ids

    @property
    def status_ids(self):
        """Gets the status_ids of this ListIssueRequestV4.

        状态   id 开始   1 进行中 2 已解决 3 测试中 4 已关闭 5 已解决 6

        :return: The status_ids of this ListIssueRequestV4.
        :rtype: list[int]
        """
        return self._status_ids

    @status_ids.setter
    def status_ids(self, status_ids):
        """Sets the status_ids of this ListIssueRequestV4.

        状态   id 开始   1 进行中 2 已解决 3 测试中 4 已关闭 5 已解决 6

        :param status_ids: The status_ids of this ListIssueRequestV4.
        :type: list[int]
        """
        self._status_ids = status_ids

    @property
    def story_point_ids(self):
        """Gets the story_point_ids of this ListIssueRequestV4.

        故事点id

        :return: The story_point_ids of this ListIssueRequestV4.
        :rtype: list[int]
        """
        return self._story_point_ids

    @story_point_ids.setter
    def story_point_ids(self, story_point_ids):
        """Sets the story_point_ids of this ListIssueRequestV4.

        故事点id

        :param story_point_ids: The story_point_ids of this ListIssueRequestV4.
        :type: list[int]
        """
        self._story_point_ids = story_point_ids

    @property
    def tracker_ids(self):
        """Gets the tracker_ids of this ListIssueRequestV4.

        工作项类型,2任务/task,3缺陷/bug,5epic,6feature,7story

        :return: The tracker_ids of this ListIssueRequestV4.
        :rtype: list[int]
        """
        return self._tracker_ids

    @tracker_ids.setter
    def tracker_ids(self, tracker_ids):
        """Sets the tracker_ids of this ListIssueRequestV4.

        工作项类型,2任务/task,3缺陷/bug,5epic,6feature,7story

        :param tracker_ids: The tracker_ids of this ListIssueRequestV4.
        :type: list[int]
        """
        self._tracker_ids = tracker_ids

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListIssueRequestV4):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
