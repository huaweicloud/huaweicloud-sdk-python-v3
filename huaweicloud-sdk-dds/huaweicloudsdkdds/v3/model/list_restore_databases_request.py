# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRestoreDatabasesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_language': 'str',
        'instance_id': 'str',
        'restore_time': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'instance_id': 'instance_id',
        'restore_time': 'restore_time',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, x_language=None, instance_id=None, restore_time=None, offset=None, limit=None):
        r"""ListRestoreDatabasesRequest

        The model defined in huaweicloud sdk

        :param x_language: 语言。
        :type x_language: str
        :param instance_id: 实例ID，可以调用“查询实例列表和详情”接口获取。如果未申请实例，可以调用“创建实例”接口创建。
        :type instance_id: str
        :param restore_time: 恢复时间点。UNIX时间戳格式，单位是毫秒，时区是UTC。
        :type restore_time: str
        :param offset: 索引位置偏移量。取值大于或等于0。不传该参数时，查询偏移量默认为0。
        :type offset: int
        :param limit: 查询个数上限值。取值范围：1~100。不传该参数时，默认查询前100条信息。
        :type limit: int
        """
        
        

        self._x_language = None
        self._instance_id = None
        self._restore_time = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        self.instance_id = instance_id
        self.restore_time = restore_time
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def x_language(self):
        r"""Gets the x_language of this ListRestoreDatabasesRequest.

        语言。

        :return: The x_language of this ListRestoreDatabasesRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ListRestoreDatabasesRequest.

        语言。

        :param x_language: The x_language of this ListRestoreDatabasesRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListRestoreDatabasesRequest.

        实例ID，可以调用“查询实例列表和详情”接口获取。如果未申请实例，可以调用“创建实例”接口创建。

        :return: The instance_id of this ListRestoreDatabasesRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListRestoreDatabasesRequest.

        实例ID，可以调用“查询实例列表和详情”接口获取。如果未申请实例，可以调用“创建实例”接口创建。

        :param instance_id: The instance_id of this ListRestoreDatabasesRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def restore_time(self):
        r"""Gets the restore_time of this ListRestoreDatabasesRequest.

        恢复时间点。UNIX时间戳格式，单位是毫秒，时区是UTC。

        :return: The restore_time of this ListRestoreDatabasesRequest.
        :rtype: str
        """
        return self._restore_time

    @restore_time.setter
    def restore_time(self, restore_time):
        r"""Sets the restore_time of this ListRestoreDatabasesRequest.

        恢复时间点。UNIX时间戳格式，单位是毫秒，时区是UTC。

        :param restore_time: The restore_time of this ListRestoreDatabasesRequest.
        :type restore_time: str
        """
        self._restore_time = restore_time

    @property
    def offset(self):
        r"""Gets the offset of this ListRestoreDatabasesRequest.

        索引位置偏移量。取值大于或等于0。不传该参数时，查询偏移量默认为0。

        :return: The offset of this ListRestoreDatabasesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListRestoreDatabasesRequest.

        索引位置偏移量。取值大于或等于0。不传该参数时，查询偏移量默认为0。

        :param offset: The offset of this ListRestoreDatabasesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListRestoreDatabasesRequest.

        查询个数上限值。取值范围：1~100。不传该参数时，默认查询前100条信息。

        :return: The limit of this ListRestoreDatabasesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListRestoreDatabasesRequest.

        查询个数上限值。取值范围：1~100。不传该参数时，默认查询前100条信息。

        :param limit: The limit of this ListRestoreDatabasesRequest.
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
        if not isinstance(other, ListRestoreDatabasesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
