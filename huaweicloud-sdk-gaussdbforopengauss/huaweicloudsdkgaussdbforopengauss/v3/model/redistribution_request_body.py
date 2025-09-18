# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RedistributionRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'redis_join_tables': 'list[list[str]]',
        'redis_parallel_jobs': 'int',
        'redis_resource_level': 'str'
    }

    attribute_map = {
        'redis_join_tables': 'redis_join_tables',
        'redis_parallel_jobs': 'redis_parallel_jobs',
        'redis_resource_level': 'redis_resource_level'
    }

    def __init__(self, redis_join_tables=None, redis_parallel_jobs=None, redis_resource_level=None):
        r"""RedistributionRequestBody

        The model defined in huaweicloud sdk

        :param redis_join_tables: **参数解释**: 具有JOIN关系的表，指定该参数则启用多表扩容模式，扩容前设置生效。 如果指定过该参数，后续调用可以传入空数组清除多表扩容配置。 按照“database名称、schema1名称、table1名称、schema2名称、table2名称...”的格式指定，带有大小写或特殊字符的表名需要加\&quot;\&quot;转义。 多个数组则表示存在多个join group。 **约束限制**: 本次扩容结束后自动清除该配置，下次扩容需要重新设置。
        :type redis_join_tables: list[list[str]]
        :param redis_parallel_jobs: **参数解释**: 重分布并发数。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。
        :type redis_parallel_jobs: int
        :param redis_resource_level: **参数解释**: 重分布资源管控级别。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。
        :type redis_resource_level: str
        """
        
        

        self._redis_join_tables = None
        self._redis_parallel_jobs = None
        self._redis_resource_level = None
        self.discriminator = None

        if redis_join_tables is not None:
            self.redis_join_tables = redis_join_tables
        if redis_parallel_jobs is not None:
            self.redis_parallel_jobs = redis_parallel_jobs
        if redis_resource_level is not None:
            self.redis_resource_level = redis_resource_level

    @property
    def redis_join_tables(self):
        r"""Gets the redis_join_tables of this RedistributionRequestBody.

        **参数解释**: 具有JOIN关系的表，指定该参数则启用多表扩容模式，扩容前设置生效。 如果指定过该参数，后续调用可以传入空数组清除多表扩容配置。 按照“database名称、schema1名称、table1名称、schema2名称、table2名称...”的格式指定，带有大小写或特殊字符的表名需要加\"\"转义。 多个数组则表示存在多个join group。 **约束限制**: 本次扩容结束后自动清除该配置，下次扩容需要重新设置。

        :return: The redis_join_tables of this RedistributionRequestBody.
        :rtype: list[list[str]]
        """
        return self._redis_join_tables

    @redis_join_tables.setter
    def redis_join_tables(self, redis_join_tables):
        r"""Sets the redis_join_tables of this RedistributionRequestBody.

        **参数解释**: 具有JOIN关系的表，指定该参数则启用多表扩容模式，扩容前设置生效。 如果指定过该参数，后续调用可以传入空数组清除多表扩容配置。 按照“database名称、schema1名称、table1名称、schema2名称、table2名称...”的格式指定，带有大小写或特殊字符的表名需要加\"\"转义。 多个数组则表示存在多个join group。 **约束限制**: 本次扩容结束后自动清除该配置，下次扩容需要重新设置。

        :param redis_join_tables: The redis_join_tables of this RedistributionRequestBody.
        :type redis_join_tables: list[list[str]]
        """
        self._redis_join_tables = redis_join_tables

    @property
    def redis_parallel_jobs(self):
        r"""Gets the redis_parallel_jobs of this RedistributionRequestBody.

        **参数解释**: 重分布并发数。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :return: The redis_parallel_jobs of this RedistributionRequestBody.
        :rtype: int
        """
        return self._redis_parallel_jobs

    @redis_parallel_jobs.setter
    def redis_parallel_jobs(self, redis_parallel_jobs):
        r"""Sets the redis_parallel_jobs of this RedistributionRequestBody.

        **参数解释**: 重分布并发数。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :param redis_parallel_jobs: The redis_parallel_jobs of this RedistributionRequestBody.
        :type redis_parallel_jobs: int
        """
        self._redis_parallel_jobs = redis_parallel_jobs

    @property
    def redis_resource_level(self):
        r"""Gets the redis_resource_level of this RedistributionRequestBody.

        **参数解释**: 重分布资源管控级别。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :return: The redis_resource_level of this RedistributionRequestBody.
        :rtype: str
        """
        return self._redis_resource_level

    @redis_resource_level.setter
    def redis_resource_level(self, redis_resource_level):
        r"""Sets the redis_resource_level of this RedistributionRequestBody.

        **参数解释**: 重分布资源管控级别。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :param redis_resource_level: The redis_resource_level of this RedistributionRequestBody.
        :type redis_resource_level: str
        """
        self._redis_resource_level = redis_resource_level

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
        if not isinstance(other, RedistributionRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
