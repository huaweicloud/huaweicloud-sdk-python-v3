# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Shards:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'object_urls': 'list[str]',
        'count': 'int',
        'total': 'int'
    }

    attribute_map = {
        'object_urls': 'object_urls',
        'count': 'count',
        'total': 'total'
    }

    def __init__(self, object_urls=None, count=None, total=None):
        r"""Shards

        The model defined in huaweicloud sdk

        :param object_urls: **参数解释**：日志分片的obs下载链接集。 **取值范围**：不涉及。
        :type object_urls: list[str]
        :param count: **参数解释**：本次请求返回的日志分片数。 **取值范围**：不涉及。
        :type count: int
        :param total: **参数解释**：本次请求命中的日志分片总数。 **取值范围**：不涉及。
        :type total: int
        """
        
        

        self._object_urls = None
        self._count = None
        self._total = None
        self.discriminator = None

        if object_urls is not None:
            self.object_urls = object_urls
        if count is not None:
            self.count = count
        if total is not None:
            self.total = total

    @property
    def object_urls(self):
        r"""Gets the object_urls of this Shards.

        **参数解释**：日志分片的obs下载链接集。 **取值范围**：不涉及。

        :return: The object_urls of this Shards.
        :rtype: list[str]
        """
        return self._object_urls

    @object_urls.setter
    def object_urls(self, object_urls):
        r"""Sets the object_urls of this Shards.

        **参数解释**：日志分片的obs下载链接集。 **取值范围**：不涉及。

        :param object_urls: The object_urls of this Shards.
        :type object_urls: list[str]
        """
        self._object_urls = object_urls

    @property
    def count(self):
        r"""Gets the count of this Shards.

        **参数解释**：本次请求返回的日志分片数。 **取值范围**：不涉及。

        :return: The count of this Shards.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this Shards.

        **参数解释**：本次请求返回的日志分片数。 **取值范围**：不涉及。

        :param count: The count of this Shards.
        :type count: int
        """
        self._count = count

    @property
    def total(self):
        r"""Gets the total of this Shards.

        **参数解释**：本次请求命中的日志分片总数。 **取值范围**：不涉及。

        :return: The total of this Shards.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this Shards.

        **参数解释**：本次请求命中的日志分片总数。 **取值范围**：不涉及。

        :param total: The total of this Shards.
        :type total: int
        """
        self._total = total

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
        if not isinstance(other, Shards):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
