# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DashboardDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'create_time': 'datetime',
        'create_user': 'str',
        'data_type': 'str',
        'id': 'str',
        'name': 'str',
        'service_id': 'str',
        'task_ids': 'list[str]',
        'task_type': 'str',
        'update_time': 'datetime',
        'update_user': 'str',
        'view_type': 'str'
    }

    attribute_map = {
        'create_time': 'create_time',
        'create_user': 'create_user',
        'data_type': 'data_type',
        'id': 'id',
        'name': 'name',
        'service_id': 'service_id',
        'task_ids': 'task_ids',
        'task_type': 'task_type',
        'update_time': 'update_time',
        'update_user': 'update_user',
        'view_type': 'view_type'
    }

    def __init__(self, create_time=None, create_user=None, data_type=None, id=None, name=None, service_id=None, task_ids=None, task_type=None, update_time=None, update_user=None, view_type=None):
        """DashboardDto

        The model defined in huaweicloud sdk

        :param create_time: 创建时间
        :type create_time: datetime
        :param create_user: 创建者
        :type create_user: str
        :param data_type: 数据类型：0&#x3D;用例成功率；1&#x3D;用例时长
        :type data_type: str
        :param id: 唯一ID，主键
        :type id: str
        :param name: 看板标题
        :type name: str
        :param service_id: 服务ID
        :type service_id: str
        :param task_ids: 任务ID列表
        :type task_ids: list[str]
        :param task_type: 任务类型，仅支持持续拨测和冒烟测试
        :type task_type: str
        :param update_time: 修改时间
        :type update_time: datetime
        :param update_user: 修改者
        :type update_user: str
        :param view_type: 看板类型：0&#x3D;折线图；1&#x3D;散点图；2&#x3D;饼图
        :type view_type: str
        """
        
        

        self._create_time = None
        self._create_user = None
        self._data_type = None
        self._id = None
        self._name = None
        self._service_id = None
        self._task_ids = None
        self._task_type = None
        self._update_time = None
        self._update_user = None
        self._view_type = None
        self.discriminator = None

        if create_time is not None:
            self.create_time = create_time
        if create_user is not None:
            self.create_user = create_user
        if data_type is not None:
            self.data_type = data_type
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if service_id is not None:
            self.service_id = service_id
        if task_ids is not None:
            self.task_ids = task_ids
        if task_type is not None:
            self.task_type = task_type
        if update_time is not None:
            self.update_time = update_time
        if update_user is not None:
            self.update_user = update_user
        if view_type is not None:
            self.view_type = view_type

    @property
    def create_time(self):
        """Gets the create_time of this DashboardDto.

        创建时间

        :return: The create_time of this DashboardDto.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this DashboardDto.

        创建时间

        :param create_time: The create_time of this DashboardDto.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def create_user(self):
        """Gets the create_user of this DashboardDto.

        创建者

        :return: The create_user of this DashboardDto.
        :rtype: str
        """
        return self._create_user

    @create_user.setter
    def create_user(self, create_user):
        """Sets the create_user of this DashboardDto.

        创建者

        :param create_user: The create_user of this DashboardDto.
        :type create_user: str
        """
        self._create_user = create_user

    @property
    def data_type(self):
        """Gets the data_type of this DashboardDto.

        数据类型：0=用例成功率；1=用例时长

        :return: The data_type of this DashboardDto.
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """Sets the data_type of this DashboardDto.

        数据类型：0=用例成功率；1=用例时长

        :param data_type: The data_type of this DashboardDto.
        :type data_type: str
        """
        self._data_type = data_type

    @property
    def id(self):
        """Gets the id of this DashboardDto.

        唯一ID，主键

        :return: The id of this DashboardDto.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DashboardDto.

        唯一ID，主键

        :param id: The id of this DashboardDto.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this DashboardDto.

        看板标题

        :return: The name of this DashboardDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DashboardDto.

        看板标题

        :param name: The name of this DashboardDto.
        :type name: str
        """
        self._name = name

    @property
    def service_id(self):
        """Gets the service_id of this DashboardDto.

        服务ID

        :return: The service_id of this DashboardDto.
        :rtype: str
        """
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        """Sets the service_id of this DashboardDto.

        服务ID

        :param service_id: The service_id of this DashboardDto.
        :type service_id: str
        """
        self._service_id = service_id

    @property
    def task_ids(self):
        """Gets the task_ids of this DashboardDto.

        任务ID列表

        :return: The task_ids of this DashboardDto.
        :rtype: list[str]
        """
        return self._task_ids

    @task_ids.setter
    def task_ids(self, task_ids):
        """Sets the task_ids of this DashboardDto.

        任务ID列表

        :param task_ids: The task_ids of this DashboardDto.
        :type task_ids: list[str]
        """
        self._task_ids = task_ids

    @property
    def task_type(self):
        """Gets the task_type of this DashboardDto.

        任务类型，仅支持持续拨测和冒烟测试

        :return: The task_type of this DashboardDto.
        :rtype: str
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        """Sets the task_type of this DashboardDto.

        任务类型，仅支持持续拨测和冒烟测试

        :param task_type: The task_type of this DashboardDto.
        :type task_type: str
        """
        self._task_type = task_type

    @property
    def update_time(self):
        """Gets the update_time of this DashboardDto.

        修改时间

        :return: The update_time of this DashboardDto.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this DashboardDto.

        修改时间

        :param update_time: The update_time of this DashboardDto.
        :type update_time: datetime
        """
        self._update_time = update_time

    @property
    def update_user(self):
        """Gets the update_user of this DashboardDto.

        修改者

        :return: The update_user of this DashboardDto.
        :rtype: str
        """
        return self._update_user

    @update_user.setter
    def update_user(self, update_user):
        """Sets the update_user of this DashboardDto.

        修改者

        :param update_user: The update_user of this DashboardDto.
        :type update_user: str
        """
        self._update_user = update_user

    @property
    def view_type(self):
        """Gets the view_type of this DashboardDto.

        看板类型：0=折线图；1=散点图；2=饼图

        :return: The view_type of this DashboardDto.
        :rtype: str
        """
        return self._view_type

    @view_type.setter
    def view_type(self, view_type):
        """Sets the view_type of this DashboardDto.

        看板类型：0=折线图；1=散点图；2=饼图

        :param view_type: The view_type of this DashboardDto.
        :type view_type: str
        """
        self._view_type = view_type

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
        if not isinstance(other, DashboardDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
