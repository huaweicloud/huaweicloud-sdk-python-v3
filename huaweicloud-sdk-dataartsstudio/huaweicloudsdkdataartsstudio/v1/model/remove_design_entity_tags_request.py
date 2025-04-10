# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RemoveDesignEntityTagsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workspace': 'str',
        'x_project_id': 'str',
        'entity_id': 'str',
        'attr_id': 'str',
        'tag': 'str'
    }

    attribute_map = {
        'workspace': 'workspace',
        'x_project_id': 'X-Project-Id',
        'entity_id': 'entity_id',
        'attr_id': 'attr_id',
        'tag': 'tag'
    }

    def __init__(self, workspace=None, x_project_id=None, entity_id=None, attr_id=None, tag=None):
        r"""RemoveDesignEntityTagsRequest

        The model defined in huaweicloud sdk

        :param workspace: 工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。
        :type workspace: str
        :param x_project_id: 项目ID，获取方法请参见[项目ID和账号ID](projectid_accountid.xml)。  多project场景采用AK/SK认证的接口请求，则该字段必选。
        :type x_project_id: str
        :param entity_id: 表的ID，ID字符串。
        :type entity_id: str
        :param attr_id: 属性的ID，ID字符串。
        :type attr_id: str
        :param tag: 标签名。
        :type tag: str
        """
        
        

        self._workspace = None
        self._x_project_id = None
        self._entity_id = None
        self._attr_id = None
        self._tag = None
        self.discriminator = None

        self.workspace = workspace
        if x_project_id is not None:
            self.x_project_id = x_project_id
        self.entity_id = entity_id
        if attr_id is not None:
            self.attr_id = attr_id
        self.tag = tag

    @property
    def workspace(self):
        r"""Gets the workspace of this RemoveDesignEntityTagsRequest.

        工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。

        :return: The workspace of this RemoveDesignEntityTagsRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        r"""Sets the workspace of this RemoveDesignEntityTagsRequest.

        工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。

        :param workspace: The workspace of this RemoveDesignEntityTagsRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def x_project_id(self):
        r"""Gets the x_project_id of this RemoveDesignEntityTagsRequest.

        项目ID，获取方法请参见[项目ID和账号ID](projectid_accountid.xml)。  多project场景采用AK/SK认证的接口请求，则该字段必选。

        :return: The x_project_id of this RemoveDesignEntityTagsRequest.
        :rtype: str
        """
        return self._x_project_id

    @x_project_id.setter
    def x_project_id(self, x_project_id):
        r"""Sets the x_project_id of this RemoveDesignEntityTagsRequest.

        项目ID，获取方法请参见[项目ID和账号ID](projectid_accountid.xml)。  多project场景采用AK/SK认证的接口请求，则该字段必选。

        :param x_project_id: The x_project_id of this RemoveDesignEntityTagsRequest.
        :type x_project_id: str
        """
        self._x_project_id = x_project_id

    @property
    def entity_id(self):
        r"""Gets the entity_id of this RemoveDesignEntityTagsRequest.

        表的ID，ID字符串。

        :return: The entity_id of this RemoveDesignEntityTagsRequest.
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        r"""Sets the entity_id of this RemoveDesignEntityTagsRequest.

        表的ID，ID字符串。

        :param entity_id: The entity_id of this RemoveDesignEntityTagsRequest.
        :type entity_id: str
        """
        self._entity_id = entity_id

    @property
    def attr_id(self):
        r"""Gets the attr_id of this RemoveDesignEntityTagsRequest.

        属性的ID，ID字符串。

        :return: The attr_id of this RemoveDesignEntityTagsRequest.
        :rtype: str
        """
        return self._attr_id

    @attr_id.setter
    def attr_id(self, attr_id):
        r"""Sets the attr_id of this RemoveDesignEntityTagsRequest.

        属性的ID，ID字符串。

        :param attr_id: The attr_id of this RemoveDesignEntityTagsRequest.
        :type attr_id: str
        """
        self._attr_id = attr_id

    @property
    def tag(self):
        r"""Gets the tag of this RemoveDesignEntityTagsRequest.

        标签名。

        :return: The tag of this RemoveDesignEntityTagsRequest.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        r"""Sets the tag of this RemoveDesignEntityTagsRequest.

        标签名。

        :param tag: The tag of this RemoveDesignEntityTagsRequest.
        :type tag: str
        """
        self._tag = tag

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
        if not isinstance(other, RemoveDesignEntityTagsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
