# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MpeCallBackReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'task_type': 'str',
        'task_id': 'str',
        'status': 'str',
        'complete_ratio': 'int',
        'description': 'str',
        'meta_data': 'MpeMetaData'
    }

    attribute_map = {
        'task_type': 'task_type',
        'task_id': 'task_id',
        'status': 'status',
        'complete_ratio': 'complete_ratio',
        'description': 'description',
        'meta_data': 'meta_data'
    }

    def __init__(self, task_type=None, task_id=None, status=None, complete_ratio=None, description=None, meta_data=None):
        """MpeCallBackReq

        The model defined in huaweicloud sdk

        :param task_type: 任务类型
        :type task_type: str
        :param task_id: 任务ID。
        :type task_id: str
        :param status: 任务状态。
        :type status: str
        :param complete_ratio: 任务完成进度百分比值。 
        :type complete_ratio: int
        :param description: 任务执行描述。
        :type description: str
        :param meta_data: 
        :type meta_data: :class:`huaweicloudsdkmpc.v1.MpeMetaData`
        """
        
        

        self._task_type = None
        self._task_id = None
        self._status = None
        self._complete_ratio = None
        self._description = None
        self._meta_data = None
        self.discriminator = None

        if task_type is not None:
            self.task_type = task_type
        if task_id is not None:
            self.task_id = task_id
        if status is not None:
            self.status = status
        if complete_ratio is not None:
            self.complete_ratio = complete_ratio
        if description is not None:
            self.description = description
        if meta_data is not None:
            self.meta_data = meta_data

    @property
    def task_type(self):
        """Gets the task_type of this MpeCallBackReq.

        任务类型

        :return: The task_type of this MpeCallBackReq.
        :rtype: str
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        """Sets the task_type of this MpeCallBackReq.

        任务类型

        :param task_type: The task_type of this MpeCallBackReq.
        :type task_type: str
        """
        self._task_type = task_type

    @property
    def task_id(self):
        """Gets the task_id of this MpeCallBackReq.

        任务ID。

        :return: The task_id of this MpeCallBackReq.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this MpeCallBackReq.

        任务ID。

        :param task_id: The task_id of this MpeCallBackReq.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def status(self):
        """Gets the status of this MpeCallBackReq.

        任务状态。

        :return: The status of this MpeCallBackReq.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this MpeCallBackReq.

        任务状态。

        :param status: The status of this MpeCallBackReq.
        :type status: str
        """
        self._status = status

    @property
    def complete_ratio(self):
        """Gets the complete_ratio of this MpeCallBackReq.

        任务完成进度百分比值。 

        :return: The complete_ratio of this MpeCallBackReq.
        :rtype: int
        """
        return self._complete_ratio

    @complete_ratio.setter
    def complete_ratio(self, complete_ratio):
        """Sets the complete_ratio of this MpeCallBackReq.

        任务完成进度百分比值。 

        :param complete_ratio: The complete_ratio of this MpeCallBackReq.
        :type complete_ratio: int
        """
        self._complete_ratio = complete_ratio

    @property
    def description(self):
        """Gets the description of this MpeCallBackReq.

        任务执行描述。

        :return: The description of this MpeCallBackReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this MpeCallBackReq.

        任务执行描述。

        :param description: The description of this MpeCallBackReq.
        :type description: str
        """
        self._description = description

    @property
    def meta_data(self):
        """Gets the meta_data of this MpeCallBackReq.

        :return: The meta_data of this MpeCallBackReq.
        :rtype: :class:`huaweicloudsdkmpc.v1.MpeMetaData`
        """
        return self._meta_data

    @meta_data.setter
    def meta_data(self, meta_data):
        """Sets the meta_data of this MpeCallBackReq.

        :param meta_data: The meta_data of this MpeCallBackReq.
        :type meta_data: :class:`huaweicloudsdkmpc.v1.MpeMetaData`
        """
        self._meta_data = meta_data

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
        if not isinstance(other, MpeCallBackReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
