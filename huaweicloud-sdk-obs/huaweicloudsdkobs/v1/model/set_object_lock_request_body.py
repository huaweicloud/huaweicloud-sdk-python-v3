# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SetObjectLockRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    xml_name = "Retention"

    sensitive_list = []

    openapi_types = {
        'mode': 'str',
        'retain_until_date': 'object'
    }

    attribute_map = {
        'mode': 'Mode',
        'retain_until_date': 'RetainUntilDate'
    }

    def __init__(self, mode=None, retain_until_date=None):
        r"""SetObjectLockRequestBody

        The model defined in huaweicloud sdk

        :param mode: Definition: Retention policy of the object. Constraints: None Range: COMPLIANCE: compliance mode Default value: None 
        :type mode: str
        :param retain_until_date: Definition: Example: 1435728035000 Constraints: The specified time must be later than the current time and can be extended but not shortened. Range: None Default value: None 
        :type retain_until_date: object
        """
        
        

        self._mode = None
        self._retain_until_date = None
        self.discriminator = None

        if mode is not None:
            self.mode = mode
        if retain_until_date is not None:
            self.retain_until_date = retain_until_date

    @property
    def mode(self):
        r"""Gets the mode of this SetObjectLockRequestBody.

        Definition: Retention policy of the object. Constraints: None Range: COMPLIANCE: compliance mode Default value: None 

        :return: The mode of this SetObjectLockRequestBody.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        r"""Sets the mode of this SetObjectLockRequestBody.

        Definition: Retention policy of the object. Constraints: None Range: COMPLIANCE: compliance mode Default value: None 

        :param mode: The mode of this SetObjectLockRequestBody.
        :type mode: str
        """
        self._mode = mode

    @property
    def retain_until_date(self):
        r"""Gets the retain_until_date of this SetObjectLockRequestBody.

        Definition: Example: 1435728035000 Constraints: The specified time must be later than the current time and can be extended but not shortened. Range: None Default value: None 

        :return: The retain_until_date of this SetObjectLockRequestBody.
        :rtype: object
        """
        return self._retain_until_date

    @retain_until_date.setter
    def retain_until_date(self, retain_until_date):
        r"""Sets the retain_until_date of this SetObjectLockRequestBody.

        Definition: Example: 1435728035000 Constraints: The specified time must be later than the current time and can be extended but not shortened. Range: None Default value: None 

        :param retain_until_date: The retain_until_date of this SetObjectLockRequestBody.
        :type retain_until_date: object
        """
        self._retain_until_date = retain_until_date

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
        if not isinstance(other, SetObjectLockRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
