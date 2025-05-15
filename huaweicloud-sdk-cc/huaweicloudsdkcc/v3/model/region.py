# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Region:

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
        'area_id': 'AreaIdDef',
        'id': 'str',
        'area_name': 'str',
        'used_scenes': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'area_id': 'area_id',
        'id': 'id',
        'area_name': 'area_name',
        'used_scenes': 'used_scenes'
    }

    def __init__(self, name=None, area_id=None, id=None, area_name=None, used_scenes=None):
        r"""Region

        The model defined in huaweicloud sdk

        :param name: 实例名称。
        :type name: str
        :param area_id: 
        :type area_id: :class:`huaweicloudsdkcc.v3.AreaIdDef`
        :param id: Region ID。
        :type id: str
        :param area_name: 大区名。
        :type area_name: str
        :param used_scenes: 云连接使用场景 er vpc vgw。
        :type used_scenes: list[str]
        """
        
        

        self._name = None
        self._area_id = None
        self._id = None
        self._area_name = None
        self._used_scenes = None
        self.discriminator = None

        self.name = name
        self.area_id = area_id
        if id is not None:
            self.id = id
        if area_name is not None:
            self.area_name = area_name
        if used_scenes is not None:
            self.used_scenes = used_scenes

    @property
    def name(self):
        r"""Gets the name of this Region.

        实例名称。

        :return: The name of this Region.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this Region.

        实例名称。

        :param name: The name of this Region.
        :type name: str
        """
        self._name = name

    @property
    def area_id(self):
        r"""Gets the area_id of this Region.

        :return: The area_id of this Region.
        :rtype: :class:`huaweicloudsdkcc.v3.AreaIdDef`
        """
        return self._area_id

    @area_id.setter
    def area_id(self, area_id):
        r"""Sets the area_id of this Region.

        :param area_id: The area_id of this Region.
        :type area_id: :class:`huaweicloudsdkcc.v3.AreaIdDef`
        """
        self._area_id = area_id

    @property
    def id(self):
        r"""Gets the id of this Region.

        Region ID。

        :return: The id of this Region.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this Region.

        Region ID。

        :param id: The id of this Region.
        :type id: str
        """
        self._id = id

    @property
    def area_name(self):
        r"""Gets the area_name of this Region.

        大区名。

        :return: The area_name of this Region.
        :rtype: str
        """
        return self._area_name

    @area_name.setter
    def area_name(self, area_name):
        r"""Sets the area_name of this Region.

        大区名。

        :param area_name: The area_name of this Region.
        :type area_name: str
        """
        self._area_name = area_name

    @property
    def used_scenes(self):
        r"""Gets the used_scenes of this Region.

        云连接使用场景 er vpc vgw。

        :return: The used_scenes of this Region.
        :rtype: list[str]
        """
        return self._used_scenes

    @used_scenes.setter
    def used_scenes(self, used_scenes):
        r"""Sets the used_scenes of this Region.

        云连接使用场景 er vpc vgw。

        :param used_scenes: The used_scenes of this Region.
        :type used_scenes: list[str]
        """
        self._used_scenes = used_scenes

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
        if not isinstance(other, Region):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
