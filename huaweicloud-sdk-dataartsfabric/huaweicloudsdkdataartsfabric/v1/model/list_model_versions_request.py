# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListModelVersionsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workspace_id': 'str',
        'model_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'version_id': 'str',
        'name': 'str'
    }

    attribute_map = {
        'workspace_id': 'workspace_id',
        'model_id': 'model_id',
        'offset': 'offset',
        'limit': 'limit',
        'version_id': 'version_id',
        'name': 'name'
    }

    def __init__(self, workspace_id=None, model_id=None, offset=None, limit=None, version_id=None, name=None):
        r"""ListModelVersionsRequest

        The model defined in huaweicloud sdk

        :param workspace_id: 工作空间ID
        :type workspace_id: str
        :param model_id: Service ID
        :type model_id: str
        :param offset: 偏移量，表示从此偏移量开始查询， offset大于等于0，默认为0。
        :type offset: int
        :param limit: 指定每一页返回的最大条目数，取值范围[1,100]，默认为10。
        :type limit: int
        :param version_id: 模型版本ID
        :type version_id: str
        :param name: 模型版本名称，支持模糊查询
        :type name: str
        """
        
        

        self._workspace_id = None
        self._model_id = None
        self._offset = None
        self._limit = None
        self._version_id = None
        self._name = None
        self.discriminator = None

        self.workspace_id = workspace_id
        self.model_id = model_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if version_id is not None:
            self.version_id = version_id
        if name is not None:
            self.name = name

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this ListModelVersionsRequest.

        工作空间ID

        :return: The workspace_id of this ListModelVersionsRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this ListModelVersionsRequest.

        工作空间ID

        :param workspace_id: The workspace_id of this ListModelVersionsRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def model_id(self):
        r"""Gets the model_id of this ListModelVersionsRequest.

        Service ID

        :return: The model_id of this ListModelVersionsRequest.
        :rtype: str
        """
        return self._model_id

    @model_id.setter
    def model_id(self, model_id):
        r"""Sets the model_id of this ListModelVersionsRequest.

        Service ID

        :param model_id: The model_id of this ListModelVersionsRequest.
        :type model_id: str
        """
        self._model_id = model_id

    @property
    def offset(self):
        r"""Gets the offset of this ListModelVersionsRequest.

        偏移量，表示从此偏移量开始查询， offset大于等于0，默认为0。

        :return: The offset of this ListModelVersionsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListModelVersionsRequest.

        偏移量，表示从此偏移量开始查询， offset大于等于0，默认为0。

        :param offset: The offset of this ListModelVersionsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListModelVersionsRequest.

        指定每一页返回的最大条目数，取值范围[1,100]，默认为10。

        :return: The limit of this ListModelVersionsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListModelVersionsRequest.

        指定每一页返回的最大条目数，取值范围[1,100]，默认为10。

        :param limit: The limit of this ListModelVersionsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def version_id(self):
        r"""Gets the version_id of this ListModelVersionsRequest.

        模型版本ID

        :return: The version_id of this ListModelVersionsRequest.
        :rtype: str
        """
        return self._version_id

    @version_id.setter
    def version_id(self, version_id):
        r"""Sets the version_id of this ListModelVersionsRequest.

        模型版本ID

        :param version_id: The version_id of this ListModelVersionsRequest.
        :type version_id: str
        """
        self._version_id = version_id

    @property
    def name(self):
        r"""Gets the name of this ListModelVersionsRequest.

        模型版本名称，支持模糊查询

        :return: The name of this ListModelVersionsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListModelVersionsRequest.

        模型版本名称，支持模糊查询

        :param name: The name of this ListModelVersionsRequest.
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
        if not isinstance(other, ListModelVersionsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
