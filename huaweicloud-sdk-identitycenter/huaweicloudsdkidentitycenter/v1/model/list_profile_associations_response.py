# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListProfileAssociationsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'associations': 'list[AssociationDto]'
    }

    attribute_map = {
        'associations': 'associations'
    }

    def __init__(self, associations=None):
        """ListProfileAssociationsResponse

        The model defined in huaweicloud sdk

        :param associations: 
        :type associations: list[:class:`huaweicloudsdkidentitycenter.v1.AssociationDto`]
        """
        
        super(ListProfileAssociationsResponse, self).__init__()

        self._associations = None
        self.discriminator = None

        if associations is not None:
            self.associations = associations

    @property
    def associations(self):
        """Gets the associations of this ListProfileAssociationsResponse.

        :return: The associations of this ListProfileAssociationsResponse.
        :rtype: list[:class:`huaweicloudsdkidentitycenter.v1.AssociationDto`]
        """
        return self._associations

    @associations.setter
    def associations(self, associations):
        """Sets the associations of this ListProfileAssociationsResponse.

        :param associations: The associations of this ListProfileAssociationsResponse.
        :type associations: list[:class:`huaweicloudsdkidentitycenter.v1.AssociationDto`]
        """
        self._associations = associations

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
        if not isinstance(other, ListProfileAssociationsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
