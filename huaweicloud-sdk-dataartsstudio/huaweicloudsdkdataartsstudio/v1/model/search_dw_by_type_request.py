# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SearchDwByTypeRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workspace': 'str',
        'x_project_id': 'str',
        'force_refresh': 'bool',
        'dw_type': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'workspace': 'workspace',
        'x_project_id': 'X-Project-Id',
        'force_refresh': 'force_refresh',
        'dw_type': 'dw_type',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, workspace=None, x_project_id=None, force_refresh=None, dw_type=None, limit=None, offset=None):
        r"""SearchDwByTypeRequest

        The model defined in huaweicloud sdk

        :param workspace: 工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。
        :type workspace: str
        :param x_project_id: 项目ID，获取方法请参见[项目ID和账号ID](projectid_accountid.xml)。  多project场景采用AK/SK认证的接口请求，则该字段必选。
        :type x_project_id: str
        :param force_refresh: 是否查询最新的。
        :type force_refresh: bool
        :param dw_type: 数据连接类型。
        :type dw_type: str
        :param limit: limit
        :type limit: int
        :param offset: limit
        :type offset: int
        """
        
        

        self._workspace = None
        self._x_project_id = None
        self._force_refresh = None
        self._dw_type = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        self.workspace = workspace
        if x_project_id is not None:
            self.x_project_id = x_project_id
        if force_refresh is not None:
            self.force_refresh = force_refresh
        self.dw_type = dw_type
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def workspace(self):
        r"""Gets the workspace of this SearchDwByTypeRequest.

        工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。

        :return: The workspace of this SearchDwByTypeRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        r"""Sets the workspace of this SearchDwByTypeRequest.

        工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。

        :param workspace: The workspace of this SearchDwByTypeRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def x_project_id(self):
        r"""Gets the x_project_id of this SearchDwByTypeRequest.

        项目ID，获取方法请参见[项目ID和账号ID](projectid_accountid.xml)。  多project场景采用AK/SK认证的接口请求，则该字段必选。

        :return: The x_project_id of this SearchDwByTypeRequest.
        :rtype: str
        """
        return self._x_project_id

    @x_project_id.setter
    def x_project_id(self, x_project_id):
        r"""Sets the x_project_id of this SearchDwByTypeRequest.

        项目ID，获取方法请参见[项目ID和账号ID](projectid_accountid.xml)。  多project场景采用AK/SK认证的接口请求，则该字段必选。

        :param x_project_id: The x_project_id of this SearchDwByTypeRequest.
        :type x_project_id: str
        """
        self._x_project_id = x_project_id

    @property
    def force_refresh(self):
        r"""Gets the force_refresh of this SearchDwByTypeRequest.

        是否查询最新的。

        :return: The force_refresh of this SearchDwByTypeRequest.
        :rtype: bool
        """
        return self._force_refresh

    @force_refresh.setter
    def force_refresh(self, force_refresh):
        r"""Sets the force_refresh of this SearchDwByTypeRequest.

        是否查询最新的。

        :param force_refresh: The force_refresh of this SearchDwByTypeRequest.
        :type force_refresh: bool
        """
        self._force_refresh = force_refresh

    @property
    def dw_type(self):
        r"""Gets the dw_type of this SearchDwByTypeRequest.

        数据连接类型。

        :return: The dw_type of this SearchDwByTypeRequest.
        :rtype: str
        """
        return self._dw_type

    @dw_type.setter
    def dw_type(self, dw_type):
        r"""Sets the dw_type of this SearchDwByTypeRequest.

        数据连接类型。

        :param dw_type: The dw_type of this SearchDwByTypeRequest.
        :type dw_type: str
        """
        self._dw_type = dw_type

    @property
    def limit(self):
        r"""Gets the limit of this SearchDwByTypeRequest.

        limit

        :return: The limit of this SearchDwByTypeRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this SearchDwByTypeRequest.

        limit

        :param limit: The limit of this SearchDwByTypeRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this SearchDwByTypeRequest.

        limit

        :return: The offset of this SearchDwByTypeRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this SearchDwByTypeRequest.

        limit

        :param offset: The offset of this SearchDwByTypeRequest.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, SearchDwByTypeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
