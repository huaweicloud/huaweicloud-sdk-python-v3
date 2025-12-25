# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EnableDataclassTypeRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enable': 'bool',
        'ids': 'list[str]'
    }

    attribute_map = {
        'enable': 'enable',
        'ids': 'ids'
    }

    def __init__(self, enable=None, ids=None):
        r"""EnableDataclassTypeRequestBody

        The model defined in huaweicloud sdk

        :param enable: 是否启用,启用：true，禁用：false
        :type enable: bool
        :param ids: 类型ids
        :type ids: list[str]
        """
        
        

        self._enable = None
        self._ids = None
        self.discriminator = None

        self.enable = enable
        self.ids = ids

    @property
    def enable(self):
        r"""Gets the enable of this EnableDataclassTypeRequestBody.

        是否启用,启用：true，禁用：false

        :return: The enable of this EnableDataclassTypeRequestBody.
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        r"""Sets the enable of this EnableDataclassTypeRequestBody.

        是否启用,启用：true，禁用：false

        :param enable: The enable of this EnableDataclassTypeRequestBody.
        :type enable: bool
        """
        self._enable = enable

    @property
    def ids(self):
        r"""Gets the ids of this EnableDataclassTypeRequestBody.

        类型ids

        :return: The ids of this EnableDataclassTypeRequestBody.
        :rtype: list[str]
        """
        return self._ids

    @ids.setter
    def ids(self, ids):
        r"""Sets the ids of this EnableDataclassTypeRequestBody.

        类型ids

        :param ids: The ids of this EnableDataclassTypeRequestBody.
        :type ids: list[str]
        """
        self._ids = ids

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
        if not isinstance(other, EnableDataclassTypeRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
