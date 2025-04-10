# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowFsTaskRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'share_id': 'str',
        'feature': 'str',
        'task_id': 'str'
    }

    attribute_map = {
        'share_id': 'share_id',
        'feature': 'feature',
        'task_id': 'task_id'
    }

    def __init__(self, share_id=None, feature=None, task_id=None):
        r"""ShowFsTaskRequest

        The model defined in huaweicloud sdk

        :param share_id: 文件系统id
        :type share_id: str
        :param feature: 任务类型。例，DU任务取值为dir-usage
        :type feature: str
        :param task_id: 任务ID
        :type task_id: str
        """
        
        

        self._share_id = None
        self._feature = None
        self._task_id = None
        self.discriminator = None

        self.share_id = share_id
        self.feature = feature
        self.task_id = task_id

    @property
    def share_id(self):
        r"""Gets the share_id of this ShowFsTaskRequest.

        文件系统id

        :return: The share_id of this ShowFsTaskRequest.
        :rtype: str
        """
        return self._share_id

    @share_id.setter
    def share_id(self, share_id):
        r"""Sets the share_id of this ShowFsTaskRequest.

        文件系统id

        :param share_id: The share_id of this ShowFsTaskRequest.
        :type share_id: str
        """
        self._share_id = share_id

    @property
    def feature(self):
        r"""Gets the feature of this ShowFsTaskRequest.

        任务类型。例，DU任务取值为dir-usage

        :return: The feature of this ShowFsTaskRequest.
        :rtype: str
        """
        return self._feature

    @feature.setter
    def feature(self, feature):
        r"""Sets the feature of this ShowFsTaskRequest.

        任务类型。例，DU任务取值为dir-usage

        :param feature: The feature of this ShowFsTaskRequest.
        :type feature: str
        """
        self._feature = feature

    @property
    def task_id(self):
        r"""Gets the task_id of this ShowFsTaskRequest.

        任务ID

        :return: The task_id of this ShowFsTaskRequest.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this ShowFsTaskRequest.

        任务ID

        :param task_id: The task_id of this ShowFsTaskRequest.
        :type task_id: str
        """
        self._task_id = task_id

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
        if not isinstance(other, ShowFsTaskRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
