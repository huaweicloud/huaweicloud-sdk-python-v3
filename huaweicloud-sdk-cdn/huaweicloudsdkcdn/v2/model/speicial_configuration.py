# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SpeicialConfiguration:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'create_time': 'int',
        'note': 'str'
    }

    attribute_map = {
        'create_time': 'create_time',
        'note': 'note'
    }

    def __init__(self, create_time=None, note=None):
        r"""SpeicialConfiguration

        The model defined in huaweicloud sdk

        :param create_time: 创建时间
        :type create_time: int
        :param note: 备忘录
        :type note: str
        """
        
        

        self._create_time = None
        self._note = None
        self.discriminator = None

        self.create_time = create_time
        self.note = note

    @property
    def create_time(self):
        r"""Gets the create_time of this SpeicialConfiguration.

        创建时间

        :return: The create_time of this SpeicialConfiguration.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this SpeicialConfiguration.

        创建时间

        :param create_time: The create_time of this SpeicialConfiguration.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def note(self):
        r"""Gets the note of this SpeicialConfiguration.

        备忘录

        :return: The note of this SpeicialConfiguration.
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        r"""Sets the note of this SpeicialConfiguration.

        备忘录

        :param note: The note of this SpeicialConfiguration.
        :type note: str
        """
        self._note = note

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
        if not isinstance(other, SpeicialConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
