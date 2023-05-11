# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTemplateGroupCollectionResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'template_group_collection_list': 'list[TemplateGroupCollection]',
        'total': 'int'
    }

    attribute_map = {
        'template_group_collection_list': 'template_group_collection_list',
        'total': 'total'
    }

    def __init__(self, template_group_collection_list=None, total=None):
        """ListTemplateGroupCollectionResponse

        The model defined in huaweicloud sdk

        :param template_group_collection_list: 模板组集合信息&lt;br/&gt; 
        :type template_group_collection_list: list[:class:`huaweicloudsdkvod.v1.TemplateGroupCollection`]
        :param total: 总记录条数&lt;br/&gt; 
        :type total: int
        """
        
        super(ListTemplateGroupCollectionResponse, self).__init__()

        self._template_group_collection_list = None
        self._total = None
        self.discriminator = None

        if template_group_collection_list is not None:
            self.template_group_collection_list = template_group_collection_list
        if total is not None:
            self.total = total

    @property
    def template_group_collection_list(self):
        """Gets the template_group_collection_list of this ListTemplateGroupCollectionResponse.

        模板组集合信息<br/> 

        :return: The template_group_collection_list of this ListTemplateGroupCollectionResponse.
        :rtype: list[:class:`huaweicloudsdkvod.v1.TemplateGroupCollection`]
        """
        return self._template_group_collection_list

    @template_group_collection_list.setter
    def template_group_collection_list(self, template_group_collection_list):
        """Sets the template_group_collection_list of this ListTemplateGroupCollectionResponse.

        模板组集合信息<br/> 

        :param template_group_collection_list: The template_group_collection_list of this ListTemplateGroupCollectionResponse.
        :type template_group_collection_list: list[:class:`huaweicloudsdkvod.v1.TemplateGroupCollection`]
        """
        self._template_group_collection_list = template_group_collection_list

    @property
    def total(self):
        """Gets the total of this ListTemplateGroupCollectionResponse.

        总记录条数<br/> 

        :return: The total of this ListTemplateGroupCollectionResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListTemplateGroupCollectionResponse.

        总记录条数<br/> 

        :param total: The total of this ListTemplateGroupCollectionResponse.
        :type total: int
        """
        self._total = total

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
        if not isinstance(other, ListTemplateGroupCollectionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
