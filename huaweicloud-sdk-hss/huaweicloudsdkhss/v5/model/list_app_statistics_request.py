# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAppStatisticsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'app_name': 'str',
        'enterprise_project_id': 'str',
        'limit': 'int',
        'offset': 'int',
        'category': 'str'
    }

    attribute_map = {
        'app_name': 'app_name',
        'enterprise_project_id': 'enterprise_project_id',
        'limit': 'limit',
        'offset': 'offset',
        'category': 'category'
    }

    def __init__(self, app_name=None, enterprise_project_id=None, limit=None, offset=None, category=None):
        r"""ListAppStatisticsRequest

        The model defined in huaweicloud sdk

        :param app_name: 软件名称
        :type app_name: str
        :param enterprise_project_id: 主机所属的企业项目ID。 开通企业项目功能后才需要配置企业项目。 企业项目ID默认取值为“0”，表示默认企业项目。如果需要查询所有企业项目下的主机，请传参“all_granted_eps”。如果您只有某个企业项目的权限，则需要传递该企业项目ID，查询该企业项目下的主机，否则会因权限不足而报错。
        :type enterprise_project_id: str
        :param limit: 每页显示数量
        :type limit: int
        :param offset: 偏移量：指定返回记录的开始位置
        :type offset: int
        :param category: 类别，默认为host，包含如下： - host：主机 - container：容器
        :type category: str
        """
        
        

        self._app_name = None
        self._enterprise_project_id = None
        self._limit = None
        self._offset = None
        self._category = None
        self.discriminator = None

        if app_name is not None:
            self.app_name = app_name
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if category is not None:
            self.category = category

    @property
    def app_name(self):
        r"""Gets the app_name of this ListAppStatisticsRequest.

        软件名称

        :return: The app_name of this ListAppStatisticsRequest.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        r"""Sets the app_name of this ListAppStatisticsRequest.

        软件名称

        :param app_name: The app_name of this ListAppStatisticsRequest.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListAppStatisticsRequest.

        主机所属的企业项目ID。 开通企业项目功能后才需要配置企业项目。 企业项目ID默认取值为“0”，表示默认企业项目。如果需要查询所有企业项目下的主机，请传参“all_granted_eps”。如果您只有某个企业项目的权限，则需要传递该企业项目ID，查询该企业项目下的主机，否则会因权限不足而报错。

        :return: The enterprise_project_id of this ListAppStatisticsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListAppStatisticsRequest.

        主机所属的企业项目ID。 开通企业项目功能后才需要配置企业项目。 企业项目ID默认取值为“0”，表示默认企业项目。如果需要查询所有企业项目下的主机，请传参“all_granted_eps”。如果您只有某个企业项目的权限，则需要传递该企业项目ID，查询该企业项目下的主机，否则会因权限不足而报错。

        :param enterprise_project_id: The enterprise_project_id of this ListAppStatisticsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def limit(self):
        r"""Gets the limit of this ListAppStatisticsRequest.

        每页显示数量

        :return: The limit of this ListAppStatisticsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListAppStatisticsRequest.

        每页显示数量

        :param limit: The limit of this ListAppStatisticsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListAppStatisticsRequest.

        偏移量：指定返回记录的开始位置

        :return: The offset of this ListAppStatisticsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListAppStatisticsRequest.

        偏移量：指定返回记录的开始位置

        :param offset: The offset of this ListAppStatisticsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def category(self):
        r"""Gets the category of this ListAppStatisticsRequest.

        类别，默认为host，包含如下： - host：主机 - container：容器

        :return: The category of this ListAppStatisticsRequest.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this ListAppStatisticsRequest.

        类别，默认为host，包含如下： - host：主机 - container：容器

        :param category: The category of this ListAppStatisticsRequest.
        :type category: str
        """
        self._category = category

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
        if not isinstance(other, ListAppStatisticsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
