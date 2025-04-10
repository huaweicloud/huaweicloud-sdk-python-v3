# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteCaptureTaskDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'task_ids': 'list[str]'
    }

    attribute_map = {
        'task_ids': 'task_ids'
    }

    def __init__(self, task_ids=None):
        r"""DeleteCaptureTaskDto

        The model defined in huaweicloud sdk

        :param task_ids: 抓包任务id列表，抓包任务id可通过[查询抓包任务接口](ListCaptureTask.xml)查询获得，通过返回值中的data.records.task_id（.表示各对象之间层级的区分）获得。
        :type task_ids: list[str]
        """
        
        

        self._task_ids = None
        self.discriminator = None

        self.task_ids = task_ids

    @property
    def task_ids(self):
        r"""Gets the task_ids of this DeleteCaptureTaskDto.

        抓包任务id列表，抓包任务id可通过[查询抓包任务接口](ListCaptureTask.xml)查询获得，通过返回值中的data.records.task_id（.表示各对象之间层级的区分）获得。

        :return: The task_ids of this DeleteCaptureTaskDto.
        :rtype: list[str]
        """
        return self._task_ids

    @task_ids.setter
    def task_ids(self, task_ids):
        r"""Sets the task_ids of this DeleteCaptureTaskDto.

        抓包任务id列表，抓包任务id可通过[查询抓包任务接口](ListCaptureTask.xml)查询获得，通过返回值中的data.records.task_id（.表示各对象之间层级的区分）获得。

        :param task_ids: The task_ids of this DeleteCaptureTaskDto.
        :type task_ids: list[str]
        """
        self._task_ids = task_ids

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
        if not isinstance(other, DeleteCaptureTaskDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
