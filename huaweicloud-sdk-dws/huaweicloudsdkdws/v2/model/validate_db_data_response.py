# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ValidateDbDataResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'success': 'int',
        'failure': 'int',
        'type': 'str',
        'data': 'list[str]'
    }

    attribute_map = {
        'total': 'total',
        'success': 'success',
        'failure': 'failure',
        'type': 'type',
        'data': 'data'
    }

    def __init__(self, total=None, success=None, failure=None, type=None, data=None):
        r"""ValidateDbDataResponse

        The model defined in huaweicloud sdk

        :param total: **参数解释**： 校验总结果数。 **默认取值**： 不涉及。
        :type total: int
        :param success: **参数解释**： 校验成功结果数。 **默认取值**： 不涉及。
        :type success: int
        :param failure: **参数解释**： 校验失败结果数。 **默认取值**： 不涉及。
        :type failure: int
        :param type: **参数解释**： 校验数据类型。 **默认取值**： schema、table
        :type type: str
        :param data: **参数解释**： 校验成功结果数据。 **默认取值**： 不涉及。
        :type data: list[str]
        """
        
        super().__init__()

        self._total = None
        self._success = None
        self._failure = None
        self._type = None
        self._data = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if success is not None:
            self.success = success
        if failure is not None:
            self.failure = failure
        if type is not None:
            self.type = type
        if data is not None:
            self.data = data

    @property
    def total(self):
        r"""Gets the total of this ValidateDbDataResponse.

        **参数解释**： 校验总结果数。 **默认取值**： 不涉及。

        :return: The total of this ValidateDbDataResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ValidateDbDataResponse.

        **参数解释**： 校验总结果数。 **默认取值**： 不涉及。

        :param total: The total of this ValidateDbDataResponse.
        :type total: int
        """
        self._total = total

    @property
    def success(self):
        r"""Gets the success of this ValidateDbDataResponse.

        **参数解释**： 校验成功结果数。 **默认取值**： 不涉及。

        :return: The success of this ValidateDbDataResponse.
        :rtype: int
        """
        return self._success

    @success.setter
    def success(self, success):
        r"""Sets the success of this ValidateDbDataResponse.

        **参数解释**： 校验成功结果数。 **默认取值**： 不涉及。

        :param success: The success of this ValidateDbDataResponse.
        :type success: int
        """
        self._success = success

    @property
    def failure(self):
        r"""Gets the failure of this ValidateDbDataResponse.

        **参数解释**： 校验失败结果数。 **默认取值**： 不涉及。

        :return: The failure of this ValidateDbDataResponse.
        :rtype: int
        """
        return self._failure

    @failure.setter
    def failure(self, failure):
        r"""Sets the failure of this ValidateDbDataResponse.

        **参数解释**： 校验失败结果数。 **默认取值**： 不涉及。

        :param failure: The failure of this ValidateDbDataResponse.
        :type failure: int
        """
        self._failure = failure

    @property
    def type(self):
        r"""Gets the type of this ValidateDbDataResponse.

        **参数解释**： 校验数据类型。 **默认取值**： schema、table

        :return: The type of this ValidateDbDataResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ValidateDbDataResponse.

        **参数解释**： 校验数据类型。 **默认取值**： schema、table

        :param type: The type of this ValidateDbDataResponse.
        :type type: str
        """
        self._type = type

    @property
    def data(self):
        r"""Gets the data of this ValidateDbDataResponse.

        **参数解释**： 校验成功结果数据。 **默认取值**： 不涉及。

        :return: The data of this ValidateDbDataResponse.
        :rtype: list[str]
        """
        return self._data

    @data.setter
    def data(self, data):
        r"""Sets the data of this ValidateDbDataResponse.

        **参数解释**： 校验成功结果数据。 **默认取值**： 不涉及。

        :param data: The data of this ValidateDbDataResponse.
        :type data: list[str]
        """
        self._data = data

    def to_dict(self):
        import warnings
        warnings.warn("ValidateDbDataResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ValidateDbDataResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
