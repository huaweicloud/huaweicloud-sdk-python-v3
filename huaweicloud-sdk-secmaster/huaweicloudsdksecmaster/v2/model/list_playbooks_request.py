# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPlaybooksRequest:

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
        'search_txt': 'str',
        'enabled': 'bool',
        'offset': 'int',
        'limit': 'int',
        'description': 'str',
        'dataclass_name': 'str',
        'name': 'str'
    }

    attribute_map = {
        'project_id': 'project_id',
        'workspace_id': 'workspace_id',
        'search_txt': 'search_txt',
        'enabled': 'enabled',
        'offset': 'offset',
        'limit': 'limit',
        'description': 'description',
        'dataclass_name': 'dataclass_name',
        'name': 'name'
    }

    def __init__(self, project_id=None, workspace_id=None, search_txt=None, enabled=None, offset=None, limit=None, description=None, dataclass_name=None, name=None):
        r"""ListPlaybooksRequest

        The model defined in huaweicloud sdk

        :param project_id: 项目ID
        :type project_id: str
        :param workspace_id: 工作空间ID
        :type workspace_id: str
        :param search_txt: 搜索关键字
        :type search_txt: str
        :param enabled: 是否启用
        :type enabled: bool
        :param offset: 分页查询参数。用于指定查询结果的起始位置，从0开始
        :type offset: int
        :param limit: 分页查询参数，用于指定一次查询最多的结果数，从1开始
        :type limit: int
        :param description: 剧本描述
        :type description: str
        :param dataclass_name: 数据类名称
        :type dataclass_name: str
        :param name: 剧本名称
        :type name: str
        """
        
        

        self._project_id = None
        self._workspace_id = None
        self._search_txt = None
        self._enabled = None
        self._offset = None
        self._limit = None
        self._description = None
        self._dataclass_name = None
        self._name = None
        self.discriminator = None

        self.project_id = project_id
        self.workspace_id = workspace_id
        if search_txt is not None:
            self.search_txt = search_txt
        if enabled is not None:
            self.enabled = enabled
        self.offset = offset
        self.limit = limit
        if description is not None:
            self.description = description
        if dataclass_name is not None:
            self.dataclass_name = dataclass_name
        if name is not None:
            self.name = name

    @property
    def project_id(self):
        r"""Gets the project_id of this ListPlaybooksRequest.

        项目ID

        :return: The project_id of this ListPlaybooksRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ListPlaybooksRequest.

        项目ID

        :param project_id: The project_id of this ListPlaybooksRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this ListPlaybooksRequest.

        工作空间ID

        :return: The workspace_id of this ListPlaybooksRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this ListPlaybooksRequest.

        工作空间ID

        :param workspace_id: The workspace_id of this ListPlaybooksRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def search_txt(self):
        r"""Gets the search_txt of this ListPlaybooksRequest.

        搜索关键字

        :return: The search_txt of this ListPlaybooksRequest.
        :rtype: str
        """
        return self._search_txt

    @search_txt.setter
    def search_txt(self, search_txt):
        r"""Sets the search_txt of this ListPlaybooksRequest.

        搜索关键字

        :param search_txt: The search_txt of this ListPlaybooksRequest.
        :type search_txt: str
        """
        self._search_txt = search_txt

    @property
    def enabled(self):
        r"""Gets the enabled of this ListPlaybooksRequest.

        是否启用

        :return: The enabled of this ListPlaybooksRequest.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this ListPlaybooksRequest.

        是否启用

        :param enabled: The enabled of this ListPlaybooksRequest.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def offset(self):
        r"""Gets the offset of this ListPlaybooksRequest.

        分页查询参数。用于指定查询结果的起始位置，从0开始

        :return: The offset of this ListPlaybooksRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListPlaybooksRequest.

        分页查询参数。用于指定查询结果的起始位置，从0开始

        :param offset: The offset of this ListPlaybooksRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListPlaybooksRequest.

        分页查询参数，用于指定一次查询最多的结果数，从1开始

        :return: The limit of this ListPlaybooksRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListPlaybooksRequest.

        分页查询参数，用于指定一次查询最多的结果数，从1开始

        :param limit: The limit of this ListPlaybooksRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def description(self):
        r"""Gets the description of this ListPlaybooksRequest.

        剧本描述

        :return: The description of this ListPlaybooksRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ListPlaybooksRequest.

        剧本描述

        :param description: The description of this ListPlaybooksRequest.
        :type description: str
        """
        self._description = description

    @property
    def dataclass_name(self):
        r"""Gets the dataclass_name of this ListPlaybooksRequest.

        数据类名称

        :return: The dataclass_name of this ListPlaybooksRequest.
        :rtype: str
        """
        return self._dataclass_name

    @dataclass_name.setter
    def dataclass_name(self, dataclass_name):
        r"""Sets the dataclass_name of this ListPlaybooksRequest.

        数据类名称

        :param dataclass_name: The dataclass_name of this ListPlaybooksRequest.
        :type dataclass_name: str
        """
        self._dataclass_name = dataclass_name

    @property
    def name(self):
        r"""Gets the name of this ListPlaybooksRequest.

        剧本名称

        :return: The name of this ListPlaybooksRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListPlaybooksRequest.

        剧本名称

        :param name: The name of this ListPlaybooksRequest.
        :type name: str
        """
        self._name = name

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
        if not isinstance(other, ListPlaybooksRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
