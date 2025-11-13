# coding: utf-8

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
        'x_language': 'str',
        'instance_id': 'str',
        'publication_id': 'str',
        'is_cloud': 'bool',
        'publication_name': 'str',
        'subscription_db_name': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'instance_id': 'instance_id',
        'publication_id': 'publication_id',
        'is_cloud': 'is_cloud',
        'publication_name': 'publication_name',
        'subscription_db_name': 'subscription_db_name',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, x_language=None, instance_id=None, publication_id=None, is_cloud=None, publication_name=None, subscription_db_name=None, offset=None, limit=None):
        r"""ListSubscriptionsRequest

        The model defined in huaweicloud sdk

        :param x_language: 语言。默认en-us。
        :type x_language: str
        :param instance_id: 实例ID
        :type instance_id: str
        :param publication_id: 发布id。不为空则查询该发布下的订阅；为空（null）则查询实例本地订阅。
        :type publication_id: str
        :param is_cloud: 订阅服务器来源  true：订阅服务器为云上实例  false：订阅服务器非云上实例  不传该参数（null）：全部订阅
        :type is_cloud: bool
        :param publication_name: 发布名（模糊匹配）
        :type publication_name: str
        :param subscription_db_name: 订阅数据库名（模糊匹配）
        :type subscription_db_name: str
        :param offset: 索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。
        :type offset: int
        :param limit: 查询记录数。默认为10，不能为负数，最小值为1，最大值为100。
        :type limit: int
        """
        
        

        self._x_language = None
        self._instance_id = None
        self._publication_id = None
        self._is_cloud = None
        self._publication_name = None
        self._subscription_db_name = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        self.instance_id = instance_id
        if publication_id is not None:
            self.publication_id = publication_id
        if is_cloud is not None:
            self.is_cloud = is_cloud
        if publication_name is not None:
            self.publication_name = publication_name
        if subscription_db_name is not None:
            self.subscription_db_name = subscription_db_name
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def x_language(self):
        r"""Gets the x_language of this ListSubscriptionsRequest.

        语言。默认en-us。

        :return: The x_language of this ListSubscriptionsRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ListSubscriptionsRequest.

        语言。默认en-us。

        :param x_language: The x_language of this ListSubscriptionsRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListSubscriptionsRequest.

        实例ID

        :return: The instance_id of this ListSubscriptionsRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListSubscriptionsRequest.

        实例ID

        :param instance_id: The instance_id of this ListSubscriptionsRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def publication_id(self):
        r"""Gets the publication_id of this ListSubscriptionsRequest.

        发布id。不为空则查询该发布下的订阅；为空（null）则查询实例本地订阅。

        :return: The publication_id of this ListSubscriptionsRequest.
        :rtype: str
        """
        return self._publication_id

    @publication_id.setter
    def publication_id(self, publication_id):
        r"""Sets the publication_id of this ListSubscriptionsRequest.

        发布id。不为空则查询该发布下的订阅；为空（null）则查询实例本地订阅。

        :param publication_id: The publication_id of this ListSubscriptionsRequest.
        :type publication_id: str
        """
        self._publication_id = publication_id

    @property
    def is_cloud(self):
        r"""Gets the is_cloud of this ListSubscriptionsRequest.

        订阅服务器来源  true：订阅服务器为云上实例  false：订阅服务器非云上实例  不传该参数（null）：全部订阅

        :return: The is_cloud of this ListSubscriptionsRequest.
        :rtype: bool
        """
        return self._is_cloud

    @is_cloud.setter
    def is_cloud(self, is_cloud):
        r"""Sets the is_cloud of this ListSubscriptionsRequest.

        订阅服务器来源  true：订阅服务器为云上实例  false：订阅服务器非云上实例  不传该参数（null）：全部订阅

        :param is_cloud: The is_cloud of this ListSubscriptionsRequest.
        :type is_cloud: bool
        """
        self._is_cloud = is_cloud

    @property
    def publication_name(self):
        r"""Gets the publication_name of this ListSubscriptionsRequest.

        发布名（模糊匹配）

        :return: The publication_name of this ListSubscriptionsRequest.
        :rtype: str
        """
        return self._publication_name

    @publication_name.setter
    def publication_name(self, publication_name):
        r"""Sets the publication_name of this ListSubscriptionsRequest.

        发布名（模糊匹配）

        :param publication_name: The publication_name of this ListSubscriptionsRequest.
        :type publication_name: str
        """
        self._publication_name = publication_name

    @property
    def subscription_db_name(self):
        r"""Gets the subscription_db_name of this ListSubscriptionsRequest.

        订阅数据库名（模糊匹配）

        :return: The subscription_db_name of this ListSubscriptionsRequest.
        :rtype: str
        """
        return self._subscription_db_name

    @subscription_db_name.setter
    def subscription_db_name(self, subscription_db_name):
        r"""Sets the subscription_db_name of this ListSubscriptionsRequest.

        订阅数据库名（模糊匹配）

        :param subscription_db_name: The subscription_db_name of this ListSubscriptionsRequest.
        :type subscription_db_name: str
        """
        self._subscription_db_name = subscription_db_name

    @property
    def offset(self):
        r"""Gets the offset of this ListSubscriptionsRequest.

        索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。

        :return: The offset of this ListSubscriptionsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListSubscriptionsRequest.

        索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。

        :param offset: The offset of this ListSubscriptionsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListSubscriptionsRequest.

        查询记录数。默认为10，不能为负数，最小值为1，最大值为100。

        :return: The limit of this ListSubscriptionsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListSubscriptionsRequest.

        查询记录数。默认为10，不能为负数，最小值为1，最大值为100。

        :param limit: The limit of this ListSubscriptionsRequest.
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
        if not isinstance(other, ListSubscriptionsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
