# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowPackageDetailRespTaskDetails:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'deploy_status': 'int',
        'deployed_version': 'int',
        'item_name': 'str',
        'pending_item_id': 'str',
        'pending_version': 'int',
        'script_id': 'str',
        'task_id': 'str',
        'start_job_status': 'int',
        'submit_timestamp': 'int',
        'submit_user_id': 'str',
        'submit_user_name': 'str',
        'task_type': 'int',
        'update_type': 'int'
    }

    attribute_map = {
        'deploy_status': 'deploy_status',
        'deployed_version': 'deployed_version',
        'item_name': 'item_name',
        'pending_item_id': 'pending_item_id',
        'pending_version': 'pending_version',
        'script_id': 'script_id',
        'task_id': 'task_id',
        'start_job_status': 'start_job_status',
        'submit_timestamp': 'submit_timestamp',
        'submit_user_id': 'submit_user_id',
        'submit_user_name': 'submit_user_name',
        'task_type': 'task_type',
        'update_type': 'update_type'
    }

    def __init__(self, deploy_status=None, deployed_version=None, item_name=None, pending_item_id=None, pending_version=None, script_id=None, task_id=None, start_job_status=None, submit_timestamp=None, submit_user_id=None, submit_user_name=None, task_type=None, update_type=None):
        """ShowPackageDetailRespTaskDetails

        The model defined in huaweicloud sdk

        :param deploy_status: 发布状态，1:待审批,2:成功,3:失败, 5:发布中
        :type deploy_status: int
        :param deployed_version: 已发布节点版本
        :type deployed_version: int
        :param item_name: 发布任务名称
        :type item_name: str
        :param pending_item_id: 发布任务ID
        :type pending_item_id: str
        :param pending_version: 节点版本
        :type pending_version: int
        :param script_id: 具体脚本ID
        :type script_id: str
        :param task_id: 作业ID
        :type task_id: str
        :param start_job_status: 作业启动状态，2：成功，3：失败
        :type start_job_status: int
        :param submit_timestamp: 提交时间戳，13位时间戳
        :type submit_timestamp: int
        :param submit_user_id: 提交人id
        :type submit_user_id: str
        :param submit_user_name: 提交人名称
        :type submit_user_name: str
        :param task_type: 任务类型（1-作业，2-脚本，3-资源）
        :type task_type: int
        :param update_type: 变更类型，默认值1，（1-新增，2-修改，3-删除）
        :type update_type: int
        """
        
        

        self._deploy_status = None
        self._deployed_version = None
        self._item_name = None
        self._pending_item_id = None
        self._pending_version = None
        self._script_id = None
        self._task_id = None
        self._start_job_status = None
        self._submit_timestamp = None
        self._submit_user_id = None
        self._submit_user_name = None
        self._task_type = None
        self._update_type = None
        self.discriminator = None

        if deploy_status is not None:
            self.deploy_status = deploy_status
        if deployed_version is not None:
            self.deployed_version = deployed_version
        if item_name is not None:
            self.item_name = item_name
        if pending_item_id is not None:
            self.pending_item_id = pending_item_id
        if pending_version is not None:
            self.pending_version = pending_version
        if script_id is not None:
            self.script_id = script_id
        if task_id is not None:
            self.task_id = task_id
        if start_job_status is not None:
            self.start_job_status = start_job_status
        if submit_timestamp is not None:
            self.submit_timestamp = submit_timestamp
        if submit_user_id is not None:
            self.submit_user_id = submit_user_id
        if submit_user_name is not None:
            self.submit_user_name = submit_user_name
        if task_type is not None:
            self.task_type = task_type
        if update_type is not None:
            self.update_type = update_type

    @property
    def deploy_status(self):
        """Gets the deploy_status of this ShowPackageDetailRespTaskDetails.

        发布状态，1:待审批,2:成功,3:失败, 5:发布中

        :return: The deploy_status of this ShowPackageDetailRespTaskDetails.
        :rtype: int
        """
        return self._deploy_status

    @deploy_status.setter
    def deploy_status(self, deploy_status):
        """Sets the deploy_status of this ShowPackageDetailRespTaskDetails.

        发布状态，1:待审批,2:成功,3:失败, 5:发布中

        :param deploy_status: The deploy_status of this ShowPackageDetailRespTaskDetails.
        :type deploy_status: int
        """
        self._deploy_status = deploy_status

    @property
    def deployed_version(self):
        """Gets the deployed_version of this ShowPackageDetailRespTaskDetails.

        已发布节点版本

        :return: The deployed_version of this ShowPackageDetailRespTaskDetails.
        :rtype: int
        """
        return self._deployed_version

    @deployed_version.setter
    def deployed_version(self, deployed_version):
        """Sets the deployed_version of this ShowPackageDetailRespTaskDetails.

        已发布节点版本

        :param deployed_version: The deployed_version of this ShowPackageDetailRespTaskDetails.
        :type deployed_version: int
        """
        self._deployed_version = deployed_version

    @property
    def item_name(self):
        """Gets the item_name of this ShowPackageDetailRespTaskDetails.

        发布任务名称

        :return: The item_name of this ShowPackageDetailRespTaskDetails.
        :rtype: str
        """
        return self._item_name

    @item_name.setter
    def item_name(self, item_name):
        """Sets the item_name of this ShowPackageDetailRespTaskDetails.

        发布任务名称

        :param item_name: The item_name of this ShowPackageDetailRespTaskDetails.
        :type item_name: str
        """
        self._item_name = item_name

    @property
    def pending_item_id(self):
        """Gets the pending_item_id of this ShowPackageDetailRespTaskDetails.

        发布任务ID

        :return: The pending_item_id of this ShowPackageDetailRespTaskDetails.
        :rtype: str
        """
        return self._pending_item_id

    @pending_item_id.setter
    def pending_item_id(self, pending_item_id):
        """Sets the pending_item_id of this ShowPackageDetailRespTaskDetails.

        发布任务ID

        :param pending_item_id: The pending_item_id of this ShowPackageDetailRespTaskDetails.
        :type pending_item_id: str
        """
        self._pending_item_id = pending_item_id

    @property
    def pending_version(self):
        """Gets the pending_version of this ShowPackageDetailRespTaskDetails.

        节点版本

        :return: The pending_version of this ShowPackageDetailRespTaskDetails.
        :rtype: int
        """
        return self._pending_version

    @pending_version.setter
    def pending_version(self, pending_version):
        """Sets the pending_version of this ShowPackageDetailRespTaskDetails.

        节点版本

        :param pending_version: The pending_version of this ShowPackageDetailRespTaskDetails.
        :type pending_version: int
        """
        self._pending_version = pending_version

    @property
    def script_id(self):
        """Gets the script_id of this ShowPackageDetailRespTaskDetails.

        具体脚本ID

        :return: The script_id of this ShowPackageDetailRespTaskDetails.
        :rtype: str
        """
        return self._script_id

    @script_id.setter
    def script_id(self, script_id):
        """Sets the script_id of this ShowPackageDetailRespTaskDetails.

        具体脚本ID

        :param script_id: The script_id of this ShowPackageDetailRespTaskDetails.
        :type script_id: str
        """
        self._script_id = script_id

    @property
    def task_id(self):
        """Gets the task_id of this ShowPackageDetailRespTaskDetails.

        作业ID

        :return: The task_id of this ShowPackageDetailRespTaskDetails.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this ShowPackageDetailRespTaskDetails.

        作业ID

        :param task_id: The task_id of this ShowPackageDetailRespTaskDetails.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def start_job_status(self):
        """Gets the start_job_status of this ShowPackageDetailRespTaskDetails.

        作业启动状态，2：成功，3：失败

        :return: The start_job_status of this ShowPackageDetailRespTaskDetails.
        :rtype: int
        """
        return self._start_job_status

    @start_job_status.setter
    def start_job_status(self, start_job_status):
        """Sets the start_job_status of this ShowPackageDetailRespTaskDetails.

        作业启动状态，2：成功，3：失败

        :param start_job_status: The start_job_status of this ShowPackageDetailRespTaskDetails.
        :type start_job_status: int
        """
        self._start_job_status = start_job_status

    @property
    def submit_timestamp(self):
        """Gets the submit_timestamp of this ShowPackageDetailRespTaskDetails.

        提交时间戳，13位时间戳

        :return: The submit_timestamp of this ShowPackageDetailRespTaskDetails.
        :rtype: int
        """
        return self._submit_timestamp

    @submit_timestamp.setter
    def submit_timestamp(self, submit_timestamp):
        """Sets the submit_timestamp of this ShowPackageDetailRespTaskDetails.

        提交时间戳，13位时间戳

        :param submit_timestamp: The submit_timestamp of this ShowPackageDetailRespTaskDetails.
        :type submit_timestamp: int
        """
        self._submit_timestamp = submit_timestamp

    @property
    def submit_user_id(self):
        """Gets the submit_user_id of this ShowPackageDetailRespTaskDetails.

        提交人id

        :return: The submit_user_id of this ShowPackageDetailRespTaskDetails.
        :rtype: str
        """
        return self._submit_user_id

    @submit_user_id.setter
    def submit_user_id(self, submit_user_id):
        """Sets the submit_user_id of this ShowPackageDetailRespTaskDetails.

        提交人id

        :param submit_user_id: The submit_user_id of this ShowPackageDetailRespTaskDetails.
        :type submit_user_id: str
        """
        self._submit_user_id = submit_user_id

    @property
    def submit_user_name(self):
        """Gets the submit_user_name of this ShowPackageDetailRespTaskDetails.

        提交人名称

        :return: The submit_user_name of this ShowPackageDetailRespTaskDetails.
        :rtype: str
        """
        return self._submit_user_name

    @submit_user_name.setter
    def submit_user_name(self, submit_user_name):
        """Sets the submit_user_name of this ShowPackageDetailRespTaskDetails.

        提交人名称

        :param submit_user_name: The submit_user_name of this ShowPackageDetailRespTaskDetails.
        :type submit_user_name: str
        """
        self._submit_user_name = submit_user_name

    @property
    def task_type(self):
        """Gets the task_type of this ShowPackageDetailRespTaskDetails.

        任务类型（1-作业，2-脚本，3-资源）

        :return: The task_type of this ShowPackageDetailRespTaskDetails.
        :rtype: int
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        """Sets the task_type of this ShowPackageDetailRespTaskDetails.

        任务类型（1-作业，2-脚本，3-资源）

        :param task_type: The task_type of this ShowPackageDetailRespTaskDetails.
        :type task_type: int
        """
        self._task_type = task_type

    @property
    def update_type(self):
        """Gets the update_type of this ShowPackageDetailRespTaskDetails.

        变更类型，默认值1，（1-新增，2-修改，3-删除）

        :return: The update_type of this ShowPackageDetailRespTaskDetails.
        :rtype: int
        """
        return self._update_type

    @update_type.setter
    def update_type(self, update_type):
        """Sets the update_type of this ShowPackageDetailRespTaskDetails.

        变更类型，默认值1，（1-新增，2-修改，3-删除）

        :param update_type: The update_type of this ShowPackageDetailRespTaskDetails.
        :type update_type: int
        """
        self._update_type = update_type

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
        if not isinstance(other, ShowPackageDetailRespTaskDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
