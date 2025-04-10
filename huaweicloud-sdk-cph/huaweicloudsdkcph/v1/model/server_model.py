# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ServerModel:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'server_model_name': 'str',
        'server_type': 'str',
        'cpu': 'int',
        'memory': 'int',
        'extend_spec': 'ServerModelExtendSpec',
        'disk_max_num': 'int',
        'product_type': 'int',
        'free_size': 'int'
    }

    attribute_map = {
        'server_model_name': 'server_model_name',
        'server_type': 'server_type',
        'cpu': 'cpu',
        'memory': 'memory',
        'extend_spec': 'extend_spec',
        'disk_max_num': 'disk_max_num',
        'product_type': 'product_type',
        'free_size': 'free_size'
    }

    def __init__(self, server_model_name=None, server_type=None, cpu=None, memory=None, extend_spec=None, disk_max_num=None, product_type=None, free_size=None):
        r"""ServerModel

        The model defined in huaweicloud sdk

        :param server_model_name: 云手机服务器的规格名称，不超过64字节。
        :type server_model_name: str
        :param server_type: 云手机服务器的型号，如Hi1616。不超过32字节。
        :type server_type: str
        :param cpu: 云手机服务器的CPU核数。
        :type cpu: int
        :param memory: 云手机服务器的内存大小，单位G。
        :type memory: int
        :param extend_spec: 
        :type extend_spec: :class:`huaweicloudsdkcph.v1.ServerModelExtendSpec`
        :param disk_max_num: 云手机服务器最大挂载磁盘数量。值为0时表示该机型磁盘为本地盘。
        :type disk_max_num: int
        :param product_type: 产品类型。 - 0：云手机 - 1：云手游
        :type product_type: int
        :param free_size: 服务器磁盘的免费配额，单位G。
        :type free_size: int
        """
        
        

        self._server_model_name = None
        self._server_type = None
        self._cpu = None
        self._memory = None
        self._extend_spec = None
        self._disk_max_num = None
        self._product_type = None
        self._free_size = None
        self.discriminator = None

        if server_model_name is not None:
            self.server_model_name = server_model_name
        if server_type is not None:
            self.server_type = server_type
        if cpu is not None:
            self.cpu = cpu
        if memory is not None:
            self.memory = memory
        if extend_spec is not None:
            self.extend_spec = extend_spec
        if disk_max_num is not None:
            self.disk_max_num = disk_max_num
        if product_type is not None:
            self.product_type = product_type
        if free_size is not None:
            self.free_size = free_size

    @property
    def server_model_name(self):
        r"""Gets the server_model_name of this ServerModel.

        云手机服务器的规格名称，不超过64字节。

        :return: The server_model_name of this ServerModel.
        :rtype: str
        """
        return self._server_model_name

    @server_model_name.setter
    def server_model_name(self, server_model_name):
        r"""Sets the server_model_name of this ServerModel.

        云手机服务器的规格名称，不超过64字节。

        :param server_model_name: The server_model_name of this ServerModel.
        :type server_model_name: str
        """
        self._server_model_name = server_model_name

    @property
    def server_type(self):
        r"""Gets the server_type of this ServerModel.

        云手机服务器的型号，如Hi1616。不超过32字节。

        :return: The server_type of this ServerModel.
        :rtype: str
        """
        return self._server_type

    @server_type.setter
    def server_type(self, server_type):
        r"""Sets the server_type of this ServerModel.

        云手机服务器的型号，如Hi1616。不超过32字节。

        :param server_type: The server_type of this ServerModel.
        :type server_type: str
        """
        self._server_type = server_type

    @property
    def cpu(self):
        r"""Gets the cpu of this ServerModel.

        云手机服务器的CPU核数。

        :return: The cpu of this ServerModel.
        :rtype: int
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        r"""Sets the cpu of this ServerModel.

        云手机服务器的CPU核数。

        :param cpu: The cpu of this ServerModel.
        :type cpu: int
        """
        self._cpu = cpu

    @property
    def memory(self):
        r"""Gets the memory of this ServerModel.

        云手机服务器的内存大小，单位G。

        :return: The memory of this ServerModel.
        :rtype: int
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        r"""Sets the memory of this ServerModel.

        云手机服务器的内存大小，单位G。

        :param memory: The memory of this ServerModel.
        :type memory: int
        """
        self._memory = memory

    @property
    def extend_spec(self):
        r"""Gets the extend_spec of this ServerModel.

        :return: The extend_spec of this ServerModel.
        :rtype: :class:`huaweicloudsdkcph.v1.ServerModelExtendSpec`
        """
        return self._extend_spec

    @extend_spec.setter
    def extend_spec(self, extend_spec):
        r"""Sets the extend_spec of this ServerModel.

        :param extend_spec: The extend_spec of this ServerModel.
        :type extend_spec: :class:`huaweicloudsdkcph.v1.ServerModelExtendSpec`
        """
        self._extend_spec = extend_spec

    @property
    def disk_max_num(self):
        r"""Gets the disk_max_num of this ServerModel.

        云手机服务器最大挂载磁盘数量。值为0时表示该机型磁盘为本地盘。

        :return: The disk_max_num of this ServerModel.
        :rtype: int
        """
        return self._disk_max_num

    @disk_max_num.setter
    def disk_max_num(self, disk_max_num):
        r"""Sets the disk_max_num of this ServerModel.

        云手机服务器最大挂载磁盘数量。值为0时表示该机型磁盘为本地盘。

        :param disk_max_num: The disk_max_num of this ServerModel.
        :type disk_max_num: int
        """
        self._disk_max_num = disk_max_num

    @property
    def product_type(self):
        r"""Gets the product_type of this ServerModel.

        产品类型。 - 0：云手机 - 1：云手游

        :return: The product_type of this ServerModel.
        :rtype: int
        """
        return self._product_type

    @product_type.setter
    def product_type(self, product_type):
        r"""Sets the product_type of this ServerModel.

        产品类型。 - 0：云手机 - 1：云手游

        :param product_type: The product_type of this ServerModel.
        :type product_type: int
        """
        self._product_type = product_type

    @property
    def free_size(self):
        r"""Gets the free_size of this ServerModel.

        服务器磁盘的免费配额，单位G。

        :return: The free_size of this ServerModel.
        :rtype: int
        """
        return self._free_size

    @free_size.setter
    def free_size(self, free_size):
        r"""Sets the free_size of this ServerModel.

        服务器磁盘的免费配额，单位G。

        :param free_size: The free_size of this ServerModel.
        :type free_size: int
        """
        self._free_size = free_size

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
        if not isinstance(other, ServerModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
