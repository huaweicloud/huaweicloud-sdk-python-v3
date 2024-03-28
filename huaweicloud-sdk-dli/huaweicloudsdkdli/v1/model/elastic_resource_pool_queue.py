# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ElasticResourcePoolQueue:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'queue_name': 'str',
        'enterprise_project_id': 'str',
        'queue_type': 'str',
        'queue_scaling_policies': 'list[QueueScalingPolicy]',
        'owner': 'str',
        'create_time': 'int',
        'engine': 'str'
    }

    attribute_map = {
        'queue_name': 'queue_name',
        'enterprise_project_id': 'enterprise_project_id',
        'queue_type': 'queue_type',
        'queue_scaling_policies': 'queue_scaling_policies',
        'owner': 'owner',
        'create_time': 'create_time',
        'engine': 'engine'
    }

    def __init__(self, queue_name=None, enterprise_project_id=None, queue_type=None, queue_scaling_policies=None, owner=None, create_time=None, engine=None):
        """ElasticResourcePoolQueue

        The model defined in huaweicloud sdk

        :param queue_name: 队列名称
        :type queue_name: str
        :param enterprise_project_id: 企业项目ID
        :type enterprise_project_id: str
        :param queue_type: 队列类型
        :type queue_type: str
        :param queue_scaling_policies: 队列扩缩容策略
        :type queue_scaling_policies: list[:class:`huaweicloudsdkdli.v1.QueueScalingPolicy`]
        :param owner: 所有者
        :type owner: str
        :param create_time: 创建时间
        :type create_time: int
        :param engine: 引擎类型
        :type engine: str
        """
        
        

        self._queue_name = None
        self._enterprise_project_id = None
        self._queue_type = None
        self._queue_scaling_policies = None
        self._owner = None
        self._create_time = None
        self._engine = None
        self.discriminator = None

        if queue_name is not None:
            self.queue_name = queue_name
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if queue_type is not None:
            self.queue_type = queue_type
        if queue_scaling_policies is not None:
            self.queue_scaling_policies = queue_scaling_policies
        if owner is not None:
            self.owner = owner
        if create_time is not None:
            self.create_time = create_time
        if engine is not None:
            self.engine = engine

    @property
    def queue_name(self):
        """Gets the queue_name of this ElasticResourcePoolQueue.

        队列名称

        :return: The queue_name of this ElasticResourcePoolQueue.
        :rtype: str
        """
        return self._queue_name

    @queue_name.setter
    def queue_name(self, queue_name):
        """Sets the queue_name of this ElasticResourcePoolQueue.

        队列名称

        :param queue_name: The queue_name of this ElasticResourcePoolQueue.
        :type queue_name: str
        """
        self._queue_name = queue_name

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ElasticResourcePoolQueue.

        企业项目ID

        :return: The enterprise_project_id of this ElasticResourcePoolQueue.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ElasticResourcePoolQueue.

        企业项目ID

        :param enterprise_project_id: The enterprise_project_id of this ElasticResourcePoolQueue.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def queue_type(self):
        """Gets the queue_type of this ElasticResourcePoolQueue.

        队列类型

        :return: The queue_type of this ElasticResourcePoolQueue.
        :rtype: str
        """
        return self._queue_type

    @queue_type.setter
    def queue_type(self, queue_type):
        """Sets the queue_type of this ElasticResourcePoolQueue.

        队列类型

        :param queue_type: The queue_type of this ElasticResourcePoolQueue.
        :type queue_type: str
        """
        self._queue_type = queue_type

    @property
    def queue_scaling_policies(self):
        """Gets the queue_scaling_policies of this ElasticResourcePoolQueue.

        队列扩缩容策略

        :return: The queue_scaling_policies of this ElasticResourcePoolQueue.
        :rtype: list[:class:`huaweicloudsdkdli.v1.QueueScalingPolicy`]
        """
        return self._queue_scaling_policies

    @queue_scaling_policies.setter
    def queue_scaling_policies(self, queue_scaling_policies):
        """Sets the queue_scaling_policies of this ElasticResourcePoolQueue.

        队列扩缩容策略

        :param queue_scaling_policies: The queue_scaling_policies of this ElasticResourcePoolQueue.
        :type queue_scaling_policies: list[:class:`huaweicloudsdkdli.v1.QueueScalingPolicy`]
        """
        self._queue_scaling_policies = queue_scaling_policies

    @property
    def owner(self):
        """Gets the owner of this ElasticResourcePoolQueue.

        所有者

        :return: The owner of this ElasticResourcePoolQueue.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this ElasticResourcePoolQueue.

        所有者

        :param owner: The owner of this ElasticResourcePoolQueue.
        :type owner: str
        """
        self._owner = owner

    @property
    def create_time(self):
        """Gets the create_time of this ElasticResourcePoolQueue.

        创建时间

        :return: The create_time of this ElasticResourcePoolQueue.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ElasticResourcePoolQueue.

        创建时间

        :param create_time: The create_time of this ElasticResourcePoolQueue.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def engine(self):
        """Gets the engine of this ElasticResourcePoolQueue.

        引擎类型

        :return: The engine of this ElasticResourcePoolQueue.
        :rtype: str
        """
        return self._engine

    @engine.setter
    def engine(self, engine):
        """Sets the engine of this ElasticResourcePoolQueue.

        引擎类型

        :param engine: The engine of this ElasticResourcePoolQueue.
        :type engine: str
        """
        self._engine = engine

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
        if not isinstance(other, ElasticResourcePoolQueue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
