# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListImageServersRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'offset': 'int',
        'limit': 'int',
        'server_name': 'str',
        'server_id': 'str',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'server_name': 'server_name',
        'server_id': 'server_id',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, offset=None, limit=None, server_name=None, server_id=None, enterprise_project_id=None):
        r"""ListImageServersRequest

        The model defined in huaweicloud sdk

        :param offset: 查询的偏移量，默认值0。
        :type offset: int
        :param limit: 查询的数量，值区间[1-100]，默认值10。
        :type limit: int
        :param server_name: 镜像实例名称，支持部分匹配。
        :type server_name: str
        :param server_id: 镜像实例唯一标识。
        :type server_id: str
        :param enterprise_project_id: 企业项目ID(字段为空或者0表示使用默认default企业项目)。
        :type enterprise_project_id: str
        """
        
        

        self._offset = None
        self._limit = None
        self._server_name = None
        self._server_id = None
        self._enterprise_project_id = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if server_name is not None:
            self.server_name = server_name
        if server_id is not None:
            self.server_id = server_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def offset(self):
        r"""Gets the offset of this ListImageServersRequest.

        查询的偏移量，默认值0。

        :return: The offset of this ListImageServersRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListImageServersRequest.

        查询的偏移量，默认值0。

        :param offset: The offset of this ListImageServersRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListImageServersRequest.

        查询的数量，值区间[1-100]，默认值10。

        :return: The limit of this ListImageServersRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListImageServersRequest.

        查询的数量，值区间[1-100]，默认值10。

        :param limit: The limit of this ListImageServersRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def server_name(self):
        r"""Gets the server_name of this ListImageServersRequest.

        镜像实例名称，支持部分匹配。

        :return: The server_name of this ListImageServersRequest.
        :rtype: str
        """
        return self._server_name

    @server_name.setter
    def server_name(self, server_name):
        r"""Sets the server_name of this ListImageServersRequest.

        镜像实例名称，支持部分匹配。

        :param server_name: The server_name of this ListImageServersRequest.
        :type server_name: str
        """
        self._server_name = server_name

    @property
    def server_id(self):
        r"""Gets the server_id of this ListImageServersRequest.

        镜像实例唯一标识。

        :return: The server_id of this ListImageServersRequest.
        :rtype: str
        """
        return self._server_id

    @server_id.setter
    def server_id(self, server_id):
        r"""Sets the server_id of this ListImageServersRequest.

        镜像实例唯一标识。

        :param server_id: The server_id of this ListImageServersRequest.
        :type server_id: str
        """
        self._server_id = server_id

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListImageServersRequest.

        企业项目ID(字段为空或者0表示使用默认default企业项目)。

        :return: The enterprise_project_id of this ListImageServersRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListImageServersRequest.

        企业项目ID(字段为空或者0表示使用默认default企业项目)。

        :param enterprise_project_id: The enterprise_project_id of this ListImageServersRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, ListImageServersRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
