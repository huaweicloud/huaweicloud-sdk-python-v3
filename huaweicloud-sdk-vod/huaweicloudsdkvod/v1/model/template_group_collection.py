# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TemplateGroupCollection:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'group_collection_id': 'str',
        'name': 'str',
        'description': 'str',
        'template_group_list': 'list[TemplateGroup]'
    }

    attribute_map = {
        'group_collection_id': 'group_collection_id',
        'name': 'name',
        'description': 'description',
        'template_group_list': 'template_group_list'
    }

    def __init__(self, group_collection_id=None, name=None, description=None, template_group_list=None):
        """TemplateGroupCollection

        The model defined in huaweicloud sdk

        :param group_collection_id: 模板组集合id&lt;br/&gt; 
        :type group_collection_id: str
        :param name: 模板组集合名称&lt;br/&gt; 
        :type name: str
        :param description: 模板介绍&lt;br/&gt; 
        :type description: str
        :param template_group_list: 转码组列表&lt;br/&gt; 
        :type template_group_list: list[:class:`huaweicloudsdkvod.v1.TemplateGroup`]
        """
        
        

        self._group_collection_id = None
        self._name = None
        self._description = None
        self._template_group_list = None
        self.discriminator = None

        if group_collection_id is not None:
            self.group_collection_id = group_collection_id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if template_group_list is not None:
            self.template_group_list = template_group_list

    @property
    def group_collection_id(self):
        """Gets the group_collection_id of this TemplateGroupCollection.

        模板组集合id<br/> 

        :return: The group_collection_id of this TemplateGroupCollection.
        :rtype: str
        """
        return self._group_collection_id

    @group_collection_id.setter
    def group_collection_id(self, group_collection_id):
        """Sets the group_collection_id of this TemplateGroupCollection.

        模板组集合id<br/> 

        :param group_collection_id: The group_collection_id of this TemplateGroupCollection.
        :type group_collection_id: str
        """
        self._group_collection_id = group_collection_id

    @property
    def name(self):
        """Gets the name of this TemplateGroupCollection.

        模板组集合名称<br/> 

        :return: The name of this TemplateGroupCollection.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TemplateGroupCollection.

        模板组集合名称<br/> 

        :param name: The name of this TemplateGroupCollection.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this TemplateGroupCollection.

        模板介绍<br/> 

        :return: The description of this TemplateGroupCollection.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TemplateGroupCollection.

        模板介绍<br/> 

        :param description: The description of this TemplateGroupCollection.
        :type description: str
        """
        self._description = description

    @property
    def template_group_list(self):
        """Gets the template_group_list of this TemplateGroupCollection.

        转码组列表<br/> 

        :return: The template_group_list of this TemplateGroupCollection.
        :rtype: list[:class:`huaweicloudsdkvod.v1.TemplateGroup`]
        """
        return self._template_group_list

    @template_group_list.setter
    def template_group_list(self, template_group_list):
        """Sets the template_group_list of this TemplateGroupCollection.

        转码组列表<br/> 

        :param template_group_list: The template_group_list of this TemplateGroupCollection.
        :type template_group_list: list[:class:`huaweicloudsdkvod.v1.TemplateGroup`]
        """
        self._template_group_list = template_group_list

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
        if not isinstance(other, TemplateGroupCollection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
