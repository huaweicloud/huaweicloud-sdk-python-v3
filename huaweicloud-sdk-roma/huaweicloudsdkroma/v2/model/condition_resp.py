# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConditionResp:

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
        'condition_value': 'str',
        'id': 'str',
        'req_param_id': 'str',
        'req_param_location': 'str'
    }

    attribute_map = {
        'req_param_name': 'req_param_name',
        'sys_param_name': 'sys_param_name',
        'cookie_param_name': 'cookie_param_name',
        'condition_type': 'condition_type',
        'condition_origin': 'condition_origin',
        'condition_value': 'condition_value',
        'id': 'id',
        'req_param_id': 'req_param_id',
        'req_param_location': 'req_param_location'
    }

    def __init__(self, req_param_name=None, sys_param_name=None, cookie_param_name=None, condition_type=None, condition_origin=None, condition_value=None, id=None, req_param_id=None, req_param_location=None):
        """ConditionResp

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
        :param id: 编号
        :type id: str
        :param req_param_id: 关联的请求参数对象编号
        :type req_param_id: str
        :param req_param_location: 关联的请求参数对象位置
        :type req_param_location: str
        """
        
        

        self._req_param_name = None
        self._sys_param_name = None
        self._cookie_param_name = None
        self._condition_type = None
        self._condition_origin = None
        self._condition_value = None
        self._id = None
        self._req_param_id = None
        self._req_param_location = None
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
        if id is not None:
            self.id = id
        if req_param_id is not None:
            self.req_param_id = req_param_id
        if req_param_location is not None:
            self.req_param_location = req_param_location

    @property
    def req_param_name(self):
        """Gets the req_param_name of this ConditionResp.

        关联的请求参数对象名称。策略类型为param时必选

        :return: The req_param_name of this ConditionResp.
        :rtype: str
        """
        return self._req_param_name

    @req_param_name.setter
    def req_param_name(self, req_param_name):
        """Sets the req_param_name of this ConditionResp.

        关联的请求参数对象名称。策略类型为param时必选

        :param req_param_name: The req_param_name of this ConditionResp.
        :type req_param_name: str
        """
        self._req_param_name = req_param_name

    @property
    def sys_param_name(self):
        """Gets the sys_param_name of this ConditionResp.

        系统参数名称。策略类型为system时必选。支持以下系统参数 - req_path：请求路径。如 /a/b - req_method：请求方法。如 GET - reqPath：请求路径，废弃。如 /a/b - reqMethod：请求方法，废弃。如 GET 

        :return: The sys_param_name of this ConditionResp.
        :rtype: str
        """
        return self._sys_param_name

    @sys_param_name.setter
    def sys_param_name(self, sys_param_name):
        """Sets the sys_param_name of this ConditionResp.

        系统参数名称。策略类型为system时必选。支持以下系统参数 - req_path：请求路径。如 /a/b - req_method：请求方法。如 GET - reqPath：请求路径，废弃。如 /a/b - reqMethod：请求方法，废弃。如 GET 

        :param sys_param_name: The sys_param_name of this ConditionResp.
        :type sys_param_name: str
        """
        self._sys_param_name = sys_param_name

    @property
    def cookie_param_name(self):
        """Gets the cookie_param_name of this ConditionResp.

        COOKIE参数名称;策略类型为cookie时必选

        :return: The cookie_param_name of this ConditionResp.
        :rtype: str
        """
        return self._cookie_param_name

    @cookie_param_name.setter
    def cookie_param_name(self, cookie_param_name):
        """Sets the cookie_param_name of this ConditionResp.

        COOKIE参数名称;策略类型为cookie时必选

        :param cookie_param_name: The cookie_param_name of this ConditionResp.
        :type cookie_param_name: str
        """
        self._cookie_param_name = cookie_param_name

    @property
    def condition_type(self):
        """Gets the condition_type of this ConditionResp.

        策略条件 - exact：绝对匹配 - enum：枚举 - pattern：正则  策略类型为param或cookie时必选 

        :return: The condition_type of this ConditionResp.
        :rtype: str
        """
        return self._condition_type

    @condition_type.setter
    def condition_type(self, condition_type):
        """Sets the condition_type of this ConditionResp.

        策略条件 - exact：绝对匹配 - enum：枚举 - pattern：正则  策略类型为param或cookie时必选 

        :param condition_type: The condition_type of this ConditionResp.
        :type condition_type: str
        """
        self._condition_type = condition_type

    @property
    def condition_origin(self):
        """Gets the condition_origin of this ConditionResp.

        策略类型 - param：参数 - source：源IP - system：系统参数 - cookie: COOKIE参数

        :return: The condition_origin of this ConditionResp.
        :rtype: str
        """
        return self._condition_origin

    @condition_origin.setter
    def condition_origin(self, condition_origin):
        """Sets the condition_origin of this ConditionResp.

        策略类型 - param：参数 - source：源IP - system：系统参数 - cookie: COOKIE参数

        :param condition_origin: The condition_origin of this ConditionResp.
        :type condition_origin: str
        """
        self._condition_origin = condition_origin

    @property
    def condition_value(self):
        """Gets the condition_value of this ConditionResp.

        策略值;策略类型为param，source,cookie时必填

        :return: The condition_value of this ConditionResp.
        :rtype: str
        """
        return self._condition_value

    @condition_value.setter
    def condition_value(self, condition_value):
        """Sets the condition_value of this ConditionResp.

        策略值;策略类型为param，source,cookie时必填

        :param condition_value: The condition_value of this ConditionResp.
        :type condition_value: str
        """
        self._condition_value = condition_value

    @property
    def id(self):
        """Gets the id of this ConditionResp.

        编号

        :return: The id of this ConditionResp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ConditionResp.

        编号

        :param id: The id of this ConditionResp.
        :type id: str
        """
        self._id = id

    @property
    def req_param_id(self):
        """Gets the req_param_id of this ConditionResp.

        关联的请求参数对象编号

        :return: The req_param_id of this ConditionResp.
        :rtype: str
        """
        return self._req_param_id

    @req_param_id.setter
    def req_param_id(self, req_param_id):
        """Sets the req_param_id of this ConditionResp.

        关联的请求参数对象编号

        :param req_param_id: The req_param_id of this ConditionResp.
        :type req_param_id: str
        """
        self._req_param_id = req_param_id

    @property
    def req_param_location(self):
        """Gets the req_param_location of this ConditionResp.

        关联的请求参数对象位置

        :return: The req_param_location of this ConditionResp.
        :rtype: str
        """
        return self._req_param_location

    @req_param_location.setter
    def req_param_location(self, req_param_location):
        """Sets the req_param_location of this ConditionResp.

        关联的请求参数对象位置

        :param req_param_location: The req_param_location of this ConditionResp.
        :type req_param_location: str
        """
        self._req_param_location = req_param_location

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
        if not isinstance(other, ConditionResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
