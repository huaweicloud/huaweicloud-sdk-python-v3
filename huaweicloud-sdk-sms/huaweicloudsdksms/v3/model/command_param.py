# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CommandParam:

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
        'bucket': 'str'
    }

    attribute_map = {
        'task_id': 'task_id',
        'bucket': 'bucket'
    }

    def __init__(self, task_id=None, bucket=None):
        r"""CommandParam

        The model defined in huaweicloud sdk

        :param task_id: 任务ID
        :type task_id: str
        :param bucket: 桶名
        :type bucket: str
        """
        
        

        self._task_id = None
        self._bucket = None
        self.discriminator = None

        if task_id is not None:
            self.task_id = task_id
        if bucket is not None:
            self.bucket = bucket

    @property
    def task_id(self):
        r"""Gets the task_id of this CommandParam.

        任务ID

        :return: The task_id of this CommandParam.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this CommandParam.

        任务ID

        :param task_id: The task_id of this CommandParam.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def bucket(self):
        r"""Gets the bucket of this CommandParam.

        桶名

        :return: The bucket of this CommandParam.
        :rtype: str
        """
        return self._bucket

    @bucket.setter
    def bucket(self, bucket):
        r"""Sets the bucket of this CommandParam.

        桶名

        :param bucket: The bucket of this CommandParam.
        :type bucket: str
        """
        self._bucket = bucket

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
        if not isinstance(other, CommandParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
