# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddDesignEntityTagsRequest:

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
        'tags': 'list[str]'
    }

    attribute_map = {
        'workspace': 'workspace',
        'x_project_id': 'X-Project-Id',
        'entity_id': 'entity_id',
        'attr_id': 'attr_id',
        'tags': 'tags'
    }

    def __init__(self, workspace=None, x_project_id=None, entity_id=None, attr_id=None, tags=None):
        """AddDesignEntityTagsRequest

        The model defined in huaweicloud sdk

        :param workspace: 工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。
        :type workspace: str
        :param x_project_id: 项目ID，获取方法请参见[项目ID和账号ID](projectid_accountid.xml)。  多project场景采用AK/SK认证的接口请求，则该字段必选。
        :type x_project_id: str
        :param entity_id: 表的ID，填写String类型替代Long类型。
        :type entity_id: str
        :param attr_id: 属性的ID，填写String类型替代Long类型。
        :type attr_id: str
        :param tags: 标签名。
        :type tags: list[str]
        """
        
        

        self._workspace = None
        self._x_project_id = None
        self._entity_id = None
        self._attr_id = None
        self._tags = None
        self.discriminator = None

        self.workspace = workspace
        if x_project_id is not None:
            self.x_project_id = x_project_id
        self.entity_id = entity_id
        if attr_id is not None:
            self.attr_id = attr_id
        self.tags = tags

    @property
    def workspace(self):
        """Gets the workspace of this AddDesignEntityTagsRequest.

        工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。

        :return: The workspace of this AddDesignEntityTagsRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        """Sets the workspace of this AddDesignEntityTagsRequest.

        工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。

        :param workspace: The workspace of this AddDesignEntityTagsRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def x_project_id(self):
        """Gets the x_project_id of this AddDesignEntityTagsRequest.

        项目ID，获取方法请参见[项目ID和账号ID](projectid_accountid.xml)。  多project场景采用AK/SK认证的接口请求，则该字段必选。

        :return: The x_project_id of this AddDesignEntityTagsRequest.
        :rtype: str
        """
        return self._x_project_id

    @x_project_id.setter
    def x_project_id(self, x_project_id):
        """Sets the x_project_id of this AddDesignEntityTagsRequest.

        项目ID，获取方法请参见[项目ID和账号ID](projectid_accountid.xml)。  多project场景采用AK/SK认证的接口请求，则该字段必选。

        :param x_project_id: The x_project_id of this AddDesignEntityTagsRequest.
        :type x_project_id: str
        """
        self._x_project_id = x_project_id

    @property
    def entity_id(self):
        """Gets the entity_id of this AddDesignEntityTagsRequest.

        表的ID，填写String类型替代Long类型。

        :return: The entity_id of this AddDesignEntityTagsRequest.
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """Sets the entity_id of this AddDesignEntityTagsRequest.

        表的ID，填写String类型替代Long类型。

        :param entity_id: The entity_id of this AddDesignEntityTagsRequest.
        :type entity_id: str
        """
        self._entity_id = entity_id

    @property
    def attr_id(self):
        """Gets the attr_id of this AddDesignEntityTagsRequest.

        属性的ID，填写String类型替代Long类型。

        :return: The attr_id of this AddDesignEntityTagsRequest.
        :rtype: str
        """
        return self._attr_id

    @attr_id.setter
    def attr_id(self, attr_id):
        """Sets the attr_id of this AddDesignEntityTagsRequest.

        属性的ID，填写String类型替代Long类型。

        :param attr_id: The attr_id of this AddDesignEntityTagsRequest.
        :type attr_id: str
        """
        self._attr_id = attr_id

    @property
    def tags(self):
        """Gets the tags of this AddDesignEntityTagsRequest.

        标签名。

        :return: The tags of this AddDesignEntityTagsRequest.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this AddDesignEntityTagsRequest.

        标签名。

        :param tags: The tags of this AddDesignEntityTagsRequest.
        :type tags: list[str]
        """
        self._tags = tags

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
        if not isinstance(other, AddDesignEntityTagsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
