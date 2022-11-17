# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateEnvironmentVariableV2Response(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'variable_value': 'str',
        'env_id': 'str',
        'group_id': 'str',
        'variable_name': 'str',
        'id': 'str'
    }

    attribute_map = {
        'variable_value': 'variable_value',
        'env_id': 'env_id',
        'group_id': 'group_id',
        'variable_name': 'variable_name',
        'id': 'id'
    }

    def __init__(self, variable_value=None, env_id=None, group_id=None, variable_name=None, id=None):
        """CreateEnvironmentVariableV2Response

        The model defined in huaweicloud sdk

        :param variable_value: 变量值支持英文字母、数字、英文格式的下划线、中划线，斜线（/）、点、冒号，1 ~ 255个字符。
        :type variable_value: str
        :param env_id: 环境编号
        :type env_id: str
        :param group_id: API分组编号
        :type group_id: str
        :param variable_name: 变量名，支持英文字母、数字、英文格式的下划线、中划线，必须以英文字母开头，3~32个字符。在API定义中等于#Name的值#部分（区分大小写），发布到环境里的API被变量值换。 &gt; 中文字符必须为UTF-8或者unicode编码。
        :type variable_name: str
        :param id: 环境变量编号
        :type id: str
        """
        
        super(CreateEnvironmentVariableV2Response, self).__init__()

        self._variable_value = None
        self._env_id = None
        self._group_id = None
        self._variable_name = None
        self._id = None
        self.discriminator = None

        self.variable_value = variable_value
        if env_id is not None:
            self.env_id = env_id
        if group_id is not None:
            self.group_id = group_id
        if variable_name is not None:
            self.variable_name = variable_name
        if id is not None:
            self.id = id

    @property
    def variable_value(self):
        """Gets the variable_value of this CreateEnvironmentVariableV2Response.

        变量值支持英文字母、数字、英文格式的下划线、中划线，斜线（/）、点、冒号，1 ~ 255个字符。

        :return: The variable_value of this CreateEnvironmentVariableV2Response.
        :rtype: str
        """
        return self._variable_value

    @variable_value.setter
    def variable_value(self, variable_value):
        """Sets the variable_value of this CreateEnvironmentVariableV2Response.

        变量值支持英文字母、数字、英文格式的下划线、中划线，斜线（/）、点、冒号，1 ~ 255个字符。

        :param variable_value: The variable_value of this CreateEnvironmentVariableV2Response.
        :type variable_value: str
        """
        self._variable_value = variable_value

    @property
    def env_id(self):
        """Gets the env_id of this CreateEnvironmentVariableV2Response.

        环境编号

        :return: The env_id of this CreateEnvironmentVariableV2Response.
        :rtype: str
        """
        return self._env_id

    @env_id.setter
    def env_id(self, env_id):
        """Sets the env_id of this CreateEnvironmentVariableV2Response.

        环境编号

        :param env_id: The env_id of this CreateEnvironmentVariableV2Response.
        :type env_id: str
        """
        self._env_id = env_id

    @property
    def group_id(self):
        """Gets the group_id of this CreateEnvironmentVariableV2Response.

        API分组编号

        :return: The group_id of this CreateEnvironmentVariableV2Response.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this CreateEnvironmentVariableV2Response.

        API分组编号

        :param group_id: The group_id of this CreateEnvironmentVariableV2Response.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def variable_name(self):
        """Gets the variable_name of this CreateEnvironmentVariableV2Response.

        变量名，支持英文字母、数字、英文格式的下划线、中划线，必须以英文字母开头，3~32个字符。在API定义中等于#Name的值#部分（区分大小写），发布到环境里的API被变量值换。 > 中文字符必须为UTF-8或者unicode编码。

        :return: The variable_name of this CreateEnvironmentVariableV2Response.
        :rtype: str
        """
        return self._variable_name

    @variable_name.setter
    def variable_name(self, variable_name):
        """Sets the variable_name of this CreateEnvironmentVariableV2Response.

        变量名，支持英文字母、数字、英文格式的下划线、中划线，必须以英文字母开头，3~32个字符。在API定义中等于#Name的值#部分（区分大小写），发布到环境里的API被变量值换。 > 中文字符必须为UTF-8或者unicode编码。

        :param variable_name: The variable_name of this CreateEnvironmentVariableV2Response.
        :type variable_name: str
        """
        self._variable_name = variable_name

    @property
    def id(self):
        """Gets the id of this CreateEnvironmentVariableV2Response.

        环境变量编号

        :return: The id of this CreateEnvironmentVariableV2Response.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CreateEnvironmentVariableV2Response.

        环境变量编号

        :param id: The id of this CreateEnvironmentVariableV2Response.
        :type id: str
        """
        self._id = id

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
        if not isinstance(other, CreateEnvironmentVariableV2Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
