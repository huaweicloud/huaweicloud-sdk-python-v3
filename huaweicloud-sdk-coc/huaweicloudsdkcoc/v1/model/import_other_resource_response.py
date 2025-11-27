# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImportOtherResourceResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'success': 'int',
        'total': 'int',
        'error_list': 'list[str]'
    }

    attribute_map = {
        'success': 'success',
        'total': 'total',
        'error_list': 'error_list'
    }

    def __init__(self, success=None, total=None, error_list=None):
        r"""ImportOtherResourceResponse

        The model defined in huaweicloud sdk

        :param success: **参数解释：** 成功数即excel表中数据通过校验成功的数据条数。 **取值范围：** 不涉及。
        :type success: int
        :param total: **参数解释：** 总条数即excel表中数据的总数据条数。 **取值范围：** 不涉及。
        :type total: int
        :param error_list: **参数解释：** 失败信息集合即excel表格中校验失败报错信息组合。 **取值范围：** 不涉及。
        :type error_list: list[str]
        """
        
        super().__init__()

        self._success = None
        self._total = None
        self._error_list = None
        self.discriminator = None

        if success is not None:
            self.success = success
        if total is not None:
            self.total = total
        if error_list is not None:
            self.error_list = error_list

    @property
    def success(self):
        r"""Gets the success of this ImportOtherResourceResponse.

        **参数解释：** 成功数即excel表中数据通过校验成功的数据条数。 **取值范围：** 不涉及。

        :return: The success of this ImportOtherResourceResponse.
        :rtype: int
        """
        return self._success

    @success.setter
    def success(self, success):
        r"""Sets the success of this ImportOtherResourceResponse.

        **参数解释：** 成功数即excel表中数据通过校验成功的数据条数。 **取值范围：** 不涉及。

        :param success: The success of this ImportOtherResourceResponse.
        :type success: int
        """
        self._success = success

    @property
    def total(self):
        r"""Gets the total of this ImportOtherResourceResponse.

        **参数解释：** 总条数即excel表中数据的总数据条数。 **取值范围：** 不涉及。

        :return: The total of this ImportOtherResourceResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ImportOtherResourceResponse.

        **参数解释：** 总条数即excel表中数据的总数据条数。 **取值范围：** 不涉及。

        :param total: The total of this ImportOtherResourceResponse.
        :type total: int
        """
        self._total = total

    @property
    def error_list(self):
        r"""Gets the error_list of this ImportOtherResourceResponse.

        **参数解释：** 失败信息集合即excel表格中校验失败报错信息组合。 **取值范围：** 不涉及。

        :return: The error_list of this ImportOtherResourceResponse.
        :rtype: list[str]
        """
        return self._error_list

    @error_list.setter
    def error_list(self, error_list):
        r"""Sets the error_list of this ImportOtherResourceResponse.

        **参数解释：** 失败信息集合即excel表格中校验失败报错信息组合。 **取值范围：** 不涉及。

        :param error_list: The error_list of this ImportOtherResourceResponse.
        :type error_list: list[str]
        """
        self._error_list = error_list

    def to_dict(self):
        import warnings
        warnings.warn("ImportOtherResourceResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ImportOtherResourceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
