# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SubAccountControlConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'separately_controlled': 'bool',
        'sub_account_type': 'str'
    }

    attribute_map = {
        'separately_controlled': 'separately_controlled',
        'sub_account_type': 'sub_account_type'
    }

    def __init__(self, separately_controlled=None, sub_account_type=None):
        r"""SubAccountControlConfig

        The model defined in huaweicloud sdk

        :param separately_controlled: 子账号业务是否单独控制。
        :type separately_controlled: bool
        :param sub_account_type: 子账号类型。 * IAM_USER: 使用调用者IAM user id填充 X-App-UserId。如果请求中携带X-App-UserId，也会被忽略替换。
        :type sub_account_type: str
        """
        
        

        self._separately_controlled = None
        self._sub_account_type = None
        self.discriminator = None

        if separately_controlled is not None:
            self.separately_controlled = separately_controlled
        if sub_account_type is not None:
            self.sub_account_type = sub_account_type

    @property
    def separately_controlled(self):
        r"""Gets the separately_controlled of this SubAccountControlConfig.

        子账号业务是否单独控制。

        :return: The separately_controlled of this SubAccountControlConfig.
        :rtype: bool
        """
        return self._separately_controlled

    @separately_controlled.setter
    def separately_controlled(self, separately_controlled):
        r"""Sets the separately_controlled of this SubAccountControlConfig.

        子账号业务是否单独控制。

        :param separately_controlled: The separately_controlled of this SubAccountControlConfig.
        :type separately_controlled: bool
        """
        self._separately_controlled = separately_controlled

    @property
    def sub_account_type(self):
        r"""Gets the sub_account_type of this SubAccountControlConfig.

        子账号类型。 * IAM_USER: 使用调用者IAM user id填充 X-App-UserId。如果请求中携带X-App-UserId，也会被忽略替换。

        :return: The sub_account_type of this SubAccountControlConfig.
        :rtype: str
        """
        return self._sub_account_type

    @sub_account_type.setter
    def sub_account_type(self, sub_account_type):
        r"""Sets the sub_account_type of this SubAccountControlConfig.

        子账号类型。 * IAM_USER: 使用调用者IAM user id填充 X-App-UserId。如果请求中携带X-App-UserId，也会被忽略替换。

        :param sub_account_type: The sub_account_type of this SubAccountControlConfig.
        :type sub_account_type: str
        """
        self._sub_account_type = sub_account_type

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
        if not isinstance(other, SubAccountControlConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
