# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateJobReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tasks': 'list[JobTaskDto]'
    }

    attribute_map = {
        'tasks': 'tasks'
    }

    def __init__(self, tasks=None):
        r"""UpdateJobReq

        The model defined in huaweicloud sdk

        :param tasks: 步骤的参数修改信息
        :type tasks: list[:class:`huaweicloudsdkeihealth.v1.JobTaskDto`]
        """
        
        

        self._tasks = None
        self.discriminator = None

        self.tasks = tasks

    @property
    def tasks(self):
        r"""Gets the tasks of this UpdateJobReq.

        步骤的参数修改信息

        :return: The tasks of this UpdateJobReq.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.JobTaskDto`]
        """
        return self._tasks

    @tasks.setter
    def tasks(self, tasks):
        r"""Sets the tasks of this UpdateJobReq.

        步骤的参数修改信息

        :param tasks: The tasks of this UpdateJobReq.
        :type tasks: list[:class:`huaweicloudsdkeihealth.v1.JobTaskDto`]
        """
        self._tasks = tasks

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
        if not isinstance(other, UpdateJobReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
