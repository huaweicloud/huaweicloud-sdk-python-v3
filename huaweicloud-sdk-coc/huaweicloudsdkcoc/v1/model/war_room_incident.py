# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WarRoomIncident:

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
        'incident_id': 'str',
        'is_change_event': 'bool',
        'failure_level': 'str',
        'incident_url': 'str'
    }

    attribute_map = {
        'id': 'id',
        'incident_id': 'incident_id',
        'is_change_event': 'is_change_event',
        'failure_level': 'failure_level',
        'incident_url': 'incident_url'
    }

    def __init__(self, id=None, incident_id=None, is_change_event=None, failure_level=None, incident_url=None):
        r"""WarRoomIncident

        The model defined in huaweicloud sdk

        :param id: 主键
        :type id: str
        :param incident_id: 事件id
        :type incident_id: str
        :param is_change_event: 是否变更事件
        :type is_change_event: bool
        :param failure_level: 事件级别
        :type failure_level: str
        :param incident_url: 事件单号链接
        :type incident_url: str
        """
        
        

        self._id = None
        self._incident_id = None
        self._is_change_event = None
        self._failure_level = None
        self._incident_url = None
        self.discriminator = None

        self.id = id
        if incident_id is not None:
            self.incident_id = incident_id
        if is_change_event is not None:
            self.is_change_event = is_change_event
        if failure_level is not None:
            self.failure_level = failure_level
        if incident_url is not None:
            self.incident_url = incident_url

    @property
    def id(self):
        r"""Gets the id of this WarRoomIncident.

        主键

        :return: The id of this WarRoomIncident.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this WarRoomIncident.

        主键

        :param id: The id of this WarRoomIncident.
        :type id: str
        """
        self._id = id

    @property
    def incident_id(self):
        r"""Gets the incident_id of this WarRoomIncident.

        事件id

        :return: The incident_id of this WarRoomIncident.
        :rtype: str
        """
        return self._incident_id

    @incident_id.setter
    def incident_id(self, incident_id):
        r"""Sets the incident_id of this WarRoomIncident.

        事件id

        :param incident_id: The incident_id of this WarRoomIncident.
        :type incident_id: str
        """
        self._incident_id = incident_id

    @property
    def is_change_event(self):
        r"""Gets the is_change_event of this WarRoomIncident.

        是否变更事件

        :return: The is_change_event of this WarRoomIncident.
        :rtype: bool
        """
        return self._is_change_event

    @is_change_event.setter
    def is_change_event(self, is_change_event):
        r"""Sets the is_change_event of this WarRoomIncident.

        是否变更事件

        :param is_change_event: The is_change_event of this WarRoomIncident.
        :type is_change_event: bool
        """
        self._is_change_event = is_change_event

    @property
    def failure_level(self):
        r"""Gets the failure_level of this WarRoomIncident.

        事件级别

        :return: The failure_level of this WarRoomIncident.
        :rtype: str
        """
        return self._failure_level

    @failure_level.setter
    def failure_level(self, failure_level):
        r"""Sets the failure_level of this WarRoomIncident.

        事件级别

        :param failure_level: The failure_level of this WarRoomIncident.
        :type failure_level: str
        """
        self._failure_level = failure_level

    @property
    def incident_url(self):
        r"""Gets the incident_url of this WarRoomIncident.

        事件单号链接

        :return: The incident_url of this WarRoomIncident.
        :rtype: str
        """
        return self._incident_url

    @incident_url.setter
    def incident_url(self, incident_url):
        r"""Sets the incident_url of this WarRoomIncident.

        事件单号链接

        :param incident_url: The incident_url of this WarRoomIncident.
        :type incident_url: str
        """
        self._incident_url = incident_url

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
        if not isinstance(other, WarRoomIncident):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
