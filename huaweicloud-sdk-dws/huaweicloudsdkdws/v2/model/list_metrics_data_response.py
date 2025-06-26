# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListMetricsDataResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'code': 'int',
        'msg': 'str',
        'data': 'list[dict(str, object)]',
        'count': 'int'
    }

    attribute_map = {
        'code': 'code',
        'msg': 'msg',
        'data': 'data',
        'count': 'count'
    }

    def __init__(self, code=None, msg=None, data=None, count=None):
        r"""ListMetricsDataResponse

        The model defined in huaweicloud sdk

        :param code: **参数解释**： 响应码。 **取值范围**： 不涉及。
        :type code: int
        :param msg: **参数解释**： 响应信息。 **取值范围**： 不涉及。
        :type msg: str
        :param data: **参数解释**： 指标采集数据列表。 **取值范围**： 不涉及。
        :type data: list[dict(str, object)]
        :param count: **参数解释**： 总列表大小。 **取值范围**： 不涉及。
        :type count: int
        """
        
        super(ListMetricsDataResponse, self).__init__()

        self._code = None
        self._msg = None
        self._data = None
        self._count = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if msg is not None:
            self.msg = msg
        if data is not None:
            self.data = data
        if count is not None:
            self.count = count

    @property
    def code(self):
        r"""Gets the code of this ListMetricsDataResponse.

        **参数解释**： 响应码。 **取值范围**： 不涉及。

        :return: The code of this ListMetricsDataResponse.
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this ListMetricsDataResponse.

        **参数解释**： 响应码。 **取值范围**： 不涉及。

        :param code: The code of this ListMetricsDataResponse.
        :type code: int
        """
        self._code = code

    @property
    def msg(self):
        r"""Gets the msg of this ListMetricsDataResponse.

        **参数解释**： 响应信息。 **取值范围**： 不涉及。

        :return: The msg of this ListMetricsDataResponse.
        :rtype: str
        """
        return self._msg

    @msg.setter
    def msg(self, msg):
        r"""Sets the msg of this ListMetricsDataResponse.

        **参数解释**： 响应信息。 **取值范围**： 不涉及。

        :param msg: The msg of this ListMetricsDataResponse.
        :type msg: str
        """
        self._msg = msg

    @property
    def data(self):
        r"""Gets the data of this ListMetricsDataResponse.

        **参数解释**： 指标采集数据列表。 **取值范围**： 不涉及。

        :return: The data of this ListMetricsDataResponse.
        :rtype: list[dict(str, object)]
        """
        return self._data

    @data.setter
    def data(self, data):
        r"""Sets the data of this ListMetricsDataResponse.

        **参数解释**： 指标采集数据列表。 **取值范围**： 不涉及。

        :param data: The data of this ListMetricsDataResponse.
        :type data: list[dict(str, object)]
        """
        self._data = data

    @property
    def count(self):
        r"""Gets the count of this ListMetricsDataResponse.

        **参数解释**： 总列表大小。 **取值范围**： 不涉及。

        :return: The count of this ListMetricsDataResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListMetricsDataResponse.

        **参数解释**： 总列表大小。 **取值范围**： 不涉及。

        :param count: The count of this ListMetricsDataResponse.
        :type count: int
        """
        self._count = count

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
        if not isinstance(other, ListMetricsDataResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
