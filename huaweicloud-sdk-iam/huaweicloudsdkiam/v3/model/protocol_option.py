# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProtocolOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'mapping_id': 'str'
    }

    attribute_map = {
        'mapping_id': 'mapping_id'
    }

    def __init__(self, mapping_id=None):
        """ProtocolOption

        The model defined in huaweicloud sdk

        :param mapping_id: 映射ID。身份提供商类型为iam_user_sso时，不需要绑定映射ID，无需传入此字段；否则此字段必填。
        :type mapping_id: str
        """
        
        

        self._mapping_id = None
        self.discriminator = None

        if mapping_id is not None:
            self.mapping_id = mapping_id

    @property
    def mapping_id(self):
        """Gets the mapping_id of this ProtocolOption.

        映射ID。身份提供商类型为iam_user_sso时，不需要绑定映射ID，无需传入此字段；否则此字段必填。

        :return: The mapping_id of this ProtocolOption.
        :rtype: str
        """
        return self._mapping_id

    @mapping_id.setter
    def mapping_id(self, mapping_id):
        """Sets the mapping_id of this ProtocolOption.

        映射ID。身份提供商类型为iam_user_sso时，不需要绑定映射ID，无需传入此字段；否则此字段必填。

        :param mapping_id: The mapping_id of this ProtocolOption.
        :type mapping_id: str
        """
        self._mapping_id = mapping_id

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
        if not isinstance(other, ProtocolOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
