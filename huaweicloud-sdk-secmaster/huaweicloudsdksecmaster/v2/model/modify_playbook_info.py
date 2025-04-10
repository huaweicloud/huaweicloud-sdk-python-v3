# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModifyPlaybookInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'description': 'str',
        'enabled': 'bool',
        'active_version_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'enabled': 'enabled',
        'active_version_id': 'active_version_id'
    }

    def __init__(self, name=None, description=None, enabled=None, active_version_id=None):
        r"""ModifyPlaybookInfo

        The model defined in huaweicloud sdk

        :param name: 剧本名称
        :type name: str
        :param description: 描述
        :type description: str
        :param enabled: 是否启用
        :type enabled: bool
        :param active_version_id: 启用的剧本版本ID
        :type active_version_id: str
        """
        
        

        self._name = None
        self._description = None
        self._enabled = None
        self._active_version_id = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if enabled is not None:
            self.enabled = enabled
        if active_version_id is not None:
            self.active_version_id = active_version_id

    @property
    def name(self):
        r"""Gets the name of this ModifyPlaybookInfo.

        剧本名称

        :return: The name of this ModifyPlaybookInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ModifyPlaybookInfo.

        剧本名称

        :param name: The name of this ModifyPlaybookInfo.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this ModifyPlaybookInfo.

        描述

        :return: The description of this ModifyPlaybookInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ModifyPlaybookInfo.

        描述

        :param description: The description of this ModifyPlaybookInfo.
        :type description: str
        """
        self._description = description

    @property
    def enabled(self):
        r"""Gets the enabled of this ModifyPlaybookInfo.

        是否启用

        :return: The enabled of this ModifyPlaybookInfo.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this ModifyPlaybookInfo.

        是否启用

        :param enabled: The enabled of this ModifyPlaybookInfo.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def active_version_id(self):
        r"""Gets the active_version_id of this ModifyPlaybookInfo.

        启用的剧本版本ID

        :return: The active_version_id of this ModifyPlaybookInfo.
        :rtype: str
        """
        return self._active_version_id

    @active_version_id.setter
    def active_version_id(self, active_version_id):
        r"""Sets the active_version_id of this ModifyPlaybookInfo.

        启用的剧本版本ID

        :param active_version_id: The active_version_id of this ModifyPlaybookInfo.
        :type active_version_id: str
        """
        self._active_version_id = active_version_id

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
        if not isinstance(other, ModifyPlaybookInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
