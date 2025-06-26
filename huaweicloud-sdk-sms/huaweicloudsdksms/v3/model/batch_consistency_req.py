# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchConsistencyReq:

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
        'source_id': 'str',
        'source_name': 'str'
    }

    attribute_map = {
        'task_id': 'task_id',
        'source_id': 'source_id',
        'source_name': 'source_name'
    }

    def __init__(self, task_id=None, source_id=None, source_name=None):
        r"""BatchConsistencyReq

        The model defined in huaweicloud sdk

        :param task_id: 任务ID
        :type task_id: str
        :param source_id: 源端ID
        :type source_id: str
        :param source_name: 源端名称
        :type source_name: str
        """
        
        

        self._task_id = None
        self._source_id = None
        self._source_name = None
        self.discriminator = None

        self.task_id = task_id
        self.source_id = source_id
        self.source_name = source_name

    @property
    def task_id(self):
        r"""Gets the task_id of this BatchConsistencyReq.

        任务ID

        :return: The task_id of this BatchConsistencyReq.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this BatchConsistencyReq.

        任务ID

        :param task_id: The task_id of this BatchConsistencyReq.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def source_id(self):
        r"""Gets the source_id of this BatchConsistencyReq.

        源端ID

        :return: The source_id of this BatchConsistencyReq.
        :rtype: str
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        r"""Sets the source_id of this BatchConsistencyReq.

        源端ID

        :param source_id: The source_id of this BatchConsistencyReq.
        :type source_id: str
        """
        self._source_id = source_id

    @property
    def source_name(self):
        r"""Gets the source_name of this BatchConsistencyReq.

        源端名称

        :return: The source_name of this BatchConsistencyReq.
        :rtype: str
        """
        return self._source_name

    @source_name.setter
    def source_name(self, source_name):
        r"""Sets the source_name of this BatchConsistencyReq.

        源端名称

        :param source_name: The source_name of this BatchConsistencyReq.
        :type source_name: str
        """
        self._source_name = source_name

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
        if not isinstance(other, BatchConsistencyReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
