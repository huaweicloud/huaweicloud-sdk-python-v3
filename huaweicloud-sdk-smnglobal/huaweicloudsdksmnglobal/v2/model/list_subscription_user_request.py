# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSubscriptionUserRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'protocol': 'str',
        'status': 'str',
        'group': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'name': 'name',
        'protocol': 'protocol',
        'status': 'status',
        'group': 'group',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, name=None, protocol=None, status=None, group=None, offset=None, limit=None):
        r"""ListSubscriptionUserRequest

        The model defined in huaweicloud sdk

        :param name: 订阅用户名称。
        :type name: str
        :param protocol: 协议。 http：HTTP终端 https：HTTPS终端 sms：短信 email：邮件
        :type protocol: str
        :param status: 订阅用户状态。 UNCONFIRMED：未确认 CONFIRMED：已确认 CANCELLED：已取消
        :type status: str
        :param group: 订阅用户分组。
        :type group: str
        :param offset: 偏移量。偏移量为一个大于0小于资源总个数的整数，表示查询该偏移量后面的所有的资源，默认值为0。
        :type offset: int
        :param limit: 查询数量限制。取值范围：1~100，取值一般为10，20，50。功能说明：每页返回的资源个数。默认值为100。
        :type limit: int
        """
        
        

        self._name = None
        self._protocol = None
        self._status = None
        self._group = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if protocol is not None:
            self.protocol = protocol
        if status is not None:
            self.status = status
        if group is not None:
            self.group = group
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def name(self):
        r"""Gets the name of this ListSubscriptionUserRequest.

        订阅用户名称。

        :return: The name of this ListSubscriptionUserRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListSubscriptionUserRequest.

        订阅用户名称。

        :param name: The name of this ListSubscriptionUserRequest.
        :type name: str
        """
        self._name = name

    @property
    def protocol(self):
        r"""Gets the protocol of this ListSubscriptionUserRequest.

        协议。 http：HTTP终端 https：HTTPS终端 sms：短信 email：邮件

        :return: The protocol of this ListSubscriptionUserRequest.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        r"""Sets the protocol of this ListSubscriptionUserRequest.

        协议。 http：HTTP终端 https：HTTPS终端 sms：短信 email：邮件

        :param protocol: The protocol of this ListSubscriptionUserRequest.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def status(self):
        r"""Gets the status of this ListSubscriptionUserRequest.

        订阅用户状态。 UNCONFIRMED：未确认 CONFIRMED：已确认 CANCELLED：已取消

        :return: The status of this ListSubscriptionUserRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListSubscriptionUserRequest.

        订阅用户状态。 UNCONFIRMED：未确认 CONFIRMED：已确认 CANCELLED：已取消

        :param status: The status of this ListSubscriptionUserRequest.
        :type status: str
        """
        self._status = status

    @property
    def group(self):
        r"""Gets the group of this ListSubscriptionUserRequest.

        订阅用户分组。

        :return: The group of this ListSubscriptionUserRequest.
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        r"""Sets the group of this ListSubscriptionUserRequest.

        订阅用户分组。

        :param group: The group of this ListSubscriptionUserRequest.
        :type group: str
        """
        self._group = group

    @property
    def offset(self):
        r"""Gets the offset of this ListSubscriptionUserRequest.

        偏移量。偏移量为一个大于0小于资源总个数的整数，表示查询该偏移量后面的所有的资源，默认值为0。

        :return: The offset of this ListSubscriptionUserRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListSubscriptionUserRequest.

        偏移量。偏移量为一个大于0小于资源总个数的整数，表示查询该偏移量后面的所有的资源，默认值为0。

        :param offset: The offset of this ListSubscriptionUserRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListSubscriptionUserRequest.

        查询数量限制。取值范围：1~100，取值一般为10，20，50。功能说明：每页返回的资源个数。默认值为100。

        :return: The limit of this ListSubscriptionUserRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListSubscriptionUserRequest.

        查询数量限制。取值范围：1~100，取值一般为10，20，50。功能说明：每页返回的资源个数。默认值为100。

        :param limit: The limit of this ListSubscriptionUserRequest.
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
        if not isinstance(other, ListSubscriptionUserRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
