# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Deployment:

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
        'source': 'str',
        'group_id': 'str',
        'node_ids': 'list[str]',
        'tags': 'list[Attributes]',
        'deployment': 'CreateAppsInDeploymentV3'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'source': 'source',
        'group_id': 'group_id',
        'node_ids': 'node_ids',
        'tags': 'tags',
        'deployment': 'deployment'
    }

    def __init__(self, name=None, description=None, source=None, group_id=None, node_ids=None, tags=None, deployment=None):
        r"""Deployment

        The model defined in huaweicloud sdk

        :param name: 部署名称，只允许英文小写字母、数字、中划线，最大长度32，英文小写字母或数字开头和结尾
        :type name: str
        :param description: 部署描述
        :type description: str
        :param source: 应用部署来源：边缘市场（iem）或自定义()
        :type source: str
        :param group_id: 应用部署到指定节点组，与node_ids二选一
        :type group_id: str
        :param node_ids: 应用部署到指定节点，当前只支持一个边缘节点
        :type node_ids: list[str]
        :param tags: 节点属性
        :type tags: list[:class:`huaweicloudsdkief.v1.Attributes`]
        :param deployment: 
        :type deployment: :class:`huaweicloudsdkief.v1.CreateAppsInDeploymentV3`
        """
        
        

        self._name = None
        self._description = None
        self._source = None
        self._group_id = None
        self._node_ids = None
        self._tags = None
        self._deployment = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        if source is not None:
            self.source = source
        if group_id is not None:
            self.group_id = group_id
        self.node_ids = node_ids
        if tags is not None:
            self.tags = tags
        self.deployment = deployment

    @property
    def name(self):
        r"""Gets the name of this Deployment.

        部署名称，只允许英文小写字母、数字、中划线，最大长度32，英文小写字母或数字开头和结尾

        :return: The name of this Deployment.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this Deployment.

        部署名称，只允许英文小写字母、数字、中划线，最大长度32，英文小写字母或数字开头和结尾

        :param name: The name of this Deployment.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this Deployment.

        部署描述

        :return: The description of this Deployment.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this Deployment.

        部署描述

        :param description: The description of this Deployment.
        :type description: str
        """
        self._description = description

    @property
    def source(self):
        r"""Gets the source of this Deployment.

        应用部署来源：边缘市场（iem）或自定义()

        :return: The source of this Deployment.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        r"""Sets the source of this Deployment.

        应用部署来源：边缘市场（iem）或自定义()

        :param source: The source of this Deployment.
        :type source: str
        """
        self._source = source

    @property
    def group_id(self):
        r"""Gets the group_id of this Deployment.

        应用部署到指定节点组，与node_ids二选一

        :return: The group_id of this Deployment.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this Deployment.

        应用部署到指定节点组，与node_ids二选一

        :param group_id: The group_id of this Deployment.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def node_ids(self):
        r"""Gets the node_ids of this Deployment.

        应用部署到指定节点，当前只支持一个边缘节点

        :return: The node_ids of this Deployment.
        :rtype: list[str]
        """
        return self._node_ids

    @node_ids.setter
    def node_ids(self, node_ids):
        r"""Sets the node_ids of this Deployment.

        应用部署到指定节点，当前只支持一个边缘节点

        :param node_ids: The node_ids of this Deployment.
        :type node_ids: list[str]
        """
        self._node_ids = node_ids

    @property
    def tags(self):
        r"""Gets the tags of this Deployment.

        节点属性

        :return: The tags of this Deployment.
        :rtype: list[:class:`huaweicloudsdkief.v1.Attributes`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this Deployment.

        节点属性

        :param tags: The tags of this Deployment.
        :type tags: list[:class:`huaweicloudsdkief.v1.Attributes`]
        """
        self._tags = tags

    @property
    def deployment(self):
        r"""Gets the deployment of this Deployment.

        :return: The deployment of this Deployment.
        :rtype: :class:`huaweicloudsdkief.v1.CreateAppsInDeploymentV3`
        """
        return self._deployment

    @deployment.setter
    def deployment(self, deployment):
        r"""Sets the deployment of this Deployment.

        :param deployment: The deployment of this Deployment.
        :type deployment: :class:`huaweicloudsdkief.v1.CreateAppsInDeploymentV3`
        """
        self._deployment = deployment

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
        if not isinstance(other, Deployment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
