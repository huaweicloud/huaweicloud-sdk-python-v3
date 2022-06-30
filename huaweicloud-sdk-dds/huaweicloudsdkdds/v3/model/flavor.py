# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Flavor:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'engine_name': 'str',
        'type': 'str',
        'vcpus': 'str',
        'ram': 'str',
        'spec_code': 'str',
        'az_status': 'object'
    }

    attribute_map = {
        'engine_name': 'engine_name',
        'type': 'type',
        'vcpus': 'vcpus',
        'ram': 'ram',
        'spec_code': 'spec_code',
        'az_status': 'az_status'
    }

    def __init__(self, engine_name=None, type=None, vcpus=None, ram=None, spec_code=None, az_status=None):
        """Flavor

        The model defined in huaweicloud sdk

        :param engine_name: 引擎名称。
        :type engine_name: str
        :param type: 节点类型。文档数据库包含以下几种节点类型： - mongos - shard - config - replica - single
        :type type: str
        :param vcpus: CPU核数。
        :type vcpus: str
        :param ram: 内存大小，单位为兆字节。
        :type ram: str
        :param spec_code: 资源规格编码。例如：dds.mongodb.c6.xlarge.2.shard。  - “dds”表示文档数据库服务产品。 - “c6.xlarge.2”表示节点性能规格，为高内存类型。 - “shard”表示节点类型。
        :type spec_code: str
        :param az_status: &#39;支持该规格的可用区ID。&#39; 示例：[\&quot;cn-east-2a\&quot;,\&quot;cn-east-2b\&quot;,\&quot;cn-east-2c\&quot;]。
        :type az_status: object
        """
        
        

        self._engine_name = None
        self._type = None
        self._vcpus = None
        self._ram = None
        self._spec_code = None
        self._az_status = None
        self.discriminator = None

        self.engine_name = engine_name
        self.type = type
        self.vcpus = vcpus
        self.ram = ram
        self.spec_code = spec_code
        self.az_status = az_status

    @property
    def engine_name(self):
        """Gets the engine_name of this Flavor.

        引擎名称。

        :return: The engine_name of this Flavor.
        :rtype: str
        """
        return self._engine_name

    @engine_name.setter
    def engine_name(self, engine_name):
        """Sets the engine_name of this Flavor.

        引擎名称。

        :param engine_name: The engine_name of this Flavor.
        :type engine_name: str
        """
        self._engine_name = engine_name

    @property
    def type(self):
        """Gets the type of this Flavor.

        节点类型。文档数据库包含以下几种节点类型： - mongos - shard - config - replica - single

        :return: The type of this Flavor.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Flavor.

        节点类型。文档数据库包含以下几种节点类型： - mongos - shard - config - replica - single

        :param type: The type of this Flavor.
        :type type: str
        """
        self._type = type

    @property
    def vcpus(self):
        """Gets the vcpus of this Flavor.

        CPU核数。

        :return: The vcpus of this Flavor.
        :rtype: str
        """
        return self._vcpus

    @vcpus.setter
    def vcpus(self, vcpus):
        """Sets the vcpus of this Flavor.

        CPU核数。

        :param vcpus: The vcpus of this Flavor.
        :type vcpus: str
        """
        self._vcpus = vcpus

    @property
    def ram(self):
        """Gets the ram of this Flavor.

        内存大小，单位为兆字节。

        :return: The ram of this Flavor.
        :rtype: str
        """
        return self._ram

    @ram.setter
    def ram(self, ram):
        """Sets the ram of this Flavor.

        内存大小，单位为兆字节。

        :param ram: The ram of this Flavor.
        :type ram: str
        """
        self._ram = ram

    @property
    def spec_code(self):
        """Gets the spec_code of this Flavor.

        资源规格编码。例如：dds.mongodb.c6.xlarge.2.shard。  - “dds”表示文档数据库服务产品。 - “c6.xlarge.2”表示节点性能规格，为高内存类型。 - “shard”表示节点类型。

        :return: The spec_code of this Flavor.
        :rtype: str
        """
        return self._spec_code

    @spec_code.setter
    def spec_code(self, spec_code):
        """Sets the spec_code of this Flavor.

        资源规格编码。例如：dds.mongodb.c6.xlarge.2.shard。  - “dds”表示文档数据库服务产品。 - “c6.xlarge.2”表示节点性能规格，为高内存类型。 - “shard”表示节点类型。

        :param spec_code: The spec_code of this Flavor.
        :type spec_code: str
        """
        self._spec_code = spec_code

    @property
    def az_status(self):
        """Gets the az_status of this Flavor.

        '支持该规格的可用区ID。' 示例：[\"cn-east-2a\",\"cn-east-2b\",\"cn-east-2c\"]。

        :return: The az_status of this Flavor.
        :rtype: object
        """
        return self._az_status

    @az_status.setter
    def az_status(self, az_status):
        """Sets the az_status of this Flavor.

        '支持该规格的可用区ID。' 示例：[\"cn-east-2a\",\"cn-east-2b\",\"cn-east-2c\"]。

        :param az_status: The az_status of this Flavor.
        :type az_status: object
        """
        self._az_status = az_status

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
        if not isinstance(other, Flavor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
