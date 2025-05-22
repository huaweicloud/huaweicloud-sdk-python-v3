# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFactoryPendingItemsRespData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'deployed_version': 'int',
        'item_name': 'str',
        'package_flag': 'int',
        'pending_item_id': 'str',
        'pending_version': 'int',
        'project_id': 'str',
        'submit_timestamp': 'int',
        'submit_user_id': 'str',
        'submit_user_name': 'str',
        'task_id': 'str',
        'task_type': 'int',
        'update_type': 'int'
    }

    attribute_map = {
        'deployed_version': 'deployed_version',
        'item_name': 'item_name',
        'package_flag': 'package_flag',
        'pending_item_id': 'pending_item_id',
        'pending_version': 'pending_version',
        'project_id': 'project_id',
        'submit_timestamp': 'submit_timestamp',
        'submit_user_id': 'submit_user_id',
        'submit_user_name': 'submit_user_name',
        'task_id': 'task_id',
        'task_type': 'task_type',
        'update_type': 'update_type'
    }

    def __init__(self, deployed_version=None, item_name=None, package_flag=None, pending_item_id=None, pending_version=None, project_id=None, submit_timestamp=None, submit_user_id=None, submit_user_name=None, task_id=None, task_type=None, update_type=None):
        r"""ListFactoryPendingItemsRespData

        The model defined in huaweicloud sdk

        :param deployed_version: 已发布节点版本
        :type deployed_version: int
        :param item_name: 任务名称
        :type item_name: str
        :param package_flag: 打包状态，0表示未打包。
        :type package_flag: int
        :param pending_item_id: 待发布包ID
        :type pending_item_id: str
        :param pending_version: 待发布包版本
        :type pending_version: int
        :param project_id: 租户id+空间id
        :type project_id: str
        :param submit_timestamp: 提交时间
        :type submit_timestamp: int
        :param submit_user_id: 提交人id
        :type submit_user_id: str
        :param submit_user_name: 提交人名称
        :type submit_user_name: str
        :param task_id: 任务id
        :type task_id: str
        :param task_type: 任务类型，取值为1和2。 1: job 2: script
        :type task_type: int
        :param update_type: 变更类型，取值为1，2和3. 1: 新增 2: 变更 3: 删除
        :type update_type: int
        """
        
        

        self._deployed_version = None
        self._item_name = None
        self._package_flag = None
        self._pending_item_id = None
        self._pending_version = None
        self._project_id = None
        self._submit_timestamp = None
        self._submit_user_id = None
        self._submit_user_name = None
        self._task_id = None
        self._task_type = None
        self._update_type = None
        self.discriminator = None

        if deployed_version is not None:
            self.deployed_version = deployed_version
        if item_name is not None:
            self.item_name = item_name
        if package_flag is not None:
            self.package_flag = package_flag
        if pending_item_id is not None:
            self.pending_item_id = pending_item_id
        if pending_version is not None:
            self.pending_version = pending_version
        if project_id is not None:
            self.project_id = project_id
        if submit_timestamp is not None:
            self.submit_timestamp = submit_timestamp
        if submit_user_id is not None:
            self.submit_user_id = submit_user_id
        if submit_user_name is not None:
            self.submit_user_name = submit_user_name
        if task_id is not None:
            self.task_id = task_id
        if task_type is not None:
            self.task_type = task_type
        if update_type is not None:
            self.update_type = update_type

    @property
    def deployed_version(self):
        r"""Gets the deployed_version of this ListFactoryPendingItemsRespData.

        已发布节点版本

        :return: The deployed_version of this ListFactoryPendingItemsRespData.
        :rtype: int
        """
        return self._deployed_version

    @deployed_version.setter
    def deployed_version(self, deployed_version):
        r"""Sets the deployed_version of this ListFactoryPendingItemsRespData.

        已发布节点版本

        :param deployed_version: The deployed_version of this ListFactoryPendingItemsRespData.
        :type deployed_version: int
        """
        self._deployed_version = deployed_version

    @property
    def item_name(self):
        r"""Gets the item_name of this ListFactoryPendingItemsRespData.

        任务名称

        :return: The item_name of this ListFactoryPendingItemsRespData.
        :rtype: str
        """
        return self._item_name

    @item_name.setter
    def item_name(self, item_name):
        r"""Sets the item_name of this ListFactoryPendingItemsRespData.

        任务名称

        :param item_name: The item_name of this ListFactoryPendingItemsRespData.
        :type item_name: str
        """
        self._item_name = item_name

    @property
    def package_flag(self):
        r"""Gets the package_flag of this ListFactoryPendingItemsRespData.

        打包状态，0表示未打包。

        :return: The package_flag of this ListFactoryPendingItemsRespData.
        :rtype: int
        """
        return self._package_flag

    @package_flag.setter
    def package_flag(self, package_flag):
        r"""Sets the package_flag of this ListFactoryPendingItemsRespData.

        打包状态，0表示未打包。

        :param package_flag: The package_flag of this ListFactoryPendingItemsRespData.
        :type package_flag: int
        """
        self._package_flag = package_flag

    @property
    def pending_item_id(self):
        r"""Gets the pending_item_id of this ListFactoryPendingItemsRespData.

        待发布包ID

        :return: The pending_item_id of this ListFactoryPendingItemsRespData.
        :rtype: str
        """
        return self._pending_item_id

    @pending_item_id.setter
    def pending_item_id(self, pending_item_id):
        r"""Sets the pending_item_id of this ListFactoryPendingItemsRespData.

        待发布包ID

        :param pending_item_id: The pending_item_id of this ListFactoryPendingItemsRespData.
        :type pending_item_id: str
        """
        self._pending_item_id = pending_item_id

    @property
    def pending_version(self):
        r"""Gets the pending_version of this ListFactoryPendingItemsRespData.

        待发布包版本

        :return: The pending_version of this ListFactoryPendingItemsRespData.
        :rtype: int
        """
        return self._pending_version

    @pending_version.setter
    def pending_version(self, pending_version):
        r"""Sets the pending_version of this ListFactoryPendingItemsRespData.

        待发布包版本

        :param pending_version: The pending_version of this ListFactoryPendingItemsRespData.
        :type pending_version: int
        """
        self._pending_version = pending_version

    @property
    def project_id(self):
        r"""Gets the project_id of this ListFactoryPendingItemsRespData.

        租户id+空间id

        :return: The project_id of this ListFactoryPendingItemsRespData.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ListFactoryPendingItemsRespData.

        租户id+空间id

        :param project_id: The project_id of this ListFactoryPendingItemsRespData.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def submit_timestamp(self):
        r"""Gets the submit_timestamp of this ListFactoryPendingItemsRespData.

        提交时间

        :return: The submit_timestamp of this ListFactoryPendingItemsRespData.
        :rtype: int
        """
        return self._submit_timestamp

    @submit_timestamp.setter
    def submit_timestamp(self, submit_timestamp):
        r"""Sets the submit_timestamp of this ListFactoryPendingItemsRespData.

        提交时间

        :param submit_timestamp: The submit_timestamp of this ListFactoryPendingItemsRespData.
        :type submit_timestamp: int
        """
        self._submit_timestamp = submit_timestamp

    @property
    def submit_user_id(self):
        r"""Gets the submit_user_id of this ListFactoryPendingItemsRespData.

        提交人id

        :return: The submit_user_id of this ListFactoryPendingItemsRespData.
        :rtype: str
        """
        return self._submit_user_id

    @submit_user_id.setter
    def submit_user_id(self, submit_user_id):
        r"""Sets the submit_user_id of this ListFactoryPendingItemsRespData.

        提交人id

        :param submit_user_id: The submit_user_id of this ListFactoryPendingItemsRespData.
        :type submit_user_id: str
        """
        self._submit_user_id = submit_user_id

    @property
    def submit_user_name(self):
        r"""Gets the submit_user_name of this ListFactoryPendingItemsRespData.

        提交人名称

        :return: The submit_user_name of this ListFactoryPendingItemsRespData.
        :rtype: str
        """
        return self._submit_user_name

    @submit_user_name.setter
    def submit_user_name(self, submit_user_name):
        r"""Sets the submit_user_name of this ListFactoryPendingItemsRespData.

        提交人名称

        :param submit_user_name: The submit_user_name of this ListFactoryPendingItemsRespData.
        :type submit_user_name: str
        """
        self._submit_user_name = submit_user_name

    @property
    def task_id(self):
        r"""Gets the task_id of this ListFactoryPendingItemsRespData.

        任务id

        :return: The task_id of this ListFactoryPendingItemsRespData.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this ListFactoryPendingItemsRespData.

        任务id

        :param task_id: The task_id of this ListFactoryPendingItemsRespData.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def task_type(self):
        r"""Gets the task_type of this ListFactoryPendingItemsRespData.

        任务类型，取值为1和2。 1: job 2: script

        :return: The task_type of this ListFactoryPendingItemsRespData.
        :rtype: int
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        r"""Sets the task_type of this ListFactoryPendingItemsRespData.

        任务类型，取值为1和2。 1: job 2: script

        :param task_type: The task_type of this ListFactoryPendingItemsRespData.
        :type task_type: int
        """
        self._task_type = task_type

    @property
    def update_type(self):
        r"""Gets the update_type of this ListFactoryPendingItemsRespData.

        变更类型，取值为1，2和3. 1: 新增 2: 变更 3: 删除

        :return: The update_type of this ListFactoryPendingItemsRespData.
        :rtype: int
        """
        return self._update_type

    @update_type.setter
    def update_type(self, update_type):
        r"""Sets the update_type of this ListFactoryPendingItemsRespData.

        变更类型，取值为1，2和3. 1: 新增 2: 变更 3: 删除

        :param update_type: The update_type of this ListFactoryPendingItemsRespData.
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
        if not isinstance(other, ListFactoryPendingItemsRespData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
