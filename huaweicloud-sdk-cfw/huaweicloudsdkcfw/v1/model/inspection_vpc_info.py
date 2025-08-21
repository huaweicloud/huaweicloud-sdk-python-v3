# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InspectionVpcInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'inspection_vpc_id': 'str',
        'name': 'str'
    }

    attribute_map = {
        'inspection_vpc_id': 'inspection_vpc_id',
        'name': 'name'
    }

    def __init__(self, inspection_vpc_id=None, name=None):
        r"""InspectionVpcInfo

        The model defined in huaweicloud sdk

        :param inspection_vpc_id: **参数解释**： 引流VPC  **取值范围**： 不涉及
        :type inspection_vpc_id: str
        :param name: **参数解释**： 引流VPC  **取值范围**： 不涉及
        :type name: str
        """
        
        

        self._inspection_vpc_id = None
        self._name = None
        self.discriminator = None

        if inspection_vpc_id is not None:
            self.inspection_vpc_id = inspection_vpc_id
        if name is not None:
            self.name = name

    @property
    def inspection_vpc_id(self):
        r"""Gets the inspection_vpc_id of this InspectionVpcInfo.

        **参数解释**： 引流VPC  **取值范围**： 不涉及

        :return: The inspection_vpc_id of this InspectionVpcInfo.
        :rtype: str
        """
        return self._inspection_vpc_id

    @inspection_vpc_id.setter
    def inspection_vpc_id(self, inspection_vpc_id):
        r"""Sets the inspection_vpc_id of this InspectionVpcInfo.

        **参数解释**： 引流VPC  **取值范围**： 不涉及

        :param inspection_vpc_id: The inspection_vpc_id of this InspectionVpcInfo.
        :type inspection_vpc_id: str
        """
        self._inspection_vpc_id = inspection_vpc_id

    @property
    def name(self):
        r"""Gets the name of this InspectionVpcInfo.

        **参数解释**： 引流VPC  **取值范围**： 不涉及

        :return: The name of this InspectionVpcInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this InspectionVpcInfo.

        **参数解释**： 引流VPC  **取值范围**： 不涉及

        :param name: The name of this InspectionVpcInfo.
        :type name: str
        """
        self._name = name

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
        if not isinstance(other, InspectionVpcInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
