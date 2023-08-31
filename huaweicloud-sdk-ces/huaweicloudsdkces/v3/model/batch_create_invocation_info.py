# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchCreateInvocationInfo:

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
        'invocation_id': 'str',
        'ret_status': 'str',
        'error_code': 'str',
        'error_msg': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'invocation_id': 'invocation_id',
        'ret_status': 'ret_status',
        'error_code': 'error_code',
        'error_msg': 'error_msg'
    }

    def __init__(self, instance_id=None, invocation_id=None, ret_status=None, error_code=None, error_msg=None):
        """BatchCreateInvocationInfo

        The model defined in huaweicloud sdk

        :param instance_id: 机器id
        :type instance_id: str
        :param invocation_id: 任务id
        :type invocation_id: str
        :param ret_status: 任务结果, successful成功，error失败
        :type ret_status: str
        :param error_code: 错误码
        :type error_code: str
        :param error_msg: 错误信息
        :type error_msg: str
        """
        
        

        self._instance_id = None
        self._invocation_id = None
        self._ret_status = None
        self._error_code = None
        self._error_msg = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if invocation_id is not None:
            self.invocation_id = invocation_id
        if ret_status is not None:
            self.ret_status = ret_status
        if error_code is not None:
            self.error_code = error_code
        if error_msg is not None:
            self.error_msg = error_msg

    @property
    def instance_id(self):
        """Gets the instance_id of this BatchCreateInvocationInfo.

        机器id

        :return: The instance_id of this BatchCreateInvocationInfo.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this BatchCreateInvocationInfo.

        机器id

        :param instance_id: The instance_id of this BatchCreateInvocationInfo.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def invocation_id(self):
        """Gets the invocation_id of this BatchCreateInvocationInfo.

        任务id

        :return: The invocation_id of this BatchCreateInvocationInfo.
        :rtype: str
        """
        return self._invocation_id

    @invocation_id.setter
    def invocation_id(self, invocation_id):
        """Sets the invocation_id of this BatchCreateInvocationInfo.

        任务id

        :param invocation_id: The invocation_id of this BatchCreateInvocationInfo.
        :type invocation_id: str
        """
        self._invocation_id = invocation_id

    @property
    def ret_status(self):
        """Gets the ret_status of this BatchCreateInvocationInfo.

        任务结果, successful成功，error失败

        :return: The ret_status of this BatchCreateInvocationInfo.
        :rtype: str
        """
        return self._ret_status

    @ret_status.setter
    def ret_status(self, ret_status):
        """Sets the ret_status of this BatchCreateInvocationInfo.

        任务结果, successful成功，error失败

        :param ret_status: The ret_status of this BatchCreateInvocationInfo.
        :type ret_status: str
        """
        self._ret_status = ret_status

    @property
    def error_code(self):
        """Gets the error_code of this BatchCreateInvocationInfo.

        错误码

        :return: The error_code of this BatchCreateInvocationInfo.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this BatchCreateInvocationInfo.

        错误码

        :param error_code: The error_code of this BatchCreateInvocationInfo.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_msg(self):
        """Gets the error_msg of this BatchCreateInvocationInfo.

        错误信息

        :return: The error_msg of this BatchCreateInvocationInfo.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        """Sets the error_msg of this BatchCreateInvocationInfo.

        错误信息

        :param error_msg: The error_msg of this BatchCreateInvocationInfo.
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
        if not isinstance(other, BatchCreateInvocationInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
