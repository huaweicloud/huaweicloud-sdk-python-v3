# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateDispatchesRequest:


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
        'dispatch_id': 'str',
        'body': 'TaskDispatch'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'task_id': 'task_id',
        'dispatch_id': 'dispatch_id',
        'body': 'body'
    }

    def __init__(self, instance_id=None, task_id=None, dispatch_id=None, body=None):
        """UpdateDispatchesRequest - a model defined in huaweicloud sdk"""
        
        

        self._instance_id = None
        self._task_id = None
        self._dispatch_id = None
        self._body = None
        self.discriminator = None

        self.instance_id = instance_id
        self.task_id = task_id
        self.dispatch_id = dispatch_id
        if body is not None:
            self.body = body

    @property
    def instance_id(self):
        """Gets the instance_id of this UpdateDispatchesRequest.

        实例ID

        :return: The instance_id of this UpdateDispatchesRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this UpdateDispatchesRequest.

        实例ID

        :param instance_id: The instance_id of this UpdateDispatchesRequest.
        :type: str
        """
        self._instance_id = instance_id

    @property
    def task_id(self):
        """Gets the task_id of this UpdateDispatchesRequest.

        任务ID

        :return: The task_id of this UpdateDispatchesRequest.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this UpdateDispatchesRequest.

        任务ID

        :param task_id: The task_id of this UpdateDispatchesRequest.
        :type: str
        """
        self._task_id = task_id

    @property
    def dispatch_id(self):
        """Gets the dispatch_id of this UpdateDispatchesRequest.

        调度唯一标识，调度计划ID

        :return: The dispatch_id of this UpdateDispatchesRequest.
        :rtype: str
        """
        return self._dispatch_id

    @dispatch_id.setter
    def dispatch_id(self, dispatch_id):
        """Sets the dispatch_id of this UpdateDispatchesRequest.

        调度唯一标识，调度计划ID

        :param dispatch_id: The dispatch_id of this UpdateDispatchesRequest.
        :type: str
        """
        self._dispatch_id = dispatch_id

    @property
    def body(self):
        """Gets the body of this UpdateDispatchesRequest.


        :return: The body of this UpdateDispatchesRequest.
        :rtype: TaskDispatch
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateDispatchesRequest.


        :param body: The body of this UpdateDispatchesRequest.
        :type: TaskDispatch
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
        if not isinstance(other, UpdateDispatchesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other