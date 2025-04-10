# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ScriptSimpleInfo:

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
        'type': 'str',
        'version': 'str',
        'create_time': 'datetime',
        'update_time': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'type': 'type',
        'version': 'version',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, id=None, name=None, description=None, type=None, version=None, create_time=None, update_time=None):
        r"""ScriptSimpleInfo

        The model defined in huaweicloud sdk

        :param id: 脚本ID。
        :type id: str
        :param name: 脚本名称。
        :type name: str
        :param description: 描述。
        :type description: str
        :param type: 脚本类型：POWERSHELL/BAT/SHELL。
        :type type: str
        :param version: 脚本版本。
        :type version: str
        :param create_time: 创建时间。
        :type create_time: datetime
        :param update_time: 更新时间。
        :type update_time: datetime
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._type = None
        self._version = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if type is not None:
            self.type = type
        if version is not None:
            self.version = version
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def id(self):
        r"""Gets the id of this ScriptSimpleInfo.

        脚本ID。

        :return: The id of this ScriptSimpleInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ScriptSimpleInfo.

        脚本ID。

        :param id: The id of this ScriptSimpleInfo.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ScriptSimpleInfo.

        脚本名称。

        :return: The name of this ScriptSimpleInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ScriptSimpleInfo.

        脚本名称。

        :param name: The name of this ScriptSimpleInfo.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this ScriptSimpleInfo.

        描述。

        :return: The description of this ScriptSimpleInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ScriptSimpleInfo.

        描述。

        :param description: The description of this ScriptSimpleInfo.
        :type description: str
        """
        self._description = description

    @property
    def type(self):
        r"""Gets the type of this ScriptSimpleInfo.

        脚本类型：POWERSHELL/BAT/SHELL。

        :return: The type of this ScriptSimpleInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ScriptSimpleInfo.

        脚本类型：POWERSHELL/BAT/SHELL。

        :param type: The type of this ScriptSimpleInfo.
        :type type: str
        """
        self._type = type

    @property
    def version(self):
        r"""Gets the version of this ScriptSimpleInfo.

        脚本版本。

        :return: The version of this ScriptSimpleInfo.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this ScriptSimpleInfo.

        脚本版本。

        :param version: The version of this ScriptSimpleInfo.
        :type version: str
        """
        self._version = version

    @property
    def create_time(self):
        r"""Gets the create_time of this ScriptSimpleInfo.

        创建时间。

        :return: The create_time of this ScriptSimpleInfo.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ScriptSimpleInfo.

        创建时间。

        :param create_time: The create_time of this ScriptSimpleInfo.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this ScriptSimpleInfo.

        更新时间。

        :return: The update_time of this ScriptSimpleInfo.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ScriptSimpleInfo.

        更新时间。

        :param update_time: The update_time of this ScriptSimpleInfo.
        :type update_time: datetime
        """
        self._update_time = update_time

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
        if not isinstance(other, ScriptSimpleInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
