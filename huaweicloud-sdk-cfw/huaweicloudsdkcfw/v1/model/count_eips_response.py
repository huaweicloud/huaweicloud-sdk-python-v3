# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CountEipsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'object_id': 'str',
        'eip_total': 'int',
        'eip_protected': 'int'
    }

    attribute_map = {
        'object_id': 'object_id',
        'eip_total': 'eip_total',
        'eip_protected': 'eip_protected'
    }

    def __init__(self, object_id=None, eip_total=None, eip_protected=None):
        """CountEipsResponse

        The model defined in huaweicloud sdk

        :param object_id: 防护对象ID
        :type object_id: str
        :param eip_total: EIP总数
        :type eip_total: int
        :param eip_protected: EIP防护数
        :type eip_protected: int
        """
        
        super(CountEipsResponse, self).__init__()

        self._object_id = None
        self._eip_total = None
        self._eip_protected = None
        self.discriminator = None

        if object_id is not None:
            self.object_id = object_id
        if eip_total is not None:
            self.eip_total = eip_total
        if eip_protected is not None:
            self.eip_protected = eip_protected

    @property
    def object_id(self):
        """Gets the object_id of this CountEipsResponse.

        防护对象ID

        :return: The object_id of this CountEipsResponse.
        :rtype: str
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        """Sets the object_id of this CountEipsResponse.

        防护对象ID

        :param object_id: The object_id of this CountEipsResponse.
        :type object_id: str
        """
        self._object_id = object_id

    @property
    def eip_total(self):
        """Gets the eip_total of this CountEipsResponse.

        EIP总数

        :return: The eip_total of this CountEipsResponse.
        :rtype: int
        """
        return self._eip_total

    @eip_total.setter
    def eip_total(self, eip_total):
        """Sets the eip_total of this CountEipsResponse.

        EIP总数

        :param eip_total: The eip_total of this CountEipsResponse.
        :type eip_total: int
        """
        self._eip_total = eip_total

    @property
    def eip_protected(self):
        """Gets the eip_protected of this CountEipsResponse.

        EIP防护数

        :return: The eip_protected of this CountEipsResponse.
        :rtype: int
        """
        return self._eip_protected

    @eip_protected.setter
    def eip_protected(self, eip_protected):
        """Sets the eip_protected of this CountEipsResponse.

        EIP防护数

        :param eip_protected: The eip_protected of this CountEipsResponse.
        :type eip_protected: int
        """
        self._eip_protected = eip_protected

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
        if not isinstance(other, CountEipsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
