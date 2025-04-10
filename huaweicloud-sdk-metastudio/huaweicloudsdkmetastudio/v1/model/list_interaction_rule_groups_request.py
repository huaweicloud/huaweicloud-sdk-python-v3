# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInteractionRuleGroupsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_app_user_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'create_since': 'str',
        'create_until': 'str',
        'group_name': 'str'
    }

    attribute_map = {
        'x_app_user_id': 'X-App-UserId',
        'offset': 'offset',
        'limit': 'limit',
        'create_since': 'create_since',
        'create_until': 'create_until',
        'group_name': 'group_name'
    }

    def __init__(self, x_app_user_id=None, offset=None, limit=None, create_since=None, create_until=None, group_name=None):
        r"""ListInteractionRuleGroupsRequest

        The model defined in huaweicloud sdk

        :param x_app_user_id: 第三方用户ID。不允许输入中文。
        :type x_app_user_id: str
        :param offset: 偏移量，表示从此偏移量开始查询。
        :type offset: int
        :param limit: 每页显示的条目数量。
        :type limit: int
        :param create_since: 过滤创建时间&gt;&#x3D;输入时间的记录。
        :type create_since: str
        :param create_until: 过滤创建时间&lt;&#x3D;输入时间的记录。
        :type create_until: str
        :param group_name: 规则库名称
        :type group_name: str
        """
        
        

        self._x_app_user_id = None
        self._offset = None
        self._limit = None
        self._create_since = None
        self._create_until = None
        self._group_name = None
        self.discriminator = None

        if x_app_user_id is not None:
            self.x_app_user_id = x_app_user_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if create_since is not None:
            self.create_since = create_since
        if create_until is not None:
            self.create_until = create_until
        if group_name is not None:
            self.group_name = group_name

    @property
    def x_app_user_id(self):
        r"""Gets the x_app_user_id of this ListInteractionRuleGroupsRequest.

        第三方用户ID。不允许输入中文。

        :return: The x_app_user_id of this ListInteractionRuleGroupsRequest.
        :rtype: str
        """
        return self._x_app_user_id

    @x_app_user_id.setter
    def x_app_user_id(self, x_app_user_id):
        r"""Sets the x_app_user_id of this ListInteractionRuleGroupsRequest.

        第三方用户ID。不允许输入中文。

        :param x_app_user_id: The x_app_user_id of this ListInteractionRuleGroupsRequest.
        :type x_app_user_id: str
        """
        self._x_app_user_id = x_app_user_id

    @property
    def offset(self):
        r"""Gets the offset of this ListInteractionRuleGroupsRequest.

        偏移量，表示从此偏移量开始查询。

        :return: The offset of this ListInteractionRuleGroupsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListInteractionRuleGroupsRequest.

        偏移量，表示从此偏移量开始查询。

        :param offset: The offset of this ListInteractionRuleGroupsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListInteractionRuleGroupsRequest.

        每页显示的条目数量。

        :return: The limit of this ListInteractionRuleGroupsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListInteractionRuleGroupsRequest.

        每页显示的条目数量。

        :param limit: The limit of this ListInteractionRuleGroupsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def create_since(self):
        r"""Gets the create_since of this ListInteractionRuleGroupsRequest.

        过滤创建时间>=输入时间的记录。

        :return: The create_since of this ListInteractionRuleGroupsRequest.
        :rtype: str
        """
        return self._create_since

    @create_since.setter
    def create_since(self, create_since):
        r"""Sets the create_since of this ListInteractionRuleGroupsRequest.

        过滤创建时间>=输入时间的记录。

        :param create_since: The create_since of this ListInteractionRuleGroupsRequest.
        :type create_since: str
        """
        self._create_since = create_since

    @property
    def create_until(self):
        r"""Gets the create_until of this ListInteractionRuleGroupsRequest.

        过滤创建时间<=输入时间的记录。

        :return: The create_until of this ListInteractionRuleGroupsRequest.
        :rtype: str
        """
        return self._create_until

    @create_until.setter
    def create_until(self, create_until):
        r"""Sets the create_until of this ListInteractionRuleGroupsRequest.

        过滤创建时间<=输入时间的记录。

        :param create_until: The create_until of this ListInteractionRuleGroupsRequest.
        :type create_until: str
        """
        self._create_until = create_until

    @property
    def group_name(self):
        r"""Gets the group_name of this ListInteractionRuleGroupsRequest.

        规则库名称

        :return: The group_name of this ListInteractionRuleGroupsRequest.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        r"""Sets the group_name of this ListInteractionRuleGroupsRequest.

        规则库名称

        :param group_name: The group_name of this ListInteractionRuleGroupsRequest.
        :type group_name: str
        """
        self._group_name = group_name

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
        if not isinstance(other, ListInteractionRuleGroupsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
