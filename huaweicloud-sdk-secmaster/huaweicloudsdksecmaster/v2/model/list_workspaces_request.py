# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListWorkspacesRequest:

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
        'offset': 'float',
        'limit': 'float',
        'region_id': 'str',
        'name': 'str',
        'description': 'str',
        'view_bind_id': 'str',
        'view_bind_name': 'str',
        'create_time_start': 'str',
        'create_time_end': 'str',
        'is_view': 'bool',
        'ids': 'str',
        'normal_project_id': 'str',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'project_id': 'project_id',
        'offset': 'offset',
        'limit': 'limit',
        'region_id': 'region_id',
        'name': 'name',
        'description': 'description',
        'view_bind_id': 'view_bind_id',
        'view_bind_name': 'view_bind_name',
        'create_time_start': 'create_time_start',
        'create_time_end': 'create_time_end',
        'is_view': 'is_view',
        'ids': 'ids',
        'normal_project_id': 'normal_project_id',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, project_id=None, offset=None, limit=None, region_id=None, name=None, description=None, view_bind_id=None, view_bind_name=None, create_time_start=None, create_time_end=None, is_view=None, ids=None, normal_project_id=None, enterprise_project_id=None):
        r"""ListWorkspacesRequest

        The model defined in huaweicloud sdk

        :param project_id: 项目id
        :type project_id: str
        :param offset: 偏移量 指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，
        :type offset: float
        :param limit: 每页显示个数
        :type limit: float
        :param region_id: 区域id
        :type region_id: str
        :param name: 名称查询
        :type name: str
        :param description: 描述查询
        :type description: str
        :param view_bind_id: 视图绑定的空间id
        :type view_bind_id: str
        :param view_bind_name: 视图绑定的空间名称
        :type view_bind_name: str
        :param create_time_start: 创建时间开始，例如2024-04-26T16:08:09Z+0800
        :type create_time_start: str
        :param create_time_end: 创建时间结束，例如2024-04-2T16:08:09Z+0800
        :type create_time_end: str
        :param is_view: 是否查询视图 true or false
        :type is_view: bool
        :param ids: 工作空间id数组，英文逗号分隔
        :type ids: str
        :param normal_project_id: 普通项目的项目id
        :type normal_project_id: str
        :param enterprise_project_id: 企业项目的项目id
        :type enterprise_project_id: str
        """
        
        

        self._project_id = None
        self._offset = None
        self._limit = None
        self._region_id = None
        self._name = None
        self._description = None
        self._view_bind_id = None
        self._view_bind_name = None
        self._create_time_start = None
        self._create_time_end = None
        self._is_view = None
        self._ids = None
        self._normal_project_id = None
        self._enterprise_project_id = None
        self.discriminator = None

        self.project_id = project_id
        self.offset = offset
        self.limit = limit
        if region_id is not None:
            self.region_id = region_id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if view_bind_id is not None:
            self.view_bind_id = view_bind_id
        if view_bind_name is not None:
            self.view_bind_name = view_bind_name
        if create_time_start is not None:
            self.create_time_start = create_time_start
        if create_time_end is not None:
            self.create_time_end = create_time_end
        if is_view is not None:
            self.is_view = is_view
        if ids is not None:
            self.ids = ids
        if normal_project_id is not None:
            self.normal_project_id = normal_project_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def project_id(self):
        r"""Gets the project_id of this ListWorkspacesRequest.

        项目id

        :return: The project_id of this ListWorkspacesRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ListWorkspacesRequest.

        项目id

        :param project_id: The project_id of this ListWorkspacesRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def offset(self):
        r"""Gets the offset of this ListWorkspacesRequest.

        偏移量 指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，

        :return: The offset of this ListWorkspacesRequest.
        :rtype: float
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListWorkspacesRequest.

        偏移量 指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，

        :param offset: The offset of this ListWorkspacesRequest.
        :type offset: float
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListWorkspacesRequest.

        每页显示个数

        :return: The limit of this ListWorkspacesRequest.
        :rtype: float
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListWorkspacesRequest.

        每页显示个数

        :param limit: The limit of this ListWorkspacesRequest.
        :type limit: float
        """
        self._limit = limit

    @property
    def region_id(self):
        r"""Gets the region_id of this ListWorkspacesRequest.

        区域id

        :return: The region_id of this ListWorkspacesRequest.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this ListWorkspacesRequest.

        区域id

        :param region_id: The region_id of this ListWorkspacesRequest.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def name(self):
        r"""Gets the name of this ListWorkspacesRequest.

        名称查询

        :return: The name of this ListWorkspacesRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListWorkspacesRequest.

        名称查询

        :param name: The name of this ListWorkspacesRequest.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this ListWorkspacesRequest.

        描述查询

        :return: The description of this ListWorkspacesRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ListWorkspacesRequest.

        描述查询

        :param description: The description of this ListWorkspacesRequest.
        :type description: str
        """
        self._description = description

    @property
    def view_bind_id(self):
        r"""Gets the view_bind_id of this ListWorkspacesRequest.

        视图绑定的空间id

        :return: The view_bind_id of this ListWorkspacesRequest.
        :rtype: str
        """
        return self._view_bind_id

    @view_bind_id.setter
    def view_bind_id(self, view_bind_id):
        r"""Sets the view_bind_id of this ListWorkspacesRequest.

        视图绑定的空间id

        :param view_bind_id: The view_bind_id of this ListWorkspacesRequest.
        :type view_bind_id: str
        """
        self._view_bind_id = view_bind_id

    @property
    def view_bind_name(self):
        r"""Gets the view_bind_name of this ListWorkspacesRequest.

        视图绑定的空间名称

        :return: The view_bind_name of this ListWorkspacesRequest.
        :rtype: str
        """
        return self._view_bind_name

    @view_bind_name.setter
    def view_bind_name(self, view_bind_name):
        r"""Sets the view_bind_name of this ListWorkspacesRequest.

        视图绑定的空间名称

        :param view_bind_name: The view_bind_name of this ListWorkspacesRequest.
        :type view_bind_name: str
        """
        self._view_bind_name = view_bind_name

    @property
    def create_time_start(self):
        r"""Gets the create_time_start of this ListWorkspacesRequest.

        创建时间开始，例如2024-04-26T16:08:09Z+0800

        :return: The create_time_start of this ListWorkspacesRequest.
        :rtype: str
        """
        return self._create_time_start

    @create_time_start.setter
    def create_time_start(self, create_time_start):
        r"""Sets the create_time_start of this ListWorkspacesRequest.

        创建时间开始，例如2024-04-26T16:08:09Z+0800

        :param create_time_start: The create_time_start of this ListWorkspacesRequest.
        :type create_time_start: str
        """
        self._create_time_start = create_time_start

    @property
    def create_time_end(self):
        r"""Gets the create_time_end of this ListWorkspacesRequest.

        创建时间结束，例如2024-04-2T16:08:09Z+0800

        :return: The create_time_end of this ListWorkspacesRequest.
        :rtype: str
        """
        return self._create_time_end

    @create_time_end.setter
    def create_time_end(self, create_time_end):
        r"""Sets the create_time_end of this ListWorkspacesRequest.

        创建时间结束，例如2024-04-2T16:08:09Z+0800

        :param create_time_end: The create_time_end of this ListWorkspacesRequest.
        :type create_time_end: str
        """
        self._create_time_end = create_time_end

    @property
    def is_view(self):
        r"""Gets the is_view of this ListWorkspacesRequest.

        是否查询视图 true or false

        :return: The is_view of this ListWorkspacesRequest.
        :rtype: bool
        """
        return self._is_view

    @is_view.setter
    def is_view(self, is_view):
        r"""Sets the is_view of this ListWorkspacesRequest.

        是否查询视图 true or false

        :param is_view: The is_view of this ListWorkspacesRequest.
        :type is_view: bool
        """
        self._is_view = is_view

    @property
    def ids(self):
        r"""Gets the ids of this ListWorkspacesRequest.

        工作空间id数组，英文逗号分隔

        :return: The ids of this ListWorkspacesRequest.
        :rtype: str
        """
        return self._ids

    @ids.setter
    def ids(self, ids):
        r"""Sets the ids of this ListWorkspacesRequest.

        工作空间id数组，英文逗号分隔

        :param ids: The ids of this ListWorkspacesRequest.
        :type ids: str
        """
        self._ids = ids

    @property
    def normal_project_id(self):
        r"""Gets the normal_project_id of this ListWorkspacesRequest.

        普通项目的项目id

        :return: The normal_project_id of this ListWorkspacesRequest.
        :rtype: str
        """
        return self._normal_project_id

    @normal_project_id.setter
    def normal_project_id(self, normal_project_id):
        r"""Sets the normal_project_id of this ListWorkspacesRequest.

        普通项目的项目id

        :param normal_project_id: The normal_project_id of this ListWorkspacesRequest.
        :type normal_project_id: str
        """
        self._normal_project_id = normal_project_id

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListWorkspacesRequest.

        企业项目的项目id

        :return: The enterprise_project_id of this ListWorkspacesRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListWorkspacesRequest.

        企业项目的项目id

        :param enterprise_project_id: The enterprise_project_id of this ListWorkspacesRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, ListWorkspacesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
