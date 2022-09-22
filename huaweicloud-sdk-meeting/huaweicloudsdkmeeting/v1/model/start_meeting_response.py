# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StartMeetingResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'uuid': 'str',
        'region_ip': 'str'
    }

    attribute_map = {
        'uuid': 'uuid',
        'region_ip': 'regionIP'
    }

    def __init__(self, uuid=None, region_ip=None):
        """StartMeetingResponse

        The model defined in huaweicloud sdk

        :param uuid: uuid。 &gt; 废弃参数，请勿使用。 
        :type uuid: str
        :param region_ip: 会议所在区域的公网IP地址。
        :type region_ip: str
        """
        
        super(StartMeetingResponse, self).__init__()

        self._uuid = None
        self._region_ip = None
        self.discriminator = None

        if uuid is not None:
            self.uuid = uuid
        if region_ip is not None:
            self.region_ip = region_ip

    @property
    def uuid(self):
        """Gets the uuid of this StartMeetingResponse.

        uuid。 > 废弃参数，请勿使用。 

        :return: The uuid of this StartMeetingResponse.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this StartMeetingResponse.

        uuid。 > 废弃参数，请勿使用。 

        :param uuid: The uuid of this StartMeetingResponse.
        :type uuid: str
        """
        self._uuid = uuid

    @property
    def region_ip(self):
        """Gets the region_ip of this StartMeetingResponse.

        会议所在区域的公网IP地址。

        :return: The region_ip of this StartMeetingResponse.
        :rtype: str
        """
        return self._region_ip

    @region_ip.setter
    def region_ip(self, region_ip):
        """Sets the region_ip of this StartMeetingResponse.

        会议所在区域的公网IP地址。

        :param region_ip: The region_ip of this StartMeetingResponse.
        :type region_ip: str
        """
        self._region_ip = region_ip

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
        if not isinstance(other, StartMeetingResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
