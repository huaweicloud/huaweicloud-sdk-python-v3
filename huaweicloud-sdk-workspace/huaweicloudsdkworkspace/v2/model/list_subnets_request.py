# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSubnetsRequest:

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
        'availability_zone_id': 'str'
    }

    attribute_map = {
        'vpc_id': 'vpc_id',
        'availability_zone_id': 'availability_zone_id'
    }

    def __init__(self, vpc_id=None, availability_zone_id=None):
        r"""ListSubnetsRequest

        The model defined in huaweicloud sdk

        :param vpc_id: 虚拟私有云ID。
        :type vpc_id: str
        :param availability_zone_id: 可用区id。
        :type availability_zone_id: str
        """
        
        

        self._vpc_id = None
        self._availability_zone_id = None
        self.discriminator = None

        if vpc_id is not None:
            self.vpc_id = vpc_id
        if availability_zone_id is not None:
            self.availability_zone_id = availability_zone_id

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this ListSubnetsRequest.

        虚拟私有云ID。

        :return: The vpc_id of this ListSubnetsRequest.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this ListSubnetsRequest.

        虚拟私有云ID。

        :param vpc_id: The vpc_id of this ListSubnetsRequest.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def availability_zone_id(self):
        r"""Gets the availability_zone_id of this ListSubnetsRequest.

        可用区id。

        :return: The availability_zone_id of this ListSubnetsRequest.
        :rtype: str
        """
        return self._availability_zone_id

    @availability_zone_id.setter
    def availability_zone_id(self, availability_zone_id):
        r"""Sets the availability_zone_id of this ListSubnetsRequest.

        可用区id。

        :param availability_zone_id: The availability_zone_id of this ListSubnetsRequest.
        :type availability_zone_id: str
        """
        self._availability_zone_id = availability_zone_id

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListSubnetsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
