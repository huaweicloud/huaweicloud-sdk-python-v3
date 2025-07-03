# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LaunchTemplate:

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
        'created_at': 'str',
        'updated_at': 'str',
        'default_version': 'int',
        'latest_version': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'default_version': 'default_version',
        'latest_version': 'latest_version'
    }

    def __init__(self, id=None, name=None, description=None, created_at=None, updated_at=None, default_version=None, latest_version=None):
        r"""LaunchTemplate

        The model defined in huaweicloud sdk

        :param id: 模板id
        :type id: str
        :param name: 模板名称
        :type name: str
        :param description: 模板描述
        :type description: str
        :param created_at: 创建时间
        :type created_at: str
        :param updated_at: 更新时间
        :type updated_at: str
        :param default_version: 模板默认版本号
        :type default_version: int
        :param latest_version: 模板最新版本号
        :type latest_version: int
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._created_at = None
        self._updated_at = None
        self._default_version = None
        self._latest_version = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.description = description
        self.created_at = created_at
        self.updated_at = updated_at
        self.default_version = default_version
        self.latest_version = latest_version

    @property
    def id(self):
        r"""Gets the id of this LaunchTemplate.

        模板id

        :return: The id of this LaunchTemplate.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this LaunchTemplate.

        模板id

        :param id: The id of this LaunchTemplate.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this LaunchTemplate.

        模板名称

        :return: The name of this LaunchTemplate.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this LaunchTemplate.

        模板名称

        :param name: The name of this LaunchTemplate.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this LaunchTemplate.

        模板描述

        :return: The description of this LaunchTemplate.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this LaunchTemplate.

        模板描述

        :param description: The description of this LaunchTemplate.
        :type description: str
        """
        self._description = description

    @property
    def created_at(self):
        r"""Gets the created_at of this LaunchTemplate.

        创建时间

        :return: The created_at of this LaunchTemplate.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this LaunchTemplate.

        创建时间

        :param created_at: The created_at of this LaunchTemplate.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this LaunchTemplate.

        更新时间

        :return: The updated_at of this LaunchTemplate.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this LaunchTemplate.

        更新时间

        :param updated_at: The updated_at of this LaunchTemplate.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def default_version(self):
        r"""Gets the default_version of this LaunchTemplate.

        模板默认版本号

        :return: The default_version of this LaunchTemplate.
        :rtype: int
        """
        return self._default_version

    @default_version.setter
    def default_version(self, default_version):
        r"""Sets the default_version of this LaunchTemplate.

        模板默认版本号

        :param default_version: The default_version of this LaunchTemplate.
        :type default_version: int
        """
        self._default_version = default_version

    @property
    def latest_version(self):
        r"""Gets the latest_version of this LaunchTemplate.

        模板最新版本号

        :return: The latest_version of this LaunchTemplate.
        :rtype: int
        """
        return self._latest_version

    @latest_version.setter
    def latest_version(self, latest_version):
        r"""Sets the latest_version of this LaunchTemplate.

        模板最新版本号

        :param latest_version: The latest_version of this LaunchTemplate.
        :type latest_version: int
        """
        self._latest_version = latest_version

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
        if not isinstance(other, LaunchTemplate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
