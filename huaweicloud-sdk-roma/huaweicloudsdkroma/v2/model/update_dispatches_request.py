# coding: utf-8

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
        r"""UpdateDispatchesRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID
        :type instance_id: str
        :param task_id: 任务ID
        :type task_id: str
        :param dispatch_id: 调度唯一标识，调度计划ID
        :type dispatch_id: str
        :param body: Body of the UpdateDispatchesRequest
        :type body: :class:`huaweicloudsdkroma.v2.TaskDispatch`
        """
        
        

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
        r"""Gets the instance_id of this UpdateDispatchesRequest.

        实例ID

        :return: The instance_id of this UpdateDispatchesRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this UpdateDispatchesRequest.

        实例ID

        :param instance_id: The instance_id of this UpdateDispatchesRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def task_id(self):
        r"""Gets the task_id of this UpdateDispatchesRequest.

        任务ID

        :return: The task_id of this UpdateDispatchesRequest.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this UpdateDispatchesRequest.

        任务ID

        :param task_id: The task_id of this UpdateDispatchesRequest.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def dispatch_id(self):
        r"""Gets the dispatch_id of this UpdateDispatchesRequest.

        调度唯一标识，调度计划ID

        :return: The dispatch_id of this UpdateDispatchesRequest.
        :rtype: str
        """
        return self._dispatch_id

    @dispatch_id.setter
    def dispatch_id(self, dispatch_id):
        r"""Sets the dispatch_id of this UpdateDispatchesRequest.

        调度唯一标识，调度计划ID

        :param dispatch_id: The dispatch_id of this UpdateDispatchesRequest.
        :type dispatch_id: str
        """
        self._dispatch_id = dispatch_id

    @property
    def body(self):
        r"""Gets the body of this UpdateDispatchesRequest.

        :return: The body of this UpdateDispatchesRequest.
        :rtype: :class:`huaweicloudsdkroma.v2.TaskDispatch`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateDispatchesRequest.

        :param body: The body of this UpdateDispatchesRequest.
        :type body: :class:`huaweicloudsdkroma.v2.TaskDispatch`
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
