# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateSubnetRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vpc_id': 'str',
        'subnet_id': 'str',
        'body': 'UpdateSubnetRequestBody'
    }

    attribute_map = {
        'vpc_id': 'vpc_id',
        'subnet_id': 'subnet_id',
        'body': 'body'
    }

    def __init__(self, vpc_id=None, subnet_id=None, body=None):
        """UpdateSubnetRequest

        The model defined in huaweicloud sdk

        :param vpc_id: 子网对应的vpc_id
        :type vpc_id: str
        :param subnet_id: 子网ID
        :type subnet_id: str
        :param body: Body of the UpdateSubnetRequest
        :type body: :class:`huaweicloudsdkvpc.v2.UpdateSubnetRequestBody`
        """
        
        

        self._vpc_id = None
        self._subnet_id = None
        self._body = None
        self.discriminator = None

        self.vpc_id = vpc_id
        self.subnet_id = subnet_id
        if body is not None:
            self.body = body

    @property
    def vpc_id(self):
        """Gets the vpc_id of this UpdateSubnetRequest.

        子网对应的vpc_id

        :return: The vpc_id of this UpdateSubnetRequest.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this UpdateSubnetRequest.

        子网对应的vpc_id

        :param vpc_id: The vpc_id of this UpdateSubnetRequest.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        """Gets the subnet_id of this UpdateSubnetRequest.

        子网ID

        :return: The subnet_id of this UpdateSubnetRequest.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this UpdateSubnetRequest.

        子网ID

        :param subnet_id: The subnet_id of this UpdateSubnetRequest.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def body(self):
        """Gets the body of this UpdateSubnetRequest.

        :return: The body of this UpdateSubnetRequest.
        :rtype: :class:`huaweicloudsdkvpc.v2.UpdateSubnetRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateSubnetRequest.

        :param body: The body of this UpdateSubnetRequest.
        :type body: :class:`huaweicloudsdkvpc.v2.UpdateSubnetRequestBody`
        """
        self._body = body

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
        if not isinstance(other, UpdateSubnetRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
