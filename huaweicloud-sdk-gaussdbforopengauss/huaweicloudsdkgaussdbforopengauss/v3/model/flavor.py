# coding: utf-8

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
        'vcpus': 'str',
        'ram': 'str',
        'spec_code': 'str',
        'availability_zone': 'list[str]',
        'az_status': 'dict(str, str)',
        'version': 'str',
        'name': 'str',
        'group_type': 'str'
    }

    attribute_map = {
        'vcpus': 'vcpus',
        'ram': 'ram',
        'spec_code': 'spec_code',
        'availability_zone': 'availability_zone',
        'az_status': 'az_status',
        'version': 'version',
        'name': 'name',
        'group_type': 'group_type'
    }

    def __init__(self, vcpus=None, ram=None, spec_code=None, availability_zone=None, az_status=None, version=None, name=None, group_type=None):
        r"""Flavor

        The model defined in huaweicloud sdk

        :param vcpus: CPU个数。
        :type vcpus: str
        :param ram: 内存大小，单位为GB。
        :type ram: str
        :param spec_code: 资源规格编码。例如：gaussdb.opengauss.ee.dn.m6.4xlarge.8.in。
        :type spec_code: str
        :param availability_zone: 可用az
        :type availability_zone: list[str]
        :param az_status: 其中key是可用区编号，value是规格所在az的状态，包含以下状态： - normal，在售。 - unsupported，暂不支持该规格。 - sellout，售罄。
        :type az_status: dict(str, str)
        :param version: 该规格支持的数据库版本号
        :type version: str
        :param name: 数组库引擎名称
        :type name: str
        :param group_type: 性能规格，包含以下状态： - normal：通用增强型。 - normal2：通用增强Ⅱ型。 - armFlavors：鲲鹏通用增强型。 - dedicicatenormal ：x86独享型。 - armlocalssd：鲲鹏通用型。 - normallocalssd：x86通用型。 - general：通用型。 - dedicated：独享型，仅云盘SSD支持。 - rapid：独享型，仅极速型SSD支持。
        :type group_type: str
        """
        
        

        self._vcpus = None
        self._ram = None
        self._spec_code = None
        self._availability_zone = None
        self._az_status = None
        self._version = None
        self._name = None
        self._group_type = None
        self.discriminator = None

        self.vcpus = vcpus
        self.ram = ram
        self.spec_code = spec_code
        self.availability_zone = availability_zone
        self.az_status = az_status
        self.version = version
        self.name = name
        self.group_type = group_type

    @property
    def vcpus(self):
        r"""Gets the vcpus of this Flavor.

        CPU个数。

        :return: The vcpus of this Flavor.
        :rtype: str
        """
        return self._vcpus

    @vcpus.setter
    def vcpus(self, vcpus):
        r"""Sets the vcpus of this Flavor.

        CPU个数。

        :param vcpus: The vcpus of this Flavor.
        :type vcpus: str
        """
        self._vcpus = vcpus

    @property
    def ram(self):
        r"""Gets the ram of this Flavor.

        内存大小，单位为GB。

        :return: The ram of this Flavor.
        :rtype: str
        """
        return self._ram

    @ram.setter
    def ram(self, ram):
        r"""Sets the ram of this Flavor.

        内存大小，单位为GB。

        :param ram: The ram of this Flavor.
        :type ram: str
        """
        self._ram = ram

    @property
    def spec_code(self):
        r"""Gets the spec_code of this Flavor.

        资源规格编码。例如：gaussdb.opengauss.ee.dn.m6.4xlarge.8.in。

        :return: The spec_code of this Flavor.
        :rtype: str
        """
        return self._spec_code

    @spec_code.setter
    def spec_code(self, spec_code):
        r"""Sets the spec_code of this Flavor.

        资源规格编码。例如：gaussdb.opengauss.ee.dn.m6.4xlarge.8.in。

        :param spec_code: The spec_code of this Flavor.
        :type spec_code: str
        """
        self._spec_code = spec_code

    @property
    def availability_zone(self):
        r"""Gets the availability_zone of this Flavor.

        可用az

        :return: The availability_zone of this Flavor.
        :rtype: list[str]
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        r"""Sets the availability_zone of this Flavor.

        可用az

        :param availability_zone: The availability_zone of this Flavor.
        :type availability_zone: list[str]
        """
        self._availability_zone = availability_zone

    @property
    def az_status(self):
        r"""Gets the az_status of this Flavor.

        其中key是可用区编号，value是规格所在az的状态，包含以下状态： - normal，在售。 - unsupported，暂不支持该规格。 - sellout，售罄。

        :return: The az_status of this Flavor.
        :rtype: dict(str, str)
        """
        return self._az_status

    @az_status.setter
    def az_status(self, az_status):
        r"""Sets the az_status of this Flavor.

        其中key是可用区编号，value是规格所在az的状态，包含以下状态： - normal，在售。 - unsupported，暂不支持该规格。 - sellout，售罄。

        :param az_status: The az_status of this Flavor.
        :type az_status: dict(str, str)
        """
        self._az_status = az_status

    @property
    def version(self):
        r"""Gets the version of this Flavor.

        该规格支持的数据库版本号

        :return: The version of this Flavor.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this Flavor.

        该规格支持的数据库版本号

        :param version: The version of this Flavor.
        :type version: str
        """
        self._version = version

    @property
    def name(self):
        r"""Gets the name of this Flavor.

        数组库引擎名称

        :return: The name of this Flavor.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this Flavor.

        数组库引擎名称

        :param name: The name of this Flavor.
        :type name: str
        """
        self._name = name

    @property
    def group_type(self):
        r"""Gets the group_type of this Flavor.

        性能规格，包含以下状态： - normal：通用增强型。 - normal2：通用增强Ⅱ型。 - armFlavors：鲲鹏通用增强型。 - dedicicatenormal ：x86独享型。 - armlocalssd：鲲鹏通用型。 - normallocalssd：x86通用型。 - general：通用型。 - dedicated：独享型，仅云盘SSD支持。 - rapid：独享型，仅极速型SSD支持。

        :return: The group_type of this Flavor.
        :rtype: str
        """
        return self._group_type

    @group_type.setter
    def group_type(self, group_type):
        r"""Sets the group_type of this Flavor.

        性能规格，包含以下状态： - normal：通用增强型。 - normal2：通用增强Ⅱ型。 - armFlavors：鲲鹏通用增强型。 - dedicicatenormal ：x86独享型。 - armlocalssd：鲲鹏通用型。 - normallocalssd：x86通用型。 - general：通用型。 - dedicated：独享型，仅云盘SSD支持。 - rapid：独享型，仅极速型SSD支持。

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
