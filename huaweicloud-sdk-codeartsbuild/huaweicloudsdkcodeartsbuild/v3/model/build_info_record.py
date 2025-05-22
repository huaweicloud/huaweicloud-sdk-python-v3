# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BuildInfoRecord:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'number': 'int',
        'build_time': 'int',
        'start_time': 'int',
        'job_running_status': 'str',
        'state': 'str',
        'user_id': 'str',
        'executor': 'str',
        'nickname': 'str',
        'daily_build_number': 'str',
        'trigger_type': 'str',
        'cost_time': 'int',
        'commit_id': 'str',
        'commit_info': 'BuildInfoRecordCommitInfo',
        'build_type': 'str',
        'code_branch': 'str',
        'scm_type': 'str',
        'scm_web_url': 'str',
        'commit_detail_url': 'str'
    }

    attribute_map = {
        'number': 'number',
        'build_time': 'build_time',
        'start_time': 'start_time',
        'job_running_status': 'job_running_status',
        'state': 'state',
        'user_id': 'user_id',
        'executor': 'executor',
        'nickname': 'nickname',
        'daily_build_number': 'daily_build_number',
        'trigger_type': 'trigger_type',
        'cost_time': 'cost_time',
        'commit_id': 'commit_id',
        'commit_info': 'commit_info',
        'build_type': 'build_type',
        'code_branch': 'code_branch',
        'scm_type': 'scm_type',
        'scm_web_url': 'scm_web_url',
        'commit_detail_url': 'commit_detail_url'
    }

    def __init__(self, number=None, build_time=None, start_time=None, job_running_status=None, state=None, user_id=None, executor=None, nickname=None, daily_build_number=None, trigger_type=None, cost_time=None, commit_id=None, commit_info=None, build_type=None, code_branch=None, scm_type=None, scm_web_url=None, commit_detail_url=None):
        r"""BuildInfoRecord

        The model defined in huaweicloud sdk

        :param number: 构建编号
        :type number: int
        :param build_time: 执行时间
        :type build_time: int
        :param start_time: 开始时间，时间戳
        :type start_time: int
        :param job_running_status: 运行状态
        :type job_running_status: str
        :param state: 任务状态
        :type state: str
        :param user_id: IAM用户ID
        :type user_id: str
        :param executor: 触发构建用户
        :type executor: str
        :param nickname: 用户名称
        :type nickname: str
        :param daily_build_number: 构建编号，每日从1开始
        :type daily_build_number: str
        :param trigger_type: 触发类型
        :type trigger_type: str
        :param cost_time: 执行时间
        :type cost_time: int
        :param commit_id: 代码提交的commit id
        :type commit_id: str
        :param commit_info: 
        :type commit_info: :class:`huaweicloudsdkcodeartsbuild.v3.BuildInfoRecordCommitInfo`
        :param build_type: 构建类型
        :type build_type: str
        :param code_branch: 代码仓分支
        :type code_branch: str
        :param scm_type: 代码源类型
        :type scm_type: str
        :param scm_web_url: 代码源地址
        :type scm_web_url: str
        :param commit_detail_url: 代码提交记录信息地址（代码源为Repo)
        :type commit_detail_url: str
        """
        
        

        self._number = None
        self._build_time = None
        self._start_time = None
        self._job_running_status = None
        self._state = None
        self._user_id = None
        self._executor = None
        self._nickname = None
        self._daily_build_number = None
        self._trigger_type = None
        self._cost_time = None
        self._commit_id = None
        self._commit_info = None
        self._build_type = None
        self._code_branch = None
        self._scm_type = None
        self._scm_web_url = None
        self._commit_detail_url = None
        self.discriminator = None

        if number is not None:
            self.number = number
        if build_time is not None:
            self.build_time = build_time
        if start_time is not None:
            self.start_time = start_time
        if job_running_status is not None:
            self.job_running_status = job_running_status
        if state is not None:
            self.state = state
        if user_id is not None:
            self.user_id = user_id
        if executor is not None:
            self.executor = executor
        if nickname is not None:
            self.nickname = nickname
        if daily_build_number is not None:
            self.daily_build_number = daily_build_number
        if trigger_type is not None:
            self.trigger_type = trigger_type
        if cost_time is not None:
            self.cost_time = cost_time
        if commit_id is not None:
            self.commit_id = commit_id
        if commit_info is not None:
            self.commit_info = commit_info
        if build_type is not None:
            self.build_type = build_type
        if code_branch is not None:
            self.code_branch = code_branch
        if scm_type is not None:
            self.scm_type = scm_type
        if scm_web_url is not None:
            self.scm_web_url = scm_web_url
        if commit_detail_url is not None:
            self.commit_detail_url = commit_detail_url

    @property
    def number(self):
        r"""Gets the number of this BuildInfoRecord.

        构建编号

        :return: The number of this BuildInfoRecord.
        :rtype: int
        """
        return self._number

    @number.setter
    def number(self, number):
        r"""Sets the number of this BuildInfoRecord.

        构建编号

        :param number: The number of this BuildInfoRecord.
        :type number: int
        """
        self._number = number

    @property
    def build_time(self):
        r"""Gets the build_time of this BuildInfoRecord.

        执行时间

        :return: The build_time of this BuildInfoRecord.
        :rtype: int
        """
        return self._build_time

    @build_time.setter
    def build_time(self, build_time):
        r"""Sets the build_time of this BuildInfoRecord.

        执行时间

        :param build_time: The build_time of this BuildInfoRecord.
        :type build_time: int
        """
        self._build_time = build_time

    @property
    def start_time(self):
        r"""Gets the start_time of this BuildInfoRecord.

        开始时间，时间戳

        :return: The start_time of this BuildInfoRecord.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this BuildInfoRecord.

        开始时间，时间戳

        :param start_time: The start_time of this BuildInfoRecord.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def job_running_status(self):
        r"""Gets the job_running_status of this BuildInfoRecord.

        运行状态

        :return: The job_running_status of this BuildInfoRecord.
        :rtype: str
        """
        return self._job_running_status

    @job_running_status.setter
    def job_running_status(self, job_running_status):
        r"""Sets the job_running_status of this BuildInfoRecord.

        运行状态

        :param job_running_status: The job_running_status of this BuildInfoRecord.
        :type job_running_status: str
        """
        self._job_running_status = job_running_status

    @property
    def state(self):
        r"""Gets the state of this BuildInfoRecord.

        任务状态

        :return: The state of this BuildInfoRecord.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this BuildInfoRecord.

        任务状态

        :param state: The state of this BuildInfoRecord.
        :type state: str
        """
        self._state = state

    @property
    def user_id(self):
        r"""Gets the user_id of this BuildInfoRecord.

        IAM用户ID

        :return: The user_id of this BuildInfoRecord.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this BuildInfoRecord.

        IAM用户ID

        :param user_id: The user_id of this BuildInfoRecord.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def executor(self):
        r"""Gets the executor of this BuildInfoRecord.

        触发构建用户

        :return: The executor of this BuildInfoRecord.
        :rtype: str
        """
        return self._executor

    @executor.setter
    def executor(self, executor):
        r"""Sets the executor of this BuildInfoRecord.

        触发构建用户

        :param executor: The executor of this BuildInfoRecord.
        :type executor: str
        """
        self._executor = executor

    @property
    def nickname(self):
        r"""Gets the nickname of this BuildInfoRecord.

        用户名称

        :return: The nickname of this BuildInfoRecord.
        :rtype: str
        """
        return self._nickname

    @nickname.setter
    def nickname(self, nickname):
        r"""Sets the nickname of this BuildInfoRecord.

        用户名称

        :param nickname: The nickname of this BuildInfoRecord.
        :type nickname: str
        """
        self._nickname = nickname

    @property
    def daily_build_number(self):
        r"""Gets the daily_build_number of this BuildInfoRecord.

        构建编号，每日从1开始

        :return: The daily_build_number of this BuildInfoRecord.
        :rtype: str
        """
        return self._daily_build_number

    @daily_build_number.setter
    def daily_build_number(self, daily_build_number):
        r"""Sets the daily_build_number of this BuildInfoRecord.

        构建编号，每日从1开始

        :param daily_build_number: The daily_build_number of this BuildInfoRecord.
        :type daily_build_number: str
        """
        self._daily_build_number = daily_build_number

    @property
    def trigger_type(self):
        r"""Gets the trigger_type of this BuildInfoRecord.

        触发类型

        :return: The trigger_type of this BuildInfoRecord.
        :rtype: str
        """
        return self._trigger_type

    @trigger_type.setter
    def trigger_type(self, trigger_type):
        r"""Sets the trigger_type of this BuildInfoRecord.

        触发类型

        :param trigger_type: The trigger_type of this BuildInfoRecord.
        :type trigger_type: str
        """
        self._trigger_type = trigger_type

    @property
    def cost_time(self):
        r"""Gets the cost_time of this BuildInfoRecord.

        执行时间

        :return: The cost_time of this BuildInfoRecord.
        :rtype: int
        """
        return self._cost_time

    @cost_time.setter
    def cost_time(self, cost_time):
        r"""Sets the cost_time of this BuildInfoRecord.

        执行时间

        :param cost_time: The cost_time of this BuildInfoRecord.
        :type cost_time: int
        """
        self._cost_time = cost_time

    @property
    def commit_id(self):
        r"""Gets the commit_id of this BuildInfoRecord.

        代码提交的commit id

        :return: The commit_id of this BuildInfoRecord.
        :rtype: str
        """
        return self._commit_id

    @commit_id.setter
    def commit_id(self, commit_id):
        r"""Sets the commit_id of this BuildInfoRecord.

        代码提交的commit id

        :param commit_id: The commit_id of this BuildInfoRecord.
        :type commit_id: str
        """
        self._commit_id = commit_id

    @property
    def commit_info(self):
        r"""Gets the commit_info of this BuildInfoRecord.

        :return: The commit_info of this BuildInfoRecord.
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.BuildInfoRecordCommitInfo`
        """
        return self._commit_info

    @commit_info.setter
    def commit_info(self, commit_info):
        r"""Sets the commit_info of this BuildInfoRecord.

        :param commit_info: The commit_info of this BuildInfoRecord.
        :type commit_info: :class:`huaweicloudsdkcodeartsbuild.v3.BuildInfoRecordCommitInfo`
        """
        self._commit_info = commit_info

    @property
    def build_type(self):
        r"""Gets the build_type of this BuildInfoRecord.

        构建类型

        :return: The build_type of this BuildInfoRecord.
        :rtype: str
        """
        return self._build_type

    @build_type.setter
    def build_type(self, build_type):
        r"""Sets the build_type of this BuildInfoRecord.

        构建类型

        :param build_type: The build_type of this BuildInfoRecord.
        :type build_type: str
        """
        self._build_type = build_type

    @property
    def code_branch(self):
        r"""Gets the code_branch of this BuildInfoRecord.

        代码仓分支

        :return: The code_branch of this BuildInfoRecord.
        :rtype: str
        """
        return self._code_branch

    @code_branch.setter
    def code_branch(self, code_branch):
        r"""Sets the code_branch of this BuildInfoRecord.

        代码仓分支

        :param code_branch: The code_branch of this BuildInfoRecord.
        :type code_branch: str
        """
        self._code_branch = code_branch

    @property
    def scm_type(self):
        r"""Gets the scm_type of this BuildInfoRecord.

        代码源类型

        :return: The scm_type of this BuildInfoRecord.
        :rtype: str
        """
        return self._scm_type

    @scm_type.setter
    def scm_type(self, scm_type):
        r"""Sets the scm_type of this BuildInfoRecord.

        代码源类型

        :param scm_type: The scm_type of this BuildInfoRecord.
        :type scm_type: str
        """
        self._scm_type = scm_type

    @property
    def scm_web_url(self):
        r"""Gets the scm_web_url of this BuildInfoRecord.

        代码源地址

        :return: The scm_web_url of this BuildInfoRecord.
        :rtype: str
        """
        return self._scm_web_url

    @scm_web_url.setter
    def scm_web_url(self, scm_web_url):
        r"""Sets the scm_web_url of this BuildInfoRecord.

        代码源地址

        :param scm_web_url: The scm_web_url of this BuildInfoRecord.
        :type scm_web_url: str
        """
        self._scm_web_url = scm_web_url

    @property
    def commit_detail_url(self):
        r"""Gets the commit_detail_url of this BuildInfoRecord.

        代码提交记录信息地址（代码源为Repo)

        :return: The commit_detail_url of this BuildInfoRecord.
        :rtype: str
        """
        return self._commit_detail_url

    @commit_detail_url.setter
    def commit_detail_url(self, commit_detail_url):
        r"""Sets the commit_detail_url of this BuildInfoRecord.

        代码提交记录信息地址（代码源为Repo)

        :param commit_detail_url: The commit_detail_url of this BuildInfoRecord.
        :type commit_detail_url: str
        """
        self._commit_detail_url = commit_detail_url

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
        if not isinstance(other, BuildInfoRecord):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
