# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BriefRecordItems:

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
        'status': 'str',
        'duration': 'int',
        'create_time': 'str',
        'schedule_time': 'str',
        'queued_time': 'str',
        'start_time': 'str',
        'finish_time': 'str',
        'build_duration': 'int',
        'pending_duration': 'int',
        'project_id': 'str',
        'build_no': 'int',
        'branch': 'str',
        'revision': 'str',
        'trigger_name': 'str',
        'daily_build_number': 'str'
    }

    attribute_map = {
        'id': 'id',
        'status': 'status',
        'duration': 'duration',
        'create_time': 'create_time',
        'schedule_time': 'schedule_time',
        'queued_time': 'queued_time',
        'start_time': 'start_time',
        'finish_time': 'finish_time',
        'build_duration': 'build_duration',
        'pending_duration': 'pending_duration',
        'project_id': 'project_id',
        'build_no': 'build_no',
        'branch': 'branch',
        'revision': 'revision',
        'trigger_name': 'trigger_name',
        'daily_build_number': 'daily_build_number'
    }

    def __init__(self, id=None, status=None, duration=None, create_time=None, schedule_time=None, queued_time=None, start_time=None, finish_time=None, build_duration=None, pending_duration=None, project_id=None, build_no=None, branch=None, revision=None, trigger_name=None, daily_build_number=None):
        r"""BriefRecordItems

        The model defined in huaweicloud sdk

        :param id: 构建任务的ID
        :type id: str
        :param status: 状态
        :type status: str
        :param duration: 构建时长
        :type duration: int
        :param create_time: 创建时间
        :type create_time: str
        :param schedule_time: 构建下发时间
        :type schedule_time: str
        :param queued_time: 构建排队耗时
        :type queued_time: str
        :param start_time: 开始时间
        :type start_time: str
        :param finish_time: 结束时间
        :type finish_time: str
        :param build_duration: 子任务构建耗时
        :type build_duration: int
        :param pending_duration: 等待时间
        :type pending_duration: int
        :param project_id: 所属的项目ID
        :type project_id: str
        :param build_no: 构建任务的构建编号，从1开始，每次构建递增1
        :type build_no: int
        :param branch: 代码分支
        :type branch: str
        :param revision: commitId
        :type revision: str
        :param trigger_name: 触发者名称
        :type trigger_name: str
        :param daily_build_number: 构建编号，每日从1开始
        :type daily_build_number: str
        """
        
        

        self._id = None
        self._status = None
        self._duration = None
        self._create_time = None
        self._schedule_time = None
        self._queued_time = None
        self._start_time = None
        self._finish_time = None
        self._build_duration = None
        self._pending_duration = None
        self._project_id = None
        self._build_no = None
        self._branch = None
        self._revision = None
        self._trigger_name = None
        self._daily_build_number = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if status is not None:
            self.status = status
        if duration is not None:
            self.duration = duration
        if create_time is not None:
            self.create_time = create_time
        if schedule_time is not None:
            self.schedule_time = schedule_time
        if queued_time is not None:
            self.queued_time = queued_time
        if start_time is not None:
            self.start_time = start_time
        if finish_time is not None:
            self.finish_time = finish_time
        if build_duration is not None:
            self.build_duration = build_duration
        if pending_duration is not None:
            self.pending_duration = pending_duration
        if project_id is not None:
            self.project_id = project_id
        if build_no is not None:
            self.build_no = build_no
        if branch is not None:
            self.branch = branch
        if revision is not None:
            self.revision = revision
        if trigger_name is not None:
            self.trigger_name = trigger_name
        if daily_build_number is not None:
            self.daily_build_number = daily_build_number

    @property
    def id(self):
        r"""Gets the id of this BriefRecordItems.

        构建任务的ID

        :return: The id of this BriefRecordItems.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this BriefRecordItems.

        构建任务的ID

        :param id: The id of this BriefRecordItems.
        :type id: str
        """
        self._id = id

    @property
    def status(self):
        r"""Gets the status of this BriefRecordItems.

        状态

        :return: The status of this BriefRecordItems.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this BriefRecordItems.

        状态

        :param status: The status of this BriefRecordItems.
        :type status: str
        """
        self._status = status

    @property
    def duration(self):
        r"""Gets the duration of this BriefRecordItems.

        构建时长

        :return: The duration of this BriefRecordItems.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        r"""Sets the duration of this BriefRecordItems.

        构建时长

        :param duration: The duration of this BriefRecordItems.
        :type duration: int
        """
        self._duration = duration

    @property
    def create_time(self):
        r"""Gets the create_time of this BriefRecordItems.

        创建时间

        :return: The create_time of this BriefRecordItems.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this BriefRecordItems.

        创建时间

        :param create_time: The create_time of this BriefRecordItems.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def schedule_time(self):
        r"""Gets the schedule_time of this BriefRecordItems.

        构建下发时间

        :return: The schedule_time of this BriefRecordItems.
        :rtype: str
        """
        return self._schedule_time

    @schedule_time.setter
    def schedule_time(self, schedule_time):
        r"""Sets the schedule_time of this BriefRecordItems.

        构建下发时间

        :param schedule_time: The schedule_time of this BriefRecordItems.
        :type schedule_time: str
        """
        self._schedule_time = schedule_time

    @property
    def queued_time(self):
        r"""Gets the queued_time of this BriefRecordItems.

        构建排队耗时

        :return: The queued_time of this BriefRecordItems.
        :rtype: str
        """
        return self._queued_time

    @queued_time.setter
    def queued_time(self, queued_time):
        r"""Sets the queued_time of this BriefRecordItems.

        构建排队耗时

        :param queued_time: The queued_time of this BriefRecordItems.
        :type queued_time: str
        """
        self._queued_time = queued_time

    @property
    def start_time(self):
        r"""Gets the start_time of this BriefRecordItems.

        开始时间

        :return: The start_time of this BriefRecordItems.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this BriefRecordItems.

        开始时间

        :param start_time: The start_time of this BriefRecordItems.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def finish_time(self):
        r"""Gets the finish_time of this BriefRecordItems.

        结束时间

        :return: The finish_time of this BriefRecordItems.
        :rtype: str
        """
        return self._finish_time

    @finish_time.setter
    def finish_time(self, finish_time):
        r"""Sets the finish_time of this BriefRecordItems.

        结束时间

        :param finish_time: The finish_time of this BriefRecordItems.
        :type finish_time: str
        """
        self._finish_time = finish_time

    @property
    def build_duration(self):
        r"""Gets the build_duration of this BriefRecordItems.

        子任务构建耗时

        :return: The build_duration of this BriefRecordItems.
        :rtype: int
        """
        return self._build_duration

    @build_duration.setter
    def build_duration(self, build_duration):
        r"""Sets the build_duration of this BriefRecordItems.

        子任务构建耗时

        :param build_duration: The build_duration of this BriefRecordItems.
        :type build_duration: int
        """
        self._build_duration = build_duration

    @property
    def pending_duration(self):
        r"""Gets the pending_duration of this BriefRecordItems.

        等待时间

        :return: The pending_duration of this BriefRecordItems.
        :rtype: int
        """
        return self._pending_duration

    @pending_duration.setter
    def pending_duration(self, pending_duration):
        r"""Sets the pending_duration of this BriefRecordItems.

        等待时间

        :param pending_duration: The pending_duration of this BriefRecordItems.
        :type pending_duration: int
        """
        self._pending_duration = pending_duration

    @property
    def project_id(self):
        r"""Gets the project_id of this BriefRecordItems.

        所属的项目ID

        :return: The project_id of this BriefRecordItems.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this BriefRecordItems.

        所属的项目ID

        :param project_id: The project_id of this BriefRecordItems.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def build_no(self):
        r"""Gets the build_no of this BriefRecordItems.

        构建任务的构建编号，从1开始，每次构建递增1

        :return: The build_no of this BriefRecordItems.
        :rtype: int
        """
        return self._build_no

    @build_no.setter
    def build_no(self, build_no):
        r"""Sets the build_no of this BriefRecordItems.

        构建任务的构建编号，从1开始，每次构建递增1

        :param build_no: The build_no of this BriefRecordItems.
        :type build_no: int
        """
        self._build_no = build_no

    @property
    def branch(self):
        r"""Gets the branch of this BriefRecordItems.

        代码分支

        :return: The branch of this BriefRecordItems.
        :rtype: str
        """
        return self._branch

    @branch.setter
    def branch(self, branch):
        r"""Sets the branch of this BriefRecordItems.

        代码分支

        :param branch: The branch of this BriefRecordItems.
        :type branch: str
        """
        self._branch = branch

    @property
    def revision(self):
        r"""Gets the revision of this BriefRecordItems.

        commitId

        :return: The revision of this BriefRecordItems.
        :rtype: str
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        r"""Sets the revision of this BriefRecordItems.

        commitId

        :param revision: The revision of this BriefRecordItems.
        :type revision: str
        """
        self._revision = revision

    @property
    def trigger_name(self):
        r"""Gets the trigger_name of this BriefRecordItems.

        触发者名称

        :return: The trigger_name of this BriefRecordItems.
        :rtype: str
        """
        return self._trigger_name

    @trigger_name.setter
    def trigger_name(self, trigger_name):
        r"""Sets the trigger_name of this BriefRecordItems.

        触发者名称

        :param trigger_name: The trigger_name of this BriefRecordItems.
        :type trigger_name: str
        """
        self._trigger_name = trigger_name

    @property
    def daily_build_number(self):
        r"""Gets the daily_build_number of this BriefRecordItems.

        构建编号，每日从1开始

        :return: The daily_build_number of this BriefRecordItems.
        :rtype: str
        """
        return self._daily_build_number

    @daily_build_number.setter
    def daily_build_number(self, daily_build_number):
        r"""Sets the daily_build_number of this BriefRecordItems.

        构建编号，每日从1开始

        :param daily_build_number: The daily_build_number of this BriefRecordItems.
        :type daily_build_number: str
        """
        self._daily_build_number = daily_build_number

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
        if not isinstance(other, BriefRecordItems):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
