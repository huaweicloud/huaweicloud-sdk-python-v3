# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateRocketMqMigrationTaskRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'overwrite': 'str',
        'name': 'str',
        'type': 'str',
        'body': 'dict(str, object)'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'overwrite': 'overwrite',
        'name': 'name',
        'type': 'type',
        'body': 'body'
    }

    def __init__(self, instance_id=None, overwrite=None, name=None, type=None, body=None):
        """CreateRocketMqMigrationTaskRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID。
        :type instance_id: str
        :param overwrite: true开启同名覆盖，会对已有的同名元数据的配置进行修改，false时当topic或group已存在则会报错。
        :type overwrite: str
        :param name: 迁移任务名称，名称规则参考创建实例
        :type name: str
        :param type: 迁移任务类型，分为自建RocketMQ上云(rocketmq)、自建RabbitMQ上云(rabbitToRocket)
        :type type: str
        :param body: 元数据json文件。
        :type body: dict(str, object)
        """
        
        

        self._instance_id = None
        self._overwrite = None
        self._name = None
        self._type = None
        self._body = None
        self.discriminator = None

        self.instance_id = instance_id
        self.overwrite = overwrite
        self.name = name
        self.type = type
        if body is not None:
            self.body = body

    @property
    def instance_id(self):
        """Gets the instance_id of this CreateRocketMqMigrationTaskRequest.

        实例ID。

        :return: The instance_id of this CreateRocketMqMigrationTaskRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this CreateRocketMqMigrationTaskRequest.

        实例ID。

        :param instance_id: The instance_id of this CreateRocketMqMigrationTaskRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def overwrite(self):
        """Gets the overwrite of this CreateRocketMqMigrationTaskRequest.

        true开启同名覆盖，会对已有的同名元数据的配置进行修改，false时当topic或group已存在则会报错。

        :return: The overwrite of this CreateRocketMqMigrationTaskRequest.
        :rtype: str
        """
        return self._overwrite

    @overwrite.setter
    def overwrite(self, overwrite):
        """Sets the overwrite of this CreateRocketMqMigrationTaskRequest.

        true开启同名覆盖，会对已有的同名元数据的配置进行修改，false时当topic或group已存在则会报错。

        :param overwrite: The overwrite of this CreateRocketMqMigrationTaskRequest.
        :type overwrite: str
        """
        self._overwrite = overwrite

    @property
    def name(self):
        """Gets the name of this CreateRocketMqMigrationTaskRequest.

        迁移任务名称，名称规则参考创建实例

        :return: The name of this CreateRocketMqMigrationTaskRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateRocketMqMigrationTaskRequest.

        迁移任务名称，名称规则参考创建实例

        :param name: The name of this CreateRocketMqMigrationTaskRequest.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        """Gets the type of this CreateRocketMqMigrationTaskRequest.

        迁移任务类型，分为自建RocketMQ上云(rocketmq)、自建RabbitMQ上云(rabbitToRocket)

        :return: The type of this CreateRocketMqMigrationTaskRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreateRocketMqMigrationTaskRequest.

        迁移任务类型，分为自建RocketMQ上云(rocketmq)、自建RabbitMQ上云(rabbitToRocket)

        :param type: The type of this CreateRocketMqMigrationTaskRequest.
        :type type: str
        """
        self._type = type

    @property
    def body(self):
        """Gets the body of this CreateRocketMqMigrationTaskRequest.

        元数据json文件。

        :return: The body of this CreateRocketMqMigrationTaskRequest.
        :rtype: dict(str, object)
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this CreateRocketMqMigrationTaskRequest.

        元数据json文件。

        :param body: The body of this CreateRocketMqMigrationTaskRequest.
        :type body: dict(str, object)
        """
        self._body = body

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
        if not isinstance(other, CreateRocketMqMigrationTaskRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
