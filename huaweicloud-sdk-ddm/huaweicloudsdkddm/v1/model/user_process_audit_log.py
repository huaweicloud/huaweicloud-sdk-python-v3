# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UserProcessAuditLog:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'instance_name': 'str',
        'process_id': 'str',
        'execute_user_name': 'str',
        'execute_time': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'instance_name': 'instance_name',
        'process_id': 'process_id',
        'execute_user_name': 'execute_user_name',
        'execute_time': 'execute_time'
    }

    def __init__(self, instance_id=None, instance_name=None, process_id=None, execute_user_name=None, execute_time=None):
        r"""UserProcessAuditLog

        The model defined in huaweicloud sdk

        :param instance_id: 实例id
        :type instance_id: str
        :param instance_name: 实例名
        :type instance_name: str
        :param process_id: 会话id
        :type process_id: str
        :param execute_user_name: 执行用户名
        :type execute_user_name: str
        :param execute_time: 发生时间，UTC时间
        :type execute_time: str
        """
        
        

        self._instance_id = None
        self._instance_name = None
        self._process_id = None
        self._execute_user_name = None
        self._execute_time = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if instance_name is not None:
            self.instance_name = instance_name
        if process_id is not None:
            self.process_id = process_id
        if execute_user_name is not None:
            self.execute_user_name = execute_user_name
        if execute_time is not None:
            self.execute_time = execute_time

    @property
    def instance_id(self):
        r"""Gets the instance_id of this UserProcessAuditLog.

        实例id

        :return: The instance_id of this UserProcessAuditLog.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this UserProcessAuditLog.

        实例id

        :param instance_id: The instance_id of this UserProcessAuditLog.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def instance_name(self):
        r"""Gets the instance_name of this UserProcessAuditLog.

        实例名

        :return: The instance_name of this UserProcessAuditLog.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        r"""Sets the instance_name of this UserProcessAuditLog.

        实例名

        :param instance_name: The instance_name of this UserProcessAuditLog.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def process_id(self):
        r"""Gets the process_id of this UserProcessAuditLog.

        会话id

        :return: The process_id of this UserProcessAuditLog.
        :rtype: str
        """
        return self._process_id

    @process_id.setter
    def process_id(self, process_id):
        r"""Sets the process_id of this UserProcessAuditLog.

        会话id

        :param process_id: The process_id of this UserProcessAuditLog.
        :type process_id: str
        """
        self._process_id = process_id

    @property
    def execute_user_name(self):
        r"""Gets the execute_user_name of this UserProcessAuditLog.

        执行用户名

        :return: The execute_user_name of this UserProcessAuditLog.
        :rtype: str
        """
        return self._execute_user_name

    @execute_user_name.setter
    def execute_user_name(self, execute_user_name):
        r"""Sets the execute_user_name of this UserProcessAuditLog.

        执行用户名

        :param execute_user_name: The execute_user_name of this UserProcessAuditLog.
        :type execute_user_name: str
        """
        self._execute_user_name = execute_user_name

    @property
    def execute_time(self):
        r"""Gets the execute_time of this UserProcessAuditLog.

        发生时间，UTC时间

        :return: The execute_time of this UserProcessAuditLog.
        :rtype: str
        """
        return self._execute_time

    @execute_time.setter
    def execute_time(self, execute_time):
        r"""Sets the execute_time of this UserProcessAuditLog.

        发生时间，UTC时间

        :param execute_time: The execute_time of this UserProcessAuditLog.
        :type execute_time: str
        """
        self._execute_time = execute_time

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
        if not isinstance(other, UserProcessAuditLog):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
