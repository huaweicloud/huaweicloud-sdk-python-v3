# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteAgencyV5Request:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'agency_id': 'str'
    }

    attribute_map = {
        'agency_id': 'agency_id'
    }

    def __init__(self, agency_id=None):
        r"""DeleteAgencyV5Request

        The model defined in huaweicloud sdk

        :param agency_id: 信任委托ID，长度为1到64个字符，只包含字母、数字和\&quot;-\&quot;的字符串。
        :type agency_id: str
        """
        
        

        self._agency_id = None
        self.discriminator = None

        self.agency_id = agency_id

    @property
    def agency_id(self):
        r"""Gets the agency_id of this DeleteAgencyV5Request.

        信任委托ID，长度为1到64个字符，只包含字母、数字和\"-\"的字符串。

        :return: The agency_id of this DeleteAgencyV5Request.
        :rtype: str
        """
        return self._agency_id

    @agency_id.setter
    def agency_id(self, agency_id):
        r"""Sets the agency_id of this DeleteAgencyV5Request.

        信任委托ID，长度为1到64个字符，只包含字母、数字和\"-\"的字符串。

        :param agency_id: The agency_id of this DeleteAgencyV5Request.
        :type agency_id: str
        """
        self._agency_id = agency_id

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
        if not isinstance(other, DeleteAgencyV5Request):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
