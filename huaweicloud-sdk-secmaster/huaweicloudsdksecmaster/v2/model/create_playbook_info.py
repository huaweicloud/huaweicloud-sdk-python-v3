# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreatePlaybookInfo:

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
        'workspace_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'workspace_id': 'workspace_id'
    }

    def __init__(self, name=None, description=None, workspace_id=None):
        r"""CreatePlaybookInfo

        The model defined in huaweicloud sdk

        :param name: 剧本名称
        :type name: str
        :param description: 描述
        :type description: str
        :param workspace_id: 工作空间ID
        :type workspace_id: str
        """
        
        

        self._name = None
        self._description = None
        self._workspace_id = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        self.workspace_id = workspace_id

    @property
    def name(self):
        r"""Gets the name of this CreatePlaybookInfo.

        剧本名称

        :return: The name of this CreatePlaybookInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreatePlaybookInfo.

        剧本名称

        :param name: The name of this CreatePlaybookInfo.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this CreatePlaybookInfo.

        描述

        :return: The description of this CreatePlaybookInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreatePlaybookInfo.

        描述

        :param description: The description of this CreatePlaybookInfo.
        :type description: str
        """
        self._description = description

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this CreatePlaybookInfo.

        工作空间ID

        :return: The workspace_id of this CreatePlaybookInfo.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this CreatePlaybookInfo.

        工作空间ID

        :param workspace_id: The workspace_id of this CreatePlaybookInfo.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

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
        if not isinstance(other, CreatePlaybookInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
