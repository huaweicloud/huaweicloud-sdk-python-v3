# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SqlTypeInfoResult:

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
        'prefixes': 'list[str]',
        'is_preset': 'bool'
    }

    attribute_map = {
        'category': 'category',
        'prefixes': 'prefixes',
        'is_preset': 'is_preset'
    }

    def __init__(self, category=None, prefixes=None, is_preset=None):
        r"""SqlTypeInfoResult

        The model defined in huaweicloud sdk

        :param category: **参数解释**: SQL类型的归类名称。 - 对常用SQL类型，简单归类为6个类别，每个类别对应一组固定的采集SQL语句类型列表，采用前缀进行匹配。 - 对于其他场景，可以使用自定义类别，允许按需自定义采集SQL的语句前缀。  **取值范围**: - all：不区分SQL类型，全部采集。 - ddl：只采集DDL语句类型。 - dml：只采集DML语句类型。 - dcl：只采集DCL语句类型。 - tcl：只采集TCL语句类型。 - dql：只采集DQL语句类型。 - custom：采集自定义语句类型。
        :type category: str
        :param prefixes: **参数解释**: 对应SQL类别中，采集的SQL语句类型列表，采用前缀方式进行匹配。 对应不同的SQL类别，取值有所不同，对应关系如下： - all：不区分SQL类型，全部采集。对应取值为： [\&quot;.*\&quot;]。 - ddl：只采集DDL语句类别，对于取值为： [\&quot;create\&quot;, \&quot;alter\&quot;, \&quot;drop\&quot;, \&quot;truncate\&quot;, \&quot;reindex\&quot;, \&quot;vacuum\&quot;, \&quot;analyze\&quot;, \&quot;declare\&quot;, \&quot;move\&quot;, \&quot;close\&quot;]。 - dml：只采集DML语句类型，对于取值为： [\&quot;insert\&quot;, \&quot;update\&quot;, \&quot;delete\&quot;, \&quot;merge\&quot;, \&quot;show\&quot;, \&quot;explain\&quot;, \&quot;prepare\&quot;, \&quot;lock\&quot;, \&quot;copy\&quot;, \&quot;execute\&quot;, \&quot;deallocate\&quot;]。 - dcl：只采集DCL语句类型，对于取值为： [\&quot;grant\&quot;, \&quot;revoke\&quot;, \&quot;reassign\&quot;, \&quot;set\&quot;]。 - tcl：只采集TCL语句类型，对于取值为： [\&quot;begin\&quot;, \&quot;commit\&quot;, \&quot;rollback\&quot;, \&quot;start\&quot;, \&quot;savepoint\&quot;, \&quot;checkpoint\&quot;, \&quot;release savepoint\&quot;]。 - dql：只采集DQL语句类型，对于取值为： [\&quot;select\&quot;]。 - custom：采集自定义语句类型。对应取值为： 开启全量SQL时，用户填写的自定义SQL语句类型列表。  **取值范围**: 不涉及。
        :type prefixes: list[str]
        :param is_preset: **参数解释**: 对应SQL类别是否为预置类别。 **取值范围**: - true：对应category取值all、ddl 、dml 、dcl 、tcl 、dql 。 - false：对应category取值custom。
        :type is_preset: bool
        """
        
        

        self._category = None
        self._prefixes = None
        self._is_preset = None
        self.discriminator = None

        if category is not None:
            self.category = category
        if prefixes is not None:
            self.prefixes = prefixes
        if is_preset is not None:
            self.is_preset = is_preset

    @property
    def category(self):
        r"""Gets the category of this SqlTypeInfoResult.

        **参数解释**: SQL类型的归类名称。 - 对常用SQL类型，简单归类为6个类别，每个类别对应一组固定的采集SQL语句类型列表，采用前缀进行匹配。 - 对于其他场景，可以使用自定义类别，允许按需自定义采集SQL的语句前缀。  **取值范围**: - all：不区分SQL类型，全部采集。 - ddl：只采集DDL语句类型。 - dml：只采集DML语句类型。 - dcl：只采集DCL语句类型。 - tcl：只采集TCL语句类型。 - dql：只采集DQL语句类型。 - custom：采集自定义语句类型。

        :return: The category of this SqlTypeInfoResult.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this SqlTypeInfoResult.

        **参数解释**: SQL类型的归类名称。 - 对常用SQL类型，简单归类为6个类别，每个类别对应一组固定的采集SQL语句类型列表，采用前缀进行匹配。 - 对于其他场景，可以使用自定义类别，允许按需自定义采集SQL的语句前缀。  **取值范围**: - all：不区分SQL类型，全部采集。 - ddl：只采集DDL语句类型。 - dml：只采集DML语句类型。 - dcl：只采集DCL语句类型。 - tcl：只采集TCL语句类型。 - dql：只采集DQL语句类型。 - custom：采集自定义语句类型。

        :param category: The category of this SqlTypeInfoResult.
        :type category: str
        """
        self._category = category

    @property
    def prefixes(self):
        r"""Gets the prefixes of this SqlTypeInfoResult.

        **参数解释**: 对应SQL类别中，采集的SQL语句类型列表，采用前缀方式进行匹配。 对应不同的SQL类别，取值有所不同，对应关系如下： - all：不区分SQL类型，全部采集。对应取值为： [\".*\"]。 - ddl：只采集DDL语句类别，对于取值为： [\"create\", \"alter\", \"drop\", \"truncate\", \"reindex\", \"vacuum\", \"analyze\", \"declare\", \"move\", \"close\"]。 - dml：只采集DML语句类型，对于取值为： [\"insert\", \"update\", \"delete\", \"merge\", \"show\", \"explain\", \"prepare\", \"lock\", \"copy\", \"execute\", \"deallocate\"]。 - dcl：只采集DCL语句类型，对于取值为： [\"grant\", \"revoke\", \"reassign\", \"set\"]。 - tcl：只采集TCL语句类型，对于取值为： [\"begin\", \"commit\", \"rollback\", \"start\", \"savepoint\", \"checkpoint\", \"release savepoint\"]。 - dql：只采集DQL语句类型，对于取值为： [\"select\"]。 - custom：采集自定义语句类型。对应取值为： 开启全量SQL时，用户填写的自定义SQL语句类型列表。  **取值范围**: 不涉及。

        :return: The prefixes of this SqlTypeInfoResult.
        :rtype: list[str]
        """
        return self._prefixes

    @prefixes.setter
    def prefixes(self, prefixes):
        r"""Sets the prefixes of this SqlTypeInfoResult.

        **参数解释**: 对应SQL类别中，采集的SQL语句类型列表，采用前缀方式进行匹配。 对应不同的SQL类别，取值有所不同，对应关系如下： - all：不区分SQL类型，全部采集。对应取值为： [\".*\"]。 - ddl：只采集DDL语句类别，对于取值为： [\"create\", \"alter\", \"drop\", \"truncate\", \"reindex\", \"vacuum\", \"analyze\", \"declare\", \"move\", \"close\"]。 - dml：只采集DML语句类型，对于取值为： [\"insert\", \"update\", \"delete\", \"merge\", \"show\", \"explain\", \"prepare\", \"lock\", \"copy\", \"execute\", \"deallocate\"]。 - dcl：只采集DCL语句类型，对于取值为： [\"grant\", \"revoke\", \"reassign\", \"set\"]。 - tcl：只采集TCL语句类型，对于取值为： [\"begin\", \"commit\", \"rollback\", \"start\", \"savepoint\", \"checkpoint\", \"release savepoint\"]。 - dql：只采集DQL语句类型，对于取值为： [\"select\"]。 - custom：采集自定义语句类型。对应取值为： 开启全量SQL时，用户填写的自定义SQL语句类型列表。  **取值范围**: 不涉及。

        :param prefixes: The prefixes of this SqlTypeInfoResult.
        :type prefixes: list[str]
        """
        self._prefixes = prefixes

    @property
    def is_preset(self):
        r"""Gets the is_preset of this SqlTypeInfoResult.

        **参数解释**: 对应SQL类别是否为预置类别。 **取值范围**: - true：对应category取值all、ddl 、dml 、dcl 、tcl 、dql 。 - false：对应category取值custom。

        :return: The is_preset of this SqlTypeInfoResult.
        :rtype: bool
        """
        return self._is_preset

    @is_preset.setter
    def is_preset(self, is_preset):
        r"""Sets the is_preset of this SqlTypeInfoResult.

        **参数解释**: 对应SQL类别是否为预置类别。 **取值范围**: - true：对应category取值all、ddl 、dml 、dcl 、tcl 、dql 。 - false：对应category取值custom。

        :param is_preset: The is_preset of this SqlTypeInfoResult.
        :type is_preset: bool
        """
        self._is_preset = is_preset

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
        if not isinstance(other, SqlTypeInfoResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
