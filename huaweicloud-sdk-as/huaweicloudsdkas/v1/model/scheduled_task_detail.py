# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ScheduledTaskDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'task_id': 'str',
        'scaling_group_id': 'str',
        'name': 'str',
        'scheduled_policy': 'ScheduledTaskPolicy',
        'instance_number': 'IntegerRange',
        'create_time': 'str',
        'tenant_id': 'str',
        'domain_id': 'str',
        'update_time': 'str'
    }

    attribute_map = {
        'task_id': 'task_id',
        'scaling_group_id': 'scaling_group_id',
        'name': 'name',
        'scheduled_policy': 'scheduled_policy',
        'instance_number': 'instance_number',
        'create_time': 'create_time',
        'tenant_id': 'tenant_id',
        'domain_id': 'domain_id',
        'update_time': 'update_time'
    }

    def __init__(self, task_id=None, scaling_group_id=None, name=None, scheduled_policy=None, instance_number=None, create_time=None, tenant_id=None, domain_id=None, update_time=None):
        """ScheduledTaskDetail

        The model defined in huaweicloud sdk

        :param task_id: 计划任务ID
        :type task_id: str
        :param scaling_group_id: 伸缩组ID
        :type scaling_group_id: str
        :param name: 名称
        :type name: str
        :param scheduled_policy: 
        :type scheduled_policy: :class:`huaweicloudsdkas.v1.ScheduledTaskPolicy`
        :param instance_number: 
        :type instance_number: :class:`huaweicloudsdkas.v1.IntegerRange`
        :param create_time: 创建时间
        :type create_time: str
        :param tenant_id: 租户ID
        :type tenant_id: str
        :param domain_id: 账号ID
        :type domain_id: str
        :param update_time: 更新时间
        :type update_time: str
        """
        
        

        self._task_id = None
        self._scaling_group_id = None
        self._name = None
        self._scheduled_policy = None
        self._instance_number = None
        self._create_time = None
        self._tenant_id = None
        self._domain_id = None
        self._update_time = None
        self.discriminator = None

        if task_id is not None:
            self.task_id = task_id
        if scaling_group_id is not None:
            self.scaling_group_id = scaling_group_id
        if name is not None:
            self.name = name
        if scheduled_policy is not None:
            self.scheduled_policy = scheduled_policy
        if instance_number is not None:
            self.instance_number = instance_number
        if create_time is not None:
            self.create_time = create_time
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if domain_id is not None:
            self.domain_id = domain_id
        if update_time is not None:
            self.update_time = update_time

    @property
    def task_id(self):
        """Gets the task_id of this ScheduledTaskDetail.

        计划任务ID

        :return: The task_id of this ScheduledTaskDetail.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this ScheduledTaskDetail.

        计划任务ID

        :param task_id: The task_id of this ScheduledTaskDetail.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def scaling_group_id(self):
        """Gets the scaling_group_id of this ScheduledTaskDetail.

        伸缩组ID

        :return: The scaling_group_id of this ScheduledTaskDetail.
        :rtype: str
        """
        return self._scaling_group_id

    @scaling_group_id.setter
    def scaling_group_id(self, scaling_group_id):
        """Sets the scaling_group_id of this ScheduledTaskDetail.

        伸缩组ID

        :param scaling_group_id: The scaling_group_id of this ScheduledTaskDetail.
        :type scaling_group_id: str
        """
        self._scaling_group_id = scaling_group_id

    @property
    def name(self):
        """Gets the name of this ScheduledTaskDetail.

        名称

        :return: The name of this ScheduledTaskDetail.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ScheduledTaskDetail.

        名称

        :param name: The name of this ScheduledTaskDetail.
        :type name: str
        """
        self._name = name

    @property
    def scheduled_policy(self):
        """Gets the scheduled_policy of this ScheduledTaskDetail.

        :return: The scheduled_policy of this ScheduledTaskDetail.
        :rtype: :class:`huaweicloudsdkas.v1.ScheduledTaskPolicy`
        """
        return self._scheduled_policy

    @scheduled_policy.setter
    def scheduled_policy(self, scheduled_policy):
        """Sets the scheduled_policy of this ScheduledTaskDetail.

        :param scheduled_policy: The scheduled_policy of this ScheduledTaskDetail.
        :type scheduled_policy: :class:`huaweicloudsdkas.v1.ScheduledTaskPolicy`
        """
        self._scheduled_policy = scheduled_policy

    @property
    def instance_number(self):
        """Gets the instance_number of this ScheduledTaskDetail.

        :return: The instance_number of this ScheduledTaskDetail.
        :rtype: :class:`huaweicloudsdkas.v1.IntegerRange`
        """
        return self._instance_number

    @instance_number.setter
    def instance_number(self, instance_number):
        """Sets the instance_number of this ScheduledTaskDetail.

        :param instance_number: The instance_number of this ScheduledTaskDetail.
        :type instance_number: :class:`huaweicloudsdkas.v1.IntegerRange`
        """
        self._instance_number = instance_number

    @property
    def create_time(self):
        """Gets the create_time of this ScheduledTaskDetail.

        创建时间

        :return: The create_time of this ScheduledTaskDetail.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ScheduledTaskDetail.

        创建时间

        :param create_time: The create_time of this ScheduledTaskDetail.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def tenant_id(self):
        """Gets the tenant_id of this ScheduledTaskDetail.

        租户ID

        :return: The tenant_id of this ScheduledTaskDetail.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this ScheduledTaskDetail.

        租户ID

        :param tenant_id: The tenant_id of this ScheduledTaskDetail.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def domain_id(self):
        """Gets the domain_id of this ScheduledTaskDetail.

        账号ID

        :return: The domain_id of this ScheduledTaskDetail.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this ScheduledTaskDetail.

        账号ID

        :param domain_id: The domain_id of this ScheduledTaskDetail.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def update_time(self):
        """Gets the update_time of this ScheduledTaskDetail.

        更新时间

        :return: The update_time of this ScheduledTaskDetail.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this ScheduledTaskDetail.

        更新时间

        :param update_time: The update_time of this ScheduledTaskDetail.
        :type update_time: str
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
        if not isinstance(other, ScheduledTaskDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
