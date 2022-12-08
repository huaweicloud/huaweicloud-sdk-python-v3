# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchCreatePublicipsV2RequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'bandwidth': 'BatchBandwidth',
        'publicip': 'BatchPublicIp',
        'publicip_number': 'int',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'bandwidth': 'bandwidth',
        'publicip': 'publicip',
        'publicip_number': 'publicip_number',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, bandwidth=None, publicip=None, publicip_number=None, enterprise_project_id=None):
        """BatchCreatePublicipsV2RequestBody

        The model defined in huaweicloud sdk

        :param bandwidth: 
        :type bandwidth: :class:`huaweicloudsdkeip.v2.BatchBandwidth`
        :param publicip: 
        :type publicip: :class:`huaweicloudsdkeip.v2.BatchPublicIp`
        :param publicip_number: 批量创建EIP的个数
        :type publicip_number: int
        :param enterprise_project_id: 企业项目id
        :type enterprise_project_id: str
        """
        
        

        self._bandwidth = None
        self._publicip = None
        self._publicip_number = None
        self._enterprise_project_id = None
        self.discriminator = None

        self.bandwidth = bandwidth
        self.publicip = publicip
        self.publicip_number = publicip_number
        self.enterprise_project_id = enterprise_project_id

    @property
    def bandwidth(self):
        """Gets the bandwidth of this BatchCreatePublicipsV2RequestBody.

        :return: The bandwidth of this BatchCreatePublicipsV2RequestBody.
        :rtype: :class:`huaweicloudsdkeip.v2.BatchBandwidth`
        """
        return self._bandwidth

    @bandwidth.setter
    def bandwidth(self, bandwidth):
        """Sets the bandwidth of this BatchCreatePublicipsV2RequestBody.

        :param bandwidth: The bandwidth of this BatchCreatePublicipsV2RequestBody.
        :type bandwidth: :class:`huaweicloudsdkeip.v2.BatchBandwidth`
        """
        self._bandwidth = bandwidth

    @property
    def publicip(self):
        """Gets the publicip of this BatchCreatePublicipsV2RequestBody.

        :return: The publicip of this BatchCreatePublicipsV2RequestBody.
        :rtype: :class:`huaweicloudsdkeip.v2.BatchPublicIp`
        """
        return self._publicip

    @publicip.setter
    def publicip(self, publicip):
        """Sets the publicip of this BatchCreatePublicipsV2RequestBody.

        :param publicip: The publicip of this BatchCreatePublicipsV2RequestBody.
        :type publicip: :class:`huaweicloudsdkeip.v2.BatchPublicIp`
        """
        self._publicip = publicip

    @property
    def publicip_number(self):
        """Gets the publicip_number of this BatchCreatePublicipsV2RequestBody.

        批量创建EIP的个数

        :return: The publicip_number of this BatchCreatePublicipsV2RequestBody.
        :rtype: int
        """
        return self._publicip_number

    @publicip_number.setter
    def publicip_number(self, publicip_number):
        """Sets the publicip_number of this BatchCreatePublicipsV2RequestBody.

        批量创建EIP的个数

        :param publicip_number: The publicip_number of this BatchCreatePublicipsV2RequestBody.
        :type publicip_number: int
        """
        self._publicip_number = publicip_number

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this BatchCreatePublicipsV2RequestBody.

        企业项目id

        :return: The enterprise_project_id of this BatchCreatePublicipsV2RequestBody.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this BatchCreatePublicipsV2RequestBody.

        企业项目id

        :param enterprise_project_id: The enterprise_project_id of this BatchCreatePublicipsV2RequestBody.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, BatchCreatePublicipsV2RequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
