# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AutoHandlerAlarmRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'task_type': 'str',
        'associated_task_id': 'str',
        'associated_task_type': 'str',
        'associated_task_name': 'str',
        'associated_task_enterprise_project_id': 'str',
        'runbook_instance_mode': 'str',
        'input_param': 'dict(str, str)',
        'target_instances': 'list[AlarmScheduleInstance]',
        'region_id': 'str',
        'sub_task_info': 'SubTaskInfoDTO'
    }

    attribute_map = {
        'task_type': 'task_type',
        'associated_task_id': 'associated_task_id',
        'associated_task_type': 'associated_task_type',
        'associated_task_name': 'associated_task_name',
        'associated_task_enterprise_project_id': 'associated_task_enterprise_project_id',
        'runbook_instance_mode': 'runbook_instance_mode',
        'input_param': 'input_param',
        'target_instances': 'target_instances',
        'region_id': 'region_id',
        'sub_task_info': 'sub_task_info'
    }

    def __init__(self, task_type=None, associated_task_id=None, associated_task_type=None, associated_task_name=None, associated_task_enterprise_project_id=None, runbook_instance_mode=None, input_param=None, target_instances=None, region_id=None, sub_task_info=None):
        r"""AutoHandlerAlarmRequestBody

        The model defined in huaweicloud sdk

        :param task_type: 任务类型
        :type task_type: str
        :param associated_task_id: 关联任务ID（脚本ID/作业ID）
        :type associated_task_id: str
        :param associated_task_type: 关联任务的类型
        :type associated_task_type: str
        :param associated_task_name: 关联任务名称（脚本名称/作业名称）
        :type associated_task_name: str
        :param associated_task_enterprise_project_id: 企业项目ID
        :type associated_task_enterprise_project_id: str
        :param runbook_instance_mode: 作业实例模式
        :type runbook_instance_mode: str
        :param input_param: 执行参数，值为json串
        :type input_param: dict(str, str)
        :param target_instances: 目标实例信息
        :type target_instances: list[:class:`huaweicloudsdkcoc.v1.AlarmScheduleInstance`]
        :param region_id: 区域ID
        :type region_id: str
        :param sub_task_info: 
        :type sub_task_info: :class:`huaweicloudsdkcoc.v1.SubTaskInfoDTO`
        """
        
        

        self._task_type = None
        self._associated_task_id = None
        self._associated_task_type = None
        self._associated_task_name = None
        self._associated_task_enterprise_project_id = None
        self._runbook_instance_mode = None
        self._input_param = None
        self._target_instances = None
        self._region_id = None
        self._sub_task_info = None
        self.discriminator = None

        self.task_type = task_type
        self.associated_task_id = associated_task_id
        self.associated_task_type = associated_task_type
        self.associated_task_name = associated_task_name
        if associated_task_enterprise_project_id is not None:
            self.associated_task_enterprise_project_id = associated_task_enterprise_project_id
        if runbook_instance_mode is not None:
            self.runbook_instance_mode = runbook_instance_mode
        self.input_param = input_param
        if target_instances is not None:
            self.target_instances = target_instances
        if region_id is not None:
            self.region_id = region_id
        if sub_task_info is not None:
            self.sub_task_info = sub_task_info

    @property
    def task_type(self):
        r"""Gets the task_type of this AutoHandlerAlarmRequestBody.

        任务类型

        :return: The task_type of this AutoHandlerAlarmRequestBody.
        :rtype: str
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        r"""Sets the task_type of this AutoHandlerAlarmRequestBody.

        任务类型

        :param task_type: The task_type of this AutoHandlerAlarmRequestBody.
        :type task_type: str
        """
        self._task_type = task_type

    @property
    def associated_task_id(self):
        r"""Gets the associated_task_id of this AutoHandlerAlarmRequestBody.

        关联任务ID（脚本ID/作业ID）

        :return: The associated_task_id of this AutoHandlerAlarmRequestBody.
        :rtype: str
        """
        return self._associated_task_id

    @associated_task_id.setter
    def associated_task_id(self, associated_task_id):
        r"""Sets the associated_task_id of this AutoHandlerAlarmRequestBody.

        关联任务ID（脚本ID/作业ID）

        :param associated_task_id: The associated_task_id of this AutoHandlerAlarmRequestBody.
        :type associated_task_id: str
        """
        self._associated_task_id = associated_task_id

    @property
    def associated_task_type(self):
        r"""Gets the associated_task_type of this AutoHandlerAlarmRequestBody.

        关联任务的类型

        :return: The associated_task_type of this AutoHandlerAlarmRequestBody.
        :rtype: str
        """
        return self._associated_task_type

    @associated_task_type.setter
    def associated_task_type(self, associated_task_type):
        r"""Sets the associated_task_type of this AutoHandlerAlarmRequestBody.

        关联任务的类型

        :param associated_task_type: The associated_task_type of this AutoHandlerAlarmRequestBody.
        :type associated_task_type: str
        """
        self._associated_task_type = associated_task_type

    @property
    def associated_task_name(self):
        r"""Gets the associated_task_name of this AutoHandlerAlarmRequestBody.

        关联任务名称（脚本名称/作业名称）

        :return: The associated_task_name of this AutoHandlerAlarmRequestBody.
        :rtype: str
        """
        return self._associated_task_name

    @associated_task_name.setter
    def associated_task_name(self, associated_task_name):
        r"""Sets the associated_task_name of this AutoHandlerAlarmRequestBody.

        关联任务名称（脚本名称/作业名称）

        :param associated_task_name: The associated_task_name of this AutoHandlerAlarmRequestBody.
        :type associated_task_name: str
        """
        self._associated_task_name = associated_task_name

    @property
    def associated_task_enterprise_project_id(self):
        r"""Gets the associated_task_enterprise_project_id of this AutoHandlerAlarmRequestBody.

        企业项目ID

        :return: The associated_task_enterprise_project_id of this AutoHandlerAlarmRequestBody.
        :rtype: str
        """
        return self._associated_task_enterprise_project_id

    @associated_task_enterprise_project_id.setter
    def associated_task_enterprise_project_id(self, associated_task_enterprise_project_id):
        r"""Sets the associated_task_enterprise_project_id of this AutoHandlerAlarmRequestBody.

        企业项目ID

        :param associated_task_enterprise_project_id: The associated_task_enterprise_project_id of this AutoHandlerAlarmRequestBody.
        :type associated_task_enterprise_project_id: str
        """
        self._associated_task_enterprise_project_id = associated_task_enterprise_project_id

    @property
    def runbook_instance_mode(self):
        r"""Gets the runbook_instance_mode of this AutoHandlerAlarmRequestBody.

        作业实例模式

        :return: The runbook_instance_mode of this AutoHandlerAlarmRequestBody.
        :rtype: str
        """
        return self._runbook_instance_mode

    @runbook_instance_mode.setter
    def runbook_instance_mode(self, runbook_instance_mode):
        r"""Sets the runbook_instance_mode of this AutoHandlerAlarmRequestBody.

        作业实例模式

        :param runbook_instance_mode: The runbook_instance_mode of this AutoHandlerAlarmRequestBody.
        :type runbook_instance_mode: str
        """
        self._runbook_instance_mode = runbook_instance_mode

    @property
    def input_param(self):
        r"""Gets the input_param of this AutoHandlerAlarmRequestBody.

        执行参数，值为json串

        :return: The input_param of this AutoHandlerAlarmRequestBody.
        :rtype: dict(str, str)
        """
        return self._input_param

    @input_param.setter
    def input_param(self, input_param):
        r"""Sets the input_param of this AutoHandlerAlarmRequestBody.

        执行参数，值为json串

        :param input_param: The input_param of this AutoHandlerAlarmRequestBody.
        :type input_param: dict(str, str)
        """
        self._input_param = input_param

    @property
    def target_instances(self):
        r"""Gets the target_instances of this AutoHandlerAlarmRequestBody.

        目标实例信息

        :return: The target_instances of this AutoHandlerAlarmRequestBody.
        :rtype: list[:class:`huaweicloudsdkcoc.v1.AlarmScheduleInstance`]
        """
        return self._target_instances

    @target_instances.setter
    def target_instances(self, target_instances):
        r"""Sets the target_instances of this AutoHandlerAlarmRequestBody.

        目标实例信息

        :param target_instances: The target_instances of this AutoHandlerAlarmRequestBody.
        :type target_instances: list[:class:`huaweicloudsdkcoc.v1.AlarmScheduleInstance`]
        """
        self._target_instances = target_instances

    @property
    def region_id(self):
        r"""Gets the region_id of this AutoHandlerAlarmRequestBody.

        区域ID

        :return: The region_id of this AutoHandlerAlarmRequestBody.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this AutoHandlerAlarmRequestBody.

        区域ID

        :param region_id: The region_id of this AutoHandlerAlarmRequestBody.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def sub_task_info(self):
        r"""Gets the sub_task_info of this AutoHandlerAlarmRequestBody.

        :return: The sub_task_info of this AutoHandlerAlarmRequestBody.
        :rtype: :class:`huaweicloudsdkcoc.v1.SubTaskInfoDTO`
        """
        return self._sub_task_info

    @sub_task_info.setter
    def sub_task_info(self, sub_task_info):
        r"""Sets the sub_task_info of this AutoHandlerAlarmRequestBody.

        :param sub_task_info: The sub_task_info of this AutoHandlerAlarmRequestBody.
        :type sub_task_info: :class:`huaweicloudsdkcoc.v1.SubTaskInfoDTO`
        """
        self._sub_task_info = sub_task_info

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
        if not isinstance(other, AutoHandlerAlarmRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
