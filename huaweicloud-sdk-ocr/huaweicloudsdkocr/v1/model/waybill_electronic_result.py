# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WaybillElectronicResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'code': 'str',
        'receiver_name': 'str',
        'receiver_phone': 'str',
        'receiver_address': 'str',
        'sender_name': 'str',
        'sender_phone': 'str',
        'sender_address': 'str',
        'waybill_number': 'str',
        'confidence': 'object'
    }

    attribute_map = {
        'code': 'code',
        'receiver_name': 'receiver_name',
        'receiver_phone': 'receiver_phone',
        'receiver_address': 'receiver_address',
        'sender_name': 'sender_name',
        'sender_phone': 'sender_phone',
        'sender_address': 'sender_address',
        'waybill_number': 'waybill_number',
        'confidence': 'confidence'
    }

    def __init__(self, code=None, receiver_name=None, receiver_phone=None, receiver_address=None, sender_name=None, sender_phone=None, sender_address=None, waybill_number=None, confidence=None):
        """WaybillElectronicResult

        The model defined in huaweicloud sdk

        :param code: 三段码。 
        :type code: str
        :param receiver_name: 收件人姓名。 
        :type receiver_name: str
        :param receiver_phone: 收件人电话。 
        :type receiver_phone: str
        :param receiver_address: 收件人地址。 
        :type receiver_address: str
        :param sender_name: 寄件人姓名。 
        :type sender_name: str
        :param sender_phone: 寄件人电话。 
        :type sender_phone: str
        :param sender_address: 寄件人地址。 
        :type sender_address: str
        :param waybill_number: 条形码运单号。 
        :type waybill_number: str
        :param confidence: 相关字段的置信度信息，取值范围0~1。 置信度越大，表示本次识别的对应字段的可靠性越高，在统计意义上，置信度越大，准确率越高。 置信度由算法给出，不直接等价于对应字段的准确率。 
        :type confidence: object
        """
        
        

        self._code = None
        self._receiver_name = None
        self._receiver_phone = None
        self._receiver_address = None
        self._sender_name = None
        self._sender_phone = None
        self._sender_address = None
        self._waybill_number = None
        self._confidence = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if receiver_name is not None:
            self.receiver_name = receiver_name
        if receiver_phone is not None:
            self.receiver_phone = receiver_phone
        if receiver_address is not None:
            self.receiver_address = receiver_address
        if sender_name is not None:
            self.sender_name = sender_name
        if sender_phone is not None:
            self.sender_phone = sender_phone
        if sender_address is not None:
            self.sender_address = sender_address
        if waybill_number is not None:
            self.waybill_number = waybill_number
        if confidence is not None:
            self.confidence = confidence

    @property
    def code(self):
        """Gets the code of this WaybillElectronicResult.

        三段码。 

        :return: The code of this WaybillElectronicResult.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this WaybillElectronicResult.

        三段码。 

        :param code: The code of this WaybillElectronicResult.
        :type code: str
        """
        self._code = code

    @property
    def receiver_name(self):
        """Gets the receiver_name of this WaybillElectronicResult.

        收件人姓名。 

        :return: The receiver_name of this WaybillElectronicResult.
        :rtype: str
        """
        return self._receiver_name

    @receiver_name.setter
    def receiver_name(self, receiver_name):
        """Sets the receiver_name of this WaybillElectronicResult.

        收件人姓名。 

        :param receiver_name: The receiver_name of this WaybillElectronicResult.
        :type receiver_name: str
        """
        self._receiver_name = receiver_name

    @property
    def receiver_phone(self):
        """Gets the receiver_phone of this WaybillElectronicResult.

        收件人电话。 

        :return: The receiver_phone of this WaybillElectronicResult.
        :rtype: str
        """
        return self._receiver_phone

    @receiver_phone.setter
    def receiver_phone(self, receiver_phone):
        """Sets the receiver_phone of this WaybillElectronicResult.

        收件人电话。 

        :param receiver_phone: The receiver_phone of this WaybillElectronicResult.
        :type receiver_phone: str
        """
        self._receiver_phone = receiver_phone

    @property
    def receiver_address(self):
        """Gets the receiver_address of this WaybillElectronicResult.

        收件人地址。 

        :return: The receiver_address of this WaybillElectronicResult.
        :rtype: str
        """
        return self._receiver_address

    @receiver_address.setter
    def receiver_address(self, receiver_address):
        """Sets the receiver_address of this WaybillElectronicResult.

        收件人地址。 

        :param receiver_address: The receiver_address of this WaybillElectronicResult.
        :type receiver_address: str
        """
        self._receiver_address = receiver_address

    @property
    def sender_name(self):
        """Gets the sender_name of this WaybillElectronicResult.

        寄件人姓名。 

        :return: The sender_name of this WaybillElectronicResult.
        :rtype: str
        """
        return self._sender_name

    @sender_name.setter
    def sender_name(self, sender_name):
        """Sets the sender_name of this WaybillElectronicResult.

        寄件人姓名。 

        :param sender_name: The sender_name of this WaybillElectronicResult.
        :type sender_name: str
        """
        self._sender_name = sender_name

    @property
    def sender_phone(self):
        """Gets the sender_phone of this WaybillElectronicResult.

        寄件人电话。 

        :return: The sender_phone of this WaybillElectronicResult.
        :rtype: str
        """
        return self._sender_phone

    @sender_phone.setter
    def sender_phone(self, sender_phone):
        """Sets the sender_phone of this WaybillElectronicResult.

        寄件人电话。 

        :param sender_phone: The sender_phone of this WaybillElectronicResult.
        :type sender_phone: str
        """
        self._sender_phone = sender_phone

    @property
    def sender_address(self):
        """Gets the sender_address of this WaybillElectronicResult.

        寄件人地址。 

        :return: The sender_address of this WaybillElectronicResult.
        :rtype: str
        """
        return self._sender_address

    @sender_address.setter
    def sender_address(self, sender_address):
        """Sets the sender_address of this WaybillElectronicResult.

        寄件人地址。 

        :param sender_address: The sender_address of this WaybillElectronicResult.
        :type sender_address: str
        """
        self._sender_address = sender_address

    @property
    def waybill_number(self):
        """Gets the waybill_number of this WaybillElectronicResult.

        条形码运单号。 

        :return: The waybill_number of this WaybillElectronicResult.
        :rtype: str
        """
        return self._waybill_number

    @waybill_number.setter
    def waybill_number(self, waybill_number):
        """Sets the waybill_number of this WaybillElectronicResult.

        条形码运单号。 

        :param waybill_number: The waybill_number of this WaybillElectronicResult.
        :type waybill_number: str
        """
        self._waybill_number = waybill_number

    @property
    def confidence(self):
        """Gets the confidence of this WaybillElectronicResult.

        相关字段的置信度信息，取值范围0~1。 置信度越大，表示本次识别的对应字段的可靠性越高，在统计意义上，置信度越大，准确率越高。 置信度由算法给出，不直接等价于对应字段的准确率。 

        :return: The confidence of this WaybillElectronicResult.
        :rtype: object
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this WaybillElectronicResult.

        相关字段的置信度信息，取值范围0~1。 置信度越大，表示本次识别的对应字段的可靠性越高，在统计意义上，置信度越大，准确率越高。 置信度由算法给出，不直接等价于对应字段的准确率。 

        :param confidence: The confidence of this WaybillElectronicResult.
        :type confidence: object
        """
        self._confidence = confidence

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
        if not isinstance(other, WaybillElectronicResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
