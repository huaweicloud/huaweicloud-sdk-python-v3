# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ComandParam:


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
        """ComandParam - a model defined in huaweicloud sdk"""
        
        

        self._task_id = None
        self._bucket = None
        self.discriminator = None

        if task_id is not None:
            self.task_id = task_id
        if bucket is not None:
            self.bucket = bucket

    @property
    def task_id(self):
        """Gets the task_id of this ComandParam.

        任务id

        :return: The task_id of this ComandParam.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this ComandParam.

        任务id

        :param task_id: The task_id of this ComandParam.
        :type: str
        """
        self._task_id = task_id

    @property
    def bucket(self):
        """Gets the bucket of this ComandParam.

        桶名

        :return: The bucket of this ComandParam.
        :rtype: str
        """
        return self._bucket

    @bucket.setter
    def bucket(self, bucket):
        """Sets the bucket of this ComandParam.

        桶名

        :param bucket: The bucket of this ComandParam.
        :type: str
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
        if not isinstance(other, ComandParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other