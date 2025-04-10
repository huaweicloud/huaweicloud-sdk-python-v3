# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AppInstallJob:

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
        'app_id': 'str',
        'app_name': 'str',
        'app_version': 'str',
        'instance_id': 'str',
        'instance_sid': 'str',
        'instance_name': 'str',
        'operator': 'str',
        'target': 'str',
        'job_status': 'JobStatus',
        'error_message': 'str',
        'create_time': 'datetime',
        'update_time': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'app_id': 'app_id',
        'app_name': 'app_name',
        'app_version': 'app_version',
        'instance_id': 'instance_id',
        'instance_sid': 'instance_sid',
        'instance_name': 'instance_name',
        'operator': 'operator',
        'target': 'target',
        'job_status': 'job_status',
        'error_message': 'error_message',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, id=None, app_id=None, app_name=None, app_version=None, instance_id=None, instance_sid=None, instance_name=None, operator=None, target=None, job_status=None, error_message=None, create_time=None, update_time=None):
        r"""AppInstallJob

        The model defined in huaweicloud sdk

        :param id: 任务ID。
        :type id: str
        :param app_id: 应用ID。
        :type app_id: str
        :param app_name: 应用名称。
        :type app_name: str
        :param app_version: 应用版本。
        :type app_version: str
        :param instance_id: 实例ID(桌面或者云应用实例的资源ID)。
        :type instance_id: str
        :param instance_sid: 实例的sid。
        :type instance_sid: str
        :param instance_name: 实例名称。
        :type instance_name: str
        :param operator: 操作用户。
        :type operator: str
        :param target: 目标用户。
        :type target: str
        :param job_status: 
        :type job_status: :class:`huaweicloudsdkworkspace.v2.JobStatus`
        :param error_message: 任务失败时的原因。
        :type error_message: str
        :param create_time: 创建时间。
        :type create_time: datetime
        :param update_time: 更新时间。
        :type update_time: datetime
        """
        
        

        self._id = None
        self._app_id = None
        self._app_name = None
        self._app_version = None
        self._instance_id = None
        self._instance_sid = None
        self._instance_name = None
        self._operator = None
        self._target = None
        self._job_status = None
        self._error_message = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if app_id is not None:
            self.app_id = app_id
        if app_name is not None:
            self.app_name = app_name
        if app_version is not None:
            self.app_version = app_version
        if instance_id is not None:
            self.instance_id = instance_id
        if instance_sid is not None:
            self.instance_sid = instance_sid
        if instance_name is not None:
            self.instance_name = instance_name
        if operator is not None:
            self.operator = operator
        if target is not None:
            self.target = target
        if job_status is not None:
            self.job_status = job_status
        if error_message is not None:
            self.error_message = error_message
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def id(self):
        r"""Gets the id of this AppInstallJob.

        任务ID。

        :return: The id of this AppInstallJob.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this AppInstallJob.

        任务ID。

        :param id: The id of this AppInstallJob.
        :type id: str
        """
        self._id = id

    @property
    def app_id(self):
        r"""Gets the app_id of this AppInstallJob.

        应用ID。

        :return: The app_id of this AppInstallJob.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        r"""Sets the app_id of this AppInstallJob.

        应用ID。

        :param app_id: The app_id of this AppInstallJob.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def app_name(self):
        r"""Gets the app_name of this AppInstallJob.

        应用名称。

        :return: The app_name of this AppInstallJob.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        r"""Sets the app_name of this AppInstallJob.

        应用名称。

        :param app_name: The app_name of this AppInstallJob.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def app_version(self):
        r"""Gets the app_version of this AppInstallJob.

        应用版本。

        :return: The app_version of this AppInstallJob.
        :rtype: str
        """
        return self._app_version

    @app_version.setter
    def app_version(self, app_version):
        r"""Sets the app_version of this AppInstallJob.

        应用版本。

        :param app_version: The app_version of this AppInstallJob.
        :type app_version: str
        """
        self._app_version = app_version

    @property
    def instance_id(self):
        r"""Gets the instance_id of this AppInstallJob.

        实例ID(桌面或者云应用实例的资源ID)。

        :return: The instance_id of this AppInstallJob.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this AppInstallJob.

        实例ID(桌面或者云应用实例的资源ID)。

        :param instance_id: The instance_id of this AppInstallJob.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def instance_sid(self):
        r"""Gets the instance_sid of this AppInstallJob.

        实例的sid。

        :return: The instance_sid of this AppInstallJob.
        :rtype: str
        """
        return self._instance_sid

    @instance_sid.setter
    def instance_sid(self, instance_sid):
        r"""Sets the instance_sid of this AppInstallJob.

        实例的sid。

        :param instance_sid: The instance_sid of this AppInstallJob.
        :type instance_sid: str
        """
        self._instance_sid = instance_sid

    @property
    def instance_name(self):
        r"""Gets the instance_name of this AppInstallJob.

        实例名称。

        :return: The instance_name of this AppInstallJob.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        r"""Sets the instance_name of this AppInstallJob.

        实例名称。

        :param instance_name: The instance_name of this AppInstallJob.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def operator(self):
        r"""Gets the operator of this AppInstallJob.

        操作用户。

        :return: The operator of this AppInstallJob.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        r"""Sets the operator of this AppInstallJob.

        操作用户。

        :param operator: The operator of this AppInstallJob.
        :type operator: str
        """
        self._operator = operator

    @property
    def target(self):
        r"""Gets the target of this AppInstallJob.

        目标用户。

        :return: The target of this AppInstallJob.
        :rtype: str
        """
        return self._target

    @target.setter
    def target(self, target):
        r"""Sets the target of this AppInstallJob.

        目标用户。

        :param target: The target of this AppInstallJob.
        :type target: str
        """
        self._target = target

    @property
    def job_status(self):
        r"""Gets the job_status of this AppInstallJob.

        :return: The job_status of this AppInstallJob.
        :rtype: :class:`huaweicloudsdkworkspace.v2.JobStatus`
        """
        return self._job_status

    @job_status.setter
    def job_status(self, job_status):
        r"""Sets the job_status of this AppInstallJob.

        :param job_status: The job_status of this AppInstallJob.
        :type job_status: :class:`huaweicloudsdkworkspace.v2.JobStatus`
        """
        self._job_status = job_status

    @property
    def error_message(self):
        r"""Gets the error_message of this AppInstallJob.

        任务失败时的原因。

        :return: The error_message of this AppInstallJob.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        r"""Sets the error_message of this AppInstallJob.

        任务失败时的原因。

        :param error_message: The error_message of this AppInstallJob.
        :type error_message: str
        """
        self._error_message = error_message

    @property
    def create_time(self):
        r"""Gets the create_time of this AppInstallJob.

        创建时间。

        :return: The create_time of this AppInstallJob.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this AppInstallJob.

        创建时间。

        :param create_time: The create_time of this AppInstallJob.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this AppInstallJob.

        更新时间。

        :return: The update_time of this AppInstallJob.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this AppInstallJob.

        更新时间。

        :param update_time: The update_time of this AppInstallJob.
        :type update_time: datetime
        """
        self._update_time = update_time

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
        if not isinstance(other, AppInstallJob):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
