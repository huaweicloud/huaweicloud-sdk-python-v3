# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResetConsumeOffsetRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'engine': 'str',
        'instance_id': 'str',
        'group': 'str',
        'body': 'ResetConsumeOffsetReq'
    }

    attribute_map = {
        'engine': 'engine',
        'instance_id': 'instance_id',
        'group': 'group',
        'body': 'body'
    }

    def __init__(self, engine=None, instance_id=None, group=None, body=None):
        r"""ResetConsumeOffsetRequest

        The model defined in huaweicloud sdk

        :param engine: **参数解释**： 引擎。 **约束限制**： 不涉及。 **取值范围**： - rocketmq：RocketMQ消息引擎。 - reliability：RocketMQ消息引擎别称。 **默认取值**： 不涉及。
        :type engine: str
        :param instance_id: **参数解释**： 实例ID。获取方法如下：调用“查询所有实例列表”接口，从响应体中获取实例ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type instance_id: str
        :param group: **参数解释**： 消费组名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type group: str
        :param body: Body of the ResetConsumeOffsetRequest
        :type body: :class:`huaweicloudsdkrocketmq.v2.ResetConsumeOffsetReq`
        """
        
        

        self._engine = None
        self._instance_id = None
        self._group = None
        self._body = None
        self.discriminator = None

        self.engine = engine
        self.instance_id = instance_id
        self.group = group
        if body is not None:
            self.body = body

    @property
    def engine(self):
        r"""Gets the engine of this ResetConsumeOffsetRequest.

        **参数解释**： 引擎。 **约束限制**： 不涉及。 **取值范围**： - rocketmq：RocketMQ消息引擎。 - reliability：RocketMQ消息引擎别称。 **默认取值**： 不涉及。

        :return: The engine of this ResetConsumeOffsetRequest.
        :rtype: str
        """
        return self._engine

    @engine.setter
    def engine(self, engine):
        r"""Sets the engine of this ResetConsumeOffsetRequest.

        **参数解释**： 引擎。 **约束限制**： 不涉及。 **取值范围**： - rocketmq：RocketMQ消息引擎。 - reliability：RocketMQ消息引擎别称。 **默认取值**： 不涉及。

        :param engine: The engine of this ResetConsumeOffsetRequest.
        :type engine: str
        """
        self._engine = engine

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ResetConsumeOffsetRequest.

        **参数解释**： 实例ID。获取方法如下：调用“查询所有实例列表”接口，从响应体中获取实例ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The instance_id of this ResetConsumeOffsetRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ResetConsumeOffsetRequest.

        **参数解释**： 实例ID。获取方法如下：调用“查询所有实例列表”接口，从响应体中获取实例ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param instance_id: The instance_id of this ResetConsumeOffsetRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def group(self):
        r"""Gets the group of this ResetConsumeOffsetRequest.

        **参数解释**： 消费组名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The group of this ResetConsumeOffsetRequest.
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        r"""Sets the group of this ResetConsumeOffsetRequest.

        **参数解释**： 消费组名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param group: The group of this ResetConsumeOffsetRequest.
        :type group: str
        """
        self._group = group

    @property
    def body(self):
        r"""Gets the body of this ResetConsumeOffsetRequest.

        :return: The body of this ResetConsumeOffsetRequest.
        :rtype: :class:`huaweicloudsdkrocketmq.v2.ResetConsumeOffsetReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this ResetConsumeOffsetRequest.

        :param body: The body of this ResetConsumeOffsetRequest.
        :type body: :class:`huaweicloudsdkrocketmq.v2.ResetConsumeOffsetReq`
        """
        self._body = body

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
        if not isinstance(other, ResetConsumeOffsetRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
