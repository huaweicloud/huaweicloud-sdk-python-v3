# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ItemResultVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'int',
        'visible': 'int',
        'resource_id': 'str',
        'resource_name': 'str',
        'check_id': 'str',
        'check_name': 'str',
        'problem_level': 'int'
    }

    attribute_map = {
        'status': 'status',
        'visible': 'visible',
        'resource_id': 'resource_id',
        'resource_name': 'resource_name',
        'check_id': 'check_id',
        'check_name': 'check_name',
        'problem_level': 'problem_level'
    }

    def __init__(self, status=None, visible=None, resource_id=None, resource_name=None, check_id=None, check_name=None, problem_level=None):
        """ItemResultVo

        The model defined in huaweicloud sdk

        :param status: 执行状态
        :type status: int
        :param visible: 是否可见
        :type visible: int
        :param resource_id: 检查项的大类Id
        :type resource_id: str
        :param resource_name: 检查项的大类名称
        :type resource_name: str
        :param check_id: 检查项ID
        :type check_id: str
        :param check_name: 执行状态
        :type check_name: str
        :param problem_level: 问题等级 0:未执行，3 正常，4 异常；可用于判断检查项执行结果
        :type problem_level: int
        """
        
        

        self._status = None
        self._visible = None
        self._resource_id = None
        self._resource_name = None
        self._check_id = None
        self._check_name = None
        self._problem_level = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if visible is not None:
            self.visible = visible
        if resource_id is not None:
            self.resource_id = resource_id
        if resource_name is not None:
            self.resource_name = resource_name
        if check_id is not None:
            self.check_id = check_id
        if check_name is not None:
            self.check_name = check_name
        if problem_level is not None:
            self.problem_level = problem_level

    @property
    def status(self):
        """Gets the status of this ItemResultVo.

        执行状态

        :return: The status of this ItemResultVo.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ItemResultVo.

        执行状态

        :param status: The status of this ItemResultVo.
        :type status: int
        """
        self._status = status

    @property
    def visible(self):
        """Gets the visible of this ItemResultVo.

        是否可见

        :return: The visible of this ItemResultVo.
        :rtype: int
        """
        return self._visible

    @visible.setter
    def visible(self, visible):
        """Sets the visible of this ItemResultVo.

        是否可见

        :param visible: The visible of this ItemResultVo.
        :type visible: int
        """
        self._visible = visible

    @property
    def resource_id(self):
        """Gets the resource_id of this ItemResultVo.

        检查项的大类Id

        :return: The resource_id of this ItemResultVo.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this ItemResultVo.

        检查项的大类Id

        :param resource_id: The resource_id of this ItemResultVo.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def resource_name(self):
        """Gets the resource_name of this ItemResultVo.

        检查项的大类名称

        :return: The resource_name of this ItemResultVo.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """Sets the resource_name of this ItemResultVo.

        检查项的大类名称

        :param resource_name: The resource_name of this ItemResultVo.
        :type resource_name: str
        """
        self._resource_name = resource_name

    @property
    def check_id(self):
        """Gets the check_id of this ItemResultVo.

        检查项ID

        :return: The check_id of this ItemResultVo.
        :rtype: str
        """
        return self._check_id

    @check_id.setter
    def check_id(self, check_id):
        """Sets the check_id of this ItemResultVo.

        检查项ID

        :param check_id: The check_id of this ItemResultVo.
        :type check_id: str
        """
        self._check_id = check_id

    @property
    def check_name(self):
        """Gets the check_name of this ItemResultVo.

        执行状态

        :return: The check_name of this ItemResultVo.
        :rtype: str
        """
        return self._check_name

    @check_name.setter
    def check_name(self, check_name):
        """Sets the check_name of this ItemResultVo.

        执行状态

        :param check_name: The check_name of this ItemResultVo.
        :type check_name: str
        """
        self._check_name = check_name

    @property
    def problem_level(self):
        """Gets the problem_level of this ItemResultVo.

        问题等级 0:未执行，3 正常，4 异常；可用于判断检查项执行结果

        :return: The problem_level of this ItemResultVo.
        :rtype: int
        """
        return self._problem_level

    @problem_level.setter
    def problem_level(self, problem_level):
        """Sets the problem_level of this ItemResultVo.

        问题等级 0:未执行，3 正常，4 异常；可用于判断检查项执行结果

        :param problem_level: The problem_level of this ItemResultVo.
        :type problem_level: int
        """
        self._problem_level = problem_level

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
        if not isinstance(other, ItemResultVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
