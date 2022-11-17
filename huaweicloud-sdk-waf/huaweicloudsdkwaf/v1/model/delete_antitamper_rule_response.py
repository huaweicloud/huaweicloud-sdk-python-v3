# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteAntitamperRuleResponse(SdkResponse):

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
        'url': 'str',
        'timestamp': 'int'
    }

    attribute_map = {
        'id': 'id',
        'policyid': 'policyid',
        'url': 'url',
        'timestamp': 'timestamp'
    }

    def __init__(self, id=None, policyid=None, url=None, timestamp=None):
        """DeleteAntitamperRuleResponse

        The model defined in huaweicloud sdk

        :param id: 规则id
        :type id: str
        :param policyid: 策略id
        :type policyid: str
        :param url: 防篡改的url
        :type url: str
        :param timestamp: 创建规则的时间戳
        :type timestamp: int
        """
        
        super(DeleteAntitamperRuleResponse, self).__init__()

        self._id = None
        self._policyid = None
        self._url = None
        self._timestamp = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if policyid is not None:
            self.policyid = policyid
        if url is not None:
            self.url = url
        if timestamp is not None:
            self.timestamp = timestamp

    @property
    def id(self):
        """Gets the id of this DeleteAntitamperRuleResponse.

        规则id

        :return: The id of this DeleteAntitamperRuleResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DeleteAntitamperRuleResponse.

        规则id

        :param id: The id of this DeleteAntitamperRuleResponse.
        :type id: str
        """
        self._id = id

    @property
    def policyid(self):
        """Gets the policyid of this DeleteAntitamperRuleResponse.

        策略id

        :return: The policyid of this DeleteAntitamperRuleResponse.
        :rtype: str
        """
        return self._policyid

    @policyid.setter
    def policyid(self, policyid):
        """Sets the policyid of this DeleteAntitamperRuleResponse.

        策略id

        :param policyid: The policyid of this DeleteAntitamperRuleResponse.
        :type policyid: str
        """
        self._policyid = policyid

    @property
    def url(self):
        """Gets the url of this DeleteAntitamperRuleResponse.

        防篡改的url

        :return: The url of this DeleteAntitamperRuleResponse.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this DeleteAntitamperRuleResponse.

        防篡改的url

        :param url: The url of this DeleteAntitamperRuleResponse.
        :type url: str
        """
        self._url = url

    @property
    def timestamp(self):
        """Gets the timestamp of this DeleteAntitamperRuleResponse.

        创建规则的时间戳

        :return: The timestamp of this DeleteAntitamperRuleResponse.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this DeleteAntitamperRuleResponse.

        创建规则的时间戳

        :param timestamp: The timestamp of this DeleteAntitamperRuleResponse.
        :type timestamp: int
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
        if not isinstance(other, DeleteAntitamperRuleResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
