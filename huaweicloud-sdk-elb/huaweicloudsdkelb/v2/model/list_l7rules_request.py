# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListL7rulesRequest:

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
        'l7policy_id': 'str',
        'id': 'str',
        'admin_state_up': 'bool',
        'type': 'str',
        'compare_type': 'str',
        'invert': 'bool',
        'key': 'str',
        'value': 'str',
        'provisioning_status': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'marker': 'marker',
        'page_reverse': 'page_reverse',
        'l7policy_id': 'l7policy_id',
        'id': 'id',
        'admin_state_up': 'admin_state_up',
        'type': 'type',
        'compare_type': 'compare_type',
        'invert': 'invert',
        'key': 'key',
        'value': 'value',
        'provisioning_status': 'provisioning_status'
    }

    def __init__(self, limit=None, marker=None, page_reverse=None, l7policy_id=None, id=None, admin_state_up=None, type=None, compare_type=None, invert=None, key=None, value=None, provisioning_status=None):
        r"""ListL7rulesRequest

        The model defined in huaweicloud sdk

        :param limit: 分页查询中每页的转发规则个数
        :type limit: int
        :param marker: 分页查询的起始的资源id，表示上一页最后一条查询记录的转发规则的id。不指定时表示查询第一页。
        :type marker: str
        :param page_reverse: 分页的顺序，true表示从后往前分页，false表示从前往后分页，默认为false。
        :type page_reverse: bool
        :param l7policy_id: 转发策略id
        :type l7policy_id: str
        :param id: 转发规则ID。
        :type id: str
        :param admin_state_up: 转发规则的管理状态；取值范围： true/false。该字段为预留字段，暂未启用。默认为true。
        :type admin_state_up: bool
        :param type: 转发规则的匹配类型。取值范围：HOST_NAME：匹配请求中的域名；PATH：匹配请求中的路径；同一个转发策略下转发规则的type不能重复。
        :type type: str
        :param compare_type: 转发匹配方式： type为HOST_NAME时，取值范围：EQUAL_TO：精确匹配； type为PATH时，取值范围：REGEX：正则匹配；STARTS_WITH：前缀匹配；EQUAL_TO：精确匹配。
        :type compare_type: str
        :param invert: 是否反向匹配；取值范围：true/false。默认值：false；该字段为预留字段，暂未启用。
        :type invert: bool
        :param key: 匹配内容的键值。默认为null。该字段为预留字段，暂未启用。
        :type key: str
        :param value: 匹配内容的值。 当type为HOST_NAME时，取值范围：String (100)，字符串只能包含英文字母、数字、“-”或“.”，且必须以字母或数字开头。 当type为PATH时，取值范围：String (128)。当转发规则的compare_type为STARTS_WITH、EQUAL_TO时，字符串只能包含英文字母、数字、_~&#39;;@^-%#&amp;$.*+?,&#x3D;!:| /()[]{}，且必须以\&quot;/\&quot;开头。
        :type value: str
        :param provisioning_status: 转发规则的配置状态，可以为ACTIVE、PENDING_CREATE 或者ERROR。默认值：ACTIVE；该字段为预留字段，暂未启用。
        :type provisioning_status: str
        """
        
        

        self._limit = None
        self._marker = None
        self._page_reverse = None
        self._l7policy_id = None
        self._id = None
        self._admin_state_up = None
        self._type = None
        self._compare_type = None
        self._invert = None
        self._key = None
        self._value = None
        self._provisioning_status = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if page_reverse is not None:
            self.page_reverse = page_reverse
        self.l7policy_id = l7policy_id
        if id is not None:
            self.id = id
        if admin_state_up is not None:
            self.admin_state_up = admin_state_up
        if type is not None:
            self.type = type
        if compare_type is not None:
            self.compare_type = compare_type
        if invert is not None:
            self.invert = invert
        if key is not None:
            self.key = key
        if value is not None:
            self.value = value
        if provisioning_status is not None:
            self.provisioning_status = provisioning_status

    @property
    def limit(self):
        r"""Gets the limit of this ListL7rulesRequest.

        分页查询中每页的转发规则个数

        :return: The limit of this ListL7rulesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListL7rulesRequest.

        分页查询中每页的转发规则个数

        :param limit: The limit of this ListL7rulesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ListL7rulesRequest.

        分页查询的起始的资源id，表示上一页最后一条查询记录的转发规则的id。不指定时表示查询第一页。

        :return: The marker of this ListL7rulesRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListL7rulesRequest.

        分页查询的起始的资源id，表示上一页最后一条查询记录的转发规则的id。不指定时表示查询第一页。

        :param marker: The marker of this ListL7rulesRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def page_reverse(self):
        r"""Gets the page_reverse of this ListL7rulesRequest.

        分页的顺序，true表示从后往前分页，false表示从前往后分页，默认为false。

        :return: The page_reverse of this ListL7rulesRequest.
        :rtype: bool
        """
        return self._page_reverse

    @page_reverse.setter
    def page_reverse(self, page_reverse):
        r"""Sets the page_reverse of this ListL7rulesRequest.

        分页的顺序，true表示从后往前分页，false表示从前往后分页，默认为false。

        :param page_reverse: The page_reverse of this ListL7rulesRequest.
        :type page_reverse: bool
        """
        self._page_reverse = page_reverse

    @property
    def l7policy_id(self):
        r"""Gets the l7policy_id of this ListL7rulesRequest.

        转发策略id

        :return: The l7policy_id of this ListL7rulesRequest.
        :rtype: str
        """
        return self._l7policy_id

    @l7policy_id.setter
    def l7policy_id(self, l7policy_id):
        r"""Sets the l7policy_id of this ListL7rulesRequest.

        转发策略id

        :param l7policy_id: The l7policy_id of this ListL7rulesRequest.
        :type l7policy_id: str
        """
        self._l7policy_id = l7policy_id

    @property
    def id(self):
        r"""Gets the id of this ListL7rulesRequest.

        转发规则ID。

        :return: The id of this ListL7rulesRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListL7rulesRequest.

        转发规则ID。

        :param id: The id of this ListL7rulesRequest.
        :type id: str
        """
        self._id = id

    @property
    def admin_state_up(self):
        r"""Gets the admin_state_up of this ListL7rulesRequest.

        转发规则的管理状态；取值范围： true/false。该字段为预留字段，暂未启用。默认为true。

        :return: The admin_state_up of this ListL7rulesRequest.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        r"""Sets the admin_state_up of this ListL7rulesRequest.

        转发规则的管理状态；取值范围： true/false。该字段为预留字段，暂未启用。默认为true。

        :param admin_state_up: The admin_state_up of this ListL7rulesRequest.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def type(self):
        r"""Gets the type of this ListL7rulesRequest.

        转发规则的匹配类型。取值范围：HOST_NAME：匹配请求中的域名；PATH：匹配请求中的路径；同一个转发策略下转发规则的type不能重复。

        :return: The type of this ListL7rulesRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListL7rulesRequest.

        转发规则的匹配类型。取值范围：HOST_NAME：匹配请求中的域名；PATH：匹配请求中的路径；同一个转发策略下转发规则的type不能重复。

        :param type: The type of this ListL7rulesRequest.
        :type type: str
        """
        self._type = type

    @property
    def compare_type(self):
        r"""Gets the compare_type of this ListL7rulesRequest.

        转发匹配方式： type为HOST_NAME时，取值范围：EQUAL_TO：精确匹配； type为PATH时，取值范围：REGEX：正则匹配；STARTS_WITH：前缀匹配；EQUAL_TO：精确匹配。

        :return: The compare_type of this ListL7rulesRequest.
        :rtype: str
        """
        return self._compare_type

    @compare_type.setter
    def compare_type(self, compare_type):
        r"""Sets the compare_type of this ListL7rulesRequest.

        转发匹配方式： type为HOST_NAME时，取值范围：EQUAL_TO：精确匹配； type为PATH时，取值范围：REGEX：正则匹配；STARTS_WITH：前缀匹配；EQUAL_TO：精确匹配。

        :param compare_type: The compare_type of this ListL7rulesRequest.
        :type compare_type: str
        """
        self._compare_type = compare_type

    @property
    def invert(self):
        r"""Gets the invert of this ListL7rulesRequest.

        是否反向匹配；取值范围：true/false。默认值：false；该字段为预留字段，暂未启用。

        :return: The invert of this ListL7rulesRequest.
        :rtype: bool
        """
        return self._invert

    @invert.setter
    def invert(self, invert):
        r"""Sets the invert of this ListL7rulesRequest.

        是否反向匹配；取值范围：true/false。默认值：false；该字段为预留字段，暂未启用。

        :param invert: The invert of this ListL7rulesRequest.
        :type invert: bool
        """
        self._invert = invert

    @property
    def key(self):
        r"""Gets the key of this ListL7rulesRequest.

        匹配内容的键值。默认为null。该字段为预留字段，暂未启用。

        :return: The key of this ListL7rulesRequest.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        r"""Sets the key of this ListL7rulesRequest.

        匹配内容的键值。默认为null。该字段为预留字段，暂未启用。

        :param key: The key of this ListL7rulesRequest.
        :type key: str
        """
        self._key = key

    @property
    def value(self):
        r"""Gets the value of this ListL7rulesRequest.

        匹配内容的值。 当type为HOST_NAME时，取值范围：String (100)，字符串只能包含英文字母、数字、“-”或“.”，且必须以字母或数字开头。 当type为PATH时，取值范围：String (128)。当转发规则的compare_type为STARTS_WITH、EQUAL_TO时，字符串只能包含英文字母、数字、_~';@^-%#&$.*+?,=!:| /()[]{}，且必须以\"/\"开头。

        :return: The value of this ListL7rulesRequest.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this ListL7rulesRequest.

        匹配内容的值。 当type为HOST_NAME时，取值范围：String (100)，字符串只能包含英文字母、数字、“-”或“.”，且必须以字母或数字开头。 当type为PATH时，取值范围：String (128)。当转发规则的compare_type为STARTS_WITH、EQUAL_TO时，字符串只能包含英文字母、数字、_~';@^-%#&$.*+?,=!:| /()[]{}，且必须以\"/\"开头。

        :param value: The value of this ListL7rulesRequest.
        :type value: str
        """
        self._value = value

    @property
    def provisioning_status(self):
        r"""Gets the provisioning_status of this ListL7rulesRequest.

        转发规则的配置状态，可以为ACTIVE、PENDING_CREATE 或者ERROR。默认值：ACTIVE；该字段为预留字段，暂未启用。

        :return: The provisioning_status of this ListL7rulesRequest.
        :rtype: str
        """
        return self._provisioning_status

    @provisioning_status.setter
    def provisioning_status(self, provisioning_status):
        r"""Sets the provisioning_status of this ListL7rulesRequest.

        转发规则的配置状态，可以为ACTIVE、PENDING_CREATE 或者ERROR。默认值：ACTIVE；该字段为预留字段，暂未启用。

        :param provisioning_status: The provisioning_status of this ListL7rulesRequest.
        :type provisioning_status: str
        """
        self._provisioning_status = provisioning_status

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
        if not isinstance(other, ListL7rulesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
