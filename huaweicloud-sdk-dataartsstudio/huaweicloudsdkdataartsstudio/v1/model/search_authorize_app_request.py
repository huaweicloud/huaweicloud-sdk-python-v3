# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SearchAuthorizeAppRequest:

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
        'api_id': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'workspace': 'workspace',
        'dlm_type': 'Dlm-Type',
        'api_id': 'api_id',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, workspace=None, dlm_type=None, api_id=None, offset=None, limit=None):
        r"""SearchAuthorizeAppRequest

        The model defined in huaweicloud sdk

        :param workspace: 工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。
        :type workspace: str
        :param dlm_type: 数据服务的版本类型，指定SHARED共享版或EXCLUSIVE专享版。
        :type dlm_type: str
        :param api_id: api编号。
        :type api_id: str
        :param offset: 查询起始坐标, 即跳过前X条数据。仅支持0或limit的整数倍，不满足则向下取整。
        :type offset: int
        :param limit: 查询条数, 即查询Y条数据。
        :type limit: int
        """
        
        

        self._workspace = None
        self._dlm_type = None
        self._api_id = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.workspace = workspace
        if dlm_type is not None:
            self.dlm_type = dlm_type
        self.api_id = api_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def workspace(self):
        r"""Gets the workspace of this SearchAuthorizeAppRequest.

        工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。

        :return: The workspace of this SearchAuthorizeAppRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        r"""Sets the workspace of this SearchAuthorizeAppRequest.

        工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。

        :param workspace: The workspace of this SearchAuthorizeAppRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def dlm_type(self):
        r"""Gets the dlm_type of this SearchAuthorizeAppRequest.

        数据服务的版本类型，指定SHARED共享版或EXCLUSIVE专享版。

        :return: The dlm_type of this SearchAuthorizeAppRequest.
        :rtype: str
        """
        return self._dlm_type

    @dlm_type.setter
    def dlm_type(self, dlm_type):
        r"""Sets the dlm_type of this SearchAuthorizeAppRequest.

        数据服务的版本类型，指定SHARED共享版或EXCLUSIVE专享版。

        :param dlm_type: The dlm_type of this SearchAuthorizeAppRequest.
        :type dlm_type: str
        """
        self._dlm_type = dlm_type

    @property
    def api_id(self):
        r"""Gets the api_id of this SearchAuthorizeAppRequest.

        api编号。

        :return: The api_id of this SearchAuthorizeAppRequest.
        :rtype: str
        """
        return self._api_id

    @api_id.setter
    def api_id(self, api_id):
        r"""Sets the api_id of this SearchAuthorizeAppRequest.

        api编号。

        :param api_id: The api_id of this SearchAuthorizeAppRequest.
        :type api_id: str
        """
        self._api_id = api_id

    @property
    def offset(self):
        r"""Gets the offset of this SearchAuthorizeAppRequest.

        查询起始坐标, 即跳过前X条数据。仅支持0或limit的整数倍，不满足则向下取整。

        :return: The offset of this SearchAuthorizeAppRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this SearchAuthorizeAppRequest.

        查询起始坐标, 即跳过前X条数据。仅支持0或limit的整数倍，不满足则向下取整。

        :param offset: The offset of this SearchAuthorizeAppRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this SearchAuthorizeAppRequest.

        查询条数, 即查询Y条数据。

        :return: The limit of this SearchAuthorizeAppRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this SearchAuthorizeAppRequest.

        查询条数, 即查询Y条数据。

        :param limit: The limit of this SearchAuthorizeAppRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, SearchAuthorizeAppRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
