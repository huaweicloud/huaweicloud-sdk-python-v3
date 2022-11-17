# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListLogtanksRequest:

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
        'marker': 'str',
        'page_reverse': 'bool',
        'enterprise_project_id': 'list[str]',
        'id': 'list[str]',
        'loadbalancer_id': 'list[str]',
        'log_group_id': 'list[str]',
        'log_topic_id': 'list[str]'
    }

    attribute_map = {
        'limit': 'limit',
        'marker': 'marker',
        'page_reverse': 'page_reverse',
        'enterprise_project_id': 'enterprise_project_id',
        'id': 'id',
        'loadbalancer_id': 'loadbalancer_id',
        'log_group_id': 'log_group_id',
        'log_topic_id': 'log_topic_id'
    }

    def __init__(self, limit=None, marker=None, page_reverse=None, enterprise_project_id=None, id=None, loadbalancer_id=None, log_group_id=None, log_topic_id=None):
        """ListLogtanksRequest

        The model defined in huaweicloud sdk

        :param limit: 每页返回的个数。
        :type limit: int
        :param marker: 上一页最后一条记录的ID。  使用说明： - 必须与limit一起使用。 - 不指定时表示查询第一页。 - 该字段不允许为空或无效的ID。
        :type marker: str
        :param page_reverse: 是否反向查询。  取值： - true：查询上一页。 - false：查询下一页，默认。  使用说明： - 必须与limit一起使用。 - 当page_reverse&#x3D;true时，若要查询上一页，marker取值为当前页返回值的previous_marker
        :type page_reverse: bool
        :param enterprise_project_id: 企业项目ID。 支持多值查询，查询条件格式：enterprise_project_id&#x3D;xxx&amp;enterprise_project_id&#x3D;xxx。  [不支持该字段，请勿使用。](tag:dt,dt_test,hcso_dt)
        :type enterprise_project_id: list[str]
        :param id: 云日志记录ID。 支持多值查询，查询条件格式：id&#x3D;xxx&amp;id&#x3D;xxx。
        :type id: list[str]
        :param loadbalancer_id: 负载均衡器ID。 支持多值查询，查询条件格式：loadbalancer_id&#x3D;xxx&amp;loadbalancer_id&#x3D;xxx。
        :type loadbalancer_id: list[str]
        :param log_group_id: 云日志分组ID。 支持多值查询，查询条件格式：log_group_id&#x3D;xxx&amp;log_group_id&#x3D;xxx。
        :type log_group_id: list[str]
        :param log_topic_id: 云日志主题ID 支持多值查询，查询条件格式：log_topic_id&#x3D;xxx&amp;log_topic_id&#x3D;xxx。
        :type log_topic_id: list[str]
        """
        
        

        self._limit = None
        self._marker = None
        self._page_reverse = None
        self._enterprise_project_id = None
        self._id = None
        self._loadbalancer_id = None
        self._log_group_id = None
        self._log_topic_id = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if page_reverse is not None:
            self.page_reverse = page_reverse
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if id is not None:
            self.id = id
        if loadbalancer_id is not None:
            self.loadbalancer_id = loadbalancer_id
        if log_group_id is not None:
            self.log_group_id = log_group_id
        if log_topic_id is not None:
            self.log_topic_id = log_topic_id

    @property
    def limit(self):
        """Gets the limit of this ListLogtanksRequest.

        每页返回的个数。

        :return: The limit of this ListLogtanksRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListLogtanksRequest.

        每页返回的个数。

        :param limit: The limit of this ListLogtanksRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListLogtanksRequest.

        上一页最后一条记录的ID。  使用说明： - 必须与limit一起使用。 - 不指定时表示查询第一页。 - 该字段不允许为空或无效的ID。

        :return: The marker of this ListLogtanksRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListLogtanksRequest.

        上一页最后一条记录的ID。  使用说明： - 必须与limit一起使用。 - 不指定时表示查询第一页。 - 该字段不允许为空或无效的ID。

        :param marker: The marker of this ListLogtanksRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def page_reverse(self):
        """Gets the page_reverse of this ListLogtanksRequest.

        是否反向查询。  取值： - true：查询上一页。 - false：查询下一页，默认。  使用说明： - 必须与limit一起使用。 - 当page_reverse=true时，若要查询上一页，marker取值为当前页返回值的previous_marker

        :return: The page_reverse of this ListLogtanksRequest.
        :rtype: bool
        """
        return self._page_reverse

    @page_reverse.setter
    def page_reverse(self, page_reverse):
        """Sets the page_reverse of this ListLogtanksRequest.

        是否反向查询。  取值： - true：查询上一页。 - false：查询下一页，默认。  使用说明： - 必须与limit一起使用。 - 当page_reverse=true时，若要查询上一页，marker取值为当前页返回值的previous_marker

        :param page_reverse: The page_reverse of this ListLogtanksRequest.
        :type page_reverse: bool
        """
        self._page_reverse = page_reverse

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListLogtanksRequest.

        企业项目ID。 支持多值查询，查询条件格式：enterprise_project_id=xxx&enterprise_project_id=xxx。  [不支持该字段，请勿使用。](tag:dt,dt_test,hcso_dt)

        :return: The enterprise_project_id of this ListLogtanksRequest.
        :rtype: list[str]
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListLogtanksRequest.

        企业项目ID。 支持多值查询，查询条件格式：enterprise_project_id=xxx&enterprise_project_id=xxx。  [不支持该字段，请勿使用。](tag:dt,dt_test,hcso_dt)

        :param enterprise_project_id: The enterprise_project_id of this ListLogtanksRequest.
        :type enterprise_project_id: list[str]
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def id(self):
        """Gets the id of this ListLogtanksRequest.

        云日志记录ID。 支持多值查询，查询条件格式：id=xxx&id=xxx。

        :return: The id of this ListLogtanksRequest.
        :rtype: list[str]
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListLogtanksRequest.

        云日志记录ID。 支持多值查询，查询条件格式：id=xxx&id=xxx。

        :param id: The id of this ListLogtanksRequest.
        :type id: list[str]
        """
        self._id = id

    @property
    def loadbalancer_id(self):
        """Gets the loadbalancer_id of this ListLogtanksRequest.

        负载均衡器ID。 支持多值查询，查询条件格式：loadbalancer_id=xxx&loadbalancer_id=xxx。

        :return: The loadbalancer_id of this ListLogtanksRequest.
        :rtype: list[str]
        """
        return self._loadbalancer_id

    @loadbalancer_id.setter
    def loadbalancer_id(self, loadbalancer_id):
        """Sets the loadbalancer_id of this ListLogtanksRequest.

        负载均衡器ID。 支持多值查询，查询条件格式：loadbalancer_id=xxx&loadbalancer_id=xxx。

        :param loadbalancer_id: The loadbalancer_id of this ListLogtanksRequest.
        :type loadbalancer_id: list[str]
        """
        self._loadbalancer_id = loadbalancer_id

    @property
    def log_group_id(self):
        """Gets the log_group_id of this ListLogtanksRequest.

        云日志分组ID。 支持多值查询，查询条件格式：log_group_id=xxx&log_group_id=xxx。

        :return: The log_group_id of this ListLogtanksRequest.
        :rtype: list[str]
        """
        return self._log_group_id

    @log_group_id.setter
    def log_group_id(self, log_group_id):
        """Sets the log_group_id of this ListLogtanksRequest.

        云日志分组ID。 支持多值查询，查询条件格式：log_group_id=xxx&log_group_id=xxx。

        :param log_group_id: The log_group_id of this ListLogtanksRequest.
        :type log_group_id: list[str]
        """
        self._log_group_id = log_group_id

    @property
    def log_topic_id(self):
        """Gets the log_topic_id of this ListLogtanksRequest.

        云日志主题ID 支持多值查询，查询条件格式：log_topic_id=xxx&log_topic_id=xxx。

        :return: The log_topic_id of this ListLogtanksRequest.
        :rtype: list[str]
        """
        return self._log_topic_id

    @log_topic_id.setter
    def log_topic_id(self, log_topic_id):
        """Sets the log_topic_id of this ListLogtanksRequest.

        云日志主题ID 支持多值查询，查询条件格式：log_topic_id=xxx&log_topic_id=xxx。

        :param log_topic_id: The log_topic_id of this ListLogtanksRequest.
        :type log_topic_id: list[str]
        """
        self._log_topic_id = log_topic_id

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
        if not isinstance(other, ListLogtanksRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
