# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckTableRestoreRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'case_sensitive': 'bool',
        'database': 'str',
        'restore_table_list': 'list[TableDetail]',
        'target_table_list': 'list[TableDetail]'
    }

    attribute_map = {
        'case_sensitive': 'case_sensitive',
        'database': 'database',
        'restore_table_list': 'restore_table_list',
        'target_table_list': 'target_table_list'
    }

    def __init__(self, case_sensitive=None, database=None, restore_table_list=None, target_table_list=None):
        r"""CheckTableRestoreRequestBody

        The model defined in huaweicloud sdk

        :param case_sensitive: **参数解释**： 名称是否区分大小写。 **取值范围**： 不涉及。
        :type case_sensitive: bool
        :param database: **参数解释**： 数据库名称。 **取值范围**： 不涉及。
        :type database: str
        :param restore_table_list: **参数解释**： 源表信息。 **取值范围**： 不涉及。
        :type restore_table_list: list[:class:`huaweicloudsdkdws.v2.TableDetail`]
        :param target_table_list: **参数解释**： 目的表信息。 **取值范围**： 不涉及。
        :type target_table_list: list[:class:`huaweicloudsdkdws.v2.TableDetail`]
        """
        
        

        self._case_sensitive = None
        self._database = None
        self._restore_table_list = None
        self._target_table_list = None
        self.discriminator = None

        self.case_sensitive = case_sensitive
        self.database = database
        self.restore_table_list = restore_table_list
        self.target_table_list = target_table_list

    @property
    def case_sensitive(self):
        r"""Gets the case_sensitive of this CheckTableRestoreRequestBody.

        **参数解释**： 名称是否区分大小写。 **取值范围**： 不涉及。

        :return: The case_sensitive of this CheckTableRestoreRequestBody.
        :rtype: bool
        """
        return self._case_sensitive

    @case_sensitive.setter
    def case_sensitive(self, case_sensitive):
        r"""Sets the case_sensitive of this CheckTableRestoreRequestBody.

        **参数解释**： 名称是否区分大小写。 **取值范围**： 不涉及。

        :param case_sensitive: The case_sensitive of this CheckTableRestoreRequestBody.
        :type case_sensitive: bool
        """
        self._case_sensitive = case_sensitive

    @property
    def database(self):
        r"""Gets the database of this CheckTableRestoreRequestBody.

        **参数解释**： 数据库名称。 **取值范围**： 不涉及。

        :return: The database of this CheckTableRestoreRequestBody.
        :rtype: str
        """
        return self._database

    @database.setter
    def database(self, database):
        r"""Sets the database of this CheckTableRestoreRequestBody.

        **参数解释**： 数据库名称。 **取值范围**： 不涉及。

        :param database: The database of this CheckTableRestoreRequestBody.
        :type database: str
        """
        self._database = database

    @property
    def restore_table_list(self):
        r"""Gets the restore_table_list of this CheckTableRestoreRequestBody.

        **参数解释**： 源表信息。 **取值范围**： 不涉及。

        :return: The restore_table_list of this CheckTableRestoreRequestBody.
        :rtype: list[:class:`huaweicloudsdkdws.v2.TableDetail`]
        """
        return self._restore_table_list

    @restore_table_list.setter
    def restore_table_list(self, restore_table_list):
        r"""Sets the restore_table_list of this CheckTableRestoreRequestBody.

        **参数解释**： 源表信息。 **取值范围**： 不涉及。

        :param restore_table_list: The restore_table_list of this CheckTableRestoreRequestBody.
        :type restore_table_list: list[:class:`huaweicloudsdkdws.v2.TableDetail`]
        """
        self._restore_table_list = restore_table_list

    @property
    def target_table_list(self):
        r"""Gets the target_table_list of this CheckTableRestoreRequestBody.

        **参数解释**： 目的表信息。 **取值范围**： 不涉及。

        :return: The target_table_list of this CheckTableRestoreRequestBody.
        :rtype: list[:class:`huaweicloudsdkdws.v2.TableDetail`]
        """
        return self._target_table_list

    @target_table_list.setter
    def target_table_list(self, target_table_list):
        r"""Sets the target_table_list of this CheckTableRestoreRequestBody.

        **参数解释**： 目的表信息。 **取值范围**： 不涉及。

        :param target_table_list: The target_table_list of this CheckTableRestoreRequestBody.
        :type target_table_list: list[:class:`huaweicloudsdkdws.v2.TableDetail`]
        """
        self._target_table_list = target_table_list

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
        if not isinstance(other, CheckTableRestoreRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
