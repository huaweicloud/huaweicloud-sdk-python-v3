# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SqlTypeConfigOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'category': 'str',
        'prefixes': 'list[str]'
    }

    attribute_map = {
        'category': 'category',
        'prefixes': 'prefixes'
    }

    def __init__(self, category=None, prefixes=None):
        r"""SqlTypeConfigOption

        The model defined in huaweicloud sdk

        :param category: **参数解释**: SQL类型的归类名称。 **约束限制**: - 对常用SQL类型，简单归类为6个类别，每个类别对应一组固定的采集SQL语句类型列表，采用前缀进行匹配。 - 对于其他场景，可以使用自定义类别，允许按需自定义采集SQL的语句前缀。  **取值范围**: - all：不区分SQL类型，全部采集。 - ddl：只采集DDL语句类别，包含如下SQL语句类型： create, alter, drop, truncate, reindex, vacuum, analyze, declare, move, close。 - dml：只采集DML语句类型，包含如下SQL语句类型： insert, update, delete, merge, show, explain, prepare, lock, copy, execute, deallocate。 - dcl：只采集DCL语句类型，包含如下SQL语句类型： grant, revoke, reassign, set。 - tcl：只采集TCL语句类型，包含如下SQL语句类型： begin, commit, rollback, start, savepoint, checkpoint, release savepoint。 - dql：只采集DQL语句类型，包含如下SQL语句类型： select。 - custom：采集自定义语句类型。需在prefixes字段中，填写要采集的SQL语句前缀片段。  **默认取值**: 不涉及。
        :type category: str
        :param prefixes: **参数解释**: 针对custom自定义类别，指定要采集的SQL语句类型的列表，默认取值为[]。采集过程中，采用前缀方式对SQL文本进行匹配。 **约束限制**: - category取值custom时，此参数必填，不可为空。 - category取值其他类别时，此参数忽略。
        :type prefixes: list[str]
        """
        
        

        self._category = None
        self._prefixes = None
        self.discriminator = None

        self.category = category
        if prefixes is not None:
            self.prefixes = prefixes

    @property
    def category(self):
        r"""Gets the category of this SqlTypeConfigOption.

        **参数解释**: SQL类型的归类名称。 **约束限制**: - 对常用SQL类型，简单归类为6个类别，每个类别对应一组固定的采集SQL语句类型列表，采用前缀进行匹配。 - 对于其他场景，可以使用自定义类别，允许按需自定义采集SQL的语句前缀。  **取值范围**: - all：不区分SQL类型，全部采集。 - ddl：只采集DDL语句类别，包含如下SQL语句类型： create, alter, drop, truncate, reindex, vacuum, analyze, declare, move, close。 - dml：只采集DML语句类型，包含如下SQL语句类型： insert, update, delete, merge, show, explain, prepare, lock, copy, execute, deallocate。 - dcl：只采集DCL语句类型，包含如下SQL语句类型： grant, revoke, reassign, set。 - tcl：只采集TCL语句类型，包含如下SQL语句类型： begin, commit, rollback, start, savepoint, checkpoint, release savepoint。 - dql：只采集DQL语句类型，包含如下SQL语句类型： select。 - custom：采集自定义语句类型。需在prefixes字段中，填写要采集的SQL语句前缀片段。  **默认取值**: 不涉及。

        :return: The category of this SqlTypeConfigOption.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this SqlTypeConfigOption.

        **参数解释**: SQL类型的归类名称。 **约束限制**: - 对常用SQL类型，简单归类为6个类别，每个类别对应一组固定的采集SQL语句类型列表，采用前缀进行匹配。 - 对于其他场景，可以使用自定义类别，允许按需自定义采集SQL的语句前缀。  **取值范围**: - all：不区分SQL类型，全部采集。 - ddl：只采集DDL语句类别，包含如下SQL语句类型： create, alter, drop, truncate, reindex, vacuum, analyze, declare, move, close。 - dml：只采集DML语句类型，包含如下SQL语句类型： insert, update, delete, merge, show, explain, prepare, lock, copy, execute, deallocate。 - dcl：只采集DCL语句类型，包含如下SQL语句类型： grant, revoke, reassign, set。 - tcl：只采集TCL语句类型，包含如下SQL语句类型： begin, commit, rollback, start, savepoint, checkpoint, release savepoint。 - dql：只采集DQL语句类型，包含如下SQL语句类型： select。 - custom：采集自定义语句类型。需在prefixes字段中，填写要采集的SQL语句前缀片段。  **默认取值**: 不涉及。

        :param category: The category of this SqlTypeConfigOption.
        :type category: str
        """
        self._category = category

    @property
    def prefixes(self):
        r"""Gets the prefixes of this SqlTypeConfigOption.

        **参数解释**: 针对custom自定义类别，指定要采集的SQL语句类型的列表，默认取值为[]。采集过程中，采用前缀方式对SQL文本进行匹配。 **约束限制**: - category取值custom时，此参数必填，不可为空。 - category取值其他类别时，此参数忽略。

        :return: The prefixes of this SqlTypeConfigOption.
        :rtype: list[str]
        """
        return self._prefixes

    @prefixes.setter
    def prefixes(self, prefixes):
        r"""Sets the prefixes of this SqlTypeConfigOption.

        **参数解释**: 针对custom自定义类别，指定要采集的SQL语句类型的列表，默认取值为[]。采集过程中，采用前缀方式对SQL文本进行匹配。 **约束限制**: - category取值custom时，此参数必填，不可为空。 - category取值其他类别时，此参数忽略。

        :param prefixes: The prefixes of this SqlTypeConfigOption.
        :type prefixes: list[str]
        """
        self._prefixes = prefixes

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
        if not isinstance(other, SqlTypeConfigOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
