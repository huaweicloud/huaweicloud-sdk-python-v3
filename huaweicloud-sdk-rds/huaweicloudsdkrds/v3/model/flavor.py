# coding: utf-8

import pprint
import re

import six





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
        'version_name': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'vcpus': 'vcpus',
        'ram': 'ram',
        'spec_code': 'spec_code',
        'instance_mode': 'instance_mode',
        'az_status': 'az_status',
        'version_name': 'version_name'
    }

    def __init__(self, id=None, vcpus=None, ram=None, spec_code=None, instance_mode=None, az_status=None, version_name=None):
        """Flavor - a model defined in huaweicloud sdk"""
        
        

        self._id = None
        self._vcpus = None
        self._ram = None
        self._spec_code = None
        self._instance_mode = None
        self._az_status = None
        self._version_name = None
        self.discriminator = None

        self.id = id
        self.vcpus = vcpus
        self.ram = ram
        self.spec_code = spec_code
        self.instance_mode = instance_mode
        self.az_status = az_status
        self.version_name = version_name

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
        :type: str
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
        :type: str
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
        :type: int
        """
        self._ram = ram

    @property
    def spec_code(self):
        """Gets the spec_code of this Flavor.

        资源规格编码。例如：rds.mysql.m1.xlarge.rr。  其中形如“xxx.xxx.mcs.i3.xxx.xxx.xxx”是超高性能型（尊享版），需要申请一定权限才可使用，更多规格说明请参考数据库实例规格。 - “rds”代表RDS产品。 - “mysql”代表数据库引擎。 - “m1.xlarge”代表性能规格，为高内存类型。 - “rr”表示只读实例（“.ha”表示主备实例，“gr”表示MySQL金融版）。

        :return: The spec_code of this Flavor.
        :rtype: str
        """
        return self._spec_code

    @spec_code.setter
    def spec_code(self, spec_code):
        """Sets the spec_code of this Flavor.

        资源规格编码。例如：rds.mysql.m1.xlarge.rr。  其中形如“xxx.xxx.mcs.i3.xxx.xxx.xxx”是超高性能型（尊享版），需要申请一定权限才可使用，更多规格说明请参考数据库实例规格。 - “rds”代表RDS产品。 - “mysql”代表数据库引擎。 - “m1.xlarge”代表性能规格，为高内存类型。 - “rr”表示只读实例（“.ha”表示主备实例，“gr”表示MySQL金融版）。

        :param spec_code: The spec_code of this Flavor.
        :type: str
        """
        self._spec_code = spec_code

    @property
    def instance_mode(self):
        """Gets the instance_mode of this Flavor.

        实例模型，包括如下类型： - ha，主备实例。 - replica，只读实例。 - single，单实例。 - gr，MySQL金融版。

        :return: The instance_mode of this Flavor.
        :rtype: str
        """
        return self._instance_mode

    @instance_mode.setter
    def instance_mode(self, instance_mode):
        """Sets the instance_mode of this Flavor.

        实例模型，包括如下类型： - ha，主备实例。 - replica，只读实例。 - single，单实例。 - gr，MySQL金融版。

        :param instance_mode: The instance_mode of this Flavor.
        :type: str
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
        :type: dict(str, str)
        """
        self._az_status = az_status

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
        :type: list[str]
        """
        self._version_name = version_name

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Flavor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
