# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UCSJobSpec:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'task_list': 'list[UCSTask]',
        'domain_id': 'str',
        'operation': 'str',
        'wait_time_out': 'int',
        'type': 'str',
        'related_objects': 'dict(str, str)',
        'extend_param': 'dict(str, object)'
    }

    attribute_map = {
        'task_list': 'taskList',
        'domain_id': 'domainID',
        'operation': 'operation',
        'wait_time_out': 'waitTimeOut',
        'type': 'type',
        'related_objects': 'relatedObjects',
        'extend_param': 'extendParam'
    }

    def __init__(self, task_list=None, domain_id=None, operation=None, wait_time_out=None, type=None, related_objects=None, extend_param=None):
        r"""UCSJobSpec

        The model defined in huaweicloud sdk

        :param task_list: 任务列表
        :type task_list: list[:class:`huaweicloudsdkucs.v1.UCSTask`]
        :param domain_id: 用户的domainID
        :type domain_id: str
        :param operation: 操作，create和retry二选一
        :type operation: str
        :param wait_time_out: Job等待时间，单位：秒
        :type wait_time_out: int
        :param type: Job类别
        :type type: str
        :param related_objects: 相关目标
        :type related_objects: dict(str, str)
        :param extend_param: 额外参数
        :type extend_param: dict(str, object)
        """
        
        

        self._task_list = None
        self._domain_id = None
        self._operation = None
        self._wait_time_out = None
        self._type = None
        self._related_objects = None
        self._extend_param = None
        self.discriminator = None

        if task_list is not None:
            self.task_list = task_list
        if domain_id is not None:
            self.domain_id = domain_id
        if operation is not None:
            self.operation = operation
        if wait_time_out is not None:
            self.wait_time_out = wait_time_out
        if type is not None:
            self.type = type
        if related_objects is not None:
            self.related_objects = related_objects
        if extend_param is not None:
            self.extend_param = extend_param

    @property
    def task_list(self):
        r"""Gets the task_list of this UCSJobSpec.

        任务列表

        :return: The task_list of this UCSJobSpec.
        :rtype: list[:class:`huaweicloudsdkucs.v1.UCSTask`]
        """
        return self._task_list

    @task_list.setter
    def task_list(self, task_list):
        r"""Sets the task_list of this UCSJobSpec.

        任务列表

        :param task_list: The task_list of this UCSJobSpec.
        :type task_list: list[:class:`huaweicloudsdkucs.v1.UCSTask`]
        """
        self._task_list = task_list

    @property
    def domain_id(self):
        r"""Gets the domain_id of this UCSJobSpec.

        用户的domainID

        :return: The domain_id of this UCSJobSpec.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this UCSJobSpec.

        用户的domainID

        :param domain_id: The domain_id of this UCSJobSpec.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def operation(self):
        r"""Gets the operation of this UCSJobSpec.

        操作，create和retry二选一

        :return: The operation of this UCSJobSpec.
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        r"""Sets the operation of this UCSJobSpec.

        操作，create和retry二选一

        :param operation: The operation of this UCSJobSpec.
        :type operation: str
        """
        self._operation = operation

    @property
    def wait_time_out(self):
        r"""Gets the wait_time_out of this UCSJobSpec.

        Job等待时间，单位：秒

        :return: The wait_time_out of this UCSJobSpec.
        :rtype: int
        """
        return self._wait_time_out

    @wait_time_out.setter
    def wait_time_out(self, wait_time_out):
        r"""Sets the wait_time_out of this UCSJobSpec.

        Job等待时间，单位：秒

        :param wait_time_out: The wait_time_out of this UCSJobSpec.
        :type wait_time_out: int
        """
        self._wait_time_out = wait_time_out

    @property
    def type(self):
        r"""Gets the type of this UCSJobSpec.

        Job类别

        :return: The type of this UCSJobSpec.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this UCSJobSpec.

        Job类别

        :param type: The type of this UCSJobSpec.
        :type type: str
        """
        self._type = type

    @property
    def related_objects(self):
        r"""Gets the related_objects of this UCSJobSpec.

        相关目标

        :return: The related_objects of this UCSJobSpec.
        :rtype: dict(str, str)
        """
        return self._related_objects

    @related_objects.setter
    def related_objects(self, related_objects):
        r"""Sets the related_objects of this UCSJobSpec.

        相关目标

        :param related_objects: The related_objects of this UCSJobSpec.
        :type related_objects: dict(str, str)
        """
        self._related_objects = related_objects

    @property
    def extend_param(self):
        r"""Gets the extend_param of this UCSJobSpec.

        额外参数

        :return: The extend_param of this UCSJobSpec.
        :rtype: dict(str, object)
        """
        return self._extend_param

    @extend_param.setter
    def extend_param(self, extend_param):
        r"""Sets the extend_param of this UCSJobSpec.

        额外参数

        :param extend_param: The extend_param of this UCSJobSpec.
        :type extend_param: dict(str, object)
        """
        self._extend_param = extend_param

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UCSJobSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
