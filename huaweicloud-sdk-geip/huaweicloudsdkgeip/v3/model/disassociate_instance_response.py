# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DisassociateInstanceResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'global_eip': 'UpdateGlobalEip',
        'job_id': 'str',
        'x_request_id': 'str'
    }

    attribute_map = {
        'global_eip': 'global_eip',
        'job_id': 'job_id',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, global_eip=None, job_id=None, x_request_id=None):
        r"""DisassociateInstanceResponse

        The model defined in huaweicloud sdk

        :param global_eip: 
        :type global_eip: :class:`huaweicloudsdkgeip.v3.UpdateGlobalEip`
        :param job_id: 本次请求的job id
        :type job_id: str
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(DisassociateInstanceResponse, self).__init__()

        self._global_eip = None
        self._job_id = None
        self._x_request_id = None
        self.discriminator = None

        if global_eip is not None:
            self.global_eip = global_eip
        if job_id is not None:
            self.job_id = job_id
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def global_eip(self):
        r"""Gets the global_eip of this DisassociateInstanceResponse.

        :return: The global_eip of this DisassociateInstanceResponse.
        :rtype: :class:`huaweicloudsdkgeip.v3.UpdateGlobalEip`
        """
        return self._global_eip

    @global_eip.setter
    def global_eip(self, global_eip):
        r"""Sets the global_eip of this DisassociateInstanceResponse.

        :param global_eip: The global_eip of this DisassociateInstanceResponse.
        :type global_eip: :class:`huaweicloudsdkgeip.v3.UpdateGlobalEip`
        """
        self._global_eip = global_eip

    @property
    def job_id(self):
        r"""Gets the job_id of this DisassociateInstanceResponse.

        本次请求的job id

        :return: The job_id of this DisassociateInstanceResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this DisassociateInstanceResponse.

        本次请求的job id

        :param job_id: The job_id of this DisassociateInstanceResponse.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this DisassociateInstanceResponse.

        :return: The x_request_id of this DisassociateInstanceResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this DisassociateInstanceResponse.

        :param x_request_id: The x_request_id of this DisassociateInstanceResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, DisassociateInstanceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
