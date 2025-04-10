# coding: utf-8

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
        'endpoint': 'str',
        'fuzzy_remark': 'str'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'protocol': 'protocol',
        'status': 'status',
        'endpoint': 'endpoint',
        'fuzzy_remark': 'fuzzy_remark'
    }

    def __init__(self, offset=None, limit=None, protocol=None, status=None, endpoint=None, fuzzy_remark=None):
        r"""ListSubscriptionsRequest

        The model defined in huaweicloud sdk

        :param offset: 偏移量。  偏移量为一个大于0小于资源总个数的整数，表示查询该偏移量后面的所有的资源，默认值为0。
        :type offset: int
        :param limit:  查询数量限制。  取值范围：1~100，取值一般为10，20，50。功能说明：每页返回的资源个数。默认值为100。
        :type limit: int
        :param protocol: 协议名称， 枚举值：http、https、sms、email、functionstage。
        :type protocol: str
        :param status: 状态。 0：未确认 1：已确认 2：不需要确认 3：已取消确认 4：已经删除。
        :type status: int
        :param endpoint: 订阅终端。
        :type endpoint: str
        :param fuzzy_remark: 检索的订阅备注字段，模糊匹配。最大长度限制为128个字节。
        :type fuzzy_remark: str
        """
        
        

        self._offset = None
        self._limit = None
        self._protocol = None
        self._status = None
        self._endpoint = None
        self._fuzzy_remark = None
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
        if fuzzy_remark is not None:
            self.fuzzy_remark = fuzzy_remark

    @property
    def offset(self):
        r"""Gets the offset of this ListSubscriptionsRequest.

        偏移量。  偏移量为一个大于0小于资源总个数的整数，表示查询该偏移量后面的所有的资源，默认值为0。

        :return: The offset of this ListSubscriptionsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListSubscriptionsRequest.

        偏移量。  偏移量为一个大于0小于资源总个数的整数，表示查询该偏移量后面的所有的资源，默认值为0。

        :param offset: The offset of this ListSubscriptionsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListSubscriptionsRequest.

         查询数量限制。  取值范围：1~100，取值一般为10，20，50。功能说明：每页返回的资源个数。默认值为100。

        :return: The limit of this ListSubscriptionsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListSubscriptionsRequest.

         查询数量限制。  取值范围：1~100，取值一般为10，20，50。功能说明：每页返回的资源个数。默认值为100。

        :param limit: The limit of this ListSubscriptionsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def protocol(self):
        r"""Gets the protocol of this ListSubscriptionsRequest.

        协议名称， 枚举值：http、https、sms、email、functionstage。

        :return: The protocol of this ListSubscriptionsRequest.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        r"""Sets the protocol of this ListSubscriptionsRequest.

        协议名称， 枚举值：http、https、sms、email、functionstage。

        :param protocol: The protocol of this ListSubscriptionsRequest.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def status(self):
        r"""Gets the status of this ListSubscriptionsRequest.

        状态。 0：未确认 1：已确认 2：不需要确认 3：已取消确认 4：已经删除。

        :return: The status of this ListSubscriptionsRequest.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListSubscriptionsRequest.

        状态。 0：未确认 1：已确认 2：不需要确认 3：已取消确认 4：已经删除。

        :param status: The status of this ListSubscriptionsRequest.
        :type status: int
        """
        self._status = status

    @property
    def endpoint(self):
        r"""Gets the endpoint of this ListSubscriptionsRequest.

        订阅终端。

        :return: The endpoint of this ListSubscriptionsRequest.
        :rtype: str
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint):
        r"""Sets the endpoint of this ListSubscriptionsRequest.

        订阅终端。

        :param endpoint: The endpoint of this ListSubscriptionsRequest.
        :type endpoint: str
        """
        self._endpoint = endpoint

    @property
    def fuzzy_remark(self):
        r"""Gets the fuzzy_remark of this ListSubscriptionsRequest.

        检索的订阅备注字段，模糊匹配。最大长度限制为128个字节。

        :return: The fuzzy_remark of this ListSubscriptionsRequest.
        :rtype: str
        """
        return self._fuzzy_remark

    @fuzzy_remark.setter
    def fuzzy_remark(self, fuzzy_remark):
        r"""Sets the fuzzy_remark of this ListSubscriptionsRequest.

        检索的订阅备注字段，模糊匹配。最大长度限制为128个字节。

        :param fuzzy_remark: The fuzzy_remark of this ListSubscriptionsRequest.
        :type fuzzy_remark: str
        """
        self._fuzzy_remark = fuzzy_remark

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
