# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BandwidthInfoResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'bandwidth_name': 'str',
        'bandwidth_number': 'int',
        'bandwidth_type': 'str',
        'bandwidth_id': 'str'
    }

    attribute_map = {
        'bandwidth_name': 'bandwidth_name',
        'bandwidth_number': 'bandwidth_number',
        'bandwidth_type': 'bandwidth_type',
        'bandwidth_id': 'bandwidth_id'
    }

    def __init__(self, bandwidth_name=None, bandwidth_number=None, bandwidth_type=None, bandwidth_id=None):
        """BandwidthInfoResp

        The model defined in huaweicloud sdk

        :param bandwidth_name: 带宽名称
        :type bandwidth_name: str
        :param bandwidth_number: 带宽大小
        :type bandwidth_number: int
        :param bandwidth_type: 带宽类型
        :type bandwidth_type: str
        :param bandwidth_id: 带宽id
        :type bandwidth_id: str
        """
        
        

        self._bandwidth_name = None
        self._bandwidth_number = None
        self._bandwidth_type = None
        self._bandwidth_id = None
        self.discriminator = None

        if bandwidth_name is not None:
            self.bandwidth_name = bandwidth_name
        if bandwidth_number is not None:
            self.bandwidth_number = bandwidth_number
        if bandwidth_type is not None:
            self.bandwidth_type = bandwidth_type
        if bandwidth_id is not None:
            self.bandwidth_id = bandwidth_id

    @property
    def bandwidth_name(self):
        """Gets the bandwidth_name of this BandwidthInfoResp.

        带宽名称

        :return: The bandwidth_name of this BandwidthInfoResp.
        :rtype: str
        """
        return self._bandwidth_name

    @bandwidth_name.setter
    def bandwidth_name(self, bandwidth_name):
        """Sets the bandwidth_name of this BandwidthInfoResp.

        带宽名称

        :param bandwidth_name: The bandwidth_name of this BandwidthInfoResp.
        :type bandwidth_name: str
        """
        self._bandwidth_name = bandwidth_name

    @property
    def bandwidth_number(self):
        """Gets the bandwidth_number of this BandwidthInfoResp.

        带宽大小

        :return: The bandwidth_number of this BandwidthInfoResp.
        :rtype: int
        """
        return self._bandwidth_number

    @bandwidth_number.setter
    def bandwidth_number(self, bandwidth_number):
        """Sets the bandwidth_number of this BandwidthInfoResp.

        带宽大小

        :param bandwidth_number: The bandwidth_number of this BandwidthInfoResp.
        :type bandwidth_number: int
        """
        self._bandwidth_number = bandwidth_number

    @property
    def bandwidth_type(self):
        """Gets the bandwidth_type of this BandwidthInfoResp.

        带宽类型

        :return: The bandwidth_type of this BandwidthInfoResp.
        :rtype: str
        """
        return self._bandwidth_type

    @bandwidth_type.setter
    def bandwidth_type(self, bandwidth_type):
        """Sets the bandwidth_type of this BandwidthInfoResp.

        带宽类型

        :param bandwidth_type: The bandwidth_type of this BandwidthInfoResp.
        :type bandwidth_type: str
        """
        self._bandwidth_type = bandwidth_type

    @property
    def bandwidth_id(self):
        """Gets the bandwidth_id of this BandwidthInfoResp.

        带宽id

        :return: The bandwidth_id of this BandwidthInfoResp.
        :rtype: str
        """
        return self._bandwidth_id

    @bandwidth_id.setter
    def bandwidth_id(self, bandwidth_id):
        """Sets the bandwidth_id of this BandwidthInfoResp.

        带宽id

        :param bandwidth_id: The bandwidth_id of this BandwidthInfoResp.
        :type bandwidth_id: str
        """
        self._bandwidth_id = bandwidth_id

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
        if not isinstance(other, BandwidthInfoResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
