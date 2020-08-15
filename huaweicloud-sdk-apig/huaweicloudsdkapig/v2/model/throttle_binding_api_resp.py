# coding: utf-8

import pprint
import re

import six





class ThrottleBindingApiResp:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'auth_type': 'str',
        'group_name': 'str',
        'publish_id': 'str',
        'throttle_apply_id': 'str',
        'apply_time': 'datetime',
        'remark': 'str',
        'run_env_id': 'str',
        'type': 'int',
        'throttle_name': 'str',
        'req_uri': 'str',
        'run_env_name': 'str',
        'group_id': 'str',
        'name': 'str',
        'id': 'str'
    }

    attribute_map = {
        'auth_type': 'auth_type',
        'group_name': 'group_name',
        'publish_id': 'publish_id',
        'throttle_apply_id': 'throttle_apply_id',
        'apply_time': 'apply_time',
        'remark': 'remark',
        'run_env_id': 'run_env_id',
        'type': 'type',
        'throttle_name': 'throttle_name',
        'req_uri': 'req_uri',
        'run_env_name': 'run_env_name',
        'group_id': 'group_id',
        'name': 'name',
        'id': 'id'
    }

    def __init__(self, auth_type=None, group_name=None, publish_id=None, throttle_apply_id=None, apply_time=None, remark=None, run_env_id=None, type=None, throttle_name=None, req_uri=None, run_env_name=None, group_id=None, name=None, id=None):
        """ThrottleBindingApiResp - a model defined in huaweicloud sdk"""
        
        

        self._auth_type = None
        self._group_name = None
        self._publish_id = None
        self._throttle_apply_id = None
        self._apply_time = None
        self._remark = None
        self._run_env_id = None
        self._type = None
        self._throttle_name = None
        self._req_uri = None
        self._run_env_name = None
        self._group_id = None
        self._name = None
        self._id = None
        self.discriminator = None

        if auth_type is not None:
            self.auth_type = auth_type
        if group_name is not None:
            self.group_name = group_name
        if publish_id is not None:
            self.publish_id = publish_id
        if throttle_apply_id is not None:
            self.throttle_apply_id = throttle_apply_id
        if apply_time is not None:
            self.apply_time = apply_time
        if remark is not None:
            self.remark = remark
        if run_env_id is not None:
            self.run_env_id = run_env_id
        if type is not None:
            self.type = type
        if throttle_name is not None:
            self.throttle_name = throttle_name
        if req_uri is not None:
            self.req_uri = req_uri
        if run_env_name is not None:
            self.run_env_name = run_env_name
        if group_id is not None:
            self.group_id = group_id
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id

    @property
    def auth_type(self):
        """Gets the auth_type of this ThrottleBindingApiResp.

        API的认证方式

        :return: The auth_type of this ThrottleBindingApiResp.
        :rtype: str
        """
        return self._auth_type

    @auth_type.setter
    def auth_type(self, auth_type):
        """Sets the auth_type of this ThrottleBindingApiResp.

        API的认证方式

        :param auth_type: The auth_type of this ThrottleBindingApiResp.
        :type: str
        """
        self._auth_type = auth_type

    @property
    def group_name(self):
        """Gets the group_name of this ThrottleBindingApiResp.

        API所属分组的名称

        :return: The group_name of this ThrottleBindingApiResp.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this ThrottleBindingApiResp.

        API所属分组的名称

        :param group_name: The group_name of this ThrottleBindingApiResp.
        :type: str
        """
        self._group_name = group_name

    @property
    def publish_id(self):
        """Gets the publish_id of this ThrottleBindingApiResp.

        API的发布记录编号

        :return: The publish_id of this ThrottleBindingApiResp.
        :rtype: str
        """
        return self._publish_id

    @publish_id.setter
    def publish_id(self, publish_id):
        """Sets the publish_id of this ThrottleBindingApiResp.

        API的发布记录编号

        :param publish_id: The publish_id of this ThrottleBindingApiResp.
        :type: str
        """
        self._publish_id = publish_id

    @property
    def throttle_apply_id(self):
        """Gets the throttle_apply_id of this ThrottleBindingApiResp.

        与流控策略的绑定关系编号

        :return: The throttle_apply_id of this ThrottleBindingApiResp.
        :rtype: str
        """
        return self._throttle_apply_id

    @throttle_apply_id.setter
    def throttle_apply_id(self, throttle_apply_id):
        """Sets the throttle_apply_id of this ThrottleBindingApiResp.

        与流控策略的绑定关系编号

        :param throttle_apply_id: The throttle_apply_id of this ThrottleBindingApiResp.
        :type: str
        """
        self._throttle_apply_id = throttle_apply_id

    @property
    def apply_time(self):
        """Gets the apply_time of this ThrottleBindingApiResp.

        已绑定的流控策略的绑定时间

        :return: The apply_time of this ThrottleBindingApiResp.
        :rtype: datetime
        """
        return self._apply_time

    @apply_time.setter
    def apply_time(self, apply_time):
        """Sets the apply_time of this ThrottleBindingApiResp.

        已绑定的流控策略的绑定时间

        :param apply_time: The apply_time of this ThrottleBindingApiResp.
        :type: datetime
        """
        self._apply_time = apply_time

    @property
    def remark(self):
        """Gets the remark of this ThrottleBindingApiResp.

        API描述

        :return: The remark of this ThrottleBindingApiResp.
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        """Sets the remark of this ThrottleBindingApiResp.

        API描述

        :param remark: The remark of this ThrottleBindingApiResp.
        :type: str
        """
        self._remark = remark

    @property
    def run_env_id(self):
        """Gets the run_env_id of this ThrottleBindingApiResp.

        发布的环境id

        :return: The run_env_id of this ThrottleBindingApiResp.
        :rtype: str
        """
        return self._run_env_id

    @run_env_id.setter
    def run_env_id(self, run_env_id):
        """Sets the run_env_id of this ThrottleBindingApiResp.

        发布的环境id

        :param run_env_id: The run_env_id of this ThrottleBindingApiResp.
        :type: str
        """
        self._run_env_id = run_env_id

    @property
    def type(self):
        """Gets the type of this ThrottleBindingApiResp.

        API类型

        :return: The type of this ThrottleBindingApiResp.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ThrottleBindingApiResp.

        API类型

        :param type: The type of this ThrottleBindingApiResp.
        :type: int
        """
        self._type = type

    @property
    def throttle_name(self):
        """Gets the throttle_name of this ThrottleBindingApiResp.

        绑定的流控策略名称

        :return: The throttle_name of this ThrottleBindingApiResp.
        :rtype: str
        """
        return self._throttle_name

    @throttle_name.setter
    def throttle_name(self, throttle_name):
        """Sets the throttle_name of this ThrottleBindingApiResp.

        绑定的流控策略名称

        :param throttle_name: The throttle_name of this ThrottleBindingApiResp.
        :type: str
        """
        self._throttle_name = throttle_name

    @property
    def req_uri(self):
        """Gets the req_uri of this ThrottleBindingApiResp.

        API的访问地址

        :return: The req_uri of this ThrottleBindingApiResp.
        :rtype: str
        """
        return self._req_uri

    @req_uri.setter
    def req_uri(self, req_uri):
        """Sets the req_uri of this ThrottleBindingApiResp.

        API的访问地址

        :param req_uri: The req_uri of this ThrottleBindingApiResp.
        :type: str
        """
        self._req_uri = req_uri

    @property
    def run_env_name(self):
        """Gets the run_env_name of this ThrottleBindingApiResp.

        发布的环境名

        :return: The run_env_name of this ThrottleBindingApiResp.
        :rtype: str
        """
        return self._run_env_name

    @run_env_name.setter
    def run_env_name(self, run_env_name):
        """Sets the run_env_name of this ThrottleBindingApiResp.

        发布的环境名

        :param run_env_name: The run_env_name of this ThrottleBindingApiResp.
        :type: str
        """
        self._run_env_name = run_env_name

    @property
    def group_id(self):
        """Gets the group_id of this ThrottleBindingApiResp.

        API所属分组的编号

        :return: The group_id of this ThrottleBindingApiResp.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this ThrottleBindingApiResp.

        API所属分组的编号

        :param group_id: The group_id of this ThrottleBindingApiResp.
        :type: str
        """
        self._group_id = group_id

    @property
    def name(self):
        """Gets the name of this ThrottleBindingApiResp.

        API名称

        :return: The name of this ThrottleBindingApiResp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ThrottleBindingApiResp.

        API名称

        :param name: The name of this ThrottleBindingApiResp.
        :type: str
        """
        self._name = name

    @property
    def id(self):
        """Gets the id of this ThrottleBindingApiResp.

        API编号

        :return: The id of this ThrottleBindingApiResp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ThrottleBindingApiResp.

        API编号

        :param id: The id of this ThrottleBindingApiResp.
        :type: str
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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ThrottleBindingApiResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
