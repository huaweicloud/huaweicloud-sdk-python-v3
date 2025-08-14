# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSecuritySensitiveDataDetailsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'offset': 'int',
        'marker': 'str',
        'database_name': 'str',
        'find_start_time': 'int',
        'find_end_time': 'int',
        'order_by': 'str',
        'order_by_asc': 'bool',
        'workspace': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'offset': 'offset',
        'marker': 'marker',
        'database_name': 'database_name',
        'find_start_time': 'find_start_time',
        'find_end_time': 'find_end_time',
        'order_by': 'order_by',
        'order_by_asc': 'order_by_asc',
        'workspace': 'workspace'
    }

    def __init__(self, limit=None, offset=None, marker=None, database_name=None, find_start_time=None, find_end_time=None, order_by=None, order_by_asc=None, workspace=None):
        r"""ListSecuritySensitiveDataDetailsRequest

        The model defined in huaweicloud sdk

        :param limit: limit
        :type limit: int
        :param offset: offset
        :type offset: int
        :param marker: 用于游标分页，表示查询ID大于该值的记录（不包含该ID），仅支持向前翻页，且不可与offset参数同时使用。
        :type marker: str
        :param database_name: 数据库名称。
        :type database_name: str
        :param find_start_time: 敏感数据发现开始时间。
        :type find_start_time: int
        :param find_end_time: 敏感数据发现结束时间。
        :type find_end_time: int
        :param order_by: 排序字段，FIND_TIME（仅使用limit、offset分页时有效）。
        :type order_by: str
        :param order_by_asc: 是否升序（仅指定排序参数，且使用limit、offset分页时有效）。
        :type order_by_asc: bool
        :param workspace: DataArts Studio工作空间ID
        :type workspace: str
        """
        
        

        self._limit = None
        self._offset = None
        self._marker = None
        self._database_name = None
        self._find_start_time = None
        self._find_end_time = None
        self._order_by = None
        self._order_by_asc = None
        self._workspace = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if marker is not None:
            self.marker = marker
        if database_name is not None:
            self.database_name = database_name
        if find_start_time is not None:
            self.find_start_time = find_start_time
        if find_end_time is not None:
            self.find_end_time = find_end_time
        if order_by is not None:
            self.order_by = order_by
        if order_by_asc is not None:
            self.order_by_asc = order_by_asc
        self.workspace = workspace

    @property
    def limit(self):
        r"""Gets the limit of this ListSecuritySensitiveDataDetailsRequest.

        limit

        :return: The limit of this ListSecuritySensitiveDataDetailsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListSecuritySensitiveDataDetailsRequest.

        limit

        :param limit: The limit of this ListSecuritySensitiveDataDetailsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListSecuritySensitiveDataDetailsRequest.

        offset

        :return: The offset of this ListSecuritySensitiveDataDetailsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListSecuritySensitiveDataDetailsRequest.

        offset

        :param offset: The offset of this ListSecuritySensitiveDataDetailsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def marker(self):
        r"""Gets the marker of this ListSecuritySensitiveDataDetailsRequest.

        用于游标分页，表示查询ID大于该值的记录（不包含该ID），仅支持向前翻页，且不可与offset参数同时使用。

        :return: The marker of this ListSecuritySensitiveDataDetailsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListSecuritySensitiveDataDetailsRequest.

        用于游标分页，表示查询ID大于该值的记录（不包含该ID），仅支持向前翻页，且不可与offset参数同时使用。

        :param marker: The marker of this ListSecuritySensitiveDataDetailsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def database_name(self):
        r"""Gets the database_name of this ListSecuritySensitiveDataDetailsRequest.

        数据库名称。

        :return: The database_name of this ListSecuritySensitiveDataDetailsRequest.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        r"""Sets the database_name of this ListSecuritySensitiveDataDetailsRequest.

        数据库名称。

        :param database_name: The database_name of this ListSecuritySensitiveDataDetailsRequest.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def find_start_time(self):
        r"""Gets the find_start_time of this ListSecuritySensitiveDataDetailsRequest.

        敏感数据发现开始时间。

        :return: The find_start_time of this ListSecuritySensitiveDataDetailsRequest.
        :rtype: int
        """
        return self._find_start_time

    @find_start_time.setter
    def find_start_time(self, find_start_time):
        r"""Sets the find_start_time of this ListSecuritySensitiveDataDetailsRequest.

        敏感数据发现开始时间。

        :param find_start_time: The find_start_time of this ListSecuritySensitiveDataDetailsRequest.
        :type find_start_time: int
        """
        self._find_start_time = find_start_time

    @property
    def find_end_time(self):
        r"""Gets the find_end_time of this ListSecuritySensitiveDataDetailsRequest.

        敏感数据发现结束时间。

        :return: The find_end_time of this ListSecuritySensitiveDataDetailsRequest.
        :rtype: int
        """
        return self._find_end_time

    @find_end_time.setter
    def find_end_time(self, find_end_time):
        r"""Sets the find_end_time of this ListSecuritySensitiveDataDetailsRequest.

        敏感数据发现结束时间。

        :param find_end_time: The find_end_time of this ListSecuritySensitiveDataDetailsRequest.
        :type find_end_time: int
        """
        self._find_end_time = find_end_time

    @property
    def order_by(self):
        r"""Gets the order_by of this ListSecuritySensitiveDataDetailsRequest.

        排序字段，FIND_TIME（仅使用limit、offset分页时有效）。

        :return: The order_by of this ListSecuritySensitiveDataDetailsRequest.
        :rtype: str
        """
        return self._order_by

    @order_by.setter
    def order_by(self, order_by):
        r"""Sets the order_by of this ListSecuritySensitiveDataDetailsRequest.

        排序字段，FIND_TIME（仅使用limit、offset分页时有效）。

        :param order_by: The order_by of this ListSecuritySensitiveDataDetailsRequest.
        :type order_by: str
        """
        self._order_by = order_by

    @property
    def order_by_asc(self):
        r"""Gets the order_by_asc of this ListSecuritySensitiveDataDetailsRequest.

        是否升序（仅指定排序参数，且使用limit、offset分页时有效）。

        :return: The order_by_asc of this ListSecuritySensitiveDataDetailsRequest.
        :rtype: bool
        """
        return self._order_by_asc

    @order_by_asc.setter
    def order_by_asc(self, order_by_asc):
        r"""Sets the order_by_asc of this ListSecuritySensitiveDataDetailsRequest.

        是否升序（仅指定排序参数，且使用limit、offset分页时有效）。

        :param order_by_asc: The order_by_asc of this ListSecuritySensitiveDataDetailsRequest.
        :type order_by_asc: bool
        """
        self._order_by_asc = order_by_asc

    @property
    def workspace(self):
        r"""Gets the workspace of this ListSecuritySensitiveDataDetailsRequest.

        DataArts Studio工作空间ID

        :return: The workspace of this ListSecuritySensitiveDataDetailsRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        r"""Sets the workspace of this ListSecuritySensitiveDataDetailsRequest.

        DataArts Studio工作空间ID

        :param workspace: The workspace of this ListSecuritySensitiveDataDetailsRequest.
        :type workspace: str
        """
        self._workspace = workspace

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
        if not isinstance(other, ListSecuritySensitiveDataDetailsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
