# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListWorkflowsRequest:

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
        'offset': 'int',
        'limit': 'int',
        'order': 'str',
        'sortby': 'str',
        'enabled': 'bool',
        'last_version': 'bool',
        'name': 'str',
        'description': 'str',
        'dataclass_id': 'str',
        'dataclass_name': 'str',
        'aop_type': 'str'
    }

    attribute_map = {
        'project_id': 'project_id',
        'workspace_id': 'workspace_id',
        'offset': 'offset',
        'limit': 'limit',
        'order': 'order',
        'sortby': 'sortby',
        'enabled': 'enabled',
        'last_version': 'last_version',
        'name': 'name',
        'description': 'description',
        'dataclass_id': 'dataclass_id',
        'dataclass_name': 'dataclass_name',
        'aop_type': 'aop_type'
    }

    def __init__(self, project_id=None, workspace_id=None, offset=None, limit=None, order=None, sortby=None, enabled=None, last_version=None, name=None, description=None, dataclass_id=None, dataclass_name=None, aop_type=None):
        r"""ListWorkflowsRequest

        The model defined in huaweicloud sdk

        :param project_id: 项目id
        :type project_id: str
        :param workspace_id: 工作空间id
        :type workspace_id: str
        :param offset: 偏移量
        :type offset: int
        :param limit: 数据量
        :type limit: int
        :param order: 排序顺序，asc：升序，desc：降序
        :type order: str
        :param sortby: 排序字段，create_time：创建时间，category：类型分类名称
        :type sortby: str
        :param enabled: 是否启用
        :type enabled: bool
        :param last_version: 最新版本号
        :type last_version: bool
        :param name: 流程名称
        :type name: str
        :param description: 流程描述
        :type description: str
        :param dataclass_id: 数据类ID
        :type dataclass_id: str
        :param dataclass_name: 数据类名称
        :type dataclass_name: str
        :param aop_type: 流程类型
        :type aop_type: str
        """
        
        

        self._project_id = None
        self._workspace_id = None
        self._offset = None
        self._limit = None
        self._order = None
        self._sortby = None
        self._enabled = None
        self._last_version = None
        self._name = None
        self._description = None
        self._dataclass_id = None
        self._dataclass_name = None
        self._aop_type = None
        self.discriminator = None

        self.project_id = project_id
        self.workspace_id = workspace_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if order is not None:
            self.order = order
        if sortby is not None:
            self.sortby = sortby
        if enabled is not None:
            self.enabled = enabled
        if last_version is not None:
            self.last_version = last_version
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if dataclass_id is not None:
            self.dataclass_id = dataclass_id
        if dataclass_name is not None:
            self.dataclass_name = dataclass_name
        if aop_type is not None:
            self.aop_type = aop_type

    @property
    def project_id(self):
        r"""Gets the project_id of this ListWorkflowsRequest.

        项目id

        :return: The project_id of this ListWorkflowsRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ListWorkflowsRequest.

        项目id

        :param project_id: The project_id of this ListWorkflowsRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this ListWorkflowsRequest.

        工作空间id

        :return: The workspace_id of this ListWorkflowsRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this ListWorkflowsRequest.

        工作空间id

        :param workspace_id: The workspace_id of this ListWorkflowsRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def offset(self):
        r"""Gets the offset of this ListWorkflowsRequest.

        偏移量

        :return: The offset of this ListWorkflowsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListWorkflowsRequest.

        偏移量

        :param offset: The offset of this ListWorkflowsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListWorkflowsRequest.

        数据量

        :return: The limit of this ListWorkflowsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListWorkflowsRequest.

        数据量

        :param limit: The limit of this ListWorkflowsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def order(self):
        r"""Gets the order of this ListWorkflowsRequest.

        排序顺序，asc：升序，desc：降序

        :return: The order of this ListWorkflowsRequest.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        r"""Sets the order of this ListWorkflowsRequest.

        排序顺序，asc：升序，desc：降序

        :param order: The order of this ListWorkflowsRequest.
        :type order: str
        """
        self._order = order

    @property
    def sortby(self):
        r"""Gets the sortby of this ListWorkflowsRequest.

        排序字段，create_time：创建时间，category：类型分类名称

        :return: The sortby of this ListWorkflowsRequest.
        :rtype: str
        """
        return self._sortby

    @sortby.setter
    def sortby(self, sortby):
        r"""Sets the sortby of this ListWorkflowsRequest.

        排序字段，create_time：创建时间，category：类型分类名称

        :param sortby: The sortby of this ListWorkflowsRequest.
        :type sortby: str
        """
        self._sortby = sortby

    @property
    def enabled(self):
        r"""Gets the enabled of this ListWorkflowsRequest.

        是否启用

        :return: The enabled of this ListWorkflowsRequest.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this ListWorkflowsRequest.

        是否启用

        :param enabled: The enabled of this ListWorkflowsRequest.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def last_version(self):
        r"""Gets the last_version of this ListWorkflowsRequest.

        最新版本号

        :return: The last_version of this ListWorkflowsRequest.
        :rtype: bool
        """
        return self._last_version

    @last_version.setter
    def last_version(self, last_version):
        r"""Sets the last_version of this ListWorkflowsRequest.

        最新版本号

        :param last_version: The last_version of this ListWorkflowsRequest.
        :type last_version: bool
        """
        self._last_version = last_version

    @property
    def name(self):
        r"""Gets the name of this ListWorkflowsRequest.

        流程名称

        :return: The name of this ListWorkflowsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListWorkflowsRequest.

        流程名称

        :param name: The name of this ListWorkflowsRequest.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this ListWorkflowsRequest.

        流程描述

        :return: The description of this ListWorkflowsRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ListWorkflowsRequest.

        流程描述

        :param description: The description of this ListWorkflowsRequest.
        :type description: str
        """
        self._description = description

    @property
    def dataclass_id(self):
        r"""Gets the dataclass_id of this ListWorkflowsRequest.

        数据类ID

        :return: The dataclass_id of this ListWorkflowsRequest.
        :rtype: str
        """
        return self._dataclass_id

    @dataclass_id.setter
    def dataclass_id(self, dataclass_id):
        r"""Sets the dataclass_id of this ListWorkflowsRequest.

        数据类ID

        :param dataclass_id: The dataclass_id of this ListWorkflowsRequest.
        :type dataclass_id: str
        """
        self._dataclass_id = dataclass_id

    @property
    def dataclass_name(self):
        r"""Gets the dataclass_name of this ListWorkflowsRequest.

        数据类名称

        :return: The dataclass_name of this ListWorkflowsRequest.
        :rtype: str
        """
        return self._dataclass_name

    @dataclass_name.setter
    def dataclass_name(self, dataclass_name):
        r"""Sets the dataclass_name of this ListWorkflowsRequest.

        数据类名称

        :param dataclass_name: The dataclass_name of this ListWorkflowsRequest.
        :type dataclass_name: str
        """
        self._dataclass_name = dataclass_name

    @property
    def aop_type(self):
        r"""Gets the aop_type of this ListWorkflowsRequest.

        流程类型

        :return: The aop_type of this ListWorkflowsRequest.
        :rtype: str
        """
        return self._aop_type

    @aop_type.setter
    def aop_type(self, aop_type):
        r"""Sets the aop_type of this ListWorkflowsRequest.

        流程类型

        :param aop_type: The aop_type of this ListWorkflowsRequest.
        :type aop_type: str
        """
        self._aop_type = aop_type

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
        if not isinstance(other, ListWorkflowsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
