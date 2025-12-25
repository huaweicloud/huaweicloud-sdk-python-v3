# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SearchCheckitemsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'builtin_checkitem_num': 'float',
        'checkitem_num': 'float',
        'customized_checkitem_num': 'float',
        'count': 'float',
        'checkitems': 'list[CheckitemModel]'
    }

    attribute_map = {
        'builtin_checkitem_num': 'builtin_checkitem_num',
        'checkitem_num': 'checkitem_num',
        'customized_checkitem_num': 'customized_checkitem_num',
        'count': 'count',
        'checkitems': 'checkitems'
    }

    def __init__(self, builtin_checkitem_num=None, checkitem_num=None, customized_checkitem_num=None, count=None, checkitems=None):
        r"""SearchCheckitemsResponse

        The model defined in huaweicloud sdk

        :param builtin_checkitem_num: 内置检查项个数
        :type builtin_checkitem_num: float
        :param checkitem_num: 检查项总数
        :type checkitem_num: float
        :param customized_checkitem_num: 自定义检查项个数
        :type customized_checkitem_num: float
        :param count: 检查项总数
        :type count: float
        :param checkitems: 检查项详情
        :type checkitems: list[:class:`huaweicloudsdksecmaster.v2.CheckitemModel`]
        """
        
        super().__init__()

        self._builtin_checkitem_num = None
        self._checkitem_num = None
        self._customized_checkitem_num = None
        self._count = None
        self._checkitems = None
        self.discriminator = None

        if builtin_checkitem_num is not None:
            self.builtin_checkitem_num = builtin_checkitem_num
        if checkitem_num is not None:
            self.checkitem_num = checkitem_num
        if customized_checkitem_num is not None:
            self.customized_checkitem_num = customized_checkitem_num
        if count is not None:
            self.count = count
        if checkitems is not None:
            self.checkitems = checkitems

    @property
    def builtin_checkitem_num(self):
        r"""Gets the builtin_checkitem_num of this SearchCheckitemsResponse.

        内置检查项个数

        :return: The builtin_checkitem_num of this SearchCheckitemsResponse.
        :rtype: float
        """
        return self._builtin_checkitem_num

    @builtin_checkitem_num.setter
    def builtin_checkitem_num(self, builtin_checkitem_num):
        r"""Sets the builtin_checkitem_num of this SearchCheckitemsResponse.

        内置检查项个数

        :param builtin_checkitem_num: The builtin_checkitem_num of this SearchCheckitemsResponse.
        :type builtin_checkitem_num: float
        """
        self._builtin_checkitem_num = builtin_checkitem_num

    @property
    def checkitem_num(self):
        r"""Gets the checkitem_num of this SearchCheckitemsResponse.

        检查项总数

        :return: The checkitem_num of this SearchCheckitemsResponse.
        :rtype: float
        """
        return self._checkitem_num

    @checkitem_num.setter
    def checkitem_num(self, checkitem_num):
        r"""Sets the checkitem_num of this SearchCheckitemsResponse.

        检查项总数

        :param checkitem_num: The checkitem_num of this SearchCheckitemsResponse.
        :type checkitem_num: float
        """
        self._checkitem_num = checkitem_num

    @property
    def customized_checkitem_num(self):
        r"""Gets the customized_checkitem_num of this SearchCheckitemsResponse.

        自定义检查项个数

        :return: The customized_checkitem_num of this SearchCheckitemsResponse.
        :rtype: float
        """
        return self._customized_checkitem_num

    @customized_checkitem_num.setter
    def customized_checkitem_num(self, customized_checkitem_num):
        r"""Sets the customized_checkitem_num of this SearchCheckitemsResponse.

        自定义检查项个数

        :param customized_checkitem_num: The customized_checkitem_num of this SearchCheckitemsResponse.
        :type customized_checkitem_num: float
        """
        self._customized_checkitem_num = customized_checkitem_num

    @property
    def count(self):
        r"""Gets the count of this SearchCheckitemsResponse.

        检查项总数

        :return: The count of this SearchCheckitemsResponse.
        :rtype: float
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this SearchCheckitemsResponse.

        检查项总数

        :param count: The count of this SearchCheckitemsResponse.
        :type count: float
        """
        self._count = count

    @property
    def checkitems(self):
        r"""Gets the checkitems of this SearchCheckitemsResponse.

        检查项详情

        :return: The checkitems of this SearchCheckitemsResponse.
        :rtype: list[:class:`huaweicloudsdksecmaster.v2.CheckitemModel`]
        """
        return self._checkitems

    @checkitems.setter
    def checkitems(self, checkitems):
        r"""Sets the checkitems of this SearchCheckitemsResponse.

        检查项详情

        :param checkitems: The checkitems of this SearchCheckitemsResponse.
        :type checkitems: list[:class:`huaweicloudsdksecmaster.v2.CheckitemModel`]
        """
        self._checkitems = checkitems

    def to_dict(self):
        import warnings
        warnings.warn("SearchCheckitemsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, SearchCheckitemsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
