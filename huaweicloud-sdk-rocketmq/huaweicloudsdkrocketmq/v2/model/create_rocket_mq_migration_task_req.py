# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateRocketMqMigrationTaskReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'topic_config_table': 'dict(str, MigrationRocketMqTopicConfig)',
        'subscription_group_table': 'dict(str, MigrationRocketMqSubscriptionGroup)',
        'vhosts': 'list[MigrationRabbitVhostMetadata]',
        'queues': 'list[MigrationRabbitQueueMetadata]',
        'exchanges': 'list[MigrationRabbitExchangeMetadata]',
        'bindings': 'list[MigrationRabbitBindingMetadata]'
    }

    attribute_map = {
        'topic_config_table': 'topicConfigTable',
        'subscription_group_table': 'subscriptionGroupTable',
        'vhosts': 'vhosts',
        'queues': 'queues',
        'exchanges': 'exchanges',
        'bindings': 'bindings'
    }

    def __init__(self, topic_config_table=None, subscription_group_table=None, vhosts=None, queues=None, exchanges=None, bindings=None):
        r"""CreateRocketMqMigrationTaskReq

        The model defined in huaweicloud sdk

        :param topic_config_table: RocketMQ Topic 元数据，键为Topic名，值为topic配置，迁移任务类型为自建RocketMQ上云(rocketmq)时必填。
        :type topic_config_table: dict(str, MigrationRocketMqTopicConfig)
        :param subscription_group_table: RocketMQ消费组元数据，键为消费组名，值为消费组配置，迁移任务类型为自建RocketMQ上云(rocketmq)时必填。
        :type subscription_group_table: dict(str, MigrationRocketMqSubscriptionGroup)
        :param vhosts: RabbitMQ vhost元数据列表，迁移任务类型为自建RabbitMQ上云(rabbitToRocket)时必填。
        :type vhosts: list[:class:`huaweicloudsdkrocketmq.v2.MigrationRabbitVhostMetadata`]
        :param queues: RabbitMQ队列元数据列表，迁移任务类型为自建RabbitMQ上云(rabbitToRocket)时必填。
        :type queues: list[:class:`huaweicloudsdkrocketmq.v2.MigrationRabbitQueueMetadata`]
        :param exchanges: RabbitMQ交换机元数据列表，迁移任务类型为自建RabbitMQ上云(rabbitToRocket)时必填。
        :type exchanges: list[:class:`huaweicloudsdkrocketmq.v2.MigrationRabbitExchangeMetadata`]
        :param bindings: RabbitMQ binding元数据列表，迁移任务类型为自建RabbitMQ上云(rabbitToRocket)时必填。
        :type bindings: list[:class:`huaweicloudsdkrocketmq.v2.MigrationRabbitBindingMetadata`]
        """
        
        

        self._topic_config_table = None
        self._subscription_group_table = None
        self._vhosts = None
        self._queues = None
        self._exchanges = None
        self._bindings = None
        self.discriminator = None

        if topic_config_table is not None:
            self.topic_config_table = topic_config_table
        if subscription_group_table is not None:
            self.subscription_group_table = subscription_group_table
        if vhosts is not None:
            self.vhosts = vhosts
        if queues is not None:
            self.queues = queues
        if exchanges is not None:
            self.exchanges = exchanges
        if bindings is not None:
            self.bindings = bindings

    @property
    def topic_config_table(self):
        r"""Gets the topic_config_table of this CreateRocketMqMigrationTaskReq.

        RocketMQ Topic 元数据，键为Topic名，值为topic配置，迁移任务类型为自建RocketMQ上云(rocketmq)时必填。

        :return: The topic_config_table of this CreateRocketMqMigrationTaskReq.
        :rtype: dict(str, MigrationRocketMqTopicConfig)
        """
        return self._topic_config_table

    @topic_config_table.setter
    def topic_config_table(self, topic_config_table):
        r"""Sets the topic_config_table of this CreateRocketMqMigrationTaskReq.

        RocketMQ Topic 元数据，键为Topic名，值为topic配置，迁移任务类型为自建RocketMQ上云(rocketmq)时必填。

        :param topic_config_table: The topic_config_table of this CreateRocketMqMigrationTaskReq.
        :type topic_config_table: dict(str, MigrationRocketMqTopicConfig)
        """
        self._topic_config_table = topic_config_table

    @property
    def subscription_group_table(self):
        r"""Gets the subscription_group_table of this CreateRocketMqMigrationTaskReq.

        RocketMQ消费组元数据，键为消费组名，值为消费组配置，迁移任务类型为自建RocketMQ上云(rocketmq)时必填。

        :return: The subscription_group_table of this CreateRocketMqMigrationTaskReq.
        :rtype: dict(str, MigrationRocketMqSubscriptionGroup)
        """
        return self._subscription_group_table

    @subscription_group_table.setter
    def subscription_group_table(self, subscription_group_table):
        r"""Sets the subscription_group_table of this CreateRocketMqMigrationTaskReq.

        RocketMQ消费组元数据，键为消费组名，值为消费组配置，迁移任务类型为自建RocketMQ上云(rocketmq)时必填。

        :param subscription_group_table: The subscription_group_table of this CreateRocketMqMigrationTaskReq.
        :type subscription_group_table: dict(str, MigrationRocketMqSubscriptionGroup)
        """
        self._subscription_group_table = subscription_group_table

    @property
    def vhosts(self):
        r"""Gets the vhosts of this CreateRocketMqMigrationTaskReq.

        RabbitMQ vhost元数据列表，迁移任务类型为自建RabbitMQ上云(rabbitToRocket)时必填。

        :return: The vhosts of this CreateRocketMqMigrationTaskReq.
        :rtype: list[:class:`huaweicloudsdkrocketmq.v2.MigrationRabbitVhostMetadata`]
        """
        return self._vhosts

    @vhosts.setter
    def vhosts(self, vhosts):
        r"""Sets the vhosts of this CreateRocketMqMigrationTaskReq.

        RabbitMQ vhost元数据列表，迁移任务类型为自建RabbitMQ上云(rabbitToRocket)时必填。

        :param vhosts: The vhosts of this CreateRocketMqMigrationTaskReq.
        :type vhosts: list[:class:`huaweicloudsdkrocketmq.v2.MigrationRabbitVhostMetadata`]
        """
        self._vhosts = vhosts

    @property
    def queues(self):
        r"""Gets the queues of this CreateRocketMqMigrationTaskReq.

        RabbitMQ队列元数据列表，迁移任务类型为自建RabbitMQ上云(rabbitToRocket)时必填。

        :return: The queues of this CreateRocketMqMigrationTaskReq.
        :rtype: list[:class:`huaweicloudsdkrocketmq.v2.MigrationRabbitQueueMetadata`]
        """
        return self._queues

    @queues.setter
    def queues(self, queues):
        r"""Sets the queues of this CreateRocketMqMigrationTaskReq.

        RabbitMQ队列元数据列表，迁移任务类型为自建RabbitMQ上云(rabbitToRocket)时必填。

        :param queues: The queues of this CreateRocketMqMigrationTaskReq.
        :type queues: list[:class:`huaweicloudsdkrocketmq.v2.MigrationRabbitQueueMetadata`]
        """
        self._queues = queues

    @property
    def exchanges(self):
        r"""Gets the exchanges of this CreateRocketMqMigrationTaskReq.

        RabbitMQ交换机元数据列表，迁移任务类型为自建RabbitMQ上云(rabbitToRocket)时必填。

        :return: The exchanges of this CreateRocketMqMigrationTaskReq.
        :rtype: list[:class:`huaweicloudsdkrocketmq.v2.MigrationRabbitExchangeMetadata`]
        """
        return self._exchanges

    @exchanges.setter
    def exchanges(self, exchanges):
        r"""Sets the exchanges of this CreateRocketMqMigrationTaskReq.

        RabbitMQ交换机元数据列表，迁移任务类型为自建RabbitMQ上云(rabbitToRocket)时必填。

        :param exchanges: The exchanges of this CreateRocketMqMigrationTaskReq.
        :type exchanges: list[:class:`huaweicloudsdkrocketmq.v2.MigrationRabbitExchangeMetadata`]
        """
        self._exchanges = exchanges

    @property
    def bindings(self):
        r"""Gets the bindings of this CreateRocketMqMigrationTaskReq.

        RabbitMQ binding元数据列表，迁移任务类型为自建RabbitMQ上云(rabbitToRocket)时必填。

        :return: The bindings of this CreateRocketMqMigrationTaskReq.
        :rtype: list[:class:`huaweicloudsdkrocketmq.v2.MigrationRabbitBindingMetadata`]
        """
        return self._bindings

    @bindings.setter
    def bindings(self, bindings):
        r"""Sets the bindings of this CreateRocketMqMigrationTaskReq.

        RabbitMQ binding元数据列表，迁移任务类型为自建RabbitMQ上云(rabbitToRocket)时必填。

        :param bindings: The bindings of this CreateRocketMqMigrationTaskReq.
        :type bindings: list[:class:`huaweicloudsdkrocketmq.v2.MigrationRabbitBindingMetadata`]
        """
        self._bindings = bindings

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
        if not isinstance(other, CreateRocketMqMigrationTaskReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
