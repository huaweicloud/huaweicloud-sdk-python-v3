# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListStackSetsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'client_request_id': 'str',
        'filter': 'str',
        'sort_key': 'list[str]',
        'sort_dir': 'list[str]',
        'call_identity': 'str',
        'marker': 'str',
        'limit': 'int'
    }

    attribute_map = {
        'client_request_id': 'Client-Request-Id',
        'filter': 'filter',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir',
        'call_identity': 'call_identity',
        'marker': 'marker',
        'limit': 'limit'
    }

    def __init__(self, client_request_id=None, filter=None, sort_key=None, sort_dir=None, call_identity=None, marker=None, limit=None):
        r"""ListStackSetsRequest

        The model defined in huaweicloud sdk

        :param client_request_id: 用户指定的，对于此请求的唯一ID，用于定位某个请求，推荐使用UUID
        :type client_request_id: str
        :param filter: 过滤条件  * 与（AND）运算符使用逗号（，）定义 * 或（OR）运算符使用竖线（|）定义，OR运算符优先级高于AND运算符 * 不支持括号 * 过滤运算符仅支持双等号（&#x3D;&#x3D;） * 过滤参数名及其值仅支持包含大小写英文、数字和下划线 * 过滤条件中禁止使用分号，如果有分号，则此条过滤会被忽略 * 一个过滤参数仅能与一个与条件相关，一个与条件中的多个或条件仅能与一个过滤参数相关
        :type filter: str
        :param sort_key: 排序字段，仅支持给予create_time
        :type sort_key: list[str]
        :param sort_dir: 指定升序还是降序   * &#x60;asc&#x60; - 升序   * &#x60;desc&#x60; - 降序
        :type sort_dir: list[str]
        :param call_identity: 仅支持资源栈集权限模式为SERVICE_MANAGED时指定该参数。用于指定用户是以组织管理账号还是成员账号中的服务委托管理员身份调用资源栈集。默认为SELF。 * 无论指定何种用户身份，创建或部署的资源栈集始终在组织管理账号名下。*   * &#x60;SELF&#x60; - 以组织管理账号身份调用。   * &#x60;DELEGATED_ADMIN&#x60; - 以服务委托管理员身份调用。用户的华为云账号必须在组织中已经被注册为”资源编排资源栈集服务“的委托管理员。
        :type call_identity: str
        :param marker: 分页标记。当一页无法返回所有结果，上一次的请求将返回next_marker以指引还有更多页数，用户可以将next_marker中的值放到此处以查询下一页的信息。此marker只能用于与上一请求指定的相同参数的请求。不指定时默认从第一页开始查询。
        :type marker: str
        :param limit: 每页返回的最多结果数量
        :type limit: int
        """
        
        

        self._client_request_id = None
        self._filter = None
        self._sort_key = None
        self._sort_dir = None
        self._call_identity = None
        self._marker = None
        self._limit = None
        self.discriminator = None

        self.client_request_id = client_request_id
        if filter is not None:
            self.filter = filter
        if sort_key is not None:
            self.sort_key = sort_key
        if sort_dir is not None:
            self.sort_dir = sort_dir
        if call_identity is not None:
            self.call_identity = call_identity
        if marker is not None:
            self.marker = marker
        if limit is not None:
            self.limit = limit

    @property
    def client_request_id(self):
        r"""Gets the client_request_id of this ListStackSetsRequest.

        用户指定的，对于此请求的唯一ID，用于定位某个请求，推荐使用UUID

        :return: The client_request_id of this ListStackSetsRequest.
        :rtype: str
        """
        return self._client_request_id

    @client_request_id.setter
    def client_request_id(self, client_request_id):
        r"""Sets the client_request_id of this ListStackSetsRequest.

        用户指定的，对于此请求的唯一ID，用于定位某个请求，推荐使用UUID

        :param client_request_id: The client_request_id of this ListStackSetsRequest.
        :type client_request_id: str
        """
        self._client_request_id = client_request_id

    @property
    def filter(self):
        r"""Gets the filter of this ListStackSetsRequest.

        过滤条件  * 与（AND）运算符使用逗号（，）定义 * 或（OR）运算符使用竖线（|）定义，OR运算符优先级高于AND运算符 * 不支持括号 * 过滤运算符仅支持双等号（==） * 过滤参数名及其值仅支持包含大小写英文、数字和下划线 * 过滤条件中禁止使用分号，如果有分号，则此条过滤会被忽略 * 一个过滤参数仅能与一个与条件相关，一个与条件中的多个或条件仅能与一个过滤参数相关

        :return: The filter of this ListStackSetsRequest.
        :rtype: str
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        r"""Sets the filter of this ListStackSetsRequest.

        过滤条件  * 与（AND）运算符使用逗号（，）定义 * 或（OR）运算符使用竖线（|）定义，OR运算符优先级高于AND运算符 * 不支持括号 * 过滤运算符仅支持双等号（==） * 过滤参数名及其值仅支持包含大小写英文、数字和下划线 * 过滤条件中禁止使用分号，如果有分号，则此条过滤会被忽略 * 一个过滤参数仅能与一个与条件相关，一个与条件中的多个或条件仅能与一个过滤参数相关

        :param filter: The filter of this ListStackSetsRequest.
        :type filter: str
        """
        self._filter = filter

    @property
    def sort_key(self):
        r"""Gets the sort_key of this ListStackSetsRequest.

        排序字段，仅支持给予create_time

        :return: The sort_key of this ListStackSetsRequest.
        :rtype: list[str]
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        r"""Sets the sort_key of this ListStackSetsRequest.

        排序字段，仅支持给予create_time

        :param sort_key: The sort_key of this ListStackSetsRequest.
        :type sort_key: list[str]
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        r"""Gets the sort_dir of this ListStackSetsRequest.

        指定升序还是降序   * `asc` - 升序   * `desc` - 降序

        :return: The sort_dir of this ListStackSetsRequest.
        :rtype: list[str]
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        r"""Sets the sort_dir of this ListStackSetsRequest.

        指定升序还是降序   * `asc` - 升序   * `desc` - 降序

        :param sort_dir: The sort_dir of this ListStackSetsRequest.
        :type sort_dir: list[str]
        """
        self._sort_dir = sort_dir

    @property
    def call_identity(self):
        r"""Gets the call_identity of this ListStackSetsRequest.

        仅支持资源栈集权限模式为SERVICE_MANAGED时指定该参数。用于指定用户是以组织管理账号还是成员账号中的服务委托管理员身份调用资源栈集。默认为SELF。 * 无论指定何种用户身份，创建或部署的资源栈集始终在组织管理账号名下。*   * `SELF` - 以组织管理账号身份调用。   * `DELEGATED_ADMIN` - 以服务委托管理员身份调用。用户的华为云账号必须在组织中已经被注册为”资源编排资源栈集服务“的委托管理员。

        :return: The call_identity of this ListStackSetsRequest.
        :rtype: str
        """
        return self._call_identity

    @call_identity.setter
    def call_identity(self, call_identity):
        r"""Sets the call_identity of this ListStackSetsRequest.

        仅支持资源栈集权限模式为SERVICE_MANAGED时指定该参数。用于指定用户是以组织管理账号还是成员账号中的服务委托管理员身份调用资源栈集。默认为SELF。 * 无论指定何种用户身份，创建或部署的资源栈集始终在组织管理账号名下。*   * `SELF` - 以组织管理账号身份调用。   * `DELEGATED_ADMIN` - 以服务委托管理员身份调用。用户的华为云账号必须在组织中已经被注册为”资源编排资源栈集服务“的委托管理员。

        :param call_identity: The call_identity of this ListStackSetsRequest.
        :type call_identity: str
        """
        self._call_identity = call_identity

    @property
    def marker(self):
        r"""Gets the marker of this ListStackSetsRequest.

        分页标记。当一页无法返回所有结果，上一次的请求将返回next_marker以指引还有更多页数，用户可以将next_marker中的值放到此处以查询下一页的信息。此marker只能用于与上一请求指定的相同参数的请求。不指定时默认从第一页开始查询。

        :return: The marker of this ListStackSetsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListStackSetsRequest.

        分页标记。当一页无法返回所有结果，上一次的请求将返回next_marker以指引还有更多页数，用户可以将next_marker中的值放到此处以查询下一页的信息。此marker只能用于与上一请求指定的相同参数的请求。不指定时默认从第一页开始查询。

        :param marker: The marker of this ListStackSetsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def limit(self):
        r"""Gets the limit of this ListStackSetsRequest.

        每页返回的最多结果数量

        :return: The limit of this ListStackSetsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListStackSetsRequest.

        每页返回的最多结果数量

        :param limit: The limit of this ListStackSetsRequest.
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
        if not isinstance(other, ListStackSetsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
