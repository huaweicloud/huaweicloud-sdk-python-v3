# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAvailableAzResponsebodyAvailabilityZone:

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
        'display_name': 'str',
        'locales': 'ShowAvailableAzResponsebodyLocales',
        'type': 'str',
        'region_id': 'str',
        'status': 'str'
    }

    attribute_map = {
        'id': 'id',
        'display_name': 'display_name',
        'locales': 'locales',
        'type': 'type',
        'region_id': 'region_id',
        'status': 'status'
    }

    def __init__(self, id=None, display_name=None, locales=None, type=None, region_id=None, status=None):
        r"""ShowAvailableAzResponsebodyAvailabilityZone

        The model defined in huaweicloud sdk

        :param id: 可用区ID
        :type id: str
        :param display_name: 显示名称
        :type display_name: str
        :param locales: 
        :type locales: :class:`huaweicloudsdkcpcs.v1.ShowAvailableAzResponsebodyLocales`
        :param type: 类型
        :type type: str
        :param region_id: 局点ID
        :type region_id: str
        :param status: 状态
        :type status: str
        """
        
        

        self._id = None
        self._display_name = None
        self._locales = None
        self._type = None
        self._region_id = None
        self._status = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if display_name is not None:
            self.display_name = display_name
        if locales is not None:
            self.locales = locales
        if type is not None:
            self.type = type
        if region_id is not None:
            self.region_id = region_id
        if status is not None:
            self.status = status

    @property
    def id(self):
        r"""Gets the id of this ShowAvailableAzResponsebodyAvailabilityZone.

        可用区ID

        :return: The id of this ShowAvailableAzResponsebodyAvailabilityZone.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowAvailableAzResponsebodyAvailabilityZone.

        可用区ID

        :param id: The id of this ShowAvailableAzResponsebodyAvailabilityZone.
        :type id: str
        """
        self._id = id

    @property
    def display_name(self):
        r"""Gets the display_name of this ShowAvailableAzResponsebodyAvailabilityZone.

        显示名称

        :return: The display_name of this ShowAvailableAzResponsebodyAvailabilityZone.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        r"""Sets the display_name of this ShowAvailableAzResponsebodyAvailabilityZone.

        显示名称

        :param display_name: The display_name of this ShowAvailableAzResponsebodyAvailabilityZone.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def locales(self):
        r"""Gets the locales of this ShowAvailableAzResponsebodyAvailabilityZone.

        :return: The locales of this ShowAvailableAzResponsebodyAvailabilityZone.
        :rtype: :class:`huaweicloudsdkcpcs.v1.ShowAvailableAzResponsebodyLocales`
        """
        return self._locales

    @locales.setter
    def locales(self, locales):
        r"""Sets the locales of this ShowAvailableAzResponsebodyAvailabilityZone.

        :param locales: The locales of this ShowAvailableAzResponsebodyAvailabilityZone.
        :type locales: :class:`huaweicloudsdkcpcs.v1.ShowAvailableAzResponsebodyLocales`
        """
        self._locales = locales

    @property
    def type(self):
        r"""Gets the type of this ShowAvailableAzResponsebodyAvailabilityZone.

        类型

        :return: The type of this ShowAvailableAzResponsebodyAvailabilityZone.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ShowAvailableAzResponsebodyAvailabilityZone.

        类型

        :param type: The type of this ShowAvailableAzResponsebodyAvailabilityZone.
        :type type: str
        """
        self._type = type

    @property
    def region_id(self):
        r"""Gets the region_id of this ShowAvailableAzResponsebodyAvailabilityZone.

        局点ID

        :return: The region_id of this ShowAvailableAzResponsebodyAvailabilityZone.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this ShowAvailableAzResponsebodyAvailabilityZone.

        局点ID

        :param region_id: The region_id of this ShowAvailableAzResponsebodyAvailabilityZone.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def status(self):
        r"""Gets the status of this ShowAvailableAzResponsebodyAvailabilityZone.

        状态

        :return: The status of this ShowAvailableAzResponsebodyAvailabilityZone.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowAvailableAzResponsebodyAvailabilityZone.

        状态

        :param status: The status of this ShowAvailableAzResponsebodyAvailabilityZone.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, ShowAvailableAzResponsebodyAvailabilityZone):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
