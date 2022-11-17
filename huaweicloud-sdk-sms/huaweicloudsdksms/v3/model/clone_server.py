# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CloneServer:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vm_id': 'str',
        'name': 'str',
        'clone_error': 'str',
        'clone_state': 'str',
        'error_msg': 'str'
    }

    attribute_map = {
        'vm_id': 'vm_id',
        'name': 'name',
        'clone_error': 'clone_error',
        'clone_state': 'clone_state',
        'error_msg': 'error_msg'
    }

    def __init__(self, vm_id=None, name=None, clone_error=None, clone_state=None, error_msg=None):
        """CloneServer

        The model defined in huaweicloud sdk

        :param vm_id: 克隆服务器ID
        :type vm_id: str
        :param name: 克隆虚拟机的名称
        :type name: str
        :param clone_error: 克隆错误信息
        :type clone_error: str
        :param clone_state: 克隆状态
        :type clone_state: str
        :param error_msg: 克隆错误信息描述
        :type error_msg: str
        """
        
        

        self._vm_id = None
        self._name = None
        self._clone_error = None
        self._clone_state = None
        self._error_msg = None
        self.discriminator = None

        if vm_id is not None:
            self.vm_id = vm_id
        if name is not None:
            self.name = name
        if clone_error is not None:
            self.clone_error = clone_error
        if clone_state is not None:
            self.clone_state = clone_state
        if error_msg is not None:
            self.error_msg = error_msg

    @property
    def vm_id(self):
        """Gets the vm_id of this CloneServer.

        克隆服务器ID

        :return: The vm_id of this CloneServer.
        :rtype: str
        """
        return self._vm_id

    @vm_id.setter
    def vm_id(self, vm_id):
        """Sets the vm_id of this CloneServer.

        克隆服务器ID

        :param vm_id: The vm_id of this CloneServer.
        :type vm_id: str
        """
        self._vm_id = vm_id

    @property
    def name(self):
        """Gets the name of this CloneServer.

        克隆虚拟机的名称

        :return: The name of this CloneServer.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CloneServer.

        克隆虚拟机的名称

        :param name: The name of this CloneServer.
        :type name: str
        """
        self._name = name

    @property
    def clone_error(self):
        """Gets the clone_error of this CloneServer.

        克隆错误信息

        :return: The clone_error of this CloneServer.
        :rtype: str
        """
        return self._clone_error

    @clone_error.setter
    def clone_error(self, clone_error):
        """Sets the clone_error of this CloneServer.

        克隆错误信息

        :param clone_error: The clone_error of this CloneServer.
        :type clone_error: str
        """
        self._clone_error = clone_error

    @property
    def clone_state(self):
        """Gets the clone_state of this CloneServer.

        克隆状态

        :return: The clone_state of this CloneServer.
        :rtype: str
        """
        return self._clone_state

    @clone_state.setter
    def clone_state(self, clone_state):
        """Sets the clone_state of this CloneServer.

        克隆状态

        :param clone_state: The clone_state of this CloneServer.
        :type clone_state: str
        """
        self._clone_state = clone_state

    @property
    def error_msg(self):
        """Gets the error_msg of this CloneServer.

        克隆错误信息描述

        :return: The error_msg of this CloneServer.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        """Sets the error_msg of this CloneServer.

        克隆错误信息描述

        :param error_msg: The error_msg of this CloneServer.
        :type error_msg: str
        """
        self._error_msg = error_msg

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
        if not isinstance(other, CloneServer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
