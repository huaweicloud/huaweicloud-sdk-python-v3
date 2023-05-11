# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListIncidentTypesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'workspace_id': 'str',
        'parent_business_code': 'str',
        'offset': 'int',
        'limit': 'int',
        'order': 'str',
        'sortby': 'str',
        'name': 'str',
        'enabled': 'bool',
        'layout_name': 'str',
        'is_built_in': 'bool'
    }

    attribute_map = {
        'project_id': 'project_id',
        'workspace_id': 'workspace_id',
        'parent_business_code': 'parent_business_code',
        'offset': 'offset',
        'limit': 'limit',
        'order': 'order',
        'sortby': 'sortby',
        'name': 'name',
        'enabled': 'enabled',
        'layout_name': 'layout_name',
        'is_built_in': 'is_built_in'
    }

    def __init__(self, project_id=None, workspace_id=None, parent_business_code=None, offset=None, limit=None, order=None, sortby=None, name=None, enabled=None, layout_name=None, is_built_in=None):
        """ListIncidentTypesRequest

        The model defined in huaweicloud sdk

        :param project_id: 项目ID
        :type project_id: str
        :param workspace_id: 工作空间ID
        :type workspace_id: str
        :param parent_business_code: 子类类型标识码
        :type parent_business_code: str
        :param offset: request offset, from 0
        :type offset: int
        :param limit: request limit size
        :type limit: int
        :param order: sort order, ASC, DESC.
        :type order: str
        :param sortby: sort by property, create_time.
        :type sortby: str
        :param name: name
        :type name: str
        :param enabled: 是否启用
        :type enabled: bool
        :param layout_name: 布局名称
        :type layout_name: str
        :param is_built_in: 是否内置
        :type is_built_in: bool
        """
        
        

        self._project_id = None
        self._workspace_id = None
        self._parent_business_code = None
        self._offset = None
        self._limit = None
        self._order = None
        self._sortby = None
        self._name = None
        self._enabled = None
        self._layout_name = None
        self._is_built_in = None
        self.discriminator = None

        self.project_id = project_id
        self.workspace_id = workspace_id
        if parent_business_code is not None:
            self.parent_business_code = parent_business_code
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if order is not None:
            self.order = order
        if sortby is not None:
            self.sortby = sortby
        if name is not None:
            self.name = name
        if enabled is not None:
            self.enabled = enabled
        if layout_name is not None:
            self.layout_name = layout_name
        if is_built_in is not None:
            self.is_built_in = is_built_in

    @property
    def project_id(self):
        """Gets the project_id of this ListIncidentTypesRequest.

        项目ID

        :return: The project_id of this ListIncidentTypesRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ListIncidentTypesRequest.

        项目ID

        :param project_id: The project_id of this ListIncidentTypesRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def workspace_id(self):
        """Gets the workspace_id of this ListIncidentTypesRequest.

        工作空间ID

        :return: The workspace_id of this ListIncidentTypesRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        """Sets the workspace_id of this ListIncidentTypesRequest.

        工作空间ID

        :param workspace_id: The workspace_id of this ListIncidentTypesRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def parent_business_code(self):
        """Gets the parent_business_code of this ListIncidentTypesRequest.

        子类类型标识码

        :return: The parent_business_code of this ListIncidentTypesRequest.
        :rtype: str
        """
        return self._parent_business_code

    @parent_business_code.setter
    def parent_business_code(self, parent_business_code):
        """Sets the parent_business_code of this ListIncidentTypesRequest.

        子类类型标识码

        :param parent_business_code: The parent_business_code of this ListIncidentTypesRequest.
        :type parent_business_code: str
        """
        self._parent_business_code = parent_business_code

    @property
    def offset(self):
        """Gets the offset of this ListIncidentTypesRequest.

        request offset, from 0

        :return: The offset of this ListIncidentTypesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListIncidentTypesRequest.

        request offset, from 0

        :param offset: The offset of this ListIncidentTypesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListIncidentTypesRequest.

        request limit size

        :return: The limit of this ListIncidentTypesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListIncidentTypesRequest.

        request limit size

        :param limit: The limit of this ListIncidentTypesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def order(self):
        """Gets the order of this ListIncidentTypesRequest.

        sort order, ASC, DESC.

        :return: The order of this ListIncidentTypesRequest.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this ListIncidentTypesRequest.

        sort order, ASC, DESC.

        :param order: The order of this ListIncidentTypesRequest.
        :type order: str
        """
        self._order = order

    @property
    def sortby(self):
        """Gets the sortby of this ListIncidentTypesRequest.

        sort by property, create_time.

        :return: The sortby of this ListIncidentTypesRequest.
        :rtype: str
        """
        return self._sortby

    @sortby.setter
    def sortby(self, sortby):
        """Sets the sortby of this ListIncidentTypesRequest.

        sort by property, create_time.

        :param sortby: The sortby of this ListIncidentTypesRequest.
        :type sortby: str
        """
        self._sortby = sortby

    @property
    def name(self):
        """Gets the name of this ListIncidentTypesRequest.

        name

        :return: The name of this ListIncidentTypesRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListIncidentTypesRequest.

        name

        :param name: The name of this ListIncidentTypesRequest.
        :type name: str
        """
        self._name = name

    @property
    def enabled(self):
        """Gets the enabled of this ListIncidentTypesRequest.

        是否启用

        :return: The enabled of this ListIncidentTypesRequest.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this ListIncidentTypesRequest.

        是否启用

        :param enabled: The enabled of this ListIncidentTypesRequest.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def layout_name(self):
        """Gets the layout_name of this ListIncidentTypesRequest.

        布局名称

        :return: The layout_name of this ListIncidentTypesRequest.
        :rtype: str
        """
        return self._layout_name

    @layout_name.setter
    def layout_name(self, layout_name):
        """Sets the layout_name of this ListIncidentTypesRequest.

        布局名称

        :param layout_name: The layout_name of this ListIncidentTypesRequest.
        :type layout_name: str
        """
        self._layout_name = layout_name

    @property
    def is_built_in(self):
        """Gets the is_built_in of this ListIncidentTypesRequest.

        是否内置

        :return: The is_built_in of this ListIncidentTypesRequest.
        :rtype: bool
        """
        return self._is_built_in

    @is_built_in.setter
    def is_built_in(self, is_built_in):
        """Sets the is_built_in of this ListIncidentTypesRequest.

        是否内置

        :param is_built_in: The is_built_in of this ListIncidentTypesRequest.
        :type is_built_in: bool
        """
        self._is_built_in = is_built_in

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
        if not isinstance(other, ListIncidentTypesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
