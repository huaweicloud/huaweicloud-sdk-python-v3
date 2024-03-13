# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFactoryTaskOverviewRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workspace': 'str',
        'is_own': 'str',
        'query_days': 'str'
    }

    attribute_map = {
        'workspace': 'workspace',
        'is_own': 'is_own',
        'query_days': 'query_days'
    }

    def __init__(self, workspace=None, is_own=None, query_days=None):
        """ListFactoryTaskOverviewRequest

        The model defined in huaweicloud sdk

        :param workspace: 工作空间ID
        :type workspace: str
        :param is_own: 是否查询当前用户的实例，默认为false，表示查询全部用户实例，为true时，表示查询当前用户的实例。
        :type is_own: str
        :param query_days: 查询的天数，取值范围为：today、yesterday、before_yesterday、all，默认为today，表示查询今天的数据，支持查询近7天的数据。 today：查询当天的实例状态数量， yesterday：查询昨天的实例状态数量， before_yesterday：查询前天的实例状态数量， all：查询7天前到当天的实例状态总量。
        :type query_days: str
        """
        
        

        self._workspace = None
        self._is_own = None
        self._query_days = None
        self.discriminator = None

        if workspace is not None:
            self.workspace = workspace
        if is_own is not None:
            self.is_own = is_own
        if query_days is not None:
            self.query_days = query_days

    @property
    def workspace(self):
        """Gets the workspace of this ListFactoryTaskOverviewRequest.

        工作空间ID

        :return: The workspace of this ListFactoryTaskOverviewRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        """Sets the workspace of this ListFactoryTaskOverviewRequest.

        工作空间ID

        :param workspace: The workspace of this ListFactoryTaskOverviewRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def is_own(self):
        """Gets the is_own of this ListFactoryTaskOverviewRequest.

        是否查询当前用户的实例，默认为false，表示查询全部用户实例，为true时，表示查询当前用户的实例。

        :return: The is_own of this ListFactoryTaskOverviewRequest.
        :rtype: str
        """
        return self._is_own

    @is_own.setter
    def is_own(self, is_own):
        """Sets the is_own of this ListFactoryTaskOverviewRequest.

        是否查询当前用户的实例，默认为false，表示查询全部用户实例，为true时，表示查询当前用户的实例。

        :param is_own: The is_own of this ListFactoryTaskOverviewRequest.
        :type is_own: str
        """
        self._is_own = is_own

    @property
    def query_days(self):
        """Gets the query_days of this ListFactoryTaskOverviewRequest.

        查询的天数，取值范围为：today、yesterday、before_yesterday、all，默认为today，表示查询今天的数据，支持查询近7天的数据。 today：查询当天的实例状态数量， yesterday：查询昨天的实例状态数量， before_yesterday：查询前天的实例状态数量， all：查询7天前到当天的实例状态总量。

        :return: The query_days of this ListFactoryTaskOverviewRequest.
        :rtype: str
        """
        return self._query_days

    @query_days.setter
    def query_days(self, query_days):
        """Sets the query_days of this ListFactoryTaskOverviewRequest.

        查询的天数，取值范围为：today、yesterday、before_yesterday、all，默认为today，表示查询今天的数据，支持查询近7天的数据。 today：查询当天的实例状态数量， yesterday：查询昨天的实例状态数量， before_yesterday：查询前天的实例状态数量， all：查询7天前到当天的实例状态总量。

        :param query_days: The query_days of this ListFactoryTaskOverviewRequest.
        :type query_days: str
        """
        self._query_days = query_days

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
        if not isinstance(other, ListFactoryTaskOverviewRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
