# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModifyConnectorTaskRequest:

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
        'task_id': 'str',
        'body': 'SmartConnectTaskEntity'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'task_id': 'task_id',
        'body': 'body'
    }

    def __init__(self, instance_id=None, task_id=None, body=None):
        r"""ModifyConnectorTaskRequest

        The model defined in huaweicloud sdk

        :param instance_id: **参数解释**： 实例ID。获取方法如下：登录Kafka控制台，在Kafka实例详情页面查找实例ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type instance_id: str
        :param task_id: **参数解释**： 任务ID。获取方法如下：登录Kafka控制台，在Smart Connect页面查找任务ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type task_id: str
        :param body: Body of the ModifyConnectorTaskRequest
        :type body: :class:`huaweicloudsdkkafka.v2.SmartConnectTaskEntity`
        """
        
        

        self._instance_id = None
        self._task_id = None
        self._body = None
        self.discriminator = None

        self.instance_id = instance_id
        self.task_id = task_id
        if body is not None:
            self.body = body

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ModifyConnectorTaskRequest.

        **参数解释**： 实例ID。获取方法如下：登录Kafka控制台，在Kafka实例详情页面查找实例ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The instance_id of this ModifyConnectorTaskRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ModifyConnectorTaskRequest.

        **参数解释**： 实例ID。获取方法如下：登录Kafka控制台，在Kafka实例详情页面查找实例ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param instance_id: The instance_id of this ModifyConnectorTaskRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def task_id(self):
        r"""Gets the task_id of this ModifyConnectorTaskRequest.

        **参数解释**： 任务ID。获取方法如下：登录Kafka控制台，在Smart Connect页面查找任务ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The task_id of this ModifyConnectorTaskRequest.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this ModifyConnectorTaskRequest.

        **参数解释**： 任务ID。获取方法如下：登录Kafka控制台，在Smart Connect页面查找任务ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param task_id: The task_id of this ModifyConnectorTaskRequest.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def body(self):
        r"""Gets the body of this ModifyConnectorTaskRequest.

        :return: The body of this ModifyConnectorTaskRequest.
        :rtype: :class:`huaweicloudsdkkafka.v2.SmartConnectTaskEntity`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this ModifyConnectorTaskRequest.

        :param body: The body of this ModifyConnectorTaskRequest.
        :type body: :class:`huaweicloudsdkkafka.v2.SmartConnectTaskEntity`
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
        if not isinstance(other, ModifyConnectorTaskRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
