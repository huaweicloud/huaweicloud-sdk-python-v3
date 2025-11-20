# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MigrateRouteSwitchReqVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'iam_account': 'IamAccount',
        'project_id': 'str',
        'instance_id': 'str',
        'task_id': 'str',
        'switch_route_begin_time': 'str',
        'switch_route_end_time': 'str',
        'is_open_api': 'bool',
        'logic_db_name': 'str'
    }

    attribute_map = {
        'iam_account': 'iam_account',
        'project_id': 'project_id',
        'instance_id': 'instance_id',
        'task_id': 'task_id',
        'switch_route_begin_time': 'switch_route_begin_time',
        'switch_route_end_time': 'switch_route_end_time',
        'is_open_api': 'is_open_api',
        'logic_db_name': 'logic_db_name'
    }

    def __init__(self, iam_account=None, project_id=None, instance_id=None, task_id=None, switch_route_begin_time=None, switch_route_end_time=None, is_open_api=None, logic_db_name=None):
        r"""MigrateRouteSwitchReqVO

        The model defined in huaweicloud sdk

        :param iam_account: 
        :type iam_account: :class:`huaweicloudsdkddm.v1.IamAccount`
        :param project_id: 项目id。
        :type project_id: str
        :param instance_id: 实例id。
        :type instance_id: str
        :param task_id: 任务id。
        :type task_id: str
        :param switch_route_begin_time: 自动切换路由开始时间。
        :type switch_route_begin_time: str
        :param switch_route_end_time: 自动切换路由结束时间。
        :type switch_route_end_time: str
        :param is_open_api: 是否openapi。
        :type is_open_api: bool
        :param logic_db_name: 逻辑库名称。
        :type logic_db_name: str
        """
        
        

        self._iam_account = None
        self._project_id = None
        self._instance_id = None
        self._task_id = None
        self._switch_route_begin_time = None
        self._switch_route_end_time = None
        self._is_open_api = None
        self._logic_db_name = None
        self.discriminator = None

        if iam_account is not None:
            self.iam_account = iam_account
        if project_id is not None:
            self.project_id = project_id
        if instance_id is not None:
            self.instance_id = instance_id
        if task_id is not None:
            self.task_id = task_id
        if switch_route_begin_time is not None:
            self.switch_route_begin_time = switch_route_begin_time
        if switch_route_end_time is not None:
            self.switch_route_end_time = switch_route_end_time
        if is_open_api is not None:
            self.is_open_api = is_open_api
        if logic_db_name is not None:
            self.logic_db_name = logic_db_name

    @property
    def iam_account(self):
        r"""Gets the iam_account of this MigrateRouteSwitchReqVO.

        :return: The iam_account of this MigrateRouteSwitchReqVO.
        :rtype: :class:`huaweicloudsdkddm.v1.IamAccount`
        """
        return self._iam_account

    @iam_account.setter
    def iam_account(self, iam_account):
        r"""Sets the iam_account of this MigrateRouteSwitchReqVO.

        :param iam_account: The iam_account of this MigrateRouteSwitchReqVO.
        :type iam_account: :class:`huaweicloudsdkddm.v1.IamAccount`
        """
        self._iam_account = iam_account

    @property
    def project_id(self):
        r"""Gets the project_id of this MigrateRouteSwitchReqVO.

        项目id。

        :return: The project_id of this MigrateRouteSwitchReqVO.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this MigrateRouteSwitchReqVO.

        项目id。

        :param project_id: The project_id of this MigrateRouteSwitchReqVO.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def instance_id(self):
        r"""Gets the instance_id of this MigrateRouteSwitchReqVO.

        实例id。

        :return: The instance_id of this MigrateRouteSwitchReqVO.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this MigrateRouteSwitchReqVO.

        实例id。

        :param instance_id: The instance_id of this MigrateRouteSwitchReqVO.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def task_id(self):
        r"""Gets the task_id of this MigrateRouteSwitchReqVO.

        任务id。

        :return: The task_id of this MigrateRouteSwitchReqVO.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this MigrateRouteSwitchReqVO.

        任务id。

        :param task_id: The task_id of this MigrateRouteSwitchReqVO.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def switch_route_begin_time(self):
        r"""Gets the switch_route_begin_time of this MigrateRouteSwitchReqVO.

        自动切换路由开始时间。

        :return: The switch_route_begin_time of this MigrateRouteSwitchReqVO.
        :rtype: str
        """
        return self._switch_route_begin_time

    @switch_route_begin_time.setter
    def switch_route_begin_time(self, switch_route_begin_time):
        r"""Sets the switch_route_begin_time of this MigrateRouteSwitchReqVO.

        自动切换路由开始时间。

        :param switch_route_begin_time: The switch_route_begin_time of this MigrateRouteSwitchReqVO.
        :type switch_route_begin_time: str
        """
        self._switch_route_begin_time = switch_route_begin_time

    @property
    def switch_route_end_time(self):
        r"""Gets the switch_route_end_time of this MigrateRouteSwitchReqVO.

        自动切换路由结束时间。

        :return: The switch_route_end_time of this MigrateRouteSwitchReqVO.
        :rtype: str
        """
        return self._switch_route_end_time

    @switch_route_end_time.setter
    def switch_route_end_time(self, switch_route_end_time):
        r"""Sets the switch_route_end_time of this MigrateRouteSwitchReqVO.

        自动切换路由结束时间。

        :param switch_route_end_time: The switch_route_end_time of this MigrateRouteSwitchReqVO.
        :type switch_route_end_time: str
        """
        self._switch_route_end_time = switch_route_end_time

    @property
    def is_open_api(self):
        r"""Gets the is_open_api of this MigrateRouteSwitchReqVO.

        是否openapi。

        :return: The is_open_api of this MigrateRouteSwitchReqVO.
        :rtype: bool
        """
        return self._is_open_api

    @is_open_api.setter
    def is_open_api(self, is_open_api):
        r"""Sets the is_open_api of this MigrateRouteSwitchReqVO.

        是否openapi。

        :param is_open_api: The is_open_api of this MigrateRouteSwitchReqVO.
        :type is_open_api: bool
        """
        self._is_open_api = is_open_api

    @property
    def logic_db_name(self):
        r"""Gets the logic_db_name of this MigrateRouteSwitchReqVO.

        逻辑库名称。

        :return: The logic_db_name of this MigrateRouteSwitchReqVO.
        :rtype: str
        """
        return self._logic_db_name

    @logic_db_name.setter
    def logic_db_name(self, logic_db_name):
        r"""Sets the logic_db_name of this MigrateRouteSwitchReqVO.

        逻辑库名称。

        :param logic_db_name: The logic_db_name of this MigrateRouteSwitchReqVO.
        :type logic_db_name: str
        """
        self._logic_db_name = logic_db_name

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, MigrateRouteSwitchReqVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
