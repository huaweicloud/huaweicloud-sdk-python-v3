# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFlavorsResult:


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
        'engine_version': 'str',
        'vcpus': 'str',
        'ram': 'str',
        'spec_code': 'str',
        'az_status': 'object'
    }

    attribute_map = {
        'engine_name': 'engine_name',
        'engine_version': 'engine_version',
        'vcpus': 'vcpus',
        'ram': 'ram',
        'spec_code': 'spec_code',
        'az_status': 'az_status'
    }

    def __init__(self, engine_name=None, engine_version=None, vcpus=None, ram=None, spec_code=None, az_status=None):
        """ListFlavorsResult - a model defined in huaweicloud sdk"""
        
        

        self._engine_name = None
        self._engine_version = None
        self._vcpus = None
        self._ram = None
        self._spec_code = None
        self._az_status = None
        self.discriminator = None

        self.engine_name = engine_name
        self.engine_version = engine_version
        self.vcpus = vcpus
        self.ram = ram
        self.spec_code = spec_code
        self.az_status = az_status

    @property
    def engine_name(self):
        """Gets the engine_name of this ListFlavorsResult.

        引擎名称。

        :return: The engine_name of this ListFlavorsResult.
        :rtype: str
        """
        return self._engine_name

    @engine_name.setter
    def engine_name(self, engine_name):
        """Sets the engine_name of this ListFlavorsResult.

        引擎名称。

        :param engine_name: The engine_name of this ListFlavorsResult.
        :type: str
        """
        self._engine_name = engine_name

    @property
    def engine_version(self):
        """Gets the engine_version of this ListFlavorsResult.

        引擎版本。

        :return: The engine_version of this ListFlavorsResult.
        :rtype: str
        """
        return self._engine_version

    @engine_version.setter
    def engine_version(self, engine_version):
        """Sets the engine_version of this ListFlavorsResult.

        引擎版本。

        :param engine_version: The engine_version of this ListFlavorsResult.
        :type: str
        """
        self._engine_version = engine_version

    @property
    def vcpus(self):
        """Gets the vcpus of this ListFlavorsResult.

        CPU核数。

        :return: The vcpus of this ListFlavorsResult.
        :rtype: str
        """
        return self._vcpus

    @vcpus.setter
    def vcpus(self, vcpus):
        """Sets the vcpus of this ListFlavorsResult.

        CPU核数。

        :param vcpus: The vcpus of this ListFlavorsResult.
        :type: str
        """
        self._vcpus = vcpus

    @property
    def ram(self):
        """Gets the ram of this ListFlavorsResult.

        内存大小，单位为兆字节。

        :return: The ram of this ListFlavorsResult.
        :rtype: str
        """
        return self._ram

    @ram.setter
    def ram(self, ram):
        """Sets the ram of this ListFlavorsResult.

        内存大小，单位为兆字节。

        :param ram: The ram of this ListFlavorsResult.
        :type: str
        """
        self._ram = ram

    @property
    def spec_code(self):
        """Gets the spec_code of this ListFlavorsResult.

        资源规格编码。例如：geminidb.cassandra.8xlarge.4   - “geminidb.cassandra”表示云数据库GaussDB NoSQL的Cassandra数据库产品。   - “8xlarge.4”表示节点性能规格。

        :return: The spec_code of this ListFlavorsResult.
        :rtype: str
        """
        return self._spec_code

    @spec_code.setter
    def spec_code(self, spec_code):
        """Sets the spec_code of this ListFlavorsResult.

        资源规格编码。例如：geminidb.cassandra.8xlarge.4   - “geminidb.cassandra”表示云数据库GaussDB NoSQL的Cassandra数据库产品。   - “8xlarge.4”表示节点性能规格。

        :param spec_code: The spec_code of this ListFlavorsResult.
        :type: str
        """
        self._spec_code = spec_code

    @property
    def az_status(self):
        """Gets the az_status of this ListFlavorsResult.

        规格在可用区内的状态，包含以下状态：   - normal，在售。   - unsupported，暂不支持该规格。   - sellout，售罄。

        :return: The az_status of this ListFlavorsResult.
        :rtype: object
        """
        return self._az_status

    @az_status.setter
    def az_status(self, az_status):
        """Sets the az_status of this ListFlavorsResult.

        规格在可用区内的状态，包含以下状态：   - normal，在售。   - unsupported，暂不支持该规格。   - sellout，售罄。

        :param az_status: The az_status of this ListFlavorsResult.
        :type: object
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
        import simplejson as json
        return json.dumps(sanitize_for_serialization(self))

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListFlavorsResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
