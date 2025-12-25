# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DataObjectCreateUpdateResponse:

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
        'event_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'event_id': 'event_id'
    }

    def __init__(self, id=None, event_id=None):
        r"""DataObjectCreateUpdateResponse

        The model defined in huaweicloud sdk

        :param id: 唯一标识ID
        :type id: str
        :param event_id: 唯一事件标识ID
        :type event_id: str
        """
        
        

        self._id = None
        self._event_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if event_id is not None:
            self.event_id = event_id

    @property
    def id(self):
        r"""Gets the id of this DataObjectCreateUpdateResponse.

        唯一标识ID

        :return: The id of this DataObjectCreateUpdateResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this DataObjectCreateUpdateResponse.

        唯一标识ID

        :param id: The id of this DataObjectCreateUpdateResponse.
        :type id: str
        """
        self._id = id

    @property
    def event_id(self):
        r"""Gets the event_id of this DataObjectCreateUpdateResponse.

        唯一事件标识ID

        :return: The event_id of this DataObjectCreateUpdateResponse.
        :rtype: str
        """
        return self._event_id

    @event_id.setter
    def event_id(self, event_id):
        r"""Sets the event_id of this DataObjectCreateUpdateResponse.

        唯一事件标识ID

        :param event_id: The event_id of this DataObjectCreateUpdateResponse.
        :type event_id: str
        """
        self._event_id = event_id

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
        if not isinstance(other, DataObjectCreateUpdateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
