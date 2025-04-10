# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChInstanceLtsConfigsInstance:

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
        'mode': 'str',
        'engine_name': 'str',
        'engine_version': 'str',
        'status': 'str',
        'enterprise_project_id': 'str',
        'enterprise_project_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'mode': 'mode',
        'engine_name': 'engine_name',
        'engine_version': 'engine_version',
        'status': 'status',
        'enterprise_project_id': 'enterprise_project_id',
        'enterprise_project_name': 'enterprise_project_name'
    }

    def __init__(self, id=None, name=None, mode=None, engine_name=None, engine_version=None, status=None, enterprise_project_id=None, enterprise_project_name=None):
        r"""ChInstanceLtsConfigsInstance

        The model defined in huaweicloud sdk

        :param id: ClickHouse实例ID。
        :type id: str
        :param name: 实例名。
        :type name: str
        :param mode: 实例主备状态。
        :type mode: str
        :param engine_name: 引擎类型。
        :type engine_name: str
        :param engine_version: 引擎版本。
        :type engine_version: str
        :param status: 实例状态。
        :type status: str
        :param enterprise_project_id: 企业project id。
        :type enterprise_project_id: str
        :param enterprise_project_name: 企业project名。
        :type enterprise_project_name: str
        """
        
        

        self._id = None
        self._name = None
        self._mode = None
        self._engine_name = None
        self._engine_version = None
        self._status = None
        self._enterprise_project_id = None
        self._enterprise_project_name = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if mode is not None:
            self.mode = mode
        if engine_name is not None:
            self.engine_name = engine_name
        if engine_version is not None:
            self.engine_version = engine_version
        if status is not None:
            self.status = status
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if enterprise_project_name is not None:
            self.enterprise_project_name = enterprise_project_name

    @property
    def id(self):
        r"""Gets the id of this ChInstanceLtsConfigsInstance.

        ClickHouse实例ID。

        :return: The id of this ChInstanceLtsConfigsInstance.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ChInstanceLtsConfigsInstance.

        ClickHouse实例ID。

        :param id: The id of this ChInstanceLtsConfigsInstance.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ChInstanceLtsConfigsInstance.

        实例名。

        :return: The name of this ChInstanceLtsConfigsInstance.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ChInstanceLtsConfigsInstance.

        实例名。

        :param name: The name of this ChInstanceLtsConfigsInstance.
        :type name: str
        """
        self._name = name

    @property
    def mode(self):
        r"""Gets the mode of this ChInstanceLtsConfigsInstance.

        实例主备状态。

        :return: The mode of this ChInstanceLtsConfigsInstance.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        r"""Sets the mode of this ChInstanceLtsConfigsInstance.

        实例主备状态。

        :param mode: The mode of this ChInstanceLtsConfigsInstance.
        :type mode: str
        """
        self._mode = mode

    @property
    def engine_name(self):
        r"""Gets the engine_name of this ChInstanceLtsConfigsInstance.

        引擎类型。

        :return: The engine_name of this ChInstanceLtsConfigsInstance.
        :rtype: str
        """
        return self._engine_name

    @engine_name.setter
    def engine_name(self, engine_name):
        r"""Sets the engine_name of this ChInstanceLtsConfigsInstance.

        引擎类型。

        :param engine_name: The engine_name of this ChInstanceLtsConfigsInstance.
        :type engine_name: str
        """
        self._engine_name = engine_name

    @property
    def engine_version(self):
        r"""Gets the engine_version of this ChInstanceLtsConfigsInstance.

        引擎版本。

        :return: The engine_version of this ChInstanceLtsConfigsInstance.
        :rtype: str
        """
        return self._engine_version

    @engine_version.setter
    def engine_version(self, engine_version):
        r"""Sets the engine_version of this ChInstanceLtsConfigsInstance.

        引擎版本。

        :param engine_version: The engine_version of this ChInstanceLtsConfigsInstance.
        :type engine_version: str
        """
        self._engine_version = engine_version

    @property
    def status(self):
        r"""Gets the status of this ChInstanceLtsConfigsInstance.

        实例状态。

        :return: The status of this ChInstanceLtsConfigsInstance.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ChInstanceLtsConfigsInstance.

        实例状态。

        :param status: The status of this ChInstanceLtsConfigsInstance.
        :type status: str
        """
        self._status = status

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ChInstanceLtsConfigsInstance.

        企业project id。

        :return: The enterprise_project_id of this ChInstanceLtsConfigsInstance.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ChInstanceLtsConfigsInstance.

        企业project id。

        :param enterprise_project_id: The enterprise_project_id of this ChInstanceLtsConfigsInstance.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def enterprise_project_name(self):
        r"""Gets the enterprise_project_name of this ChInstanceLtsConfigsInstance.

        企业project名。

        :return: The enterprise_project_name of this ChInstanceLtsConfigsInstance.
        :rtype: str
        """
        return self._enterprise_project_name

    @enterprise_project_name.setter
    def enterprise_project_name(self, enterprise_project_name):
        r"""Sets the enterprise_project_name of this ChInstanceLtsConfigsInstance.

        企业project名。

        :param enterprise_project_name: The enterprise_project_name of this ChInstanceLtsConfigsInstance.
        :type enterprise_project_name: str
        """
        self._enterprise_project_name = enterprise_project_name

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
        if not isinstance(other, ChInstanceLtsConfigsInstance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
