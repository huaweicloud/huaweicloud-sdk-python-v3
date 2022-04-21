# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RpoStattisticsParams:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'point_time': 'str',
        'resource_num': 'int',
        'resource_type': 'str',
        'created_at': 'str',
        'updated_at': 'str'
    }

    attribute_map = {
        'id': 'id',
        'point_time': 'point_time',
        'resource_num': 'resource_num',
        'resource_type': 'resource_type',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, point_time=None, resource_num=None, resource_type=None, created_at=None, updated_at=None):
        """RpoStattisticsParams

        The model defined in huaweicloud sdk

        :param id: 资源的RPO超标趋势记录id。
        :type id: str
        :param point_time: 资源的RPO超标趋势记录打点时间。默认格式为：\&quot;yyyy-MM-dd HH:mm\&quot;。
        :type point_time: str
        :param resource_num: RPO超标的资源个数。
        :type resource_num: int
        :param resource_type: RPO超标的资源类型。replication：表示查询复制对的RPO超标趋势记录。
        :type resource_type: str
        :param created_at: 创建时间。默认格式为：\&quot;yyyy-MM-dd HH:mm:ss.SSS\&quot;，例：\&quot;2019-04-01 12:00:00.000\&quot;。
        :type created_at: str
        :param updated_at: 更新时间。默认格式为：\&quot;yyyy-MM-dd HH:mm:ss.SSS\&quot;，例：\&quot;2019-04-01 12:00:00.000\&quot;。
        :type updated_at: str
        """
        
        

        self._id = None
        self._point_time = None
        self._resource_num = None
        self._resource_type = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        self.id = id
        self.point_time = point_time
        self.resource_num = resource_num
        self.resource_type = resource_type
        self.created_at = created_at
        self.updated_at = updated_at

    @property
    def id(self):
        """Gets the id of this RpoStattisticsParams.

        资源的RPO超标趋势记录id。

        :return: The id of this RpoStattisticsParams.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RpoStattisticsParams.

        资源的RPO超标趋势记录id。

        :param id: The id of this RpoStattisticsParams.
        :type id: str
        """
        self._id = id

    @property
    def point_time(self):
        """Gets the point_time of this RpoStattisticsParams.

        资源的RPO超标趋势记录打点时间。默认格式为：\"yyyy-MM-dd HH:mm\"。

        :return: The point_time of this RpoStattisticsParams.
        :rtype: str
        """
        return self._point_time

    @point_time.setter
    def point_time(self, point_time):
        """Sets the point_time of this RpoStattisticsParams.

        资源的RPO超标趋势记录打点时间。默认格式为：\"yyyy-MM-dd HH:mm\"。

        :param point_time: The point_time of this RpoStattisticsParams.
        :type point_time: str
        """
        self._point_time = point_time

    @property
    def resource_num(self):
        """Gets the resource_num of this RpoStattisticsParams.

        RPO超标的资源个数。

        :return: The resource_num of this RpoStattisticsParams.
        :rtype: int
        """
        return self._resource_num

    @resource_num.setter
    def resource_num(self, resource_num):
        """Sets the resource_num of this RpoStattisticsParams.

        RPO超标的资源个数。

        :param resource_num: The resource_num of this RpoStattisticsParams.
        :type resource_num: int
        """
        self._resource_num = resource_num

    @property
    def resource_type(self):
        """Gets the resource_type of this RpoStattisticsParams.

        RPO超标的资源类型。replication：表示查询复制对的RPO超标趋势记录。

        :return: The resource_type of this RpoStattisticsParams.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this RpoStattisticsParams.

        RPO超标的资源类型。replication：表示查询复制对的RPO超标趋势记录。

        :param resource_type: The resource_type of this RpoStattisticsParams.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def created_at(self):
        """Gets the created_at of this RpoStattisticsParams.

        创建时间。默认格式为：\"yyyy-MM-dd HH:mm:ss.SSS\"，例：\"2019-04-01 12:00:00.000\"。

        :return: The created_at of this RpoStattisticsParams.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this RpoStattisticsParams.

        创建时间。默认格式为：\"yyyy-MM-dd HH:mm:ss.SSS\"，例：\"2019-04-01 12:00:00.000\"。

        :param created_at: The created_at of this RpoStattisticsParams.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this RpoStattisticsParams.

        更新时间。默认格式为：\"yyyy-MM-dd HH:mm:ss.SSS\"，例：\"2019-04-01 12:00:00.000\"。

        :return: The updated_at of this RpoStattisticsParams.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this RpoStattisticsParams.

        更新时间。默认格式为：\"yyyy-MM-dd HH:mm:ss.SSS\"，例：\"2019-04-01 12:00:00.000\"。

        :param updated_at: The updated_at of this RpoStattisticsParams.
        :type updated_at: str
        """
        self._updated_at = updated_at

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
        if not isinstance(other, RpoStattisticsParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
