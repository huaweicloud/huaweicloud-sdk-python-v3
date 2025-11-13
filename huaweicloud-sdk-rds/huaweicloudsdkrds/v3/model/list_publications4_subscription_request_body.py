# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPublications4SubscriptionRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'publication_instance_id': 'str',
        'publication_instance_name': 'str',
        'publication_name': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'publication_instance_id': 'publication_instance_id',
        'publication_instance_name': 'publication_instance_name',
        'publication_name': 'publication_name',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, publication_instance_id=None, publication_instance_name=None, publication_name=None, offset=None, limit=None):
        r"""ListPublications4SubscriptionRequestBody

        The model defined in huaweicloud sdk

        :param publication_instance_id: 发布实例id。若不为空，优先查该实例下的发布。
        :type publication_instance_id: str
        :param publication_instance_name: 发布实例名称（模糊匹配）。
        :type publication_instance_name: str
        :param publication_name: 发布名称（模糊匹配）。
        :type publication_name: str
        :param offset: 索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。
        :type offset: int
        :param limit: 查询记录数。默认为10，不能为负数，最小值为1，最大值为1000。
        :type limit: int
        """
        
        

        self._publication_instance_id = None
        self._publication_instance_name = None
        self._publication_name = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if publication_instance_id is not None:
            self.publication_instance_id = publication_instance_id
        if publication_instance_name is not None:
            self.publication_instance_name = publication_instance_name
        if publication_name is not None:
            self.publication_name = publication_name
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def publication_instance_id(self):
        r"""Gets the publication_instance_id of this ListPublications4SubscriptionRequestBody.

        发布实例id。若不为空，优先查该实例下的发布。

        :return: The publication_instance_id of this ListPublications4SubscriptionRequestBody.
        :rtype: str
        """
        return self._publication_instance_id

    @publication_instance_id.setter
    def publication_instance_id(self, publication_instance_id):
        r"""Sets the publication_instance_id of this ListPublications4SubscriptionRequestBody.

        发布实例id。若不为空，优先查该实例下的发布。

        :param publication_instance_id: The publication_instance_id of this ListPublications4SubscriptionRequestBody.
        :type publication_instance_id: str
        """
        self._publication_instance_id = publication_instance_id

    @property
    def publication_instance_name(self):
        r"""Gets the publication_instance_name of this ListPublications4SubscriptionRequestBody.

        发布实例名称（模糊匹配）。

        :return: The publication_instance_name of this ListPublications4SubscriptionRequestBody.
        :rtype: str
        """
        return self._publication_instance_name

    @publication_instance_name.setter
    def publication_instance_name(self, publication_instance_name):
        r"""Sets the publication_instance_name of this ListPublications4SubscriptionRequestBody.

        发布实例名称（模糊匹配）。

        :param publication_instance_name: The publication_instance_name of this ListPublications4SubscriptionRequestBody.
        :type publication_instance_name: str
        """
        self._publication_instance_name = publication_instance_name

    @property
    def publication_name(self):
        r"""Gets the publication_name of this ListPublications4SubscriptionRequestBody.

        发布名称（模糊匹配）。

        :return: The publication_name of this ListPublications4SubscriptionRequestBody.
        :rtype: str
        """
        return self._publication_name

    @publication_name.setter
    def publication_name(self, publication_name):
        r"""Sets the publication_name of this ListPublications4SubscriptionRequestBody.

        发布名称（模糊匹配）。

        :param publication_name: The publication_name of this ListPublications4SubscriptionRequestBody.
        :type publication_name: str
        """
        self._publication_name = publication_name

    @property
    def offset(self):
        r"""Gets the offset of this ListPublications4SubscriptionRequestBody.

        索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。

        :return: The offset of this ListPublications4SubscriptionRequestBody.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListPublications4SubscriptionRequestBody.

        索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。

        :param offset: The offset of this ListPublications4SubscriptionRequestBody.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListPublications4SubscriptionRequestBody.

        查询记录数。默认为10，不能为负数，最小值为1，最大值为1000。

        :return: The limit of this ListPublications4SubscriptionRequestBody.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListPublications4SubscriptionRequestBody.

        查询记录数。默认为10，不能为负数，最小值为1，最大值为1000。

        :param limit: The limit of this ListPublications4SubscriptionRequestBody.
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
        if not isinstance(other, ListPublications4SubscriptionRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
