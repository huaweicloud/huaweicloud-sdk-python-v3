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
        'job_type': 'str',
        'from_connector_name': 'str',
        'to_config_values': 'ConfigValues',
        'to_link_name': 'str',
        'driver_config_values': 'ConfigValues',
        'from_config_values': 'ConfigValues',
        'to_connector_name': 'str',
        'name': 'str',
        'from_link_name': 'str',
        'creation_user': 'str',
        'creation_date': 'int',
        'update_date': 'int',
        'update_user': 'str',
        'status': 'str'
    }

    attribute_map = {
        'job_type': 'job_type',
        'from_connector_name': 'from-connector-name',
        'to_config_values': 'to-config-values',
        'to_link_name': 'to-link-name',
        'driver_config_values': 'driver-config-values',
        'from_config_values': 'from-config-values',
        'to_connector_name': 'to-connector-name',
        'name': 'name',
        'from_link_name': 'from-link-name',
        'creation_user': 'creation-user',
        'creation_date': 'creation-date',
        'update_date': 'update-date',
        'update_user': 'update-user',
        'status': 'status'
    }

    def __init__(self, job_type=None, from_connector_name=None, to_config_values=None, to_link_name=None, driver_config_values=None, from_config_values=None, to_connector_name=None, name=None, from_link_name=None, creation_user=None, creation_date=None, update_date=None, update_user=None, status=None):
        """Job - a model defined in huaweicloud sdk"""
        
        

        self._job_type = None
        self._from_connector_name = None
        self._to_config_values = None
        self._to_link_name = None
        self._driver_config_values = None
        self._from_config_values = None
        self._to_connector_name = None
        self._name = None
        self._from_link_name = None
        self._creation_user = None
        self._creation_date = None
        self._update_date = None
        self._update_user = None
        self._status = None
        self.discriminator = None

        if job_type is not None:
            self.job_type = job_type
        if from_connector_name is not None:
            self.from_connector_name = from_connector_name
        if to_config_values is not None:
            self.to_config_values = to_config_values
        if to_link_name is not None:
            self.to_link_name = to_link_name
        if driver_config_values is not None:
            self.driver_config_values = driver_config_values
        if from_config_values is not None:
            self.from_config_values = from_config_values
        if to_connector_name is not None:
            self.to_connector_name = to_connector_name
        if name is not None:
            self.name = name
        if from_link_name is not None:
            self.from_link_name = from_link_name
        if creation_user is not None:
            self.creation_user = creation_user
        if creation_date is not None:
            self.creation_date = creation_date
        if update_date is not None:
            self.update_date = update_date
        if update_user is not None:
            self.update_user = update_user
        if status is not None:
            self.status = status

    @property
    def job_type(self):
        """Gets the job_type of this Job.

        作业类型： - NORMAL_JOB：表/文件迁移。 - BATCH_JOB：整库迁移。 - SCENARIO_JOB：场景迁移。

        :return: The job_type of this Job.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        """Sets the job_type of this Job.

        作业类型： - NORMAL_JOB：表/文件迁移。 - BATCH_JOB：整库迁移。 - SCENARIO_JOB：场景迁移。

        :param job_type: The job_type of this Job.
        :type: str
        """
        self._job_type = job_type

    @property
    def from_connector_name(self):
        """Gets the from_connector_name of this Job.

        源端连接类型

        :return: The from_connector_name of this Job.
        :rtype: str
        """
        return self._from_connector_name

    @from_connector_name.setter
    def from_connector_name(self, from_connector_name):
        """Sets the from_connector_name of this Job.

        源端连接类型

        :param from_connector_name: The from_connector_name of this Job.
        :type: str
        """
        self._from_connector_name = from_connector_name

    @property
    def to_config_values(self):
        """Gets the to_config_values of this Job.


        :return: The to_config_values of this Job.
        :rtype: ConfigValues
        """
        return self._to_config_values

    @to_config_values.setter
    def to_config_values(self, to_config_values):
        """Sets the to_config_values of this Job.


        :param to_config_values: The to_config_values of this Job.
        :type: ConfigValues
        """
        self._to_config_values = to_config_values

    @property
    def to_link_name(self):
        """Gets the to_link_name of this Job.

        目的端连接名称

        :return: The to_link_name of this Job.
        :rtype: str
        """
        return self._to_link_name

    @to_link_name.setter
    def to_link_name(self, to_link_name):
        """Sets the to_link_name of this Job.

        目的端连接名称

        :param to_link_name: The to_link_name of this Job.
        :type: str
        """
        self._to_link_name = to_link_name

    @property
    def driver_config_values(self):
        """Gets the driver_config_values of this Job.


        :return: The driver_config_values of this Job.
        :rtype: ConfigValues
        """
        return self._driver_config_values

    @driver_config_values.setter
    def driver_config_values(self, driver_config_values):
        """Sets the driver_config_values of this Job.


        :param driver_config_values: The driver_config_values of this Job.
        :type: ConfigValues
        """
        self._driver_config_values = driver_config_values

    @property
    def from_config_values(self):
        """Gets the from_config_values of this Job.


        :return: The from_config_values of this Job.
        :rtype: ConfigValues
        """
        return self._from_config_values

    @from_config_values.setter
    def from_config_values(self, from_config_values):
        """Sets the from_config_values of this Job.


        :param from_config_values: The from_config_values of this Job.
        :type: ConfigValues
        """
        self._from_config_values = from_config_values

    @property
    def to_connector_name(self):
        """Gets the to_connector_name of this Job.

        目的端连接类型

        :return: The to_connector_name of this Job.
        :rtype: str
        """
        return self._to_connector_name

    @to_connector_name.setter
    def to_connector_name(self, to_connector_name):
        """Sets the to_connector_name of this Job.

        目的端连接类型

        :param to_connector_name: The to_connector_name of this Job.
        :type: str
        """
        self._to_connector_name = to_connector_name

    @property
    def name(self):
        """Gets the name of this Job.

        作业名称，长度在1到240个字符之间

        :return: The name of this Job.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Job.

        作业名称，长度在1到240个字符之间

        :param name: The name of this Job.
        :type: str
        """
        self._name = name

    @property
    def from_link_name(self):
        """Gets the from_link_name of this Job.

        源连接名称

        :return: The from_link_name of this Job.
        :rtype: str
        """
        return self._from_link_name

    @from_link_name.setter
    def from_link_name(self, from_link_name):
        """Sets the from_link_name of this Job.

        源连接名称

        :param from_link_name: The from_link_name of this Job.
        :type: str
        """
        self._from_link_name = from_link_name

    @property
    def creation_user(self):
        """Gets the creation_user of this Job.

        创建的用户。

        :return: The creation_user of this Job.
        :rtype: str
        """
        return self._creation_user

    @creation_user.setter
    def creation_user(self, creation_user):
        """Sets the creation_user of this Job.

        创建的用户。

        :param creation_user: The creation_user of this Job.
        :type: str
        """
        self._creation_user = creation_user

    @property
    def creation_date(self):
        """Gets the creation_date of this Job.

        作业创建的时间，单位：毫秒。

        :return: The creation_date of this Job.
        :rtype: int
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this Job.

        作业创建的时间，单位：毫秒。

        :param creation_date: The creation_date of this Job.
        :type: int
        """
        self._creation_date = creation_date

    @property
    def update_date(self):
        """Gets the update_date of this Job.

        作业最后更新的时间，单位：毫秒。

        :return: The update_date of this Job.
        :rtype: int
        """
        return self._update_date

    @update_date.setter
    def update_date(self, update_date):
        """Sets the update_date of this Job.

        作业最后更新的时间，单位：毫秒。

        :param update_date: The update_date of this Job.
        :type: int
        """
        self._update_date = update_date

    @property
    def update_user(self):
        """Gets the update_user of this Job.

        作业最后更新的用户。

        :return: The update_user of this Job.
        :rtype: str
        """
        return self._update_user

    @update_user.setter
    def update_user(self, update_user):
        """Sets the update_user of this Job.

        作业最后更新的用户。

        :param update_user: The update_user of this Job.
        :type: str
        """
        self._update_user = update_user

    @property
    def status(self):
        """Gets the status of this Job.

        作业最后的执行状态： - BOOTING：启动中。 - RUNNING：运行中。 - SUCCEEDED：成功。 - FAILED：失败。 - NEW：未被执行。

        :return: The status of this Job.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Job.

        作业最后的执行状态： - BOOTING：启动中。 - RUNNING：运行中。 - SUCCEEDED：成功。 - FAILED：失败。 - NEW：未被执行。

        :param status: The status of this Job.
        :type: str
        """
        self._status = status

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
