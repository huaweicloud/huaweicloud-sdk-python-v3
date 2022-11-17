# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteQueuePlanRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'plan_id': 'int',
        'queue_name': 'str'
    }

    attribute_map = {
        'plan_id': 'plan_id',
        'queue_name': 'queue_name'
    }

    def __init__(self, plan_id=None, queue_name=None):
        """DeleteQueuePlanRequest

        The model defined in huaweicloud sdk

        :param plan_id: 待删除的队列扩缩容计划的ID
        :type plan_id: int
        :param queue_name: 待删除定时扩缩计划的队列名称
        :type queue_name: str
        """
        
        

        self._plan_id = None
        self._queue_name = None
        self.discriminator = None

        self.plan_id = plan_id
        self.queue_name = queue_name

    @property
    def plan_id(self):
        """Gets the plan_id of this DeleteQueuePlanRequest.

        待删除的队列扩缩容计划的ID

        :return: The plan_id of this DeleteQueuePlanRequest.
        :rtype: int
        """
        return self._plan_id

    @plan_id.setter
    def plan_id(self, plan_id):
        """Sets the plan_id of this DeleteQueuePlanRequest.

        待删除的队列扩缩容计划的ID

        :param plan_id: The plan_id of this DeleteQueuePlanRequest.
        :type plan_id: int
        """
        self._plan_id = plan_id

    @property
    def queue_name(self):
        """Gets the queue_name of this DeleteQueuePlanRequest.

        待删除定时扩缩计划的队列名称

        :return: The queue_name of this DeleteQueuePlanRequest.
        :rtype: str
        """
        return self._queue_name

    @queue_name.setter
    def queue_name(self, queue_name):
        """Sets the queue_name of this DeleteQueuePlanRequest.

        待删除定时扩缩计划的队列名称

        :param queue_name: The queue_name of this DeleteQueuePlanRequest.
        :type queue_name: str
        """
        self._queue_name = queue_name

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
        if not isinstance(other, DeleteQueuePlanRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
