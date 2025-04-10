# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDataclassRequest:

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
        'name': 'str',
        'business_code': 'str',
        'description': 'str',
        'is_built_in': 'bool'
    }

    attribute_map = {
        'project_id': 'project_id',
        'workspace_id': 'workspace_id',
        'offset': 'offset',
        'limit': 'limit',
        'name': 'name',
        'business_code': 'business_code',
        'description': 'description',
        'is_built_in': 'is_built_in'
    }

    def __init__(self, project_id=None, workspace_id=None, offset=None, limit=None, name=None, business_code=None, description=None, is_built_in=None):
        r"""ListDataclassRequest

        The model defined in huaweicloud sdk

        :param project_id: 项目id
        :type project_id: str
        :param workspace_id: 工作空间id
        :type workspace_id: str
        :param offset: 偏移量
        :type offset: int
        :param limit: 数据量
        :type limit: int
        :param name: 名称查询
        :type name: str
        :param business_code: 业务编码
        :type business_code: str
        :param description: 描述
        :type description: str
        :param is_built_in: 是否内置
        :type is_built_in: bool
        """
        
        

        self._project_id = None
        self._workspace_id = None
        self._offset = None
        self._limit = None
        self._name = None
        self._business_code = None
        self._description = None
        self._is_built_in = None
        self.discriminator = None

        self.project_id = project_id
        self.workspace_id = workspace_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if name is not None:
            self.name = name
        if business_code is not None:
            self.business_code = business_code
        if description is not None:
            self.description = description
        if is_built_in is not None:
            self.is_built_in = is_built_in

    @property
    def project_id(self):
        r"""Gets the project_id of this ListDataclassRequest.

        项目id

        :return: The project_id of this ListDataclassRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ListDataclassRequest.

        项目id

        :param project_id: The project_id of this ListDataclassRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this ListDataclassRequest.

        工作空间id

        :return: The workspace_id of this ListDataclassRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this ListDataclassRequest.

        工作空间id

        :param workspace_id: The workspace_id of this ListDataclassRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def offset(self):
        r"""Gets the offset of this ListDataclassRequest.

        偏移量

        :return: The offset of this ListDataclassRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListDataclassRequest.

        偏移量

        :param offset: The offset of this ListDataclassRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListDataclassRequest.

        数据量

        :return: The limit of this ListDataclassRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListDataclassRequest.

        数据量

        :param limit: The limit of this ListDataclassRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def name(self):
        r"""Gets the name of this ListDataclassRequest.

        名称查询

        :return: The name of this ListDataclassRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListDataclassRequest.

        名称查询

        :param name: The name of this ListDataclassRequest.
        :type name: str
        """
        self._name = name

    @property
    def business_code(self):
        r"""Gets the business_code of this ListDataclassRequest.

        业务编码

        :return: The business_code of this ListDataclassRequest.
        :rtype: str
        """
        return self._business_code

    @business_code.setter
    def business_code(self, business_code):
        r"""Sets the business_code of this ListDataclassRequest.

        业务编码

        :param business_code: The business_code of this ListDataclassRequest.
        :type business_code: str
        """
        self._business_code = business_code

    @property
    def description(self):
        r"""Gets the description of this ListDataclassRequest.

        描述

        :return: The description of this ListDataclassRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ListDataclassRequest.

        描述

        :param description: The description of this ListDataclassRequest.
        :type description: str
        """
        self._description = description

    @property
    def is_built_in(self):
        r"""Gets the is_built_in of this ListDataclassRequest.

        是否内置

        :return: The is_built_in of this ListDataclassRequest.
        :rtype: bool
        """
        return self._is_built_in

    @is_built_in.setter
    def is_built_in(self, is_built_in):
        r"""Sets the is_built_in of this ListDataclassRequest.

        是否内置

        :param is_built_in: The is_built_in of this ListDataclassRequest.
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
        if not isinstance(other, ListDataclassRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
