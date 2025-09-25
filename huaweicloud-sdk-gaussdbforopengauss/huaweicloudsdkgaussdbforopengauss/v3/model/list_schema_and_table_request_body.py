# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSchemaAndTableRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sql_text': 'str',
        'instance_id': 'str'
    }

    attribute_map = {
        'sql_text': 'sql_text',
        'instance_id': 'instance_id'
    }

    def __init__(self, sql_text=None, instance_id=None):
        r"""ListSchemaAndTableRequestBody

        The model defined in huaweicloud sdk

        :param sql_text: **参数解释**: SQL文本。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。
        :type sql_text: str
        :param instance_id: **参数解释**: 实例ID，此参数是用户创建实例的唯一标识。 **约束限制**: 不涉及。 **取值范围**: 只能由英文字母、数字组成，且长度为36个字符。 **默认取值**: 不涉及。
        :type instance_id: str
        """
        
        

        self._sql_text = None
        self._instance_id = None
        self.discriminator = None

        self.sql_text = sql_text
        if instance_id is not None:
            self.instance_id = instance_id

    @property
    def sql_text(self):
        r"""Gets the sql_text of this ListSchemaAndTableRequestBody.

        **参数解释**: SQL文本。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :return: The sql_text of this ListSchemaAndTableRequestBody.
        :rtype: str
        """
        return self._sql_text

    @sql_text.setter
    def sql_text(self, sql_text):
        r"""Sets the sql_text of this ListSchemaAndTableRequestBody.

        **参数解释**: SQL文本。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :param sql_text: The sql_text of this ListSchemaAndTableRequestBody.
        :type sql_text: str
        """
        self._sql_text = sql_text

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListSchemaAndTableRequestBody.

        **参数解释**: 实例ID，此参数是用户创建实例的唯一标识。 **约束限制**: 不涉及。 **取值范围**: 只能由英文字母、数字组成，且长度为36个字符。 **默认取值**: 不涉及。

        :return: The instance_id of this ListSchemaAndTableRequestBody.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListSchemaAndTableRequestBody.

        **参数解释**: 实例ID，此参数是用户创建实例的唯一标识。 **约束限制**: 不涉及。 **取值范围**: 只能由英文字母、数字组成，且长度为36个字符。 **默认取值**: 不涉及。

        :param instance_id: The instance_id of this ListSchemaAndTableRequestBody.
        :type instance_id: str
        """
        self._instance_id = instance_id

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
        if not isinstance(other, ListSchemaAndTableRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
