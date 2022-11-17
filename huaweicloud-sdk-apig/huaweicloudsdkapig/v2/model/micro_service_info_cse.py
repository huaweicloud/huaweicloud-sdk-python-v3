# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MicroServiceInfoCSE:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'engine_id': 'str',
        'service_id': 'str',
        'engine_name': 'str',
        'service_name': 'str',
        'register_address': 'str',
        'cse_app_id': 'str',
        'version': 'str'
    }

    attribute_map = {
        'engine_id': 'engine_id',
        'service_id': 'service_id',
        'engine_name': 'engine_name',
        'service_name': 'service_name',
        'register_address': 'register_address',
        'cse_app_id': 'cse_app_id',
        'version': 'version'
    }

    def __init__(self, engine_id=None, service_id=None, engine_name=None, service_name=None, register_address=None, cse_app_id=None, version=None):
        """MicroServiceInfoCSE

        The model defined in huaweicloud sdk

        :param engine_id: 微服务引擎编号
        :type engine_id: str
        :param service_id: 微服务编号
        :type service_id: str
        :param engine_name: 微服务引擎名称
        :type engine_name: str
        :param service_name: 微服务名称
        :type service_name: str
        :param register_address: 注册中心地址
        :type register_address: str
        :param cse_app_id: 微服务所属的应用
        :type cse_app_id: str
        :param version: 微服务的版本，已废弃，通过后端服务器组中的版本承载。
        :type version: str
        """
        
        

        self._engine_id = None
        self._service_id = None
        self._engine_name = None
        self._service_name = None
        self._register_address = None
        self._cse_app_id = None
        self._version = None
        self.discriminator = None

        self.engine_id = engine_id
        self.service_id = service_id
        if engine_name is not None:
            self.engine_name = engine_name
        if service_name is not None:
            self.service_name = service_name
        if register_address is not None:
            self.register_address = register_address
        if cse_app_id is not None:
            self.cse_app_id = cse_app_id
        if version is not None:
            self.version = version

    @property
    def engine_id(self):
        """Gets the engine_id of this MicroServiceInfoCSE.

        微服务引擎编号

        :return: The engine_id of this MicroServiceInfoCSE.
        :rtype: str
        """
        return self._engine_id

    @engine_id.setter
    def engine_id(self, engine_id):
        """Sets the engine_id of this MicroServiceInfoCSE.

        微服务引擎编号

        :param engine_id: The engine_id of this MicroServiceInfoCSE.
        :type engine_id: str
        """
        self._engine_id = engine_id

    @property
    def service_id(self):
        """Gets the service_id of this MicroServiceInfoCSE.

        微服务编号

        :return: The service_id of this MicroServiceInfoCSE.
        :rtype: str
        """
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        """Sets the service_id of this MicroServiceInfoCSE.

        微服务编号

        :param service_id: The service_id of this MicroServiceInfoCSE.
        :type service_id: str
        """
        self._service_id = service_id

    @property
    def engine_name(self):
        """Gets the engine_name of this MicroServiceInfoCSE.

        微服务引擎名称

        :return: The engine_name of this MicroServiceInfoCSE.
        :rtype: str
        """
        return self._engine_name

    @engine_name.setter
    def engine_name(self, engine_name):
        """Sets the engine_name of this MicroServiceInfoCSE.

        微服务引擎名称

        :param engine_name: The engine_name of this MicroServiceInfoCSE.
        :type engine_name: str
        """
        self._engine_name = engine_name

    @property
    def service_name(self):
        """Gets the service_name of this MicroServiceInfoCSE.

        微服务名称

        :return: The service_name of this MicroServiceInfoCSE.
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        """Sets the service_name of this MicroServiceInfoCSE.

        微服务名称

        :param service_name: The service_name of this MicroServiceInfoCSE.
        :type service_name: str
        """
        self._service_name = service_name

    @property
    def register_address(self):
        """Gets the register_address of this MicroServiceInfoCSE.

        注册中心地址

        :return: The register_address of this MicroServiceInfoCSE.
        :rtype: str
        """
        return self._register_address

    @register_address.setter
    def register_address(self, register_address):
        """Sets the register_address of this MicroServiceInfoCSE.

        注册中心地址

        :param register_address: The register_address of this MicroServiceInfoCSE.
        :type register_address: str
        """
        self._register_address = register_address

    @property
    def cse_app_id(self):
        """Gets the cse_app_id of this MicroServiceInfoCSE.

        微服务所属的应用

        :return: The cse_app_id of this MicroServiceInfoCSE.
        :rtype: str
        """
        return self._cse_app_id

    @cse_app_id.setter
    def cse_app_id(self, cse_app_id):
        """Sets the cse_app_id of this MicroServiceInfoCSE.

        微服务所属的应用

        :param cse_app_id: The cse_app_id of this MicroServiceInfoCSE.
        :type cse_app_id: str
        """
        self._cse_app_id = cse_app_id

    @property
    def version(self):
        """Gets the version of this MicroServiceInfoCSE.

        微服务的版本，已废弃，通过后端服务器组中的版本承载。

        :return: The version of this MicroServiceInfoCSE.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this MicroServiceInfoCSE.

        微服务的版本，已废弃，通过后端服务器组中的版本承载。

        :param version: The version of this MicroServiceInfoCSE.
        :type version: str
        """
        self._version = version

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
        if not isinstance(other, MicroServiceInfoCSE):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
