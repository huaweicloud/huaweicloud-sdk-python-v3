# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FlavorInfo:

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
        'az_status': 'object',
        'engine_versions': 'list[str]'
    }

    attribute_map = {
        'engine_name': 'engine_name',
        'type': 'type',
        'vcpus': 'vcpus',
        'ram': 'ram',
        'spec_code': 'spec_code',
        'az_status': 'az_status',
        'engine_versions': 'engine_versions'
    }

    def __init__(self, engine_name=None, type=None, vcpus=None, ram=None, spec_code=None, az_status=None, engine_versions=None):
        """FlavorInfo

        The model defined in huaweicloud sdk

        :param engine_name: 引擎名称。
        :type engine_name: str
        :param type: 节点类型。文档数据库包含以下几种节点类型： - mongos - shard - config - replica - single - readonly
        :type type: str
        :param vcpus: CPU核数。
        :type vcpus: str
        :param ram: 内存大小，单位为兆字节。
        :type ram: str
        :param spec_code: 资源规格编码。例如：dds.mongodb.c6.xlarge.2.shard。  - “dds”表示文档数据库服务产品。 - “c6.xlarge.2”表示节点性能规格，为高内存类型。 - “shard”表示节点类型。
        :type spec_code: str
        :param az_status: &#39;支持该规格的可用区ID。&#39; 示例：[\&quot;cn-east-2a\&quot;,\&quot;cn-east-2b\&quot;,\&quot;cn-east-2c\&quot;]。
        :type az_status: object
        :param engine_versions: 数据库版本号列表。针对DDS引擎的mongos节点，例如：{\&quot;3.4\&quot;, \&quot;4.0\&quot;}
        :type engine_versions: list[str]
        """
        
        

        self._engine_name = None
        self._type = None
        self._vcpus = None
        self._ram = None
        self._spec_code = None
        self._az_status = None
        self._engine_versions = None
        self.discriminator = None

        self.engine_name = engine_name
        self.type = type
        self.vcpus = vcpus
        self.ram = ram
        self.spec_code = spec_code
        self.az_status = az_status
        self.engine_versions = engine_versions

    @property
    def engine_name(self):
        """Gets the engine_name of this FlavorInfo.

        引擎名称。

        :return: The engine_name of this FlavorInfo.
        :rtype: str
        """
        return self._engine_name

    @engine_name.setter
    def engine_name(self, engine_name):
        """Sets the engine_name of this FlavorInfo.

        引擎名称。

        :param engine_name: The engine_name of this FlavorInfo.
        :type engine_name: str
        """
        self._engine_name = engine_name

    @property
    def type(self):
        """Gets the type of this FlavorInfo.

        节点类型。文档数据库包含以下几种节点类型： - mongos - shard - config - replica - single - readonly

        :return: The type of this FlavorInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this FlavorInfo.

        节点类型。文档数据库包含以下几种节点类型： - mongos - shard - config - replica - single - readonly

        :param type: The type of this FlavorInfo.
        :type type: str
        """
        self._type = type

    @property
    def vcpus(self):
        """Gets the vcpus of this FlavorInfo.

        CPU核数。

        :return: The vcpus of this FlavorInfo.
        :rtype: str
        """
        return self._vcpus

    @vcpus.setter
    def vcpus(self, vcpus):
        """Sets the vcpus of this FlavorInfo.

        CPU核数。

        :param vcpus: The vcpus of this FlavorInfo.
        :type vcpus: str
        """
        self._vcpus = vcpus

    @property
    def ram(self):
        """Gets the ram of this FlavorInfo.

        内存大小，单位为兆字节。

        :return: The ram of this FlavorInfo.
        :rtype: str
        """
        return self._ram

    @ram.setter
    def ram(self, ram):
        """Sets the ram of this FlavorInfo.

        内存大小，单位为兆字节。

        :param ram: The ram of this FlavorInfo.
        :type ram: str
        """
        self._ram = ram

    @property
    def spec_code(self):
        """Gets the spec_code of this FlavorInfo.

        资源规格编码。例如：dds.mongodb.c6.xlarge.2.shard。  - “dds”表示文档数据库服务产品。 - “c6.xlarge.2”表示节点性能规格，为高内存类型。 - “shard”表示节点类型。

        :return: The spec_code of this FlavorInfo.
        :rtype: str
        """
        return self._spec_code

    @spec_code.setter
    def spec_code(self, spec_code):
        """Sets the spec_code of this FlavorInfo.

        资源规格编码。例如：dds.mongodb.c6.xlarge.2.shard。  - “dds”表示文档数据库服务产品。 - “c6.xlarge.2”表示节点性能规格，为高内存类型。 - “shard”表示节点类型。

        :param spec_code: The spec_code of this FlavorInfo.
        :type spec_code: str
        """
        self._spec_code = spec_code

    @property
    def az_status(self):
        """Gets the az_status of this FlavorInfo.

        '支持该规格的可用区ID。' 示例：[\"cn-east-2a\",\"cn-east-2b\",\"cn-east-2c\"]。

        :return: The az_status of this FlavorInfo.
        :rtype: object
        """
        return self._az_status

    @az_status.setter
    def az_status(self, az_status):
        """Sets the az_status of this FlavorInfo.

        '支持该规格的可用区ID。' 示例：[\"cn-east-2a\",\"cn-east-2b\",\"cn-east-2c\"]。

        :param az_status: The az_status of this FlavorInfo.
        :type az_status: object
        """
        self._az_status = az_status

    @property
    def engine_versions(self):
        """Gets the engine_versions of this FlavorInfo.

        数据库版本号列表。针对DDS引擎的mongos节点，例如：{\"3.4\", \"4.0\"}

        :return: The engine_versions of this FlavorInfo.
        :rtype: list[str]
        """
        return self._engine_versions

    @engine_versions.setter
    def engine_versions(self, engine_versions):
        """Sets the engine_versions of this FlavorInfo.

        数据库版本号列表。针对DDS引擎的mongos节点，例如：{\"3.4\", \"4.0\"}

        :param engine_versions: The engine_versions of this FlavorInfo.
        :type engine_versions: list[str]
        """
        self._engine_versions = engine_versions

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
        if not isinstance(other, FlavorInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
