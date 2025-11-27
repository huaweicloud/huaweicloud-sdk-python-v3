# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListReplicationErrorsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'subscription_id': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'subscription_id': 'subscription_id',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, instance_id=None, subscription_id=None, offset=None, limit=None):
        r"""ListReplicationErrorsRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID。
        :type instance_id: str
        :param subscription_id: 订阅id。 若该参数为空，则查询当前实例作为分发服务器时，分发下的所有报错信息。 若该参数不为空，则查询该订阅的所有报错信息。
        :type subscription_id: str
        :param offset: 索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。
        :type offset: int
        :param limit: 查询记录数。默认为10，不能为负数，最小值为1，最大值为100。
        :type limit: int
        """
        
        

        self._instance_id = None
        self._subscription_id = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.instance_id = instance_id
        if subscription_id is not None:
            self.subscription_id = subscription_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListReplicationErrorsRequest.

        实例ID。

        :return: The instance_id of this ListReplicationErrorsRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListReplicationErrorsRequest.

        实例ID。

        :param instance_id: The instance_id of this ListReplicationErrorsRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def subscription_id(self):
        r"""Gets the subscription_id of this ListReplicationErrorsRequest.

        订阅id。 若该参数为空，则查询当前实例作为分发服务器时，分发下的所有报错信息。 若该参数不为空，则查询该订阅的所有报错信息。

        :return: The subscription_id of this ListReplicationErrorsRequest.
        :rtype: str
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        r"""Sets the subscription_id of this ListReplicationErrorsRequest.

        订阅id。 若该参数为空，则查询当前实例作为分发服务器时，分发下的所有报错信息。 若该参数不为空，则查询该订阅的所有报错信息。

        :param subscription_id: The subscription_id of this ListReplicationErrorsRequest.
        :type subscription_id: str
        """
        self._subscription_id = subscription_id

    @property
    def offset(self):
        r"""Gets the offset of this ListReplicationErrorsRequest.

        索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。

        :return: The offset of this ListReplicationErrorsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListReplicationErrorsRequest.

        索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。

        :param offset: The offset of this ListReplicationErrorsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListReplicationErrorsRequest.

        查询记录数。默认为10，不能为负数，最小值为1，最大值为100。

        :return: The limit of this ListReplicationErrorsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListReplicationErrorsRequest.

        查询记录数。默认为10，不能为负数，最小值为1，最大值为100。

        :param limit: The limit of this ListReplicationErrorsRequest.
        :type limit: int
        """
        self._limit = limit

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListReplicationErrorsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
