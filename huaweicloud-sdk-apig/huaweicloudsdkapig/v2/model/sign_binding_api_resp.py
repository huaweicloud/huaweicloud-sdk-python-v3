# coding: utf-8

import pprint
import re

import six





class SignBindingApiResp:


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
        'sign_secret': 'str',
        'group_name': 'str',
        'sign_id': 'str',
        'sign_key': 'str',
        'binding_time': 'datetime',
        'env_id': 'str',
        'env_name': 'str',
        'sign_name': 'str',
        'api_type': 'int',
        'api_name': 'str',
        'id': 'str',
        'api_remark': 'str'
    }

    attribute_map = {
        'publish_id': 'publish_id',
        'api_id': 'api_id',
        'sign_secret': 'sign_secret',
        'group_name': 'group_name',
        'sign_id': 'sign_id',
        'sign_key': 'sign_key',
        'binding_time': 'binding_time',
        'env_id': 'env_id',
        'env_name': 'env_name',
        'sign_name': 'sign_name',
        'api_type': 'api_type',
        'api_name': 'api_name',
        'id': 'id',
        'api_remark': 'api_remark'
    }

    def __init__(self, publish_id=None, api_id=None, sign_secret=None, group_name=None, sign_id=None, sign_key=None, binding_time=None, env_id=None, env_name=None, sign_name=None, api_type=None, api_name=None, id=None, api_remark=None):
        """SignBindingApiResp - a model defined in huaweicloud sdk"""
        
        

        self._publish_id = None
        self._api_id = None
        self._sign_secret = None
        self._group_name = None
        self._sign_id = None
        self._sign_key = None
        self._binding_time = None
        self._env_id = None
        self._env_name = None
        self._sign_name = None
        self._api_type = None
        self._api_name = None
        self._id = None
        self._api_remark = None
        self.discriminator = None

        if publish_id is not None:
            self.publish_id = publish_id
        if api_id is not None:
            self.api_id = api_id
        if sign_secret is not None:
            self.sign_secret = sign_secret
        if group_name is not None:
            self.group_name = group_name
        if sign_id is not None:
            self.sign_id = sign_id
        if sign_key is not None:
            self.sign_key = sign_key
        if binding_time is not None:
            self.binding_time = binding_time
        if env_id is not None:
            self.env_id = env_id
        if env_name is not None:
            self.env_name = env_name
        if sign_name is not None:
            self.sign_name = sign_name
        if api_type is not None:
            self.api_type = api_type
        if api_name is not None:
            self.api_name = api_name
        if id is not None:
            self.id = id
        if api_remark is not None:
            self.api_remark = api_remark

    @property
    def publish_id(self):
        """Gets the publish_id of this SignBindingApiResp.

        API的发布编号

        :return: The publish_id of this SignBindingApiResp.
        :rtype: str
        """
        return self._publish_id

    @publish_id.setter
    def publish_id(self, publish_id):
        """Sets the publish_id of this SignBindingApiResp.

        API的发布编号

        :param publish_id: The publish_id of this SignBindingApiResp.
        :type: str
        """
        self._publish_id = publish_id

    @property
    def api_id(self):
        """Gets the api_id of this SignBindingApiResp.

        API编号

        :return: The api_id of this SignBindingApiResp.
        :rtype: str
        """
        return self._api_id

    @api_id.setter
    def api_id(self, api_id):
        """Sets the api_id of this SignBindingApiResp.

        API编号

        :param api_id: The api_id of this SignBindingApiResp.
        :type: str
        """
        self._api_id = api_id

    @property
    def sign_secret(self):
        """Gets the sign_secret of this SignBindingApiResp.

        签名密钥的密钥

        :return: The sign_secret of this SignBindingApiResp.
        :rtype: str
        """
        return self._sign_secret

    @sign_secret.setter
    def sign_secret(self, sign_secret):
        """Sets the sign_secret of this SignBindingApiResp.

        签名密钥的密钥

        :param sign_secret: The sign_secret of this SignBindingApiResp.
        :type: str
        """
        self._sign_secret = sign_secret

    @property
    def group_name(self):
        """Gets the group_name of this SignBindingApiResp.

        API所属分组的名称

        :return: The group_name of this SignBindingApiResp.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this SignBindingApiResp.

        API所属分组的名称

        :param group_name: The group_name of this SignBindingApiResp.
        :type: str
        """
        self._group_name = group_name

    @property
    def sign_id(self):
        """Gets the sign_id of this SignBindingApiResp.

        签名密钥的编号

        :return: The sign_id of this SignBindingApiResp.
        :rtype: str
        """
        return self._sign_id

    @sign_id.setter
    def sign_id(self, sign_id):
        """Sets the sign_id of this SignBindingApiResp.

        签名密钥的编号

        :param sign_id: The sign_id of this SignBindingApiResp.
        :type: str
        """
        self._sign_id = sign_id

    @property
    def sign_key(self):
        """Gets the sign_key of this SignBindingApiResp.

        签名密钥的key

        :return: The sign_key of this SignBindingApiResp.
        :rtype: str
        """
        return self._sign_key

    @sign_key.setter
    def sign_key(self, sign_key):
        """Sets the sign_key of this SignBindingApiResp.

        签名密钥的key

        :param sign_key: The sign_key of this SignBindingApiResp.
        :type: str
        """
        self._sign_key = sign_key

    @property
    def binding_time(self):
        """Gets the binding_time of this SignBindingApiResp.

        绑定时间

        :return: The binding_time of this SignBindingApiResp.
        :rtype: datetime
        """
        return self._binding_time

    @binding_time.setter
    def binding_time(self, binding_time):
        """Sets the binding_time of this SignBindingApiResp.

        绑定时间

        :param binding_time: The binding_time of this SignBindingApiResp.
        :type: datetime
        """
        self._binding_time = binding_time

    @property
    def env_id(self):
        """Gets the env_id of this SignBindingApiResp.

        API所属环境的编号

        :return: The env_id of this SignBindingApiResp.
        :rtype: str
        """
        return self._env_id

    @env_id.setter
    def env_id(self, env_id):
        """Sets the env_id of this SignBindingApiResp.

        API所属环境的编号

        :param env_id: The env_id of this SignBindingApiResp.
        :type: str
        """
        self._env_id = env_id

    @property
    def env_name(self):
        """Gets the env_name of this SignBindingApiResp.

        API所属环境的名称

        :return: The env_name of this SignBindingApiResp.
        :rtype: str
        """
        return self._env_name

    @env_name.setter
    def env_name(self, env_name):
        """Sets the env_name of this SignBindingApiResp.

        API所属环境的名称

        :param env_name: The env_name of this SignBindingApiResp.
        :type: str
        """
        self._env_name = env_name

    @property
    def sign_name(self):
        """Gets the sign_name of this SignBindingApiResp.

        签名密钥的名称

        :return: The sign_name of this SignBindingApiResp.
        :rtype: str
        """
        return self._sign_name

    @sign_name.setter
    def sign_name(self, sign_name):
        """Sets the sign_name of this SignBindingApiResp.

        签名密钥的名称

        :param sign_name: The sign_name of this SignBindingApiResp.
        :type: str
        """
        self._sign_name = sign_name

    @property
    def api_type(self):
        """Gets the api_type of this SignBindingApiResp.

        API类型

        :return: The api_type of this SignBindingApiResp.
        :rtype: int
        """
        return self._api_type

    @api_type.setter
    def api_type(self, api_type):
        """Sets the api_type of this SignBindingApiResp.

        API类型

        :param api_type: The api_type of this SignBindingApiResp.
        :type: int
        """
        self._api_type = api_type

    @property
    def api_name(self):
        """Gets the api_name of this SignBindingApiResp.

        API名称

        :return: The api_name of this SignBindingApiResp.
        :rtype: str
        """
        return self._api_name

    @api_name.setter
    def api_name(self, api_name):
        """Sets the api_name of this SignBindingApiResp.

        API名称

        :param api_name: The api_name of this SignBindingApiResp.
        :type: str
        """
        self._api_name = api_name

    @property
    def id(self):
        """Gets the id of this SignBindingApiResp.

        绑定关系的ID

        :return: The id of this SignBindingApiResp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SignBindingApiResp.

        绑定关系的ID

        :param id: The id of this SignBindingApiResp.
        :type: str
        """
        self._id = id

    @property
    def api_remark(self):
        """Gets the api_remark of this SignBindingApiResp.

        API描述

        :return: The api_remark of this SignBindingApiResp.
        :rtype: str
        """
        return self._api_remark

    @api_remark.setter
    def api_remark(self, api_remark):
        """Sets the api_remark of this SignBindingApiResp.

        API描述

        :param api_remark: The api_remark of this SignBindingApiResp.
        :type: str
        """
        self._api_remark = api_remark

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SignBindingApiResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
