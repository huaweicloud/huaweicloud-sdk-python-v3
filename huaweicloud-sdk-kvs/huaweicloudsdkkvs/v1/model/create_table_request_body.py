# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateTableRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'table_name': 'str',
        'bill_mode': 'str',
        'provisioned_throughput': 'ProvisionedThroughput',
        'primary_key_schema': 'PrimaryKeySchema',
        'local_secondary_index_schema': 'list[SecondaryIndex]',
        'global_secondary_index_schema': 'list[GlobalSecondaryIndex]',
        'pre_split_key_options': 'PreSplitKeyOptions',
        'ttl_specification': 'TtlSpecification',
        'sse_specification': 'SseSpecification'
    }

    attribute_map = {
        'table_name': 'table_name',
        'bill_mode': 'bill_mode',
        'provisioned_throughput': 'provisioned_throughput',
        'primary_key_schema': 'primary_key_schema',
        'local_secondary_index_schema': 'local_secondary_index_schema',
        'global_secondary_index_schema': 'global_secondary_index_schema',
        'pre_split_key_options': 'pre_split_key_options',
        'ttl_specification': 'ttl_specification',
        'sse_specification': 'sse_specification'
    }

    def __init__(self, table_name=None, bill_mode=None, provisioned_throughput=None, primary_key_schema=None, local_secondary_index_schema=None, global_secondary_index_schema=None, pre_split_key_options=None, ttl_specification=None, sse_specification=None):
        r"""CreateTableRequestBody

        The model defined in huaweicloud sdk

        :param table_name: 表名，仓内唯一。
        :type table_name: str
        :param bill_mode: 表计费模式，可为\&quot;provisioned\&quot;或\&quot;on_demand\&quot; - 预置模式：provisioned - 按需模式：on_demand
        :type bill_mode: str
        :param provisioned_throughput: 
        :type provisioned_throughput: :class:`huaweicloudsdkkvs.v1.ProvisionedThroughput`
        :param primary_key_schema: 
        :type primary_key_schema: :class:`huaweicloudsdkkvs.v1.PrimaryKeySchema`
        :param local_secondary_index_schema: 本地二级索引模板，可以多个。
        :type local_secondary_index_schema: list[:class:`huaweicloudsdkkvs.v1.SecondaryIndex`]
        :param global_secondary_index_schema: 全局二级索引模板。
        :type global_secondary_index_schema: list[:class:`huaweicloudsdkkvs.v1.GlobalSecondaryIndex`]
        :param pre_split_key_options: 
        :type pre_split_key_options: :class:`huaweicloudsdkkvs.v1.PreSplitKeyOptions`
        :param ttl_specification: 
        :type ttl_specification: :class:`huaweicloudsdkkvs.v1.TtlSpecification`
        :param sse_specification: 
        :type sse_specification: :class:`huaweicloudsdkkvs.v1.SseSpecification`
        """
        
        

        self._table_name = None
        self._bill_mode = None
        self._provisioned_throughput = None
        self._primary_key_schema = None
        self._local_secondary_index_schema = None
        self._global_secondary_index_schema = None
        self._pre_split_key_options = None
        self._ttl_specification = None
        self._sse_specification = None
        self.discriminator = None

        self.table_name = table_name
        if bill_mode is not None:
            self.bill_mode = bill_mode
        if provisioned_throughput is not None:
            self.provisioned_throughput = provisioned_throughput
        self.primary_key_schema = primary_key_schema
        if local_secondary_index_schema is not None:
            self.local_secondary_index_schema = local_secondary_index_schema
        if global_secondary_index_schema is not None:
            self.global_secondary_index_schema = global_secondary_index_schema
        if pre_split_key_options is not None:
            self.pre_split_key_options = pre_split_key_options
        if ttl_specification is not None:
            self.ttl_specification = ttl_specification
        if sse_specification is not None:
            self.sse_specification = sse_specification

    @property
    def table_name(self):
        r"""Gets the table_name of this CreateTableRequestBody.

        表名，仓内唯一。

        :return: The table_name of this CreateTableRequestBody.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        r"""Sets the table_name of this CreateTableRequestBody.

        表名，仓内唯一。

        :param table_name: The table_name of this CreateTableRequestBody.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def bill_mode(self):
        r"""Gets the bill_mode of this CreateTableRequestBody.

        表计费模式，可为\"provisioned\"或\"on_demand\" - 预置模式：provisioned - 按需模式：on_demand

        :return: The bill_mode of this CreateTableRequestBody.
        :rtype: str
        """
        return self._bill_mode

    @bill_mode.setter
    def bill_mode(self, bill_mode):
        r"""Sets the bill_mode of this CreateTableRequestBody.

        表计费模式，可为\"provisioned\"或\"on_demand\" - 预置模式：provisioned - 按需模式：on_demand

        :param bill_mode: The bill_mode of this CreateTableRequestBody.
        :type bill_mode: str
        """
        self._bill_mode = bill_mode

    @property
    def provisioned_throughput(self):
        r"""Gets the provisioned_throughput of this CreateTableRequestBody.

        :return: The provisioned_throughput of this CreateTableRequestBody.
        :rtype: :class:`huaweicloudsdkkvs.v1.ProvisionedThroughput`
        """
        return self._provisioned_throughput

    @provisioned_throughput.setter
    def provisioned_throughput(self, provisioned_throughput):
        r"""Sets the provisioned_throughput of this CreateTableRequestBody.

        :param provisioned_throughput: The provisioned_throughput of this CreateTableRequestBody.
        :type provisioned_throughput: :class:`huaweicloudsdkkvs.v1.ProvisionedThroughput`
        """
        self._provisioned_throughput = provisioned_throughput

    @property
    def primary_key_schema(self):
        r"""Gets the primary_key_schema of this CreateTableRequestBody.

        :return: The primary_key_schema of this CreateTableRequestBody.
        :rtype: :class:`huaweicloudsdkkvs.v1.PrimaryKeySchema`
        """
        return self._primary_key_schema

    @primary_key_schema.setter
    def primary_key_schema(self, primary_key_schema):
        r"""Sets the primary_key_schema of this CreateTableRequestBody.

        :param primary_key_schema: The primary_key_schema of this CreateTableRequestBody.
        :type primary_key_schema: :class:`huaweicloudsdkkvs.v1.PrimaryKeySchema`
        """
        self._primary_key_schema = primary_key_schema

    @property
    def local_secondary_index_schema(self):
        r"""Gets the local_secondary_index_schema of this CreateTableRequestBody.

        本地二级索引模板，可以多个。

        :return: The local_secondary_index_schema of this CreateTableRequestBody.
        :rtype: list[:class:`huaweicloudsdkkvs.v1.SecondaryIndex`]
        """
        return self._local_secondary_index_schema

    @local_secondary_index_schema.setter
    def local_secondary_index_schema(self, local_secondary_index_schema):
        r"""Sets the local_secondary_index_schema of this CreateTableRequestBody.

        本地二级索引模板，可以多个。

        :param local_secondary_index_schema: The local_secondary_index_schema of this CreateTableRequestBody.
        :type local_secondary_index_schema: list[:class:`huaweicloudsdkkvs.v1.SecondaryIndex`]
        """
        self._local_secondary_index_schema = local_secondary_index_schema

    @property
    def global_secondary_index_schema(self):
        r"""Gets the global_secondary_index_schema of this CreateTableRequestBody.

        全局二级索引模板。

        :return: The global_secondary_index_schema of this CreateTableRequestBody.
        :rtype: list[:class:`huaweicloudsdkkvs.v1.GlobalSecondaryIndex`]
        """
        return self._global_secondary_index_schema

    @global_secondary_index_schema.setter
    def global_secondary_index_schema(self, global_secondary_index_schema):
        r"""Sets the global_secondary_index_schema of this CreateTableRequestBody.

        全局二级索引模板。

        :param global_secondary_index_schema: The global_secondary_index_schema of this CreateTableRequestBody.
        :type global_secondary_index_schema: list[:class:`huaweicloudsdkkvs.v1.GlobalSecondaryIndex`]
        """
        self._global_secondary_index_schema = global_secondary_index_schema

    @property
    def pre_split_key_options(self):
        r"""Gets the pre_split_key_options of this CreateTableRequestBody.

        :return: The pre_split_key_options of this CreateTableRequestBody.
        :rtype: :class:`huaweicloudsdkkvs.v1.PreSplitKeyOptions`
        """
        return self._pre_split_key_options

    @pre_split_key_options.setter
    def pre_split_key_options(self, pre_split_key_options):
        r"""Sets the pre_split_key_options of this CreateTableRequestBody.

        :param pre_split_key_options: The pre_split_key_options of this CreateTableRequestBody.
        :type pre_split_key_options: :class:`huaweicloudsdkkvs.v1.PreSplitKeyOptions`
        """
        self._pre_split_key_options = pre_split_key_options

    @property
    def ttl_specification(self):
        r"""Gets the ttl_specification of this CreateTableRequestBody.

        :return: The ttl_specification of this CreateTableRequestBody.
        :rtype: :class:`huaweicloudsdkkvs.v1.TtlSpecification`
        """
        return self._ttl_specification

    @ttl_specification.setter
    def ttl_specification(self, ttl_specification):
        r"""Sets the ttl_specification of this CreateTableRequestBody.

        :param ttl_specification: The ttl_specification of this CreateTableRequestBody.
        :type ttl_specification: :class:`huaweicloudsdkkvs.v1.TtlSpecification`
        """
        self._ttl_specification = ttl_specification

    @property
    def sse_specification(self):
        r"""Gets the sse_specification of this CreateTableRequestBody.

        :return: The sse_specification of this CreateTableRequestBody.
        :rtype: :class:`huaweicloudsdkkvs.v1.SseSpecification`
        """
        return self._sse_specification

    @sse_specification.setter
    def sse_specification(self, sse_specification):
        r"""Sets the sse_specification of this CreateTableRequestBody.

        :param sse_specification: The sse_specification of this CreateTableRequestBody.
        :type sse_specification: :class:`huaweicloudsdkkvs.v1.SseSpecification`
        """
        self._sse_specification = sse_specification

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
        if not isinstance(other, CreateTableRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
