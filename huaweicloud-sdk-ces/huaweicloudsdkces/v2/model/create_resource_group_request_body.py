# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateResourceGroupRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_name': 'str',
        'enterprise_project_id': 'str',
        'type': 'str',
        'tags': 'list[ResourceGroupTagRelation]',
        'association_ep_ids': 'list[str]'
    }

    attribute_map = {
        'group_name': 'group_name',
        'enterprise_project_id': 'enterprise_project_id',
        'type': 'type',
        'tags': 'tags',
        'association_ep_ids': 'association_ep_ids'
    }

    def __init__(self, group_name=None, enterprise_project_id=None, type=None, tags=None, association_ep_ids=None):
        """CreateResourceGroupRequestBody

        The model defined in huaweicloud sdk

        :param group_name: 资源分组的名称，只能为字母、数字、汉字、-、_，最大长度为128
        :type group_name: str
        :param enterprise_project_id: 资源分组归属企业项目ID
        :type enterprise_project_id: str
        :param type: 资源分组创建方式，取值只能为EPS（同步企业项目）,TAG（标签动态匹配）,不传为手动添加
        :type type: str
        :param tags: 标签动态匹配时的关联标签,type为TAG时必传
        :type tags: list[:class:`huaweicloudsdkces.v2.ResourceGroupTagRelation`]
        :param association_ep_ids: 该资源分组内包含的资源来源的企业项目ID，type为EPS时必传
        :type association_ep_ids: list[str]
        """
        
        

        self._group_name = None
        self._enterprise_project_id = None
        self._type = None
        self._tags = None
        self._association_ep_ids = None
        self.discriminator = None

        self.group_name = group_name
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if type is not None:
            self.type = type
        if tags is not None:
            self.tags = tags
        if association_ep_ids is not None:
            self.association_ep_ids = association_ep_ids

    @property
    def group_name(self):
        """Gets the group_name of this CreateResourceGroupRequestBody.

        资源分组的名称，只能为字母、数字、汉字、-、_，最大长度为128

        :return: The group_name of this CreateResourceGroupRequestBody.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this CreateResourceGroupRequestBody.

        资源分组的名称，只能为字母、数字、汉字、-、_，最大长度为128

        :param group_name: The group_name of this CreateResourceGroupRequestBody.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this CreateResourceGroupRequestBody.

        资源分组归属企业项目ID

        :return: The enterprise_project_id of this CreateResourceGroupRequestBody.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this CreateResourceGroupRequestBody.

        资源分组归属企业项目ID

        :param enterprise_project_id: The enterprise_project_id of this CreateResourceGroupRequestBody.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def type(self):
        """Gets the type of this CreateResourceGroupRequestBody.

        资源分组创建方式，取值只能为EPS（同步企业项目）,TAG（标签动态匹配）,不传为手动添加

        :return: The type of this CreateResourceGroupRequestBody.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreateResourceGroupRequestBody.

        资源分组创建方式，取值只能为EPS（同步企业项目）,TAG（标签动态匹配）,不传为手动添加

        :param type: The type of this CreateResourceGroupRequestBody.
        :type type: str
        """
        self._type = type

    @property
    def tags(self):
        """Gets the tags of this CreateResourceGroupRequestBody.

        标签动态匹配时的关联标签,type为TAG时必传

        :return: The tags of this CreateResourceGroupRequestBody.
        :rtype: list[:class:`huaweicloudsdkces.v2.ResourceGroupTagRelation`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CreateResourceGroupRequestBody.

        标签动态匹配时的关联标签,type为TAG时必传

        :param tags: The tags of this CreateResourceGroupRequestBody.
        :type tags: list[:class:`huaweicloudsdkces.v2.ResourceGroupTagRelation`]
        """
        self._tags = tags

    @property
    def association_ep_ids(self):
        """Gets the association_ep_ids of this CreateResourceGroupRequestBody.

        该资源分组内包含的资源来源的企业项目ID，type为EPS时必传

        :return: The association_ep_ids of this CreateResourceGroupRequestBody.
        :rtype: list[str]
        """
        return self._association_ep_ids

    @association_ep_ids.setter
    def association_ep_ids(self, association_ep_ids):
        """Sets the association_ep_ids of this CreateResourceGroupRequestBody.

        该资源分组内包含的资源来源的企业项目ID，type为EPS时必传

        :param association_ep_ids: The association_ep_ids of this CreateResourceGroupRequestBody.
        :type association_ep_ids: list[str]
        """
        self._association_ep_ids = association_ep_ids

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
        if not isinstance(other, CreateResourceGroupRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
