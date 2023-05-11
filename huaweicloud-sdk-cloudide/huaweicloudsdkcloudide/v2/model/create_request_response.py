# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateRequestResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'request_id': 'str',
        'status': 'RequestStatus',
        'dispatched_task_number': 'int'
    }

    attribute_map = {
        'request_id': 'request_id',
        'status': 'status',
        'dispatched_task_number': 'dispatched_task_number'
    }

    def __init__(self, request_id=None, status=None, dispatched_task_number=None):
        """CreateRequestResponse

        The model defined in huaweicloud sdk

        :param request_id: the unique id of the request
        :type request_id: str
        :param status: 
        :type status: :class:`huaweicloudsdkcloudide.v2.RequestStatus`
        :param dispatched_task_number: the number of tasks dispatched successfully
        :type dispatched_task_number: int
        """
        
        super(CreateRequestResponse, self).__init__()

        self._request_id = None
        self._status = None
        self._dispatched_task_number = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if status is not None:
            self.status = status
        if dispatched_task_number is not None:
            self.dispatched_task_number = dispatched_task_number

    @property
    def request_id(self):
        """Gets the request_id of this CreateRequestResponse.

        the unique id of the request

        :return: The request_id of this CreateRequestResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this CreateRequestResponse.

        the unique id of the request

        :param request_id: The request_id of this CreateRequestResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def status(self):
        """Gets the status of this CreateRequestResponse.

        :return: The status of this CreateRequestResponse.
        :rtype: :class:`huaweicloudsdkcloudide.v2.RequestStatus`
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CreateRequestResponse.

        :param status: The status of this CreateRequestResponse.
        :type status: :class:`huaweicloudsdkcloudide.v2.RequestStatus`
        """
        self._status = status

    @property
    def dispatched_task_number(self):
        """Gets the dispatched_task_number of this CreateRequestResponse.

        the number of tasks dispatched successfully

        :return: The dispatched_task_number of this CreateRequestResponse.
        :rtype: int
        """
        return self._dispatched_task_number

    @dispatched_task_number.setter
    def dispatched_task_number(self, dispatched_task_number):
        """Sets the dispatched_task_number of this CreateRequestResponse.

        the number of tasks dispatched successfully

        :param dispatched_task_number: The dispatched_task_number of this CreateRequestResponse.
        :type dispatched_task_number: int
        """
        self._dispatched_task_number = dispatched_task_number

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
        if not isinstance(other, CreateRequestResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
