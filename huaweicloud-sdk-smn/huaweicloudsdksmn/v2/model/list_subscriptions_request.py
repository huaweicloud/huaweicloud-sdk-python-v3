# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSubscriptionsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'offset': 'int',
        'limit': 'int',
        'protocol': 'str',
        'status': 'int',
        'endpoint': 'str'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'protocol': 'protocol',
        'status': 'status',
        'endpoint': 'endpoint'
    }

    def __init__(self, offset=None, limit=None, protocol=None, status=None, endpoint=None):
        """ListSubscriptionsRequest

        The model defined in huaweicloud sdk

        :param offset: 偏移量。  偏移量为一个大于0小于资源总个数的整数，表示查询该偏移量后面的所有的资源，默认值为0。
        :type offset: int
        :param limit:  查询数量限制。  取值范围：1~100，取值一般为10，20，50。功能说明：每页返回的资源个数。默认值为100。
        :type limit: int
        :param protocol: 协议名称， 枚举值：http、https、sms、email、functionstage、dms、application。
        :type protocol: str
        :param status: 状态。 0：未确认 1：已确认 2：不需要确认 3：已取消确认 4：已经删除。
        :type status: int
        :param endpoint: 订阅终端。
        :type endpoint: str
        """
        
        

        self._offset = None
        self._limit = None
        self._protocol = None
        self._status = None
        self._endpoint = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if protocol is not None:
            self.protocol = protocol
        if status is not None:
            self.status = status
        if endpoint is not None:
            self.endpoint = endpoint

    @property
    def offset(self):
        """Gets the offset of this ListSubscriptionsRequest.

        偏移量。  偏移量为一个大于0小于资源总个数的整数，表示查询该偏移量后面的所有的资源，默认值为0。

        :return: The offset of this ListSubscriptionsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListSubscriptionsRequest.

        偏移量。  偏移量为一个大于0小于资源总个数的整数，表示查询该偏移量后面的所有的资源，默认值为0。

        :param offset: The offset of this ListSubscriptionsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListSubscriptionsRequest.

         查询数量限制。  取值范围：1~100，取值一般为10，20，50。功能说明：每页返回的资源个数。默认值为100。

        :return: The limit of this ListSubscriptionsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListSubscriptionsRequest.

         查询数量限制。  取值范围：1~100，取值一般为10，20，50。功能说明：每页返回的资源个数。默认值为100。

        :param limit: The limit of this ListSubscriptionsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def protocol(self):
        """Gets the protocol of this ListSubscriptionsRequest.

        协议名称， 枚举值：http、https、sms、email、functionstage、dms、application。

        :return: The protocol of this ListSubscriptionsRequest.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this ListSubscriptionsRequest.

        协议名称， 枚举值：http、https、sms、email、functionstage、dms、application。

        :param protocol: The protocol of this ListSubscriptionsRequest.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def status(self):
        """Gets the status of this ListSubscriptionsRequest.

        状态。 0：未确认 1：已确认 2：不需要确认 3：已取消确认 4：已经删除。

        :return: The status of this ListSubscriptionsRequest.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListSubscriptionsRequest.

        状态。 0：未确认 1：已确认 2：不需要确认 3：已取消确认 4：已经删除。

        :param status: The status of this ListSubscriptionsRequest.
        :type status: int
        """
        self._status = status

    @property
    def endpoint(self):
        """Gets the endpoint of this ListSubscriptionsRequest.

        订阅终端。

        :return: The endpoint of this ListSubscriptionsRequest.
        :rtype: str
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint):
        """Sets the endpoint of this ListSubscriptionsRequest.

        订阅终端。

        :param endpoint: The endpoint of this ListSubscriptionsRequest.
        :type endpoint: str
        """
        self._endpoint = endpoint

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
        if not isinstance(other, ListSubscriptionsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
