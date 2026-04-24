# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SetBucketObjectLockDefaultRetention:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    xml_name = "DefaultRetention"

    sensitive_list = []

    openapi_types = {
        'mode': 'str',
        'days': 'int',
        'years': 'int'
    }

    attribute_map = {
        'mode': 'Mode',
        'days': 'Days',
        'years': 'Years'
    }

    def __init__(self, mode=None, days=None, years=None):
        r"""SetBucketObjectLockDefaultRetention

        The model defined in huaweicloud sdk

        :param mode: Definition: WORM retention policy of a bucket. Constraints: None Range: COMPLIANCE: compliance mode Default value: None 
        :type mode: str
        :param days: Definition: Number of retention days. Constraints: Only one of Days and Years can be set to a value other than 0. The value must be within the allowed range. Range: 1 to 36500 Default value: None 
        :type days: int
        :param years: Definition: Default retention years. Constraints: One year is considered as 365 days, regardless of the leap year. Only one of Days and Years can be set to a value other than 0. The value must be within the allowed range. Range: 1 to 100 Default value: None 
        :type years: int
        """
        
        

        self._mode = None
        self._days = None
        self._years = None
        self.discriminator = None

        self.mode = mode
        if days is not None:
            self.days = days
        if years is not None:
            self.years = years

    @property
    def mode(self):
        r"""Gets the mode of this SetBucketObjectLockDefaultRetention.

        Definition: WORM retention policy of a bucket. Constraints: None Range: COMPLIANCE: compliance mode Default value: None 

        :return: The mode of this SetBucketObjectLockDefaultRetention.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        r"""Sets the mode of this SetBucketObjectLockDefaultRetention.

        Definition: WORM retention policy of a bucket. Constraints: None Range: COMPLIANCE: compliance mode Default value: None 

        :param mode: The mode of this SetBucketObjectLockDefaultRetention.
        :type mode: str
        """
        self._mode = mode

    @property
    def days(self):
        r"""Gets the days of this SetBucketObjectLockDefaultRetention.

        Definition: Number of retention days. Constraints: Only one of Days and Years can be set to a value other than 0. The value must be within the allowed range. Range: 1 to 36500 Default value: None 

        :return: The days of this SetBucketObjectLockDefaultRetention.
        :rtype: int
        """
        return self._days

    @days.setter
    def days(self, days):
        r"""Sets the days of this SetBucketObjectLockDefaultRetention.

        Definition: Number of retention days. Constraints: Only one of Days and Years can be set to a value other than 0. The value must be within the allowed range. Range: 1 to 36500 Default value: None 

        :param days: The days of this SetBucketObjectLockDefaultRetention.
        :type days: int
        """
        self._days = days

    @property
    def years(self):
        r"""Gets the years of this SetBucketObjectLockDefaultRetention.

        Definition: Default retention years. Constraints: One year is considered as 365 days, regardless of the leap year. Only one of Days and Years can be set to a value other than 0. The value must be within the allowed range. Range: 1 to 100 Default value: None 

        :return: The years of this SetBucketObjectLockDefaultRetention.
        :rtype: int
        """
        return self._years

    @years.setter
    def years(self, years):
        r"""Sets the years of this SetBucketObjectLockDefaultRetention.

        Definition: Default retention years. Constraints: One year is considered as 365 days, regardless of the leap year. Only one of Days and Years can be set to a value other than 0. The value must be within the allowed range. Range: 1 to 100 Default value: None 

        :param years: The years of this SetBucketObjectLockDefaultRetention.
        :type years: int
        """
        self._years = years

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
        if not isinstance(other, SetBucketObjectLockDefaultRetention):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
