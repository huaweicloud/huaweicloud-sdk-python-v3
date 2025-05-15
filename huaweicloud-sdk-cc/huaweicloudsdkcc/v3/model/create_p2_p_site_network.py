# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateP2PSiteNetwork:

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
        'tags': 'list[Tag]',
        'enterprise_project_id': 'str',
        'sites': 'list[CreateSiteInformation]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'tags': 'tags',
        'enterprise_project_id': 'enterprise_project_id',
        'sites': 'sites'
    }

    def __init__(self, name=None, description=None, tags=None, enterprise_project_id=None, sites=None):
        r"""CreateP2PSiteNetwork

        The model defined in huaweicloud sdk

        :param name: 实例名称。
        :type name: str
        :param description: 实例描述。不支持 &lt;&gt;。
        :type description: str
        :param tags: 实例标签。
        :type tags: list[:class:`huaweicloudsdkcc.v3.Tag`]
        :param enterprise_project_id: 实例所属企业项目ID。
        :type enterprise_project_id: str
        :param sites: 端到端（P2P）类型分支网络连接的两个端点定义，长度固定为2的数组。
        :type sites: list[:class:`huaweicloudsdkcc.v3.CreateSiteInformation`]
        """
        
        

        self._name = None
        self._description = None
        self._tags = None
        self._enterprise_project_id = None
        self._sites = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        if tags is not None:
            self.tags = tags
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.sites = sites

    @property
    def name(self):
        r"""Gets the name of this CreateP2PSiteNetwork.

        实例名称。

        :return: The name of this CreateP2PSiteNetwork.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateP2PSiteNetwork.

        实例名称。

        :param name: The name of this CreateP2PSiteNetwork.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this CreateP2PSiteNetwork.

        实例描述。不支持 <>。

        :return: The description of this CreateP2PSiteNetwork.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateP2PSiteNetwork.

        实例描述。不支持 <>。

        :param description: The description of this CreateP2PSiteNetwork.
        :type description: str
        """
        self._description = description

    @property
    def tags(self):
        r"""Gets the tags of this CreateP2PSiteNetwork.

        实例标签。

        :return: The tags of this CreateP2PSiteNetwork.
        :rtype: list[:class:`huaweicloudsdkcc.v3.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this CreateP2PSiteNetwork.

        实例标签。

        :param tags: The tags of this CreateP2PSiteNetwork.
        :type tags: list[:class:`huaweicloudsdkcc.v3.Tag`]
        """
        self._tags = tags

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this CreateP2PSiteNetwork.

        实例所属企业项目ID。

        :return: The enterprise_project_id of this CreateP2PSiteNetwork.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this CreateP2PSiteNetwork.

        实例所属企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this CreateP2PSiteNetwork.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def sites(self):
        r"""Gets the sites of this CreateP2PSiteNetwork.

        端到端（P2P）类型分支网络连接的两个端点定义，长度固定为2的数组。

        :return: The sites of this CreateP2PSiteNetwork.
        :rtype: list[:class:`huaweicloudsdkcc.v3.CreateSiteInformation`]
        """
        return self._sites

    @sites.setter
    def sites(self, sites):
        r"""Sets the sites of this CreateP2PSiteNetwork.

        端到端（P2P）类型分支网络连接的两个端点定义，长度固定为2的数组。

        :param sites: The sites of this CreateP2PSiteNetwork.
        :type sites: list[:class:`huaweicloudsdkcc.v3.CreateSiteInformation`]
        """
        self._sites = sites

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
        if not isinstance(other, CreateP2PSiteNetwork):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
