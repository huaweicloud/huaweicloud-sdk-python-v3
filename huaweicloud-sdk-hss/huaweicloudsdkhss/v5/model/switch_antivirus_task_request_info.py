# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SwitchAntivirusTaskRequestInfo:

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
        'task_name': 'str',
        'host_ids': 'list[str]'
    }

    attribute_map = {
        'task_id': 'task_id',
        'task_name': 'task_name',
        'host_ids': 'host_ids'
    }

    def __init__(self, task_id=None, task_name=None, host_ids=None):
        r"""SwitchAntivirusTaskRequestInfo

        The model defined in huaweicloud sdk

        :param task_id: 任务ID
        :type task_id: str
        :param task_name: 任务名称
        :type task_name: str
        :param host_ids: 关联主机列表
        :type host_ids: list[str]
        """
        
        

        self._task_id = None
        self._task_name = None
        self._host_ids = None
        self.discriminator = None

        self.task_id = task_id
        self.task_name = task_name
        self.host_ids = host_ids

    @property
    def task_id(self):
        r"""Gets the task_id of this SwitchAntivirusTaskRequestInfo.

        任务ID

        :return: The task_id of this SwitchAntivirusTaskRequestInfo.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this SwitchAntivirusTaskRequestInfo.

        任务ID

        :param task_id: The task_id of this SwitchAntivirusTaskRequestInfo.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def task_name(self):
        r"""Gets the task_name of this SwitchAntivirusTaskRequestInfo.

        任务名称

        :return: The task_name of this SwitchAntivirusTaskRequestInfo.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        r"""Sets the task_name of this SwitchAntivirusTaskRequestInfo.

        任务名称

        :param task_name: The task_name of this SwitchAntivirusTaskRequestInfo.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def host_ids(self):
        r"""Gets the host_ids of this SwitchAntivirusTaskRequestInfo.

        关联主机列表

        :return: The host_ids of this SwitchAntivirusTaskRequestInfo.
        :rtype: list[str]
        """
        return self._host_ids

    @host_ids.setter
    def host_ids(self, host_ids):
        r"""Sets the host_ids of this SwitchAntivirusTaskRequestInfo.

        关联主机列表

        :param host_ids: The host_ids of this SwitchAntivirusTaskRequestInfo.
        :type host_ids: list[str]
        """
        self._host_ids = host_ids

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
        if not isinstance(other, SwitchAntivirusTaskRequestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
