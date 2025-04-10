# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeployV2OperationsDO:

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
        'name': 'str',
        'description': 'str',
        'code': 'str',
        'params': 'str',
        'entrance': 'str',
        'version': 'str',
        'module_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'code': 'code',
        'params': 'params',
        'entrance': 'entrance',
        'version': 'version',
        'module_id': 'module_id'
    }

    def __init__(self, id=None, name=None, description=None, code=None, params=None, entrance=None, version=None, module_id=None):
        r"""DeployV2OperationsDO

        The model defined in huaweicloud sdk

        :param id: 步骤id
        :type id: str
        :param name: 步骤名称
        :type name: str
        :param description: 步骤描述
        :type description: str
        :param code: 下载地址
        :type code: str
        :param params: 步骤详细定义
        :type params: str
        :param entrance: 入口函数
        :type entrance: str
        :param version: 版本
        :type version: str
        :param module_id: 模块id
        :type module_id: str
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._code = None
        self._params = None
        self._entrance = None
        self._version = None
        self._module_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if code is not None:
            self.code = code
        if params is not None:
            self.params = params
        if entrance is not None:
            self.entrance = entrance
        if version is not None:
            self.version = version
        if module_id is not None:
            self.module_id = module_id

    @property
    def id(self):
        r"""Gets the id of this DeployV2OperationsDO.

        步骤id

        :return: The id of this DeployV2OperationsDO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this DeployV2OperationsDO.

        步骤id

        :param id: The id of this DeployV2OperationsDO.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this DeployV2OperationsDO.

        步骤名称

        :return: The name of this DeployV2OperationsDO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this DeployV2OperationsDO.

        步骤名称

        :param name: The name of this DeployV2OperationsDO.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this DeployV2OperationsDO.

        步骤描述

        :return: The description of this DeployV2OperationsDO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this DeployV2OperationsDO.

        步骤描述

        :param description: The description of this DeployV2OperationsDO.
        :type description: str
        """
        self._description = description

    @property
    def code(self):
        r"""Gets the code of this DeployV2OperationsDO.

        下载地址

        :return: The code of this DeployV2OperationsDO.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this DeployV2OperationsDO.

        下载地址

        :param code: The code of this DeployV2OperationsDO.
        :type code: str
        """
        self._code = code

    @property
    def params(self):
        r"""Gets the params of this DeployV2OperationsDO.

        步骤详细定义

        :return: The params of this DeployV2OperationsDO.
        :rtype: str
        """
        return self._params

    @params.setter
    def params(self, params):
        r"""Sets the params of this DeployV2OperationsDO.

        步骤详细定义

        :param params: The params of this DeployV2OperationsDO.
        :type params: str
        """
        self._params = params

    @property
    def entrance(self):
        r"""Gets the entrance of this DeployV2OperationsDO.

        入口函数

        :return: The entrance of this DeployV2OperationsDO.
        :rtype: str
        """
        return self._entrance

    @entrance.setter
    def entrance(self, entrance):
        r"""Sets the entrance of this DeployV2OperationsDO.

        入口函数

        :param entrance: The entrance of this DeployV2OperationsDO.
        :type entrance: str
        """
        self._entrance = entrance

    @property
    def version(self):
        r"""Gets the version of this DeployV2OperationsDO.

        版本

        :return: The version of this DeployV2OperationsDO.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this DeployV2OperationsDO.

        版本

        :param version: The version of this DeployV2OperationsDO.
        :type version: str
        """
        self._version = version

    @property
    def module_id(self):
        r"""Gets the module_id of this DeployV2OperationsDO.

        模块id

        :return: The module_id of this DeployV2OperationsDO.
        :rtype: str
        """
        return self._module_id

    @module_id.setter
    def module_id(self, module_id):
        r"""Sets the module_id of this DeployV2OperationsDO.

        模块id

        :param module_id: The module_id of this DeployV2OperationsDO.
        :type module_id: str
        """
        self._module_id = module_id

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
        if not isinstance(other, DeployV2OperationsDO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
