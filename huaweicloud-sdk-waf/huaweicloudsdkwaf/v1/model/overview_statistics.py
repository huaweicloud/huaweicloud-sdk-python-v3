# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OverviewStatistics:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'text_request_count': 'int',
        'image_request_count': 'int',
        'access_type_stats': 'list[AccessTypeStatistics]',
        'category_stats': 'list[CategoryStatistics]',
        'action_stats': 'list[ActionStatistics]',
        'time_range': 'TimeRange',
        'active_app_count': 'int'
    }

    attribute_map = {
        'project_id': 'project_id',
        'text_request_count': 'text_request_count',
        'image_request_count': 'image_request_count',
        'access_type_stats': 'access_type_stats',
        'category_stats': 'category_stats',
        'action_stats': 'action_stats',
        'time_range': 'time_range',
        'active_app_count': 'active_app_count'
    }

    def __init__(self, project_id=None, text_request_count=None, image_request_count=None, access_type_stats=None, category_stats=None, action_stats=None, time_range=None, active_app_count=None):
        r"""OverviewStatistics

        The model defined in huaweicloud sdk

        :param project_id: 项目ID
        :type project_id: str
        :param text_request_count: 用户输入请求数
        :type text_request_count: int
        :param image_request_count: 用户输出请求数
        :type image_request_count: int
        :param access_type_stats: 按接入类型统计
        :type access_type_stats: list[:class:`huaweicloudsdkwaf.v1.AccessTypeStatistics`]
        :param category_stats: 分类别统计数据
        :type category_stats: list[:class:`huaweicloudsdkwaf.v1.CategoryStatistics`]
        :param action_stats: 处置动作统计数据
        :type action_stats: list[:class:`huaweicloudsdkwaf.v1.ActionStatistics`]
        :param time_range: 
        :type time_range: :class:`huaweicloudsdkwaf.v1.TimeRange`
        :param active_app_count: 已开启的AI应用数量
        :type active_app_count: int
        """
        
        

        self._project_id = None
        self._text_request_count = None
        self._image_request_count = None
        self._access_type_stats = None
        self._category_stats = None
        self._action_stats = None
        self._time_range = None
        self._active_app_count = None
        self.discriminator = None

        self.project_id = project_id
        self.text_request_count = text_request_count
        self.image_request_count = image_request_count
        self.access_type_stats = access_type_stats
        self.category_stats = category_stats
        self.action_stats = action_stats
        self.time_range = time_range
        if active_app_count is not None:
            self.active_app_count = active_app_count

    @property
    def project_id(self):
        r"""Gets the project_id of this OverviewStatistics.

        项目ID

        :return: The project_id of this OverviewStatistics.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this OverviewStatistics.

        项目ID

        :param project_id: The project_id of this OverviewStatistics.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def text_request_count(self):
        r"""Gets the text_request_count of this OverviewStatistics.

        用户输入请求数

        :return: The text_request_count of this OverviewStatistics.
        :rtype: int
        """
        return self._text_request_count

    @text_request_count.setter
    def text_request_count(self, text_request_count):
        r"""Sets the text_request_count of this OverviewStatistics.

        用户输入请求数

        :param text_request_count: The text_request_count of this OverviewStatistics.
        :type text_request_count: int
        """
        self._text_request_count = text_request_count

    @property
    def image_request_count(self):
        r"""Gets the image_request_count of this OverviewStatistics.

        用户输出请求数

        :return: The image_request_count of this OverviewStatistics.
        :rtype: int
        """
        return self._image_request_count

    @image_request_count.setter
    def image_request_count(self, image_request_count):
        r"""Sets the image_request_count of this OverviewStatistics.

        用户输出请求数

        :param image_request_count: The image_request_count of this OverviewStatistics.
        :type image_request_count: int
        """
        self._image_request_count = image_request_count

    @property
    def access_type_stats(self):
        r"""Gets the access_type_stats of this OverviewStatistics.

        按接入类型统计

        :return: The access_type_stats of this OverviewStatistics.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.AccessTypeStatistics`]
        """
        return self._access_type_stats

    @access_type_stats.setter
    def access_type_stats(self, access_type_stats):
        r"""Sets the access_type_stats of this OverviewStatistics.

        按接入类型统计

        :param access_type_stats: The access_type_stats of this OverviewStatistics.
        :type access_type_stats: list[:class:`huaweicloudsdkwaf.v1.AccessTypeStatistics`]
        """
        self._access_type_stats = access_type_stats

    @property
    def category_stats(self):
        r"""Gets the category_stats of this OverviewStatistics.

        分类别统计数据

        :return: The category_stats of this OverviewStatistics.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.CategoryStatistics`]
        """
        return self._category_stats

    @category_stats.setter
    def category_stats(self, category_stats):
        r"""Sets the category_stats of this OverviewStatistics.

        分类别统计数据

        :param category_stats: The category_stats of this OverviewStatistics.
        :type category_stats: list[:class:`huaweicloudsdkwaf.v1.CategoryStatistics`]
        """
        self._category_stats = category_stats

    @property
    def action_stats(self):
        r"""Gets the action_stats of this OverviewStatistics.

        处置动作统计数据

        :return: The action_stats of this OverviewStatistics.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.ActionStatistics`]
        """
        return self._action_stats

    @action_stats.setter
    def action_stats(self, action_stats):
        r"""Sets the action_stats of this OverviewStatistics.

        处置动作统计数据

        :param action_stats: The action_stats of this OverviewStatistics.
        :type action_stats: list[:class:`huaweicloudsdkwaf.v1.ActionStatistics`]
        """
        self._action_stats = action_stats

    @property
    def time_range(self):
        r"""Gets the time_range of this OverviewStatistics.

        :return: The time_range of this OverviewStatistics.
        :rtype: :class:`huaweicloudsdkwaf.v1.TimeRange`
        """
        return self._time_range

    @time_range.setter
    def time_range(self, time_range):
        r"""Sets the time_range of this OverviewStatistics.

        :param time_range: The time_range of this OverviewStatistics.
        :type time_range: :class:`huaweicloudsdkwaf.v1.TimeRange`
        """
        self._time_range = time_range

    @property
    def active_app_count(self):
        r"""Gets the active_app_count of this OverviewStatistics.

        已开启的AI应用数量

        :return: The active_app_count of this OverviewStatistics.
        :rtype: int
        """
        return self._active_app_count

    @active_app_count.setter
    def active_app_count(self, active_app_count):
        r"""Sets the active_app_count of this OverviewStatistics.

        已开启的AI应用数量

        :param active_app_count: The active_app_count of this OverviewStatistics.
        :type active_app_count: int
        """
        self._active_app_count = active_app_count

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
        if not isinstance(other, OverviewStatistics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
