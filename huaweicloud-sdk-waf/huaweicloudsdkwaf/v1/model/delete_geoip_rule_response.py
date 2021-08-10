# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteGeoipRuleResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'policyid': 'str',
        'geoip': 'str',
        'white': 'int',
        'description': 'str',
        'timestamp': 'int'
    }

    attribute_map = {
        'id': 'id',
        'policyid': 'policyid',
        'geoip': 'geoip',
        'white': 'white',
        'description': 'description',
        'timestamp': 'timestamp'
    }

    def __init__(self, id=None, policyid=None, geoip=None, white=None, description=None, timestamp=None):
        """DeleteGeoipRuleResponse - a model defined in huaweicloud sdk"""
        
        super(DeleteGeoipRuleResponse, self).__init__()

        self._id = None
        self._policyid = None
        self._geoip = None
        self._white = None
        self._description = None
        self._timestamp = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if policyid is not None:
            self.policyid = policyid
        if geoip is not None:
            self.geoip = geoip
        if white is not None:
            self.white = white
        if description is not None:
            self.description = description
        if timestamp is not None:
            self.timestamp = timestamp

    @property
    def id(self):
        """Gets the id of this DeleteGeoipRuleResponse.

        规则id

        :return: The id of this DeleteGeoipRuleResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DeleteGeoipRuleResponse.

        规则id

        :param id: The id of this DeleteGeoipRuleResponse.
        :type: str
        """
        self._id = id

    @property
    def policyid(self):
        """Gets the policyid of this DeleteGeoipRuleResponse.

        策略id

        :return: The policyid of this DeleteGeoipRuleResponse.
        :rtype: str
        """
        return self._policyid

    @policyid.setter
    def policyid(self, policyid):
        """Sets the policyid of this DeleteGeoipRuleResponse.

        策略id

        :param policyid: The policyid of this DeleteGeoipRuleResponse.
        :type: str
        """
        self._policyid = policyid

    @property
    def geoip(self):
        """Gets the geoip of this DeleteGeoipRuleResponse.

        地理位置封禁区域

        :return: The geoip of this DeleteGeoipRuleResponse.
        :rtype: str
        """
        return self._geoip

    @geoip.setter
    def geoip(self, geoip):
        """Sets the geoip of this DeleteGeoipRuleResponse.

        地理位置封禁区域

        :param geoip: The geoip of this DeleteGeoipRuleResponse.
        :type: str
        """
        self._geoip = geoip

    @property
    def white(self):
        """Gets the white of this DeleteGeoipRuleResponse.

        放行或者拦截（0拦截，1放行）

        :return: The white of this DeleteGeoipRuleResponse.
        :rtype: int
        """
        return self._white

    @white.setter
    def white(self, white):
        """Sets the white of this DeleteGeoipRuleResponse.

        放行或者拦截（0拦截，1放行）

        :param white: The white of this DeleteGeoipRuleResponse.
        :type: int
        """
        self._white = white

    @property
    def description(self):
        """Gets the description of this DeleteGeoipRuleResponse.

        描述

        :return: The description of this DeleteGeoipRuleResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DeleteGeoipRuleResponse.

        描述

        :param description: The description of this DeleteGeoipRuleResponse.
        :type: str
        """
        self._description = description

    @property
    def timestamp(self):
        """Gets the timestamp of this DeleteGeoipRuleResponse.

        创建规则时间戳

        :return: The timestamp of this DeleteGeoipRuleResponse.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this DeleteGeoipRuleResponse.

        创建规则时间戳

        :param timestamp: The timestamp of this DeleteGeoipRuleResponse.
        :type: int
        """
        self._timestamp = timestamp

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
        if not isinstance(other, DeleteGeoipRuleResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
