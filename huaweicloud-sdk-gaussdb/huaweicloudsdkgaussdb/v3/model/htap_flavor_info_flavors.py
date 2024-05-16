# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HtapFlavorInfoFlavors:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'vcpus': 'str',
        'ram': 'str',
        'id': 'str',
        'spec_code': 'str',
        'version_name': 'str',
        'instance_mode': 'str',
        'az_status': 'dict(str, str)'
    }

    attribute_map = {
        'type': 'type',
        'vcpus': 'vcpus',
        'ram': 'ram',
        'id': 'id',
        'spec_code': 'spec_code',
        'version_name': 'version_name',
        'instance_mode': 'instance_mode',
        'az_status': 'az_status'
    }

    def __init__(self, type=None, vcpus=None, ram=None, id=None, spec_code=None, version_name=None, instance_mode=None, az_status=None):
        """HtapFlavorInfoFlavors

        The model defined in huaweicloud sdk

        :param type: 规格类型，取值为arm、x86和generalX86。  arm：独享型arm规格。  x86：独享型x86规格。  generalX86：通用型X86规格。
        :type type: str
        :param vcpus: CPU大小。例如：1表示1U。
        :type vcpus: str
        :param ram: 内存大小，单位为GB。
        :type ram: str
        :param id: 规格ID，该字段唯一。
        :type id: str
        :param spec_code: 资源规格编码，.同创建指定的flavor_ref。例如：gaussdb.sr-be.xlarge.x86.4。  “gaussdb.sr”代表产品。  “xlarge” 代表计算规格为4U。  “x86” 代表CPU架构为x86。  “4” 表示vCPU和内存为1:4。
        :type spec_code: str
        :param version_name: 数据库版本号。
        :type version_name: str
        :param instance_mode: 实例类型。目前仅支持Cluster、Single。
        :type instance_mode: str
        :param az_status: 规格所在AZ的状态，包含以下状态：  normal：在售。  unsupported：暂不支持该规格。  sellout：售罄。
        :type az_status: dict(str, str)
        """
        
        

        self._type = None
        self._vcpus = None
        self._ram = None
        self._id = None
        self._spec_code = None
        self._version_name = None
        self._instance_mode = None
        self._az_status = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if vcpus is not None:
            self.vcpus = vcpus
        if ram is not None:
            self.ram = ram
        if id is not None:
            self.id = id
        if spec_code is not None:
            self.spec_code = spec_code
        if version_name is not None:
            self.version_name = version_name
        if instance_mode is not None:
            self.instance_mode = instance_mode
        if az_status is not None:
            self.az_status = az_status

    @property
    def type(self):
        """Gets the type of this HtapFlavorInfoFlavors.

        规格类型，取值为arm、x86和generalX86。  arm：独享型arm规格。  x86：独享型x86规格。  generalX86：通用型X86规格。

        :return: The type of this HtapFlavorInfoFlavors.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this HtapFlavorInfoFlavors.

        规格类型，取值为arm、x86和generalX86。  arm：独享型arm规格。  x86：独享型x86规格。  generalX86：通用型X86规格。

        :param type: The type of this HtapFlavorInfoFlavors.
        :type type: str
        """
        self._type = type

    @property
    def vcpus(self):
        """Gets the vcpus of this HtapFlavorInfoFlavors.

        CPU大小。例如：1表示1U。

        :return: The vcpus of this HtapFlavorInfoFlavors.
        :rtype: str
        """
        return self._vcpus

    @vcpus.setter
    def vcpus(self, vcpus):
        """Sets the vcpus of this HtapFlavorInfoFlavors.

        CPU大小。例如：1表示1U。

        :param vcpus: The vcpus of this HtapFlavorInfoFlavors.
        :type vcpus: str
        """
        self._vcpus = vcpus

    @property
    def ram(self):
        """Gets the ram of this HtapFlavorInfoFlavors.

        内存大小，单位为GB。

        :return: The ram of this HtapFlavorInfoFlavors.
        :rtype: str
        """
        return self._ram

    @ram.setter
    def ram(self, ram):
        """Sets the ram of this HtapFlavorInfoFlavors.

        内存大小，单位为GB。

        :param ram: The ram of this HtapFlavorInfoFlavors.
        :type ram: str
        """
        self._ram = ram

    @property
    def id(self):
        """Gets the id of this HtapFlavorInfoFlavors.

        规格ID，该字段唯一。

        :return: The id of this HtapFlavorInfoFlavors.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this HtapFlavorInfoFlavors.

        规格ID，该字段唯一。

        :param id: The id of this HtapFlavorInfoFlavors.
        :type id: str
        """
        self._id = id

    @property
    def spec_code(self):
        """Gets the spec_code of this HtapFlavorInfoFlavors.

        资源规格编码，.同创建指定的flavor_ref。例如：gaussdb.sr-be.xlarge.x86.4。  “gaussdb.sr”代表产品。  “xlarge” 代表计算规格为4U。  “x86” 代表CPU架构为x86。  “4” 表示vCPU和内存为1:4。

        :return: The spec_code of this HtapFlavorInfoFlavors.
        :rtype: str
        """
        return self._spec_code

    @spec_code.setter
    def spec_code(self, spec_code):
        """Sets the spec_code of this HtapFlavorInfoFlavors.

        资源规格编码，.同创建指定的flavor_ref。例如：gaussdb.sr-be.xlarge.x86.4。  “gaussdb.sr”代表产品。  “xlarge” 代表计算规格为4U。  “x86” 代表CPU架构为x86。  “4” 表示vCPU和内存为1:4。

        :param spec_code: The spec_code of this HtapFlavorInfoFlavors.
        :type spec_code: str
        """
        self._spec_code = spec_code

    @property
    def version_name(self):
        """Gets the version_name of this HtapFlavorInfoFlavors.

        数据库版本号。

        :return: The version_name of this HtapFlavorInfoFlavors.
        :rtype: str
        """
        return self._version_name

    @version_name.setter
    def version_name(self, version_name):
        """Sets the version_name of this HtapFlavorInfoFlavors.

        数据库版本号。

        :param version_name: The version_name of this HtapFlavorInfoFlavors.
        :type version_name: str
        """
        self._version_name = version_name

    @property
    def instance_mode(self):
        """Gets the instance_mode of this HtapFlavorInfoFlavors.

        实例类型。目前仅支持Cluster、Single。

        :return: The instance_mode of this HtapFlavorInfoFlavors.
        :rtype: str
        """
        return self._instance_mode

    @instance_mode.setter
    def instance_mode(self, instance_mode):
        """Sets the instance_mode of this HtapFlavorInfoFlavors.

        实例类型。目前仅支持Cluster、Single。

        :param instance_mode: The instance_mode of this HtapFlavorInfoFlavors.
        :type instance_mode: str
        """
        self._instance_mode = instance_mode

    @property
    def az_status(self):
        """Gets the az_status of this HtapFlavorInfoFlavors.

        规格所在AZ的状态，包含以下状态：  normal：在售。  unsupported：暂不支持该规格。  sellout：售罄。

        :return: The az_status of this HtapFlavorInfoFlavors.
        :rtype: dict(str, str)
        """
        return self._az_status

    @az_status.setter
    def az_status(self, az_status):
        """Sets the az_status of this HtapFlavorInfoFlavors.

        规格所在AZ的状态，包含以下状态：  normal：在售。  unsupported：暂不支持该规格。  sellout：售罄。

        :param az_status: The az_status of this HtapFlavorInfoFlavors.
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
        if not isinstance(other, HtapFlavorInfoFlavors):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
