# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEventsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'enterprise_project_id': 'str',
        'limit': 'int',
        'marker': 'str',
        'body': 'EventQueryParam2'
    }

    attribute_map = {
        'type': 'type',
        'enterprise_project_id': 'Enterprise-Project-Id',
        'limit': 'limit',
        'marker': 'marker',
        'body': 'body'
    }

    def __init__(self, type=None, enterprise_project_id=None, limit=None, marker=None, body=None):
        r"""ListEventsRequest

        The model defined in huaweicloud sdk

        :param type: 查询类型。type&#x3D;active_alert代表查询活动告警，type&#x3D;history_alert代表查询历史告警。不传或者传其他值则返回指定查询条件的所有信息。
        :type type: str
        :param enterprise_project_id: 企业项目id。 - 查询单个企业项目下实例，填写企业项目id。 - 查询所有企业项目下实例，填写“all_granted_eps”。
        :type enterprise_project_id: str
        :param limit: 不填默认值为1000
        :type limit: int
        :param marker: 分页标记，初始为0，后续值为返回体中的next_marker
        :type marker: str
        :param body: Body of the ListEventsRequest
        :type body: :class:`huaweicloudsdkaom.v2.EventQueryParam2`
        """
        
        

        self._type = None
        self._enterprise_project_id = None
        self._limit = None
        self._marker = None
        self._body = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if body is not None:
            self.body = body

    @property
    def type(self):
        r"""Gets the type of this ListEventsRequest.

        查询类型。type=active_alert代表查询活动告警，type=history_alert代表查询历史告警。不传或者传其他值则返回指定查询条件的所有信息。

        :return: The type of this ListEventsRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListEventsRequest.

        查询类型。type=active_alert代表查询活动告警，type=history_alert代表查询历史告警。不传或者传其他值则返回指定查询条件的所有信息。

        :param type: The type of this ListEventsRequest.
        :type type: str
        """
        self._type = type

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListEventsRequest.

        企业项目id。 - 查询单个企业项目下实例，填写企业项目id。 - 查询所有企业项目下实例，填写“all_granted_eps”。

        :return: The enterprise_project_id of this ListEventsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListEventsRequest.

        企业项目id。 - 查询单个企业项目下实例，填写企业项目id。 - 查询所有企业项目下实例，填写“all_granted_eps”。

        :param enterprise_project_id: The enterprise_project_id of this ListEventsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def limit(self):
        r"""Gets the limit of this ListEventsRequest.

        不填默认值为1000

        :return: The limit of this ListEventsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListEventsRequest.

        不填默认值为1000

        :param limit: The limit of this ListEventsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ListEventsRequest.

        分页标记，初始为0，后续值为返回体中的next_marker

        :return: The marker of this ListEventsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListEventsRequest.

        分页标记，初始为0，后续值为返回体中的next_marker

        :param marker: The marker of this ListEventsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def body(self):
        r"""Gets the body of this ListEventsRequest.

        :return: The body of this ListEventsRequest.
        :rtype: :class:`huaweicloudsdkaom.v2.EventQueryParam2`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this ListEventsRequest.

        :param body: The body of this ListEventsRequest.
        :type body: :class:`huaweicloudsdkaom.v2.EventQueryParam2`
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
        if not isinstance(other, ListEventsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
