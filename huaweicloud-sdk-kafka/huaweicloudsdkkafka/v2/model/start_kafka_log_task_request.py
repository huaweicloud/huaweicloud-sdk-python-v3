# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StartKafkaLogTaskRequest:

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
        'log_type': 'str',
        'body': 'StartKafkaLogTaskReq'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'log_type': 'log_type',
        'body': 'body'
    }

    def __init__(self, instance_id=None, log_type=None, body=None):
        r"""StartKafkaLogTaskRequest

        The model defined in huaweicloud sdk

        :param instance_id: **参数解释**： 实例ID。获取方法如下：调用“查询所有实例列表”接口，从响应体中获取实例ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type instance_id: str
        :param log_type: **参数解释**： 日志任务类型。 **约束限制**： 不涉及。 **取值范围**： - REBALANCE：重平衡日志。 - topic_log：Topic日志。 **默认取值**： 不涉及。
        :type log_type: str
        :param body: Body of the StartKafkaLogTaskRequest
        :type body: :class:`huaweicloudsdkkafka.v2.StartKafkaLogTaskReq`
        """
        
        

        self._instance_id = None
        self._log_type = None
        self._body = None
        self.discriminator = None

        self.instance_id = instance_id
        self.log_type = log_type
        if body is not None:
            self.body = body

    @property
    def instance_id(self):
        r"""Gets the instance_id of this StartKafkaLogTaskRequest.

        **参数解释**： 实例ID。获取方法如下：调用“查询所有实例列表”接口，从响应体中获取实例ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The instance_id of this StartKafkaLogTaskRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this StartKafkaLogTaskRequest.

        **参数解释**： 实例ID。获取方法如下：调用“查询所有实例列表”接口，从响应体中获取实例ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param instance_id: The instance_id of this StartKafkaLogTaskRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def log_type(self):
        r"""Gets the log_type of this StartKafkaLogTaskRequest.

        **参数解释**： 日志任务类型。 **约束限制**： 不涉及。 **取值范围**： - REBALANCE：重平衡日志。 - topic_log：Topic日志。 **默认取值**： 不涉及。

        :return: The log_type of this StartKafkaLogTaskRequest.
        :rtype: str
        """
        return self._log_type

    @log_type.setter
    def log_type(self, log_type):
        r"""Sets the log_type of this StartKafkaLogTaskRequest.

        **参数解释**： 日志任务类型。 **约束限制**： 不涉及。 **取值范围**： - REBALANCE：重平衡日志。 - topic_log：Topic日志。 **默认取值**： 不涉及。

        :param log_type: The log_type of this StartKafkaLogTaskRequest.
        :type log_type: str
        """
        self._log_type = log_type

    @property
    def body(self):
        r"""Gets the body of this StartKafkaLogTaskRequest.

        :return: The body of this StartKafkaLogTaskRequest.
        :rtype: :class:`huaweicloudsdkkafka.v2.StartKafkaLogTaskReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this StartKafkaLogTaskRequest.

        :param body: The body of this StartKafkaLogTaskRequest.
        :type body: :class:`huaweicloudsdkkafka.v2.StartKafkaLogTaskReq`
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
        if not isinstance(other, StartKafkaLogTaskRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
