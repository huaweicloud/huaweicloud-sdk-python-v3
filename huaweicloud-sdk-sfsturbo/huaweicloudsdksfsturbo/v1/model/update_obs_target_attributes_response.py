# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateObsTargetAttributesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'target_id': 'str',
        'attributes': 'ObsTargetAttributes',
        'x_request_id': 'str'
    }

    attribute_map = {
        'target_id': 'target_id',
        'attributes': 'attributes',
        'x_request_id': 'X-request-id'
    }

    def __init__(self, target_id=None, attributes=None, x_request_id=None):
        r"""UpdateObsTargetAttributesResponse

        The model defined in huaweicloud sdk

        :param target_id: 绑定关系Id
        :type target_id: str
        :param attributes: 
        :type attributes: :class:`huaweicloudsdksfsturbo.v1.ObsTargetAttributes`
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(UpdateObsTargetAttributesResponse, self).__init__()

        self._target_id = None
        self._attributes = None
        self._x_request_id = None
        self.discriminator = None

        if target_id is not None:
            self.target_id = target_id
        if attributes is not None:
            self.attributes = attributes
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def target_id(self):
        r"""Gets the target_id of this UpdateObsTargetAttributesResponse.

        绑定关系Id

        :return: The target_id of this UpdateObsTargetAttributesResponse.
        :rtype: str
        """
        return self._target_id

    @target_id.setter
    def target_id(self, target_id):
        r"""Sets the target_id of this UpdateObsTargetAttributesResponse.

        绑定关系Id

        :param target_id: The target_id of this UpdateObsTargetAttributesResponse.
        :type target_id: str
        """
        self._target_id = target_id

    @property
    def attributes(self):
        r"""Gets the attributes of this UpdateObsTargetAttributesResponse.

        :return: The attributes of this UpdateObsTargetAttributesResponse.
        :rtype: :class:`huaweicloudsdksfsturbo.v1.ObsTargetAttributes`
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        r"""Sets the attributes of this UpdateObsTargetAttributesResponse.

        :param attributes: The attributes of this UpdateObsTargetAttributesResponse.
        :type attributes: :class:`huaweicloudsdksfsturbo.v1.ObsTargetAttributes`
        """
        self._attributes = attributes

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this UpdateObsTargetAttributesResponse.

        :return: The x_request_id of this UpdateObsTargetAttributesResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this UpdateObsTargetAttributesResponse.

        :param x_request_id: The x_request_id of this UpdateObsTargetAttributesResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, UpdateObsTargetAttributesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
