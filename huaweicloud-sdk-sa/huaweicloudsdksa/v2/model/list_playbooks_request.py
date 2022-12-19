# coding: utf-8

import re
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
        'component_id': 'str',
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
        'component_id': 'component_id',
        'enabled': 'enabled',
        'offset': 'offset',
        'limit': 'limit',
        'description': 'description',
        'dataclass_name': 'dataclass_name',
        'name': 'name'
    }

    def __init__(self, project_id=None, workspace_id=None, search_txt=None, component_id=None, enabled=None, offset=None, limit=None, description=None, dataclass_name=None, name=None):
        """ListPlaybooksRequest

        The model defined in huaweicloud sdk

        :param project_id: ID of project
        :type project_id: str
        :param workspace_id: ID of workspace
        :type workspace_id: str
        :param search_txt: 搜索关键字
        :type search_txt: str
        :param component_id: component id.
        :type component_id: str
        :param enabled: 是否启用
        :type enabled: bool
        :param offset: request offset, from 0
        :type offset: int
        :param limit: request limit size
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
        self._component_id = None
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
        if component_id is not None:
            self.component_id = component_id
        if enabled is not None:
            self.enabled = enabled
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if description is not None:
            self.description = description
        if dataclass_name is not None:
            self.dataclass_name = dataclass_name
        if name is not None:
            self.name = name

    @property
    def project_id(self):
        """Gets the project_id of this ListPlaybooksRequest.

        ID of project

        :return: The project_id of this ListPlaybooksRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ListPlaybooksRequest.

        ID of project

        :param project_id: The project_id of this ListPlaybooksRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def workspace_id(self):
        """Gets the workspace_id of this ListPlaybooksRequest.

        ID of workspace

        :return: The workspace_id of this ListPlaybooksRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        """Sets the workspace_id of this ListPlaybooksRequest.

        ID of workspace

        :param workspace_id: The workspace_id of this ListPlaybooksRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def search_txt(self):
        """Gets the search_txt of this ListPlaybooksRequest.

        搜索关键字

        :return: The search_txt of this ListPlaybooksRequest.
        :rtype: str
        """
        return self._search_txt

    @search_txt.setter
    def search_txt(self, search_txt):
        """Sets the search_txt of this ListPlaybooksRequest.

        搜索关键字

        :param search_txt: The search_txt of this ListPlaybooksRequest.
        :type search_txt: str
        """
        self._search_txt = search_txt

    @property
    def component_id(self):
        """Gets the component_id of this ListPlaybooksRequest.

        component id.

        :return: The component_id of this ListPlaybooksRequest.
        :rtype: str
        """
        return self._component_id

    @component_id.setter
    def component_id(self, component_id):
        """Sets the component_id of this ListPlaybooksRequest.

        component id.

        :param component_id: The component_id of this ListPlaybooksRequest.
        :type component_id: str
        """
        self._component_id = component_id

    @property
    def enabled(self):
        """Gets the enabled of this ListPlaybooksRequest.

        是否启用

        :return: The enabled of this ListPlaybooksRequest.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this ListPlaybooksRequest.

        是否启用

        :param enabled: The enabled of this ListPlaybooksRequest.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def offset(self):
        """Gets the offset of this ListPlaybooksRequest.

        request offset, from 0

        :return: The offset of this ListPlaybooksRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListPlaybooksRequest.

        request offset, from 0

        :param offset: The offset of this ListPlaybooksRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListPlaybooksRequest.

        request limit size

        :return: The limit of this ListPlaybooksRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListPlaybooksRequest.

        request limit size

        :param limit: The limit of this ListPlaybooksRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def description(self):
        """Gets the description of this ListPlaybooksRequest.

        剧本描述

        :return: The description of this ListPlaybooksRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ListPlaybooksRequest.

        剧本描述

        :param description: The description of this ListPlaybooksRequest.
        :type description: str
        """
        self._description = description

    @property
    def dataclass_name(self):
        """Gets the dataclass_name of this ListPlaybooksRequest.

        数据类名称

        :return: The dataclass_name of this ListPlaybooksRequest.
        :rtype: str
        """
        return self._dataclass_name

    @dataclass_name.setter
    def dataclass_name(self, dataclass_name):
        """Sets the dataclass_name of this ListPlaybooksRequest.

        数据类名称

        :param dataclass_name: The dataclass_name of this ListPlaybooksRequest.
        :type dataclass_name: str
        """
        self._dataclass_name = dataclass_name

    @property
    def name(self):
        """Gets the name of this ListPlaybooksRequest.

        剧本名称

        :return: The name of this ListPlaybooksRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListPlaybooksRequest.

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
