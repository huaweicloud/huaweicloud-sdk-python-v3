# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CapacityReservationSpecification:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'preference': 'str'
    }

    attribute_map = {
        'id': 'id',
        'preference': 'preference'
    }

    def __init__(self, id=None, preference=None):
        r"""CapacityReservationSpecification

        The model defined in huaweicloud sdk

        :param id: 私有池id，preference为none时忽略该值
        :type id: str
        :param preference: 私有池容量选项，为 none 时表示不指定容量预留，为 targeted 时表示指定容量预留，此时 id 不能为空
        :type preference: str
        """
        
        

        self._id = None
        self._preference = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if preference is not None:
            self.preference = preference

    @property
    def id(self):
        r"""Gets the id of this CapacityReservationSpecification.

        私有池id，preference为none时忽略该值

        :return: The id of this CapacityReservationSpecification.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CapacityReservationSpecification.

        私有池id，preference为none时忽略该值

        :param id: The id of this CapacityReservationSpecification.
        :type id: str
        """
        self._id = id

    @property
    def preference(self):
        r"""Gets the preference of this CapacityReservationSpecification.

        私有池容量选项，为 none 时表示不指定容量预留，为 targeted 时表示指定容量预留，此时 id 不能为空

        :return: The preference of this CapacityReservationSpecification.
        :rtype: str
        """
        return self._preference

    @preference.setter
    def preference(self, preference):
        r"""Sets the preference of this CapacityReservationSpecification.

        私有池容量选项，为 none 时表示不指定容量预留，为 targeted 时表示指定容量预留，此时 id 不能为空

        :param preference: The preference of this CapacityReservationSpecification.
        :type preference: str
        """
        self._preference = preference

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
        if not isinstance(other, CapacityReservationSpecification):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
