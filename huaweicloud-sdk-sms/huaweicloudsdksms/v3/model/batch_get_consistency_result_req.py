# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchGetConsistencyResultReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'task_info': 'list[BatchConsistencyReq]'
    }

    attribute_map = {
        'task_info': 'task_info'
    }

    def __init__(self, task_info=None):
        r"""BatchGetConsistencyResultReq

        The model defined in huaweicloud sdk

        :param task_info: 所有任务信息
        :type task_info: list[:class:`huaweicloudsdksms.v3.BatchConsistencyReq`]
        """
        
        

        self._task_info = None
        self.discriminator = None

        self.task_info = task_info

    @property
    def task_info(self):
        r"""Gets the task_info of this BatchGetConsistencyResultReq.

        所有任务信息

        :return: The task_info of this BatchGetConsistencyResultReq.
        :rtype: list[:class:`huaweicloudsdksms.v3.BatchConsistencyReq`]
        """
        return self._task_info

    @task_info.setter
    def task_info(self, task_info):
        r"""Sets the task_info of this BatchGetConsistencyResultReq.

        所有任务信息

        :param task_info: The task_info of this BatchGetConsistencyResultReq.
        :type task_info: list[:class:`huaweicloudsdksms.v3.BatchConsistencyReq`]
        """
        self._task_info = task_info

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
        if not isinstance(other, BatchGetConsistencyResultReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
