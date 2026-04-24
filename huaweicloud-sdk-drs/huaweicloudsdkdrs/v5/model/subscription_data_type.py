# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SubscriptionDataType:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_dml_subscribed': 'bool',
        'is_ddl_subscribed': 'bool'
    }

    attribute_map = {
        'is_dml_subscribed': 'is_dml_subscribed',
        'is_ddl_subscribed': 'is_ddl_subscribed'
    }

    def __init__(self, is_dml_subscribed=None, is_ddl_subscribed=None):
        r"""SubscriptionDataType

        The model defined in huaweicloud sdk

        :param is_dml_subscribed: 数据操作语言，取值： true：订阅DML false：不订阅DML
        :type is_dml_subscribed: bool
        :param is_ddl_subscribed: 数据定义语言，取值： true：订阅DDL false：不订阅DDL
        :type is_ddl_subscribed: bool
        """
        
        

        self._is_dml_subscribed = None
        self._is_ddl_subscribed = None
        self.discriminator = None

        self.is_dml_subscribed = is_dml_subscribed
        self.is_ddl_subscribed = is_ddl_subscribed

    @property
    def is_dml_subscribed(self):
        r"""Gets the is_dml_subscribed of this SubscriptionDataType.

        数据操作语言，取值： true：订阅DML false：不订阅DML

        :return: The is_dml_subscribed of this SubscriptionDataType.
        :rtype: bool
        """
        return self._is_dml_subscribed

    @is_dml_subscribed.setter
    def is_dml_subscribed(self, is_dml_subscribed):
        r"""Sets the is_dml_subscribed of this SubscriptionDataType.

        数据操作语言，取值： true：订阅DML false：不订阅DML

        :param is_dml_subscribed: The is_dml_subscribed of this SubscriptionDataType.
        :type is_dml_subscribed: bool
        """
        self._is_dml_subscribed = is_dml_subscribed

    @property
    def is_ddl_subscribed(self):
        r"""Gets the is_ddl_subscribed of this SubscriptionDataType.

        数据定义语言，取值： true：订阅DDL false：不订阅DDL

        :return: The is_ddl_subscribed of this SubscriptionDataType.
        :rtype: bool
        """
        return self._is_ddl_subscribed

    @is_ddl_subscribed.setter
    def is_ddl_subscribed(self, is_ddl_subscribed):
        r"""Sets the is_ddl_subscribed of this SubscriptionDataType.

        数据定义语言，取值： true：订阅DDL false：不订阅DDL

        :param is_ddl_subscribed: The is_ddl_subscribed of this SubscriptionDataType.
        :type is_ddl_subscribed: bool
        """
        self._is_ddl_subscribed = is_ddl_subscribed

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
        if not isinstance(other, SubscriptionDataType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
