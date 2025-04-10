# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StageRun:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'category': 'str',
        'name': 'str',
        'identifier': 'str',
        'run_always': 'bool',
        'parallel': 'str',
        'is_select': 'bool',
        'sequence': 'int',
        'depends_on': 'list[str]',
        'condition': 'str',
        'status': 'str',
        'start_time': 'int',
        'end_time': 'int',
        'pre': 'list[StepRun]',
        'post': 'list[StepRun]',
        'jobs': 'list[JobRun]'
    }

    attribute_map = {
        'id': 'id',
        'category': 'category',
        'name': 'name',
        'identifier': 'identifier',
        'run_always': 'run_always',
        'parallel': 'parallel',
        'is_select': 'is_select',
        'sequence': 'sequence',
        'depends_on': 'depends_on',
        'condition': 'condition',
        'status': 'status',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'pre': 'pre',
        'post': 'post',
        'jobs': 'jobs'
    }

    def __init__(self, id=None, category=None, name=None, identifier=None, run_always=None, parallel=None, is_select=None, sequence=None, depends_on=None, condition=None, status=None, start_time=None, end_time=None, pre=None, post=None, jobs=None):
        r"""StageRun

        The model defined in huaweicloud sdk

        :param id: 阶段ID
        :type id: str
        :param category: 阶段类型
        :type category: str
        :param name: 阶段名称
        :type name: str
        :param identifier: 唯一标识
        :type identifier: str
        :param run_always: 是否总是运行
        :type run_always: bool
        :param parallel: 是否并行
        :type parallel: str
        :param is_select: 是否选中
        :type is_select: bool
        :param sequence: 序列号
        :type sequence: int
        :param depends_on: 依赖
        :type depends_on: list[str]
        :param condition: 运行条件
        :type condition: str
        :param status: 状态
        :type status: str
        :param start_time: 开始时间
        :type start_time: int
        :param end_time: 结束时间
        :type end_time: int
        :param pre: 阶段准入
        :type pre: list[:class:`huaweicloudsdkcodeartspipeline.v2.StepRun`]
        :param post: 阶段准出
        :type post: list[:class:`huaweicloudsdkcodeartspipeline.v2.StepRun`]
        :param jobs: 任务
        :type jobs: list[:class:`huaweicloudsdkcodeartspipeline.v2.JobRun`]
        """
        
        

        self._id = None
        self._category = None
        self._name = None
        self._identifier = None
        self._run_always = None
        self._parallel = None
        self._is_select = None
        self._sequence = None
        self._depends_on = None
        self._condition = None
        self._status = None
        self._start_time = None
        self._end_time = None
        self._pre = None
        self._post = None
        self._jobs = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if category is not None:
            self.category = category
        if name is not None:
            self.name = name
        if identifier is not None:
            self.identifier = identifier
        if run_always is not None:
            self.run_always = run_always
        if parallel is not None:
            self.parallel = parallel
        if is_select is not None:
            self.is_select = is_select
        if sequence is not None:
            self.sequence = sequence
        if depends_on is not None:
            self.depends_on = depends_on
        if condition is not None:
            self.condition = condition
        if status is not None:
            self.status = status
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if pre is not None:
            self.pre = pre
        if post is not None:
            self.post = post
        if jobs is not None:
            self.jobs = jobs

    @property
    def id(self):
        r"""Gets the id of this StageRun.

        阶段ID

        :return: The id of this StageRun.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this StageRun.

        阶段ID

        :param id: The id of this StageRun.
        :type id: str
        """
        self._id = id

    @property
    def category(self):
        r"""Gets the category of this StageRun.

        阶段类型

        :return: The category of this StageRun.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this StageRun.

        阶段类型

        :param category: The category of this StageRun.
        :type category: str
        """
        self._category = category

    @property
    def name(self):
        r"""Gets the name of this StageRun.

        阶段名称

        :return: The name of this StageRun.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this StageRun.

        阶段名称

        :param name: The name of this StageRun.
        :type name: str
        """
        self._name = name

    @property
    def identifier(self):
        r"""Gets the identifier of this StageRun.

        唯一标识

        :return: The identifier of this StageRun.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        r"""Sets the identifier of this StageRun.

        唯一标识

        :param identifier: The identifier of this StageRun.
        :type identifier: str
        """
        self._identifier = identifier

    @property
    def run_always(self):
        r"""Gets the run_always of this StageRun.

        是否总是运行

        :return: The run_always of this StageRun.
        :rtype: bool
        """
        return self._run_always

    @run_always.setter
    def run_always(self, run_always):
        r"""Sets the run_always of this StageRun.

        是否总是运行

        :param run_always: The run_always of this StageRun.
        :type run_always: bool
        """
        self._run_always = run_always

    @property
    def parallel(self):
        r"""Gets the parallel of this StageRun.

        是否并行

        :return: The parallel of this StageRun.
        :rtype: str
        """
        return self._parallel

    @parallel.setter
    def parallel(self, parallel):
        r"""Sets the parallel of this StageRun.

        是否并行

        :param parallel: The parallel of this StageRun.
        :type parallel: str
        """
        self._parallel = parallel

    @property
    def is_select(self):
        r"""Gets the is_select of this StageRun.

        是否选中

        :return: The is_select of this StageRun.
        :rtype: bool
        """
        return self._is_select

    @is_select.setter
    def is_select(self, is_select):
        r"""Sets the is_select of this StageRun.

        是否选中

        :param is_select: The is_select of this StageRun.
        :type is_select: bool
        """
        self._is_select = is_select

    @property
    def sequence(self):
        r"""Gets the sequence of this StageRun.

        序列号

        :return: The sequence of this StageRun.
        :rtype: int
        """
        return self._sequence

    @sequence.setter
    def sequence(self, sequence):
        r"""Sets the sequence of this StageRun.

        序列号

        :param sequence: The sequence of this StageRun.
        :type sequence: int
        """
        self._sequence = sequence

    @property
    def depends_on(self):
        r"""Gets the depends_on of this StageRun.

        依赖

        :return: The depends_on of this StageRun.
        :rtype: list[str]
        """
        return self._depends_on

    @depends_on.setter
    def depends_on(self, depends_on):
        r"""Sets the depends_on of this StageRun.

        依赖

        :param depends_on: The depends_on of this StageRun.
        :type depends_on: list[str]
        """
        self._depends_on = depends_on

    @property
    def condition(self):
        r"""Gets the condition of this StageRun.

        运行条件

        :return: The condition of this StageRun.
        :rtype: str
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        r"""Sets the condition of this StageRun.

        运行条件

        :param condition: The condition of this StageRun.
        :type condition: str
        """
        self._condition = condition

    @property
    def status(self):
        r"""Gets the status of this StageRun.

        状态

        :return: The status of this StageRun.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this StageRun.

        状态

        :param status: The status of this StageRun.
        :type status: str
        """
        self._status = status

    @property
    def start_time(self):
        r"""Gets the start_time of this StageRun.

        开始时间

        :return: The start_time of this StageRun.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this StageRun.

        开始时间

        :param start_time: The start_time of this StageRun.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this StageRun.

        结束时间

        :return: The end_time of this StageRun.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this StageRun.

        结束时间

        :param end_time: The end_time of this StageRun.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def pre(self):
        r"""Gets the pre of this StageRun.

        阶段准入

        :return: The pre of this StageRun.
        :rtype: list[:class:`huaweicloudsdkcodeartspipeline.v2.StepRun`]
        """
        return self._pre

    @pre.setter
    def pre(self, pre):
        r"""Sets the pre of this StageRun.

        阶段准入

        :param pre: The pre of this StageRun.
        :type pre: list[:class:`huaweicloudsdkcodeartspipeline.v2.StepRun`]
        """
        self._pre = pre

    @property
    def post(self):
        r"""Gets the post of this StageRun.

        阶段准出

        :return: The post of this StageRun.
        :rtype: list[:class:`huaweicloudsdkcodeartspipeline.v2.StepRun`]
        """
        return self._post

    @post.setter
    def post(self, post):
        r"""Sets the post of this StageRun.

        阶段准出

        :param post: The post of this StageRun.
        :type post: list[:class:`huaweicloudsdkcodeartspipeline.v2.StepRun`]
        """
        self._post = post

    @property
    def jobs(self):
        r"""Gets the jobs of this StageRun.

        任务

        :return: The jobs of this StageRun.
        :rtype: list[:class:`huaweicloudsdkcodeartspipeline.v2.JobRun`]
        """
        return self._jobs

    @jobs.setter
    def jobs(self, jobs):
        r"""Sets the jobs of this StageRun.

        任务

        :param jobs: The jobs of this StageRun.
        :type jobs: list[:class:`huaweicloudsdkcodeartspipeline.v2.JobRun`]
        """
        self._jobs = jobs

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
        if not isinstance(other, StageRun):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
