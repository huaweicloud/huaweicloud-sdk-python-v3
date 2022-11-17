# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConfCtlRecordInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'operate_time': 'int',
        'operate_source': 'str',
        'operator': 'str',
        'operate_code': 'str',
        'operation_object': 'str',
        'operate_result': 'str',
        'detail': 'str'
    }

    attribute_map = {
        'operate_time': 'operateTime',
        'operate_source': 'operateSource',
        'operator': 'operator',
        'operate_code': 'operateCode',
        'operation_object': 'operationObject',
        'operate_result': 'operateResult',
        'detail': 'detail'
    }

    def __init__(self, operate_time=None, operate_source=None, operator=None, operate_code=None, operation_object=None, operate_result=None, detail=None):
        """ConfCtlRecordInfo

        The model defined in huaweicloud sdk

        :param operate_time: 操作时间（UTC时间，单位毫秒）。
        :type operate_time: int
        :param operate_source: 操作来源。
        :type operate_source: str
        :param operator: 操作者。
        :type operator: str
        :param operate_code: 操作描述。
        :type operate_code: str
        :param operation_object: 被操作对象。
        :type operation_object: str
        :param operate_result: 操作结果。
        :type operate_result: str
        :param detail: 详情。
        :type detail: str
        """
        
        

        self._operate_time = None
        self._operate_source = None
        self._operator = None
        self._operate_code = None
        self._operation_object = None
        self._operate_result = None
        self._detail = None
        self.discriminator = None

        if operate_time is not None:
            self.operate_time = operate_time
        if operate_source is not None:
            self.operate_source = operate_source
        if operator is not None:
            self.operator = operator
        if operate_code is not None:
            self.operate_code = operate_code
        if operation_object is not None:
            self.operation_object = operation_object
        if operate_result is not None:
            self.operate_result = operate_result
        if detail is not None:
            self.detail = detail

    @property
    def operate_time(self):
        """Gets the operate_time of this ConfCtlRecordInfo.

        操作时间（UTC时间，单位毫秒）。

        :return: The operate_time of this ConfCtlRecordInfo.
        :rtype: int
        """
        return self._operate_time

    @operate_time.setter
    def operate_time(self, operate_time):
        """Sets the operate_time of this ConfCtlRecordInfo.

        操作时间（UTC时间，单位毫秒）。

        :param operate_time: The operate_time of this ConfCtlRecordInfo.
        :type operate_time: int
        """
        self._operate_time = operate_time

    @property
    def operate_source(self):
        """Gets the operate_source of this ConfCtlRecordInfo.

        操作来源。

        :return: The operate_source of this ConfCtlRecordInfo.
        :rtype: str
        """
        return self._operate_source

    @operate_source.setter
    def operate_source(self, operate_source):
        """Sets the operate_source of this ConfCtlRecordInfo.

        操作来源。

        :param operate_source: The operate_source of this ConfCtlRecordInfo.
        :type operate_source: str
        """
        self._operate_source = operate_source

    @property
    def operator(self):
        """Gets the operator of this ConfCtlRecordInfo.

        操作者。

        :return: The operator of this ConfCtlRecordInfo.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this ConfCtlRecordInfo.

        操作者。

        :param operator: The operator of this ConfCtlRecordInfo.
        :type operator: str
        """
        self._operator = operator

    @property
    def operate_code(self):
        """Gets the operate_code of this ConfCtlRecordInfo.

        操作描述。

        :return: The operate_code of this ConfCtlRecordInfo.
        :rtype: str
        """
        return self._operate_code

    @operate_code.setter
    def operate_code(self, operate_code):
        """Sets the operate_code of this ConfCtlRecordInfo.

        操作描述。

        :param operate_code: The operate_code of this ConfCtlRecordInfo.
        :type operate_code: str
        """
        self._operate_code = operate_code

    @property
    def operation_object(self):
        """Gets the operation_object of this ConfCtlRecordInfo.

        被操作对象。

        :return: The operation_object of this ConfCtlRecordInfo.
        :rtype: str
        """
        return self._operation_object

    @operation_object.setter
    def operation_object(self, operation_object):
        """Sets the operation_object of this ConfCtlRecordInfo.

        被操作对象。

        :param operation_object: The operation_object of this ConfCtlRecordInfo.
        :type operation_object: str
        """
        self._operation_object = operation_object

    @property
    def operate_result(self):
        """Gets the operate_result of this ConfCtlRecordInfo.

        操作结果。

        :return: The operate_result of this ConfCtlRecordInfo.
        :rtype: str
        """
        return self._operate_result

    @operate_result.setter
    def operate_result(self, operate_result):
        """Sets the operate_result of this ConfCtlRecordInfo.

        操作结果。

        :param operate_result: The operate_result of this ConfCtlRecordInfo.
        :type operate_result: str
        """
        self._operate_result = operate_result

    @property
    def detail(self):
        """Gets the detail of this ConfCtlRecordInfo.

        详情。

        :return: The detail of this ConfCtlRecordInfo.
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this ConfCtlRecordInfo.

        详情。

        :param detail: The detail of this ConfCtlRecordInfo.
        :type detail: str
        """
        self._detail = detail

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
        if not isinstance(other, ConfCtlRecordInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
