# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListBcsEventsStatisticRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'blockchain_id': 'str',
        'type': 'str',
        'body': 'ListBcsEventRequestBody'
    }

    attribute_map = {
        'blockchain_id': 'blockchain_id',
        'type': 'type',
        'body': 'body'
    }

    def __init__(self, blockchain_id=None, type=None, body=None):
        """ListBcsEventsStatisticRequest

        The model defined in huaweicloud sdk

        :param blockchain_id: 区块链服务id
        :type blockchain_id: str
        :param type: 查询类型。type&#x3D;active_alert代表查询活动告警，type&#x3D;history_alert代表查询历史告警。不传或者传其他值则返回指定查询条件的所有信息
        :type type: str
        :param body: Body of the ListBcsEventsStatisticRequest
        :type body: :class:`huaweicloudsdkbcs.v2.ListBcsEventRequestBody`
        """
        
        

        self._blockchain_id = None
        self._type = None
        self._body = None
        self.discriminator = None

        self.blockchain_id = blockchain_id
        if type is not None:
            self.type = type
        if body is not None:
            self.body = body

    @property
    def blockchain_id(self):
        """Gets the blockchain_id of this ListBcsEventsStatisticRequest.

        区块链服务id

        :return: The blockchain_id of this ListBcsEventsStatisticRequest.
        :rtype: str
        """
        return self._blockchain_id

    @blockchain_id.setter
    def blockchain_id(self, blockchain_id):
        """Sets the blockchain_id of this ListBcsEventsStatisticRequest.

        区块链服务id

        :param blockchain_id: The blockchain_id of this ListBcsEventsStatisticRequest.
        :type blockchain_id: str
        """
        self._blockchain_id = blockchain_id

    @property
    def type(self):
        """Gets the type of this ListBcsEventsStatisticRequest.

        查询类型。type=active_alert代表查询活动告警，type=history_alert代表查询历史告警。不传或者传其他值则返回指定查询条件的所有信息

        :return: The type of this ListBcsEventsStatisticRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListBcsEventsStatisticRequest.

        查询类型。type=active_alert代表查询活动告警，type=history_alert代表查询历史告警。不传或者传其他值则返回指定查询条件的所有信息

        :param type: The type of this ListBcsEventsStatisticRequest.
        :type type: str
        """
        self._type = type

    @property
    def body(self):
        """Gets the body of this ListBcsEventsStatisticRequest.

        :return: The body of this ListBcsEventsStatisticRequest.
        :rtype: :class:`huaweicloudsdkbcs.v2.ListBcsEventRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this ListBcsEventsStatisticRequest.

        :param body: The body of this ListBcsEventsStatisticRequest.
        :type body: :class:`huaweicloudsdkbcs.v2.ListBcsEventRequestBody`
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
        if not isinstance(other, ListBcsEventsStatisticRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
