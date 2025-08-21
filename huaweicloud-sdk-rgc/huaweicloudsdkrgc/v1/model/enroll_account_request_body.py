# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EnrollAccountRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'parent_organizational_unit_id': 'str',
        'blueprint': 'Blueprint'
    }

    attribute_map = {
        'parent_organizational_unit_id': 'parent_organizational_unit_id',
        'blueprint': 'blueprint'
    }

    def __init__(self, parent_organizational_unit_id=None, blueprint=None):
        r"""EnrollAccountRequestBody

        The model defined in huaweicloud sdk

        :param parent_organizational_unit_id: 父注册OU ID。
        :type parent_organizational_unit_id: str
        :param blueprint: 
        :type blueprint: :class:`huaweicloudsdkrgc.v1.Blueprint`
        """
        
        

        self._parent_organizational_unit_id = None
        self._blueprint = None
        self.discriminator = None

        self.parent_organizational_unit_id = parent_organizational_unit_id
        if blueprint is not None:
            self.blueprint = blueprint

    @property
    def parent_organizational_unit_id(self):
        r"""Gets the parent_organizational_unit_id of this EnrollAccountRequestBody.

        父注册OU ID。

        :return: The parent_organizational_unit_id of this EnrollAccountRequestBody.
        :rtype: str
        """
        return self._parent_organizational_unit_id

    @parent_organizational_unit_id.setter
    def parent_organizational_unit_id(self, parent_organizational_unit_id):
        r"""Sets the parent_organizational_unit_id of this EnrollAccountRequestBody.

        父注册OU ID。

        :param parent_organizational_unit_id: The parent_organizational_unit_id of this EnrollAccountRequestBody.
        :type parent_organizational_unit_id: str
        """
        self._parent_organizational_unit_id = parent_organizational_unit_id

    @property
    def blueprint(self):
        r"""Gets the blueprint of this EnrollAccountRequestBody.

        :return: The blueprint of this EnrollAccountRequestBody.
        :rtype: :class:`huaweicloudsdkrgc.v1.Blueprint`
        """
        return self._blueprint

    @blueprint.setter
    def blueprint(self, blueprint):
        r"""Sets the blueprint of this EnrollAccountRequestBody.

        :param blueprint: The blueprint of this EnrollAccountRequestBody.
        :type blueprint: :class:`huaweicloudsdkrgc.v1.Blueprint`
        """
        self._blueprint = blueprint

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
        if not isinstance(other, EnrollAccountRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
