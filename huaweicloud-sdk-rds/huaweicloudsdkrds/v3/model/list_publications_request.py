# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPublicationsRequest:

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
        'publication_name': 'str',
        'publication_db_name': 'str',
        'subscriber_instance_id': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'instance_id': 'instance_id',
        'publication_name': 'publication_name',
        'publication_db_name': 'publication_db_name',
        'subscriber_instance_id': 'subscriber_instance_id',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, x_language=None, instance_id=None, publication_name=None, publication_db_name=None, subscriber_instance_id=None, offset=None, limit=None):
        r"""ListPublicationsRequest

        The model defined in huaweicloud sdk

        :param x_language: 语言。默认en-us。
        :type x_language: str
        :param instance_id: 实例ID
        :type instance_id: str
        :param publication_name: 发布名（模糊匹配）
        :type publication_name: str
        :param publication_db_name: 发布数据库名（模糊匹配）
        :type publication_db_name: str
        :param subscriber_instance_id: 订阅实例id
        :type subscriber_instance_id: str
        :param offset: 索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。
        :type offset: int
        :param limit: 查询记录数。默认为10，不能为负数，最小值为1，最大值为100。
        :type limit: int
        """
        
        

        self._x_language = None
        self._instance_id = None
        self._publication_name = None
        self._publication_db_name = None
        self._subscriber_instance_id = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        self.instance_id = instance_id
        if publication_name is not None:
            self.publication_name = publication_name
        if publication_db_name is not None:
            self.publication_db_name = publication_db_name
        if subscriber_instance_id is not None:
            self.subscriber_instance_id = subscriber_instance_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def x_language(self):
        r"""Gets the x_language of this ListPublicationsRequest.

        语言。默认en-us。

        :return: The x_language of this ListPublicationsRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ListPublicationsRequest.

        语言。默认en-us。

        :param x_language: The x_language of this ListPublicationsRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListPublicationsRequest.

        实例ID

        :return: The instance_id of this ListPublicationsRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListPublicationsRequest.

        实例ID

        :param instance_id: The instance_id of this ListPublicationsRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def publication_name(self):
        r"""Gets the publication_name of this ListPublicationsRequest.

        发布名（模糊匹配）

        :return: The publication_name of this ListPublicationsRequest.
        :rtype: str
        """
        return self._publication_name

    @publication_name.setter
    def publication_name(self, publication_name):
        r"""Sets the publication_name of this ListPublicationsRequest.

        发布名（模糊匹配）

        :param publication_name: The publication_name of this ListPublicationsRequest.
        :type publication_name: str
        """
        self._publication_name = publication_name

    @property
    def publication_db_name(self):
        r"""Gets the publication_db_name of this ListPublicationsRequest.

        发布数据库名（模糊匹配）

        :return: The publication_db_name of this ListPublicationsRequest.
        :rtype: str
        """
        return self._publication_db_name

    @publication_db_name.setter
    def publication_db_name(self, publication_db_name):
        r"""Sets the publication_db_name of this ListPublicationsRequest.

        发布数据库名（模糊匹配）

        :param publication_db_name: The publication_db_name of this ListPublicationsRequest.
        :type publication_db_name: str
        """
        self._publication_db_name = publication_db_name

    @property
    def subscriber_instance_id(self):
        r"""Gets the subscriber_instance_id of this ListPublicationsRequest.

        订阅实例id

        :return: The subscriber_instance_id of this ListPublicationsRequest.
        :rtype: str
        """
        return self._subscriber_instance_id

    @subscriber_instance_id.setter
    def subscriber_instance_id(self, subscriber_instance_id):
        r"""Sets the subscriber_instance_id of this ListPublicationsRequest.

        订阅实例id

        :param subscriber_instance_id: The subscriber_instance_id of this ListPublicationsRequest.
        :type subscriber_instance_id: str
        """
        self._subscriber_instance_id = subscriber_instance_id

    @property
    def offset(self):
        r"""Gets the offset of this ListPublicationsRequest.

        索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。

        :return: The offset of this ListPublicationsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListPublicationsRequest.

        索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。

        :param offset: The offset of this ListPublicationsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListPublicationsRequest.

        查询记录数。默认为10，不能为负数，最小值为1，最大值为100。

        :return: The limit of this ListPublicationsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListPublicationsRequest.

        查询记录数。默认为10，不能为负数，最小值为1，最大值为100。

        :param limit: The limit of this ListPublicationsRequest.
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
        if not isinstance(other, ListPublicationsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
