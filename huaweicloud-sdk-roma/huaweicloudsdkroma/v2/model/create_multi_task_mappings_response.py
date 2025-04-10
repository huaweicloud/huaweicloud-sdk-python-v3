# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateMultiTaskMappingsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'mapping_id': 'str'
    }

    attribute_map = {
        'mapping_id': 'mapping_id'
    }

    def __init__(self, mapping_id=None):
        r"""CreateMultiTaskMappingsResponse

        The model defined in huaweicloud sdk

        :param mapping_id: 映射唯一ID
        :type mapping_id: str
        """
        
        super(CreateMultiTaskMappingsResponse, self).__init__()

        self._mapping_id = None
        self.discriminator = None

        if mapping_id is not None:
            self.mapping_id = mapping_id

    @property
    def mapping_id(self):
        r"""Gets the mapping_id of this CreateMultiTaskMappingsResponse.

        映射唯一ID

        :return: The mapping_id of this CreateMultiTaskMappingsResponse.
        :rtype: str
        """
        return self._mapping_id

    @mapping_id.setter
    def mapping_id(self, mapping_id):
        r"""Sets the mapping_id of this CreateMultiTaskMappingsResponse.

        映射唯一ID

        :param mapping_id: The mapping_id of this CreateMultiTaskMappingsResponse.
        :type mapping_id: str
        """
        self._mapping_id = mapping_id

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
        if not isinstance(other, CreateMultiTaskMappingsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
