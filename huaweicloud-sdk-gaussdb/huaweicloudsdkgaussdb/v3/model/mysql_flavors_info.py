# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MysqlFlavorsInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vcpus': 'str',
        'ram': 'str',
        'type': 'str',
        'id': 'str',
        'spec_code': 'str',
        'version_name': 'str',
        'instance_mode': 'str',
        'az_status': 'dict(str, str)'
    }

    attribute_map = {
        'vcpus': 'vcpus',
        'ram': 'ram',
        'type': 'type',
        'id': 'id',
        'spec_code': 'spec_code',
        'version_name': 'version_name',
        'instance_mode': 'instance_mode',
        'az_status': 'az_status'
    }

    def __init__(self, vcpus=None, ram=None, type=None, id=None, spec_code=None, version_name=None, instance_mode=None, az_status=None):
        """MysqlFlavorsInfo

        The model defined in huaweicloud sdk

        :param vcpus: CPU大小。例如：1表示1U。
        :type vcpus: str
        :param ram: 内存大小，单位为GB。
        :type ram: str
        :param type: 规格类型，取值为arm、x86和generalX86。  - arm：独享型arm规格。 - x86：独享型x86规格。 - generalX86：通用型X86规格。
        :type type: str
        :param id: 规格ID，该字段唯一
        :type id: str
        :param spec_code: 资源规格编码，同创建指定的flavor_ref。例如：gaussdb.mysql.xlarge.x86.4。
        :type spec_code: str
        :param version_name: 数据库版本号。
        :type version_name: str
        :param instance_mode: 实例类型。目前仅支持Cluster。
        :type instance_mode: str
        :param az_status: 规格所在az的状态，包含以下状态：  - normal，在售 - unsupported，暂不支持该规格 - sellout，售罄。
        :type az_status: dict(str, str)
        """
        
        

        self._vcpus = None
        self._ram = None
        self._type = None
        self._id = None
        self._spec_code = None
        self._version_name = None
        self._instance_mode = None
        self._az_status = None
        self.discriminator = None

        self.vcpus = vcpus
        self.ram = ram
        self.type = type
        self.id = id
        self.spec_code = spec_code
        self.version_name = version_name
        self.instance_mode = instance_mode
        self.az_status = az_status

    @property
    def vcpus(self):
        """Gets the vcpus of this MysqlFlavorsInfo.

        CPU大小。例如：1表示1U。

        :return: The vcpus of this MysqlFlavorsInfo.
        :rtype: str
        """
        return self._vcpus

    @vcpus.setter
    def vcpus(self, vcpus):
        """Sets the vcpus of this MysqlFlavorsInfo.

        CPU大小。例如：1表示1U。

        :param vcpus: The vcpus of this MysqlFlavorsInfo.
        :type vcpus: str
        """
        self._vcpus = vcpus

    @property
    def ram(self):
        """Gets the ram of this MysqlFlavorsInfo.

        内存大小，单位为GB。

        :return: The ram of this MysqlFlavorsInfo.
        :rtype: str
        """
        return self._ram

    @ram.setter
    def ram(self, ram):
        """Sets the ram of this MysqlFlavorsInfo.

        内存大小，单位为GB。

        :param ram: The ram of this MysqlFlavorsInfo.
        :type ram: str
        """
        self._ram = ram

    @property
    def type(self):
        """Gets the type of this MysqlFlavorsInfo.

        规格类型，取值为arm、x86和generalX86。  - arm：独享型arm规格。 - x86：独享型x86规格。 - generalX86：通用型X86规格。

        :return: The type of this MysqlFlavorsInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this MysqlFlavorsInfo.

        规格类型，取值为arm、x86和generalX86。  - arm：独享型arm规格。 - x86：独享型x86规格。 - generalX86：通用型X86规格。

        :param type: The type of this MysqlFlavorsInfo.
        :type type: str
        """
        self._type = type

    @property
    def id(self):
        """Gets the id of this MysqlFlavorsInfo.

        规格ID，该字段唯一

        :return: The id of this MysqlFlavorsInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MysqlFlavorsInfo.

        规格ID，该字段唯一

        :param id: The id of this MysqlFlavorsInfo.
        :type id: str
        """
        self._id = id

    @property
    def spec_code(self):
        """Gets the spec_code of this MysqlFlavorsInfo.

        资源规格编码，同创建指定的flavor_ref。例如：gaussdb.mysql.xlarge.x86.4。

        :return: The spec_code of this MysqlFlavorsInfo.
        :rtype: str
        """
        return self._spec_code

    @spec_code.setter
    def spec_code(self, spec_code):
        """Sets the spec_code of this MysqlFlavorsInfo.

        资源规格编码，同创建指定的flavor_ref。例如：gaussdb.mysql.xlarge.x86.4。

        :param spec_code: The spec_code of this MysqlFlavorsInfo.
        :type spec_code: str
        """
        self._spec_code = spec_code

    @property
    def version_name(self):
        """Gets the version_name of this MysqlFlavorsInfo.

        数据库版本号。

        :return: The version_name of this MysqlFlavorsInfo.
        :rtype: str
        """
        return self._version_name

    @version_name.setter
    def version_name(self, version_name):
        """Sets the version_name of this MysqlFlavorsInfo.

        数据库版本号。

        :param version_name: The version_name of this MysqlFlavorsInfo.
        :type version_name: str
        """
        self._version_name = version_name

    @property
    def instance_mode(self):
        """Gets the instance_mode of this MysqlFlavorsInfo.

        实例类型。目前仅支持Cluster。

        :return: The instance_mode of this MysqlFlavorsInfo.
        :rtype: str
        """
        return self._instance_mode

    @instance_mode.setter
    def instance_mode(self, instance_mode):
        """Sets the instance_mode of this MysqlFlavorsInfo.

        实例类型。目前仅支持Cluster。

        :param instance_mode: The instance_mode of this MysqlFlavorsInfo.
        :type instance_mode: str
        """
        self._instance_mode = instance_mode

    @property
    def az_status(self):
        """Gets the az_status of this MysqlFlavorsInfo.

        规格所在az的状态，包含以下状态：  - normal，在售 - unsupported，暂不支持该规格 - sellout，售罄。

        :return: The az_status of this MysqlFlavorsInfo.
        :rtype: dict(str, str)
        """
        return self._az_status

    @az_status.setter
    def az_status(self, az_status):
        """Sets the az_status of this MysqlFlavorsInfo.

        规格所在az的状态，包含以下状态：  - normal，在售 - unsupported，暂不支持该规格 - sellout，售罄。

        :param az_status: The az_status of this MysqlFlavorsInfo.
        :type az_status: dict(str, str)
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
        if not isinstance(other, MysqlFlavorsInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
