# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPubInfosRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'pub_name': 'str',
        'state': 'int',
        'start_time': 'datetime',
        'offset': 'int',
        'limit': 'int',
        'end_time': 'datetime',
        'industry': 'str',
        'approve_state': 'int'
    }

    attribute_map = {
        'pub_name': 'pub_name',
        'state': 'state',
        'start_time': 'start_time',
        'offset': 'offset',
        'limit': 'limit',
        'end_time': 'end_time',
        'industry': 'industry',
        'approve_state': 'approve_state'
    }

    def __init__(self, pub_name=None, state=None, start_time=None, offset=None, limit=None, end_time=None, industry=None, approve_state=None):
        r"""ListPubInfosRequest

        The model defined in huaweicloud sdk

        :param pub_name: 服务号名称。
        :type pub_name: str
        :param state: 服务号状态。  - 1：未生效  - 2：已生效  - 3：已失效  - 4：已冻结 
        :type state: int
        :param start_time: 开始上线时间，格式为：yyyy-MM-ddTHH:mm:ssZ。
        :type start_time: datetime
        :param offset: 偏移量，表示从此偏移量开始查询，offset大于等于0。
        :type offset: int
        :param limit: 每页显示的条目数量。
        :type limit: int
        :param end_time: 结束上线时间，格式为：yyyy-MM-ddTHH:mm:ssZ。
        :type end_time: datetime
        :param industry: 服务号所属行业。 - 1：金融理财 - 2：社交通讯 - 3：影音娱乐 - 4：旅游出行 - 5：购物 - 6：本地生活 - 7：运动健康 - 8：教育培训 - 9：新闻阅读 - 10：运营商  - 11：其他 
        :type industry: str
        :param approve_state: 审核状态。  - 1：审核中 - 2：审核通过 - 3：驳回 
        :type approve_state: int
        """
        
        

        self._pub_name = None
        self._state = None
        self._start_time = None
        self._offset = None
        self._limit = None
        self._end_time = None
        self._industry = None
        self._approve_state = None
        self.discriminator = None

        if pub_name is not None:
            self.pub_name = pub_name
        if state is not None:
            self.state = state
        if start_time is not None:
            self.start_time = start_time
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if end_time is not None:
            self.end_time = end_time
        if industry is not None:
            self.industry = industry
        if approve_state is not None:
            self.approve_state = approve_state

    @property
    def pub_name(self):
        r"""Gets the pub_name of this ListPubInfosRequest.

        服务号名称。

        :return: The pub_name of this ListPubInfosRequest.
        :rtype: str
        """
        return self._pub_name

    @pub_name.setter
    def pub_name(self, pub_name):
        r"""Sets the pub_name of this ListPubInfosRequest.

        服务号名称。

        :param pub_name: The pub_name of this ListPubInfosRequest.
        :type pub_name: str
        """
        self._pub_name = pub_name

    @property
    def state(self):
        r"""Gets the state of this ListPubInfosRequest.

        服务号状态。  - 1：未生效  - 2：已生效  - 3：已失效  - 4：已冻结 

        :return: The state of this ListPubInfosRequest.
        :rtype: int
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this ListPubInfosRequest.

        服务号状态。  - 1：未生效  - 2：已生效  - 3：已失效  - 4：已冻结 

        :param state: The state of this ListPubInfosRequest.
        :type state: int
        """
        self._state = state

    @property
    def start_time(self):
        r"""Gets the start_time of this ListPubInfosRequest.

        开始上线时间，格式为：yyyy-MM-ddTHH:mm:ssZ。

        :return: The start_time of this ListPubInfosRequest.
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListPubInfosRequest.

        开始上线时间，格式为：yyyy-MM-ddTHH:mm:ssZ。

        :param start_time: The start_time of this ListPubInfosRequest.
        :type start_time: datetime
        """
        self._start_time = start_time

    @property
    def offset(self):
        r"""Gets the offset of this ListPubInfosRequest.

        偏移量，表示从此偏移量开始查询，offset大于等于0。

        :return: The offset of this ListPubInfosRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListPubInfosRequest.

        偏移量，表示从此偏移量开始查询，offset大于等于0。

        :param offset: The offset of this ListPubInfosRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListPubInfosRequest.

        每页显示的条目数量。

        :return: The limit of this ListPubInfosRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListPubInfosRequest.

        每页显示的条目数量。

        :param limit: The limit of this ListPubInfosRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def end_time(self):
        r"""Gets the end_time of this ListPubInfosRequest.

        结束上线时间，格式为：yyyy-MM-ddTHH:mm:ssZ。

        :return: The end_time of this ListPubInfosRequest.
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListPubInfosRequest.

        结束上线时间，格式为：yyyy-MM-ddTHH:mm:ssZ。

        :param end_time: The end_time of this ListPubInfosRequest.
        :type end_time: datetime
        """
        self._end_time = end_time

    @property
    def industry(self):
        r"""Gets the industry of this ListPubInfosRequest.

        服务号所属行业。 - 1：金融理财 - 2：社交通讯 - 3：影音娱乐 - 4：旅游出行 - 5：购物 - 6：本地生活 - 7：运动健康 - 8：教育培训 - 9：新闻阅读 - 10：运营商  - 11：其他 

        :return: The industry of this ListPubInfosRequest.
        :rtype: str
        """
        return self._industry

    @industry.setter
    def industry(self, industry):
        r"""Sets the industry of this ListPubInfosRequest.

        服务号所属行业。 - 1：金融理财 - 2：社交通讯 - 3：影音娱乐 - 4：旅游出行 - 5：购物 - 6：本地生活 - 7：运动健康 - 8：教育培训 - 9：新闻阅读 - 10：运营商  - 11：其他 

        :param industry: The industry of this ListPubInfosRequest.
        :type industry: str
        """
        self._industry = industry

    @property
    def approve_state(self):
        r"""Gets the approve_state of this ListPubInfosRequest.

        审核状态。  - 1：审核中 - 2：审核通过 - 3：驳回 

        :return: The approve_state of this ListPubInfosRequest.
        :rtype: int
        """
        return self._approve_state

    @approve_state.setter
    def approve_state(self, approve_state):
        r"""Sets the approve_state of this ListPubInfosRequest.

        审核状态。  - 1：审核中 - 2：审核通过 - 3：驳回 

        :param approve_state: The approve_state of this ListPubInfosRequest.
        :type approve_state: int
        """
        self._approve_state = approve_state

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
        if not isinstance(other, ListPubInfosRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
