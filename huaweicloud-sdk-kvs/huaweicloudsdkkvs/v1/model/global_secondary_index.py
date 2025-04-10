# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GlobalSecondaryIndex:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'index_name': 'str',
        'shard_key_fields': 'list[Field]',
        'shard_mode': 'str',
        'sort_key_fields': 'list[Field]',
        'abstract_fields': 'list[str]',
        'provisioned_throughput': 'ProvisionedThroughput'
    }

    attribute_map = {
        'index_name': 'index_name',
        'shard_key_fields': 'shard_key_fields',
        'shard_mode': 'shard_mode',
        'sort_key_fields': 'sort_key_fields',
        'abstract_fields': 'abstract_fields',
        'provisioned_throughput': 'provisioned_throughput'
    }

    def __init__(self, index_name=None, shard_key_fields=None, shard_mode=None, sort_key_fields=None, abstract_fields=None, provisioned_throughput=None):
        r"""GlobalSecondaryIndex

        The model defined in huaweicloud sdk

        :param index_name: 二级索引名称，表内唯一。
        :type index_name: str
        :param shard_key_fields: 分区键字段名数组，顺序组合。
        :type shard_key_fields: list[:class:`huaweicloudsdkkvs.v1.Field`]
        :param shard_mode: 分区模式。
        :type shard_mode: str
        :param sort_key_fields: 排序键字段名数组，顺序组合。
        :type sort_key_fields: list[:class:`huaweicloudsdkkvs.v1.Field`]
        :param abstract_fields: 摘要字段名数组。
        :type abstract_fields: list[str]
        :param provisioned_throughput: 
        :type provisioned_throughput: :class:`huaweicloudsdkkvs.v1.ProvisionedThroughput`
        """
        
        

        self._index_name = None
        self._shard_key_fields = None
        self._shard_mode = None
        self._sort_key_fields = None
        self._abstract_fields = None
        self._provisioned_throughput = None
        self.discriminator = None

        self.index_name = index_name
        self.shard_key_fields = shard_key_fields
        if shard_mode is not None:
            self.shard_mode = shard_mode
        if sort_key_fields is not None:
            self.sort_key_fields = sort_key_fields
        if abstract_fields is not None:
            self.abstract_fields = abstract_fields
        if provisioned_throughput is not None:
            self.provisioned_throughput = provisioned_throughput

    @property
    def index_name(self):
        r"""Gets the index_name of this GlobalSecondaryIndex.

        二级索引名称，表内唯一。

        :return: The index_name of this GlobalSecondaryIndex.
        :rtype: str
        """
        return self._index_name

    @index_name.setter
    def index_name(self, index_name):
        r"""Sets the index_name of this GlobalSecondaryIndex.

        二级索引名称，表内唯一。

        :param index_name: The index_name of this GlobalSecondaryIndex.
        :type index_name: str
        """
        self._index_name = index_name

    @property
    def shard_key_fields(self):
        r"""Gets the shard_key_fields of this GlobalSecondaryIndex.

        分区键字段名数组，顺序组合。

        :return: The shard_key_fields of this GlobalSecondaryIndex.
        :rtype: list[:class:`huaweicloudsdkkvs.v1.Field`]
        """
        return self._shard_key_fields

    @shard_key_fields.setter
    def shard_key_fields(self, shard_key_fields):
        r"""Sets the shard_key_fields of this GlobalSecondaryIndex.

        分区键字段名数组，顺序组合。

        :param shard_key_fields: The shard_key_fields of this GlobalSecondaryIndex.
        :type shard_key_fields: list[:class:`huaweicloudsdkkvs.v1.Field`]
        """
        self._shard_key_fields = shard_key_fields

    @property
    def shard_mode(self):
        r"""Gets the shard_mode of this GlobalSecondaryIndex.

        分区模式。

        :return: The shard_mode of this GlobalSecondaryIndex.
        :rtype: str
        """
        return self._shard_mode

    @shard_mode.setter
    def shard_mode(self, shard_mode):
        r"""Sets the shard_mode of this GlobalSecondaryIndex.

        分区模式。

        :param shard_mode: The shard_mode of this GlobalSecondaryIndex.
        :type shard_mode: str
        """
        self._shard_mode = shard_mode

    @property
    def sort_key_fields(self):
        r"""Gets the sort_key_fields of this GlobalSecondaryIndex.

        排序键字段名数组，顺序组合。

        :return: The sort_key_fields of this GlobalSecondaryIndex.
        :rtype: list[:class:`huaweicloudsdkkvs.v1.Field`]
        """
        return self._sort_key_fields

    @sort_key_fields.setter
    def sort_key_fields(self, sort_key_fields):
        r"""Sets the sort_key_fields of this GlobalSecondaryIndex.

        排序键字段名数组，顺序组合。

        :param sort_key_fields: The sort_key_fields of this GlobalSecondaryIndex.
        :type sort_key_fields: list[:class:`huaweicloudsdkkvs.v1.Field`]
        """
        self._sort_key_fields = sort_key_fields

    @property
    def abstract_fields(self):
        r"""Gets the abstract_fields of this GlobalSecondaryIndex.

        摘要字段名数组。

        :return: The abstract_fields of this GlobalSecondaryIndex.
        :rtype: list[str]
        """
        return self._abstract_fields

    @abstract_fields.setter
    def abstract_fields(self, abstract_fields):
        r"""Sets the abstract_fields of this GlobalSecondaryIndex.

        摘要字段名数组。

        :param abstract_fields: The abstract_fields of this GlobalSecondaryIndex.
        :type abstract_fields: list[str]
        """
        self._abstract_fields = abstract_fields

    @property
    def provisioned_throughput(self):
        r"""Gets the provisioned_throughput of this GlobalSecondaryIndex.

        :return: The provisioned_throughput of this GlobalSecondaryIndex.
        :rtype: :class:`huaweicloudsdkkvs.v1.ProvisionedThroughput`
        """
        return self._provisioned_throughput

    @provisioned_throughput.setter
    def provisioned_throughput(self, provisioned_throughput):
        r"""Sets the provisioned_throughput of this GlobalSecondaryIndex.

        :param provisioned_throughput: The provisioned_throughput of this GlobalSecondaryIndex.
        :type provisioned_throughput: :class:`huaweicloudsdkkvs.v1.ProvisionedThroughput`
        """
        self._provisioned_throughput = provisioned_throughput

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
        if not isinstance(other, GlobalSecondaryIndex):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
