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
        'id': 'str',
        'vcpus': 'str',
        'ram': 'int',
        'spec_code': 'str',
        'instance_mode': 'str',
        'az_status': 'dict(str, str)',
        'az_desc': 'dict(str, str)',
        'version_name': 'list[str]',
        'group_type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'vcpus': 'vcpus',
        'ram': 'ram',
        'spec_code': 'spec_code',
        'instance_mode': 'instance_mode',
        'az_status': 'az_status',
        'az_desc': 'az_desc',
        'version_name': 'version_name',
        'group_type': 'group_type'
    }

    def __init__(self, id=None, vcpus=None, ram=None, spec_code=None, instance_mode=None, az_status=None, az_desc=None, version_name=None, group_type=None):
        """Flavor

        The model defined in huaweicloud sdk

        :param id: 规格id
        :type id: str
        :param vcpus: CPU个数。
        :type vcpus: str
        :param ram: 内存大小，单位为GB。
        :type ram: int
        :param spec_code: 资源规格编码。例如：rds.mysql.m1.xlarge.rr。  其中形如“xxx.xxx.mcs.i3.xxx.xxx.xxx”是超高性能型（尊享版），需要申请一定权限才可使用，更多规格说明请参考数据库实例规格。 - “rds”代表RDS产品。 - “mysql”代表数据库引擎。 - “m1.xlarge”代表性能规格，为高内存类型。
        :type spec_code: str
        :param instance_mode: 实例模型，包括如下类型： - ha，主备实例。 - replica，只读实例。 - single，单实例。
        :type instance_mode: str
        :param az_status: 其中key是可用区编号，value是规格所在az的状态，包含以下状态： - normal，在售。 - unsupported，暂不支持该规格。 - sellout，售罄。
        :type az_status: dict(str, str)
        :param az_desc: 规格所在az的描述。
        :type az_desc: dict(str, str)
        :param version_name: 数组形式版本号
        :type version_name: list[str]
        :param group_type: 性能规格，包含以下状态： - normal：通用增强型。 - normal2：通用增强Ⅱ型。 - armFlavors：鲲鹏通用增强型。 - dedicicatenormal ：x86独享型。 - armlocalssd：鲲鹏通用型。 - normallocalssd：x86通用型。 - general：通用型。 - dedicated：独享型，仅云盘SSD支持。 - rapid：独享型，仅极速型SSD支持。 - bigmen：超大内存型。
        :type group_type: str
        """
        
        

        self._id = None
        self._vcpus = None
        self._ram = None
        self._spec_code = None
        self._instance_mode = None
        self._az_status = None
        self._az_desc = None
        self._version_name = None
        self._group_type = None
        self.discriminator = None

        self.id = id
        self.vcpus = vcpus
        self.ram = ram
        self.spec_code = spec_code
        self.instance_mode = instance_mode
        self.az_status = az_status
        self.az_desc = az_desc
        self.version_name = version_name
        self.group_type = group_type

    @property
    def id(self):
        """Gets the id of this Flavor.

        规格id

        :return: The id of this Flavor.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Flavor.

        规格id

        :param id: The id of this Flavor.
        :type id: str
        """
        self._id = id

    @property
    def vcpus(self):
        """Gets the vcpus of this Flavor.

        CPU个数。

        :return: The vcpus of this Flavor.
        :rtype: str
        """
        return self._vcpus

    @vcpus.setter
    def vcpus(self, vcpus):
        """Sets the vcpus of this Flavor.

        CPU个数。

        :param vcpus: The vcpus of this Flavor.
        :type vcpus: str
        """
        self._vcpus = vcpus

    @property
    def ram(self):
        """Gets the ram of this Flavor.

        内存大小，单位为GB。

        :return: The ram of this Flavor.
        :rtype: int
        """
        return self._ram

    @ram.setter
    def ram(self, ram):
        """Sets the ram of this Flavor.

        内存大小，单位为GB。

        :param ram: The ram of this Flavor.
        :type ram: int
        """
        self._ram = ram

    @property
    def spec_code(self):
        """Gets the spec_code of this Flavor.

        资源规格编码。例如：rds.mysql.m1.xlarge.rr。  其中形如“xxx.xxx.mcs.i3.xxx.xxx.xxx”是超高性能型（尊享版），需要申请一定权限才可使用，更多规格说明请参考数据库实例规格。 - “rds”代表RDS产品。 - “mysql”代表数据库引擎。 - “m1.xlarge”代表性能规格，为高内存类型。

        :return: The spec_code of this Flavor.
        :rtype: str
        """
        return self._spec_code

    @spec_code.setter
    def spec_code(self, spec_code):
        """Sets the spec_code of this Flavor.

        资源规格编码。例如：rds.mysql.m1.xlarge.rr。  其中形如“xxx.xxx.mcs.i3.xxx.xxx.xxx”是超高性能型（尊享版），需要申请一定权限才可使用，更多规格说明请参考数据库实例规格。 - “rds”代表RDS产品。 - “mysql”代表数据库引擎。 - “m1.xlarge”代表性能规格，为高内存类型。

        :param spec_code: The spec_code of this Flavor.
        :type spec_code: str
        """
        self._spec_code = spec_code

    @property
    def instance_mode(self):
        """Gets the instance_mode of this Flavor.

        实例模型，包括如下类型： - ha，主备实例。 - replica，只读实例。 - single，单实例。

        :return: The instance_mode of this Flavor.
        :rtype: str
        """
        return self._instance_mode

    @instance_mode.setter
    def instance_mode(self, instance_mode):
        """Sets the instance_mode of this Flavor.

        实例模型，包括如下类型： - ha，主备实例。 - replica，只读实例。 - single，单实例。

        :param instance_mode: The instance_mode of this Flavor.
        :type instance_mode: str
        """
        self._instance_mode = instance_mode

    @property
    def az_status(self):
        """Gets the az_status of this Flavor.

        其中key是可用区编号，value是规格所在az的状态，包含以下状态： - normal，在售。 - unsupported，暂不支持该规格。 - sellout，售罄。

        :return: The az_status of this Flavor.
        :rtype: dict(str, str)
        """
        return self._az_status

    @az_status.setter
    def az_status(self, az_status):
        """Sets the az_status of this Flavor.

        其中key是可用区编号，value是规格所在az的状态，包含以下状态： - normal，在售。 - unsupported，暂不支持该规格。 - sellout，售罄。

        :param az_status: The az_status of this Flavor.
        :type az_status: dict(str, str)
        """
        self._az_status = az_status

    @property
    def az_desc(self):
        """Gets the az_desc of this Flavor.

        规格所在az的描述。

        :return: The az_desc of this Flavor.
        :rtype: dict(str, str)
        """
        return self._az_desc

    @az_desc.setter
    def az_desc(self, az_desc):
        """Sets the az_desc of this Flavor.

        规格所在az的描述。

        :param az_desc: The az_desc of this Flavor.
        :type az_desc: dict(str, str)
        """
        self._az_desc = az_desc

    @property
    def version_name(self):
        """Gets the version_name of this Flavor.

        数组形式版本号

        :return: The version_name of this Flavor.
        :rtype: list[str]
        """
        return self._version_name

    @version_name.setter
    def version_name(self, version_name):
        """Sets the version_name of this Flavor.

        数组形式版本号

        :param version_name: The version_name of this Flavor.
        :type version_name: list[str]
        """
        self._version_name = version_name

    @property
    def group_type(self):
        """Gets the group_type of this Flavor.

        性能规格，包含以下状态： - normal：通用增强型。 - normal2：通用增强Ⅱ型。 - armFlavors：鲲鹏通用增强型。 - dedicicatenormal ：x86独享型。 - armlocalssd：鲲鹏通用型。 - normallocalssd：x86通用型。 - general：通用型。 - dedicated：独享型，仅云盘SSD支持。 - rapid：独享型，仅极速型SSD支持。 - bigmen：超大内存型。

        :return: The group_type of this Flavor.
        :rtype: str
        """
        return self._group_type

    @group_type.setter
    def group_type(self, group_type):
        """Sets the group_type of this Flavor.

        性能规格，包含以下状态： - normal：通用增强型。 - normal2：通用增强Ⅱ型。 - armFlavors：鲲鹏通用增强型。 - dedicicatenormal ：x86独享型。 - armlocalssd：鲲鹏通用型。 - normallocalssd：x86通用型。 - general：通用型。 - dedicated：独享型，仅云盘SSD支持。 - rapid：独享型，仅极速型SSD支持。 - bigmen：超大内存型。

        :param group_type: The group_type of this Flavor.
        :type group_type: str
        """
        self._group_type = group_type

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
