# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListActiveOrHistoryAlarmsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain_id': 'str',
        'type': 'str',
        'marker': 'str',
        'limit': 'int',
        'body': 'ListActiveOrHistoryAlarmsRequestBody'
    }

    attribute_map = {
        'domain_id': 'domain_id',
        'type': 'type',
        'marker': 'marker',
        'limit': 'limit',
        'body': 'body'
    }

    def __init__(self, domain_id=None, type=None, marker=None, limit=None, body=None):
        r"""ListActiveOrHistoryAlarmsRequest

        The model defined in huaweicloud sdk

        :param domain_id: domainId
        :type domain_id: str
        :param type: 是活动告警还是历史告警
        :type type: str
        :param marker: 取值为上一页数据的最后一条记录的id(填写上一页数据返回得previous_marker或者next_marker值。)
        :type marker: str
        :param limit: 每页数据量
        :type limit: int
        :param body: Body of the ListActiveOrHistoryAlarmsRequest
        :type body: :class:`huaweicloudsdklts.v2.ListActiveOrHistoryAlarmsRequestBody`
        """
        
        

        self._domain_id = None
        self._type = None
        self._marker = None
        self._limit = None
        self._body = None
        self.discriminator = None

        self.domain_id = domain_id
        self.type = type
        if marker is not None:
            self.marker = marker
        if limit is not None:
            self.limit = limit
        if body is not None:
            self.body = body

    @property
    def domain_id(self):
        r"""Gets the domain_id of this ListActiveOrHistoryAlarmsRequest.

        domainId

        :return: The domain_id of this ListActiveOrHistoryAlarmsRequest.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this ListActiveOrHistoryAlarmsRequest.

        domainId

        :param domain_id: The domain_id of this ListActiveOrHistoryAlarmsRequest.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def type(self):
        r"""Gets the type of this ListActiveOrHistoryAlarmsRequest.

        是活动告警还是历史告警

        :return: The type of this ListActiveOrHistoryAlarmsRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListActiveOrHistoryAlarmsRequest.

        是活动告警还是历史告警

        :param type: The type of this ListActiveOrHistoryAlarmsRequest.
        :type type: str
        """
        self._type = type

    @property
    def marker(self):
        r"""Gets the marker of this ListActiveOrHistoryAlarmsRequest.

        取值为上一页数据的最后一条记录的id(填写上一页数据返回得previous_marker或者next_marker值。)

        :return: The marker of this ListActiveOrHistoryAlarmsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListActiveOrHistoryAlarmsRequest.

        取值为上一页数据的最后一条记录的id(填写上一页数据返回得previous_marker或者next_marker值。)

        :param marker: The marker of this ListActiveOrHistoryAlarmsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def limit(self):
        r"""Gets the limit of this ListActiveOrHistoryAlarmsRequest.

        每页数据量

        :return: The limit of this ListActiveOrHistoryAlarmsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListActiveOrHistoryAlarmsRequest.

        每页数据量

        :param limit: The limit of this ListActiveOrHistoryAlarmsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def body(self):
        r"""Gets the body of this ListActiveOrHistoryAlarmsRequest.

        :return: The body of this ListActiveOrHistoryAlarmsRequest.
        :rtype: :class:`huaweicloudsdklts.v2.ListActiveOrHistoryAlarmsRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this ListActiveOrHistoryAlarmsRequest.

        :param body: The body of this ListActiveOrHistoryAlarmsRequest.
        :type body: :class:`huaweicloudsdklts.v2.ListActiveOrHistoryAlarmsRequestBody`
        """
        self._body = body

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
        if not isinstance(other, ListActiveOrHistoryAlarmsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
