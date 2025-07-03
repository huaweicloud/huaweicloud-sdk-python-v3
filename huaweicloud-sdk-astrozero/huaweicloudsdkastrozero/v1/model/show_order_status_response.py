# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowOrderStatusResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'res_code': 'str',
        'res_msg': 'str',
        'result': 'object'
    }

    attribute_map = {
        'res_code': 'resCode',
        'res_msg': 'resMsg',
        'result': 'result'
    }

    def __init__(self, res_code=None, res_msg=None, result=None):
        r"""ShowOrderStatusResponse

        The model defined in huaweicloud sdk

        :param res_code: 响应码
        :type res_code: str
        :param res_msg: 响应信息
        :type res_msg: str
        :param result: 
        :type result: :class:`huaweicloudsdkastrozero.v1.object`
        """
        
        super(ShowOrderStatusResponse, self).__init__()

        self._res_code = None
        self._res_msg = None
        self._result = None
        self.discriminator = None

        if res_code is not None:
            self.res_code = res_code
        if res_msg is not None:
            self.res_msg = res_msg
        if result is not None:
            self.result = result

    @property
    def res_code(self):
        r"""Gets the res_code of this ShowOrderStatusResponse.

        响应码

        :return: The res_code of this ShowOrderStatusResponse.
        :rtype: str
        """
        return self._res_code

    @res_code.setter
    def res_code(self, res_code):
        r"""Sets the res_code of this ShowOrderStatusResponse.

        响应码

        :param res_code: The res_code of this ShowOrderStatusResponse.
        :type res_code: str
        """
        self._res_code = res_code

    @property
    def res_msg(self):
        r"""Gets the res_msg of this ShowOrderStatusResponse.

        响应信息

        :return: The res_msg of this ShowOrderStatusResponse.
        :rtype: str
        """
        return self._res_msg

    @res_msg.setter
    def res_msg(self, res_msg):
        r"""Sets the res_msg of this ShowOrderStatusResponse.

        响应信息

        :param res_msg: The res_msg of this ShowOrderStatusResponse.
        :type res_msg: str
        """
        self._res_msg = res_msg

    @property
    def result(self):
        r"""Gets the result of this ShowOrderStatusResponse.

        :return: The result of this ShowOrderStatusResponse.
        :rtype: :class:`huaweicloudsdkastrozero.v1.object`
        """
        return self._result

    @result.setter
    def result(self, result):
        r"""Sets the result of this ShowOrderStatusResponse.

        :param result: The result of this ShowOrderStatusResponse.
        :type result: :class:`huaweicloudsdkastrozero.v1.object`
        """
        self._result = result

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
        if not isinstance(other, ShowOrderStatusResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
