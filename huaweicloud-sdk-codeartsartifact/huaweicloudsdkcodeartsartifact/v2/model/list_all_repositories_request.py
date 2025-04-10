# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAllRepositoriesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tenant_id': 'str',
        'project_id': 'str',
        'group_id': 'str',
        'page_no': 'int',
        'page_size': 'int',
        'sort': 'str',
        'qname': 'str',
        'type': 'str',
        'format': 'str',
        'format_list': 'str',
        'is_recycle_bin': 'bool',
        'is_need_paging': 'bool',
        'in_project': 'bool'
    }

    attribute_map = {
        'tenant_id': 'tenant_id',
        'project_id': 'project_id',
        'group_id': 'group_id',
        'page_no': 'page_no',
        'page_size': 'page_size',
        'sort': 'sort',
        'qname': 'qname',
        'type': 'type',
        'format': 'format',
        'format_list': 'format_list',
        'is_recycle_bin': 'is_recycle_bin',
        'is_need_paging': 'is_need_paging',
        'in_project': 'in_project'
    }

    def __init__(self, tenant_id=None, project_id=None, group_id=None, page_no=None, page_size=None, sort=None, qname=None, type=None, format=None, format_list=None, is_recycle_bin=None, is_need_paging=None, in_project=None):
        r"""ListAllRepositoriesRequest

        The model defined in huaweicloud sdk

        :param tenant_id: 租户id
        :type tenant_id: str
        :param project_id: 项目id
        :type project_id: str
        :param group_id: 组id
        :type group_id: str
        :param page_no: 页码
        :type page_no: int
        :param page_size: 每页大小
        :type page_size: int
        :param sort: 排序类型
        :type sort: str
        :param qname: 查询内容
        :type qname: str
        :param type: 仓库类型
        :type type: str
        :param format: 仓库格式
        :type format: str
        :param format_list: 仓库格式列表
        :type format_list: str
        :param is_recycle_bin: 是否是回收站文件
        :type is_recycle_bin: bool
        :param is_need_paging: 是否需要分页
        :type is_need_paging: bool
        :param in_project: 是否在项目中
        :type in_project: bool
        """
        
        

        self._tenant_id = None
        self._project_id = None
        self._group_id = None
        self._page_no = None
        self._page_size = None
        self._sort = None
        self._qname = None
        self._type = None
        self._format = None
        self._format_list = None
        self._is_recycle_bin = None
        self._is_need_paging = None
        self._in_project = None
        self.discriminator = None

        self.tenant_id = tenant_id
        self.project_id = project_id
        if group_id is not None:
            self.group_id = group_id
        if page_no is not None:
            self.page_no = page_no
        if page_size is not None:
            self.page_size = page_size
        if sort is not None:
            self.sort = sort
        if qname is not None:
            self.qname = qname
        if type is not None:
            self.type = type
        if format is not None:
            self.format = format
        if format_list is not None:
            self.format_list = format_list
        if is_recycle_bin is not None:
            self.is_recycle_bin = is_recycle_bin
        if is_need_paging is not None:
            self.is_need_paging = is_need_paging
        if in_project is not None:
            self.in_project = in_project

    @property
    def tenant_id(self):
        r"""Gets the tenant_id of this ListAllRepositoriesRequest.

        租户id

        :return: The tenant_id of this ListAllRepositoriesRequest.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        r"""Sets the tenant_id of this ListAllRepositoriesRequest.

        租户id

        :param tenant_id: The tenant_id of this ListAllRepositoriesRequest.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def project_id(self):
        r"""Gets the project_id of this ListAllRepositoriesRequest.

        项目id

        :return: The project_id of this ListAllRepositoriesRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ListAllRepositoriesRequest.

        项目id

        :param project_id: The project_id of this ListAllRepositoriesRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def group_id(self):
        r"""Gets the group_id of this ListAllRepositoriesRequest.

        组id

        :return: The group_id of this ListAllRepositoriesRequest.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this ListAllRepositoriesRequest.

        组id

        :param group_id: The group_id of this ListAllRepositoriesRequest.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def page_no(self):
        r"""Gets the page_no of this ListAllRepositoriesRequest.

        页码

        :return: The page_no of this ListAllRepositoriesRequest.
        :rtype: int
        """
        return self._page_no

    @page_no.setter
    def page_no(self, page_no):
        r"""Sets the page_no of this ListAllRepositoriesRequest.

        页码

        :param page_no: The page_no of this ListAllRepositoriesRequest.
        :type page_no: int
        """
        self._page_no = page_no

    @property
    def page_size(self):
        r"""Gets the page_size of this ListAllRepositoriesRequest.

        每页大小

        :return: The page_size of this ListAllRepositoriesRequest.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        r"""Sets the page_size of this ListAllRepositoriesRequest.

        每页大小

        :param page_size: The page_size of this ListAllRepositoriesRequest.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def sort(self):
        r"""Gets the sort of this ListAllRepositoriesRequest.

        排序类型

        :return: The sort of this ListAllRepositoriesRequest.
        :rtype: str
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        r"""Sets the sort of this ListAllRepositoriesRequest.

        排序类型

        :param sort: The sort of this ListAllRepositoriesRequest.
        :type sort: str
        """
        self._sort = sort

    @property
    def qname(self):
        r"""Gets the qname of this ListAllRepositoriesRequest.

        查询内容

        :return: The qname of this ListAllRepositoriesRequest.
        :rtype: str
        """
        return self._qname

    @qname.setter
    def qname(self, qname):
        r"""Sets the qname of this ListAllRepositoriesRequest.

        查询内容

        :param qname: The qname of this ListAllRepositoriesRequest.
        :type qname: str
        """
        self._qname = qname

    @property
    def type(self):
        r"""Gets the type of this ListAllRepositoriesRequest.

        仓库类型

        :return: The type of this ListAllRepositoriesRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListAllRepositoriesRequest.

        仓库类型

        :param type: The type of this ListAllRepositoriesRequest.
        :type type: str
        """
        self._type = type

    @property
    def format(self):
        r"""Gets the format of this ListAllRepositoriesRequest.

        仓库格式

        :return: The format of this ListAllRepositoriesRequest.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        r"""Sets the format of this ListAllRepositoriesRequest.

        仓库格式

        :param format: The format of this ListAllRepositoriesRequest.
        :type format: str
        """
        self._format = format

    @property
    def format_list(self):
        r"""Gets the format_list of this ListAllRepositoriesRequest.

        仓库格式列表

        :return: The format_list of this ListAllRepositoriesRequest.
        :rtype: str
        """
        return self._format_list

    @format_list.setter
    def format_list(self, format_list):
        r"""Sets the format_list of this ListAllRepositoriesRequest.

        仓库格式列表

        :param format_list: The format_list of this ListAllRepositoriesRequest.
        :type format_list: str
        """
        self._format_list = format_list

    @property
    def is_recycle_bin(self):
        r"""Gets the is_recycle_bin of this ListAllRepositoriesRequest.

        是否是回收站文件

        :return: The is_recycle_bin of this ListAllRepositoriesRequest.
        :rtype: bool
        """
        return self._is_recycle_bin

    @is_recycle_bin.setter
    def is_recycle_bin(self, is_recycle_bin):
        r"""Sets the is_recycle_bin of this ListAllRepositoriesRequest.

        是否是回收站文件

        :param is_recycle_bin: The is_recycle_bin of this ListAllRepositoriesRequest.
        :type is_recycle_bin: bool
        """
        self._is_recycle_bin = is_recycle_bin

    @property
    def is_need_paging(self):
        r"""Gets the is_need_paging of this ListAllRepositoriesRequest.

        是否需要分页

        :return: The is_need_paging of this ListAllRepositoriesRequest.
        :rtype: bool
        """
        return self._is_need_paging

    @is_need_paging.setter
    def is_need_paging(self, is_need_paging):
        r"""Sets the is_need_paging of this ListAllRepositoriesRequest.

        是否需要分页

        :param is_need_paging: The is_need_paging of this ListAllRepositoriesRequest.
        :type is_need_paging: bool
        """
        self._is_need_paging = is_need_paging

    @property
    def in_project(self):
        r"""Gets the in_project of this ListAllRepositoriesRequest.

        是否在项目中

        :return: The in_project of this ListAllRepositoriesRequest.
        :rtype: bool
        """
        return self._in_project

    @in_project.setter
    def in_project(self, in_project):
        r"""Sets the in_project of this ListAllRepositoriesRequest.

        是否在项目中

        :param in_project: The in_project of this ListAllRepositoriesRequest.
        :type in_project: bool
        """
        self._in_project = in_project

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
        if not isinstance(other, ListAllRepositoriesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
