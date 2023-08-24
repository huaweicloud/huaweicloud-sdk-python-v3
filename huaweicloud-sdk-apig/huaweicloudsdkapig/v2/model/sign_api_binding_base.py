# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SignApiBindingBase:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'publish_id': 'str',
        'api_id': 'str',
        'group_name': 'str',
        'binding_time': 'datetime',
        'env_id': 'str',
        'env_name': 'str',
        'api_type': 'int',
        'api_name': 'str',
        'id': 'str',
        'api_remark': 'str',
        'sign_id': 'str',
        'sign_name': 'str',
        'req_method': 'str'
    }

    attribute_map = {
        'publish_id': 'publish_id',
        'api_id': 'api_id',
        'group_name': 'group_name',
        'binding_time': 'binding_time',
        'env_id': 'env_id',
        'env_name': 'env_name',
        'api_type': 'api_type',
        'api_name': 'api_name',
        'id': 'id',
        'api_remark': 'api_remark',
        'sign_id': 'sign_id',
        'sign_name': 'sign_name',
        'req_method': 'req_method'
    }

    def __init__(self, publish_id=None, api_id=None, group_name=None, binding_time=None, env_id=None, env_name=None, api_type=None, api_name=None, id=None, api_remark=None, sign_id=None, sign_name=None, req_method=None):
        """SignApiBindingBase

        The model defined in huaweicloud sdk

        :param publish_id: API的发布编号
        :type publish_id: str
        :param api_id: API编号
        :type api_id: str
        :param group_name: API所属分组的名称
        :type group_name: str
        :param binding_time: 绑定时间
        :type binding_time: datetime
        :param env_id: API所属环境的编号
        :type env_id: str
        :param env_name: API所属环境的名称
        :type env_name: str
        :param api_type: API类型
        :type api_type: int
        :param api_name: API名称
        :type api_name: str
        :param id: 绑定关系的ID
        :type id: str
        :param api_remark: API描述
        :type api_remark: str
        :param sign_id: 签名密钥的编号
        :type sign_id: str
        :param sign_name: 签名密钥的名称。支持汉字，英文，数字，下划线，且只能以英文和汉字开头，3 ~ 64字符。 &gt; 中文字符必须为UTF-8或者unicode编码。
        :type sign_name: str
        :param req_method: API请求方法
        :type req_method: str
        """
        
        

        self._publish_id = None
        self._api_id = None
        self._group_name = None
        self._binding_time = None
        self._env_id = None
        self._env_name = None
        self._api_type = None
        self._api_name = None
        self._id = None
        self._api_remark = None
        self._sign_id = None
        self._sign_name = None
        self._req_method = None
        self.discriminator = None

        if publish_id is not None:
            self.publish_id = publish_id
        if api_id is not None:
            self.api_id = api_id
        if group_name is not None:
            self.group_name = group_name
        if binding_time is not None:
            self.binding_time = binding_time
        if env_id is not None:
            self.env_id = env_id
        if env_name is not None:
            self.env_name = env_name
        if api_type is not None:
            self.api_type = api_type
        if api_name is not None:
            self.api_name = api_name
        if id is not None:
            self.id = id
        if api_remark is not None:
            self.api_remark = api_remark
        if sign_id is not None:
            self.sign_id = sign_id
        if sign_name is not None:
            self.sign_name = sign_name
        if req_method is not None:
            self.req_method = req_method

    @property
    def publish_id(self):
        """Gets the publish_id of this SignApiBindingBase.

        API的发布编号

        :return: The publish_id of this SignApiBindingBase.
        :rtype: str
        """
        return self._publish_id

    @publish_id.setter
    def publish_id(self, publish_id):
        """Sets the publish_id of this SignApiBindingBase.

        API的发布编号

        :param publish_id: The publish_id of this SignApiBindingBase.
        :type publish_id: str
        """
        self._publish_id = publish_id

    @property
    def api_id(self):
        """Gets the api_id of this SignApiBindingBase.

        API编号

        :return: The api_id of this SignApiBindingBase.
        :rtype: str
        """
        return self._api_id

    @api_id.setter
    def api_id(self, api_id):
        """Sets the api_id of this SignApiBindingBase.

        API编号

        :param api_id: The api_id of this SignApiBindingBase.
        :type api_id: str
        """
        self._api_id = api_id

    @property
    def group_name(self):
        """Gets the group_name of this SignApiBindingBase.

        API所属分组的名称

        :return: The group_name of this SignApiBindingBase.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this SignApiBindingBase.

        API所属分组的名称

        :param group_name: The group_name of this SignApiBindingBase.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def binding_time(self):
        """Gets the binding_time of this SignApiBindingBase.

        绑定时间

        :return: The binding_time of this SignApiBindingBase.
        :rtype: datetime
        """
        return self._binding_time

    @binding_time.setter
    def binding_time(self, binding_time):
        """Sets the binding_time of this SignApiBindingBase.

        绑定时间

        :param binding_time: The binding_time of this SignApiBindingBase.
        :type binding_time: datetime
        """
        self._binding_time = binding_time

    @property
    def env_id(self):
        """Gets the env_id of this SignApiBindingBase.

        API所属环境的编号

        :return: The env_id of this SignApiBindingBase.
        :rtype: str
        """
        return self._env_id

    @env_id.setter
    def env_id(self, env_id):
        """Sets the env_id of this SignApiBindingBase.

        API所属环境的编号

        :param env_id: The env_id of this SignApiBindingBase.
        :type env_id: str
        """
        self._env_id = env_id

    @property
    def env_name(self):
        """Gets the env_name of this SignApiBindingBase.

        API所属环境的名称

        :return: The env_name of this SignApiBindingBase.
        :rtype: str
        """
        return self._env_name

    @env_name.setter
    def env_name(self, env_name):
        """Sets the env_name of this SignApiBindingBase.

        API所属环境的名称

        :param env_name: The env_name of this SignApiBindingBase.
        :type env_name: str
        """
        self._env_name = env_name

    @property
    def api_type(self):
        """Gets the api_type of this SignApiBindingBase.

        API类型

        :return: The api_type of this SignApiBindingBase.
        :rtype: int
        """
        return self._api_type

    @api_type.setter
    def api_type(self, api_type):
        """Sets the api_type of this SignApiBindingBase.

        API类型

        :param api_type: The api_type of this SignApiBindingBase.
        :type api_type: int
        """
        self._api_type = api_type

    @property
    def api_name(self):
        """Gets the api_name of this SignApiBindingBase.

        API名称

        :return: The api_name of this SignApiBindingBase.
        :rtype: str
        """
        return self._api_name

    @api_name.setter
    def api_name(self, api_name):
        """Sets the api_name of this SignApiBindingBase.

        API名称

        :param api_name: The api_name of this SignApiBindingBase.
        :type api_name: str
        """
        self._api_name = api_name

    @property
    def id(self):
        """Gets the id of this SignApiBindingBase.

        绑定关系的ID

        :return: The id of this SignApiBindingBase.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SignApiBindingBase.

        绑定关系的ID

        :param id: The id of this SignApiBindingBase.
        :type id: str
        """
        self._id = id

    @property
    def api_remark(self):
        """Gets the api_remark of this SignApiBindingBase.

        API描述

        :return: The api_remark of this SignApiBindingBase.
        :rtype: str
        """
        return self._api_remark

    @api_remark.setter
    def api_remark(self, api_remark):
        """Sets the api_remark of this SignApiBindingBase.

        API描述

        :param api_remark: The api_remark of this SignApiBindingBase.
        :type api_remark: str
        """
        self._api_remark = api_remark

    @property
    def sign_id(self):
        """Gets the sign_id of this SignApiBindingBase.

        签名密钥的编号

        :return: The sign_id of this SignApiBindingBase.
        :rtype: str
        """
        return self._sign_id

    @sign_id.setter
    def sign_id(self, sign_id):
        """Sets the sign_id of this SignApiBindingBase.

        签名密钥的编号

        :param sign_id: The sign_id of this SignApiBindingBase.
        :type sign_id: str
        """
        self._sign_id = sign_id

    @property
    def sign_name(self):
        """Gets the sign_name of this SignApiBindingBase.

        签名密钥的名称。支持汉字，英文，数字，下划线，且只能以英文和汉字开头，3 ~ 64字符。 > 中文字符必须为UTF-8或者unicode编码。

        :return: The sign_name of this SignApiBindingBase.
        :rtype: str
        """
        return self._sign_name

    @sign_name.setter
    def sign_name(self, sign_name):
        """Sets the sign_name of this SignApiBindingBase.

        签名密钥的名称。支持汉字，英文，数字，下划线，且只能以英文和汉字开头，3 ~ 64字符。 > 中文字符必须为UTF-8或者unicode编码。

        :param sign_name: The sign_name of this SignApiBindingBase.
        :type sign_name: str
        """
        self._sign_name = sign_name

    @property
    def req_method(self):
        """Gets the req_method of this SignApiBindingBase.

        API请求方法

        :return: The req_method of this SignApiBindingBase.
        :rtype: str
        """
        return self._req_method

    @req_method.setter
    def req_method(self, req_method):
        """Sets the req_method of this SignApiBindingBase.

        API请求方法

        :param req_method: The req_method of this SignApiBindingBase.
        :type req_method: str
        """
        self._req_method = req_method

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
        if not isinstance(other, SignApiBindingBase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
