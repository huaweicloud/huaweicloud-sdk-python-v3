# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProjectStatistic:

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
        'name': 'str',
        'role_type': 'str',
        'creator': 'str',
        'create_time': 'str',
        'update_time': 'str',
        'top_time': 'str',
        'user_statistics': 'list[StatisticDto]',
        'total_statistics': 'list[StatisticDto]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'role_type': 'role_type',
        'creator': 'creator',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'top_time': 'top_time',
        'user_statistics': 'user_statistics',
        'total_statistics': 'total_statistics'
    }

    def __init__(self, id=None, name=None, role_type=None, creator=None, create_time=None, update_time=None, top_time=None, user_statistics=None, total_statistics=None):
        r"""ProjectStatistic

        The model defined in huaweicloud sdk

        :param id: 空间ID。
        :type id: str
        :param name: 空间名称。
        :type name: str
        :param role_type: 用户所属空间的角色。
        :type role_type: str
        :param creator: 空间所有者。
        :type creator: str
        :param create_time: 空间创建时间。
        :type create_time: str
        :param update_time: 空间更新时间。
        :type update_time: str
        :param top_time: 空间置顶时间。
        :type top_time: str
        :param user_statistics: 用户资源统计详情
        :type user_statistics: list[:class:`huaweicloudsdkeihealth.v1.StatisticDto`]
        :param total_statistics: 总资源统计详情
        :type total_statistics: list[:class:`huaweicloudsdkeihealth.v1.StatisticDto`]
        """
        
        

        self._id = None
        self._name = None
        self._role_type = None
        self._creator = None
        self._create_time = None
        self._update_time = None
        self._top_time = None
        self._user_statistics = None
        self._total_statistics = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if role_type is not None:
            self.role_type = role_type
        if creator is not None:
            self.creator = creator
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if top_time is not None:
            self.top_time = top_time
        if user_statistics is not None:
            self.user_statistics = user_statistics
        if total_statistics is not None:
            self.total_statistics = total_statistics

    @property
    def id(self):
        r"""Gets the id of this ProjectStatistic.

        空间ID。

        :return: The id of this ProjectStatistic.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ProjectStatistic.

        空间ID。

        :param id: The id of this ProjectStatistic.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ProjectStatistic.

        空间名称。

        :return: The name of this ProjectStatistic.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ProjectStatistic.

        空间名称。

        :param name: The name of this ProjectStatistic.
        :type name: str
        """
        self._name = name

    @property
    def role_type(self):
        r"""Gets the role_type of this ProjectStatistic.

        用户所属空间的角色。

        :return: The role_type of this ProjectStatistic.
        :rtype: str
        """
        return self._role_type

    @role_type.setter
    def role_type(self, role_type):
        r"""Sets the role_type of this ProjectStatistic.

        用户所属空间的角色。

        :param role_type: The role_type of this ProjectStatistic.
        :type role_type: str
        """
        self._role_type = role_type

    @property
    def creator(self):
        r"""Gets the creator of this ProjectStatistic.

        空间所有者。

        :return: The creator of this ProjectStatistic.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        r"""Sets the creator of this ProjectStatistic.

        空间所有者。

        :param creator: The creator of this ProjectStatistic.
        :type creator: str
        """
        self._creator = creator

    @property
    def create_time(self):
        r"""Gets the create_time of this ProjectStatistic.

        空间创建时间。

        :return: The create_time of this ProjectStatistic.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ProjectStatistic.

        空间创建时间。

        :param create_time: The create_time of this ProjectStatistic.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this ProjectStatistic.

        空间更新时间。

        :return: The update_time of this ProjectStatistic.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ProjectStatistic.

        空间更新时间。

        :param update_time: The update_time of this ProjectStatistic.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def top_time(self):
        r"""Gets the top_time of this ProjectStatistic.

        空间置顶时间。

        :return: The top_time of this ProjectStatistic.
        :rtype: str
        """
        return self._top_time

    @top_time.setter
    def top_time(self, top_time):
        r"""Sets the top_time of this ProjectStatistic.

        空间置顶时间。

        :param top_time: The top_time of this ProjectStatistic.
        :type top_time: str
        """
        self._top_time = top_time

    @property
    def user_statistics(self):
        r"""Gets the user_statistics of this ProjectStatistic.

        用户资源统计详情

        :return: The user_statistics of this ProjectStatistic.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.StatisticDto`]
        """
        return self._user_statistics

    @user_statistics.setter
    def user_statistics(self, user_statistics):
        r"""Sets the user_statistics of this ProjectStatistic.

        用户资源统计详情

        :param user_statistics: The user_statistics of this ProjectStatistic.
        :type user_statistics: list[:class:`huaweicloudsdkeihealth.v1.StatisticDto`]
        """
        self._user_statistics = user_statistics

    @property
    def total_statistics(self):
        r"""Gets the total_statistics of this ProjectStatistic.

        总资源统计详情

        :return: The total_statistics of this ProjectStatistic.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.StatisticDto`]
        """
        return self._total_statistics

    @total_statistics.setter
    def total_statistics(self, total_statistics):
        r"""Sets the total_statistics of this ProjectStatistic.

        总资源统计详情

        :param total_statistics: The total_statistics of this ProjectStatistic.
        :type total_statistics: list[:class:`huaweicloudsdkeihealth.v1.StatisticDto`]
        """
        self._total_statistics = total_statistics

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
        if not isinstance(other, ProjectStatistic):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
