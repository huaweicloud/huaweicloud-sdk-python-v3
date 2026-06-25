# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ToOndemandServiceResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_id': 'str',
        'result': 'str',
        'error_code': 'str',
        'error_msg': 'str',
        'order_id': 'str'
    }

    attribute_map = {
        'resource_id': 'resource_id',
        'result': 'result',
        'error_code': 'error_code',
        'error_msg': 'error_msg',
        'order_id': 'order_id'
    }

    def __init__(self, resource_id=None, result=None, error_code=None, error_msg=None, order_id=None):
        r"""ToOndemandServiceResult

        The model defined in huaweicloud sdk

        :param resource_id: |参数名称：转按需的服务实例id/根资源id| |参数约束以及描述：转按需的服务实例id/根资源id。对应请求体中的资源id。|
        :type resource_id: str
        :param result: |参数名称：转按需结果| |参数约束以及描述：转按需结果。SUCCESS：成功；AUDIT：审核中；FAIL：转按需失败。|
        :type result: str
        :param error_code: |参数名称：状态码| |参数约束以及描述：状态码，result&#x3D;FAIL时，必填|
        :type error_code: str
        :param error_msg: |参数名称：错误描述信息| |参数约束以及描述：错误描述信息，result&#x3D;FAIL时，必填|
        :type error_msg: str
        :param order_id: |参数名称：订单Id| |参数约束以及描述：订单Id。result&#x3D; SUCCESS、 AUDIT时，必填；其他为空。|
        :type order_id: str
        """
        
        

        self._resource_id = None
        self._result = None
        self._error_code = None
        self._error_msg = None
        self._order_id = None
        self.discriminator = None

        if resource_id is not None:
            self.resource_id = resource_id
        if result is not None:
            self.result = result
        if error_code is not None:
            self.error_code = error_code
        if error_msg is not None:
            self.error_msg = error_msg
        if order_id is not None:
            self.order_id = order_id

    @property
    def resource_id(self):
        r"""Gets the resource_id of this ToOndemandServiceResult.

        |参数名称：转按需的服务实例id/根资源id| |参数约束以及描述：转按需的服务实例id/根资源id。对应请求体中的资源id。|

        :return: The resource_id of this ToOndemandServiceResult.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this ToOndemandServiceResult.

        |参数名称：转按需的服务实例id/根资源id| |参数约束以及描述：转按需的服务实例id/根资源id。对应请求体中的资源id。|

        :param resource_id: The resource_id of this ToOndemandServiceResult.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def result(self):
        r"""Gets the result of this ToOndemandServiceResult.

        |参数名称：转按需结果| |参数约束以及描述：转按需结果。SUCCESS：成功；AUDIT：审核中；FAIL：转按需失败。|

        :return: The result of this ToOndemandServiceResult.
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        r"""Sets the result of this ToOndemandServiceResult.

        |参数名称：转按需结果| |参数约束以及描述：转按需结果。SUCCESS：成功；AUDIT：审核中；FAIL：转按需失败。|

        :param result: The result of this ToOndemandServiceResult.
        :type result: str
        """
        self._result = result

    @property
    def error_code(self):
        r"""Gets the error_code of this ToOndemandServiceResult.

        |参数名称：状态码| |参数约束以及描述：状态码，result=FAIL时，必填|

        :return: The error_code of this ToOndemandServiceResult.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        r"""Sets the error_code of this ToOndemandServiceResult.

        |参数名称：状态码| |参数约束以及描述：状态码，result=FAIL时，必填|

        :param error_code: The error_code of this ToOndemandServiceResult.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_msg(self):
        r"""Gets the error_msg of this ToOndemandServiceResult.

        |参数名称：错误描述信息| |参数约束以及描述：错误描述信息，result=FAIL时，必填|

        :return: The error_msg of this ToOndemandServiceResult.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        r"""Sets the error_msg of this ToOndemandServiceResult.

        |参数名称：错误描述信息| |参数约束以及描述：错误描述信息，result=FAIL时，必填|

        :param error_msg: The error_msg of this ToOndemandServiceResult.
        :type error_msg: str
        """
        self._error_msg = error_msg

    @property
    def order_id(self):
        r"""Gets the order_id of this ToOndemandServiceResult.

        |参数名称：订单Id| |参数约束以及描述：订单Id。result= SUCCESS、 AUDIT时，必填；其他为空。|

        :return: The order_id of this ToOndemandServiceResult.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        r"""Sets the order_id of this ToOndemandServiceResult.

        |参数名称：订单Id| |参数约束以及描述：订单Id。result= SUCCESS、 AUDIT时，必填；其他为空。|

        :param order_id: The order_id of this ToOndemandServiceResult.
        :type order_id: str
        """
        self._order_id = order_id

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
        if not isinstance(other, ToOndemandServiceResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
