# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateManagedAccountRequestBody:

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
        'parent_organizational_unit_name': 'str',
        'blueprint': 'Blueprint'
    }

    attribute_map = {
        'parent_organizational_unit_id': 'parent_organizational_unit_id',
        'parent_organizational_unit_name': 'parent_organizational_unit_name',
        'blueprint': 'blueprint'
    }

    def __init__(self, parent_organizational_unit_id=None, parent_organizational_unit_name=None, blueprint=None):
        r"""UpdateManagedAccountRequestBody

        The model defined in huaweicloud sdk

        :param parent_organizational_unit_id: 父注册OU ID。
        :type parent_organizational_unit_id: str
        :param parent_organizational_unit_name: 父注册OU名称。
        :type parent_organizational_unit_name: str
        :param blueprint: 
        :type blueprint: :class:`huaweicloudsdkrgc.v1.Blueprint`
        """
        
        

        self._parent_organizational_unit_id = None
        self._parent_organizational_unit_name = None
        self._blueprint = None
        self.discriminator = None

        self.parent_organizational_unit_id = parent_organizational_unit_id
        self.parent_organizational_unit_name = parent_organizational_unit_name
        if blueprint is not None:
            self.blueprint = blueprint

    @property
    def parent_organizational_unit_id(self):
        r"""Gets the parent_organizational_unit_id of this UpdateManagedAccountRequestBody.

        父注册OU ID。

        :return: The parent_organizational_unit_id of this UpdateManagedAccountRequestBody.
        :rtype: str
        """
        return self._parent_organizational_unit_id

    @parent_organizational_unit_id.setter
    def parent_organizational_unit_id(self, parent_organizational_unit_id):
        r"""Sets the parent_organizational_unit_id of this UpdateManagedAccountRequestBody.

        父注册OU ID。

        :param parent_organizational_unit_id: The parent_organizational_unit_id of this UpdateManagedAccountRequestBody.
        :type parent_organizational_unit_id: str
        """
        self._parent_organizational_unit_id = parent_organizational_unit_id

    @property
    def parent_organizational_unit_name(self):
        r"""Gets the parent_organizational_unit_name of this UpdateManagedAccountRequestBody.

        父注册OU名称。

        :return: The parent_organizational_unit_name of this UpdateManagedAccountRequestBody.
        :rtype: str
        """
        return self._parent_organizational_unit_name

    @parent_organizational_unit_name.setter
    def parent_organizational_unit_name(self, parent_organizational_unit_name):
        r"""Sets the parent_organizational_unit_name of this UpdateManagedAccountRequestBody.

        父注册OU名称。

        :param parent_organizational_unit_name: The parent_organizational_unit_name of this UpdateManagedAccountRequestBody.
        :type parent_organizational_unit_name: str
        """
        self._parent_organizational_unit_name = parent_organizational_unit_name

    @property
    def blueprint(self):
        r"""Gets the blueprint of this UpdateManagedAccountRequestBody.

        :return: The blueprint of this UpdateManagedAccountRequestBody.
        :rtype: :class:`huaweicloudsdkrgc.v1.Blueprint`
        """
        return self._blueprint

    @blueprint.setter
    def blueprint(self, blueprint):
        r"""Sets the blueprint of this UpdateManagedAccountRequestBody.

        :param blueprint: The blueprint of this UpdateManagedAccountRequestBody.
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
        if not isinstance(other, UpdateManagedAccountRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
