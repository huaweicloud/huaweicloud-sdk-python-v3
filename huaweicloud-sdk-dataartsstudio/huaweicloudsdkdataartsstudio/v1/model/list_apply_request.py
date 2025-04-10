# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListApplyRequest:

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
        'dlm_type': 'str',
        'offset': 'int',
        'limit': 'int',
        'api_name': 'str',
        'query_type': 'int'
    }

    attribute_map = {
        'workspace': 'workspace',
        'dlm_type': 'Dlm-Type',
        'offset': 'offset',
        'limit': 'limit',
        'api_name': 'api_name',
        'query_type': 'query_type'
    }

    def __init__(self, workspace=None, dlm_type=None, offset=None, limit=None, api_name=None, query_type=None):
        r"""ListApplyRequest

        The model defined in huaweicloud sdk

        :param workspace: 工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。
        :type workspace: str
        :param dlm_type: 数据服务的版本类型，指定SHARED共享版或EXCLUSIVE专享版。
        :type dlm_type: str
        :param offset: 查询起始坐标, 即跳过前X条数据。仅支持0或limit的整数倍，不满足则向下取整。
        :type offset: int
        :param limit: 查询条数, 即查询Y条数据。
        :type limit: int
        :param api_name: api名称。
        :type api_name: str
        :param query_type: 查询类型, 0:收到的申请(待审核), 1:收到的申请(已审核), 2:发出的申请(开发), 3:发出的申请(调用)。
        :type query_type: int
        """
        
        

        self._workspace = None
        self._dlm_type = None
        self._offset = None
        self._limit = None
        self._api_name = None
        self._query_type = None
        self.discriminator = None

        self.workspace = workspace
        if dlm_type is not None:
            self.dlm_type = dlm_type
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if api_name is not None:
            self.api_name = api_name
        if query_type is not None:
            self.query_type = query_type

    @property
    def workspace(self):
        r"""Gets the workspace of this ListApplyRequest.

        工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。

        :return: The workspace of this ListApplyRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        r"""Sets the workspace of this ListApplyRequest.

        工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。

        :param workspace: The workspace of this ListApplyRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def dlm_type(self):
        r"""Gets the dlm_type of this ListApplyRequest.

        数据服务的版本类型，指定SHARED共享版或EXCLUSIVE专享版。

        :return: The dlm_type of this ListApplyRequest.
        :rtype: str
        """
        return self._dlm_type

    @dlm_type.setter
    def dlm_type(self, dlm_type):
        r"""Sets the dlm_type of this ListApplyRequest.

        数据服务的版本类型，指定SHARED共享版或EXCLUSIVE专享版。

        :param dlm_type: The dlm_type of this ListApplyRequest.
        :type dlm_type: str
        """
        self._dlm_type = dlm_type

    @property
    def offset(self):
        r"""Gets the offset of this ListApplyRequest.

        查询起始坐标, 即跳过前X条数据。仅支持0或limit的整数倍，不满足则向下取整。

        :return: The offset of this ListApplyRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListApplyRequest.

        查询起始坐标, 即跳过前X条数据。仅支持0或limit的整数倍，不满足则向下取整。

        :param offset: The offset of this ListApplyRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListApplyRequest.

        查询条数, 即查询Y条数据。

        :return: The limit of this ListApplyRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListApplyRequest.

        查询条数, 即查询Y条数据。

        :param limit: The limit of this ListApplyRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def api_name(self):
        r"""Gets the api_name of this ListApplyRequest.

        api名称。

        :return: The api_name of this ListApplyRequest.
        :rtype: str
        """
        return self._api_name

    @api_name.setter
    def api_name(self, api_name):
        r"""Sets the api_name of this ListApplyRequest.

        api名称。

        :param api_name: The api_name of this ListApplyRequest.
        :type api_name: str
        """
        self._api_name = api_name

    @property
    def query_type(self):
        r"""Gets the query_type of this ListApplyRequest.

        查询类型, 0:收到的申请(待审核), 1:收到的申请(已审核), 2:发出的申请(开发), 3:发出的申请(调用)。

        :return: The query_type of this ListApplyRequest.
        :rtype: int
        """
        return self._query_type

    @query_type.setter
    def query_type(self, query_type):
        r"""Sets the query_type of this ListApplyRequest.

        查询类型, 0:收到的申请(待审核), 1:收到的申请(已审核), 2:发出的申请(开发), 3:发出的申请(调用)。

        :param query_type: The query_type of this ListApplyRequest.
        :type query_type: int
        """
        self._query_type = query_type

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
        if not isinstance(other, ListApplyRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
