# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetGroupIdReqBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'alternate_identifier': 'AlternateIdentifierDto'
    }

    attribute_map = {
        'alternate_identifier': 'alternate_identifier'
    }

    def __init__(self, alternate_identifier=None):
        r"""GetGroupIdReqBody

        The model defined in huaweicloud sdk

        :param alternate_identifier: 
        :type alternate_identifier: :class:`huaweicloudsdkidentitycenterstore.v1.AlternateIdentifierDto`
        """
        
        

        self._alternate_identifier = None
        self.discriminator = None

        self.alternate_identifier = alternate_identifier

    @property
    def alternate_identifier(self):
        r"""Gets the alternate_identifier of this GetGroupIdReqBody.

        :return: The alternate_identifier of this GetGroupIdReqBody.
        :rtype: :class:`huaweicloudsdkidentitycenterstore.v1.AlternateIdentifierDto`
        """
        return self._alternate_identifier

    @alternate_identifier.setter
    def alternate_identifier(self, alternate_identifier):
        r"""Sets the alternate_identifier of this GetGroupIdReqBody.

        :param alternate_identifier: The alternate_identifier of this GetGroupIdReqBody.
        :type alternate_identifier: :class:`huaweicloudsdkidentitycenterstore.v1.AlternateIdentifierDto`
        """
        self._alternate_identifier = alternate_identifier

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
        if not isinstance(other, GetGroupIdReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
