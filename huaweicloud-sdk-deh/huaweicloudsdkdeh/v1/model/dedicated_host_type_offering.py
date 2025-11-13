# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DedicatedHostTypeOffering:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'availability_zone': 'str',
        'status': 'str'
    }

    attribute_map = {
        'availability_zone': 'availability_zone',
        'status': 'status'
    }

    def __init__(self, availability_zone=None, status=None):
        r"""DedicatedHostTypeOffering

        The model defined in huaweicloud sdk

        :param availability_zone: 
        :type availability_zone: str
        :param status: 
        :type status: str
        """
        
        

        self._availability_zone = None
        self._status = None
        self.discriminator = None

        if availability_zone is not None:
            self.availability_zone = availability_zone
        if status is not None:
            self.status = status

    @property
    def availability_zone(self):
        r"""Gets the availability_zone of this DedicatedHostTypeOffering.

        :return: The availability_zone of this DedicatedHostTypeOffering.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        r"""Sets the availability_zone of this DedicatedHostTypeOffering.

        :param availability_zone: The availability_zone of this DedicatedHostTypeOffering.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def status(self):
        r"""Gets the status of this DedicatedHostTypeOffering.

        :return: The status of this DedicatedHostTypeOffering.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this DedicatedHostTypeOffering.

        :param status: The status of this DedicatedHostTypeOffering.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, DedicatedHostTypeOffering):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
