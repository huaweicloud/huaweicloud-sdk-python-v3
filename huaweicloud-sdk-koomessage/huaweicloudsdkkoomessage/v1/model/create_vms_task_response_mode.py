# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateVmsTaskResponseMode:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ret_code': 'str',
        'task_id': 'str',
        'desc': 'str'
    }

    attribute_map = {
        'ret_code': 'ret_code',
        'task_id': 'task_id',
        'desc': 'desc'
    }

    def __init__(self, ret_code=None, task_id=None, desc=None):
        r"""CreateVmsTaskResponseMode

        The model defined in huaweicloud sdk

        :param ret_code: 智能信息基础版下发结果返回码。
        :type ret_code: str
        :param task_id: 智能信息基础版下发任务批次ID。
        :type task_id: str
        :param desc: 智能信息基础版下发描述信息。
        :type desc: str
        """
        
        

        self._ret_code = None
        self._task_id = None
        self._desc = None
        self.discriminator = None

        if ret_code is not None:
            self.ret_code = ret_code
        if task_id is not None:
            self.task_id = task_id
        if desc is not None:
            self.desc = desc

    @property
    def ret_code(self):
        r"""Gets the ret_code of this CreateVmsTaskResponseMode.

        智能信息基础版下发结果返回码。

        :return: The ret_code of this CreateVmsTaskResponseMode.
        :rtype: str
        """
        return self._ret_code

    @ret_code.setter
    def ret_code(self, ret_code):
        r"""Sets the ret_code of this CreateVmsTaskResponseMode.

        智能信息基础版下发结果返回码。

        :param ret_code: The ret_code of this CreateVmsTaskResponseMode.
        :type ret_code: str
        """
        self._ret_code = ret_code

    @property
    def task_id(self):
        r"""Gets the task_id of this CreateVmsTaskResponseMode.

        智能信息基础版下发任务批次ID。

        :return: The task_id of this CreateVmsTaskResponseMode.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this CreateVmsTaskResponseMode.

        智能信息基础版下发任务批次ID。

        :param task_id: The task_id of this CreateVmsTaskResponseMode.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def desc(self):
        r"""Gets the desc of this CreateVmsTaskResponseMode.

        智能信息基础版下发描述信息。

        :return: The desc of this CreateVmsTaskResponseMode.
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        r"""Sets the desc of this CreateVmsTaskResponseMode.

        智能信息基础版下发描述信息。

        :param desc: The desc of this CreateVmsTaskResponseMode.
        :type desc: str
        """
        self._desc = desc

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
        if not isinstance(other, CreateVmsTaskResponseMode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
