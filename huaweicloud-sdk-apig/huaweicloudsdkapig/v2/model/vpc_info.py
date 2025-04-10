# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VpcInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ecs_id': 'str',
        'ecs_name': 'str',
        'cascade_flag': 'bool',
        'vpc_channel_proxy_host': 'str',
        'vpc_channel_id': 'str',
        'vpc_channel_port': 'int'
    }

    attribute_map = {
        'ecs_id': 'ecs_id',
        'ecs_name': 'ecs_name',
        'cascade_flag': 'cascade_flag',
        'vpc_channel_proxy_host': 'vpc_channel_proxy_host',
        'vpc_channel_id': 'vpc_channel_id',
        'vpc_channel_port': 'vpc_channel_port'
    }

    def __init__(self, ecs_id=None, ecs_name=None, cascade_flag=None, vpc_channel_proxy_host=None, vpc_channel_id=None, vpc_channel_port=None):
        r"""VpcInfo

        The model defined in huaweicloud sdk

        :param ecs_id: 云服务器ID
        :type ecs_id: str
        :param ecs_name: 云服务器名称
        :type ecs_name: str
        :param cascade_flag: 是否使用级联方式  暂不支持
        :type cascade_flag: bool
        :param vpc_channel_proxy_host: 代理主机
        :type vpc_channel_proxy_host: str
        :param vpc_channel_id: VPC通道编号
        :type vpc_channel_id: str
        :param vpc_channel_port: VPC通道端口
        :type vpc_channel_port: int
        """
        
        

        self._ecs_id = None
        self._ecs_name = None
        self._cascade_flag = None
        self._vpc_channel_proxy_host = None
        self._vpc_channel_id = None
        self._vpc_channel_port = None
        self.discriminator = None

        if ecs_id is not None:
            self.ecs_id = ecs_id
        if ecs_name is not None:
            self.ecs_name = ecs_name
        if cascade_flag is not None:
            self.cascade_flag = cascade_flag
        if vpc_channel_proxy_host is not None:
            self.vpc_channel_proxy_host = vpc_channel_proxy_host
        if vpc_channel_id is not None:
            self.vpc_channel_id = vpc_channel_id
        if vpc_channel_port is not None:
            self.vpc_channel_port = vpc_channel_port

    @property
    def ecs_id(self):
        r"""Gets the ecs_id of this VpcInfo.

        云服务器ID

        :return: The ecs_id of this VpcInfo.
        :rtype: str
        """
        return self._ecs_id

    @ecs_id.setter
    def ecs_id(self, ecs_id):
        r"""Sets the ecs_id of this VpcInfo.

        云服务器ID

        :param ecs_id: The ecs_id of this VpcInfo.
        :type ecs_id: str
        """
        self._ecs_id = ecs_id

    @property
    def ecs_name(self):
        r"""Gets the ecs_name of this VpcInfo.

        云服务器名称

        :return: The ecs_name of this VpcInfo.
        :rtype: str
        """
        return self._ecs_name

    @ecs_name.setter
    def ecs_name(self, ecs_name):
        r"""Sets the ecs_name of this VpcInfo.

        云服务器名称

        :param ecs_name: The ecs_name of this VpcInfo.
        :type ecs_name: str
        """
        self._ecs_name = ecs_name

    @property
    def cascade_flag(self):
        r"""Gets the cascade_flag of this VpcInfo.

        是否使用级联方式  暂不支持

        :return: The cascade_flag of this VpcInfo.
        :rtype: bool
        """
        return self._cascade_flag

    @cascade_flag.setter
    def cascade_flag(self, cascade_flag):
        r"""Sets the cascade_flag of this VpcInfo.

        是否使用级联方式  暂不支持

        :param cascade_flag: The cascade_flag of this VpcInfo.
        :type cascade_flag: bool
        """
        self._cascade_flag = cascade_flag

    @property
    def vpc_channel_proxy_host(self):
        r"""Gets the vpc_channel_proxy_host of this VpcInfo.

        代理主机

        :return: The vpc_channel_proxy_host of this VpcInfo.
        :rtype: str
        """
        return self._vpc_channel_proxy_host

    @vpc_channel_proxy_host.setter
    def vpc_channel_proxy_host(self, vpc_channel_proxy_host):
        r"""Sets the vpc_channel_proxy_host of this VpcInfo.

        代理主机

        :param vpc_channel_proxy_host: The vpc_channel_proxy_host of this VpcInfo.
        :type vpc_channel_proxy_host: str
        """
        self._vpc_channel_proxy_host = vpc_channel_proxy_host

    @property
    def vpc_channel_id(self):
        r"""Gets the vpc_channel_id of this VpcInfo.

        VPC通道编号

        :return: The vpc_channel_id of this VpcInfo.
        :rtype: str
        """
        return self._vpc_channel_id

    @vpc_channel_id.setter
    def vpc_channel_id(self, vpc_channel_id):
        r"""Sets the vpc_channel_id of this VpcInfo.

        VPC通道编号

        :param vpc_channel_id: The vpc_channel_id of this VpcInfo.
        :type vpc_channel_id: str
        """
        self._vpc_channel_id = vpc_channel_id

    @property
    def vpc_channel_port(self):
        r"""Gets the vpc_channel_port of this VpcInfo.

        VPC通道端口

        :return: The vpc_channel_port of this VpcInfo.
        :rtype: int
        """
        return self._vpc_channel_port

    @vpc_channel_port.setter
    def vpc_channel_port(self, vpc_channel_port):
        r"""Sets the vpc_channel_port of this VpcInfo.

        VPC通道端口

        :param vpc_channel_port: The vpc_channel_port of this VpcInfo.
        :type vpc_channel_port: int
        """
        self._vpc_channel_port = vpc_channel_port

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
        if not isinstance(other, VpcInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
