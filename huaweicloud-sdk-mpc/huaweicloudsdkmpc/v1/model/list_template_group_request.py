# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTemplateGroupRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_id': 'list[str]',
        'group_name': 'list[str]',
        'page': 'int',
        'size': 'int'
    }

    attribute_map = {
        'group_id': 'group_id',
        'group_name': 'group_name',
        'page': 'page',
        'size': 'size'
    }

    def __init__(self, group_id=None, group_name=None, page=None, size=None):
        """ListTemplateGroupRequest

        The model defined in huaweicloud sdk

        :param group_id: 转码模板组ID，最多10个 
        :type group_id: list[str]
        :param group_name: 转码模板组名，最多10个 
        :type group_name: list[str]
        :param page: 分页编号。查询指定“group_id”时，该参数无效。  默认值：0。 
        :type page: int
        :param size: 每页记录数。取值范围：[1,100]，指定group_id时该参数无效。 
        :type size: int
        """
        
        

        self._group_id = None
        self._group_name = None
        self._page = None
        self._size = None
        self.discriminator = None

        if group_id is not None:
            self.group_id = group_id
        if group_name is not None:
            self.group_name = group_name
        if page is not None:
            self.page = page
        if size is not None:
            self.size = size

    @property
    def group_id(self):
        """Gets the group_id of this ListTemplateGroupRequest.

        转码模板组ID，最多10个 

        :return: The group_id of this ListTemplateGroupRequest.
        :rtype: list[str]
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this ListTemplateGroupRequest.

        转码模板组ID，最多10个 

        :param group_id: The group_id of this ListTemplateGroupRequest.
        :type group_id: list[str]
        """
        self._group_id = group_id

    @property
    def group_name(self):
        """Gets the group_name of this ListTemplateGroupRequest.

        转码模板组名，最多10个 

        :return: The group_name of this ListTemplateGroupRequest.
        :rtype: list[str]
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this ListTemplateGroupRequest.

        转码模板组名，最多10个 

        :param group_name: The group_name of this ListTemplateGroupRequest.
        :type group_name: list[str]
        """
        self._group_name = group_name

    @property
    def page(self):
        """Gets the page of this ListTemplateGroupRequest.

        分页编号。查询指定“group_id”时，该参数无效。  默认值：0。 

        :return: The page of this ListTemplateGroupRequest.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this ListTemplateGroupRequest.

        分页编号。查询指定“group_id”时，该参数无效。  默认值：0。 

        :param page: The page of this ListTemplateGroupRequest.
        :type page: int
        """
        self._page = page

    @property
    def size(self):
        """Gets the size of this ListTemplateGroupRequest.

        每页记录数。取值范围：[1,100]，指定group_id时该参数无效。 

        :return: The size of this ListTemplateGroupRequest.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ListTemplateGroupRequest.

        每页记录数。取值范围：[1,100]，指定group_id时该参数无效。 

        :param size: The size of this ListTemplateGroupRequest.
        :type size: int
        """
        self._size = size

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
        if not isinstance(other, ListTemplateGroupRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
