# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddCicdConfigurationResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cicd_id': 'object'
    }

    attribute_map = {
        'cicd_id': 'cicd_id'
    }

    def __init__(self, cicd_id=None):
        r"""AddCicdConfigurationResponse

        The model defined in huaweicloud sdk

        :param cicd_id: **参数解释**： cicd标识 **取值范围**： 字符长度1-128位 
        :type cicd_id: object
        """
        
        super(AddCicdConfigurationResponse, self).__init__()

        self._cicd_id = None
        self.discriminator = None

        if cicd_id is not None:
            self.cicd_id = cicd_id

    @property
    def cicd_id(self):
        r"""Gets the cicd_id of this AddCicdConfigurationResponse.

        **参数解释**： cicd标识 **取值范围**： 字符长度1-128位 

        :return: The cicd_id of this AddCicdConfigurationResponse.
        :rtype: object
        """
        return self._cicd_id

    @cicd_id.setter
    def cicd_id(self, cicd_id):
        r"""Sets the cicd_id of this AddCicdConfigurationResponse.

        **参数解释**： cicd标识 **取值范围**： 字符长度1-128位 

        :param cicd_id: The cicd_id of this AddCicdConfigurationResponse.
        :type cicd_id: object
        """
        self._cicd_id = cicd_id

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
        if not isinstance(other, AddCicdConfigurationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
