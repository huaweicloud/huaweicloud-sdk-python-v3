# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OriginRangeBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'range_status': 'str',
        'domain_id': 'str'
    }

    attribute_map = {
        'range_status': 'range_status',
        'domain_id': 'domain_id'
    }

    def __init__(self, range_status=None, domain_id=None):
        r"""OriginRangeBody

        The model defined in huaweicloud sdk

        :param range_status: range状态（\&quot;off\&quot;/\&quot;on\&quot;）
        :type range_status: str
        :param domain_id: 加速域名id。
        :type domain_id: str
        """
        
        

        self._range_status = None
        self._domain_id = None
        self.discriminator = None

        if range_status is not None:
            self.range_status = range_status
        if domain_id is not None:
            self.domain_id = domain_id

    @property
    def range_status(self):
        r"""Gets the range_status of this OriginRangeBody.

        range状态（\"off\"/\"on\"）

        :return: The range_status of this OriginRangeBody.
        :rtype: str
        """
        return self._range_status

    @range_status.setter
    def range_status(self, range_status):
        r"""Sets the range_status of this OriginRangeBody.

        range状态（\"off\"/\"on\"）

        :param range_status: The range_status of this OriginRangeBody.
        :type range_status: str
        """
        self._range_status = range_status

    @property
    def domain_id(self):
        r"""Gets the domain_id of this OriginRangeBody.

        加速域名id。

        :return: The domain_id of this OriginRangeBody.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this OriginRangeBody.

        加速域名id。

        :param domain_id: The domain_id of this OriginRangeBody.
        :type domain_id: str
        """
        self._domain_id = domain_id

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
        if not isinstance(other, OriginRangeBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
