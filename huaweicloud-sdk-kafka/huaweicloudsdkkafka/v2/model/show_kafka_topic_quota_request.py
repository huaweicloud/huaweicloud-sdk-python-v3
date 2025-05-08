# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowKafkaTopicQuotaRequest:

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
        'type': 'str',
        'limit': 'str',
        'offset': 'str',
        'keyword': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'type': 'type',
        'limit': 'limit',
        'offset': 'offset',
        'keyword': 'keyword'
    }

    def __init__(self, instance_id=None, type=None, limit=None, offset=None, keyword=None):
        r"""ShowKafkaTopicQuotaRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID。
        :type instance_id: str
        :param type: 查询类型，默认为topic。
        :type type: str
        :param limit: 每一页显示的流控数量。
        :type limit: str
        :param offset: 页数。
        :type offset: str
        :param keyword: 查询关键字。
        :type keyword: str
        """
        
        

        self._instance_id = None
        self._type = None
        self._limit = None
        self._offset = None
        self._keyword = None
        self.discriminator = None

        self.instance_id = instance_id
        if type is not None:
            self.type = type
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if keyword is not None:
            self.keyword = keyword

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ShowKafkaTopicQuotaRequest.

        实例ID。

        :return: The instance_id of this ShowKafkaTopicQuotaRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ShowKafkaTopicQuotaRequest.

        实例ID。

        :param instance_id: The instance_id of this ShowKafkaTopicQuotaRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def type(self):
        r"""Gets the type of this ShowKafkaTopicQuotaRequest.

        查询类型，默认为topic。

        :return: The type of this ShowKafkaTopicQuotaRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ShowKafkaTopicQuotaRequest.

        查询类型，默认为topic。

        :param type: The type of this ShowKafkaTopicQuotaRequest.
        :type type: str
        """
        self._type = type

    @property
    def limit(self):
        r"""Gets the limit of this ShowKafkaTopicQuotaRequest.

        每一页显示的流控数量。

        :return: The limit of this ShowKafkaTopicQuotaRequest.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ShowKafkaTopicQuotaRequest.

        每一页显示的流控数量。

        :param limit: The limit of this ShowKafkaTopicQuotaRequest.
        :type limit: str
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ShowKafkaTopicQuotaRequest.

        页数。

        :return: The offset of this ShowKafkaTopicQuotaRequest.
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ShowKafkaTopicQuotaRequest.

        页数。

        :param offset: The offset of this ShowKafkaTopicQuotaRequest.
        :type offset: str
        """
        self._offset = offset

    @property
    def keyword(self):
        r"""Gets the keyword of this ShowKafkaTopicQuotaRequest.

        查询关键字。

        :return: The keyword of this ShowKafkaTopicQuotaRequest.
        :rtype: str
        """
        return self._keyword

    @keyword.setter
    def keyword(self, keyword):
        r"""Sets the keyword of this ShowKafkaTopicQuotaRequest.

        查询关键字。

        :param keyword: The keyword of this ShowKafkaTopicQuotaRequest.
        :type keyword: str
        """
        self._keyword = keyword

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
        if not isinstance(other, ShowKafkaTopicQuotaRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
