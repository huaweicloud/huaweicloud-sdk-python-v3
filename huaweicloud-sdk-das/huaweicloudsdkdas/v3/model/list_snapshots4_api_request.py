# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSnapshots4ApiRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'connection_id': 'str',
        'module': 'int',
        'start_at': 'int',
        'end_at': 'int',
        'per_page': 'int',
        'cur_page': 'int'
    }

    attribute_map = {
        'connection_id': 'connection_id',
        'module': 'module',
        'start_at': 'start_at',
        'end_at': 'end_at',
        'per_page': 'per_page',
        'cur_page': 'cur_page'
    }

    def __init__(self, connection_id=None, module=None, start_at=None, end_at=None, per_page=None, cur_page=None):
        r"""ListSnapshots4ApiRequest

        The model defined in huaweicloud sdk

        :param connection_id: 连接ID
        :type connection_id: str
        :param module: 模块
        :type module: int
        :param start_at: 开始时间（Unix时间戳，毫秒）
        :type start_at: int
        :param end_at: 结束时间（Unix时间戳，毫秒）
        :type end_at: int
        :param per_page: 每页记录数
        :type per_page: int
        :param cur_page: 当前页码
        :type cur_page: int
        """
        
        

        self._connection_id = None
        self._module = None
        self._start_at = None
        self._end_at = None
        self._per_page = None
        self._cur_page = None
        self.discriminator = None

        self.connection_id = connection_id
        if module is not None:
            self.module = module
        if start_at is not None:
            self.start_at = start_at
        if end_at is not None:
            self.end_at = end_at
        if per_page is not None:
            self.per_page = per_page
        if cur_page is not None:
            self.cur_page = cur_page

    @property
    def connection_id(self):
        r"""Gets the connection_id of this ListSnapshots4ApiRequest.

        连接ID

        :return: The connection_id of this ListSnapshots4ApiRequest.
        :rtype: str
        """
        return self._connection_id

    @connection_id.setter
    def connection_id(self, connection_id):
        r"""Sets the connection_id of this ListSnapshots4ApiRequest.

        连接ID

        :param connection_id: The connection_id of this ListSnapshots4ApiRequest.
        :type connection_id: str
        """
        self._connection_id = connection_id

    @property
    def module(self):
        r"""Gets the module of this ListSnapshots4ApiRequest.

        模块

        :return: The module of this ListSnapshots4ApiRequest.
        :rtype: int
        """
        return self._module

    @module.setter
    def module(self, module):
        r"""Sets the module of this ListSnapshots4ApiRequest.

        模块

        :param module: The module of this ListSnapshots4ApiRequest.
        :type module: int
        """
        self._module = module

    @property
    def start_at(self):
        r"""Gets the start_at of this ListSnapshots4ApiRequest.

        开始时间（Unix时间戳，毫秒）

        :return: The start_at of this ListSnapshots4ApiRequest.
        :rtype: int
        """
        return self._start_at

    @start_at.setter
    def start_at(self, start_at):
        r"""Sets the start_at of this ListSnapshots4ApiRequest.

        开始时间（Unix时间戳，毫秒）

        :param start_at: The start_at of this ListSnapshots4ApiRequest.
        :type start_at: int
        """
        self._start_at = start_at

    @property
    def end_at(self):
        r"""Gets the end_at of this ListSnapshots4ApiRequest.

        结束时间（Unix时间戳，毫秒）

        :return: The end_at of this ListSnapshots4ApiRequest.
        :rtype: int
        """
        return self._end_at

    @end_at.setter
    def end_at(self, end_at):
        r"""Sets the end_at of this ListSnapshots4ApiRequest.

        结束时间（Unix时间戳，毫秒）

        :param end_at: The end_at of this ListSnapshots4ApiRequest.
        :type end_at: int
        """
        self._end_at = end_at

    @property
    def per_page(self):
        r"""Gets the per_page of this ListSnapshots4ApiRequest.

        每页记录数

        :return: The per_page of this ListSnapshots4ApiRequest.
        :rtype: int
        """
        return self._per_page

    @per_page.setter
    def per_page(self, per_page):
        r"""Sets the per_page of this ListSnapshots4ApiRequest.

        每页记录数

        :param per_page: The per_page of this ListSnapshots4ApiRequest.
        :type per_page: int
        """
        self._per_page = per_page

    @property
    def cur_page(self):
        r"""Gets the cur_page of this ListSnapshots4ApiRequest.

        当前页码

        :return: The cur_page of this ListSnapshots4ApiRequest.
        :rtype: int
        """
        return self._cur_page

    @cur_page.setter
    def cur_page(self, cur_page):
        r"""Sets the cur_page of this ListSnapshots4ApiRequest.

        当前页码

        :param cur_page: The cur_page of this ListSnapshots4ApiRequest.
        :type cur_page: int
        """
        self._cur_page = cur_page

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListSnapshots4ApiRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
