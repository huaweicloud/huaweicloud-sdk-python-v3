# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DisasterFailoverReqBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_support_restore': 'bool',
        'disaster_type': 'str'
    }

    attribute_map = {
        'is_support_restore': 'is_support_restore',
        'disaster_type': 'disaster_type'
    }

    def __init__(self, is_support_restore=None, disaster_type=None):
        r"""DisasterFailoverReqBody

        The model defined in huaweicloud sdk

        :param is_support_restore: 是否支持容灾回切(仅支持数据库版本大于等于3.100)   - true支持   - false不支持(默认false)
        :type is_support_restore: bool
        :param disaster_type: 容灾类型。
        :type disaster_type: str
        """
        
        

        self._is_support_restore = None
        self._disaster_type = None
        self.discriminator = None

        if is_support_restore is not None:
            self.is_support_restore = is_support_restore
        self.disaster_type = disaster_type

    @property
    def is_support_restore(self):
        r"""Gets the is_support_restore of this DisasterFailoverReqBody.

        是否支持容灾回切(仅支持数据库版本大于等于3.100)   - true支持   - false不支持(默认false)

        :return: The is_support_restore of this DisasterFailoverReqBody.
        :rtype: bool
        """
        return self._is_support_restore

    @is_support_restore.setter
    def is_support_restore(self, is_support_restore):
        r"""Sets the is_support_restore of this DisasterFailoverReqBody.

        是否支持容灾回切(仅支持数据库版本大于等于3.100)   - true支持   - false不支持(默认false)

        :param is_support_restore: The is_support_restore of this DisasterFailoverReqBody.
        :type is_support_restore: bool
        """
        self._is_support_restore = is_support_restore

    @property
    def disaster_type(self):
        r"""Gets the disaster_type of this DisasterFailoverReqBody.

        容灾类型。

        :return: The disaster_type of this DisasterFailoverReqBody.
        :rtype: str
        """
        return self._disaster_type

    @disaster_type.setter
    def disaster_type(self, disaster_type):
        r"""Sets the disaster_type of this DisasterFailoverReqBody.

        容灾类型。

        :param disaster_type: The disaster_type of this DisasterFailoverReqBody.
        :type disaster_type: str
        """
        self._disaster_type = disaster_type

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
        if not isinstance(other, DisasterFailoverReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
