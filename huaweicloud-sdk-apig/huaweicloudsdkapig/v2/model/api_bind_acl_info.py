# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApiBindAclInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'acl_id': 'str',
        'acl_name': 'str',
        'entity_type': 'str',
        'acl_type': 'str',
        'acl_value': 'str',
        'env_id': 'str',
        'env_name': 'str',
        'bind_id': 'str',
        'bind_time': 'datetime'
    }

    attribute_map = {
        'acl_id': 'acl_id',
        'acl_name': 'acl_name',
        'entity_type': 'entity_type',
        'acl_type': 'acl_type',
        'acl_value': 'acl_value',
        'env_id': 'env_id',
        'env_name': 'env_name',
        'bind_id': 'bind_id',
        'bind_time': 'bind_time'
    }

    def __init__(self, acl_id=None, acl_name=None, entity_type=None, acl_type=None, acl_value=None, env_id=None, env_name=None, bind_id=None, bind_time=None):
        """ApiBindAclInfo

        The model defined in huaweicloud sdk

        :param acl_id: ACL策略编号
        :type acl_id: str
        :param acl_name: ACL策略名称
        :type acl_name: str
        :param entity_type: ACL策略作用的对象类型
        :type entity_type: str
        :param acl_type: ACL策略类型 - PERMIT：白名单类型 - DENY：黑名单类型
        :type acl_type: str
        :param acl_value: ACL策略值
        :type acl_value: str
        :param env_id: 生效的环境编号
        :type env_id: str
        :param env_name: 生效的环境名称
        :type env_name: str
        :param bind_id: 绑定关系编号
        :type bind_id: str
        :param bind_time: 绑定时间
        :type bind_time: datetime
        """
        
        

        self._acl_id = None
        self._acl_name = None
        self._entity_type = None
        self._acl_type = None
        self._acl_value = None
        self._env_id = None
        self._env_name = None
        self._bind_id = None
        self._bind_time = None
        self.discriminator = None

        if acl_id is not None:
            self.acl_id = acl_id
        if acl_name is not None:
            self.acl_name = acl_name
        if entity_type is not None:
            self.entity_type = entity_type
        if acl_type is not None:
            self.acl_type = acl_type
        if acl_value is not None:
            self.acl_value = acl_value
        if env_id is not None:
            self.env_id = env_id
        if env_name is not None:
            self.env_name = env_name
        if bind_id is not None:
            self.bind_id = bind_id
        if bind_time is not None:
            self.bind_time = bind_time

    @property
    def acl_id(self):
        """Gets the acl_id of this ApiBindAclInfo.

        ACL策略编号

        :return: The acl_id of this ApiBindAclInfo.
        :rtype: str
        """
        return self._acl_id

    @acl_id.setter
    def acl_id(self, acl_id):
        """Sets the acl_id of this ApiBindAclInfo.

        ACL策略编号

        :param acl_id: The acl_id of this ApiBindAclInfo.
        :type acl_id: str
        """
        self._acl_id = acl_id

    @property
    def acl_name(self):
        """Gets the acl_name of this ApiBindAclInfo.

        ACL策略名称

        :return: The acl_name of this ApiBindAclInfo.
        :rtype: str
        """
        return self._acl_name

    @acl_name.setter
    def acl_name(self, acl_name):
        """Sets the acl_name of this ApiBindAclInfo.

        ACL策略名称

        :param acl_name: The acl_name of this ApiBindAclInfo.
        :type acl_name: str
        """
        self._acl_name = acl_name

    @property
    def entity_type(self):
        """Gets the entity_type of this ApiBindAclInfo.

        ACL策略作用的对象类型

        :return: The entity_type of this ApiBindAclInfo.
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """Sets the entity_type of this ApiBindAclInfo.

        ACL策略作用的对象类型

        :param entity_type: The entity_type of this ApiBindAclInfo.
        :type entity_type: str
        """
        self._entity_type = entity_type

    @property
    def acl_type(self):
        """Gets the acl_type of this ApiBindAclInfo.

        ACL策略类型 - PERMIT：白名单类型 - DENY：黑名单类型

        :return: The acl_type of this ApiBindAclInfo.
        :rtype: str
        """
        return self._acl_type

    @acl_type.setter
    def acl_type(self, acl_type):
        """Sets the acl_type of this ApiBindAclInfo.

        ACL策略类型 - PERMIT：白名单类型 - DENY：黑名单类型

        :param acl_type: The acl_type of this ApiBindAclInfo.
        :type acl_type: str
        """
        self._acl_type = acl_type

    @property
    def acl_value(self):
        """Gets the acl_value of this ApiBindAclInfo.

        ACL策略值

        :return: The acl_value of this ApiBindAclInfo.
        :rtype: str
        """
        return self._acl_value

    @acl_value.setter
    def acl_value(self, acl_value):
        """Sets the acl_value of this ApiBindAclInfo.

        ACL策略值

        :param acl_value: The acl_value of this ApiBindAclInfo.
        :type acl_value: str
        """
        self._acl_value = acl_value

    @property
    def env_id(self):
        """Gets the env_id of this ApiBindAclInfo.

        生效的环境编号

        :return: The env_id of this ApiBindAclInfo.
        :rtype: str
        """
        return self._env_id

    @env_id.setter
    def env_id(self, env_id):
        """Sets the env_id of this ApiBindAclInfo.

        生效的环境编号

        :param env_id: The env_id of this ApiBindAclInfo.
        :type env_id: str
        """
        self._env_id = env_id

    @property
    def env_name(self):
        """Gets the env_name of this ApiBindAclInfo.

        生效的环境名称

        :return: The env_name of this ApiBindAclInfo.
        :rtype: str
        """
        return self._env_name

    @env_name.setter
    def env_name(self, env_name):
        """Sets the env_name of this ApiBindAclInfo.

        生效的环境名称

        :param env_name: The env_name of this ApiBindAclInfo.
        :type env_name: str
        """
        self._env_name = env_name

    @property
    def bind_id(self):
        """Gets the bind_id of this ApiBindAclInfo.

        绑定关系编号

        :return: The bind_id of this ApiBindAclInfo.
        :rtype: str
        """
        return self._bind_id

    @bind_id.setter
    def bind_id(self, bind_id):
        """Sets the bind_id of this ApiBindAclInfo.

        绑定关系编号

        :param bind_id: The bind_id of this ApiBindAclInfo.
        :type bind_id: str
        """
        self._bind_id = bind_id

    @property
    def bind_time(self):
        """Gets the bind_time of this ApiBindAclInfo.

        绑定时间

        :return: The bind_time of this ApiBindAclInfo.
        :rtype: datetime
        """
        return self._bind_time

    @bind_time.setter
    def bind_time(self, bind_time):
        """Sets the bind_time of this ApiBindAclInfo.

        绑定时间

        :param bind_time: The bind_time of this ApiBindAclInfo.
        :type bind_time: datetime
        """
        self._bind_time = bind_time

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
        if not isinstance(other, ApiBindAclInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
