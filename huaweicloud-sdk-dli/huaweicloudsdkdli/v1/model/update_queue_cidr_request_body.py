# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateQueueCidrRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cidr_in_vpc': 'str'
    }

    attribute_map = {
        'cidr_in_vpc': 'cidr_in_vpc'
    }

    def __init__(self, cidr_in_vpc=None):
        """UpdateQueueCidrRequestBody

        The model defined in huaweicloud sdk

        :param cidr_in_vpc: 队列虚拟私有云网段。  不同CU规格队列支持的网段范围：  - 4cu:  10.0.0.0/8 ~ 10.255.255.192/26  172.16.0.0/12 ~ 172.31.255.192/26  192.168.0.0/16 ~ 192.168.255.192/26  - 16cu:  10.0.0.0/8 ~ 10.255.255.0/24  172.16.0.0/12 ~ 172.31.255.0/24  192.168.0.0/16 ~ 192.168.255.0/24  - 64cu:  10.0.0.0/8 ~ 10.255.252.0/22  172.16.0.0/12 ~ 172.31.252.0/22  192.168.0.0/16 ~ 192.168.252.0/22  - 128cu:  10.0.0.0/8 ~ 10.255.252.0/21  172.16.0.0/12 ~ 172.31.252.0/21  192.168.0.0/16 ~ 192.168.252.0/21
        :type cidr_in_vpc: str
        """
        
        

        self._cidr_in_vpc = None
        self.discriminator = None

        if cidr_in_vpc is not None:
            self.cidr_in_vpc = cidr_in_vpc

    @property
    def cidr_in_vpc(self):
        """Gets the cidr_in_vpc of this UpdateQueueCidrRequestBody.

        队列虚拟私有云网段。  不同CU规格队列支持的网段范围：  - 4cu:  10.0.0.0/8 ~ 10.255.255.192/26  172.16.0.0/12 ~ 172.31.255.192/26  192.168.0.0/16 ~ 192.168.255.192/26  - 16cu:  10.0.0.0/8 ~ 10.255.255.0/24  172.16.0.0/12 ~ 172.31.255.0/24  192.168.0.0/16 ~ 192.168.255.0/24  - 64cu:  10.0.0.0/8 ~ 10.255.252.0/22  172.16.0.0/12 ~ 172.31.252.0/22  192.168.0.0/16 ~ 192.168.252.0/22  - 128cu:  10.0.0.0/8 ~ 10.255.252.0/21  172.16.0.0/12 ~ 172.31.252.0/21  192.168.0.0/16 ~ 192.168.252.0/21

        :return: The cidr_in_vpc of this UpdateQueueCidrRequestBody.
        :rtype: str
        """
        return self._cidr_in_vpc

    @cidr_in_vpc.setter
    def cidr_in_vpc(self, cidr_in_vpc):
        """Sets the cidr_in_vpc of this UpdateQueueCidrRequestBody.

        队列虚拟私有云网段。  不同CU规格队列支持的网段范围：  - 4cu:  10.0.0.0/8 ~ 10.255.255.192/26  172.16.0.0/12 ~ 172.31.255.192/26  192.168.0.0/16 ~ 192.168.255.192/26  - 16cu:  10.0.0.0/8 ~ 10.255.255.0/24  172.16.0.0/12 ~ 172.31.255.0/24  192.168.0.0/16 ~ 192.168.255.0/24  - 64cu:  10.0.0.0/8 ~ 10.255.252.0/22  172.16.0.0/12 ~ 172.31.252.0/22  192.168.0.0/16 ~ 192.168.252.0/22  - 128cu:  10.0.0.0/8 ~ 10.255.252.0/21  172.16.0.0/12 ~ 172.31.252.0/21  192.168.0.0/16 ~ 192.168.252.0/21

        :param cidr_in_vpc: The cidr_in_vpc of this UpdateQueueCidrRequestBody.
        :type cidr_in_vpc: str
        """
        self._cidr_in_vpc = cidr_in_vpc

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
        if not isinstance(other, UpdateQueueCidrRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
