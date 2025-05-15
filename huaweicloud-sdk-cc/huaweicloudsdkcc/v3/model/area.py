# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Area:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'id': 'str',
        'en_name': 'str',
        'es_name': 'str',
        'pt_name': 'str',
        'station': 'str'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'en_name': 'en_name',
        'es_name': 'es_name',
        'pt_name': 'pt_name',
        'station': 'station'
    }

    def __init__(self, name=None, id=None, en_name=None, es_name=None, pt_name=None, station=None):
        r"""Area

        The model defined in huaweicloud sdk

        :param name: 实例名称。
        :type name: str
        :param id: Area ID。
        :type id: str
        :param en_name: 英文 Area Name。
        :type en_name: str
        :param es_name: 西语 Area Name。
        :type es_name: str
        :param pt_name: 葡语 Area Name。
        :type pt_name: str
        :param station: 站点。
        :type station: str
        """
        
        

        self._name = None
        self._id = None
        self._en_name = None
        self._es_name = None
        self._pt_name = None
        self._station = None
        self.discriminator = None

        self.name = name
        if id is not None:
            self.id = id
        if en_name is not None:
            self.en_name = en_name
        if es_name is not None:
            self.es_name = es_name
        if pt_name is not None:
            self.pt_name = pt_name
        if station is not None:
            self.station = station

    @property
    def name(self):
        r"""Gets the name of this Area.

        实例名称。

        :return: The name of this Area.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this Area.

        实例名称。

        :param name: The name of this Area.
        :type name: str
        """
        self._name = name

    @property
    def id(self):
        r"""Gets the id of this Area.

        Area ID。

        :return: The id of this Area.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this Area.

        Area ID。

        :param id: The id of this Area.
        :type id: str
        """
        self._id = id

    @property
    def en_name(self):
        r"""Gets the en_name of this Area.

        英文 Area Name。

        :return: The en_name of this Area.
        :rtype: str
        """
        return self._en_name

    @en_name.setter
    def en_name(self, en_name):
        r"""Sets the en_name of this Area.

        英文 Area Name。

        :param en_name: The en_name of this Area.
        :type en_name: str
        """
        self._en_name = en_name

    @property
    def es_name(self):
        r"""Gets the es_name of this Area.

        西语 Area Name。

        :return: The es_name of this Area.
        :rtype: str
        """
        return self._es_name

    @es_name.setter
    def es_name(self, es_name):
        r"""Sets the es_name of this Area.

        西语 Area Name。

        :param es_name: The es_name of this Area.
        :type es_name: str
        """
        self._es_name = es_name

    @property
    def pt_name(self):
        r"""Gets the pt_name of this Area.

        葡语 Area Name。

        :return: The pt_name of this Area.
        :rtype: str
        """
        return self._pt_name

    @pt_name.setter
    def pt_name(self, pt_name):
        r"""Sets the pt_name of this Area.

        葡语 Area Name。

        :param pt_name: The pt_name of this Area.
        :type pt_name: str
        """
        self._pt_name = pt_name

    @property
    def station(self):
        r"""Gets the station of this Area.

        站点。

        :return: The station of this Area.
        :rtype: str
        """
        return self._station

    @station.setter
    def station(self, station):
        r"""Sets the station of this Area.

        站点。

        :param station: The station of this Area.
        :type station: str
        """
        self._station = station

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
        if not isinstance(other, Area):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
