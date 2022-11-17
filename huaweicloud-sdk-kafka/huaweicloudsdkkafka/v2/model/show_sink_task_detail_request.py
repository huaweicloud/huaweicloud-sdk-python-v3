# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSinkTaskDetailRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'connector_id': 'str',
        'task_id': 'str',
        'topic_info': 'str'
    }

    attribute_map = {
        'connector_id': 'connector_id',
        'task_id': 'task_id',
        'topic_info': 'topic-info'
    }

    def __init__(self, connector_id=None, task_id=None, topic_info=None):
        """ShowSinkTaskDetailRequest

        The model defined in huaweicloud sdk

        :param connector_id: 实例转储ID。 请参考[实例生命周期][查询实例]接口返回的数据。
        :type connector_id: str
        :param task_id: 转储任务ID。
        :type task_id: str
        :param topic_info: 是否包含topic信息。默认是false。
        :type topic_info: str
        """
        
        

        self._connector_id = None
        self._task_id = None
        self._topic_info = None
        self.discriminator = None

        self.connector_id = connector_id
        self.task_id = task_id
        if topic_info is not None:
            self.topic_info = topic_info

    @property
    def connector_id(self):
        """Gets the connector_id of this ShowSinkTaskDetailRequest.

        实例转储ID。 请参考[实例生命周期][查询实例]接口返回的数据。

        :return: The connector_id of this ShowSinkTaskDetailRequest.
        :rtype: str
        """
        return self._connector_id

    @connector_id.setter
    def connector_id(self, connector_id):
        """Sets the connector_id of this ShowSinkTaskDetailRequest.

        实例转储ID。 请参考[实例生命周期][查询实例]接口返回的数据。

        :param connector_id: The connector_id of this ShowSinkTaskDetailRequest.
        :type connector_id: str
        """
        self._connector_id = connector_id

    @property
    def task_id(self):
        """Gets the task_id of this ShowSinkTaskDetailRequest.

        转储任务ID。

        :return: The task_id of this ShowSinkTaskDetailRequest.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this ShowSinkTaskDetailRequest.

        转储任务ID。

        :param task_id: The task_id of this ShowSinkTaskDetailRequest.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def topic_info(self):
        """Gets the topic_info of this ShowSinkTaskDetailRequest.

        是否包含topic信息。默认是false。

        :return: The topic_info of this ShowSinkTaskDetailRequest.
        :rtype: str
        """
        return self._topic_info

    @topic_info.setter
    def topic_info(self, topic_info):
        """Sets the topic_info of this ShowSinkTaskDetailRequest.

        是否包含topic信息。默认是false。

        :param topic_info: The topic_info of this ShowSinkTaskDetailRequest.
        :type topic_info: str
        """
        self._topic_info = topic_info

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
        if not isinstance(other, ShowSinkTaskDetailRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
