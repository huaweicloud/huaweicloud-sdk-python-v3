# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApiConditionCreate:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'req_param_name': 'str',
        'sys_param_name': 'str',
        'cookie_param_name': 'str',
        'condition_type': 'str',
        'condition_origin': 'str',
        'condition_value': 'str'
    }

    attribute_map = {
        'req_param_name': 'req_param_name',
        'sys_param_name': 'sys_param_name',
        'cookie_param_name': 'cookie_param_name',
        'condition_type': 'condition_type',
        'condition_origin': 'condition_origin',
        'condition_value': 'condition_value'
    }

    def __init__(self, req_param_name=None, sys_param_name=None, cookie_param_name=None, condition_type=None, condition_origin=None, condition_value=None):
        r"""ApiConditionCreate

        The model defined in huaweicloud sdk

        :param req_param_name: 关联的请求参数对象名称。策略类型为param时必选
        :type req_param_name: str
        :param sys_param_name: 系统参数名称。策略类型为system时必选。支持以下系统参数 - req_path：请求路径。如 /a/b - req_method：请求方法。如 GET - reqPath：请求路径，废弃。如 /a/b - reqMethod：请求方法，废弃。如 GET 
        :type sys_param_name: str
        :param cookie_param_name: COOKIE参数名称;策略类型为cookie时必选
        :type cookie_param_name: str
        :param condition_type: 策略条件 - exact：绝对匹配 - enum：枚举 - pattern：正则  策略类型为param或cookie时必选 
        :type condition_type: str
        :param condition_origin: 策略类型 - param：参数 - source：源IP - system：系统参数 - cookie: COOKIE参数
        :type condition_origin: str
        :param condition_value: 策略值;策略类型为param，source,cookie时必填
        :type condition_value: str
        """
        
        

        self._req_param_name = None
        self._sys_param_name = None
        self._cookie_param_name = None
        self._condition_type = None
        self._condition_origin = None
        self._condition_value = None
        self.discriminator = None

        if req_param_name is not None:
            self.req_param_name = req_param_name
        if sys_param_name is not None:
            self.sys_param_name = sys_param_name
        if cookie_param_name is not None:
            self.cookie_param_name = cookie_param_name
        if condition_type is not None:
            self.condition_type = condition_type
        self.condition_origin = condition_origin
        self.condition_value = condition_value

    @property
    def req_param_name(self):
        r"""Gets the req_param_name of this ApiConditionCreate.

        关联的请求参数对象名称。策略类型为param时必选

        :return: The req_param_name of this ApiConditionCreate.
        :rtype: str
        """
        return self._req_param_name

    @req_param_name.setter
    def req_param_name(self, req_param_name):
        r"""Sets the req_param_name of this ApiConditionCreate.

        关联的请求参数对象名称。策略类型为param时必选

        :param req_param_name: The req_param_name of this ApiConditionCreate.
        :type req_param_name: str
        """
        self._req_param_name = req_param_name

    @property
    def sys_param_name(self):
        r"""Gets the sys_param_name of this ApiConditionCreate.

        系统参数名称。策略类型为system时必选。支持以下系统参数 - req_path：请求路径。如 /a/b - req_method：请求方法。如 GET - reqPath：请求路径，废弃。如 /a/b - reqMethod：请求方法，废弃。如 GET 

        :return: The sys_param_name of this ApiConditionCreate.
        :rtype: str
        """
        return self._sys_param_name

    @sys_param_name.setter
    def sys_param_name(self, sys_param_name):
        r"""Sets the sys_param_name of this ApiConditionCreate.

        系统参数名称。策略类型为system时必选。支持以下系统参数 - req_path：请求路径。如 /a/b - req_method：请求方法。如 GET - reqPath：请求路径，废弃。如 /a/b - reqMethod：请求方法，废弃。如 GET 

        :param sys_param_name: The sys_param_name of this ApiConditionCreate.
        :type sys_param_name: str
        """
        self._sys_param_name = sys_param_name

    @property
    def cookie_param_name(self):
        r"""Gets the cookie_param_name of this ApiConditionCreate.

        COOKIE参数名称;策略类型为cookie时必选

        :return: The cookie_param_name of this ApiConditionCreate.
        :rtype: str
        """
        return self._cookie_param_name

    @cookie_param_name.setter
    def cookie_param_name(self, cookie_param_name):
        r"""Sets the cookie_param_name of this ApiConditionCreate.

        COOKIE参数名称;策略类型为cookie时必选

        :param cookie_param_name: The cookie_param_name of this ApiConditionCreate.
        :type cookie_param_name: str
        """
        self._cookie_param_name = cookie_param_name

    @property
    def condition_type(self):
        r"""Gets the condition_type of this ApiConditionCreate.

        策略条件 - exact：绝对匹配 - enum：枚举 - pattern：正则  策略类型为param或cookie时必选 

        :return: The condition_type of this ApiConditionCreate.
        :rtype: str
        """
        return self._condition_type

    @condition_type.setter
    def condition_type(self, condition_type):
        r"""Sets the condition_type of this ApiConditionCreate.

        策略条件 - exact：绝对匹配 - enum：枚举 - pattern：正则  策略类型为param或cookie时必选 

        :param condition_type: The condition_type of this ApiConditionCreate.
        :type condition_type: str
        """
        self._condition_type = condition_type

    @property
    def condition_origin(self):
        r"""Gets the condition_origin of this ApiConditionCreate.

        策略类型 - param：参数 - source：源IP - system：系统参数 - cookie: COOKIE参数

        :return: The condition_origin of this ApiConditionCreate.
        :rtype: str
        """
        return self._condition_origin

    @condition_origin.setter
    def condition_origin(self, condition_origin):
        r"""Sets the condition_origin of this ApiConditionCreate.

        策略类型 - param：参数 - source：源IP - system：系统参数 - cookie: COOKIE参数

        :param condition_origin: The condition_origin of this ApiConditionCreate.
        :type condition_origin: str
        """
        self._condition_origin = condition_origin

    @property
    def condition_value(self):
        r"""Gets the condition_value of this ApiConditionCreate.

        策略值;策略类型为param，source,cookie时必填

        :return: The condition_value of this ApiConditionCreate.
        :rtype: str
        """
        return self._condition_value

    @condition_value.setter
    def condition_value(self, condition_value):
        r"""Sets the condition_value of this ApiConditionCreate.

        策略值;策略类型为param，source,cookie时必填

        :param condition_value: The condition_value of this ApiConditionCreate.
        :type condition_value: str
        """
        self._condition_value = condition_value

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
        if not isinstance(other, ApiConditionCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
