# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Job:

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
        'job_name': 'str',
        'job_creator': 'str',
        'user_name': 'str',
        'last_build_time': 'float',
        'health_score': 'int',
        'source_code': 'str',
        'last_build_status': 'str',
        'is_finished': 'bool',
        'disabled': 'bool',
        'favorite': 'bool',
        'is_modify': 'bool',
        'is_delete': 'bool',
        'is_execute': 'bool',
        'is_copy': 'bool',
        'is_forbidden': 'bool',
        'is_view': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'job_name': 'job_name',
        'job_creator': 'job_creator',
        'user_name': 'user_name',
        'last_build_time': 'last_build_time',
        'health_score': 'health_score',
        'source_code': 'source_code',
        'last_build_status': 'last_build_status',
        'is_finished': 'is_finished',
        'disabled': 'disabled',
        'favorite': 'favorite',
        'is_modify': 'is_modify',
        'is_delete': 'is_delete',
        'is_execute': 'is_execute',
        'is_copy': 'is_copy',
        'is_forbidden': 'is_forbidden',
        'is_view': 'is_view'
    }

    def __init__(self, id=None, job_name=None, job_creator=None, user_name=None, last_build_time=None, health_score=None, source_code=None, last_build_status=None, is_finished=None, disabled=None, favorite=None, is_modify=None, is_delete=None, is_execute=None, is_copy=None, is_forbidden=None, is_view=None):
        """Job

        The model defined in huaweicloud sdk

        :param id: 任务ID
        :type id: str
        :param job_name: 任务名称
        :type job_name: str
        :param job_creator: 任务创建者
        :type job_creator: str
        :param user_name: 用户名称
        :type user_name: str
        :param last_build_time: 最新执行时间
        :type last_build_time: float
        :param health_score: 健康分值
        :type health_score: int
        :param source_code: 代码来源
        :type source_code: str
        :param last_build_status: 最新构建状态
        :type last_build_status: str
        :param is_finished: 是否已结束
        :type is_finished: bool
        :param disabled: 是否已禁用
        :type disabled: bool
        :param favorite: 是否已收藏
        :type favorite: bool
        :param is_modify: 是否有修改任务权限
        :type is_modify: bool
        :param is_delete: 是否有删除任务权限
        :type is_delete: bool
        :param is_execute: 是否有执行任务权限
        :type is_execute: bool
        :param is_copy: 是否有复制任务权限
        :type is_copy: bool
        :param is_forbidden: 是否有禁用任务权限
        :type is_forbidden: bool
        :param is_view: 是否有查看任务权限
        :type is_view: bool
        """
        
        

        self._id = None
        self._job_name = None
        self._job_creator = None
        self._user_name = None
        self._last_build_time = None
        self._health_score = None
        self._source_code = None
        self._last_build_status = None
        self._is_finished = None
        self._disabled = None
        self._favorite = None
        self._is_modify = None
        self._is_delete = None
        self._is_execute = None
        self._is_copy = None
        self._is_forbidden = None
        self._is_view = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if job_name is not None:
            self.job_name = job_name
        if job_creator is not None:
            self.job_creator = job_creator
        if user_name is not None:
            self.user_name = user_name
        if last_build_time is not None:
            self.last_build_time = last_build_time
        if health_score is not None:
            self.health_score = health_score
        if source_code is not None:
            self.source_code = source_code
        if last_build_status is not None:
            self.last_build_status = last_build_status
        if is_finished is not None:
            self.is_finished = is_finished
        if disabled is not None:
            self.disabled = disabled
        if favorite is not None:
            self.favorite = favorite
        if is_modify is not None:
            self.is_modify = is_modify
        if is_delete is not None:
            self.is_delete = is_delete
        if is_execute is not None:
            self.is_execute = is_execute
        if is_copy is not None:
            self.is_copy = is_copy
        if is_forbidden is not None:
            self.is_forbidden = is_forbidden
        if is_view is not None:
            self.is_view = is_view

    @property
    def id(self):
        """Gets the id of this Job.

        任务ID

        :return: The id of this Job.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Job.

        任务ID

        :param id: The id of this Job.
        :type id: str
        """
        self._id = id

    @property
    def job_name(self):
        """Gets the job_name of this Job.

        任务名称

        :return: The job_name of this Job.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        """Sets the job_name of this Job.

        任务名称

        :param job_name: The job_name of this Job.
        :type job_name: str
        """
        self._job_name = job_name

    @property
    def job_creator(self):
        """Gets the job_creator of this Job.

        任务创建者

        :return: The job_creator of this Job.
        :rtype: str
        """
        return self._job_creator

    @job_creator.setter
    def job_creator(self, job_creator):
        """Sets the job_creator of this Job.

        任务创建者

        :param job_creator: The job_creator of this Job.
        :type job_creator: str
        """
        self._job_creator = job_creator

    @property
    def user_name(self):
        """Gets the user_name of this Job.

        用户名称

        :return: The user_name of this Job.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this Job.

        用户名称

        :param user_name: The user_name of this Job.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def last_build_time(self):
        """Gets the last_build_time of this Job.

        最新执行时间

        :return: The last_build_time of this Job.
        :rtype: float
        """
        return self._last_build_time

    @last_build_time.setter
    def last_build_time(self, last_build_time):
        """Sets the last_build_time of this Job.

        最新执行时间

        :param last_build_time: The last_build_time of this Job.
        :type last_build_time: float
        """
        self._last_build_time = last_build_time

    @property
    def health_score(self):
        """Gets the health_score of this Job.

        健康分值

        :return: The health_score of this Job.
        :rtype: int
        """
        return self._health_score

    @health_score.setter
    def health_score(self, health_score):
        """Sets the health_score of this Job.

        健康分值

        :param health_score: The health_score of this Job.
        :type health_score: int
        """
        self._health_score = health_score

    @property
    def source_code(self):
        """Gets the source_code of this Job.

        代码来源

        :return: The source_code of this Job.
        :rtype: str
        """
        return self._source_code

    @source_code.setter
    def source_code(self, source_code):
        """Sets the source_code of this Job.

        代码来源

        :param source_code: The source_code of this Job.
        :type source_code: str
        """
        self._source_code = source_code

    @property
    def last_build_status(self):
        """Gets the last_build_status of this Job.

        最新构建状态

        :return: The last_build_status of this Job.
        :rtype: str
        """
        return self._last_build_status

    @last_build_status.setter
    def last_build_status(self, last_build_status):
        """Sets the last_build_status of this Job.

        最新构建状态

        :param last_build_status: The last_build_status of this Job.
        :type last_build_status: str
        """
        self._last_build_status = last_build_status

    @property
    def is_finished(self):
        """Gets the is_finished of this Job.

        是否已结束

        :return: The is_finished of this Job.
        :rtype: bool
        """
        return self._is_finished

    @is_finished.setter
    def is_finished(self, is_finished):
        """Sets the is_finished of this Job.

        是否已结束

        :param is_finished: The is_finished of this Job.
        :type is_finished: bool
        """
        self._is_finished = is_finished

    @property
    def disabled(self):
        """Gets the disabled of this Job.

        是否已禁用

        :return: The disabled of this Job.
        :rtype: bool
        """
        return self._disabled

    @disabled.setter
    def disabled(self, disabled):
        """Sets the disabled of this Job.

        是否已禁用

        :param disabled: The disabled of this Job.
        :type disabled: bool
        """
        self._disabled = disabled

    @property
    def favorite(self):
        """Gets the favorite of this Job.

        是否已收藏

        :return: The favorite of this Job.
        :rtype: bool
        """
        return self._favorite

    @favorite.setter
    def favorite(self, favorite):
        """Sets the favorite of this Job.

        是否已收藏

        :param favorite: The favorite of this Job.
        :type favorite: bool
        """
        self._favorite = favorite

    @property
    def is_modify(self):
        """Gets the is_modify of this Job.

        是否有修改任务权限

        :return: The is_modify of this Job.
        :rtype: bool
        """
        return self._is_modify

    @is_modify.setter
    def is_modify(self, is_modify):
        """Sets the is_modify of this Job.

        是否有修改任务权限

        :param is_modify: The is_modify of this Job.
        :type is_modify: bool
        """
        self._is_modify = is_modify

    @property
    def is_delete(self):
        """Gets the is_delete of this Job.

        是否有删除任务权限

        :return: The is_delete of this Job.
        :rtype: bool
        """
        return self._is_delete

    @is_delete.setter
    def is_delete(self, is_delete):
        """Sets the is_delete of this Job.

        是否有删除任务权限

        :param is_delete: The is_delete of this Job.
        :type is_delete: bool
        """
        self._is_delete = is_delete

    @property
    def is_execute(self):
        """Gets the is_execute of this Job.

        是否有执行任务权限

        :return: The is_execute of this Job.
        :rtype: bool
        """
        return self._is_execute

    @is_execute.setter
    def is_execute(self, is_execute):
        """Sets the is_execute of this Job.

        是否有执行任务权限

        :param is_execute: The is_execute of this Job.
        :type is_execute: bool
        """
        self._is_execute = is_execute

    @property
    def is_copy(self):
        """Gets the is_copy of this Job.

        是否有复制任务权限

        :return: The is_copy of this Job.
        :rtype: bool
        """
        return self._is_copy

    @is_copy.setter
    def is_copy(self, is_copy):
        """Sets the is_copy of this Job.

        是否有复制任务权限

        :param is_copy: The is_copy of this Job.
        :type is_copy: bool
        """
        self._is_copy = is_copy

    @property
    def is_forbidden(self):
        """Gets the is_forbidden of this Job.

        是否有禁用任务权限

        :return: The is_forbidden of this Job.
        :rtype: bool
        """
        return self._is_forbidden

    @is_forbidden.setter
    def is_forbidden(self, is_forbidden):
        """Sets the is_forbidden of this Job.

        是否有禁用任务权限

        :param is_forbidden: The is_forbidden of this Job.
        :type is_forbidden: bool
        """
        self._is_forbidden = is_forbidden

    @property
    def is_view(self):
        """Gets the is_view of this Job.

        是否有查看任务权限

        :return: The is_view of this Job.
        :rtype: bool
        """
        return self._is_view

    @is_view.setter
    def is_view(self, is_view):
        """Sets the is_view of this Job.

        是否有查看任务权限

        :param is_view: The is_view of this Job.
        :type is_view: bool
        """
        self._is_view = is_view

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
        if not isinstance(other, Job):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
