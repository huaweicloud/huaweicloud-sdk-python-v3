# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateScheduleTaskResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_tasks': 'list[InstanceTaskDetail]'
    }

    attribute_map = {
        'instance_tasks': 'instance_tasks'
    }

    def __init__(self, instance_tasks=None):
        r"""CreateScheduleTaskResponse

        The model defined in huaweicloud sdk

        :param instance_tasks: 任务ID。
        :type instance_tasks: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.InstanceTaskDetail`]
        """
        
        super(CreateScheduleTaskResponse, self).__init__()

        self._instance_tasks = None
        self.discriminator = None

        if instance_tasks is not None:
            self.instance_tasks = instance_tasks

    @property
    def instance_tasks(self):
        r"""Gets the instance_tasks of this CreateScheduleTaskResponse.

        任务ID。

        :return: The instance_tasks of this CreateScheduleTaskResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.InstanceTaskDetail`]
        """
        return self._instance_tasks

    @instance_tasks.setter
    def instance_tasks(self, instance_tasks):
        r"""Sets the instance_tasks of this CreateScheduleTaskResponse.

        任务ID。

        :param instance_tasks: The instance_tasks of this CreateScheduleTaskResponse.
        :type instance_tasks: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.InstanceTaskDetail`]
        """
        self._instance_tasks = instance_tasks

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
        if not isinstance(other, CreateScheduleTaskResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
