# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDesktopPoolsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'type': 'str',
        'enterprise_project_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'in_maintenance_mode': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'enterprise_project_id': 'enterprise_project_id',
        'offset': 'offset',
        'limit': 'limit',
        'in_maintenance_mode': 'in_maintenance_mode'
    }

    def __init__(self, name=None, type=None, enterprise_project_id=None, offset=None, limit=None, in_maintenance_mode=None):
        r"""ListDesktopPoolsRequest

        The model defined in huaweicloud sdk

        :param name: 桌面池名称。
        :type name: str
        :param type: 桌面池类型，DYNAMIC：动态池，STATIC：静态池。
        :type type: str
        :param enterprise_project_id: 企业项目ID。
        :type enterprise_project_id: str
        :param offset: 用于分页查询，查询的起始记录序号，从0开始。
        :type offset: int
        :param limit: 用于分页查询，取值范围0-1000，默认值1000。
        :type limit: int
        :param in_maintenance_mode: 按照维护状态过滤。
        :type in_maintenance_mode: bool
        """
        
        

        self._name = None
        self._type = None
        self._enterprise_project_id = None
        self._offset = None
        self._limit = None
        self._in_maintenance_mode = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if in_maintenance_mode is not None:
            self.in_maintenance_mode = in_maintenance_mode

    @property
    def name(self):
        r"""Gets the name of this ListDesktopPoolsRequest.

        桌面池名称。

        :return: The name of this ListDesktopPoolsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListDesktopPoolsRequest.

        桌面池名称。

        :param name: The name of this ListDesktopPoolsRequest.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this ListDesktopPoolsRequest.

        桌面池类型，DYNAMIC：动态池，STATIC：静态池。

        :return: The type of this ListDesktopPoolsRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListDesktopPoolsRequest.

        桌面池类型，DYNAMIC：动态池，STATIC：静态池。

        :param type: The type of this ListDesktopPoolsRequest.
        :type type: str
        """
        self._type = type

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListDesktopPoolsRequest.

        企业项目ID。

        :return: The enterprise_project_id of this ListDesktopPoolsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListDesktopPoolsRequest.

        企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this ListDesktopPoolsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def offset(self):
        r"""Gets the offset of this ListDesktopPoolsRequest.

        用于分页查询，查询的起始记录序号，从0开始。

        :return: The offset of this ListDesktopPoolsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListDesktopPoolsRequest.

        用于分页查询，查询的起始记录序号，从0开始。

        :param offset: The offset of this ListDesktopPoolsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListDesktopPoolsRequest.

        用于分页查询，取值范围0-1000，默认值1000。

        :return: The limit of this ListDesktopPoolsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListDesktopPoolsRequest.

        用于分页查询，取值范围0-1000，默认值1000。

        :param limit: The limit of this ListDesktopPoolsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def in_maintenance_mode(self):
        r"""Gets the in_maintenance_mode of this ListDesktopPoolsRequest.

        按照维护状态过滤。

        :return: The in_maintenance_mode of this ListDesktopPoolsRequest.
        :rtype: bool
        """
        return self._in_maintenance_mode

    @in_maintenance_mode.setter
    def in_maintenance_mode(self, in_maintenance_mode):
        r"""Sets the in_maintenance_mode of this ListDesktopPoolsRequest.

        按照维护状态过滤。

        :param in_maintenance_mode: The in_maintenance_mode of this ListDesktopPoolsRequest.
        :type in_maintenance_mode: bool
        """
        self._in_maintenance_mode = in_maintenance_mode

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
        if not isinstance(other, ListDesktopPoolsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
