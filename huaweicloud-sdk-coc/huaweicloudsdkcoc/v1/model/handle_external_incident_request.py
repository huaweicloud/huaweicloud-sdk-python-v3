# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HandleExternalIncidentRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'incident_num': 'str',
        'operator': 'str',
        'operate_key': 'str',
        'parameter': 'dict(str, object)'
    }

    attribute_map = {
        'incident_num': 'incident_num',
        'operator': 'operator',
        'operate_key': 'operate_key',
        'parameter': 'parameter'
    }

    def __init__(self, incident_num=None, operator=None, operate_key=None, parameter=None):
        r"""HandleExternalIncidentRequest

        The model defined in huaweicloud sdk

        :param incident_num: 事件单号
        :type incident_num: str
        :param operator: 操作人ID
        :type operator: str
        :param operate_key: 操作类型
        :type operate_key: str
        :param parameter: 入参
        :type parameter: dict(str, object)
        """
        
        

        self._incident_num = None
        self._operator = None
        self._operate_key = None
        self._parameter = None
        self.discriminator = None

        self.incident_num = incident_num
        self.operator = operator
        self.operate_key = operate_key
        if parameter is not None:
            self.parameter = parameter

    @property
    def incident_num(self):
        r"""Gets the incident_num of this HandleExternalIncidentRequest.

        事件单号

        :return: The incident_num of this HandleExternalIncidentRequest.
        :rtype: str
        """
        return self._incident_num

    @incident_num.setter
    def incident_num(self, incident_num):
        r"""Sets the incident_num of this HandleExternalIncidentRequest.

        事件单号

        :param incident_num: The incident_num of this HandleExternalIncidentRequest.
        :type incident_num: str
        """
        self._incident_num = incident_num

    @property
    def operator(self):
        r"""Gets the operator of this HandleExternalIncidentRequest.

        操作人ID

        :return: The operator of this HandleExternalIncidentRequest.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        r"""Sets the operator of this HandleExternalIncidentRequest.

        操作人ID

        :param operator: The operator of this HandleExternalIncidentRequest.
        :type operator: str
        """
        self._operator = operator

    @property
    def operate_key(self):
        r"""Gets the operate_key of this HandleExternalIncidentRequest.

        操作类型

        :return: The operate_key of this HandleExternalIncidentRequest.
        :rtype: str
        """
        return self._operate_key

    @operate_key.setter
    def operate_key(self, operate_key):
        r"""Sets the operate_key of this HandleExternalIncidentRequest.

        操作类型

        :param operate_key: The operate_key of this HandleExternalIncidentRequest.
        :type operate_key: str
        """
        self._operate_key = operate_key

    @property
    def parameter(self):
        r"""Gets the parameter of this HandleExternalIncidentRequest.

        入参

        :return: The parameter of this HandleExternalIncidentRequest.
        :rtype: dict(str, object)
        """
        return self._parameter

    @parameter.setter
    def parameter(self, parameter):
        r"""Sets the parameter of this HandleExternalIncidentRequest.

        入参

        :param parameter: The parameter of this HandleExternalIncidentRequest.
        :type parameter: dict(str, object)
        """
        self._parameter = parameter

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
        if not isinstance(other, HandleExternalIncidentRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
