# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Vpc:

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
        'vpc_region': 'str'
    }

    attribute_map = {
        'vpc_id': 'vpc_id',
        'vpc_region': 'vpc_region'
    }

    def __init__(self, vpc_id=None, vpc_region=None):
        r"""Vpc

        The model defined in huaweicloud sdk

        :param vpc_id: 关联VPC的ID。
        :type vpc_id: str
        :param vpc_region: 关联VPC所在的region。
        :type vpc_region: str
        """
        
        

        self._vpc_id = None
        self._vpc_region = None
        self.discriminator = None

        self.vpc_id = vpc_id
        if vpc_region is not None:
            self.vpc_region = vpc_region

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this Vpc.

        关联VPC的ID。

        :return: The vpc_id of this Vpc.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this Vpc.

        关联VPC的ID。

        :param vpc_id: The vpc_id of this Vpc.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def vpc_region(self):
        r"""Gets the vpc_region of this Vpc.

        关联VPC所在的region。

        :return: The vpc_region of this Vpc.
        :rtype: str
        """
        return self._vpc_region

    @vpc_region.setter
    def vpc_region(self, vpc_region):
        r"""Sets the vpc_region of this Vpc.

        关联VPC所在的region。

        :param vpc_region: The vpc_region of this Vpc.
        :type vpc_region: str
        """
        self._vpc_region = vpc_region

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
        if not isinstance(other, Vpc):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
