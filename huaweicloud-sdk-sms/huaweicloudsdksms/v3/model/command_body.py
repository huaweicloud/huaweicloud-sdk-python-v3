# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CommandBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'command_name': 'str',
        'result': 'str',
        'result_detail': 'object'
    }

    attribute_map = {
        'command_name': 'command_name',
        'result': 'result',
        'result_detail': 'result_detail'
    }

    def __init__(self, command_name=None, result=None, result_detail=None):
        """CommandBody

        The model defined in huaweicloud sdk

        :param command_name: 命令名称，分为：START、STOP、DELETE、SYNC、UPLOAD_LOG、RSET_LOG_ACL
        :type command_name: str
        :param result: 命令执行结果  success代表执行命令成功  fail代表命令执行失败 
        :type result: str
        :param result_detail: JSON格式的命令执行结果，只用于保存数据库，没有其他作用
        :type result_detail: object
        """
        
        

        self._command_name = None
        self._result = None
        self._result_detail = None
        self.discriminator = None

        self.command_name = command_name
        self.result = result
        self.result_detail = result_detail

    @property
    def command_name(self):
        """Gets the command_name of this CommandBody.

        命令名称，分为：START、STOP、DELETE、SYNC、UPLOAD_LOG、RSET_LOG_ACL

        :return: The command_name of this CommandBody.
        :rtype: str
        """
        return self._command_name

    @command_name.setter
    def command_name(self, command_name):
        """Sets the command_name of this CommandBody.

        命令名称，分为：START、STOP、DELETE、SYNC、UPLOAD_LOG、RSET_LOG_ACL

        :param command_name: The command_name of this CommandBody.
        :type command_name: str
        """
        self._command_name = command_name

    @property
    def result(self):
        """Gets the result of this CommandBody.

        命令执行结果  success代表执行命令成功  fail代表命令执行失败 

        :return: The result of this CommandBody.
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this CommandBody.

        命令执行结果  success代表执行命令成功  fail代表命令执行失败 

        :param result: The result of this CommandBody.
        :type result: str
        """
        self._result = result

    @property
    def result_detail(self):
        """Gets the result_detail of this CommandBody.

        JSON格式的命令执行结果，只用于保存数据库，没有其他作用

        :return: The result_detail of this CommandBody.
        :rtype: object
        """
        return self._result_detail

    @result_detail.setter
    def result_detail(self, result_detail):
        """Sets the result_detail of this CommandBody.

        JSON格式的命令执行结果，只用于保存数据库，没有其他作用

        :param result_detail: The result_detail of this CommandBody.
        :type result_detail: object
        """
        self._result_detail = result_detail

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
        if not isinstance(other, CommandBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
