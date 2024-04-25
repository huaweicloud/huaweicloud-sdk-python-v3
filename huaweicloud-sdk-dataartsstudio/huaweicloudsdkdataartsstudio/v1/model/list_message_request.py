# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListMessageRequest:

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
        'api_name': 'str'
    }

    attribute_map = {
        'workspace': 'workspace',
        'dlm_type': 'Dlm-Type',
        'offset': 'offset',
        'limit': 'limit',
        'api_name': 'api_name'
    }

    def __init__(self, workspace=None, dlm_type=None, offset=None, limit=None, api_name=None):
        """ListMessageRequest

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
        """
        
        

        self._workspace = None
        self._dlm_type = None
        self._offset = None
        self._limit = None
        self._api_name = None
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

    @property
    def workspace(self):
        """Gets the workspace of this ListMessageRequest.

        工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。

        :return: The workspace of this ListMessageRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        """Sets the workspace of this ListMessageRequest.

        工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。

        :param workspace: The workspace of this ListMessageRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def dlm_type(self):
        """Gets the dlm_type of this ListMessageRequest.

        数据服务的版本类型，指定SHARED共享版或EXCLUSIVE专享版。

        :return: The dlm_type of this ListMessageRequest.
        :rtype: str
        """
        return self._dlm_type

    @dlm_type.setter
    def dlm_type(self, dlm_type):
        """Sets the dlm_type of this ListMessageRequest.

        数据服务的版本类型，指定SHARED共享版或EXCLUSIVE专享版。

        :param dlm_type: The dlm_type of this ListMessageRequest.
        :type dlm_type: str
        """
        self._dlm_type = dlm_type

    @property
    def offset(self):
        """Gets the offset of this ListMessageRequest.

        查询起始坐标, 即跳过前X条数据。仅支持0或limit的整数倍，不满足则向下取整。

        :return: The offset of this ListMessageRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListMessageRequest.

        查询起始坐标, 即跳过前X条数据。仅支持0或limit的整数倍，不满足则向下取整。

        :param offset: The offset of this ListMessageRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListMessageRequest.

        查询条数, 即查询Y条数据。

        :return: The limit of this ListMessageRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListMessageRequest.

        查询条数, 即查询Y条数据。

        :param limit: The limit of this ListMessageRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def api_name(self):
        """Gets the api_name of this ListMessageRequest.

        api名称。

        :return: The api_name of this ListMessageRequest.
        :rtype: str
        """
        return self._api_name

    @api_name.setter
    def api_name(self, api_name):
        """Sets the api_name of this ListMessageRequest.

        api名称。

        :param api_name: The api_name of this ListMessageRequest.
        :type api_name: str
        """
        self._api_name = api_name

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
        if not isinstance(other, ListMessageRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
