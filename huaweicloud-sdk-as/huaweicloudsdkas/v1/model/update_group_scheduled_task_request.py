# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateGroupScheduledTaskRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'scaling_group_id': 'str',
        'scheduled_task_id': 'str',
        'body': 'UpdateScheduledTaskOption'
    }

    attribute_map = {
        'scaling_group_id': 'scaling_group_id',
        'scheduled_task_id': 'scheduled_task_id',
        'body': 'body'
    }

    def __init__(self, scaling_group_id=None, scheduled_task_id=None, body=None):
        r"""UpdateGroupScheduledTaskRequest

        The model defined in huaweicloud sdk

        :param scaling_group_id: 伸缩组ID
        :type scaling_group_id: str
        :param scheduled_task_id: 计划任务ID
        :type scheduled_task_id: str
        :param body: Body of the UpdateGroupScheduledTaskRequest
        :type body: :class:`huaweicloudsdkas.v1.UpdateScheduledTaskOption`
        """
        
        

        self._scaling_group_id = None
        self._scheduled_task_id = None
        self._body = None
        self.discriminator = None

        self.scaling_group_id = scaling_group_id
        self.scheduled_task_id = scheduled_task_id
        if body is not None:
            self.body = body

    @property
    def scaling_group_id(self):
        r"""Gets the scaling_group_id of this UpdateGroupScheduledTaskRequest.

        伸缩组ID

        :return: The scaling_group_id of this UpdateGroupScheduledTaskRequest.
        :rtype: str
        """
        return self._scaling_group_id

    @scaling_group_id.setter
    def scaling_group_id(self, scaling_group_id):
        r"""Sets the scaling_group_id of this UpdateGroupScheduledTaskRequest.

        伸缩组ID

        :param scaling_group_id: The scaling_group_id of this UpdateGroupScheduledTaskRequest.
        :type scaling_group_id: str
        """
        self._scaling_group_id = scaling_group_id

    @property
    def scheduled_task_id(self):
        r"""Gets the scheduled_task_id of this UpdateGroupScheduledTaskRequest.

        计划任务ID

        :return: The scheduled_task_id of this UpdateGroupScheduledTaskRequest.
        :rtype: str
        """
        return self._scheduled_task_id

    @scheduled_task_id.setter
    def scheduled_task_id(self, scheduled_task_id):
        r"""Sets the scheduled_task_id of this UpdateGroupScheduledTaskRequest.

        计划任务ID

        :param scheduled_task_id: The scheduled_task_id of this UpdateGroupScheduledTaskRequest.
        :type scheduled_task_id: str
        """
        self._scheduled_task_id = scheduled_task_id

    @property
    def body(self):
        r"""Gets the body of this UpdateGroupScheduledTaskRequest.

        :return: The body of this UpdateGroupScheduledTaskRequest.
        :rtype: :class:`huaweicloudsdkas.v1.UpdateScheduledTaskOption`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateGroupScheduledTaskRequest.

        :param body: The body of this UpdateGroupScheduledTaskRequest.
        :type body: :class:`huaweicloudsdkas.v1.UpdateScheduledTaskOption`
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
        if not isinstance(other, UpdateGroupScheduledTaskRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
