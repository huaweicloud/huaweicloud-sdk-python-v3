# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEcsSpecificationResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'specification': 'list[EcsSpecificationBean]'
    }

    attribute_map = {
        'specification': 'specification'
    }

    def __init__(self, specification=None):
        """ListEcsSpecificationResponse

        The model defined in huaweicloud sdk

        :param specification: ecs规格集合
        :type specification: list[:class:`huaweicloudsdkdbss.v1.EcsSpecificationBean`]
        """
        
        super(ListEcsSpecificationResponse, self).__init__()

        self._specification = None
        self.discriminator = None

        if specification is not None:
            self.specification = specification

    @property
    def specification(self):
        """Gets the specification of this ListEcsSpecificationResponse.

        ecs规格集合

        :return: The specification of this ListEcsSpecificationResponse.
        :rtype: list[:class:`huaweicloudsdkdbss.v1.EcsSpecificationBean`]
        """
        return self._specification

    @specification.setter
    def specification(self, specification):
        """Sets the specification of this ListEcsSpecificationResponse.

        ecs规格集合

        :param specification: The specification of this ListEcsSpecificationResponse.
        :type specification: list[:class:`huaweicloudsdkdbss.v1.EcsSpecificationBean`]
        """
        self._specification = specification

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
        if not isinstance(other, ListEcsSpecificationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
