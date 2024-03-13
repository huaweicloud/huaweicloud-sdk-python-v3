# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DisassociateGeipSegmentInstanceResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_id': 'str',
        'global_eip_segment': 'ShortGlobalEipSegment',
        'x_request_id': 'str'
    }

    attribute_map = {
        'job_id': 'job_id',
        'global_eip_segment': 'global_eip_segment',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, job_id=None, global_eip_segment=None, x_request_id=None):
        """DisassociateGeipSegmentInstanceResponse

        The model defined in huaweicloud sdk

        :param job_id: 本次请求的job id
        :type job_id: str
        :param global_eip_segment: 
        :type global_eip_segment: :class:`huaweicloudsdkgeip.v3.ShortGlobalEipSegment`
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(DisassociateGeipSegmentInstanceResponse, self).__init__()

        self._job_id = None
        self._global_eip_segment = None
        self._x_request_id = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if global_eip_segment is not None:
            self.global_eip_segment = global_eip_segment
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def job_id(self):
        """Gets the job_id of this DisassociateGeipSegmentInstanceResponse.

        本次请求的job id

        :return: The job_id of this DisassociateGeipSegmentInstanceResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this DisassociateGeipSegmentInstanceResponse.

        本次请求的job id

        :param job_id: The job_id of this DisassociateGeipSegmentInstanceResponse.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def global_eip_segment(self):
        """Gets the global_eip_segment of this DisassociateGeipSegmentInstanceResponse.

        :return: The global_eip_segment of this DisassociateGeipSegmentInstanceResponse.
        :rtype: :class:`huaweicloudsdkgeip.v3.ShortGlobalEipSegment`
        """
        return self._global_eip_segment

    @global_eip_segment.setter
    def global_eip_segment(self, global_eip_segment):
        """Sets the global_eip_segment of this DisassociateGeipSegmentInstanceResponse.

        :param global_eip_segment: The global_eip_segment of this DisassociateGeipSegmentInstanceResponse.
        :type global_eip_segment: :class:`huaweicloudsdkgeip.v3.ShortGlobalEipSegment`
        """
        self._global_eip_segment = global_eip_segment

    @property
    def x_request_id(self):
        """Gets the x_request_id of this DisassociateGeipSegmentInstanceResponse.

        :return: The x_request_id of this DisassociateGeipSegmentInstanceResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        """Sets the x_request_id of this DisassociateGeipSegmentInstanceResponse.

        :param x_request_id: The x_request_id of this DisassociateGeipSegmentInstanceResponse.
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
        if not isinstance(other, DisassociateGeipSegmentInstanceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
