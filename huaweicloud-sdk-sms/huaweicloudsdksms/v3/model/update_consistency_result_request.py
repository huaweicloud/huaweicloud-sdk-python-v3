# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateConsistencyResultRequest:

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
        'body': 'SetConsistencyResultRequestBody'
    }

    attribute_map = {
        'task_id': 'task_id',
        'body': 'body'
    }

    def __init__(self, task_id=None, body=None):
        r"""UpdateConsistencyResultRequest

        The model defined in huaweicloud sdk

        :param task_id: 任务id
        :type task_id: str
        :param body: Body of the UpdateConsistencyResultRequest
        :type body: :class:`huaweicloudsdksms.v3.SetConsistencyResultRequestBody`
        """
        
        

        self._task_id = None
        self._body = None
        self.discriminator = None

        self.task_id = task_id
        if body is not None:
            self.body = body

    @property
    def task_id(self):
        r"""Gets the task_id of this UpdateConsistencyResultRequest.

        任务id

        :return: The task_id of this UpdateConsistencyResultRequest.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this UpdateConsistencyResultRequest.

        任务id

        :param task_id: The task_id of this UpdateConsistencyResultRequest.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def body(self):
        r"""Gets the body of this UpdateConsistencyResultRequest.

        :return: The body of this UpdateConsistencyResultRequest.
        :rtype: :class:`huaweicloudsdksms.v3.SetConsistencyResultRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateConsistencyResultRequest.

        :param body: The body of this UpdateConsistencyResultRequest.
        :type body: :class:`huaweicloudsdksms.v3.SetConsistencyResultRequestBody`
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
        if not isinstance(other, UpdateConsistencyResultRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
