# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAppCodesV2Response(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'size': 'int',
        'total': 'int',
        'app_codes': 'list[AppCodeBaseInfo]'
    }

    attribute_map = {
        'size': 'size',
        'total': 'total',
        'app_codes': 'app_codes'
    }

    def __init__(self, size=None, total=None, app_codes=None):
        r"""ListAppCodesV2Response

        The model defined in huaweicloud sdk

        :param size: 本次返回的列表长度
        :type size: int
        :param total: 满足条件的记录数
        :type total: int
        :param app_codes: App Code列表
        :type app_codes: list[:class:`huaweicloudsdkroma.v2.AppCodeBaseInfo`]
        """
        
        super(ListAppCodesV2Response, self).__init__()

        self._size = None
        self._total = None
        self._app_codes = None
        self.discriminator = None

        self.size = size
        self.total = total
        if app_codes is not None:
            self.app_codes = app_codes

    @property
    def size(self):
        r"""Gets the size of this ListAppCodesV2Response.

        本次返回的列表长度

        :return: The size of this ListAppCodesV2Response.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this ListAppCodesV2Response.

        本次返回的列表长度

        :param size: The size of this ListAppCodesV2Response.
        :type size: int
        """
        self._size = size

    @property
    def total(self):
        r"""Gets the total of this ListAppCodesV2Response.

        满足条件的记录数

        :return: The total of this ListAppCodesV2Response.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListAppCodesV2Response.

        满足条件的记录数

        :param total: The total of this ListAppCodesV2Response.
        :type total: int
        """
        self._total = total

    @property
    def app_codes(self):
        r"""Gets the app_codes of this ListAppCodesV2Response.

        App Code列表

        :return: The app_codes of this ListAppCodesV2Response.
        :rtype: list[:class:`huaweicloudsdkroma.v2.AppCodeBaseInfo`]
        """
        return self._app_codes

    @app_codes.setter
    def app_codes(self, app_codes):
        r"""Sets the app_codes of this ListAppCodesV2Response.

        App Code列表

        :param app_codes: The app_codes of this ListAppCodesV2Response.
        :type app_codes: list[:class:`huaweicloudsdkroma.v2.AppCodeBaseInfo`]
        """
        self._app_codes = app_codes

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
        if not isinstance(other, ListAppCodesV2Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
