# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteTableResponse(SdkResponse):

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
        'primary_key_schema': 'PrimaryKeySchema',
        'local_secondary_index_schema': 'list[SecondaryIndex]',
        'global_secondary_index_schema': 'list[GlobalSecondaryIndex]',
        'run_time_info': 'RunTimeInfo',
        'ttl_specification': 'TtlSpecification'
    }

    attribute_map = {
        'table_name': 'table_name',
        'primary_key_schema': 'primary_key_schema',
        'local_secondary_index_schema': 'local_secondary_index_schema',
        'global_secondary_index_schema': 'global_secondary_index_schema',
        'run_time_info': 'run_time_info',
        'ttl_specification': 'ttl_specification'
    }

    def __init__(self, table_name=None, primary_key_schema=None, local_secondary_index_schema=None, global_secondary_index_schema=None, run_time_info=None, ttl_specification=None):
        r"""DeleteTableResponse

        The model defined in huaweicloud sdk

        :param table_name: 表名。 - 长度：[3, 63] - 取值字符限制：[a-z0-9_-]+
        :type table_name: str
        :param primary_key_schema: 
        :type primary_key_schema: :class:`huaweicloudsdkkvs.v1.PrimaryKeySchema`
        :param local_secondary_index_schema: 本地二级索引模板，可以多个。
        :type local_secondary_index_schema: list[:class:`huaweicloudsdkkvs.v1.SecondaryIndex`]
        :param global_secondary_index_schema: 全局二级索引模板。
        :type global_secondary_index_schema: list[:class:`huaweicloudsdkkvs.v1.GlobalSecondaryIndex`]
        :param run_time_info: 
        :type run_time_info: :class:`huaweicloudsdkkvs.v1.RunTimeInfo`
        :param ttl_specification: 
        :type ttl_specification: :class:`huaweicloudsdkkvs.v1.TtlSpecification`
        """
        
        super(DeleteTableResponse, self).__init__()

        self._table_name = None
        self._primary_key_schema = None
        self._local_secondary_index_schema = None
        self._global_secondary_index_schema = None
        self._run_time_info = None
        self._ttl_specification = None
        self.discriminator = None

        if table_name is not None:
            self.table_name = table_name
        if primary_key_schema is not None:
            self.primary_key_schema = primary_key_schema
        if local_secondary_index_schema is not None:
            self.local_secondary_index_schema = local_secondary_index_schema
        if global_secondary_index_schema is not None:
            self.global_secondary_index_schema = global_secondary_index_schema
        if run_time_info is not None:
            self.run_time_info = run_time_info
        if ttl_specification is not None:
            self.ttl_specification = ttl_specification

    @property
    def table_name(self):
        r"""Gets the table_name of this DeleteTableResponse.

        表名。 - 长度：[3, 63] - 取值字符限制：[a-z0-9_-]+

        :return: The table_name of this DeleteTableResponse.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        r"""Sets the table_name of this DeleteTableResponse.

        表名。 - 长度：[3, 63] - 取值字符限制：[a-z0-9_-]+

        :param table_name: The table_name of this DeleteTableResponse.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def primary_key_schema(self):
        r"""Gets the primary_key_schema of this DeleteTableResponse.

        :return: The primary_key_schema of this DeleteTableResponse.
        :rtype: :class:`huaweicloudsdkkvs.v1.PrimaryKeySchema`
        """
        return self._primary_key_schema

    @primary_key_schema.setter
    def primary_key_schema(self, primary_key_schema):
        r"""Sets the primary_key_schema of this DeleteTableResponse.

        :param primary_key_schema: The primary_key_schema of this DeleteTableResponse.
        :type primary_key_schema: :class:`huaweicloudsdkkvs.v1.PrimaryKeySchema`
        """
        self._primary_key_schema = primary_key_schema

    @property
    def local_secondary_index_schema(self):
        r"""Gets the local_secondary_index_schema of this DeleteTableResponse.

        本地二级索引模板，可以多个。

        :return: The local_secondary_index_schema of this DeleteTableResponse.
        :rtype: list[:class:`huaweicloudsdkkvs.v1.SecondaryIndex`]
        """
        return self._local_secondary_index_schema

    @local_secondary_index_schema.setter
    def local_secondary_index_schema(self, local_secondary_index_schema):
        r"""Sets the local_secondary_index_schema of this DeleteTableResponse.

        本地二级索引模板，可以多个。

        :param local_secondary_index_schema: The local_secondary_index_schema of this DeleteTableResponse.
        :type local_secondary_index_schema: list[:class:`huaweicloudsdkkvs.v1.SecondaryIndex`]
        """
        self._local_secondary_index_schema = local_secondary_index_schema

    @property
    def global_secondary_index_schema(self):
        r"""Gets the global_secondary_index_schema of this DeleteTableResponse.

        全局二级索引模板。

        :return: The global_secondary_index_schema of this DeleteTableResponse.
        :rtype: list[:class:`huaweicloudsdkkvs.v1.GlobalSecondaryIndex`]
        """
        return self._global_secondary_index_schema

    @global_secondary_index_schema.setter
    def global_secondary_index_schema(self, global_secondary_index_schema):
        r"""Sets the global_secondary_index_schema of this DeleteTableResponse.

        全局二级索引模板。

        :param global_secondary_index_schema: The global_secondary_index_schema of this DeleteTableResponse.
        :type global_secondary_index_schema: list[:class:`huaweicloudsdkkvs.v1.GlobalSecondaryIndex`]
        """
        self._global_secondary_index_schema = global_secondary_index_schema

    @property
    def run_time_info(self):
        r"""Gets the run_time_info of this DeleteTableResponse.

        :return: The run_time_info of this DeleteTableResponse.
        :rtype: :class:`huaweicloudsdkkvs.v1.RunTimeInfo`
        """
        return self._run_time_info

    @run_time_info.setter
    def run_time_info(self, run_time_info):
        r"""Sets the run_time_info of this DeleteTableResponse.

        :param run_time_info: The run_time_info of this DeleteTableResponse.
        :type run_time_info: :class:`huaweicloudsdkkvs.v1.RunTimeInfo`
        """
        self._run_time_info = run_time_info

    @property
    def ttl_specification(self):
        r"""Gets the ttl_specification of this DeleteTableResponse.

        :return: The ttl_specification of this DeleteTableResponse.
        :rtype: :class:`huaweicloudsdkkvs.v1.TtlSpecification`
        """
        return self._ttl_specification

    @ttl_specification.setter
    def ttl_specification(self, ttl_specification):
        r"""Sets the ttl_specification of this DeleteTableResponse.

        :param ttl_specification: The ttl_specification of this DeleteTableResponse.
        :type ttl_specification: :class:`huaweicloudsdkkvs.v1.TtlSpecification`
        """
        self._ttl_specification = ttl_specification

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
        if not isinstance(other, DeleteTableResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
