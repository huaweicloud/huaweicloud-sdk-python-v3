# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RocketMqDetail:

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
        'group': 'str',
        'topic': 'str',
        'access_key': 'str',
        'secret_key': 'str',
        'vpc_id': 'str',
        'subnet_id': 'str',
        'namesrv_address': 'str',
        'ssl_enable': 'bool',
        'enable_acl': 'bool'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'group': 'group',
        'topic': 'topic',
        'access_key': 'access_key',
        'secret_key': 'secret_key',
        'vpc_id': 'vpc_id',
        'subnet_id': 'subnet_id',
        'namesrv_address': 'namesrv_address',
        'ssl_enable': 'ssl_enable',
        'enable_acl': 'enable_acl'
    }

    def __init__(self, instance_id=None, group=None, topic=None, access_key=None, secret_key=None, vpc_id=None, subnet_id=None, namesrv_address=None, ssl_enable=None, enable_acl=None):
        r"""RocketMqDetail

        The model defined in huaweicloud sdk

        :param instance_id: RocketMQ实例ID
        :type instance_id: str
        :param group: 消费组
        :type group: str
        :param topic: Topic
        :type topic: str
        :param access_key: 用户名
        :type access_key: str
        :param secret_key: 密钥
        :type secret_key: str
        :param vpc_id: 虚拟私有云
        :type vpc_id: str
        :param subnet_id: 子网
        :type subnet_id: str
        :param namesrv_address: 连接地址
        :type namesrv_address: str
        :param ssl_enable: SSL
        :type ssl_enable: bool
        :param enable_acl: ACL访问控制
        :type enable_acl: bool
        """
        
        

        self._instance_id = None
        self._group = None
        self._topic = None
        self._access_key = None
        self._secret_key = None
        self._vpc_id = None
        self._subnet_id = None
        self._namesrv_address = None
        self._ssl_enable = None
        self._enable_acl = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        self.group = group
        self.topic = topic
        self.access_key = access_key
        self.secret_key = secret_key
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if subnet_id is not None:
            self.subnet_id = subnet_id
        if namesrv_address is not None:
            self.namesrv_address = namesrv_address
        if ssl_enable is not None:
            self.ssl_enable = ssl_enable
        if enable_acl is not None:
            self.enable_acl = enable_acl

    @property
    def instance_id(self):
        r"""Gets the instance_id of this RocketMqDetail.

        RocketMQ实例ID

        :return: The instance_id of this RocketMqDetail.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this RocketMqDetail.

        RocketMQ实例ID

        :param instance_id: The instance_id of this RocketMqDetail.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def group(self):
        r"""Gets the group of this RocketMqDetail.

        消费组

        :return: The group of this RocketMqDetail.
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        r"""Sets the group of this RocketMqDetail.

        消费组

        :param group: The group of this RocketMqDetail.
        :type group: str
        """
        self._group = group

    @property
    def topic(self):
        r"""Gets the topic of this RocketMqDetail.

        Topic

        :return: The topic of this RocketMqDetail.
        :rtype: str
        """
        return self._topic

    @topic.setter
    def topic(self, topic):
        r"""Sets the topic of this RocketMqDetail.

        Topic

        :param topic: The topic of this RocketMqDetail.
        :type topic: str
        """
        self._topic = topic

    @property
    def access_key(self):
        r"""Gets the access_key of this RocketMqDetail.

        用户名

        :return: The access_key of this RocketMqDetail.
        :rtype: str
        """
        return self._access_key

    @access_key.setter
    def access_key(self, access_key):
        r"""Sets the access_key of this RocketMqDetail.

        用户名

        :param access_key: The access_key of this RocketMqDetail.
        :type access_key: str
        """
        self._access_key = access_key

    @property
    def secret_key(self):
        r"""Gets the secret_key of this RocketMqDetail.

        密钥

        :return: The secret_key of this RocketMqDetail.
        :rtype: str
        """
        return self._secret_key

    @secret_key.setter
    def secret_key(self, secret_key):
        r"""Sets the secret_key of this RocketMqDetail.

        密钥

        :param secret_key: The secret_key of this RocketMqDetail.
        :type secret_key: str
        """
        self._secret_key = secret_key

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this RocketMqDetail.

        虚拟私有云

        :return: The vpc_id of this RocketMqDetail.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this RocketMqDetail.

        虚拟私有云

        :param vpc_id: The vpc_id of this RocketMqDetail.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        r"""Gets the subnet_id of this RocketMqDetail.

        子网

        :return: The subnet_id of this RocketMqDetail.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        r"""Sets the subnet_id of this RocketMqDetail.

        子网

        :param subnet_id: The subnet_id of this RocketMqDetail.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def namesrv_address(self):
        r"""Gets the namesrv_address of this RocketMqDetail.

        连接地址

        :return: The namesrv_address of this RocketMqDetail.
        :rtype: str
        """
        return self._namesrv_address

    @namesrv_address.setter
    def namesrv_address(self, namesrv_address):
        r"""Sets the namesrv_address of this RocketMqDetail.

        连接地址

        :param namesrv_address: The namesrv_address of this RocketMqDetail.
        :type namesrv_address: str
        """
        self._namesrv_address = namesrv_address

    @property
    def ssl_enable(self):
        r"""Gets the ssl_enable of this RocketMqDetail.

        SSL

        :return: The ssl_enable of this RocketMqDetail.
        :rtype: bool
        """
        return self._ssl_enable

    @ssl_enable.setter
    def ssl_enable(self, ssl_enable):
        r"""Sets the ssl_enable of this RocketMqDetail.

        SSL

        :param ssl_enable: The ssl_enable of this RocketMqDetail.
        :type ssl_enable: bool
        """
        self._ssl_enable = ssl_enable

    @property
    def enable_acl(self):
        r"""Gets the enable_acl of this RocketMqDetail.

        ACL访问控制

        :return: The enable_acl of this RocketMqDetail.
        :rtype: bool
        """
        return self._enable_acl

    @enable_acl.setter
    def enable_acl(self, enable_acl):
        r"""Sets the enable_acl of this RocketMqDetail.

        ACL访问控制

        :param enable_acl: The enable_acl of this RocketMqDetail.
        :type enable_acl: bool
        """
        self._enable_acl = enable_acl

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
        if not isinstance(other, RocketMqDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
