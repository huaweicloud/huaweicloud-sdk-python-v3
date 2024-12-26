# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowIpsUpdateTimeResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'data': 'list[IpsRuleUpdateTimeVO]',
        'error_code': 'str',
        'error_description': 'str',
        'fail_reason': 'str',
        'job_id': 'str',
        'order_id': 'str',
        'trace_id': 'str'
    }

    attribute_map = {
        'data': 'data',
        'error_code': 'error_code',
        'error_description': 'error_description',
        'fail_reason': 'fail_reason',
        'job_id': 'job_id',
        'order_id': 'order_id',
        'trace_id': 'trace_id'
    }

    def __init__(self, data=None, error_code=None, error_description=None, fail_reason=None, job_id=None, order_id=None, trace_id=None):
        """ShowIpsUpdateTimeResponse

        The model defined in huaweicloud sdk

        :param data: 
        :type data: list[:class:`huaweicloudsdkcfw.v1.IpsRuleUpdateTimeVO`]
        :param error_code: 
        :type error_code: str
        :param error_description: 
        :type error_description: str
        :param fail_reason: 
        :type fail_reason: str
        :param job_id: 
        :type job_id: str
        :param order_id: 
        :type order_id: str
        :param trace_id: 
        :type trace_id: str
        """
        
        super(ShowIpsUpdateTimeResponse, self).__init__()

        self._data = None
        self._error_code = None
        self._error_description = None
        self._fail_reason = None
        self._job_id = None
        self._order_id = None
        self._trace_id = None
        self.discriminator = None

        if data is not None:
            self.data = data
        if error_code is not None:
            self.error_code = error_code
        if error_description is not None:
            self.error_description = error_description
        if fail_reason is not None:
            self.fail_reason = fail_reason
        if job_id is not None:
            self.job_id = job_id
        if order_id is not None:
            self.order_id = order_id
        if trace_id is not None:
            self.trace_id = trace_id

    @property
    def data(self):
        """Gets the data of this ShowIpsUpdateTimeResponse.

        :return: The data of this ShowIpsUpdateTimeResponse.
        :rtype: list[:class:`huaweicloudsdkcfw.v1.IpsRuleUpdateTimeVO`]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this ShowIpsUpdateTimeResponse.

        :param data: The data of this ShowIpsUpdateTimeResponse.
        :type data: list[:class:`huaweicloudsdkcfw.v1.IpsRuleUpdateTimeVO`]
        """
        self._data = data

    @property
    def error_code(self):
        """Gets the error_code of this ShowIpsUpdateTimeResponse.

        :return: The error_code of this ShowIpsUpdateTimeResponse.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this ShowIpsUpdateTimeResponse.

        :param error_code: The error_code of this ShowIpsUpdateTimeResponse.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_description(self):
        """Gets the error_description of this ShowIpsUpdateTimeResponse.

        :return: The error_description of this ShowIpsUpdateTimeResponse.
        :rtype: str
        """
        return self._error_description

    @error_description.setter
    def error_description(self, error_description):
        """Sets the error_description of this ShowIpsUpdateTimeResponse.

        :param error_description: The error_description of this ShowIpsUpdateTimeResponse.
        :type error_description: str
        """
        self._error_description = error_description

    @property
    def fail_reason(self):
        """Gets the fail_reason of this ShowIpsUpdateTimeResponse.

        :return: The fail_reason of this ShowIpsUpdateTimeResponse.
        :rtype: str
        """
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, fail_reason):
        """Sets the fail_reason of this ShowIpsUpdateTimeResponse.

        :param fail_reason: The fail_reason of this ShowIpsUpdateTimeResponse.
        :type fail_reason: str
        """
        self._fail_reason = fail_reason

    @property
    def job_id(self):
        """Gets the job_id of this ShowIpsUpdateTimeResponse.

        :return: The job_id of this ShowIpsUpdateTimeResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this ShowIpsUpdateTimeResponse.

        :param job_id: The job_id of this ShowIpsUpdateTimeResponse.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def order_id(self):
        """Gets the order_id of this ShowIpsUpdateTimeResponse.

        :return: The order_id of this ShowIpsUpdateTimeResponse.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this ShowIpsUpdateTimeResponse.

        :param order_id: The order_id of this ShowIpsUpdateTimeResponse.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def trace_id(self):
        """Gets the trace_id of this ShowIpsUpdateTimeResponse.

        :return: The trace_id of this ShowIpsUpdateTimeResponse.
        :rtype: str
        """
        return self._trace_id

    @trace_id.setter
    def trace_id(self, trace_id):
        """Sets the trace_id of this ShowIpsUpdateTimeResponse.

        :param trace_id: The trace_id of this ShowIpsUpdateTimeResponse.
        :type trace_id: str
        """
        self._trace_id = trace_id

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
        if not isinstance(other, ShowIpsUpdateTimeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
