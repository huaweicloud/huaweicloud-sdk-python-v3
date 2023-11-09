# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateWorkspaceResponse(SdkResponse):

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
        'enterprise_id': 'str',
        'dc_vnc_ip': 'str'
    }

    attribute_map = {
        'job_id': 'job_id',
        'enterprise_id': 'enterprise_id',
        'dc_vnc_ip': 'dc_vnc_ip'
    }

    def __init__(self, job_id=None, enterprise_id=None, dc_vnc_ip=None):
        """UpdateWorkspaceResponse

        The model defined in huaweicloud sdk

        :param job_id: 修改云办公服务属性的任务ID
        :type job_id: str
        :param enterprise_id: 企业ID
        :type enterprise_id: str
        :param dc_vnc_ip: 专线vnc访问的ip
        :type dc_vnc_ip: str
        """
        
        super(UpdateWorkspaceResponse, self).__init__()

        self._job_id = None
        self._enterprise_id = None
        self._dc_vnc_ip = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if enterprise_id is not None:
            self.enterprise_id = enterprise_id
        if dc_vnc_ip is not None:
            self.dc_vnc_ip = dc_vnc_ip

    @property
    def job_id(self):
        """Gets the job_id of this UpdateWorkspaceResponse.

        修改云办公服务属性的任务ID

        :return: The job_id of this UpdateWorkspaceResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this UpdateWorkspaceResponse.

        修改云办公服务属性的任务ID

        :param job_id: The job_id of this UpdateWorkspaceResponse.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def enterprise_id(self):
        """Gets the enterprise_id of this UpdateWorkspaceResponse.

        企业ID

        :return: The enterprise_id of this UpdateWorkspaceResponse.
        :rtype: str
        """
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, enterprise_id):
        """Sets the enterprise_id of this UpdateWorkspaceResponse.

        企业ID

        :param enterprise_id: The enterprise_id of this UpdateWorkspaceResponse.
        :type enterprise_id: str
        """
        self._enterprise_id = enterprise_id

    @property
    def dc_vnc_ip(self):
        """Gets the dc_vnc_ip of this UpdateWorkspaceResponse.

        专线vnc访问的ip

        :return: The dc_vnc_ip of this UpdateWorkspaceResponse.
        :rtype: str
        """
        return self._dc_vnc_ip

    @dc_vnc_ip.setter
    def dc_vnc_ip(self, dc_vnc_ip):
        """Sets the dc_vnc_ip of this UpdateWorkspaceResponse.

        专线vnc访问的ip

        :param dc_vnc_ip: The dc_vnc_ip of this UpdateWorkspaceResponse.
        :type dc_vnc_ip: str
        """
        self._dc_vnc_ip = dc_vnc_ip

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
        if not isinstance(other, UpdateWorkspaceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
